# Blog Retrieval Fix Plan

## Goal
Make every LoopWorker post easier for search engines and LLMs to extract, attribute, and cluster by topic.

## Top 15 Completed First
These were selected from the site's internal link graph, not from title guesses:

1. `blog/ai-brand-photography-cost.html`
2. `blog/ai-photography-prompts-that-dont-look-ai.html`
3. `blog/ai-vs-traditional-product-photography.html`
4. `blog/ai-brand-photography-vs-stock-photos.html`
5. `blog/build-brand-identity-with-ai.html`
6. `blog/content-calendar-template-small-business.html`
7. `blog/ecommerce-ai-product-photos.html`
8. `blog/how-to-automate-instagram-posting.html`
9. `blog/hiring-photographer-vs-ai-photography.html`
10. `blog/how-to-create-brand-style-guide-ai.html`
11. `blog/ai-content-automation-small-business.html`
12. `blog/ai-photography-for-personal-brands.html`
13. `blog/ai-product-photography-amazon-sellers.html`
14. `blog/restaurant-ai-photography.html`
15. `blog/social-media-content-strategy-small-business.html`

Applied to this tier:

- Rewrote major section headings into direct buyer questions.
- Normalized `https://www.loopworker.com` canonical and structured-data URLs.
- Removed corrupted `I create done-for-you content` copy where it appeared in these pages.
- Added missing `Related Reading` blocks on high-priority pages that lacked them.
- Cleaned obviously broken FAQ phrasing where it appeared inside this set.

## Audit Baseline For The Full Corpus

- `236` blog posts total.
- Only `8 / 2061` H2s were phrased as questions before this pass.
- `12` posts used non-`www` canonicals.
- `43` posts contained the corrupted `I create done-for-you content` phrase.
- `51` posts were missing at least one of: FAQ, breadcrumb, or `Related Reading`.

## Fix Order For The Remaining Posts

### Tier 2: Next 25 By PageRank
Use the same manual rewrite standard as the top 15.

- Prioritize commercially relevant cluster pages first.
- Favor pages that already have strong internal links and existing FAQ schema.
- Hit comparison guides, system guides, and "how much does it cost" posts before niche long-tail posts.

### Tier 3: Cluster Owners
Finish the pages that define the main authority clusters:

- AI brand photography
- AI product photography
- content automation
- social media systems
- local business customer acquisition
- restaurant marketing/content systems
- personal brand visual systems

### Tier 4: Vertical Playbooks
Move through service and industry pages in batches:

- restaurants and food
- ecommerce and product brands
- fitness and gyms
- med spa / beauty / personal care
- real estate / hospitality
- general local business

### Tier 5: Long-Tail Support Content
Clean up the remaining tactical posts after the cluster owners are stable.

## Per-Page Fix Checklist

- Rewrite the subtitle or first paragraph into an answer-first summary.
- Rewrite every major H2 into a buyer question.
- Make FAQ schema use actual searcher wording, not section labels.
- Add `Related Reading` with 3-5 relevant cluster links.
- Normalize canonical, `og:url`, and JSON-LD URLs to `https://www.loopworker.com`.
- Remove broken copy substitutions and vague positioning language.
- Add a named framework, checklist, table, or model where the topic allows it.
- Make the CTA match the article's intent and cluster.

## What Can Be Automated

- canonical and `og:url` normalization
- structured-data hostname normalization
- broken-phrase cleanup
- detection of missing FAQ / breadcrumb / `Related Reading`
- detection of posts with zero question-based H2s

## What Still Needs Manual Editorial Work

- rewriting intros so the first 100 words answer the query directly
- turning generic H2s into strong buyer questions
- improving internal link relevance inside clusters
- inserting named frameworks and comparison models
- tightening CTA language to match page intent

## Suggested Rollout Cadence

- Batch size: `15-20` posts at a time
- Order inside each batch: highest PageRank first, then highest commercial intent
- QA after each batch: check canonicals, `Related Reading`, H2 questions, bad phrase count, and broken links

## QA Gate Before Publish

- no corrupted phrase substitutions
- all structured URLs use `www`
- at least one answer-first summary near the top
- every major H2 is a real question or an unavoidable utility heading
- `Related Reading` present and relevant
- CTA still makes sense for the page
