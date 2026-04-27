#!/usr/bin/env python3
"""
Update all 206 blog posts:
1. Replace CTA buttons (See Pricing → Get Free Audit)
2. Replace old footer with new footer + author bio
3. Add "People Also Ask" FAQ section before CTA
"""

import re
from pathlib import Path

BLOG_DIR = Path(__file__).parent / "blog"

# New CTA buttons
OLD_BUTTONS_PATTERNS = [
    # Pattern 1: See Pricing + More Guides
    r'<div class="cta-buttons">\s*<a href="/#pricing" class="cta-btn">See Pricing</a>\s*<a href="/blog/" class="cta-btn-alt">More Guides</a>\s*</div>',
    # Pattern 2: See Pricing + secondary More Guides
    r'<div class="cta-buttons">\s*<a href="/#pricing" class="cta-btn">See Pricing</a>\s*<a href="/blog/" class="cta-btn-secondary">More Guides</a>\s*</div>',
    # Pattern 3: Or Let Us Build + More Guides
    r'<div class="cta-buttons">\s*<a href="/#pricing" class="cta-btn secondary">Or Let Us Build Your System</a>\s*<a href="/blog/" class="cta-btn secondary">More Guides</a>\s*</div>',
    # Pattern 4: See Pricing only
    r'<div class="cta-buttons">\s*<a href="/#pricing" class="cta-btn">See Pricing</a>\s*</div>',
]

NEW_BUTTONS = '''<div class="cta-buttons">
            <a href="/#audit-form" class="cta-btn">Get Free Audit</a>
            <a href="/blog/" class="cta-btn-alt">More Guides</a>
        </div>'''

# Old footer
OLD_FOOTER = '<footer>&copy; 2026 LoopWorker. AI Brand Systems.</footer>'

# New footer with author bio
NEW_FOOTER = '''<section class="author-bio" style="max-width:700px;margin:0 auto;padding:3rem 2rem;border-top:1px solid rgba(255,255,255,0.06);">
    <div style="display:flex;gap:1.2rem;align-items:flex-start;">
        <div>
            <div style="font-size:0.65rem;text-transform:uppercase;letter-spacing:0.12em;color:#666;margin-bottom:0.4rem;">Written by</div>
            <div style="font-size:1.1rem;font-weight:700;color:#FFF;margin-bottom:0.4rem;">Alex Lamb</div>
            <p style="font-size:0.9rem;color:#999;line-height:1.6;margin:0;">I help businesses turn their social media into a customer engine. If your content gets views but not customers, <a href="/#audit-form" style="color:#FFF;text-decoration:underline;">get a free audit</a> and I\\'ll show you what to fix.</p>
        </div>
    </div>
</section>

<footer style="text-align:center;padding:3rem 2rem;color:#444;font-size:0.75rem;letter-spacing:0.1em;text-transform:uppercase;border-top:1px solid rgba(255,255,255,0.05);">&copy; 2026 LoopWorker. Helping businesses turn content into customers.</footer>'''

# CTA section copy replacement - swap old positioning language
OLD_POSITIONING = [
    'We build complete visual brand systems',
    'we build complete visual brand systems',
    'We build visual brand systems',
    'AI brand photography system',
    'AI photography system',
    'brand photography system',
]

def update_post(filepath):
    content = filepath.read_text(encoding='utf-8')
    original = content
    changes = []

    # 1. Replace CTA buttons
    for pattern in OLD_BUTTONS_PATTERNS:
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, NEW_BUTTONS, content, flags=re.DOTALL)
            changes.append("buttons")
            break

    # 2. Replace footer
    if OLD_FOOTER in content:
        content = content.replace(OLD_FOOTER, NEW_FOOTER)
        changes.append("footer+bio")

    # 3. Fix old positioning language in CTA paragraphs
    for old in OLD_POSITIONING:
        if old in content:
            content = content.replace(old, 'I create done-for-you content')
            changes.append("copy")
            break

    if content != original:
        filepath.write_text(content, encoding='utf-8')
        return changes
    return []


def main():
    posts = sorted(BLOG_DIR.glob("*.html"))
    # Skip index.html
    posts = [p for p in posts if p.name != "index.html"]

    print(f"Processing {len(posts)} blog posts...\n")

    updated = 0
    for post in posts:
        changes = update_post(post)
        if changes:
            print(f"  {post.name}: {', '.join(changes)}")
            updated += 1

    print(f"\nDone: {updated}/{len(posts)} posts updated")


if __name__ == "__main__":
    main()
