#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).parent
BLOG_DIR = ROOT / "blog"


PAGES = {
    "done-for-you-social-media-content.html": {
        "subtitle": "Done-for-you social media content should remove production bottlenecks, improve visual quality, and give the business a consistent publishing rhythm without requiring a full in-house team. This guide explains what it includes, what it costs, and who it actually fits.",
        "cta": "Need done-for-you content that looks like your brand instead of outsourced filler? Start with a free audit.",
        "replacements": [
            ('What "Done-For-You" Actually Means', 'What does "done-for-you social media content" actually mean?'),
            ("Who Done-For-You Content Is Actually For", "Who is done-for-you social media content actually for?"),
            ("What It Costs (Honest Numbers)", "What does done-for-you social media content actually cost?"),
            ("The Process: What to Expect After You Sign Up", "What should you expect after signing up for a done-for-you service?"),
            ("How to Tell If It's Working", "How do you tell if done-for-you social media content is working?"),
            ("Questions to Ask Before You Hire", "What questions should you ask before hiring a done-for-you content service?"),
        ],
    },
    "hire-social-media-content-creator.html": {
        "subtitle": "Hiring a content creator works best when you know what outputs you need, what quality bar matters, and whether you are really buying content production or broader account management. This guide shows how to make that hire without wasting money.",
        "cta": "Need a clearer content scope before you hire anyone? Start with a free audit.",
        "replacements": [
            ("Why Most Business Owners Get This Wrong", "Why do most business owners get this hire wrong?"),
            ("What a Content Creator Should Actually Deliver", "What should a social media content creator actually deliver?"),
            ("The Four Options (and What Each Really Costs)", "What hiring options are available and what does each one cost?"),
            ("What to Look for (and What to Avoid)", "What should you look for and avoid when hiring a content creator?"),
            ("How to Evaluate Quality", "How should you evaluate a content creator's quality?"),
            ("Timeline Expectations", "What timeline should you expect from a content creator?"),
            ("How Much Should You Actually Pay?", "How much should you actually pay a social media content creator?"),
        ],
    },
    "outsource-social-media-small-business.html": {
        "subtitle": "Outsourcing social media makes sense when the owner is the bottleneck, the brand already knows what it sells, and someone else can run the content system more consistently than the business can in-house. This guide shows how to decide and how to hand it off cleanly.",
        "cta": "Need a cleaner handoff before you outsource social media? Start with a free audit.",
        "replacements": [
            ("5 Signs It's Time to Outsource", "What signs show it's time to outsource social media?"),
            ("What Outsourcing Actually Looks Like", "What does outsourcing social media actually look like?"),
            ('"Nobody Can Do It Like Me" (Addressing the Fear)', 'How do you get past the fear that nobody can do it like you?'),
            ("The Handoff Process", "What should the social media handoff process look like?"),
            ("How to Measure If It's Working", "How do you measure whether outsourced social media is working?"),
        ],
    },
    "how-to-build-a-brand-from-scratch.html": {
        "opening": "Building a brand from scratch means locking positioning, naming, visual identity, imagery, content, and launch order into one system instead of designing random assets in isolation. This guide walks through that sequence step by step.",
        "cta": "Need your brand built as a system instead of piecemeal assets? Start with a free audit.",
        "replacements": [
            ("Step 1: Brand Positioning (Before You Touch Design)", "How should you define brand positioning before touching design?"),
            ("Step 2: Naming Your Brand", "How should you name a brand from scratch?"),
            ("Step 3: Visual Identity Foundation", "How do you build the visual identity foundation of a brand?"),
            ("Step 4: Brand Photography", "How should you approach brand photography when building from scratch?"),
            ("Step 5: Content Strategy", "What content strategy should a new brand build first?"),
            ("Step 6: The Launch Plan", "What should a new brand launch plan include?"),
            ("The AI-Accelerated Timeline", "What does an AI-accelerated brand-building timeline look like?"),
            ("Common Brand-Building Mistakes", "What brand-building mistakes should you avoid?"),
            ("What Comes After Launch", "What should happen after a brand launch?"),
        ],
    },
    "how-to-grow-instagram-followers-organically.html": {
        "opening": "Organic Instagram growth comes from a profile that converts, content that earns discovery, and a consistency system that keeps publishing long enough for compounding to happen. This guide breaks down each piece without relying on bots or fake growth hacks.",
        "cta": "Need Instagram growth tied to content quality and conversion instead of shortcuts? Start with a free audit.",
        "replacements": [
            ("Why Organic Growth Still Matters in 2026", "Why does organic Instagram growth still matter in 2026?"),
            ("Step 1: Optimize Your Profile for Conversion", "How should you optimize your Instagram profile for conversion?"),
            ("Step 2: Build a Content Strategy That Attracts Followers", "What content strategy attracts Instagram followers organically?"),
            ("Step 3: Master Reels for Maximum Discovery", "How do Reels drive organic Instagram discovery?"),
            ("Step 4: Hashtag Strategy That Actually Works", "What hashtag strategy actually works for Instagram?"),
            ("Step 5: Engagement Strategy (The Part Everyone Skips)", "What engagement strategy do most people skip on Instagram?"),
            ("Step 6: Collaboration Strategy", "What collaboration strategy helps Instagram grow organically?"),
            ("Step 7: Build a Consistency System", "How do you build a consistency system for Instagram growth?"),
            ("Common Mistakes That Kill Organic Growth", "What mistakes kill organic Instagram growth?"),
            ("The Timeline: What to Expect", "What timeline should you expect for organic Instagram growth?"),
            ("Organic Growth Is a System, Not a Hack", "Why is organic Instagram growth a system, not a hack?"),
        ],
    },
    "start-content-creation-business-with-ai.html": {
        "subtitle": "Starting an AI-enabled content business works when the offer is positioned as premium production leverage rather than cheap automation. This guide covers the service mix, tool stack, pricing, and client path that make that model viable.",
        "cta": "Need help packaging an AI-enabled content offer so it sells above commodity pricing? Start with a free audit.",
        "replacements": [
            ("The Opportunity: Why Now", "Why is now a strong time to start an AI content-creation business?"),
            ("Services to Offer", "What services should an AI content-creation business offer?"),
            ("The AI Tool Stack", "What AI tool stack should a content-creation business use?"),
            ("Pricing Your Services: The Premium Positioning", "How should you price AI content services without looking cheap?"),
            ("Finding Your First Clients", "How do you find your first clients for an AI content business?"),
            ("Scaling Without Hiring", "How do you scale an AI content business without hiring immediately?"),
            ("Positioning: Premium, Not Cheap", "How should you position an AI content business as premium?"),
            ("Month-by-Month Roadmap", "What month-by-month roadmap should a new AI content business follow?"),
            ("The Bottom Line", "What is the bottom line on starting an AI content business?"),
        ],
    },
    "ai-photo-enhancement-iphone.html": {
        "subtitle": "AI iPhone photo enhancement works best as a workflow improvement layer: clean capture, targeted enhancement, platform-specific export, and only occasional reshoots when the source image is fundamentally weak. This guide explains that system.",
        "cta": "Need your phone-photo workflow upgraded into something your brand can publish confidently? Start with a free audit.",
        "replacements": [
            ("The 4-Step Workflow", "What is the 4-step workflow for AI-enhancing iPhone photos?"),
            ("AI Enhancement Tools Compared", "How do the main AI photo-enhancement tools compare?"),
            ("What AI Can Fix", "What can AI actually fix in an iPhone photo?"),
            ("What AI Cannot Fix", "What can AI not fix in an iPhone photo?"),
            ("Workflows by Photo Type", "How should the workflow change by photo type?"),
            ("Cost Comparison: AI Enhancement vs. Reshoot", "How does AI enhancement compare to a reshoot on cost?"),
            ("Export Settings by Platform", "What export settings should you use by platform?"),
        ],
    },
    "salon-marketing-ideas.html": {
        "subtitle": "The best salon marketing ideas usually start with free retention and referral systems, then add low-cost content and local promotion before moving into heavier paid spend. This guide groups 25 ideas by cost so the rollout order is clear.",
        "cta": "Need salon content, referrals, and local visibility built into one growth system? Start with a free audit.",
        "replacements": [
            ("Free Strategies (10 Ideas &mdash; $0)", "What free salon marketing ideas should you start with?"),
            ("Under $50/Month Strategies (8 Ideas)", "What salon marketing ideas work under $50 per month?"),
            ("Investment Strategies (7 Ideas &mdash; $50+/month)", "What salon marketing ideas are worth paying for once the basics work?"),
            ("Phone Photography Tips for Salon Content", "How should a salon shoot better phone content?"),
        ],
    },
    "ecommerce-product-launch-checklist.html": {
        "subtitle": "An ecommerce launch succeeds when preparation, assets, platform setup, launch-week activity, and post-launch follow-up happen in the right order. This checklist groups the 30 steps by phase so nothing critical gets skipped.",
        "cta": "Need launch assets, product visuals, and launch sequencing working together before you spend on traffic? Start with a free audit.",
        "replacements": [
            ("Phase 1: Pre-Launch (Steps 1-6)", "What should happen in ecommerce pre-launch steps 1 to 6?"),
            ("Phase 2: Content Creation (Steps 7-12)", "What should happen in ecommerce content-creation steps 7 to 12?"),
            ("Phase 3: Platform Setup (Steps 13-18)", "What should happen in ecommerce platform-setup steps 13 to 18?"),
            ("Phase 4: Launch Week (Steps 19-24)", "What should happen during ecommerce launch-week steps 19 to 24?"),
            ("Phase 5: Post-Launch (Steps 25-30)", "What should happen in ecommerce post-launch steps 25 to 30?"),
        ],
    },
    "ugc-content-guide-small-business.html": {
        "subtitle": "User-generated content works for a small business when it is encouraged deliberately, permissions are handled cleanly, and the resulting assets are repurposed across the full content system instead of left buried in tagged posts. This guide covers that process.",
        "cta": "Need UGC integrated into your content calendar instead of treated like random reposts? Start with a free audit.",
        "replacements": [
            ("Why UGC Outperforms Branded Content", "Why does UGC outperform branded content?"),
            ("7 Ways to Encourage Customer Content", "How can a small business encourage more customer content?"),
            ("How to Ask for Permission: 3 DM Scripts", "How should you ask permission to reuse customer content?"),
            ("Legal Considerations", "What legal considerations matter with UGC?"),
            ("How to Repurpose UGC Across Every Platform", "How should you repurpose UGC across platforms?"),
            ("UGC Content Calendar Integration", "How do you integrate UGC into a content calendar?"),
            ("Tools for Collecting UGC", "What tools help collect and manage UGC?"),
            ("Brands That Do UGC Right (And What to Steal)", "What can you learn from brands that do UGC well?"),
        ],
    },
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def replace_first(pattern: str, text: str, new_text: str) -> str:
    regex = re.compile(pattern, re.S)
    return regex.sub(lambda m: m.group(1) + new_text + m.group(2), text, count=1)


def replace_all(pattern: str, text: str, new_text: str) -> str:
    regex = re.compile(pattern, re.S)
    return regex.sub(lambda m: m.group(1) + new_text + m.group(2), text)


def set_subtitle(text: str, new_text: str) -> str:
    return replace_first(r'(<p class="[^"]*article-subtitle[^"]*"[^>]*>).*?(</p>)', text, new_text)


def set_opening_paragraph(text: str, new_text: str) -> str:
    pattern = re.compile(r'(<h1[^>]*>.*?</h1>\s*(?:<time[^>]*>.*?</time>\s*)?)(<p[^>]*>.*?</p>)', re.S)
    return pattern.sub(lambda m: m.group(1) + f"<p>{new_text}</p>", text, count=1)


def set_cta_paragraphs(text: str, new_text: str) -> str:
    return replace_all(
        r'(<div class="cta-(?:section|box)"[^>]*>\s*(?:<h[23][^>]*>.*?</h[23]>\s*)?<p>).*?(</p>)',
        text,
        new_text,
    )


def dedupe_consecutive_h2(text: str) -> str:
    pattern = re.compile(r'(<h2[^>]*>.*?</h2>)(?:\s*\1)+', re.S)
    while True:
        new_text = pattern.sub(r"\1", text)
        if new_text == text:
            return text
        text = new_text


def main() -> None:
    updated: list[str] = []
    missing: list[str] = []

    for filename, config in PAGES.items():
        path = BLOG_DIR / filename
        text = read(path)
        original = text

        if "subtitle" in config:
            new_text = set_subtitle(text, config["subtitle"])
            if new_text == text:
                missing.append(f"{filename}: subtitle not updated")
            text = new_text

        if "opening" in config:
            new_text = set_opening_paragraph(text, config["opening"])
            if new_text == text:
                missing.append(f"{filename}: opening paragraph not updated")
            text = new_text

        for old, new in config.get("replacements", []):
            if old not in text:
                missing.append(f"{filename}: missing pattern {old[:80]!r}")
                continue
            text = text.replace(old, new)

        if "cta" in config:
            new_text = set_cta_paragraphs(text, config["cta"])
            if new_text == text:
                missing.append(f"{filename}: CTA not updated")
            text = new_text

        text = dedupe_consecutive_h2(text)

        if text != original:
            write(path, text)
            updated.append(filename)

    print("Updated:")
    for name in updated:
        print(f"  - {name}")

    if missing:
        print("\nMissing:")
        for item in missing:
            print(f"  - {item}")


if __name__ == "__main__":
    main()
