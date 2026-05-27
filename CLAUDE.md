# LoopWorker Website — loopworker-site

Static HTML site for LoopWorker — **Market Intelligence for Modern Brands**. Tagline: *Evidence before execution.*

Positioning pivoted May 21 2026 from DFY brand photography → market intelligence Sprint + Systems Retainer.

## Core pages
| File | Page |
|------|------|
| `index.html` | Homepage (Market Intelligence for Modern Brands) |
| `sprint.html` | The Sprint — full product walkthrough + 3-tier pricing |
| `pricing.html` | Pricing — Sprint Lite/Pro/Full + Systems Retainer |
| `services.html` | Implementation / signal environments |
| `case-studies.html` | Case studies (4 anonymized engagements) |
| `about.html` | About |
| `book.html` | Booking page (Cal.com embed pending) |
| `free-resources.html` | Lead magnets |
| `audit.html` | Standalone audit form |
| `404.html` | 404 page |

## Sprint ladder (live May 26 2026)
- **Signal Snapshot** — $750 / 48 hours — gateway, one signal pulled deep (test-the-waters)
- **Sprint Lite** — $2,500 / 5 days — one focused research round
- **Sprint Pro** ★ — $8,500 / 10 days — standard connected market brief
- **Sprint Full** — $25,000 / 14 days — launch / repositioning / pitch-deck
- **Systems Retainer** — $4,500/mo — post-Sprint execution

CTAs route directly to Stripe Payment Links. Ledger: `Memory/Code_Scripts/STRIPE_PAYMENT_LINKS.json`. Refresh links via `python3 create_stripe_links.py` (needs STRIPE_SECRET_KEY in env or `Projects/LoopWorker/.env`).

## Killed May 26 2026 (off-positioning)
restaurants · med-spa · fitness · ecommerce · clothing · real-estate · hotels (top-level vertical pages) + book/restaurant · book/medspa · book/fitness. Internal links re-routed to /sprint.html or removed.

## Blog (30+ SEO articles)
`blog/` — kept for SEO. Some vertical-specific articles (restaurant social media, ecommerce IG, med spa, fitness studio) remain — still rank, still drive traffic into Sprint funnel.

## Scripts
```bash
python fill_table_with_reels.py       # Fill Airtable with reels
python fill_table_with_text_posts.py  # Fill Airtable with text
python rewrite_and_generate_table1.py # Rewrite + generate
python rewrite_all_posts.py           # Rewrite copy
python prospect_finder.py             # Find prospects
python check_blotato.py               # Check Blotato status
```

## Hosting
Static HTML — no build step. Open any .html file directly or serve with any static server.
