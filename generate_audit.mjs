#!/usr/bin/env node
/**
 * LoopWorker Audit Generator
 *
 * Takes form data, scrapes their Instagram, generates a full audit HTML.
 *
 * Usage:
 *   node generate_audit.mjs --name "John" --business "Primo Tacos" --handle "primotacos.mpls" --type "restaurant" --challenge "not getting customers from social"
 *   node generate_audit.mjs --handle "myburgerusa" --type "restaurant"
 *   node generate_audit.mjs --config audit_intake.json
 */

import { chromium } from 'playwright';
import { writeFileSync, readFileSync, existsSync, mkdirSync } from 'fs';
import { resolve, join } from 'path';

const CHROME_PROFILE = '/Users/alexlamb/Library/Caches/ms-playwright/mcp-chrome-manual';

// ============================================================
// INDUSTRY PRESETS — pre-loaded from playbook
// ============================================================
const INDUSTRY = {
  restaurant: {
    benchmark_er: '3-5%',
    pillar_quality: {
      title: 'Visual Quality',
      opportunity: 'Your food already looks great in person. With better lighting and tighter framing, your photos can make people feel hungry just from scrolling. That\'s when content drives walk-ins.',
      fixes: [
        'Warm, directional lighting that brings out texture and depth',
        'Tight crops that show the cheese pull, the sear marks, the steam',
        'Clean backgrounds — the food becomes the hero',
        'Every image looks intentional and scroll-stopping',
      ],
    },
    pillar_consistency: {
      title: 'Feed Consistency',
      opportunity: 'Imagine someone landing on your profile and instantly knowing exactly what you\'re about. A consistent visual identity makes your brand feel established, trustworthy, and worth visiting.',
      fixes: [
        'Locked brand palette that matches your space and packaging',
        'Same lighting style across every post — instant recognition',
        'Campaign sets — 6 images that feel like one cohesive brand',
        'Your grid becomes a destination, not a random collection',
      ],
    },
    pillar_engagement: {
      title: 'Engagement & Conversion',
      opportunity: 'You\'re already posting consistently — that\'s the hard part. Now it\'s about making each post work harder. The right hooks and CTAs can turn your existing audience into actual customers walking through the door.',
      fixes: [
        'Every caption starts with a hook — "This sold out by 7pm last night"',
        'Urgency built into every post — people feel like they need to act',
        'Clear CTA on every post — "Come in before it\'s gone" / "Tag someone"',
        'Content designed for saves and shares — the algorithm rewards this',
      ],
    },
    post_ideas: [
      { hook: '"This sold out by 7pm last night."', desc: 'Film the last portion. Show the empty tray. Urgency that makes people come early.', format: 'Reel — 15 sec' },
      { hook: '"What 6 AM prep looks like"', desc: 'Timelapse of morning setup. The work behind the food.', format: 'Reel — 30 sec' },
      { hook: '"The thing nobody orders but should."', desc: 'Close-up of the most underrated item. Curiosity drives visits.', format: 'Reel — 10 sec' },
      { hook: '"Friday night, 8 PM."', desc: 'Wide shot of the restaurant full. Social proof — no caption needed beyond the time.', format: 'Static photo' },
      { hook: '"We almost took this off the menu."', desc: 'The story of a menu item that almost got cut. Nostalgia + urgency.', format: 'Reel — 20 sec' },
    ],
    caption_before: [
      { before: 'Come try our new special! Available now.', after: 'We made 40 of these this morning. They were gone before lunch. Making 60 tomorrow.' },
      { before: 'Happy Tuesday!', after: 'The thing nobody orders but should. Trust me on this one.' },
    ],
  },
  medspa: {
    benchmark_er: '2-4%',
    pillar_quality: {
      title: 'Visual Quality',
      opportunity: 'Your space is premium — your content should match. With the right lighting and composition, your social media can feel as elevated as your actual experience.',
      fixes: [
        'Bright, clean natural light — clinical but warm',
        'Real skin texture in portraits — healthy, not filtered',
        'Treatment close-ups that are satisfying to watch',
        'Space photography that shows the environment people are walking into',
      ],
    },
    pillar_consistency: {
      title: 'Feed Consistency',
      opportunity: 'The best med spas have a visual identity you recognize instantly. A consistent palette and style makes you look like the expert — not just another clinic.',
      fixes: [
        'Locked palette that matches your brand colors across every post',
        'Consistent lighting and composition — every image feels connected',
        'Before/after content with the same framing every time',
        'Your grid looks like a brand, not a brochure',
      ],
    },
    pillar_engagement: {
      title: 'Engagement & Conversion',
      opportunity: 'You have the expertise — now it\'s about showing it. Educational hooks build trust faster than "Book now" ever will. When people trust you, they DM you.',
      fixes: [
        'Educational hooks — "Most clients wait too long before starting..."',
        'Authority-building captions that position you as the expert',
        '"DM us" CTAs instead of generic "Book now"',
        'Content that answers real questions people are already asking',
      ],
    },
    post_ideas: [
      { hook: '"Most clients wait too long before starting this."', desc: 'Educational hook about timing. Builds authority and drives DMs.', format: 'Reel — 20 sec' },
      { hook: '"What this treatment actually looks like."', desc: 'Real procedure, no filter. Satisfying and trust-building.', format: 'Reel — 30 sec' },
      { hook: '"The question I get asked most."', desc: 'Answer the #1 thing people DM about. Positions you as the expert.', format: 'Reel — 15 sec' },
      { hook: '"6 weeks later."', desc: 'Before/after with specific timeline. Real results, real trust.', format: 'Carousel — 2 slides' },
      { hook: '"The treatment nobody talks about but should."', desc: 'Spotlight an underrated service. Curiosity drives consultations.', format: 'Reel — 15 sec' },
    ],
    caption_before: [
      { before: 'Botox appointments available. Book now!', after: 'Most clients wait too long before starting Botox. The best results come from starting earlier and maintaining consistency.' },
      { before: 'Check out our services!', after: 'The question I get asked most: "Is it too early to start?" Here\'s what I tell every client.' },
    ],
  },
  gym: {
    benchmark_er: '1-3%',
    pillar_quality: {
      title: 'Visual Quality',
      opportunity: 'Your space has energy that photos can\'t capture yet. With the right angles and lighting, your content can make people feel the atmosphere before they ever walk in.',
      fixes: [
        'Natural light and movement — capture the energy of a real session',
        'People mid-action, not posed — authenticity beats polish',
        'Wide shots that show community, not just equipment',
        'Close-ups of effort — chalk, sweat, focus',
      ],
    },
    pillar_consistency: {
      title: 'Feed Consistency',
      opportunity: 'The best gym accounts have a look that\'s instantly recognizable. Your brand should feel as strong online as the experience feels in person.',
      fixes: [
        'Consistent color palette that matches your space',
        'Same shooting style across all content — documentary, real',
        'Member spotlights with a consistent format',
        'Your grid tells the story of a community, not a facility',
      ],
    },
    pillar_engagement: {
      title: 'Engagement & Conversion',
      opportunity: 'You\'re already building a community in person. Now it\'s about bringing that energy online. Content that makes people feel welcome converts better than content that shows equipment.',
      fixes: [
        'Hooks that speak to beginners — "What your first day actually looks like"',
        'Community stories, not just class schedules',
        '"Try it this week" CTAs that lower the barrier',
        'Content that makes your space feel accessible, not intimidating',
      ],
    },
    post_ideas: [
      { hook: '"If you\'ve been saying I\'ll start next week..."', desc: 'Motivational hook that meets people where they are. Drives trial sign-ups.', format: 'Reel — 15 sec' },
      { hook: '"What your first day actually looks like."', desc: 'Walk through the experience. Remove intimidation. Drive first visits.', format: 'Reel — 30 sec' },
      { hook: '"The class that scares people the most."', desc: 'Show it\'s not as scary as they think. Makes people curious enough to try.', format: 'Reel — 20 sec' },
      { hook: '"Why [member name] keeps coming back."', desc: 'Real member story. Community content that builds trust.', format: 'Reel — 20 sec' },
      { hook: '"Saturday morning energy."', desc: 'Film the room mid-class. Music, movement, community. Pure vibe.', format: 'Reel — 15 sec' },
    ],
    caption_before: [
      { before: 'New class schedule is out!', after: 'If you\'ve been saying "I\'ll start next week"... this is your sign to stop waiting.' },
      { before: 'Come check us out!', after: 'What your first day actually looks like (it\'s not as scary as you think).' },
    ],
  },
  salon: {
    benchmark_er: '2-5%',
    pillar_quality: {
      title: 'Visual Quality',
      opportunity: 'Your work is the content. With consistent lighting and the right angles, every cut, color, or style becomes a scroll-stopping portfolio piece.',
      fixes: [
        'Same chair, same angle, same lighting — builds a recognizable portfolio',
        'Before/after with identical framing every time',
        'Slow-motion reveals of the finished result',
        'Close-ups that show the detail and craft',
      ],
    },
    pillar_consistency: {
      title: 'Feed Consistency',
      opportunity: 'Your grid is your portfolio. When every image has the same look and feel, people trust your work before they ever sit in your chair.',
      fixes: [
        'Consistent background and lighting setup',
        'Same composition style — your signature look',
        'Color-accurate photos that show real results',
        'A feed that looks like a curated portfolio, not a phone camera roll',
      ],
    },
    pillar_engagement: {
      title: 'Engagement & Conversion',
      opportunity: 'Transformation content is the most engaging format on Instagram. You create transformations every day — now it\'s about capturing and sharing them in a way that drives bookings.',
      fixes: [
        'Before/after Reels with satisfying reveals',
        '"The most requested style right now" — trend hooks',
        'DM-to-book CTAs on every transformation post',
        'Process content — people love watching the work happen',
      ],
    },
    post_ideas: [
      { hook: '"The transformation that made me stop mid-cut."', desc: 'Before/after with a story. The best ones have personality.', format: 'Reel — 15 sec' },
      { hook: '"The most requested style this month."', desc: 'Trend content with your work. Drives saves and bookings.', format: 'Reel — 10 sec' },
      { hook: '"Before vs. after — pay attention to the layers."', desc: 'Educational transformation. Shows your expertise.', format: 'Carousel — 2 slides' },
      { hook: '"Satisfying fade in 60 seconds."', desc: 'Process content. Slow-mo finish. People can\'t stop watching.', format: 'Reel — 60 sec' },
      { hook: '"What I\'d recommend for this face shape."', desc: 'Expert advice on camera. Builds trust and authority.', format: 'Reel — 20 sec' },
    ],
    caption_before: [
      { before: 'Love this new look!', after: 'The transformation that made me stop mid-cut. Swipe to see the before.' },
      { before: 'Book your appointment today!', after: 'This is the most requested style this month. DM "layers" to book yours.' },
    ],
  },
  coffee: {
    benchmark_er: '2-4%',
    pillar_quality: {
      title: 'Visual Quality',
      opportunity: 'Coffee is one of the most photogenic products there is. With warm lighting and consistent styling, your feed can become the reason people choose you over the shop down the street.',
      fixes: [
        'Warm, natural-light photography — cozy and inviting',
        'Latte art pours and espresso pulls in slow motion',
        'Consistent backgrounds that become your signature',
        'The space photographed like it belongs in a magazine',
      ],
    },
    pillar_consistency: {
      title: 'Feed Consistency',
      opportunity: 'The best coffee accounts have a visual warmth you can feel through the screen. That consistency is what makes someone follow — and then visit.',
      fixes: [
        'Locked warm palette — the colors should feel like your shop',
        'Same angles and surfaces across posts',
        'A feed that looks cozy and intentional, not random',
        'Seasonal content with consistent brand styling',
      ],
    },
    pillar_engagement: {
      title: 'Engagement & Conversion',
      opportunity: 'People don\'t just follow coffee shops for coffee — they follow for the feeling. Content that captures the atmosphere and the people drives more engagement than product shots alone.',
      fixes: [
        'Neighborhood content — "What 7am looks like on our block"',
        '"The drink nobody knows about" — secret menu energy',
        'Barista personality content — people connect with people',
        'Morning ritual content that makes people want to start their day here',
      ],
    },
    post_ideas: [
      { hook: '"The drink nobody knows about."', desc: 'Secret menu energy. Curiosity drives visits.', format: 'Reel — 10 sec' },
      { hook: '"What 7 AM looks like here."', desc: 'Morning open-up ritual. Cozy, warm, real.', format: 'Reel — 20 sec' },
      { hook: '"We tested 4 new drinks. This one won."', desc: 'Taste test content. Engagement + product launch.', format: 'Reel — 15 sec' },
      { hook: '"Our barista\'s personal favorite."', desc: 'Staff pick content. Personality-driven.', format: 'Reel — 10 sec' },
      { hook: '"Rainy day essentials."', desc: 'Seasonal/weather content. Cozy vibes that drive walk-ins.', format: 'Static photo' },
    ],
    caption_before: [
      { before: 'Come try our new latte!', after: 'The drink nobody knows about. Ask for it by name.' },
      { before: 'Happy Monday!', after: 'What 7 AM looks like here. Come start your week right.' },
    ],
  },
  realestate: {
    benchmark_er: '1-3%',
    pillar_quality: {
      title: 'Visual Quality',
      opportunity: 'Properties sell on emotion, not specs. With cinematic photography and golden-hour timing, your listings can make people feel something before they ever schedule a showing.',
      fixes: [
        'Golden hour exterior shots with warm interior glow',
        'Wide-angle walkthrough Reels with music',
        'Detail shots — the fixtures, the finishes, the light',
        'Lifestyle content that sells the feeling of living there',
      ],
    },
    pillar_consistency: {
      title: 'Feed Consistency',
      opportunity: 'The best agents are known for their area, not just their listings. A consistent visual style makes you the go-to expert people trust.',
      fixes: [
        'Consistent shooting style across all properties',
        'Neighborhood content with your signature look',
        'A grid that says "I know this area" not just "I sell houses"',
        'Local expertise content with consistent branding',
      ],
    },
    pillar_engagement: {
      title: 'Engagement & Conversion',
      opportunity: 'Listing walkthroughs get views but neighborhood guides get followers. The agents with the biggest audiences are the ones who teach you about the area — not just show you houses.',
      fixes: [
        '"3 things about [neighborhood] most people don\'t know"',
        '"What $X gets you in [area]" — price context content',
        'Local restaurant/business spotlights — become the neighborhood expert',
        'Market updates delivered with personality, not stats',
      ],
    },
    post_ideas: [
      { hook: '"3 things about this neighborhood most people don\'t know."', desc: 'Local expert content. Gets saved and shared.', format: 'Carousel — 4 slides' },
      { hook: '"What $500K gets you here."', desc: 'Price context. People can\'t resist comparing.', format: 'Reel — 20 sec' },
      { hook: '"Their first morning in the new place."', desc: 'Buyer experience content. Emotional and shareable.', format: 'Reel — 15 sec' },
      { hook: '"The view I can\'t stop thinking about."', desc: 'Golden hour hero shot. Architecture as content.', format: 'Static photo' },
      { hook: '"My 5 favorite restaurants in [area]."', desc: 'Neighborhood guide. Positions you as the local expert.', format: 'Carousel — 6 slides' },
    ],
    caption_before: [
      { before: 'Just listed! 3 bed, 2 bath. Link in bio.', after: '3 things about this neighborhood most people don\'t know. (Swipe — #3 is why people never leave.)' },
      { before: 'Open house this weekend!', after: 'What $450K actually gets you in Uptown right now. The kitchen alone is worth the visit.' },
    ],
  },
};

