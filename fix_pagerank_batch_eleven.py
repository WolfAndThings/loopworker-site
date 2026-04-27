#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).parent
BLOG_DIR = ROOT / "blog"


PAGES = {
    "fiverr-vs-professional-brand-design.html": {
        "subtitle": "Fiverr and professional brand design solve two very different problems: one gets you a cheap asset quickly, the other builds a system that can actually support positioning, consistency, and growth. This guide shows where the cheap option becomes expensive later.",
        "cta": "Need a brand system that does more than generate another generic logo? Start with a free audit.",
        "replacements": [
            ("What You Actually Get on Fiverr", "What do you actually get on Fiverr?"),
            ("What Professional Brand Design Includes", "What does professional brand design actually include?"),
            ("The Comparison", "How do Fiverr and professional brand design compare?"),
            ("Why Cheap Logos Create Expensive Problems", "Why do cheap logos create expensive problems later?"),
            ("When Fiverr Actually Makes Sense", "When does Fiverr actually make sense?"),
            ("The Real Cost of Looking Cheap", "What is the real cost of looking cheap?"),
            ("The Brand System Approach", "What does the brand-system approach look like?"),
            ("The Verdict", "What is the verdict for most businesses?"),
        ],
    },
    "iphone-portrait-mode-business.html": {
        "subtitle": "iPhone Portrait Mode works for business photography when you choose the right subject distance, light, and scene for the effect instead of using it blindly on everything. This guide shows how to get cleaner headshots, product close-ups, and lifestyle images from the phone you already have.",
        "cta": "Need business photos that look more intentional without hiring a crew for every shoot? Start with a free audit.",
        "replacements": [
            ("Team Headshots with Portrait Mode", "How should you use Portrait Mode for team headshots?"),
            ("Product Close-Ups with Portrait Mode", "How should you use Portrait Mode for product close-ups?"),
            ("Lifestyle Shots with Portrait Mode", "How should you use Portrait Mode for lifestyle business photos?"),
            ("The 7 Most Common Portrait Mode Mistakes", "What Portrait Mode mistakes should businesses avoid?"),
            ("When to Skip Portrait Mode", "When should you skip Portrait Mode entirely?"),
        ],
    },
    "free-ai-prompts-for-small-business.html": {
        "opening": "These AI prompts work best when you treat them as reusable starting points for real business tasks, not magic commands. This guide organizes 100 prompts by use case so you can get useful drafts for marketing, planning, customer communication, and brand work faster.",
        "cta": "Need AI prompts tied to a stronger marketing system instead of random outputs? Start with a free audit.",
        "replacements": [
            ("Social Media Captions (1-20)", "Which AI prompts help with social media captions?"),
            ("Email Marketing (21-35)", "Which AI prompts help with email marketing?"),
            ("Blog Post Outlines (36-50)", "Which AI prompts help with blog post outlines?"),
            ("Product Descriptions (51-65)", "Which AI prompts help with product descriptions?"),
            ("Ad Copy (66-75)", "Which AI prompts help with ad copy?"),
            ("Brand Strategy (76-85)", "Which AI prompts help with brand strategy?"),
            ("Customer Service (86-95)", "Which AI prompts help with customer service?"),
            ("Content Planning (96-100)", "Which AI prompts help with content planning?"),
            ("How to Get Better Results from These Prompts", "How do you get better results from these AI prompts?"),
        ],
    },
    "food-photography-props-guide.html": {
        "subtitle": "A food photography prop kit works when it gives you enough surfaces, vessels, texture, and light control to style many scenes without buying a closet full of random objects. This guide shows what to buy first, where to save money, and what to skip.",
        "cta": "Need food visuals that look styled and consistent without overspending on props? Start with a free audit.",
        "replacements": [
            ("Category 1: Surfaces and Backgrounds", "What surfaces and backgrounds should you buy first?"),
            ("Category 2: Plates and Bowls", "What plates and bowls work best for food photography?"),
            ("Category 3: Utensils", "What utensils make good food photography props?"),
            ("Category 4: Textiles", "What textiles help food photos look better?"),
            ("Category 5: Garnishes and Fresh Elements", "What garnishes and fresh elements should you keep on hand?"),
            ("Category 6: Glassware and Drinks", "What glassware and drink props are worth buying?"),
            ("Category 7: Lighting Essentials", "What lighting essentials belong in a food prop kit?"),
            ("The Complete Budget Shopping List", "What should a budget food-photography shopping list include?"),
            ("Where to Shop: The Best Sources Ranked", "Where should you shop for food photography props?"),
            ("Props to Avoid", "What food photography props should you avoid?"),
        ],
    },
    "food-styling-tips-beginners.html": {
        "subtitle": "Food styling for beginners is mostly about making deliberate choices before the photo happens: plate selection, garnish, texture, spacing, and cleanup. This guide shows how to make simple dishes look more editorial without specialized training.",
        "cta": "Need food content that looks styled instead of accidental? Start with a free audit.",
        "replacements": [
            ("The 7 Principles of Food Styling", "What principles make food styling work?"),
            ("Plate Selection Guide", "How should you choose plates for food styling?"),
            ("Background Surfaces Ranked", "What background surfaces work best for styled food photos?"),
            ("Props That Elevate the Shot", "What props elevate a food photo without cluttering it?"),
            ("Common Styling Mistakes", "What food styling mistakes should beginners avoid?"),
            ("Dish-Specific Styling Tips", "What styling tips work for different kinds of dishes?"),
            ("Quick Fixes for Common Problems", "What quick fixes solve common food-styling problems?"),
        ],
    },
    "pinterest-marketing-small-business.html": {
        "opening": "Pinterest marketing works for small businesses because the platform behaves more like a visual search engine than a social feed. That changes the strategy completely: keyword alignment, pin design, consistency, and traffic paths matter more than day-to-day engagement tricks.",
        "cta": "Need a traffic channel that compounds instead of disappearing 24 hours after you post? Start with a free audit.",
        "replacements": [
            ("Pinterest Is a Search Engine, Not Social Media", "Why does Pinterest work more like a search engine than social media?"),
            ("Pin Design That Gets Clicks", "What pin design actually gets clicks?"),
            ("Pinterest SEO: How to Rank in Search", "How do you rank in Pinterest search?"),
            ("Rich Pins: The Feature Most Businesses Skip", "What are Rich Pins and why do they matter?"),
            ("Scheduling and Consistency: The Pinterest Algorithm", "How do scheduling and consistency affect Pinterest performance?"),
            ("Driving Traffic: From Pinterest to Your Website", "How do you drive traffic from Pinterest to your website?"),
            ("AI Tools for Pin Creation", "Which AI tools help create Pinterest content?"),
            ("Measuring What Matters", "What Pinterest metrics actually matter?"),
            ("The Pinterest Strategy That Compounds", "What Pinterest strategy compounds over time?"),
        ],
    },
    "ai-photography-for-dental-practices.html": {
        "subtitle": "AI photography helps dental practices close the visual trust gap when the website, GBP, and social profiles do not reflect the quality of the office or team. This guide shows where AI imagery helps, how to use it responsibly, and where real patient results still matter more.",
        "cta": "Need a dental brand that looks more trustworthy online before a patient ever calls? Start with a free audit.",
        "replacements": [
            ("The Trust Gap in Dental Marketing", "What is the trust gap in dental marketing?"),
            ("What AI Photography Can Do for Dental Practices", "What can AI photography do for dental practices?"),
            ("Prompt Strategies for Medical-Adjacent Content", "What prompt strategies work for medical-adjacent dental content?"),
            ("Google Business Profile: The Channel That Matters Most", "How should dental practices use AI imagery on Google Business Profile?"),
            ("Social Media for Dental: What Actually Gets Engagement", "What dental social media content actually gets engagement?"),
            ("Cost Comparison: Traditional vs. AI-Augmented", "How does AI-augmented photography compare on cost?"),
            ("The Hybrid System That Works", "What hybrid photography system works best for dental practices?"),
        ],
    },
    "restaurant-social-media-manager-cost.html": {
        "subtitle": "Restaurant social media pricing only makes sense once you separate content creation, posting, and full management into different scopes. This guide breaks down what restaurants are actually paying for and where generic social media packages miss the operational reality of food businesses.",
        "cta": "Need restaurant content help scoped clearly before you overpay for the wrong service? Start with a free audit.",
        "replacements": [
            ("Why Restaurant Social Media Is Different", "Why is restaurant social media different from generic social media work?"),
            ("The Restaurant Social Media Pricing Tiers", "What restaurant social media pricing tiers exist?"),
            ("Tier 1: Content Creation Only ($300-750)", "What does restaurant content creation only usually cost?"),
            ("Tier 2: Content + Posting ($500-1,500/month)", "What does restaurant content plus posting usually cost?"),
            ("Tier 3: Full Management ($1,500-4,000/month)", "What does full restaurant social media management usually cost?"),
            ("What Restaurants Specifically Need (That Generic Services Miss)", "What do restaurants need that generic social media services miss?"),
            ("How to Measure If It's Working", "How should a restaurant measure whether social media help is working?"),
            ("The Smart Starting Point for Most Restaurants", "What is the smart starting point for most restaurants?"),
        ],
    },
    "small-business-marketing-budget.html": {
        "opening": "A small-business marketing budget works when spending follows a framework instead of fear, habit, or whatever platform shouted loudest this week. This guide shows how to set the total budget, divide it across channels, and increase it only when the math supports it.",
        "cta": "Need a marketing budget tied to actual growth priorities instead of guesswork? Start with a free audit.",
        "replacements": [
            ("The Revenue-Based Budgeting Formula", "How should a small business budget marketing as a percentage of revenue?"),
            ("The 2026 Channel Allocation Framework", "How should you allocate a marketing budget across channels in 2026?"),
            ("How AI Tools Are Changing Budget Math", "How are AI tools changing marketing budget math?"),
            ("The Organic vs. Paid Split", "How should you split budget between organic and paid marketing?"),
            ("Content vs. Advertising: The Long Game", "How should you think about content versus advertising spend?"),
            ("When to Increase Your Marketing Budget", "When should a small business increase its marketing budget?"),
            ("Budget Allocation by Business Type", "How should marketing budgets change by business type?"),
            ("Tracking What Works", "How should a small business track marketing performance?"),
            ("The Minimum Viable Marketing Stack for 2026", "What is the minimum viable marketing stack for 2026?"),
        ],
    },
    "landing-page-copywriting-guide.html": {
        "subtitle": "Landing page copy converts when the structure answers objections in the right order: clear promise, relevant proof, tangible benefits, and a CTA that feels like the obvious next step. This guide shows how to build that flow instead of relying on random sections.",
        "cta": "Need landing pages that convert because the message is clear, not because you keep changing button colors? Start with a free audit.",
        "replacements": [
            ("Above the Fold: The 5-Second Test", "What should a landing page communicate above the fold?"),
            ("Headline Formulas That Convert", "What headline formulas convert on landing pages?"),
            ("Benefits vs. Features: The Section That Sells", "How should you balance benefits and features on a landing page?"),
            ("Social Proof Placement", "Where should social proof go on a landing page?"),
            ("CTA Button Copywriting", "What CTA button copy works best on landing pages?"),
            ("Template 1: Service Business Landing Page", "What should a service-business landing page look like?"),
            ("Template 2: E-Commerce Product Page", "What should an ecommerce product landing page look like?"),
            ("Template 3: Lead Magnet / Opt-in Page", "What should a lead-magnet landing page look like?"),
            ("Common Landing Page Mistakes", "What landing page copy mistakes should you avoid?"),
        ],
    },
    "restaurant-google-business-profile.html": {
        "subtitle": "A restaurant Google Business Profile works when the setup, photo library, posts, reviews, and Q&A all reinforce the same dining decision: this place looks worth visiting right now. This guide breaks down how restaurants should optimize GBP specifically, not generically.",
        "cta": "Need your restaurant to look better in Google before customers ever reach your website? Start with a free audit.",
        "replacements": [
            ("Complete Setup Walkthrough", "How should a restaurant set up Google Business Profile completely?"),
            ("Photo Strategy: 10 Photo Types Every Restaurant Needs", "What photos does every restaurant Google Business Profile need?"),
            ("Google Posts for Restaurants", "How should restaurants use Google Posts?"),
            ("Review Strategy", "What review strategy helps a restaurant Google Business Profile grow?"),
            ("Q&A Section Optimization", "How should restaurants optimize the GBP Q&A section?"),
            ("How GBP Connects to Local Search", "How does GBP connect to restaurant local search visibility?"),
            ("What to Measure in GBP Insights", "What should restaurants measure inside GBP insights?"),
        ],
    },
    "how-to-create-social-media-graphics.html": {
        "opening": "Social media graphics work when they communicate one clear idea instantly, match the platform’s format, and stay visually consistent with the brand. This guide focuses on building that system instead of endlessly tweaking decorative details that do not help the post perform.",
        "cta": "Need social graphics that actually support your brand and stop the scroll? Start with a free audit.",
        "replacements": [
            ("Design Principles That Actually Matter", "What design principles actually matter for social media graphics?"),
            ("Tools for Creating Social Media Graphics", "What tools should you use to create social media graphics?"),
            ("Platform-Specific Sizing Guide", "What sizes should social media graphics use by platform?"),
            ("Carousel Design: The Highest-Performing Format", "How should you design carousels for social media?"),
            ("Story Design: Ephemeral But Important", "How should you design social media stories?"),
            ("Templates vs. Custom: The Real Trade-Off", "When should you use templates versus custom graphics?"),
            ("Building a Graphic Creation System", "How do you build a repeatable graphic creation system?"),
            ("Stop Designing, Start Communicating", "How do you design graphics that communicate instead of decorate?"),
        ],
    },
    "restaurant-user-generated-content.html": {
        "subtitle": "Restaurant UGC works when customers are nudged into creating content, permissions are handled cleanly, and reposting becomes a repeatable system instead of a random win. This guide shows how to engineer more customer-made content without looking desperate.",
        "cta": "Need more customer content and social proof without producing every post yourself? Start with a free audit.",
        "replacements": [
            ("Engineering Photo-Worthy Moments", "How do you engineer photo-worthy moments in a restaurant?"),
            ("Building Your Hashtag Strategy", "How should a restaurant build a UGC hashtag strategy?"),
            ("The Reposting Workflow", "What should a restaurant reposting workflow look like?"),
            ("UGC Rights: What You Can and Cannot Do", "What can a restaurant legally do with customer-generated content?"),
            ("Incentivizing UGC Without Being Desperate", "How do you incentivize UGC without looking desperate?"),
            ("Measuring Your UGC Program", "How should a restaurant measure its UGC program?"),
        ],
    },
    "restaurant-video-content-guide.html": {
        "subtitle": "Restaurant video works when the format, shooting environment, editing workflow, and posting schedule are designed for the realities of a busy kitchen and dining room. This guide shows how to make video a usable system instead of another content idea that dies after two weeks.",
        "cta": "Need restaurant video content that looks better and ships consistently? Start with a free audit.",
        "replacements": [
            ("The 8 Video Formats That Work for Restaurants", "What restaurant video formats actually work?"),
            ("Equipment You Actually Need", "What video equipment does a restaurant actually need?"),
            ("Editing Apps Ranked", "Which editing apps work best for restaurant video?"),
            ("Audio Strategy", "How should restaurants handle audio in video content?"),
            ("The Weekly Video Posting Calendar", "What should a weekly restaurant video posting calendar look like?"),
            ("Shooting Tips for Restaurant Environments", "What shooting tips help in real restaurant environments?"),
        ],
    },
    "restaurant-seasonal-marketing.html": {
        "subtitle": "Restaurant seasonal marketing works when promotions, menu transitions, email themes, social posts, and photography are planned far enough ahead that each month feels intentional instead of rushed. This guide turns the year into a repeatable content and promotion calendar.",
        "cta": "Need a seasonal restaurant marketing calendar that stays ahead of the month instead of reacting to it? Start with a free audit.",
        "replacements": [
            ("January: Fresh Start Energy", "What should restaurants market in January?"),
            ("February: Love and Connection", "What should restaurants market in February?"),
            ("March: Spring Awakening", "What should restaurants market in March?"),
            ("April: Easter and Earth", "What should restaurants market in April?"),
            ("May: Celebrations", "What should restaurants market in May?"),
            ("June: Summer Launch", "What should restaurants market in June?"),
            ("July: Peak Summer", "What should restaurants market in July?"),
            ("August: Late Summer", "What should restaurants market in August?"),
            ("September: Fall Transition", "What should restaurants market in September?"),
            ("October: Festive Energy", "What should restaurants market in October?"),
            ("November: Holiday Ramp-Up", "What should restaurants market in November?"),
            ("December: Peak Season", "What should restaurants market in December?"),
            ("How to Plan Seasonal Menu Transitions", "How should restaurants plan seasonal menu transitions?"),
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
