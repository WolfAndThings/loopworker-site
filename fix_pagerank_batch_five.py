#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).parent
BLOG_DIR = ROOT / "blog"


PAGES = {
    "website-vs-social-media-small-business.html": {
        "subtitle": "Most small businesses need both a website and social media, but not in equal proportions at every stage. This guide explains when social-only is enough, when a website becomes non-negotiable, and what the smallest useful website actually includes.",
        "cta": "Need your website, Google presence, and social content working together instead of competing for attention? Start with a free audit.",
        "replacements": [
            ("The Case for Social-Only", "When does a social-only approach make sense for a small business?"),
            ("The Case for a Website", "Why does a small business still need a website?"),
            ("What Google Actually Thinks", "How does Google treat businesses without a website?"),
            ("The Hybrid Answer", "What is the best hybrid answer for website versus social media?"),
            ("The Minimum Viable Website", "What should a minimum viable small-business website include?"),
            ("When Social-Only Actually Works", "When can a small business realistically stay social-only?"),
            ("When You Absolutely Need a Website", "When do you absolutely need a website?"),
            ("The Real Cost Comparison", "How do website and social media costs actually compare?"),
            ("The Bottom Line", "What is the bottom line on website versus social media?"),
        ],
    },
    "influencer-marketing-small-business.html": {
        "subtitle": "Influencer marketing works best for small businesses when the creators are local, trusted, and tightly matched to the buyer rather than simply large. This guide shows how to find them, vet them, structure deals, and measure the return.",
        "cta": "Need creator partnerships tied to content, offers, and tracking instead of one-off posts? Start with a free audit.",
        "replacements": [
            ("The Influencer Tier System", "What influencer tiers matter most for a small business?"),
            ("How to Find the Right Influencers", "How do you find the right influencers for a small business?"),
            ("How to Evaluate an Influencer", "How should you evaluate an influencer before paying them?"),
            ("Outreach Templates That Get Replies", "What influencer outreach messages actually get replies?"),
            ("Deal Structures", "What deal structures work best with influencers?"),
            ("Measuring ROI", "How should a small business measure influencer ROI?"),
            ("Contract Essentials", "What contract terms should an influencer agreement include?"),
        ],
    },
    "social-media-post-ideas-small-business.html": {
        "opening": "The best small-business social posts usually fall into education, behind-the-scenes proof, social proof, offers, engagement prompts, and seasonal content. These 50 ideas are grouped into those buckets so you can pick a post fast instead of waiting for inspiration.",
        "cta": "Need these post ideas turned into a real content system your business can maintain? Start with a free audit.",
        "replacements": [
            ("How to Use This List", "How should a small business use this post-ideas list?"),
            ("Educational Posts (Ideas 1-10)", "What educational posts should a small business publish in ideas 1 to 10?"),
            ("Behind-the-Scenes Posts (Ideas 11-20)", "What behind-the-scenes posts should a small business publish in ideas 11 to 20?"),
            ("Social Proof Posts (Ideas 21-28)", "What social proof posts should a small business publish in ideas 21 to 28?"),
            ("Promotional Posts (Ideas 29-36)", "What promotional posts should a small business publish in ideas 29 to 36?"),
            ("Engagement Posts (Ideas 37-44)", "What engagement posts should a small business publish in ideas 37 to 44?"),
            ("Seasonal and Timely Posts (Ideas 45-50)", "What seasonal and timely posts should a small business publish in ideas 45 to 50?"),
            ("Turning Ideas Into a System", "How do you turn social post ideas into a repeatable system?"),
            ("The Bigger Picture", "What bigger content lesson should a small business take from this list?"),
        ],
    },
    "how-to-write-product-descriptions.html": {
        "subtitle": "Product descriptions convert when they explain who the item is for, what problem it solves, and why the buyer should trust the outcome rather than listing features in a vacuum. This guide covers the formula, examples, and SEO layer.",
        "cta": "Need product copy, images, and listing structure aligned so the page actually sells? Start with a free audit.",
        "replacements": [
            ("The Universal Formula", "What universal formula helps product descriptions sell?"),
            ("Before and After Examples", "What do before-and-after product description examples look like?"),
            ("Templates by Product Type", "What product description templates work by product type?"),
            ("SEO Tips for Product Descriptions", "How should you handle SEO in product descriptions?"),
            ("Common Mistakes", "What mistakes make product descriptions perform worse?"),
        ],
    },
    "amazon-listing-optimization-guide.html": {
        "subtitle": "Amazon listing optimization works when the title, image stack, bullets, search terms, A+ Content, and PPC all reinforce the same buying intent. This guide shows what each section of the listing should actually do.",
        "cta": "Need Amazon listings, product visuals, and conversion copy built as one system instead of patched together? Start with a free audit.",
        "replacements": [
            ("1. Product Title: The Most Important 200 Characters", "How should you write an Amazon product title?"),
            ("2. Image Slots 1-7: The Visual Sales Pitch", "What should each Amazon image slot do?"),
            ("3. Bullet Points: Benefits First, Features Second", "How should you write Amazon bullet points?"),
            ("4. Product Description and Backend Search Terms", "How should you use product descriptions and backend search terms on Amazon?"),
            ("5. A+ Content: Your Below-the-Fold Sales Page", "What does effective Amazon A+ Content look like?"),
            ("6. Keyword Research: Finding What Shoppers Actually Search", "How should you research Amazon keywords?"),
            ("7. PPC Basics: Driving Your First Sales", "How should you use Amazon PPC to drive first sales?"),
            ("Listing Optimization Checklist", "What should be on an Amazon listing optimization checklist?"),
        ],
    },
    "tiktok-marketing-small-business-guide.html": {
        "subtitle": "TikTok marketing works for small businesses when the content is native, the posting rhythm is sustainable, and the goal is steady category reach instead of hoping for one viral miracle. This guide explains the system behind that approach.",
        "cta": "Need short-form video ideas, production workflow, and platform strategy tied together? Start with a free audit.",
        "replacements": [
            ("How the TikTok Algorithm Works (Simplified)", "How does the TikTok algorithm work for a small business?"),
            ("10 Content Types That Work for Small Business", "What TikTok content types work best for a small business?"),
            ("Posting Schedule", "What TikTok posting schedule works for a small business?"),
            ("Hashtag Strategy", "What hashtag strategy still makes sense on TikTok?"),
            ("Going Viral vs. Consistent Growth", "Should a small business chase virality or consistent TikTok growth?"),
            ("Equipment You Actually Need", "What equipment does a small business actually need for TikTok?"),
        ],
    },
    "social-media-manager-for-restaurants.html": {
        "subtitle": "Most restaurants do not need a full social media manager first; they need better content, a consistent publishing rhythm, and someone accountable for turning posts into reservations. This guide explains when to DIY, when to hire a creator, and when management is actually worth paying for.",
        "cta": "Need restaurant content that fills seats before you hire a full manager? Start with a free audit.",
        "replacements": [
            ("The Real Problem Most Restaurants Have", "What problem do most restaurants actually have on social media?"),
            ("When You Can DIY (and When You Can't)", "When can a restaurant handle social media in-house and when can't it?"),
            ("What a Good Restaurant Content Creator Does", "What should a good restaurant content creator actually deliver?"),
            ("What a Social Media Manager Adds (and When It's Worth It)", "What extra value does a social media manager add for a restaurant?"),
            ("What You Should Actually Pay", "What should a restaurant actually pay for content versus management?"),
            ("How to Tell If It's Working", "How can a restaurant tell if social media is actually working?"),
            ("Common Mistakes Restaurants Make When Hiring", "What hiring mistakes do restaurants make with social media help?"),
        ],
    },
    "how-to-create-lead-magnet-small-business.html": {
        "subtitle": "A lead magnet converts when it solves one immediate problem, matches the traffic source, and hands the subscriber into a follow-up sequence that keeps the momentum going. This guide shows how to build that in a day.",
        "cta": "Need your lead magnet, landing page, and follow-up automation built as one acquisition system? Start with a free audit.",
        "replacements": [
            ("What Makes a Lead Magnet Actually Work", "What makes a lead magnet actually work?"),
            ("The Lead Magnet Types That Convert Best", "What lead magnet types convert best for a small business?"),
            ("How to Build a Lead Magnet in a Day with AI", "How do you build a lead magnet in a day with AI?"),
            ("Landing Page Essentials", "What should a lead magnet landing page include?"),
            ("Delivery Automation That Actually Works", "What lead magnet delivery automation actually works?"),
            ("Promoting Your Lead Magnet on Social Media", "How should you promote a lead magnet on social media?"),
            ("Real Conversion Benchmarks", "What conversion benchmarks are realistic for a lead magnet?"),
            ("Common Mistakes That Kill Lead Magnets", "What mistakes kill lead magnet performance?"),
            ("The Bottom Line", "What is the bottom line on building a lead magnet?"),
        ],
    },
    "how-to-run-a-giveaway-instagram.html": {
        "subtitle": "Instagram giveaways grow the right audience only when the prize filters for your buyer, the rules are clean, and the follow-up turns entrants into subscribers or customers. This guide covers the structure that makes that happen.",
        "cta": "Need giveaways, content, and follow-up offers connected instead of treated as a one-off spike? Start with a free audit.",
        "replacements": [
            ("The Rules (Legal Requirements)", "What rules and legal requirements should an Instagram giveaway follow?"),
            ("Prize Ideas by Industry", "What giveaway prizes work best by industry?"),
            ("Caption Template", "What caption template works for an Instagram giveaway?"),
            ("Partner Giveaway Structure", "How should you structure a partner Instagram giveaway?"),
            ("Timeline for a 7-Day Giveaway", "What timeline should a 7-day Instagram giveaway follow?"),
            ("Post-Giveaway Follow-Up (This Is Where Most People Fail)", "How should you follow up after an Instagram giveaway ends?"),
            ("Common Mistakes", "What giveaway mistakes create low-quality followers?"),
        ],
    },
    "content-creation-packages-small-business.html": {
        "subtitle": "Content-creation packages should be judged by the kind of assets produced, the amount of custom work included, and whether posting and management are separate services. This guide shows what each pricing tier should realistically buy.",
        "cta": "Need a content package built around your brand instead of generic templates and vague deliverables? Start with a free audit.",
        "replacements": [
            ("The Full Pricing Breakdown", "What does a full content-creation pricing breakdown look like?"),
            ("What You Get at Each Price Point (In Detail)", "What do you actually get at each content-package price point?"),
            ("Content Creation vs. Content Management (They're Different Services)", "What is the difference between content creation and content management?"),
            ("Red Flags in Cheap Packages", "What red flags show up in cheap content packages?"),
            ("How to Compare Packages (The Checklist)", "How should a small business compare content packages?"),
            ('What "Custom Content" Actually Means', 'What does "custom content" actually mean in a package?'),
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