// ============================================================
// INSTAGRAM SCRAPER
// ============================================================
async function scrapeInstagram(handle) {
  console.log(`Scraping @${handle}...`);

  let browser;
  try {
    browser = await chromium.launchPersistentContext(CHROME_PROFILE, {
      headless: false,
      channel: 'chrome',
      viewport: { width: 1280, height: 900 },
      args: ['--disable-blink-features=AutomationControlled'],
    });
  } catch {
    console.log('  Chrome profile in use — trying headless Chromium...');
    browser = await chromium.launch({ headless: true });
  }

  const page = browser.pages?.()[0] || await browser.newPage();

  await page.goto(`https://www.instagram.com/${handle}/`, {
    waitUntil: 'domcontentloaded',
    timeout: 30000,
  });
  await new Promise(r => setTimeout(r, 5000));

  const data = await page.evaluate(() => {
    const meta = document.querySelector('meta[name="description"]')?.content || '';
    const followersMatch = meta.match(/([\d,.]+[KMkm]?)\s*Followers/i);
    const postsMatch = meta.match(/([\d,.]+)\s*Posts/i);
    return {
      followers: followersMatch ? followersMatch[1] : '?',
      posts: postsMatch ? postsMatch[1] : '?',
      bio: meta,
    };
  });

  // Scrape first 6 posts for engagement
  const postLinks = await page.evaluate(() => {
    const links = document.querySelectorAll('a[href*="/p/"], a[href*="/reel/"]');
    return [...links].slice(0, 6).map(a => a.getAttribute('href'));
  });

  const scrapedPosts = [];
  for (const link of postLinks) {
    try {
      const url = link.startsWith('http') ? link : `https://www.instagram.com${link}`;
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 15000 });
      await new Promise(r => setTimeout(r, 2000));

      const post = await page.evaluate(() => {
        const meta = document.querySelector('meta[name="description"]')?.content || '';
        const likes = meta.match(/([\d,.]+[KMkm]?)\s*likes/i);
        const comments = meta.match(/([\d,.]+[KMkm]?)\s*comments/i);
        const time = document.querySelector('time');
        return {
          likes: likes ? likes[1] : '0',
          comments: comments ? comments[1] : '0',
          date: time?.getAttribute('datetime')?.slice(0, 10) || '',
        };
      });
      scrapedPosts.push(post);
    } catch { }
  }

  await browser.close();

  // Calculate engagement rate
  let followers = data.followers.replace(/,/g, '');
  if (followers.includes('K')) followers = parseFloat(followers) * 1000;
  else if (followers.includes('M')) followers = parseFloat(followers) * 1000000;
  else followers = parseInt(followers) || 0;

  let totalLikes = 0;
  let count = 0;
  for (const p of scrapedPosts) {
    let l = p.likes.replace(/,/g, '');
    if (l.includes('K')) l = parseFloat(l) * 1000;
    else l = parseInt(l) || 0;
    totalLikes += l;
    count++;
  }

  const avgLikes = count > 0 ? totalLikes / count : 0;
  const er = followers > 0 ? ((avgLikes / followers) * 100).toFixed(1) : '?';
  const postsPerWeek = scrapedPosts.length >= 2 && scrapedPosts[0].date && scrapedPosts[scrapedPosts.length - 1].date
    ? Math.round((scrapedPosts.length / ((new Date(scrapedPosts[0].date) - new Date(scrapedPosts[scrapedPosts.length - 1].date)) / (7 * 86400000))) * 10) / 10
    : '?';

  return {
    handle,
    followers: data.followers,
    followersNum: followers,
    posts: data.posts,
    bio: data.bio,
    engagementRate: er,
    avgLikes: Math.round(avgLikes),
    postsPerWeek: postsPerWeek || '?',
    scrapedPosts,
  };
}

