# LoopWorker Website — loopworker-site

Static HTML site for LoopWorker — **the Decision Read**: an independent, evidence-backed second opinion on one important business decision. Public evidence investigated, options ranked, every material claim graded high/med/low with its source. Founder-led (Alex Lamb). Fixed price, days not months, money back if not useful.

Positioning pivoted May 21 2026 (DFY brand photography → market intelligence), then Jul 2026 to the current **Decision Read** framing. **The old "Sprint" brand is dead — never reintroduce Sprint / Atlas / Signal Snapshot / Compass / Surface / "Operating System" names.**

## Design systems
- **v6 "Graded Evidence"** (`v6-system.css`) — amber `#E3A44A` on near-black `#070708`, sharp 2-4px corners, Instrument Serif display + Inter body + JetBrains Mono tags, mono `►` labels, crop marks (`.marks`), VERIFIED/FLAGGED stamp chips, film grain, one warm aurora that drifts page-wide. Motion: scroll-reveal (`v6-reveal.js`), nav transparent→solid on scroll, specimen 3-card deck, receipt stamp-in. **Card display text = Inter, NEVER Instrument-Serif-italic (illegible at card size — Alex flagged repeatedly).**
- **v5** (`v5-system.css`) — the older shell still used by blog/, glossary/, vs/. **Rethemed Jul 17 to the same amber palette** (one var swap), so the whole tail is on-brand. Don't reintroduce indigo (`#6366F1`).
- **Cache-buster convention:** every v6 page links `/v6-system.css?v=graded-evidence-N`. After editing v6-system.css, bump N on all v6 pages so browsers refetch. Currently **graded-evidence-22**.
- **After any push:** curl the referenced css/assets on production, not just the page (a missing committed file 404s silently).

## The offer — four Reads, four depths
Everything is **the Decision Read**, sold by the buyer's question (lead with the question, small `►` Read-name tag on top):
- **The Competitor Read** — "How did my competitor do that?"
- **The Growth Read** — "Where should my next dollar go?"
- **The Pricing Read** — "What should I charge?"
- **The Market Read** — "Is this market worth entering?"

**Depth ladder = duration-only names** (tier names dropped Jul 16):
- **The 48-hour Read** — $750 (smallest paid step)
- **The 5-day Read** — $3,200 (includes review call)
- **The 10-day Read** — $8,000 (anchor: "default for six-figure decisions")
- **The 30-day Engagement** — $25,000, billed per milestone

**Free competitor teardown = top-of-funnel tripwire** (`/free-teardown.html` + `#free-teardown` on index): name one competitor, get a 48h public-signal teardown free, email-captured (Formspree `xbdpddrn`, tagged FREE TEARDOWN), bridges to the paid Read. This is the primary cold-traffic entry — the hero leads with it.

**Guarantee:** quiet "Terms of work / You're the judge of the work", 14-day usefulness refund. NEVER a loud slogan ("100% money back" and "useful or you don't pay" both rejected as cheap).

**No live Stripe checkout on the site** — all dead-product buy-links were killed Jul 17. CTAs route to `/free-teardown.html` or the `#send-question` form. Form-first, "no call to start."

## Core pages (all v6 unless noted)
| Path | Page |
|------|------|
| `index.html` | Homepage — hero (free-teardown CTA), specimen 3-card deck, proof ticker, 4 question cards, Recent Reads (3 real redacted receipts), how it works, pricing, FAQ, form |
| `pricing.html` | Four Reads + depth ladder + "what lands on your desk" doc breakdown + quiet terms |
| `faq.html` | AEO FAQ, FAQPage schema, grouped Q&A |
| `sample-brief.html` | Real redacted Competitor Read (Benesch Threat Read) embedded inline + PDF |
| `free-teardown.html` | Standalone free-teardown landing + Service/FAQ schema |
| `about.html` | Founder page (real photo, honest fit) |
| `thank-you.html` | Path-aware (free-teardown vs Read) via `?from=` |
| `law-firms/`, `beauty/`, `apparel/`, `food-beverage/`, `private-equity/` | ICP vertical landing pages (each = free-teardown funnel + Service/FAQ schema) |
| `reports/vitamin-c-serum-ads/`, `reports/functional-beverage-ads/` | Ad-library micro-reports built from REAL on-disk data (Dataset schema, free-to-cite) |
| `downloads/read-{law,coach,brand,threat}-redacted.html` + `.pdf` | 4 redacted sample Reads. HTML versions are indexable (canonical, web fonts). **NEVER regenerate from originals without re-running the full redaction verification** |
| `vs/*.html` | Comparison pages (mckinsey/bain/bcg/semrush/etc.) — v5 shell, amber, funnel-wired. Weak tool pages (ahrefs/zoominfo/crunchbase/g2/foreplay) redirect to free-teardown |
| `404.html`, `terms.html`, `privacy.html` | Utility |

Redirect stubs (noindex, preserve old inbound links): `sprint.html`→pricing, killed verticals (medspas/restaurants/etc.), `book.html`→#send-question, thank-you variants→thank-you.

## ICP (resolved Jul 17 — two lanes, one ladder)
- **Volume lane ($750-3,200):** founders of SHIPPING consumer brands (beauty/hair, apparel, scaled food+CPG) with live ad spend + an event trigger. NOT pre-launch.
- **Premium lane ($3,200-25,000):** traditional owner-operated ~$5M+, PE + portcos, corporate/defense law firms (buyer = CMO/CBDO).
- **Medspa OUT.** Food&bev floor ~$5M or national-retail/raise. Excluded: pre-revenue, local, AI/agency/recruiter sellers.

## Killed May 26 2026 (off-positioning)
Top-level vertical pages for restaurants · med-spa · fitness · ecommerce · clothing · real-estate · hotels (now redirect stubs).

## Blog + glossary (SEO, v5 shell, amber)
`blog/` (~39 articles) + `glossary/` — kept for SEO, on v5-system.css (amber). Some still carry legacy "Sprint" copy in body/nav; scrub opportunistically, don't mass-rewrite. Some glossary pages have broken `{{ }}` inline CSS (base v5-css still applies).

## Hard rules
- **NEVER fake data.** Micro-reports use only verified numbers from real on-disk pulls, dated, with methodology + caveats. No fabricated stats, no invented client names, no guessed LinkedIn URLs.
- **No em dashes** in visible copy. Plain voice, full sentences.
- **Never reintroduce** Sprint/Atlas/Signal Snapshot names or indigo.

## Hosting
Static HTML, no build step. **GitHub Pages** from `WolfAndThings/loopworker-site`, branch `main`, CNAME `www.loopworker.com`. Push to main = auto-deploy (~1-2 min). Forms on a Cloudflare Worker in `_serverless/`.
