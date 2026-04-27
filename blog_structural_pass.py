#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).parent
BLOG_DIR = ROOT / "blog"
QUEUE_PATH = ROOT / "BLOG_PAGERANK_QUEUE.tsv"
GAPS_JSON_PATH = ROOT / "BLOG_SCHEMA_SUPPORT_GAPS.json"
GAPS_MD_PATH = ROOT / "BLOG_SCHEMA_SUPPORT_GAPS.md"
SKIPS_PATH = ROOT / "BLOG_STRUCTURAL_SKIPS.md"

TOP_15 = {
    "ai-brand-photography-cost.html",
    "ai-photography-prompts-that-dont-look-ai.html",
    "ai-vs-traditional-product-photography.html",
    "ai-brand-photography-vs-stock-photos.html",
    "build-brand-identity-with-ai.html",
    "content-calendar-template-small-business.html",
    "ecommerce-ai-product-photos.html",
    "how-to-automate-instagram-posting.html",
    "hiring-photographer-vs-ai-photography.html",
    "how-to-create-brand-style-guide-ai.html",
    "ai-content-automation-small-business.html",
    "ai-photography-for-personal-brands.html",
    "ai-product-photography-amazon-sellers.html",
    "restaurant-ai-photography.html",
    "social-media-content-strategy-small-business.html",
}


def blog_files() -> list[Path]:
    return sorted(p for p in BLOG_DIR.glob("*.html") if p.name != "index.html")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text)).strip()


def get_title(text: str, fallback: str) -> str:
    m = re.search(r"<title>(.*?)</title>", text, re.S | re.I)
    return clean_text(m.group(1)) if m else fallback


def extract_h2s(text: str) -> list[str]:
    return [
        clean_text(m.group(1))
        for m in re.finditer(r"<h2[^>]*>(.*?)</h2>", text, re.S | re.I)
    ]


def extract_links(text: str) -> list[str]:
    return [m.group(1) for m in re.finditer(r'<a[^>]+href=["\']([^"\']+)["\']', text, re.I)]


def norm_href(href: str, from_rel: str, valid: set[str]) -> str | None:
    href = href.strip()
    if href.startswith(("mailto:", "tel:", "javascript:")):
        return None
    if re.match(r"^https?://", href, re.I):
        try:
            from urllib.parse import urlparse

            parsed = urlparse(href)
        except Exception:
            return None
        if not parsed.hostname or not parsed.hostname.endswith("loopworker.com"):
            return None
        href = parsed.path
    href = href.split("#", 1)[0].split("?", 1)[0]
    if not href:
        return None
    if href.startswith("/"):
        rel = href[1:]
    else:
        rel = str((Path(from_rel).parent / href).as_posix())
    if rel.endswith("/"):
        rel += "index.html"
    if rel == "":
        rel = "index.html"
    if not rel.endswith(".html"):
        return None
    return rel if rel in valid else None


def compute_pagerank() -> list[dict]:
    all_html = sorted(ROOT.rglob("*.html"))
    rels = [str(p.relative_to(ROOT).as_posix()) for p in all_html if ".git/" not in str(p)]
    valid = set(rels)
    out_links: dict[str, list[str]] = {}
    in_counts = Counter({rel: 0 for rel in rels})

    for rel in rels:
        text = read(ROOT / rel)
        targets = sorted(
            {
                t
                for href in extract_links(text)
                if (t := norm_href(href, rel, valid)) and t != rel
            }
        )
        out_links[rel] = targets
        for target in targets:
            in_counts[target] += 1

    blog_nodes = [rel for rel in rels if rel.startswith("blog/") and rel != "blog/index.html"]
    n = len(blog_nodes)
    damping = 0.85
    pr = {node: 1 / n for node in blog_nodes}

    blog_set = set(blog_nodes)
    for _ in range(60):
        next_pr = {node: (1 - damping) / n for node in blog_nodes}
        for src in rels:
            outs = [t for t in out_links.get(src, []) if t in blog_set]
            if not outs:
                continue
            share = damping * pr.get(src, 0) / len(outs)
            for target in outs:
                next_pr[target] += share
        pr = next_pr

    rows = []
    for rel in blog_nodes:
        path = ROOT / rel
        text = read(path)
        rows.append(
            {
                "rel": rel,
                "slug": Path(rel).name,
                "pr": pr.get(rel, 0.0),
                "in_links": in_counts[rel],
                "title": get_title(text, rel),
            }
        )
    rows.sort(key=lambda row: row["pr"], reverse=True)
    return rows


def write_queue(rows: list[dict]) -> None:
    lines = ["rank\tpath\tpagerank\tin_links\ttitle"]
    for idx, row in enumerate(rows, start=1):
        lines.append(
            f"{idx}\t{row['rel']}\t{row['pr']:.6f}\t{row['in_links']}\t{row['title']}"
        )
    write(QUEUE_PATH, "\n".join(lines) + "\n")


