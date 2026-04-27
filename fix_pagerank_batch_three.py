#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).parent
BLOG_DIR = ROOT / "blog"


PAGES = {
    "local-seo-guide-small-business.html": {
        "subtitle": "Local SEO for a small business comes down to five systems: Google Business Profile, NAP consistency, citations, reviews, and location-specific site signals. This guide explains what each one does and what to fix first.",
        "cta": "Need local SEO, reviews, Google Business Profile, and content working together instead of as separate chores? Start with a free audit.",
        "replacements": [
            ("1. Google Business Profile: Your Most Important Asset", "Why is Google Business Profile your most important local SEO asset?"),
            ("2. NAP Consistency: The Foundation", "Why does NAP consistency matter for local SEO?"),
            ("3. Citation Building: Get Listed Everywhere", "How should you build local citations without wasting time?"),
            ("4. Review Generation: The Ranking Multiplier", "How do reviews improve local SEO rankings?"),
            ("5. Local Keyword Strategy", "What local keyword strategy should a small business use?"),
            ("Monthly Local SEO Checklist", "What should be on a monthly local SEO checklist?"),
        ],
    },
    "how-to-write-a-business-bio.html": {
        "subtitle": "A good business bio says what you do, who you help, and why someone should trust you, then adapts that formula to each platform's limits. These templates cover Instagram, LinkedIn, your website, and Google Business Profile.",
        "cta": "Need the bio, positioning, and visual system behind your offer cleaned up together? Start with a free audit.",
        "replacements": [
            ("Instagram Bio (150 Characters)", "What should an Instagram business bio include in 150 characters?"),
            ("What should an Instagram business bio include? (150 characters)", "What should an Instagram business bio include in 150 characters?"),
            ("LinkedIn Bio (2,600 Characters)", "What should a LinkedIn business bio include in 2,600 characters?"),
            ("What should a LinkedIn business bio include? (2,600 characters)", "What should a LinkedIn business bio include in 2,600 characters?"),
            ("Website About Page (300-500 Words)", "What should a website About page bio include in 300 to 500 words?"),
            ("What should a website About page bio include? (300-500 words)", "What should a website About page bio include in 300 to 500 words?"),
            ("Google Business Profile Description (750 Characters)", "What should a Google Business Profile description include in 750 characters?"),
            ("What should a Google Business Profile description include? (750 characters)", "What should a Google Business Profile description include in 750 characters?"),
            ("The 4 Elements Every Bio Needs", "What 4 elements does every business bio need?"),
        ],
    },
    "yelp-optimization-guide.html": {
        "subtitle": "Yelp optimization matters when your category depends on local trust, service quality, and review volume. This guide covers profile setup, photo strategy, review handling, and whether Yelp ads are worth paying for.",
        "cta": "Need Yelp, Google reviews, and local profile content working as one system? Start with a free audit.",
        "replacements": [
            ("Profile Setup Checklist", "What should be on a Yelp profile setup checklist?"),
            ("Photo Strategy", "What photos should you add to Yelp?"),
            ("Review Response Templates", "How should you respond to Yelp reviews?"),
            ("Yelp's Review Filter: What You Need to Know", "How does Yelp's review filter work?"),
            ("Should You Pay for Yelp Ads?", "Should you pay for Yelp Ads?"),
            ("Quick Wins You Can Do Today", "What Yelp fixes can you do today?"),
        ],
    },
    "how-to-create-a-portfolio-website.html": {
        "subtitle": "A portfolio website should prove your work, explain your offer, and move the right visitor toward inquiry. This guide covers platform choice, essential pages, SEO basics, and a realistic cost range.",
        "cta": "Need a portfolio site supported by stronger brand visuals and positioning? Start with a free audit.",
        "replacements": [
            ("Platform Comparison", "Which platform should you use for a portfolio website?"),
            ("The 5 Essential Pages", "What pages does a portfolio website actually need?"),
            ("SEO Basics for Portfolio Sites", "How do you handle SEO basics for a portfolio site?"),
            ("Total Cost Breakdown", "What does a portfolio website really cost?"),
        ],
    },
    "small-business-photography-checklist.html": {
        "subtitle": "A useful small business photo library includes space, team, product, process, customer, and lifestyle shots so you can support your website, ads, and social without reusing the same five images. This 50-shot checklist is organized for one production day.",
        "cta": "Need the full shot list turned into an ongoing visual system instead of a one-time scramble? Start with a free audit.",
        "replacements": [
            ("Category 1: Your Space (Shots 1-10)", "What space photos should every small business capture in shots 1 to 10?"),
            ("What space photos should every small business capture? (Shots 1-10)", "What space photos should every small business capture in shots 1 to 10?"),
            ("Category 2: Your Team (Shots 11-18)", "What team photos should every small business capture in shots 11 to 18?"),
            ("What team photos should every small business capture? (Shots 11-18)", "What team photos should every small business capture in shots 11 to 18?"),
            ("Category 3: Your Products or Services (Shots 19-30)", "What product or service photos should every small business capture in shots 19 to 30?"),
            ("What product or service photos should every small business capture? (Shots 19-30)", "What product or service photos should every small business capture in shots 19 to 30?"),
            ("Category 4: Behind the Scenes (Shots 31-38)", "What behind-the-scenes photos should every small business capture in shots 31 to 38?"),
            ("What behind-the-scenes photos should every small business capture? (Shots 31-38)", "What behind-the-scenes photos should every small business capture in shots 31 to 38?"),
            ("Category 5: Customer Experience (Shots 39-44)", "What customer-experience photos should every small business capture in shots 39 to 44?"),
            ("What customer-experience photos should every small business capture? (Shots 39-44)", "What customer-experience photos should every small business capture in shots 39 to 44?"),
            ("Category 6: Lifestyle and Context (Shots 45-50)", "What lifestyle and context photos should every small business capture in shots 45 to 50?"),
            ("What lifestyle and context photos should every small business capture? (Shots 45-50)", "What lifestyle and context photos should every small business capture in shots 45 to 50?"),
        ],
    },
    "food-photography-tips-phone.html": {
        "subtitle": "Good phone food photography comes from angle choice, window light, plate styling, and fast editing rather than expensive gear. This guide shows the settings, compositions, and mistakes that matter most.",
        "cta": "Need food photos that look consistent across menus, Google, and Instagram? Start with a free audit.",
        "replacements": [
            ("The 5 Essential Food Photography Angles", "What food photography angles work best on a phone?"),
            ("Phone Camera Settings for Food", "What phone camera settings work best for food photos?"),
            ("Natural Light Positioning", "How should you position natural light for food photography?"),
            ("The Steam Trick", "How do you make steam show up in food photos?"),
            ("Plate Styling Basics", "How should you style a plate for better food photos?"),
            ("Lightroom Mobile Editing Workflow (Step by Step)", "What is a simple Lightroom Mobile workflow for food photos?"),
            ("10 Common Food Photo Mistakes", "What food photo mistakes make dishes look worse?"),
            ("Best Free Editing Apps (Ranked)", "Which free editing apps are best for food photography?"),
        ],
    },
    "ai-copywriting-tools-small-business.html": {
        "subtitle": "The best AI copywriting tool depends on the job: ChatGPT for flexibility, Claude for long-form reasoning, Jasper for packaged marketing workflows, and Copy.ai for faster templated output. This comparison shows where each one fits.",
        "cta": "Need AI writing tools connected to a real content workflow instead of used ad hoc? We build the prompts, templates, and automation layer together.",
        "replacements": [
            ("The Comparison Table", "How do the main AI copywriting tools compare side by side?"),
            ("ChatGPT: The Swiss Army Knife", "When is ChatGPT the best AI copywriting tool?"),
            ("Claude: The Thoughtful Writer", "When is Claude the best AI copywriting tool?"),
            ("Jasper: The Marketing Specialist", "When is Jasper the best AI copywriting tool?"),
            ("Copy.ai: The Quick-Hit Generator", "When is Copy.ai the best AI copywriting tool?"),
            ("Which Tool Should You Use?", "Which AI copywriting tool should a small business choose?"),
            ("The Golden Rule of AI Copy", "What is the golden rule of AI-generated marketing copy?"),
        ],
    },
    "google-ads-for-small-business-beginners.html": {
        "subtitle": "Google Ads works for small businesses when tracking, keyword intent, negatives, and landing pages are set correctly before spend ramps. This guide walks through the setup sequence that protects a small budget.",
        "cta": "Need paid search, landing pages, and local conversion tracking aligned before you spend? Start with a free audit.",
        "replacements": [
            ("Step 1: Account Setup (Do NOT Use Smart Campaigns)", "How should a beginner set up a Google Ads account?"),
            ("Step 2: Conversion Tracking (Set This Up First)", "How should a small business set up Google Ads conversion tracking?"),
            ("Step 3: Keyword Research", "How should a small business research Google Ads keywords?"),
            ("Step 4: Negative Keywords (Save Your Budget)", "How do negative keywords protect your budget?"),
            ("Step 5: Ad Copy Templates", "What ad copy structure works for beginner Google Ads campaigns?"),
            ("Step 6: Budget Allocation", "How should a small business allocate a Google Ads budget?"),
            ("Step 7: Bidding Strategy", "Which bidding strategy should a beginner use in Google Ads?"),
            ("Step 8: Landing Pages", "What makes a landing page work with Google Ads?"),
            ("Week-by-Week Optimization Schedule", "What should a week-by-week Google Ads optimization schedule look like?"),
            ("Common Mistakes That Waste Money", "What Google Ads mistakes waste the most money?"),
        ],
    },
    "social-media-manager-vs-ai-automation.html": {
        "subtitle": "A social media manager handles strategy, relationships, and judgment, while AI automation handles production, scheduling, and repeatable workflows. This guide shows the cost difference, the capability split, and the hybrid model that usually makes the most sense.",
        "cta": "Need the hybrid model built so your team is not choosing between expensive labor and chaotic automation? Start with a free audit.",
        "replacements": [
            ("What a Social Media Manager Actually Does", "What does a social media manager actually do?"),
            ("What AI Automation Actually Handles", "What does AI automation actually handle?"),
            ("The Cost Comparison", "How do the costs compare between a social media manager and AI automation?"),
            ("What AI Can't Do (And Shouldn't Try)", "What can AI not do well in social media?"),
            ("What Humans Are Bad At (That AI Handles Perfectly)", "What repetitive social media tasks does AI handle better than humans?"),
            ("The Hybrid Model (This Is the Right Answer)", "What does the right hybrid social media model look like?"),
            ("When to Hire a Full Social Media Manager", "When should you hire a full social media manager?"),
            ("When to Lean Into Automation", "When should you lean harder into automation?"),
            ("ROI: Running the Numbers", "How should you calculate ROI for a manager versus automation?"),
            ("The Verdict", "What is the verdict: hire a manager, use AI, or combine both?"),
        ],
    },
    "social-media-scheduling-tools-compared.html": {
        "subtitle": "A good social scheduling tool should match your channel mix, approval workflow, analytics needs, and budget rather than win on feature count alone. This guide compares eight common tools by use case.",
        "cta": "Need the scheduler, templates, and content workflow chosen as one system instead of one-off tools? Start with a free audit.",
        "replacements": [
            ("The Big Comparison Table", "How do the main social media scheduling tools compare side by side?"),
            ("1. Buffer — The Simple One", "When is Buffer the right scheduling tool?"),
            ("1. Buffer &mdash; The Simple One", "When is Buffer the right scheduling tool?"),
            ("2. Later — The Instagram-First Tool", "When is Later the right scheduling tool?"),
            ("2. Later &mdash; The Instagram-First Tool", "When is Later the right scheduling tool?"),
            ("3. Hootsuite — The Enterprise Veteran", "When is Hootsuite the right scheduling tool?"),
            ("3. Hootsuite &mdash; The Enterprise Veteran", "When is Hootsuite the right scheduling tool?"),
            ("4. Planoly — The Visual Grid Planner", "When is Planoly the right scheduling tool?"),
            ("4. Planoly &mdash; The Visual Grid Planner", "When is Planoly the right scheduling tool?"),
            ("5. Sprout Social — The Premium Choice", "When is Sprout Social the right scheduling tool?"),
            ("5. Sprout Social &mdash; The Premium Choice", "When is Sprout Social the right scheduling tool?"),
            ("6. Loomly — The Team Collaboration Tool", "When is Loomly the right scheduling tool?"),
            ("6. Loomly &mdash; The Team Collaboration Tool", "When is Loomly the right scheduling tool?"),
            ("7. SocialBee — The Content Recycler", "When is SocialBee the right scheduling tool?"),
            ("7. SocialBee &mdash; The Content Recycler", "When is SocialBee the right scheduling tool?"),
            ("8. Metricool — The Analytics-First Scheduler", "When is Metricool the right scheduling tool?"),
            ("8. Metricool &mdash; The Analytics-First Scheduler", "When is Metricool the right scheduling tool?"),
            ("Quick Decision Framework", "What decision framework should you use to choose a scheduler?"),
            ("What I Actually Use", "Which scheduling tools do I actually use?"),
            ("Tips That Apply to Every Tool", "What posting rules apply no matter which scheduler you pick?"),
        ],
    },
    "how-to-take-product-photos-with-phone.html": {
        "opening": "You can take usable product photos with a phone if you control light, stabilize the shot, simplify the background, and edit lightly afterward. This guide covers the setup, the limits, and when AI becomes the better production option.",
        "cta": "Need consistent product imagery without shooting every variation by hand? Start with a free audit.",
        "replacements": [
            ("Phone Camera Settings That Actually Matter", "What phone camera settings actually matter for product photos?"),
            ("Lighting: The Only Thing That Really Matters", "How should you light product photos with a phone?"),
            ("Backgrounds and Surfaces", "What backgrounds and surfaces work best for product photos?"),
            ("Composition Rules for Product Photography", "What composition rules help product photos look better?"),
            ("Editing Apps Worth Using", "Which editing apps are worth using for product photos?"),
            ("Where Phone Photography Hits a Wall", "Where does phone product photography hit a wall?"),
            ("When AI Photography Is the Better Choice", "When is AI photography the better choice for product images?"),
            ("The Hybrid Approach", "What does the hybrid approach look like for product photography?"),
            ("Getting Started Today", "How should you get started with phone product photography today?"),
        ],
    },
    "lighting-setup-product-photography-diy.html": {
        "opening": "A DIY product-lighting setup only needs three decisions: your budget tier, your light position, and the type of consistency you need. This guide lays out exact setups at $20, $200, and $2000, then shows when AI is a better use of money.",
        "cta": "Need consistent product imagery without rebuilding a lighting setup for every new launch? Start with a free audit.",
        "replacements": [
            ("Tier 1: The $20 Setup", "What does a $20 product photography lighting setup look like?"),
            ("Tier 2: The $200 Setup", "What does a $200 product photography lighting setup look like?"),
            ("Tier 3: The $2000 Setup", "What does a $2000 product photography lighting setup look like?"),
            ("Comparison: What You Get at Each Tier", "How do the three lighting setups compare?"),
            ("When AI Photography Makes All of This Unnecessary", "When does AI photography make DIY lighting unnecessary?"),
        ],
    },
    "ai-photography-for-fashion-brands.html": {
        "subtitle": "AI fashion photography works best for lookbooks, editorial mood, flat lays, and campaign concepting, while exact on-model product truth still needs real photography. This guide breaks down where AI helps and where it still fails.",
        "cta": "Need a fashion content system that blends real product truth with scalable AI visuals? Start with a free audit.",
        "replacements": [
            ("What AI Can Generate for Fashion Brands", "What can AI generate for fashion brands right now?"),
            ("What AI Can't Do Yet", "What can AI not do yet for fashion brands?"),
            ("Prompt Strategies for Fashion Aesthetics", "How should fashion brands prompt AI for better aesthetics?"),
            ("Seasonal Collection Imagery at Scale", "How can fashion brands scale seasonal collection imagery?"),
            ("Cost Comparison: Traditional Fashion Shoot vs AI System", "How does an AI system compare to a traditional fashion shoot on cost?"),
            ("Quality Benchmarks: How to Know If Your AI Output Is Good Enough", "How do you know if AI fashion output is good enough?"),
            ("When to Hire a Photographer Anyway", "When should a fashion brand still hire a photographer?"),
            ("Building the System", "What does an AI fashion photography system look like?"),
        ],
    },
    "linkedin-content-strategy-small-business.html": {
        "subtitle": "LinkedIn content works for small businesses when posts demonstrate expertise, profile pages convert attention, and comments create warm paths to DM. This guide covers the publishing system that turns LinkedIn into a client channel.",
        "cta": "Need a LinkedIn content system tied to positioning, profile conversion, and content production? Start with a free audit.",
        "replacements": [
            ("Why LinkedIn Is Different (And Why That Matters)", "Why is LinkedIn different from other social platforms for small businesses?"),
            ("The LinkedIn Algorithm in 2026", "How does the LinkedIn algorithm work in 2026?"),
            ("Content Pillars for Service Businesses", "What LinkedIn content pillars work for service businesses?"),
            ("Posting Frequency and Timing", "How often should a small business post on LinkedIn and when?"),
            ("Profile Optimization for Conversion", "How should you optimize a LinkedIn profile for conversion?"),
            ("Using AI to Write LinkedIn Posts Without Sounding Robotic", "How should you use AI to write LinkedIn posts without sounding robotic?"),
            ("The Comment Strategy", "What LinkedIn comment strategy actually builds reach?"),
            ("The DM Approach After Engagement", "How should you handle DMs after engagement?"),
            ("What to Measure", "What should you measure on LinkedIn?"),
        ],
    },
    "how-to-price-creative-services.html": {
        "subtitle": "Creative services should be priced from value, delivery scope, and margin targets rather than vague confidence or what the client seems willing to pay. This guide covers tiering, anchors, objections, and pricing AI-enhanced work.",
        "cta": "Need your offer, pricing, and delivery system aligned so margins actually hold? Start with a free audit.",
        "replacements": [
            ("Why Creatives Undercharge", "Why do creatives undercharge?"),
            ("Value-Based Pricing Explained", "What is value-based pricing for creative services?"),
            ("The 3-Tier Framework", "What does a 3-tier pricing framework look like?"),
            ("Calculating Your Actual Costs", "How do you calculate your real delivery costs?"),
            ("Anchoring and Positioning", "How do anchoring and positioning affect pricing?"),
            ("When to Raise Prices", "When should you raise your prices?"),
            ('Handling "That Is Too Expensive"', 'How should you handle "that is too expensive" objections?'),
            ('Handling \\"That Is Too Expensive\\"', 'How should you handle "that is too expensive" objections?'),
            ("Pricing AI-Enhanced Services", "How should you price AI-enhanced creative services?"),
            ("Real Pricing by Service Type", "What pricing ranges make sense by service type?"),
            ("The Bottom Line", "What is the bottom line on pricing creative services?"),
        ],
    },
    "how-to-write-instagram-captions.html": {
        "cta": "Need a caption system your team can actually keep up with? We build content workflows that generate hooks, captions, and visuals together.",
    },
    "how-to-increase-instagram-engagement.html": {
        "cta": "Need an Instagram system built around engagement and conversion, not random posting? Start with a free audit.",
    },
    "how-to-get-clients-on-instagram.html": {
        "cta": "Need an Instagram pipeline that turns attention into real inquiries? Start with a free audit.",
    },
    "instagram-reel-ideas-small-business.html": {
        "cta": "Need Reels supported by a stronger visual system? We build the photo direction, content templates, and workflow behind the posting.",
    },
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def replace_first(pattern: str, text: str, new_text: str) -> str:
    regex = re.compile(pattern, re.S)

    def repl(match: re.Match[str]) -> str:
        return f"{match.group(1)}{new_text}{match.group(2)}"

    return regex.sub(repl, text, count=1)


def replace_all(pattern: str, text: str, new_text: str) -> str:
    regex = re.compile(pattern, re.S)

    def repl(match: re.Match[str]) -> str:
        return f"{match.group(1)}{new_text}{match.group(2)}"

    return regex.sub(repl, text)


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
