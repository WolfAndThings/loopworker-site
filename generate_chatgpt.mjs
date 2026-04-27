import { chromium } from 'playwright';
import { resolve, join } from 'path';
import { mkdirSync, existsSync, writeFileSync } from 'fs';

const CHROME_PROFILE = '/Users/alexlamb/Library/Caches/ms-playwright/mcp-chrome-manual';
const OUTPUT_DIR = resolve('images/case_studies');
const REF_DIR = resolve('images/case_studies/references');

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

const BRANDS = {
  myburger: {
    refs: [join(REF_DIR, 'myburger/01.jpg'), join(REF_DIR, 'myburger/02.jpg'), join(REF_DIR, 'myburger/03.jpg')],
    prompts: [
      {
        name: 'hero_counter',
        prompt: `Use the attached reference images as style, color, and brand reference for My Burger — a family-owned Minneapolis burger chain. Brand colors: chocolate brown #342200, golden amber #f1b257, brick red #a76868.

A smash burger on a paper-lined red plastic tray at a diner counter, shot from slightly above. Melted American cheese dripping over the edges, caramelized onions. Condensation on a glass bottle next to it. Worn laminate counter. Cook in a black apron blurred behind the counter. Direct flash, warm overhead fluorescents. The vibe matches My Burger's locations — casual, warm, real neighborhood spot in Minneapolis. Real photograph. 2:3 vertical, no text overlays.`,
      },
      {
        name: 'social_booth',
        prompt: `Use the attached reference images as style, color, and brand reference for My Burger — Minneapolis burger chain. Brand colors: #342200, #f1b257, #a76868.

Three friends crammed into a booth at a burger restaurant, mid-laugh, holding burgers. Sauce on someone's chin. Crumpled wax paper, scattered fries, half-empty drinks. Worn red vinyl booth. Warm light, afternoon sun from window. Background blurred. Feels like My Burger's casual Minneapolis vibe — not a chain, a neighborhood spot. Real candid photo. 2:3 vertical, no text overlays.`,
      },
      {
        name: 'detail_smash',
        prompt: `Use the attached reference images as style reference for My Burger.

Extreme close-up of a spatula pressing a beef patty flat onto a hot griddle. Grease splattering, sear marks, steam. Cook's hand in a black glove. Griddle seasoned from years of use. Warm golden blur behind. This is the "Flippin' Good Burgers" moment. Real photograph. 2:3 vertical, no text overlays.`,
      },
      {
        name: 'environmental_storefront',
        prompt: `Use the attached reference images as style and brand reference for My Burger — 11 locations across Minneapolis-St. Paul. Brand colors: chocolate brown #342200, golden amber #f1b257.

Wide shot of a casual burger restaurant storefront at golden hour in a Minneapolis suburb. Warm interior light through windows. A family approaching — dad holding door, kid running ahead. Small parking lot. The exterior feels like a real My Burger location — modern fast-casual, warm brand colors on the facade, neighborhood feel. Real photograph. 2:3 vertical, no text overlays.`,
      },
      {
        name: 'action_handoff',
        prompt: `Use the attached reference images as style reference for My Burger.

Medium shot of a counter worker in a black apron sliding a tray of burgers and fries across the counter to a customer reaching for it. Worker smiling naturally, not at camera. Warm overhead lights, stainless steel behind. Real moment, real energy. 2:3 vertical, no text overlays.`,
      },
      {
        name: 'closing_latenight',
        prompt: `Use the attached reference images as style reference for My Burger.

A half-eaten burger on a tray by a window at night. Streetlights blurred outside. Crumpled napkin, empty drink cup. Restaurant warm and nearly empty, end of night. An employee wiping a table in the blurred background. Quiet, real, end-of-day at a neighborhood burger spot. 2:3 vertical, no text overlays.`,
      },
    ],
  },
  marina: {
    refs: [join(REF_DIR, 'marina/01.jpg'), join(REF_DIR, 'marina/02.jpg'), join(REF_DIR, 'marina/03.jpg')],
    prompts: [
      {
        name: 'hero_consultation',
        prompt: `Use the attached reference images as style and brand reference for Marina MedSpa — a premium medspa in Marina del Rey, Los Angeles. Brand colors: teal #26c4db, warm beige #dbcec2, white.

A female patient in her mid-30s in a modern medspa treatment chair, talking naturally with a female aesthetician in a white coat. Aesthetician gesturing toward patient's jawline, holding a tablet. Bright airy room, large window, diffused LA light. Both relaxed, mid-conversation. Skin has real texture — pores, natural. The space feels like Marina MedSpa — clean, premium, teal accents, Marina del Rey sophistication. Real photograph. 2:3 vertical, no text overlays.`,
      },
      {
        name: 'portrait_patient',
        prompt: `Use the attached reference images as style reference for Marina MedSpa. Brand colors: teal #26c4db, warm beige #dbcec2.

Tight portrait of a woman in her early 40s, three-quarter angle, soft smile. Cream camisole. Real skin — laugh lines, natural brows, light freckles. Window light from right. Warm beige wall behind, blurred. She looks healthy, not perfect. Real photograph. 2:3 vertical, no text overlays.`,
      },
      {
        name: 'detail_treatment',
        prompt: `Use the attached reference images as style reference for Marina MedSpa.

Close-up of a gloved hand holding a syringe near a patient's cheek. Only lower half of face visible. Light blue nitrile glove, fine needle. Real skin — pores, slight redness. Bright clinical lighting. Teal accent blurred in background. Clean, precise. Real photograph. 2:3 vertical, no text overlays.`,
      },
      {
        name: 'environmental_reception',
        prompt: `Use the attached reference images as style and brand reference for Marina MedSpa — Marina del Rey, CA. Brand colors: teal #26c4db, warm beige #dbcec2.

Wide shot of a modern medspa reception area. White desk, warm beige accent wall. Receptionist handing clipboard to a woman arriving — sunglasses on head, linen blazer. Bright LA light through windows. Small flowers on desk. Feels like Marina del Rey — minimal, clean, warm, coastal-luxury. Real photograph. 2:3 vertical, no text overlays.`,
      },
      {
        name: 'social_result',
        prompt: `Use the attached reference images as style reference for Marina MedSpa.

A woman in her late 30s looking in a handheld mirror after treatment, touching her jawline. Treatment chair, robe. Subtle satisfaction — quietly pleased. Nurse behind, arms crossed. Natural, unposed. Real photograph. 2:3 vertical, no text overlays.`,
      },
      {
        name: 'stilllife_tools',
        prompt: `Use the attached reference images as style reference for Marina MedSpa. Brand accent: teal #26c4db.

Overhead flat lay of a medspa treatment tray on white surface. Syringe, filler bottle, nitrile gloves, cotton pad, glass vial. Real medical-grade. Soft light from upper left. Stainless tray with small teal towel at one edge. Clinical but beautiful. Real photograph. 2:3 vertical, no text overlays.`,
      },
    ],
  },
  bouldering: {
    refs: [join(REF_DIR, 'bouldering/01.jpg'), join(REF_DIR, 'bouldering/02.jpg'), join(REF_DIR, 'bouldering/03.jpg')],
    prompts: [
      {
        name: 'hero_wall',
        prompt: `Use the attached reference images as style and brand reference for Bouldering Project — an indoor climbing gym in St. Paul, Minnesota. Brand: black and white identity, walls carry the color (blues, teals, oranges, yellows). "Fall in love with difficult pursuits."

Wide shot of a large indoor bouldering gym, busy afternoon. 8-10 climbers at various heights. Cool blue and teal wall panels with multicolored holds — orange, yellow, pink, green. Thick crash mats. Tall ceilings, exposed beams. Massive windows with natural afternoon light. Active but relaxed, community vibe. Feels like Bouldering Project St. Paul — brand new, huge, natural light everywhere. Real photograph. 2:3 vertical, no text overlays.`,
      },
      {
        name: 'portrait_climber',
        prompt: `Use the attached reference images as style reference for Bouldering Project.

Medium-tight portrait of a woman in her late 20s at the base of a climbing wall, looking up with chalk on her hands. Black tank top, olive pants, messy bun. Chalk bag on waist. Focused — reading holds. Teal wall with orange and yellow holds blurred behind. Natural window light. Chalk dust on forearms. Real photograph. 2:3 vertical, no text overlays.`,
      },
      {
        name: 'social_beta',
        prompt: `Use the attached reference images as style reference for Bouldering Project.

Two climbers at the base of a problem looking up. Man pointing at a hold with chalked hand, woman nodding, arms crossed. Casual climbing clothes. Chalk bags, water bottles, shoes on the mat. Others blurred behind. Bright natural skylight. Friends solving a problem. Real photograph. 2:3 vertical, no text overlays.`,
      },
      {
        name: 'action_send',
        prompt: `Use the attached reference images as style reference for Bouldering Project.

A climber mid-move on an overhanging wall, reaching dynamically for the top hold. Body extended, feet flagging. Green and orange holds on dark blue wall. Shot from below. Spotter below, arms raised. Natural backlight from windows. Real photograph. 2:3 vertical, no text overlays.`,
      },
      {
        name: 'environmental_space',
        prompt: `Use the attached reference images as style and brand reference for Bouldering Project St. Paul — North America's largest new bouldering gym (2025). 11,300 sq ft of climbing wall.

Wide establishing shot from the entrance. Massive walls with multicolored holds. Yoga studio through glass walls on left. Bouldering area in center. Fitness area on right. Tall ceilings, exposed ductwork. Natural light from floor-to-ceiling windows. Industrial cathedral for play. Real photograph. 2:3 vertical, no text overlays.`,
      },
      {
        name: 'closing_rest',
        prompt: `Use the attached reference images as style reference for Bouldering Project.

Two friends on crash mats after climbing, backs against wall, legs out. One drinking water, other unlacing shoes. Chalk on hands. Gear between them. Late afternoon golden light through windows. Few climbers on walls blurred behind. Tired, satisfied, social. Real photograph. 2:3 vertical, no text overlays.`,
      },
    ],
  },
};

