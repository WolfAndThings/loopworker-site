#!/usr/bin/env python3
"""
Scaffold a new A-B-C-A AEO blog post.

Usage:
    python3 new_post.py "Why your ads stop working after 60 days"
    python3 new_post.py "Your title" --slug custom-slug

Creates blog/<slug>.html from _post_template.html with:
- Title, slug, canonical, og tags, JSON-LD all rewritten
- Today's date stamped in published/modified meta + JSON-LD + visible byline
- TODO markers in body for you to fill in TLDR + A/B/C/A' + FAQ + CTA

After filling in:
- Update sitemap.xml (1 line)
- Add to blog/index.html article cards
"""
import sys, re, datetime
from pathlib import Path

if len(sys.argv) < 2:
    sys.exit("Usage: python3 new_post.py \"Post title\" [--slug custom-slug]")

title = sys.argv[1]
slug = None
if '--slug' in sys.argv:
    slug = sys.argv[sys.argv.index('--slug') + 1]
else:
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

template = Path(__file__).parent / '_post_template.html'
target = Path(__file__).parent / f'{slug}.html'
if target.exists():
    sys.exit(f"Exists: {target.name}. Pick a different slug.")

today = datetime.date.today().isoformat()
today_pretty = datetime.date.today().strftime('%B %-d, %Y')

t = template.read_text()

# Swap title across <title>, og, twitter, JSON-LD
t = re.sub(r'(<title>)[^<]+(</title>)', f'\\1{title} · Signals · LoopWorker\\2', t)
t = re.sub(r'(og:title" content=")[^"]+(")', f'\\1{title}\\2', t)
t = re.sub(r'(twitter:title" content=")[^"]+(")', f'\\1{title}\\2', t)
t = re.sub(r'(headline": ")[^"]+(")', f'\\1{title}\\2', t)
t = re.sub(r'(<h1 class="sig-h1">)[^<]+(</h1>)', f'\\1{title}\\2', t)

# Swap canonical/url/breadcrumb link
old_slug_match = re.search(r'/blog/([\w-]+)\.html', t)
if old_slug_match:
    old_slug = old_slug_match.group(1)
    t = t.replace(f'/blog/{old_slug}.html', f'/blog/{slug}.html')

# Date stamps
t = re.sub(r'article:published_time" content="[^"]+"', f'article:published_time" content="{today}"', t)
t = re.sub(r'article:modified_time" content="[^"]+"', f'article:modified_time" content="{today}"', t)
t = re.sub(r'"datePublished": "[^"]+"', f'"datePublished": "{today}"', t)
t = re.sub(r'"dateModified": "[^"]+"', f'"dateModified": "{today}"', t)
t = re.sub(r'Last updated [^.]+\. Field notes', f'Last updated {today_pretty}. Field notes', t)
t = re.sub(r'<span>May 31, 2026</span>', f'<span>{today_pretty}</span>', t)

# Mark body for human fill
t = re.sub(
    r'(<p class="sig-lead">)[^<]+(</p>)',
    r'\1[TODO: 1-line sub-hook for the title]\2',
    t
)
# Mark TLDR
t = re.sub(
    r'(<aside class="sig-tldr">\s*<span class="sig-tldr-label">◆ TL;DR</span>\s*<p>)[^<]+(</p>)',
    r'\1[TODO: 40-60 word answer-ready summary for AI search snippets]\2',
    t
)

