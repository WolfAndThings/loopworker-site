# LoopWorker Website — loopworker-site

Static HTML site for LoopWorker — **Market Intelligence for Modern Brands**. Tagline: *Evidence before execution.*

Positioning pivoted May 21 2026 from DFY brand photography → market intelligence Sprint + Systems Retainer.

## Design system — V6 "Graded Evidence" (locked Jul 16 2026)
`v6-system.css` — amber `#E3A44A` accent (indigo is dead), sharp 2-4px corners, Instrument Serif display + Inter body + JetBrains Mono evidence tags, mono `►` labels, crop marks (`.marks`), VERIFIED/FLAGGED stamp chips, glass cards, one warm glow per section, film-grain overlay. Refs: Craft Agency + Perplexity Personal Computer + Spade (Mobbin). **index.html converted Jul 16 (copy 100% verbatim); all other pages still `v5-system.css` — roll page by page.** Revenue widgets (v5-revenue.js) keep v5-* class names, re-skinned inside v6-system.css. Reference mock: `_mocks/index_v6_mock.html`.

## Core pages
| File | Page |
|------|------|
| `index.html` | Homepage — The Decision Read (Jul 16: question-voice hero, 4 buyer-question cards, Recent Reads proof section w/ 3 downloadable redacted sample PDFs, 8 sections total). Source copy: `home-decision-read.html` (kept in sync) |
| `downloads/` | 4 redacted sample Reads (BW editorial style, Lora/WorkSans/JetBrains Mono): `read-law-redacted` (RWI Law growth read), `read-coach-redacted` (Jocelyn audit), `read-brand-redacted` (Gesine exec summary), `read-threat-redacted` (Benesch/Honigman Threat Read; original: `Memory/Strategy/benesch_hammerstrom_read/`). All verified zero client identifiers in HTML + PDF. NEVER regenerate from originals without re-running the full redaction verification |
| `sample-brief.html` | Sample Read page (hero "See a sample" + footer link). Rebuilt Jul 16 2026 in V6: real redacted Benesch Threat Read embedded inline + PDF download. REPLACED the fabricated "Decision Brief #247" placeholder — never restore it |
| `sprint.html` | The Sprint — full product walkthrough + 4-tier pricing |
| `pricing.html` | Pricing — Signal Snapshot/Competitive Intelligence Brief/Atlas/Market Operating System + Systems Retainer |
| `services.html` | Implementation / signal environments |
| `case-studies.html` | Case studies (4 anonymized engagements) |
| `about.html` | About |
| `book.html` | Booking page (Cal.com embed pending) |
| `free-resources.html` | Lead magnets |
| `audit.html` | Standalone audit form |
| `404.html` | 404 page |

## Decision Read ladder (renamed Jul 15 2026 — descriptive names convert better cold; durations synced to live pricing.html)
Everything is "The Decision Read" at four depths. Guarantee = usefulness, 14-day window, money back. Dated-call wedge REJECTED (see auto-memory `project_loopworker_offer_spine`).
- **Signal Snapshot** — $750 / 48 hours — gateway, one narrow question, fast second opinion (web + social + 3 next moves)
- **Competitive Intelligence Brief** — $3,200 / 5 days — competitive read + your strategic answer + 30-min call
- **Atlas** — $8,000 / 10 days — answer + full decision-grade read (competitor, customer, pricing, market) + call
- **Market Operating System** — $25,000 / 30 days + 3-month support — Atlas + positioning architecture + 90-day roadmap + execution playbook; billed per milestone
- **Systems Retainer** — $4,500/mo — post-engagement execution
- OLD names (do not use, pre Jul 15): Surface→Signal Snapshot, Compass→Competitive Intelligence Brief, Operating System→Market Operating System. Atlas unchanged.

Stripe ledger: `Memory/Code_Scripts/STRIPE_PAYMENT_LINKS.json` (all 5 links click-tested Jun 1 2026, 6/6 verified clean including Operating System).

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
