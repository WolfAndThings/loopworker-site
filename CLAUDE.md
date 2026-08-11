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

**Depth ladder = depth-of-deliverable names** (locked Jul 18; duration is spec next to price, never the label):
- **The One-Page Read** — $750 · 48h (smallest paid step)
- **The Focused Read** — $3,200 · 5 days (includes review call)
- **The Deep Read** — $8,000 · 10 days (anchor: "default for six-figure decisions")
- **The Engagement** — $25,000 · 30 days, billed per milestone
Duration-only names (48-hour/5-day/10-day Read) are retired — don't reintroduce them as labels.

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
| `vs/index.html` | Comparison hub (v6). Groups the 14 live vs pages: consultancies, Big Four, tools. Carries the caveat that competitor prices come from published rate cards and public reporting, not quotes. Linked sitewide from the footer "More:" row |
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

## SEO + AEO baseline (clean as of Aug 10 2026 — keep it that way)
Every indexable page: title ≤62 chars, description 110-165, canonical, og:image, exactly one h1, JSON-LD. Verify after any page work with an attribute-aware regex; a `content=["\']` pattern silently truncates at the first apostrophe and under-reports lengths.
- **`llms.txt` is offer copy, not boilerplate.** It feeds ChatGPT and Perplexity. Re-check it against the NAMING CANON whenever pricing or product names move; it shipped retired duration names for weeks after the Jul 18 rename.
- **`robots.txt` names the AI crawlers** (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, Perplexity-User, ClaudeBot, Claude-User, Google-Extended, Applebot-Extended). A named user-agent group REPLACES the wildcard group, so every group repeats the full disallow list. Never add a group without the disallows.
- **FAQPage markup must match visible text exactly.** Site FAQs live in `<details><summary>`, not headings, so a heading-only grep will wrongly report "no FAQ."
- **New pages need an inbound internal link,** not just a sitemap entry. Sitemap presence alone left 37 pages orphaned. Hubs: footer "More:" row (13 core pages) → `/vs/`, `/reports/`, `/glossary/`, `/blog/`; `for/{vert}.html` → its 5 children.
- **Never generate a page with `canvas-design` fonts left in place** — those `@font-face` rules point at `/Users/alexlamb/.claude/skills/...`, which 404s in production and publishes the local path. Swap to Google Fonts before shipping.
- **After any deploy that changes titles, descriptions, pricing or `llms.txt`, run `./_blog_tools/indexnow_ping.sh`.** Pings Bing, Yandex, Naver, Seznam, Yep. The hosted key is the 48-hex `.txt` in the repo root; `.indexnow-key` holds a local copy and is gitignored. **Google does not participate in IndexNow** — Google needs a Search Console re-index request.

## Search Console and analytics access (state as of Aug 11 2026)
- GSC property **is verified** (`google9258fb3826a9df03.html`, live, 200). Sitemap is live and valid at 145 URLs.
- **No API credentials on this machine.** `google_auth.py --check` reports tier -1; there is no `~/.config/claude-seo/google-api.json`. So no session can read ranking, impression, or indexation data until that is set up. Do not claim performance numbers without it.
- To wire it: Google Cloud project → enable Search Console API → OAuth desktop client → `claude-seo run google_auth.py --auth --creds <client_secret.json>`. A plain `GOOGLE_API_KEY` alone unlocks PageSpeed and CrUX but NOT Search Console.
- **Bing Webmaster Tools is not set up** (no `BingSiteAuth.xml`). It imports from GSC in one click and it is what feeds Copilot.
- The seo skill runtime is missing `requests` and `playwright`, so its network and screenshot scripts fail. Either `pip install -r ~/.claude/skills/seo/requirements.txt` or do the call directly.

## Hard rules
- **NEVER fake data.** Micro-reports use only verified numbers from real on-disk pulls, dated, with methodology + caveats. No fabricated stats, no invented client names, no guessed LinkedIn URLs.
- **No em dashes** in visible copy. Plain voice, full sentences.
- **Never reintroduce** Sprint/Atlas/Signal Snapshot names or indigo.

## Hosting
Static HTML, no build step. **GitHub Pages** from `WolfAndThings/loopworker-site`, branch `main`, CNAME `www.loopworker.com`. Push to main = auto-deploy (~1-2 min). Forms on a Cloudflare Worker in `_serverless/`.
