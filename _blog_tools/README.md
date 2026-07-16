# LoopWorker Blog Build Standard

Reusable tooling + checklist for building and reviving `blog/` posts. Every new or revived post must meet this standard before deploy. Established Jun 2026 (8-post SEO revive batch).

## The blog system (know this first)
- `blog/` holds 400+ HTML files but only ~31 are real "Signals" posts (v5-system.css design, `v5-nav`). The other ~370 are `noindex` redirect STUBS (killed in the May 2026 market-intelligence pivot, commit `2238f68`). Stubs still pull residual Google impressions with 0 clicks = revive targets.
- Real pre-stub content lives in git: `git show <commit>:blog/FILE > blog/FILE` to restore. Last real version is usually at commit `8dea7f8` (some earlier, e.g. `ee1970d`). Find it: `for c in $(git log --format=%H -- blog/FILE); do echo $c $(git show $c:blog/FILE | grep -m1 '<title>'); done`
- Separate `/glossary/` system = ~50 v5 `DefinedTerm` pages catching definitional queries. Head-term queries (e.g. time-to-value, retention-cohort) land there, NOT blog. Avoid cannibalization: glossary = definition intent, blog = guide intent, cross-link both. NOTE: glossary `<style>` has escaped `{{ }}` braces (generated) — never touch the style, only title/desc/lead.

## Every post MUST have (checklist)
1. Indexable: `robots = index, follow, max-snippet:-1, ...`, self-canonical, NOT a redirect stub.
2. SEO `<title>` + matching og:title/twitter:title + Article schema `headline`. Hook style that wins (from web research): specific number + "actually works" skeptic-kill + stakes framing + colon subtitle + year stamp.
3. `<h1>` + `<p class="article-subtitle">` hook.
4. **Quick Answer block** right after subtitle: a 2-sentence, LLM-grabbable direct answer (green left-border box). Alex's rule: "if an LLM can't summarize you in 2 sentences, you don't exist to it."
5. Key Takeaways box.
6. Body sections (idea-cards / h2s).
7. **Visible FAQ section** (`<h2>Frequently Asked Questions</h2>` + idea-cards) AND matching `FAQPage` JSON-LD. Visible text must match schema.
8. **Engagement block** (before author-bio): lazy-loaded Disqus comments (shortname `loopworker`, loads on click = zero pagespeed cost), share bar (LinkedIn/X/copy, each fires a Plausible event), "Was this helpful?" (fires Plausible event). Comments style = "no agenda, just talk" (Alex: "we just comment, we don't have an agenda").
9. **Sprint funnel CTA** → `/sprint.html` (Surface scan gateway) + `/book.html`. NEVER old dead anchors `/#audit-form`, `/#examples`, `/#pricing`. Footer tagline = "Evidence before execution."
10. **NO em dash (—) or `&mdash;` anywhere** — standing rule, it's an AI tell. (All-lowercase is ONLY for LinkedIn comments, NOT blog.)
11. Hand-reviewed to sound human (read aloud), no fabricated stats.

## After building, wire it in
- Add URL to `sitemap.xml` (`<lastmod>` today, priority 0.8), verify `xmllint --noout sitemap.xml`.
- Append to `/llms.txt` "Guides and Signals posts" section (title · URL · one-line).
- Add a `post-card` to `blog/index.html` (Operator Guides section) for internal links.
- If a glossary term exists, cross-link both ways.

## Alex's SEO playbook (the notes, Jun 2026)
1. Write around NON-branded searches, not your own name (new domains can't win branded terms early).
2. Comparison pages for every competitor: `/vs/consultant|agency|in-house` + `/for/<industry>` (already live).
3. `llms.txt` + FAQ schema + quick-answer on everything (ChatGPT/Perplexity traffic is real).
4. Technical: canonical, IndexNow ping after each publish, hreflang only if multi-language.
5. Hand-review every piece, never publish raw AI.

## Tools in this dir
- `build_post.py` — generator for NEW posts (head+schema+nav+quick-answer+takeaways+body+FAQ+CTA+engagement from a content dict). Edit the post dict, run.
- `inject_faqs.py` — add visible FAQ section + FAQPage schema to existing posts.
- `inject_engagement.py` — add the engagement block (Disqus lazy + share + helpful) to existing posts. `DISQUS` var sets shortname.
- `lint_strip_dashes.py` — strip all em/en dashes from given files. Run before every commit.
- `_ref_apply_notes_2026-06-18.py` — reference: the IG anti-hashtag rebuild + quick-answer batch.

## Deploy
Static, no build step. Repo `WolfAndThings/loopworker-site`, branch `main` → GitHub Pages → www.loopworker.com. Alex pushes (harness blocks some pushes). After publish, ping IndexNow.