// ============================================================
// HTML GENERATOR
// ============================================================
function generateAuditHTML(config, igData, industry) {
  const { name, business, handle, type, challenge } = config;
  const date = new Date().toLocaleDateString('en-US', { month: 'long', year: 'numeric' });
  const er = igData?.engagementRate || '?';
  const followers = igData?.followers || '?';
  const pPerWeek = igData?.postsPerWeek || '?';
  const benchmarkER = industry.benchmark_er;

  // Calculate benchmark bar width (er as % of 5%)
  const erNum = parseFloat(er) || 0;
  const barWidth = Math.min(Math.round((erNum / 5) * 100), 100);
  const barColor = erNum >= 3 ? 'good' : erNum >= 1.5 ? 'mid' : 'low';

  const postIdeasHTML = industry.post_ideas.map((p, i) => `
        <div class="post-idea">
            <div class="post-idea-num">Post ${i + 1}</div>
            <div class="post-idea-hook">${p.hook}</div>
            <div class="post-idea-desc">${p.desc}</div>
            <div class="post-idea-format">${p.format}</div>
        </div>`).join('\n');

  const captionsHTML = industry.caption_before.map(c => `
        <div class="before-after">
            <div class="ba-card before">
                <div class="ba-tag">Current Style</div>
                <p>"${c.before}"</p>
            </div>
            <div class="ba-card after">
                <div class="ba-tag">What We'd Write</div>
                <p>"${c.after}"</p>
            </div>
        </div>`).join('\n');

  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="noindex, nofollow">
    <title>Content Audit — ${business} | LoopWorker</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../audit-styles.css">
</head>
<body>
<div class="audit-container">

    <div class="audit-header">
        <div class="audit-badge">Content Audit</div>
        <h1>${business}</h1>
        <div class="client-info">
            <strong>@${handle}</strong> · ${type}<br>
            Prepared by Alex Lamb · ${date}
        </div>
    </div>

    <div class="audit-section">
        <h2>The Short Version</h2>
        <p><strong>The opportunity:</strong> Your business is already doing great work — your content just needs to match it. With the right visuals and hooks, your social media can become your best source of new customers.</p>
        <p><strong>The move:</strong> Better visuals, stronger hooks, and content that makes people act — not just scroll past.</p>
        <p><strong>The one rule:</strong> Every post should make someone think "I need to check this out."</p>
    </div>

    <hr class="audit-divider">

    <div class="audit-section">
        <h2>Your Numbers</h2>
        <div class="stat-row">
            <div class="stat-card">
                <div class="stat-number">${followers}</div>
                <div class="stat-label">Followers</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">${er}%</div>
                <div class="stat-label">Engagement Rate</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">${pPerWeek}</div>
                <div class="stat-label">Posts / Week</div>
            </div>
        </div>
        <div class="benchmark">
            <div class="benchmark-label">Your Engagement vs. Industry Benchmark</div>
            <div class="benchmark-bar">
                <div class="benchmark-fill ${barColor}" style="width: ${barWidth}%;"></div>
            </div>
            <div class="benchmark-numbers">
                <span>0%</span>
                <span><strong>You: ${er}%</strong></span>
                <span>Target: ${benchmarkER}</span>
            </div>
        </div>
    </div>

    <hr class="audit-divider">

    <div class="audit-section">
        <h2>Three Things That Will Change Everything</h2>
        <p>Your content is close. Here's where small upgrades create the biggest impact.</p>

        <div class="pillar-card">
            <div class="pillar-header">
                <h3>${industry.pillar_quality.title}</h3>
                <span class="pillar-badge">Big Opportunity</span>
            </div>
            <p>${industry.pillar_quality.opportunity}</p>
            <h4>What we'd do</h4>
            <ul class="audit-list fix">
                ${industry.pillar_quality.fixes.map(f => `<li>${f}</li>`).join('\n                ')}
            </ul>
        </div>

        <div class="pillar-card">
            <div class="pillar-header">
                <h3>${industry.pillar_consistency.title}</h3>
                <span class="pillar-badge">Big Opportunity</span>
            </div>
            <p>${industry.pillar_consistency.opportunity}</p>
            <h4>What we'd do</h4>
            <ul class="audit-list fix">
                ${industry.pillar_consistency.fixes.map(f => `<li>${f}</li>`).join('\n                ')}
            </ul>
        </div>

        <div class="pillar-card">
            <div class="pillar-header">
                <h3>${industry.pillar_engagement.title}</h3>
                <span class="pillar-badge">Ready to Grow</span>
            </div>
            <p>${industry.pillar_engagement.opportunity}</p>
            <h4>What we'd do</h4>
            <ul class="audit-list fix">
                ${industry.pillar_engagement.fixes.map(f => `<li>${f}</li>`).join('\n                ')}
            </ul>
        </div>
    </div>

    <hr class="audit-divider">

    <div class="audit-section">
        <h2>Same Business, Stronger Hooks</h2>
        ${captionsHTML}
    </div>

    <hr class="audit-divider">

    <div class="audit-section">
        <h2>5 Posts We'd Create For You</h2>
        ${postIdeasHTML}
    </div>

    <hr class="audit-divider">

    <div class="audit-cta">
        <h2>Want Us to Build This For You?</h2>
        <p>We do all the heavy lifting. Visuals, captions, hooks, videos, posting plan — created and delivered ready to post. You just hit publish.</p>
        <a href="https://www.loopworker.com/#audit-form" class="btn">Let's Go</a>
        <div class="pricing">Starter $300 · Growth $750 · Full Build $1,500</div>
    </div>

    <div class="audit-footer">
        <p><a href="https://www.loopworker.com">LoopWorker</a> · Helping businesses turn content into customers.</p>
    </div>

</div>
</body>
</html>`;
}

// ============================================================
// MAIN
// ============================================================
async function main() {
  const args = process.argv.slice(2);

  // Parse args
  const config = {};
  for (let i = 0; i < args.length; i += 2) {
    const key = args[i].replace('--', '');
    config[key] = args[i + 1];
  }

  // Load from config file if provided
  if (config.config && existsSync(config.config)) {
    Object.assign(config, JSON.parse(readFileSync(config.config, 'utf-8')));
  }

  const { name = 'there', business = 'Your Business', handle, type = 'restaurant', challenge = '' } = config;

  if (!handle) {
    console.log('Usage: node generate_audit.mjs --handle "instagramhandle" --business "Business Name" --type "restaurant"');
    console.log('Types: restaurant, medspa, gym, salon, coffee, realestate');
    process.exit(1);
  }

  const industryKey = type.toLowerCase().replace(/[^a-z]/g, '');
  const industry = INDUSTRY[industryKey] || INDUSTRY.restaurant;

  console.log(`\n=== Generating audit for ${business} (@${handle}) ===`);
  console.log(`Industry: ${type}\n`);

  // Scrape Instagram
  let igData = null;
  try {
    igData = await scrapeInstagram(handle);
    console.log(`  Followers: ${igData.followers}`);
    console.log(`  Engagement: ${igData.engagementRate}%`);
    console.log(`  Posts/week: ${igData.postsPerWeek}`);
  } catch (e) {
    console.log(`  Instagram scrape failed: ${e.message}`);
    igData = { followers: '?', engagementRate: '?', postsPerWeek: '?', avgLikes: 0 };
  }

  // Generate HTML
  const html = generateAuditHTML(config, igData, industry);

  const outDir = resolve('audits');
  mkdirSync(outDir, { recursive: true });
  const slug = business.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/-+/g, '-');
  const outPath = join(outDir, `${slug}.html`);

  writeFileSync(outPath, html);
  console.log(`\nAudit saved: ${outPath}`);
  console.log(`View: loopworker.com/audits/${slug}.html`);
}

main().catch(console.error);
