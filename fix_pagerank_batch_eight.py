#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).parent
BLOG_DIR = ROOT / "blog"


PAGES = {
    "instagram-vs-tiktok-small-business.html": {
        "subtitle": "For most small businesses, the right Instagram-versus-TikTok choice comes down to audience behavior, conversion path, content workload, and whether the brand needs discovery or trust first. This guide shows how to make that decision without trying to force both platforms at once.",
        "cta": "Need a platform strategy that matches your business instead of generic creator advice? Start with a free audit.",
        "replacements": [
            ("Audience Demographics: Who's Actually There", "Which audience is actually on Instagram versus TikTok?"),
            ("Algorithm Behavior: Completely Different Games", "How do Instagram and TikTok algorithms work differently?"),
            ("Organic Reach: TikTok Has the Edge (With Caveats)", "Which platform gives small businesses better organic reach?"),
            ("Conversion Rates: Instagram Wins for Most Businesses", "Which platform converts better for most small businesses?"),
            ("Content Creation Effort: Instagram Is More Efficient", "Which platform is more efficient to create content for?"),
            ("Which Industries Win Where", "Which industries tend to win on each platform?"),
            ("The Ad Platform Comparison", "How do the ad platforms compare?"),
            ("The Biggest Mistake: Trying to Do Both Badly", "What is the biggest mistake businesses make with Instagram and TikTok?"),
            ("How to Pick: The Decision Framework", "How should you decide between Instagram and TikTok?"),
            ("Building a Visual Brand on Your Chosen Platform", "How do you build a visual brand on the platform you choose?"),
            ("The Verdict", "What is the verdict for most small businesses?"),
        ],
    },
    "how-to-get-testimonials-from-clients.html": {
        "opening": "Getting testimonials from clients works when the ask happens at the right moment, the format is easy to complete, and the result gets reused across sales pages, proposals, email, and social content instead of sitting in a folder. This guide shows how to make that process repeatable.",
        "cta": "Need stronger proof assets woven into your content and sales flow? Start with a free audit.",
        "replacements": [
            ("Why Testimonials Matter More Than You Think", "Why do testimonials matter so much?"),
            ("When to Ask: The Timing That Changes Everything", "When should you ask for a testimonial?"),
            ("How to Ask: Scripts That Actually Work", "How should you ask for a testimonial?"),
            ("Video vs. Written: Which Format Wins", "Should you ask for video or written testimonials?"),
            ("Testimonial Templates Your Clients Can Steal", "What testimonial templates can clients use?"),
            ("Where to Display Testimonials for Maximum Impact", "Where should you display testimonials for the most impact?"),
            ("Automating the Ask So You Never Forget", "How do you automate testimonial requests?"),
            ("Turning Testimonials Into Content", "How do you turn testimonials into content?"),
            ("Common Mistakes That Kill Your Testimonial Game", "What testimonial mistakes should you avoid?"),
            ("The Testimonial Flywheel", "What does a testimonial flywheel look like?"),
        ],
    },
    "ai-tools-for-photographers.html": {
        "opening": "AI tools help photographers when they remove repetitive editing, accelerate proofing, support concepting, and automate admin without replacing judgment, taste, or client trust. This guide focuses on where the time savings are real and where the hype is not.",
        "cta": "Need a photography workflow that uses AI as leverage without making the work feel generic? Start with a free audit.",
        "replacements": [
            ("AI Editing Tools: Where the Time Savings Are Real", "Which AI editing tools actually save photographers time?"),
            ("Background Removal and Compositing", "How can AI help with background removal and compositing?"),
            ("AI Upscaling and Enhancement", "How does AI help with upscaling and enhancement?"),
            ("Client Proofing and Gallery Delivery", "How can AI improve client proofing and gallery delivery?"),
            ("Portfolio Generation and Concept Testing", "How can AI help with portfolio generation and concept testing?"),
            ("Workflow Automation Beyond Editing", "What workflow automation can photographers use beyond editing?"),
            ("Pricing AI-Enhanced Services Higher, Not Lower", "How should photographers price AI-enhanced services?"),
            ("Tools to Avoid and Common Traps", "Which AI tools and traps should photographers avoid?"),
            ("Building Your AI-Enhanced Workflow", "How do you build an AI-enhanced photography workflow?"),
            ("The Future Is Hybrid", "Why is the future of photography hybrid?"),
        ],
    },
    "climbing-gym-marketing.html": {
        "subtitle": "Climbing gym marketing works when beginner acquisition, community retention, local partnerships, youth programming, and approachable brand positioning all reinforce each other instead of running as disconnected tactics. This guide lays out that growth system.",
        "cta": "Need a climbing gym marketing system that makes the sport feel approachable and keeps members engaged? Start with a free audit.",
        "replacements": [
            ("Beginner Outreach: Your Biggest Growth Lever", "How should a climbing gym market to beginners?"),
            ("Community Events That Build Loyalty", "What community events build loyalty for climbing gyms?"),
            ("Social Media for Climbing Gyms", "What social media strategy works for climbing gyms?"),
            ("Local Partnerships", "What local partnerships help a climbing gym grow?"),
            ("Youth Programs: The Long Game", "How do youth programs support long-term climbing gym growth?"),
            ("Making Climbing Feel Accessible", "How do you make climbing feel accessible in your marketing?"),
        ],
    },
    "fitness-studio-instagram-strategy.html": {
        "subtitle": "A fitness studio Instagram strategy works when class energy, instructor personality, member proof, and trial-offer content all point toward one goal: getting followers to book a first visit and come back. This guide shows how to structure that feed.",
        "cta": "Need a fitness studio Instagram system that sells the class experience instead of just posting harder? Start with a free audit.",
        "replacements": [
            ("Class Energy Reels: Your Best Marketing Asset", "Why are class-energy Reels a fitness studio's best marketing asset?"),
            ("Instructor Content: Your Secret Weapon", "How should instructor content support a fitness studio Instagram strategy?"),
            ("Member Stories That Convert", "What member-story content actually converts?"),
            ("Trial Offer Content", "How should studios post trial-offer content?"),
            ("Building Community on Instagram", "How do fitness studios build community on Instagram?"),
            ("Weekly Content Schedule", "What should a weekly Instagram schedule look like for a fitness studio?"),
        ],
    },
    "gym-instagram-content-ideas.html": {
        "subtitle": "Gym Instagram content works when it mixes member proof, class energy, coach expertise, facility experience, and participation prompts instead of repeating generic workout shots. These ideas are grouped so the feed stays useful and varied.",
        "cta": "Need a gym content mix that turns Instagram into a membership channel instead of a photo dump? Start with a free audit.",
        "replacements": [
            ("Member Story Content", "What member-story content should gyms post?"),
            ("Class and Energy Content", "What class and energy content should gyms post?"),
            ("Trainer and Coach Content", "What trainer and coach content should gyms post?"),
            ("Facility and Experience Content", "What facility and experience content should gyms post?"),
            ("Engagement and Challenge Content", "What engagement and challenge content should gyms post?"),
            ("Motivational Content (Done Right)", "How should gyms do motivational content without sounding generic?"),
        ],
    },
    "gym-social-media-strategy.html": {
        "subtitle": "A gym social media strategy works when content pillars are clear, beginner friction is reduced, community proof outweighs empty facility shots, and posting frequency is sustainable enough to compound. This guide explains how to run that system.",
        "cta": "Need a gym content system built to attract beginners and convert them into members? Start with a free audit.",
        "replacements": [
            ("The 5 Content Pillars for Gyms", "What content pillars should a gym post consistently?"),
            ("Community Content vs. Facility Content", "How should gyms balance community content versus facility content?"),
            ("Member Spotlights That Actually Work", "What member spotlights actually work for gyms?"),
            ("Beginner-Friendly Hooks", "What beginner-friendly hooks attract new gym members?"),
            ("Posting Frequency and Schedule", "How often should a gym post and on what schedule?"),
            ("What to Stop Posting", "What should gyms stop posting on social media?"),
        ],
    },
    "how-much-does-social-media-management-cost.html": {
        "subtitle": "Social media management pricing only makes sense when you separate strategy, posting, community management, and content production into distinct scopes. This guide breaks down the real cost ranges so you can compare freelancers, agencies, in-house hires, and done-for-you content rationally.",
        "cta": "Need clearer scope before you spend on social media support? Start with a free audit.",
        "replacements": [
            ("Why Pricing Is So Confusing", "Why is social media management pricing so confusing?"),
            ("Content Creation vs. Social Media Management", "What is the difference between content creation and social media management?"),
            ("The Full Pricing Breakdown", "What does the full pricing breakdown look like?"),
            ("Freelancers ($500-2,000/month)", "What do freelancers usually charge for social media management?"),
            ("Agencies ($2,000-10,000/month)", "What do agencies usually charge for social media management?"),
            ("In-House Employee ($3,000-6,000/month)", "What does an in-house social media employee cost?"),
            ("DFY Content Packages ($300-1,500)", "What do done-for-you content packages cost?"),
            ("How to Calculate Your Real Budget", "How should you calculate your real social media budget?"),
            ("What Most Small Businesses Should Actually Do", "What should most small businesses actually do?"),
        ],
    },
    "social-media-help-for-small-business.html": {
        "subtitle": "Small-business social media help usually means one of four things: learn it yourself, hire an employee, hire an agency, or buy done-for-you content. This guide helps you decide which option fits your stage, budget, and actual bottleneck.",
        "cta": "Need help choosing the right level of social media support before you waste budget? Start with a free audit.",
        "replacements": [
            ("First, Let's Be Honest About the Problem", "What problem are small business owners actually trying to solve?"),
            ("Option 1: Learn It Yourself (Free, But Slow)", "Should you learn social media yourself?"),
            ("Option 2: Hire a Social Media Employee ($3,000-6,000/mo)", "Should you hire a social media employee?"),
            ("Option 3: Hire an Agency ($2,000-10,000/mo)", "Should you hire a social media agency?"),
            ("Option 4: Done-For-You Content Service ($300-1,500)", "Should you use a done-for-you content service?"),
            ("How to Figure Out Which Stage You're At", "How do you figure out which stage your business is in?"),
            ("The Content Creation vs. Management Distinction", "What is the difference between content creation and management?"),
            ("What to Look for in Any Social Media Help", "What should you look for in any social media help?"),
            ("The Real Cost of Doing Nothing", "What is the real cost of doing nothing?"),
        ],
    },
    "ai-background-removal-product-photos.html": {
        "subtitle": "AI background removal works when product cutouts are clean, batch workflows are predictable, and the removed assets can be reused across Amazon, Shopify, ads, and lifestyle composites without manual cleanup every time. This guide shows where the tools help and where they still fail.",
        "cta": "Need cleaner product photography workflows for marketplaces, ecommerce, and ads? Start with a free audit.",
        "replacements": [
            ("Why Clean Backgrounds Matter", "Why do clean product backgrounds matter?"),
            ("Free Tools Ranked", "Which free AI background-removal tools are worth using?"),
            ("Paid Tools for Higher Volume", "Which paid tools are better for higher-volume work?"),
            ("Step-by-Step Workflow", "What is the step-by-step workflow for AI background removal?"),
            ("Problem Products: When AI Struggles", "Which products cause AI background removal to struggle?"),
            ("Adding Lifestyle Backgrounds After Removal", "How do you add lifestyle backgrounds after removal?"),
            ("Batch Processing for E-Commerce Catalogs", "How should you batch-process background removal for ecommerce catalogs?"),
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
    pattern = re.compile(
        r'(<h1[^>]*>.*?</h1>\s*(?:<div class="meta"[^>]*>.*?</div>\s*)?(?:<time[^>]*>.*?</time>\s*)?)(<p[^>]*>.*?</p>)',
        re.S,
    )
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