async function main() {
  console.log('\n=== ChatGPT Image Generator — All 3 Brands ===\n');

  const browser = await chromium.launchPersistentContext(CHROME_PROFILE, {
    headless: false,
    channel: 'chrome',
    viewport: { width: 1280, height: 900 },
    args: ['--disable-blink-features=AutomationControlled'],
  });

  const page = browser.pages()[0] || await browser.newPage();
  const allBrands = Object.keys(BRANDS);
  const total = allBrands.reduce((s, b) => s + BRANDS[b].prompts.length, 0);
  let count = 0;

  for (const brandKey of allBrands) {
    const brand = BRANDS[brandKey];
    const outDir = join(OUTPUT_DIR, brandKey);
    mkdirSync(outDir, { recursive: true });

    console.log(`\n--- ${brandKey.toUpperCase()} (${brand.prompts.length} prompts) ---`);

    for (let i = 0; i < brand.prompts.length; i++) {
      const { name, prompt } = brand.prompts[i];
      const outPath = join(outDir, `${name}.png`);
      count++;

      if (existsSync(outPath)) {
        console.log(`[${count}/${total}] ${brandKey}/${name} — exists, skipping`);
        continue;
      }

      console.log(`[${count}/${total}] ${brandKey}/${name}`);

      // New conversation
      await page.goto('https://chatgpt.com/', { waitUntil: 'domcontentloaded', timeout: 60000 });
      await sleep(5000);

      // Upload reference images
      try {
        const fileInput = await page.locator('input[type="file"]').first();
        const refs = brand.refs.filter(r => existsSync(r));
        if (refs.length > 0) {
          await fileInput.setInputFiles(refs);
          console.log(`    ${refs.length} reference images uploaded`);
          await sleep(3000);
        }
      } catch (e) {
        console.log('    Ref upload skipped:', e.message);
      }

      // Type prompt
      const textarea = page.locator('#prompt-textarea, [contenteditable="true"]').first();
      await textarea.click();
      await sleep(500);

      try {
        await textarea.fill(prompt);
      } catch {
        // contenteditable fallback
        await page.keyboard.insertText(prompt);
      }
      await sleep(1000);

      // Send
      try {
        const sendBtn = page.locator('[data-testid="send-button"], button[aria-label="Send prompt"]').first();
        await sendBtn.click();
      } catch {
        await page.keyboard.press('Enter');
      }
      console.log('    Sent, waiting for image...');

      // Wait for generated image (up to 3 min)
      let imageUrl = null;
      for (let poll = 0; poll < 36; poll++) {
        await sleep(5000);

        // Check for images
        imageUrl = await page.evaluate(() => {
          const imgs = document.querySelectorAll('img');
          for (const img of imgs) {
            const src = img.src || '';
            if ((src.includes('oaidalleapiprodscus') || src.includes('dalle') || src.includes('.openai.com'))
                && !src.includes('avatar') && !src.includes('logo') && img.width > 200) {
              return src;
            }
          }
          return null;
        });

        if (imageUrl) break;
        if (poll % 6 === 5) console.log(`    Still waiting... (${(poll + 1) * 5}s)`);
      }

      if (imageUrl) {
        try {
          const res = await fetch(imageUrl);
          const buf = Buffer.from(await res.arrayBuffer());
          writeFileSync(outPath, buf);
          console.log(`    Saved: ${outPath}`);
        } catch (e) {
          console.log(`    Download failed: ${e.message}`);
          // Screenshot fallback
          try {
            const imgEl = page.locator('img[src*="oaidalleapiprodscus"], img[src*="dalle"]').first();
            await imgEl.screenshot({ path: outPath });
            console.log(`    Saved via screenshot: ${outPath}`);
          } catch {}
        }
      } else {
        console.log('    No image found after 3 minutes');
      }

      await sleep(3000);
    }
  }

  console.log(`\n=== Done: ${count}/${total} ===`);
  console.log(`Images at: ${OUTPUT_DIR}`);
  // Leave browser open for inspection
}

main().catch(console.error);
