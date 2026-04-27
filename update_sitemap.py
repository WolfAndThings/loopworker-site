#!/usr/bin/env python3
"""
Add all new blog posts to sitemap.xml for crawl prioritization.
Also generates a Google Search Console ping URL.
"""

import os
import glob
import re
from datetime import datetime

SITE_DIR = os.path.dirname(__file__)
BLOG_DIR = os.path.join(SITE_DIR, "blog")
SITEMAP_PATH = os.path.join(SITE_DIR, "sitemap.xml")

# Read existing sitemap
with open(SITEMAP_PATH, "r") as f:
    existing = f.read()

# Get all blog HTML files
blog_files = sorted(glob.glob(os.path.join(BLOG_DIR, "*.html")))

# Extract existing URLs from sitemap
existing_urls = set(re.findall(r'<loc>(.*?)</loc>', existing))

# Find new blog posts not in sitemap
new_entries = []
for filepath in blog_files:
    filename = os.path.basename(filepath)
    if filename == "index.html":
        continue
    url = f"https://www.loopworker.com/blog/{filename}"
    if url not in existing_urls:
        # Try to extract publish date from the file
        with open(filepath, "r") as f:
            content = f.read()
        date_match = re.search(r'article:published_time.*?content="(\d{4}-\d{2}-\d{2})"', content)
        pub_date = date_match.group(1) if date_match else "2026-04-14"
        new_entries.append((url, pub_date))

if not new_entries:
    print("No new blog posts to add to sitemap.")
    exit()

# Build new sitemap entries
new_xml = ""
for url, date in new_entries:
    new_xml += f"""  <url>
    <loc>{url}</loc>
    <lastmod>{date}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
"""

# Insert before closing </urlset>
updated = existing.replace("</urlset>", new_xml + "</urlset>")

with open(SITEMAP_PATH, "w") as f:
    f.write(updated)

print(f"Added {len(new_entries)} new blog posts to sitemap.xml")
print(f"Total sitemap URLs: {len(existing_urls) + len(new_entries)}")
print()
print("=== CRAWL PRIORITY STEPS ===")
print()
print("1. SUBMIT SITEMAP to Google Search Console:")
print("   https://search.google.com/search-console → Sitemaps → Add sitemap.xml")
print()
print("2. PING Google with updated sitemap:")
print("   https://www.google.com/ping?sitemap=https://www.loopworker.com/sitemap.xml")
print()
print("3. REQUEST INDEXING for highest-priority pages in Search Console:")
print("   URL Inspection → Enter URL → Request Indexing")
print()
print("   Priority URLs to submit first (highest search volume keywords):")
priority_slugs = [
    "brewery-marketing-guide",
    "pilates-studio-marketing",
    "crossfit-gym-marketing",
    "hvac-marketing-guide",
    "plumber-marketing-guide",
    "daycare-marketing-guide",
    "social-media-content-creation-cost",
    "google-ads-cost-local-business",
    "google-ads-vs-meta-ads-local-business",
    "seo-vs-ppc-for-local-business",
    "why-your-social-media-is-not-getting-customers",
    "the-90-day-marketing-sprint",
    "how-to-create-instagram-reels-for-business",
    "how-to-respond-to-negative-reviews",
    "ai-content-strategy-local-business",
]
for slug in priority_slugs:
    print(f"   - https://www.loopworker.com/blog/{slug}.html")
print()
print("4. INTERNAL LINKING is already handled — each post links to 4 related existing posts.")
print("5. BLOG INDEX PAGE needs updating — run update_blog_index.py next.")
