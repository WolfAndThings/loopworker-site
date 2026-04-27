import { chromium } from 'playwright';
import { mkdirSync, existsSync, writeFileSync } from 'fs';
import { join, resolve } from 'path';
import https from 'https';
import http from 'http';

const CHROME_PROFILE = '/Users/alexlamb/Library/Caches/ms-playwright/mcp-chrome-manual';
const OUTPUT_DIR = resolve('images/case_studies/references');

const ACCOUNTS = [
  { name: 'myburger', handle: 'myburgerusa', count: 12 },
  { name: 'marina', handle: 'marina.medspa', count: 12 },
  { name: 'bouldering', handle: 'minneapolisboulderingproject', count: 12 },
];

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

async function downloadFile(url, dest) {
  const res = await fetch(url, { headers: { 'User-Agent': 'Mozilla/5.0' } });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const buf = Buffer.from(await res.arrayBuffer());
  writeFileSync(dest, buf);
}

async function main() {
  console.log('\n=== Instagram Reference Image Scraper ===\n');

  const browser = await chromium.launchPersistentContext(CHROME_PROFILE, {
    headless: false,
    channel: 'chrome',
    viewport: { width: 1280, height: 900 },
    args: ['--disable-blink-features=AutomationControlled'],
  });

  const page = browser.pages()[0] || await browser.newPage();

  for (const account of ACCOUNTS) {
    const outDir = join(OUTPUT_DIR, account.name);
    mkdirSync(outDir, { recursive: true });

    console.log(`--- @${account.handle} (${account.count} images) ---`);

    await page.goto(`https://www.instagram.com/${account.handle}/`, {
      waitUntil: 'domcontentloaded',
      timeout: 60000,
    });
    await sleep(5000);

    // Scroll down to load more posts
    for (let s = 0; s < 3; s++) {
      await page.evaluate(() => window.scrollBy(0, 1000));
      await sleep(2000);
    }

    // Grab all post images from the grid
    const imgSrcs = await page.evaluate(() => {
      const imgs = document.querySelectorAll('article img, main img[src*="instagram"], img[src*="cdninstagram"], img[src*="scontent"]');
      const srcs = [];
      for (const img of imgs) {
        const src = img.src;
        if (src && src.includes('scontent') && !src.includes('150x150') && !srcs.includes(src)) {
          srcs.push(src);
        }
      }
      return srcs;
    });

    console.log(`  Found ${imgSrcs.length} images`);

    const toDownload = imgSrcs.slice(0, account.count);
    let downloaded = 0;

    for (let i = 0; i < toDownload.length; i++) {
      const dest = join(outDir, `${String(i + 1).padStart(2, '0')}.jpg`);
      if (existsSync(dest)) {
        console.log(`  ${i + 1}/${toDownload.length} — exists, skipping`);
        downloaded++;
        continue;
      }
      try {
        await downloadFile(toDownload[i], dest);
        console.log(`  ${i + 1}/${toDownload.length} — saved`);
        downloaded++;
      } catch (e) {
        console.log(`  ${i + 1}/${toDownload.length} — failed: ${e.message}`);
      }
    }

    console.log(`  Done: ${downloaded}/${toDownload.length}\n`);
    await sleep(3000);
  }

  console.log('=== All done ===');
  console.log(`References at: ${OUTPUT_DIR}`);
  await browser.close();
}

main().catch(console.error);
