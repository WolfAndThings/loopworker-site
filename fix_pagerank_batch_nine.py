#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).parent
BLOG_DIR = ROOT / "blog"


PAGES = {
    "ai-photography-for-gyms-fitness.html": {
        "subtitle": "AI photography helps gyms and fitness brands keep up with the constant demand for social, Google, website, and campaign visuals without booking a new shoot for every promotion. This guide shows where it works, where real photography still matters, and how to blend the two.",
        "cta": "Need a fitness content system that can keep up with promotions, memberships, and seasonal campaigns? Start with a free audit.",
        "replacements": [
            ("The Visual Demands of a Fitness Business", "What visual demands does a fitness business actually have?"),
            ("What AI Generates Well for Fitness", "What does AI generate well for gyms and fitness brands?"),
            ("What Still Needs Real Photos", "What still needs real photography for a fitness brand?"),
            ("Prompt Strategies for Gym Aesthetics", "What prompt strategies work for gym aesthetics?"),
            ("Social Content Calendar for Gyms", "What should an AI-assisted social content calendar look like for gyms?"),
            ("Google Business Profile for Gyms", "How should gyms use AI imagery on Google Business Profile?"),
            ("Cost Comparison: Photographer vs. AI", "How does AI compare to a photographer on cost?"),
            ("Seasonal Campaigns: The AI Advantage", "Why does AI help with seasonal fitness campaigns?"),
            ("Getting Started", "How should a gym get started with AI photography?"),
        ],
    },
    "brand-color-palette-guide.html": {
        "subtitle": "A strong brand color palette balances psychology, hierarchy, contrast, and practical usage rules so the brand looks recognizable everywhere from the logo to the website to social graphics. This guide shows how to build that palette step by step.",
        "cta": "Need a color system that makes your brand look consistent instead of improvised? Start with a free audit.",
        "replacements": [
            ("Color Psychology: What Each Color Actually Signals", "What does each brand color actually signal?"),
            ("The Anatomy of a Brand Color Palette", "What belongs in a brand color palette?"),
            ("The 60-30-10 Rule", "How does the 60-30-10 color rule work?"),
            ("Step-by-Step: Building Your Palette", "How do you build a brand color palette step by step?"),
            ("Free Tools for Building Palettes", "What free tools help build brand color palettes?"),
            ("10 Industry-Specific Palettes (With Hex Codes)", "What brand color palettes work by industry?"),
            ("How to Document Your Colors in a Brand Guide", "How should you document brand colors in a guide?"),
            ("Common Mistakes", "What brand color palette mistakes should you avoid?"),
        ],
    },
    "before-after-content-small-business.html": {
        "subtitle": "Before-and-after content works because it combines proof, curiosity, and transformation in a format people stop to inspect. This guide shows how small businesses can shoot it consistently, caption it well, and use it across posts, Reels, and sales assets.",
        "cta": "Need transformation content that actually earns attention and trust for your business? Start with a free audit.",
        "replacements": [
            ("Why Before/After Outperforms Everything Else", "Why does before-and-after content outperform other formats?"),
            ("Industries That Crush It", "Which industries win with before-and-after content?"),
            ("How to Shoot: The Consistency Rule", "How should you shoot before-and-after content consistently?"),
            ("Carousel Format: The 3-Slide Formula", "What carousel formula works for before-and-after posts?"),
            ("Reel Format: The Quick Reveal", "What Reel format works for before-and-after posts?"),
            ("Apps for Side-by-Side Images", "What apps help create before-and-after visuals?"),
            ("5 Caption Formulas for Before/After Posts", "What caption formulas work for before-and-after posts?"),
            ("Getting Client Permission", "How should you get client permission for before-and-after content?"),
        ],
    },
    "coffee-shop-branding-guide.html": {
        "subtitle": "Coffee shop branding works when the vibe is intentional across voice, color, typography, photography, packaging, and the in-store experience instead of being left to random design choices. This guide shows how to build that feeling on a small budget.",
        "cta": "Need your coffee shop to look memorable online and in person without hiring a full agency? Start with a free audit.",
        "replacements": [
            ('The "Vibe Gap" &mdash; Why Most Coffee Shops Look Generic', "What creates the vibe gap for most coffee shops?"),
            ("Brand DNA: Voice, Color Palette, and Typography", "What should a coffee shop's brand DNA include?"),
            ("Photography Direction: What to Shoot and How", "What photography direction should a coffee shop follow?"),
            ("Menu Design That Sells", "How should a coffee shop design menus that sell?"),
            ("Packaging and Cups on a Budget", "How can a coffee shop improve packaging on a budget?"),
            ("Instagram Grid Strategy for Coffee Shops", "What Instagram grid strategy works for coffee shops?"),
            ("Signage and In-Store Branding", "How should signage and in-store branding support the coffee shop brand?"),
            ("The $200 Branding Starter Kit", "What should a $200 coffee shop branding starter kit include?"),
        ],
    },
    "ai-photography-for-coaches-consultants.html": {
        "subtitle": "AI photography helps coaches and consultants build a consistent authority presence when real shoots are too slow, expensive, or operationally annoying to repeat every quarter. This guide covers the visuals to create, the prompts that work, and the cases where real photos still matter.",
        "cta": "Need authority visuals that keep your content consistent without booking another full photoshoot? Start with a free audit.",
        "replacements": [
            ("Why Visuals Matter More for Coaches Than Almost Anyone Else", "Why do visuals matter so much for coaches and consultants?"),
            ("What AI Photography Actually Produces for Coaches", "What does AI photography actually produce for coaches and consultants?"),
            ("The Prompt Strategy That Works for Professional Services", "What prompt strategy works for professional-service brands?"),
            ("Platform-by-Platform Usage", "How should coaches use AI photos across platforms?"),
            ("Before and After: The Brand Consistency Effect", "How does AI photography improve brand consistency over time?"),
            ("The Cost Reality", "What does AI photography really cost for coaches?"),
            ("When You Still Need a Real Photographer", "When do coaches still need a real photographer?"),
            ("Getting Started This Week", "How should a coach get started with AI photography this week?"),
        ],
    },
    "local-business-instagram-growth.html": {
        "subtitle": "Instagram growth for a local business is not about chasing huge follower counts. It is about reaching nearby buyers consistently enough that they remember the brand, respond to DMs, and eventually show up. This guide explains how to build that system.",
        "cta": "Need local Instagram growth tied to real customers instead of vanity metrics? Start with a free audit.",
        "replacements": [
            ("Set Up Your Content Pillars", "How should a local business set up Instagram content pillars?"),
            ("Posting Frequency: What's Realistic", "How often should a local business post on Instagram?"),
            ("Reels vs. Static Posts: The Real Answer", "Should a local business prioritize Reels or static posts?"),
            ("Local Hashtags and Geo-Tagging", "How should local businesses use hashtags and geo-tags?"),
            ("Engage with Your Neighborhood Online", "How should you engage with your local community online?"),
            ("DM Strategy: Where Sales Actually Happen", "How do local-business Instagram DMs turn into sales?"),
            ("Converting Followers to Customers", "How do you convert local Instagram followers into customers?"),
            ("What Metrics Actually Matter for Local Businesses", "What Instagram metrics actually matter for local businesses?"),
        ],
    },
    "best-social-media-service-for-local-business.html": {
        "subtitle": "The best social media service for a local business depends on whether you need software, design help, strategy, content production, or full execution. This guide compares the common options so you can match the spend to the actual problem.",
        "cta": "Need help choosing between tools, freelancers, agencies, and done-for-you content? Start with a free audit.",
        "replacements": [
            ("The Quick Comparison", "What is the quick comparison of social media service options?"),
            ("Scheduling Tools: Hootsuite, Buffer, Later", "How do scheduling tools compare for local businesses?"),
            ("Canva Pro ($13/month)", "Is Canva Pro enough for local-business social media?"),
            ("Fiverr Freelancers ($50-500 per project)", "Are Fiverr freelancers a good fit for local-business social media?"),
            ("Local Agencies ($2,000-8,000/month)", "When is a local agency worth paying for?"),
            ("DFY Content Services ($300-1,500)", "When does a done-for-you content service make sense?"),
            ("How to Choose: The Decision Framework", "How should a local business choose a social media service?"),
        ],
    },
    "canva-vs-custom-brand-design.html": {
        "subtitle": "The Canva-versus-custom-brand-design decision is really a question of speed versus strategic differentiation. This guide shows what Canva is good at, where it starts to cap your brand, and when a custom system becomes worth paying for.",
        "cta": "Need a brand system that looks intentional instead of template-driven? Start with a free audit.",
        "replacements": [
            ("What Canva Does Well", "What does Canva do well?"),
            ("Where Canva Falls Short", "Where does Canva fall short?"),
            ("What Custom Brand Design Gives You", "What does custom brand design give you?"),
            ("The Cost Comparison", "How do Canva and custom brand design compare on cost?"),
            ("The Canva Trap: How It Actually Plays Out", "What does the Canva trap look like in practice?"),
            ("When Canva Is the Right Call", "When is Canva the right choice?"),
            ("When to Invest in Custom Brand Design", "When should you invest in custom brand design?"),
            ("The Third Option: AI-Powered Brand Systems", "What is the third option between Canva and custom design?"),
            ("The Verdict", "What is the verdict for most businesses?"),
        ],
    },
    "ai-photography-real-estate-listings.html": {
        "subtitle": "AI photography for real-estate listings is useful when it accelerates staging, marketing variations, and high-volume content without crossing MLS, disclosure, or trust lines. This guide explains where it helps agents move faster and where it can create risk.",
        "cta": "Need listing visuals and marketing assets produced faster without compromising trust? Start with a free audit.",
        "replacements": [
            ("Virtual Staging vs. AI Photography: They're Not the Same Thing", "How is AI photography different from virtual staging?"),
            ("What Agents Actually Need: Image by Image", "What images do agents actually need for a listing?"),
            ("MLS Compliance: What You Need to Know", "What MLS compliance rules matter for AI listing images?"),
            ("Cost Comparison: Per Listing", "How does AI photography compare on a per-listing cost basis?"),
            ("The High-Volume Agent Workflow: 10+ Listings Per Month", "What workflow works for agents handling 10+ listings per month?"),
            ("Ethical Considerations and Disclosure", "What ethical and disclosure issues matter with AI real-estate imagery?"),
            ("Where AI Falls Short in Real Estate", "Where does AI fall short in real-estate marketing?"),
            ("The Bottom Line for Agents", "What is the bottom line for agents?"),
        ],
    },
    "etsy-seo-guide-2026.html": {
        "subtitle": "Etsy SEO works when tags, titles, listing quality, seasonal timing, and photos all reinforce the same buyer intent instead of pulling in different directions. This guide breaks down how to structure a listing so the right searches can actually find it.",
        "cta": "Need product visuals and listing structure working together so your Etsy shop converts better? Start with a free audit.",
        "replacements": [
            ("1. Tag Strategy: Your 13 Keyword Slots", "How should you use Etsy's 13 tag slots?"),
            ("2. Title Optimization: Front-Load What Matters", "How should you optimize Etsy titles?"),
            ("3. Long-Tail Keyword Research", "How do you research long-tail keywords for Etsy?"),
            ("4. Seasonal Planning: The Calendar That Drives Sales", "How should seasonal planning shape Etsy SEO?"),
            ("5. Listing Quality Score: What Etsy Actually Measures", "What does Etsy actually measure in listing quality?"),
            ("6. Etsy Ads Basics: When and How to Advertise", "When should you use Etsy Ads and how?"),
            ("7. Photo Optimization for Etsy Search", "How should you optimize product photos for Etsy search?"),
            ("Monthly Etsy SEO Checklist", "What should a monthly Etsy SEO checklist include?"),
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