# Replace the body sections from "The 8 PM scroll" through "Back to" with A-B-C-A markers
# Find <section class="sig-section"> blocks and replace contents
new_body = '''
    <section class="sig-section">
      <h2>[TODO A · Scene/hook]</h2>
      <p>[TODO: Open with a specific scene, moment, or observation. 2-4 sentences. Plant the question.]</p>
    </section>

    <section class="sig-section">
      <h2>[TODO B · Mechanism/why]</h2>
      <div class="sig-def"><strong>[Key term]:</strong>[One-sentence definition. AEO loves this.]</div>
      <p>[TODO: Explain WHY the thing in A happens. Cite mechanism, data, evidence.]</p>
      <div class="sig-stat-row">
        <div class="sig-stat"><div class="sig-stat-num">[X]</div><div class="sig-stat-label">[stat label]</div></div>
        <div class="sig-stat"><div class="sig-stat-num">[X]</div><div class="sig-stat-label">[stat label]</div></div>
        <div class="sig-stat"><div class="sig-stat-num">[X]</div><div class="sig-stat-label">[stat label]</div></div>
      </div>
      <div class="sig-callout"><p>[Short italic pull-quote that crystalizes the mechanism]</p></div>
    </section>

    <section class="sig-section">
      <h2>[TODO C · Application/the move]</h2>
      <p>[TODO: What to do with the insight. Concrete steps.]</p>
      <ol>
        <li><strong>[Step 1]</strong> description</li>
        <li><strong>[Step 2]</strong> description</li>
        <li><strong>[Step 3]</strong> description</li>
      </ol>
      <h3>[TODO: When NOT to do this / counter-case]</h3>
      <p>[TODO: One paragraph showing edge case or when the move is wrong.]</p>
    </section>

    <section class="sig-section">
      <h2>[TODO A' · Callback to scene]</h2>
      <p>[TODO: Return to the opening scene with new meaning. 2-3 sentences. Don't over-resolve.]</p>
    </section>
'''
# Replace all sig-section blocks (5 of them in template) with placeholder
t = re.sub(
    r'<section class="sig-section">.*?</section>\s*(?=<section class="sig-faq">)',
    new_body + '\n    ',
    t, count=1, flags=re.S
)

# Reset FAQ to placeholder
faq_placeholder = '''<section class="sig-faq">
      <div class="sig-faq-label">◆ Common questions</div>
      <details><summary>[TODO Q1?]</summary><p>[TODO 40-60 word answer]</p></details>
      <details><summary>[TODO Q2?]</summary><p>[TODO 40-60 word answer]</p></details>
      <details><summary>[TODO Q3?]</summary><p>[TODO 40-60 word answer]</p></details>
      <details><summary>[TODO Q4?]</summary><p>[TODO 40-60 word answer]</p></details>
      <details><summary>[TODO Q5?]</summary><p>[TODO 40-60 word answer]</p></details>
    </section>'''
t = re.sub(r'<section class="sig-faq">.*?</section>', faq_placeholder, t, count=1, flags=re.S)

# Reset JSON-LD FAQ entities
ld_faq = '''"mainEntity": [
          { "@type": "Question", "name": "[TODO Q1?]", "acceptedAnswer": { "@type": "Answer", "text": "[TODO 40-60 word answer]" } },
          { "@type": "Question", "name": "[TODO Q2?]", "acceptedAnswer": { "@type": "Answer", "text": "[TODO 40-60 word answer]" } },
          { "@type": "Question", "name": "[TODO Q3?]", "acceptedAnswer": { "@type": "Answer", "text": "[TODO 40-60 word answer]" } },
          { "@type": "Question", "name": "[TODO Q4?]", "acceptedAnswer": { "@type": "Answer", "text": "[TODO 40-60 word answer]" } },
          { "@type": "Question", "name": "[TODO Q5?]", "acceptedAnswer": { "@type": "Answer", "text": "[TODO 40-60 word answer]" } }
        ]'''
t = re.sub(r'"mainEntity": \[.*?\]', ld_faq, t, count=1, flags=re.S)

target.write_text(t)
print(f"Created blog/{slug}.html")
print(f"Title: {title}")
print(f"Date:  {today}")
print()
print("Next steps:")
print(f"  1. Fill in [TODO] markers in blog/{slug}.html")
print(f"  2. Add to sitemap.xml:")
print(f'     <url><loc>https://www.loopworker.com/blog/{slug}.html</loc><lastmod>{today}</lastmod><changefreq>monthly</changefreq><priority>0.65</priority></url>')
print(f"  3. Add to blog/index.html article card grid")
