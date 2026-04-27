---
tags: [dashboard, blog, loopworker-site]
---

# Blog Dashboard — loopworker.com

> 387 blog posts in `Projects/loopworker-site/blog/`

## Blog Stats
- **Total posts:** 387
- **Format:** Static HTML
- **Sitemap:** `Projects/loopworker-site/sitemap.xml` (80KB)
- **PageRank Queue:** `Projects/loopworker-site/BLOG_PAGERANK_QUEUE.tsv` (33KB)
- **Schema Gaps:** `Projects/loopworker-site/BLOG_SCHEMA_SUPPORT_GAPS.json` (66KB)

## Content Categories

### AI Photography by Niche
Bakeries, bookstores, breweries, chiropractors, coaches, coffee roasters, dance studios, dental, etsy sellers, event venues, fashion, fitness apparel, florists, food brands, furniture, gyms, hair salons, home services, hotels, interior design, jewelry, landscaping, laundromats, law firms, meal prep, med spas, music studios, nail salons, nonprofits, optometrists, outdoor brands, pet businesses, photography studios, pilates, plumbers, pottery studios, real estate, restaurants, skincare, small business, spas, tattoo shops, therapists, tutoring, veterinarians, vintage shops, wedding vendors, wineries, yoga studios

### General Topics
AI brand photography cost, AI vs stock photos, AI content automation, AI headshots, AI marketing for local business, content strategy, visual branding, brand identity, social media marketing

## Scripts
| Script | What It Does |
|--------|-------------|
| `generate_150_blogs.py` | Batch blog generation |
| `generate_5_more.py` | Small batch additions |
| `fix_pagerank_batch_*.py` (10 scripts) | PageRank optimization |

## Blog Post Briefs
```dataview
TABLE title, target_keyword, status
FROM #blog
SORT created DESC
```

## SEO Status
- [ ] All 387 posts have schema markup
- [ ] Sitemap up to date
- [ ] Internal linking audit complete
- [ ] PageRank gaps addressed
