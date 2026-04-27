import { chromium } from 'playwright';
import { mkdirSync, writeFileSync } from 'fs';
import { resolve, join } from 'path';

const CHROME_PROFILE = '/Users/alexlamb/Library/Caches/ms-playwright/mcp-chrome-manual';
const OUTPUT_DIR = resolve('competitor_data');

const ACCOUNTS = [
  // Restaurants
  'frankprisinzano', 'eggslut', 'badroman.nyc', 'fatherandfish', 'tartinebakery',
  // Med Spas
  'beautyboostmedspa', 'sanctuarymedicalcenter', 'tribecamedspa', 'skinlaundry', 'bestyoumedspa',
  // Gyms
  'solidcore', 'rumble_boxing', 'therebelworkout', 'crossfit_nyc',
  // Salons
  'staygold31', 'edwardsandco', 'blindbarber',
  // Coffee
  'intelligentsiacoffee', 'daaborecoffee', 'birchcoffee', 'boldbeancoffee',
  // Real Estate / Hotels
  'jasoncassity', 'hawaiilife', 'zerogeorge',
];

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

async function scrapeAccount(page, handle) {
  console.log(`  @${handle}...`);

  await page.goto(`https://www.instagram.com/${handle}/`, {
    waitUntil: 'domcontentloaded',
    timeout: 30000,
  });
  await sleep(4000);

  const data = await page.evaluate(() => {
    // Get follower count, post count, following from meta or page text
    const metaDesc = document.querySelector('meta[name="description"]')?.content || '';
    const pageText = document.body.innerText;

    // Try to parse followers from meta description
    // Format: "X Followers, Y Following, Z Posts - ..."
    const metaMatch = metaDesc.match(/([\d,.]+[KMkm]?)\s*Followers/i);
    const postMatch = metaDesc.match(/([\d,.]+)\s*Posts/i);
    const followingMatch = metaDesc.match(/([\d,.]+)\s*Following/i);

    // Also try header stats
    const statEls = document.querySelectorAll('header li, header span[title], [class*="count"]');
    let followers = metaMatch ? metaMatch[1] : '';
    let posts = postMatch ? postMatch[1] : '';
    let following = followingMatch ? followingMatch[1] : '';

    // Get bio
    const bioEl = document.querySelector('header section > div > span, [class*="biography"], meta[property="og:description"]');
    const bio = bioEl?.textContent || document.querySelector('meta[property="og:description"]')?.content || '';

    // Get profile name
    const nameEl = document.querySelector('header h2, header h1, [class*="header"] h1');
    const name = nameEl?.textContent || '';

    // Scrape visible posts - get images and any visible engagement
    const postEls = document.querySelectorAll('article a[href*="/p/"], article a[href*="/reel/"], main a[href*="/p/"], main a[href*="/reel/"]');
    const postLinks = [];
    for (const el of postEls) {
      const href = el.getAttribute('href');
      const img = el.querySelector('img');
      const imgSrc = img?.src || '';
      const alt = img?.alt || '';

      // Try to get likes/views from overlay
      const overlay = el.querySelector('[class*="overlay"], [class*="Overlay"]');
      const overlayText = overlay?.textContent || '';

      postLinks.push({
        url: href,
        imgSrc,
        alt,
        overlayText,
      });
    }

    return {
      name,
      followers,
      posts,
      following,
      bio,
      postCount: postLinks.length,
      topPosts: postLinks.slice(0, 12),
    };
  });

  // Now scrape the first 3 individual posts for engagement data
  const postDetails = [];
  const postsToScrape = data.topPosts.slice(0, 6);

  for (const post of postsToScrape) {
    if (!post.url) continue;
    try {
      const fullUrl = post.url.startsWith('http') ? post.url : `https://www.instagram.com${post.url}`;
      await page.goto(fullUrl, { waitUntil: 'domcontentloaded', timeout: 15000 });
      await sleep(2000);

      const detail = await page.evaluate(() => {
        const text = document.body.innerText;
        const metaDesc = document.querySelector('meta[name="description"]')?.content || '';

        // Try to get likes from meta: "X likes, Y comments - ..."
        const likesMatch = metaDesc.match(/([\d,.]+[KMkm]?)\s*likes/i);
        const commentsMatch = metaDesc.match(/([\d,.]+[KMkm]?)\s*comments/i);
        const viewsMatch = metaDesc.match(/([\d,.]+[KMkm]?)\s*(?:views|plays)/i);

        // Get caption
        const captionEl = document.querySelector('[class*="caption"] span, article span[dir="auto"]');
        const caption = captionEl?.textContent?.slice(0, 200) || '';

        // Get date
        const timeEl = document.querySelector('time');
        const date = timeEl?.getAttribute('datetime') || timeEl?.textContent || '';

        return {
          likes: likesMatch ? likesMatch[1] : '',
          comments: commentsMatch ? commentsMatch[1] : '',
          views: viewsMatch ? viewsMatch[1] : '',
          caption: caption.slice(0, 150),
          date,
        };
      });

      postDetails.push({ ...post, ...detail });
    } catch (e) {
      postDetails.push({ ...post, error: e.message });
    }
  }

  return {
    handle,
    ...data,
    scrapedPosts: postDetails,
  };
}

async function main() {
  mkdirSync(OUTPUT_DIR, { recursive: true });

  console.log(`\n=== Competitor Scraper — ${ACCOUNTS.length} accounts ===\n`);

  const browser = await chromium.launchPersistentContext(CHROME_PROFILE, {
    headless: false,
    channel: 'chrome',
    viewport: { width: 1280, height: 900 },
    args: ['--disable-blink-features=AutomationControlled'],
  });

  const page = browser.pages()[0] || await browser.newPage();
  const results = [];

  for (let i = 0; i < ACCOUNTS.length; i++) {
    const handle = ACCOUNTS[i];
    console.log(`[${i + 1}/${ACCOUNTS.length}] @${handle}`);

    try {
      const data = await scrapeAccount(page, handle);
      results.push(data);
      console.log(`    ${data.followers} followers, ${data.postCount} posts visible, ${data.scrapedPosts.length} scraped`);

      // Save incrementally
      writeFileSync(
        join(OUTPUT_DIR, 'competitors.json'),
        JSON.stringify(results, null, 2)
      );
    } catch (e) {
      console.log(`    ERROR: ${e.message}`);
      results.push({ handle, error: e.message });
    }

    // Rate limit — don't hammer Instagram
    if (i < ACCOUNTS.length - 1) {
      const delay = 5000 + Math.random() * 5000;
      await sleep(delay);
    }
  }

  // Save final results
  writeFileSync(
    join(OUTPUT_DIR, 'competitors.json'),
    JSON.stringify(results, null, 2)
  );

  console.log(`\n=== Done: ${results.length}/${ACCOUNTS.length} accounts ===`);
  console.log(`Data saved to: ${OUTPUT_DIR}/competitors.json`);

  await browser.close();
}

main().catch(console.error);