def related_choices(slug: str) -> list[tuple[str, str]]:
    s = slug.replace(".html", "")

    if re.search(r"(restaurant|pizza|bbq|bar|vegan|food-truck|bakery|brunch|sushi|food|cocktail)", s):
        return [
            ("/blog/restaurant-social-media-strategy.html", "Restaurant Social Media Strategy"),
            ("/blog/restaurant-instagram-content-ideas.html", "Restaurant Instagram Content Ideas"),
            ("/blog/restaurant-ai-photography.html", "AI Photography for Restaurants"),
            ("/blog/food-photography-tips-phone.html", "Food Photography Tips with Your Phone"),
        ]

    if re.search(r"(google-business-profile|google-reviews|local-seo|yelp|local-business|google-business-profile-posts)", s):
        return [
            ("/blog/google-business-profile-optimization.html", "Google Business Profile Optimization"),
            ("/blog/how-to-get-more-google-reviews.html", "How to Get More Google Reviews"),
            ("/blog/local-seo-guide-small-business.html", "Local SEO Guide for Small Business"),
            ("/blog/yelp-optimization-guide.html", "Yelp Optimization Guide"),
        ]

    if re.search(r"(n8n|zapier|make|automation|batch|repurposing|email-marketing)", s):
        return [
            ("/blog/ai-content-automation-small-business.html", "AI Content Automation for Small Business"),
            ("/blog/how-to-automate-instagram-posting.html", "How to Automate Instagram Posting"),
            ("/blog/how-to-batch-content-creation.html", "How to Batch Content Creation"),
            ("/blog/content-repurposing-strategy.html", "Content Repurposing Strategy"),
        ]

    if re.search(r"(instagram|reel|carousel|captions|followers|engagement|clients-on-instagram|visual-brand)", s):
        return [
            ("/blog/social-media-content-strategy-small-business.html", "Social Media Content Strategy for Small Business"),
            ("/blog/content-calendar-template-small-business.html", "Free Content Calendar Template for Small Business"),
            ("/blog/how-to-batch-content-creation.html", "How to Batch Content Creation"),
            ("/blog/how-to-write-instagram-captions.html", "How to Write Instagram Captions"),
        ]

    if re.search(r"(product|amazon|ecommerce|lighting|shopify)", s):
        return [
            ("/blog/ecommerce-ai-product-photos.html", "AI Product Photography for E-commerce"),
            ("/blog/ai-product-photography-amazon-sellers.html", "AI Product Photography for Amazon Sellers"),
            ("/blog/ai-vs-traditional-product-photography.html", "AI vs Traditional Product Photography"),
            ("/blog/how-to-take-product-photos-with-phone.html", "How to Take Product Photos with Your Phone"),
        ]

    if re.search(r"(brand|branding|agency|style-guide|stock|headshots|midjourney|fashion|personal-brands|photography)", s):
        return [
            ("/blog/ai-brand-photography-cost.html", "How Much Does AI Brand Photography Actually Cost?"),
            ("/blog/build-brand-identity-with-ai.html", "How to Build a Complete Brand Identity Using AI in 7 Days"),
            ("/blog/how-to-create-brand-style-guide-ai.html", "How to Create a Brand Style Guide with AI"),
            ("/blog/ai-photography-prompts-that-dont-look-ai.html", "50 AI Photography Prompts That Don't Look Like AI"),
        ]

    return [
        ("/blog/social-media-content-strategy-small-business.html", "Social Media Content Strategy for Small Business"),
        ("/blog/content-calendar-template-small-business.html", "Free Content Calendar Template for Small Business"),
        ("/blog/ai-content-automation-small-business.html", "AI Content Automation for Small Business"),
        ("/blog/how-to-batch-content-creation.html", "How to Batch Content Creation"),
    ]


def build_related_block(slug: str) -> str:
    choices = [item for item in related_choices(slug) if Path(item[0]).name != slug][:4]
    links = "\n".join(
        f'        <li><a href="{href}">{label}</a></li>' for href, label in choices
    )
    return (
        "    <h2>Related Reading</h2>\n"
        "    <ul>\n"
        f"{links}\n"
        "    </ul>\n\n"
    )


