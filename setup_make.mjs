import { chromium } from 'playwright';

const CHROME_PROFILE = '/Users/alexlamb/Library/Caches/ms-playwright/mcp-chrome-manual';

async function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

async function main() {
  console.log('Opening Make.com — please sign in if needed...');

  const browser = await chromium.launchPersistentContext(CHROME_PROFILE, {
    headless: false,
    channel: 'chrome',
    viewport: { width: 1400, height: 900 },
    args: ['--disable-blink-features=AutomationControlled'],
  });

  const page = browser.pages()[0] || await browser.newPage();

  // Go to Make.com login
  await page.goto('https://www.make.com/en/login', { waitUntil: 'domcontentloaded', timeout: 60000 });

  console.log('Waiting for you to sign in... (I\'ll continue once I detect the dashboard)');

  // Wait for dashboard to load (user signs in manually)
  for (let i = 0; i < 120; i++) {
    await sleep(5000);
    const url = page.url();
    if (url.includes('/scenarios') || url.includes('/dashboard') || url.includes('/organization')) {
      console.log('Signed in! Detected dashboard.');
      break;
    }
    if (i % 6 === 5) console.log(`Still waiting for sign-in... (${(i+1)*5}s)`);
  }

  // Navigate to create new scenario
  console.log('Creating new scenario...');
  await page.goto('https://us1.make.com/scenarios/add', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await sleep(5000);

  // Look for the "+" or initial module area to start building
  // Make.com's scenario builder is a visual canvas - we need to click to add the first module

  // Try clicking the center "+" button to add first module
  try {
    const addBtn = page.locator('[data-testid="add-module"], .add-module, [class*="AddModule"], [class*="add-trigger"]').first();
    await addBtn.click({ timeout: 10000 });
    console.log('Clicked add module');
  } catch {
    // Try clicking the big + in the center
    try {
      const plusBtn = page.locator('text="+"').first();
      await plusBtn.click({ timeout: 5000 });
      console.log('Clicked + button');
    } catch {
      console.log('Could not find add button — Make.com UI may have changed. Please add a Webhook module manually.');
    }
  }
  await sleep(3000);

  // Search for Webhooks module
  try {
    const searchInput = page.locator('input[placeholder*="Search"], input[type="search"], [data-testid="search-input"]').first();
    await searchInput.fill('Webhooks');
    await sleep(2000);

    // Click on Webhooks result
    const webhookOption = page.locator('text="Webhooks"').first();
    await webhookOption.click();
    await sleep(2000);

    // Select "Custom webhook"
    const customWebhook = page.locator('text="Custom webhook"').first();
    await customWebhook.click();
    await sleep(3000);

    console.log('Webhook module added!');

    // Try to create/add a new webhook
    const addWebhook = page.locator('text="Add", button:has-text("Add")').first();
    await addWebhook.click({ timeout: 5000 });
    await sleep(2000);

    // Name it
    const nameInput = page.locator('input[placeholder*="name"], input[name*="name"]').first();
    await nameInput.fill('LoopWorker Audit Form');
    await sleep(1000);

    // Save
    const saveBtn = page.locator('text="Save", button:has-text("Save")').first();
    await saveBtn.click({ timeout: 5000 });
    await sleep(3000);

    // Get the webhook URL
    const webhookUrl = await page.evaluate(() => {
      // Look for the URL in the page
      const els = document.querySelectorAll('input, textarea, [class*="url"], [class*="webhook"]');
      for (const el of els) {
        const val = el.value || el.textContent;
        if (val && val.includes('hook.us1.make.com')) return val;
      }
      // Also check clipboard or displayed text
      const allText = document.body.innerText;
      const match = allText.match(/https:\/\/hook\..*?make\.com\/[^\s"']+/);
      return match ? match[0] : null;
    });

    if (webhookUrl) {
      console.log(`\n✓ WEBHOOK URL: ${webhookUrl}\n`);
      // Save it to a file
      const fs = await import('fs');
      fs.writeFileSync('/Users/alexlamb/Desktop/AE_Exports/loopworker-site/make_webhook_url.txt', webhookUrl);
      console.log('Saved to make_webhook_url.txt');
    } else {
      console.log('Could not auto-detect webhook URL. Copy it from the Make.com interface.');
    }

  } catch (e) {
    console.log('Automation hit a snag:', e.message);
    console.log('The Make.com scenario builder is open — please add a Custom Webhook module manually.');
  }

  console.log('\nBrowser is open. Set up the rest in Make.com:');
  console.log('1. The webhook module should be created');
  console.log('2. Add a Gmail > Send an Email module next');
  console.log('3. Set To: {{email}}, Subject: "Got your audit request", Body: (see below)');
  console.log('\nLeaving browser open for you to finish...');

  // Keep alive
  await sleep(600000);
}

main().catch(console.error);