def fix_phrase_corruption(text: str) -> str:
    replacements = [
        (r"\bA I create done-for-you content\b", "A brand photography system"),
        (r"\bAn I create done-for-you content\b", "A brand photography system"),
        (r"\ba I create done-for-you content\b", "a brand photography system"),
        (r"\ban I create done-for-you content\b", "a brand photography system"),
        (r"\bthe I create done-for-you content\b", "the brand photography system"),
        (r"\bThe I create done-for-you content\b", "The brand photography system"),
        (r"\byour I create done-for-you content\b", "your brand photography system"),
        (r"\bTheir I create done-for-you content\b", "Their brand photography system"),
        (r"\btheir I create done-for-you content\b", "their brand photography system"),
        (r"\bI create done-for-you contents\b", "brand photography systems"),
        (r"\bI create done-for-you content\b", "brand photography systems"),
    ]
    updated = text
    for pattern, replacement in replacements:
        updated = re.sub(pattern, replacement, updated)
    return updated


def insert_related_block(text: str, slug: str) -> tuple[str, bool]:
    if "Related Reading" in text:
        return text, False
    block = build_related_block(slug)
    if '<div class="cta-section">' in text:
        return text.replace('<div class="cta-section">', block + '    <div class="cta-section">', 1), True
    if '<div class="cta-box">' in text:
        return text.replace('<div class="cta-box">', block + '    <div class="cta-box">', 1), True
    if "</article>" in text:
        return text.replace("</article>", block + "</article>", 1), True
    return text, False


def structural_pass() -> dict:
    rows = compute_pagerank()
    write_queue(rows)
    skip_notes: list[str] = []
    fix_counts = Counter()

    for row in rows:
        slug = row["slug"]
        if slug in TOP_15:
            continue

        path = BLOG_DIR / slug
        text = read(path)
        original = text

        new_text = text.replace("https://loopworker.com/", "https://www.loopworker.com/")
        if new_text != text:
            fix_counts["normalized_www"] += 1
            text = new_text

        new_text = fix_phrase_corruption(text)
        if new_text != text:
            fix_counts["fixed_bad_phrase_files"] += 1
            fix_counts["fixed_bad_phrase_hits"] += len(
                re.findall(r"I create done-for-you content", text)
            )
            text = new_text

        new_text, inserted = insert_related_block(text, slug)
        if inserted:
            fix_counts["added_related"] += 1
            text = new_text
        elif "Related Reading" not in text:
            skip_notes.append(f"- {slug}: no safe insertion point for Related Reading")

        if text != original:
            write(path, text)

    gaps = []
    counts = Counter()
    for row in rows:
        slug = row["slug"]
        text = read(BLOG_DIR / slug)
        h2s = extract_h2s(text)
        q_h2 = sum(1 for h in h2s if "?" in h)
        item = {
            "path": f"blog/{slug}",
            "pagerank": round(row["pr"], 6),
            "in_links": row["in_links"],
            "has_faq": '"@type": "FAQPage"' in text,
            "has_breadcrumb": '"@type": "BreadcrumbList"' in text,
            "has_speakable": "SpeakableSpecification" in text,
            "has_related": "Related Reading" in text,
            "question_h2_count": q_h2,
            "h2_count": len(h2s),
        }
        gaps.append(item)
        if not item["has_faq"]:
            counts["missing_faq"] += 1
        if not item["has_breadcrumb"]:
            counts["missing_breadcrumb"] += 1
        if not item["has_speakable"]:
            counts["missing_speakable"] += 1
        if not item["has_related"]:
            counts["missing_related"] += 1
        if item["question_h2_count"] == 0:
            counts["zero_question_h2"] += 1

    write(GAPS_JSON_PATH, json.dumps({"counts": counts, "posts": gaps}, indent=2) + "\n")

    md_lines = [
        "# Blog Schema And Support Gaps",
        "",
        "## Counts",
        "",
    ]
    for key in ["missing_faq", "missing_breadcrumb", "missing_speakable", "missing_related", "zero_question_h2"]:
        md_lines.append(f"- `{key}`: {counts.get(key, 0)}")

    md_lines.extend(["", "## Remaining Gaps By Post", ""])
    for item in gaps:
        issues = []
        if not item["has_faq"]:
            issues.append("missing FAQ")
        if not item["has_breadcrumb"]:
            issues.append("missing breadcrumb")
        if not item["has_speakable"]:
            issues.append("missing speakable")
        if not item["has_related"]:
            issues.append("missing related")
        if item["question_h2_count"] == 0:
            issues.append("no question H2s")
        if issues:
            md_lines.append(
                f"- `{item['path']}`: {', '.join(issues)}"
            )
    write(GAPS_MD_PATH, "\n".join(md_lines) + "\n")

    if not skip_notes:
        skip_notes = ["# Structural Skips", "", "- None"]
    else:
        skip_notes = ["# Structural Skips", ""] + skip_notes
    write(SKIPS_PATH, "\n".join(skip_notes) + "\n")

    return {"fix_counts": fix_counts, "gap_counts": counts}


if __name__ == "__main__":
    result = structural_pass()
    print(json.dumps(result, indent=2))
