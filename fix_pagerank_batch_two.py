#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).parent
BLOG_DIR = ROOT / "blog"
SKIPS_PATH = ROOT / "BLOG_EDITORIAL_SKIPS.md"


PAGES = {
    "how-to-batch-content-creation.html": {
        "subtitle": "Content batching works because it reduces context switching, turns planning into a repeatable process, and makes it possible to create weeks of content in one focused session. This guide breaks down the system, the schedule, and the tools that make batching sustainable.",
        "cta": "Need a content batching system that creates, schedules, and publishes with less manual work? We build AI-assisted content pipelines that turn one production block into a full week of publish-ready content.",
        "replacements": [
            ("Why Batching Works (The Cognitive Science)", "Why does batching work better than creating one post at a time?"),
            ("The 4-Phase Batching System", "What is the 4-phase content batching system?"),
            ("How AI Changes the Batching Math", "How does AI change the content batching math?"),
            ("Batching by Content Type", "How should you batch content by format?"),
            ("A Real Weekly Schedule", "What does a real weekly batching schedule look like?"),
            ("The Tools That Make It Work", "What tools make content batching easier?"),
            ("Common Batching Mistakes", "What mistakes ruin a batching workflow?"),
            ("Start With One Batch Day", "How should you start with one batch day?"),
        ],
    },
    "build-visual-brand-instagram.html": {
        "subtitle": "A visual brand on Instagram comes from a fixed color system, repeatable content types, and templates that make the feed recognizable at a glance. This guide shows how to build that system from zero and keep it consistent as you grow.",
        "cta": "Need a visual brand system your Instagram can actually sustain? We build the brand rules, templates, and production workflow so the feed stays consistent.",
        "replacements": [
            ("Step 1: Define Your Visual Identity Before You Post Anything", "How do you define your visual identity before posting anything?"),
            ("Step 2: Plan Your Content Types", "How should you plan your Instagram content types?"),
            ("Step 3: Build a Consistency System", "How do you build a consistency system for Instagram?"),
            ("Step 4: Use AI to Maintain Visual Consistency", "How can AI help maintain visual consistency?"),
            ("Step 5: Growing from 0 to 1,000 Followers", "How do you grow from 0 to 1,000 followers without losing brand consistency?"),
            ("Common Visual Mistakes That Kill Brand Perception", "What visual mistakes hurt brand perception on Instagram?"),
            ("The Compound Effect", "Why does a strong Instagram visual brand compound over time?"),
        ],
    },
    "best-ai-tools-small-business-marketing.html": {
        "subtitle": "The best AI tools for small business marketing usually fall into six jobs: copy, images, video, automation, scheduling, and analytics. This guide compares the tools that matter, what they cost, and where they break.",
        "cta": "Need the AI stack configured into one working marketing system? We build the generation, automation, and publishing layer together.",
        "replacements": [
            ("Image Generation", "Which AI image tools are best for small business marketing?"),
            ("Video Production", "Which AI video tools are actually worth using?"),
            ("Content Writing", "Which AI writing tools help most with marketing?"),
            ("Workflow Automation", "Which automation tools save the most time?"),
            ("Social Media Posting and Scheduling", "Which scheduling tools are worth it for social posting?"),
            ("Analytics and Research", "Which AI analytics and research tools are useful?"),
            ("The Stack I Actually Recommend", "What AI marketing stack do I actually recommend?"),
            ("What to Avoid", "What AI marketing tools should you avoid?"),
            ("The Real Competitive Advantage", "What is the real competitive advantage with AI tools?"),
        ],
    },
    "ai-headshots-for-business.html": {
        "subtitle": "AI headshots are useful for LinkedIn, team pages, and fast visual updates when you need speed and consistency more than a full production. This guide covers the cost, quality tradeoffs, and where studio photography still wins.",
        "cta": "Need more than a one-off headshot? We build full visual systems for teams that need headshots, brand imagery, and ongoing content.",
        "replacements": [
            ("The Current State of AI Headshots", "What is the current state of AI headshots?"),
            ("Cost Comparison: The Real Numbers", "How much do AI headshots cost compared to studio photos?"),
            ("When AI Headshots Work", "When do AI headshots actually work well?"),
            ("When Studio Photography Still Wins", "When does studio photography still win?"),
            ("The Hybrid Approach: Best of Both", "What does the best hybrid headshot approach look like?"),
            ("Making AI Headshots Look Less AI", "How do you make AI headshots look less artificial?"),
            ("LinkedIn Optimization: Beyond the Photo", "How should you use AI headshots on LinkedIn?"),
            ("The Verdict", "What is the verdict on AI headshots for business?"),
        ],
    },
    "ai-generated-lifestyle-photography.html": {
        "subtitle": "AI-generated lifestyle photography is best for high-volume brand content where context, mood, and product storytelling matter more than exact one-to-one realism. This guide covers where it works, where it fails, and how to make it look usable.",
        "cta": "Need lifestyle imagery that matches your brand every week, not once a quarter? We build AI-powered visual systems that generate and organize it.",
        "replacements": [
            ("Lifestyle Photography vs. Product Photography: Why It Matters", "Why does lifestyle photography matter more than isolated product shots?"),
            ("How AI Generates Lifestyle Photography", "How does AI generate lifestyle photography?"),
            ("5 Lifestyle Shot Types Every Brand Needs", "What lifestyle shot types does every brand need?"),
            ("Post-Processing: Making AI Output Feel Real", "How do you make AI lifestyle photography feel more real?"),
            ("When to Use Real Photography Instead", "When should you use real photography instead of AI?"),
            ('Quality Benchmarks: What "Good Enough" Looks Like', 'What does "good enough" AI lifestyle photography look like?'),
            ("Getting Started", "How should a brand get started with AI lifestyle photography?"),
        ],
    },
    "google-business-profile-optimization.html": {
        "subtitle": "Google Business Profile is often the highest-leverage local marketing asset because it drives calls, map views, reviews, and discovery before a customer ever reaches your website. This guide shows what to optimize first and what most businesses ignore.",
        "cta": "Need your Google Business Profile, reviews, and content system cleaned up together? Start with a free audit.",
        "replacements": [
            ("Why GBP Matters More Than Your Website", "Why does Google Business Profile matter more than your website for local discovery?"),
            ("The Complete Setup Checklist", "What should be on a complete Google Business Profile setup checklist?"),
            ("Photo Optimization: The Biggest Gap", "How should you optimize photos on Google Business Profile?"),
            ("Review Strategy: The Growth Engine", "What review strategy actually drives GBP growth?"),
            ("GBP Posts: The Feature Nobody Uses", "How should businesses use GBP posts?"),
            ("Q&A Section: Control the Narrative", "How do you use the GBP Q&A section to control the narrative?"),
            ("Categories and Attributes: The Hidden Ranking Levers", "How do categories and attributes affect GBP rankings?"),
            ("Tracking Performance", "What should you track inside Google Business Profile?"),
            ("Common Mistakes That Tank Your Profile", "What mistakes tank a Google Business Profile?"),
            ("AI Tools for GBP Management", "Which AI tools help manage a Google Business Profile?"),
            ("Start Today", "What should you do first if you fix your GBP today?"),
        ],
    },
    "how-to-write-instagram-captions.html": {
        "opening": "Instagram captions convert best when they open with a clear hook, carry one useful idea, and end with a low-friction action. This guide breaks down the structure, formulas, and workflow that make captions easier to write consistently.",
        "cta": "Need a caption system your team can actually keep up with? We build content workflows that generate hooks, captions, and visuals together.",
        "replacements": [
            ("Why Your Captions Are Not Converting", "Why are your Instagram captions not converting?"),
            ("The Anatomy of a High-Converting Caption", "What does a high-converting Instagram caption include?"),
            ("Caption Length: The Debate That Does Not Matter", "How much does caption length actually matter?"),
            ("Building a Consistent Brand Voice in Your Captions", "How do you build a consistent brand voice in captions?"),
            ("Storytelling in Captions: The Engagement Multiplier", "How does storytelling improve Instagram captions?"),
            ("Hashtag Strategy in 2026", "What hashtag strategy still works in 2026?"),
            ("Using AI Tools for Caption Writing", "How should you use AI tools for caption writing?"),
            ("Caption Formulas You Can Use Today", "What caption formulas can you use today?"),
            ("The Posting Workflow That Saves You Time", "What posting workflow saves the most time?"),
            ("Measuring What Works", "How should you measure which captions work?"),
        ],
    },
    "how-to-get-more-google-reviews.html": {
        "subtitle": "The best way to get more Google reviews is to ask during peak satisfaction, make the request frictionless, and build review asks into your operating process instead of treating them as one-off favors. This guide shows the system.",
        "cta": "Need a local growth system that improves reviews, visibility, and conversion together? Start with a free audit.",
        "replacements": [
            ("Why Google Reviews Actually Matter", "Why do Google reviews actually matter?"),
            ("The Psychology of Why People Do Not Leave Reviews", "Why do customers avoid leaving reviews?"),
            ("Timing Your Ask: The Peak Satisfaction Window", "When should you ask for a Google review?"),
            ("Methods That Actually Work", "What review request methods actually work?"),
            ("Responding to Reviews: Templates That Work", "How should you respond to Google reviews?"),
            ("Review Velocity: How Many and How Fast", "How many reviews should you aim for and how quickly?"),
            ("Common Mistakes That Will Hurt You", "What review tactics can hurt your business?"),
            ("Review Management Tools Worth Considering", "Which review management tools are worth considering?"),
            ("The System: Putting It All Together", "What does a repeatable Google review system look like?"),
        ],
    },
    "brand-photography-for-small-business.html": {
        "subtitle": "Small business brand photography should create a reusable library of website, social, and sales assets without overspending on one hero shoot. This guide compares traditional, AI, and hybrid approaches and shows which fits each business type.",
        "cta": "Need the whole visual library built, not just a one-day shoot? We build brand systems with prompts, image libraries, and production workflow.",
        "replacements": [
            ("Why Brand Photography Actually Matters", "Why does brand photography actually matter for a small business?"),
            ("What You Actually Need: The Shot List by Business Type", "What shots does each business type actually need?"),
            ("Path 1: Traditional Photography", "When should a small business choose traditional photography?"),
            ("Path 2: AI Brand Photography", "When should a small business choose AI brand photography?"),
            ("Path 3: The Hybrid Approach (What Most Businesses Should Do)", "What does the hybrid approach look like for most small businesses?"),
            ("DIY Tips for Budget Brands", "What can budget brands do themselves without ruining the result?"),
            ("Building a Visual Library That Lasts", "How do you build a visual library that lasts?"),
            ("Maintaining Visual Consistency", "How do you maintain visual consistency over time?"),
            ("The Bottom Line for Small Business Owners", "What is the bottom line for small business owners?"),
            ("Industry-Specific Guides", "Which industry-specific brand photography guides should you read next?"),
        ],
    },
    "content-repurposing-strategy.html": {
        "subtitle": "Content repurposing works when one strong source asset gets re-cut for each platform's format, intent, and audience instead of being copy-pasted everywhere. This guide shows the system, the workflow, and the automation layer.",
        "cta": "Need a repurposing system that turns one idea into a full week of content? We build the workflow and automation stack.",
        "replacements": [
            ("The Repurposing Pyramid", "What is the content repurposing pyramid?"),
            ("Platform-Specific Reformatting", "How should you reformat content for each platform?"),
            ("What NOT to Repurpose", "What content should you not repurpose?"),
            ("Maintaining Quality Across Formats", "How do you maintain quality across formats?"),
            ("Real Example: One Blog Post Becomes 10 Pieces", "How does one blog post become 10 useful content pieces?"),
            ("Tools and AI for Repurposing", "Which tools and AI workflows help with repurposing?"),
            ("Workflow Automation: The Next Level", "How does workflow automation change content repurposing?"),
            ("The Mindset Shift", "What mindset shift makes repurposing work long term?"),
        ],
    },
    "restaurant-instagram-content-ideas.html": {
        "opening": "The best restaurant Instagram content mixes menu shots, kitchen moments, guest proof, and brand atmosphere so the feed sells the experience, not just the dishes. These 40 ideas are organized by content type so you can actually use them.",
        "cta": "Ideas help, but the visuals still need to stop the scroll. We build restaurant content systems that combine photo direction, templates, and publishing workflow.",
        "replacements": [
            ("Menu Content (8 Ideas)", "What menu content should restaurants post? (8 ideas)"),
            ("Behind-the-Kitchen Content (8 Ideas)", "What behind-the-kitchen content should restaurants post? (8 ideas)"),
            ("Customer &amp; Community Content (8 Ideas)", "What customer community content should restaurants post? (8 ideas)"),
            ("Brand &amp; Vibe Content (8 Ideas)", "What brand vibe content should restaurants post? (8 ideas)"),
            ("Engagement Content (8 Ideas)", "What engagement content should restaurants post? (8 ideas)"),
            ("Phone Photography Tips for Restaurants", "How should restaurants shoot better phone photos?"),
        ],
    },
    "n8n-vs-zapier-vs-make-automation.html": {
        "subtitle": "The right automation tool depends less on headline features and more on your stage: Zapier for speed, Make for visual workflow building, and n8n for flexibility and lower long-run cost. This guide compares them specifically for content operations.",
        "cta": "Need the automation layer chosen and wired into your content system? We build content pipelines that run without daily manual work.",
        "replacements": [
            ("What Each Tool Does (The Quick Version)", "What does each automation tool actually do?"),
            ("The Pricing Breakdown (This Is Where It Gets Real)", "How do n8n, Zapier, and Make compare on pricing?"),
            ("Ease of Use: Honest Assessment", "Which tool is actually easiest to use?"),
            ("Content Marketing Use Cases", "Which content marketing use cases fit each tool best?"),
            ("Integration Count: Does It Matter?", "Does integration count actually matter?"),
            ("The Self-Hosting Advantage (n8n Only)", "Why does n8n's self-hosting option matter?"),
            ("Which One for Which Stage", "Which tool fits each stage of business growth?"),
            ("Real Workflow Example: Daily Brand Content Pipeline", "What does a real daily brand content pipeline look like in each tool?"),
            ("The Verdict", "What is the verdict: n8n, Zapier, or Make?"),
        ],
    },
    "instagram-carousel-strategy.html": {
        "subtitle": "Instagram carousels outperform most other feed formats because they create dwell time, saves, and shares at the same time. This guide breaks down the structure, design rules, and publishing system that make them compound.",
        "cta": "Need a repeatable carousel system instead of one-off design work? We build the templates, visual rules, and workflow.",
        "replacements": [
            ("Why Carousels Outperform Everything Else", "Why do Instagram carousels outperform other feed formats?"),
            ("Anatomy of a High-Performing Carousel", "What does a high-performing carousel look like?"),
            ("Design Principles That Drive Saves", "What design principles drive saves and shares?"),
            ("Content Types That Work as Carousels", "What content types work best as carousels?"),
            ("Posting Frequency and Timing", "How often should you post carousels and when?"),
            ("Caption Strategy for Carousels", "How should you write captions for Instagram carousels?"),
            ("Using AI to Generate Carousel Visuals", "How can AI help generate carousel visuals?"),
            ("Common Carousel Mistakes", "What mistakes kill carousel performance?"),
            ("The Compounding Effect", "Why do carousels compound over time?"),
        ],
    },
    "midjourney-vs-chatgpt-brand-photography.html": {
        "subtitle": "Midjourney is stronger for mood and editorial atmosphere, while ChatGPT is stronger for precision, iteration, and scalable brand production. This guide compares them by image quality, workflow, and practical use case.",
        "cta": "Need a brand photography system built on the right model stack, not trial and error? Start with a free audit.",
        "replacements": [
            ("Image Quality: The Gap Is Narrower Than You Think", "How does image quality compare between Midjourney and ChatGPT?"),
            ("Prompting: Fundamentally Different Approaches", "How do prompting workflows differ between Midjourney and ChatGPT?"),
            ("The Comparison Table", "How do Midjourney and ChatGPT compare side by side?"),
            ("Speed and Workflow: ChatGPT Wins Decisively", "Which tool wins on speed and workflow?"),
            ("Where Midjourney Still Wins", "Where does Midjourney still win?"),
            ("Where ChatGPT Wins", "Where does ChatGPT win?"),
            ("Use Case Breakdown", "Which use cases fit each tool best?"),
            ("Pricing Reality Check", "How do the pricing models actually compare?"),
            ("The Verdict", "What is the verdict on Midjourney versus ChatGPT for brand photography?"),
        ],
    },
    "ai-marketing-for-local-business.html": {
        "subtitle": "A practical AI marketing stack for a local business usually combines copy generation, photo production, scheduling, email automation, and Google Business Profile management for under a few hundred dollars a month. This guide shows the working stack.",
        "cta": "Need the local marketing stack built and connected instead of assembled tool by tool? Start with a free audit.",
        "replacements": [
            ("The Local Business Marketing Challenge", "What makes marketing hard for local businesses?"),
            ("The AI Marketing Stack: What You Actually Need", "What AI marketing stack does a local business actually need?"),
            ("The Real Cost Breakdown", "What does the real cost breakdown look like?"),
            ("Google Business Profile: Your Most Important Asset", "Why is Google Business Profile the most important asset for local businesses?"),
            ("Social Media for Local: What Actually Works", "What social media tactics actually work for local businesses?"),
            ("Email Marketing Automation: Set It and Forget It", "How should local businesses use email automation?"),
            ("Measuring ROI: Keep It Simple", "How should a local business measure marketing ROI?"),
            ("The Weekly Workflow: 3 Hours Total", "What does a 3-hour weekly marketing workflow look like?"),
            ("Start This Week", "What should a local business start this week?"),
        ],
    },
    "instagram-reel-ideas-small-business.html": {
        "opening": "The best Instagram Reel ideas for a small business are fast to film, hook in the first three seconds, and map to a repeatable content category instead of requiring constant new creativity. These 30 ideas are built to be filmed today.",
        "cta": "Need Reels supported by a stronger visual system? We build the photo direction, content templates, and workflow behind the posting.",
        "replacements": [
            ("Behind-the-Scenes (Reels 1-6)", "What behind-the-scenes Reels should a small business film? (1-6)"),
            ("Educational / How-To (Reels 7-12)", "What educational Reels should a small business film? (7-12)"),
            ("Trending / Timely (Reels 13-17)", "What timely or trend-based Reels should a small business film? (13-17)"),
            ("Product Showcase (Reels 18-23)", "What product showcase Reels should a small business film? (18-23)"),
            ("Personal Brand (Reels 24-27)", "What personal-brand Reels should a small business film? (24-27)"),
            ("Engagement Bait (Reels 28-30)", "What engagement-focused Reels should a small business film? (28-30)"),
            ("How to Film These Efficiently", "How do you film these Reels efficiently?"),
        ],
    },
    "how-to-increase-instagram-engagement.html": {
        "opening": "Instagram engagement improves when posts are built for saves, shares, replies, and repeat viewing rather than vanity reach alone. This guide covers the content formats, timing, community habits, and metrics that actually move engagement.",
        "cta": "Need an Instagram system built around engagement and conversion, not random posting? Start with a free audit.",
        "replacements": [
            ("How the Instagram Algorithm Works in 2026", "How does the Instagram algorithm work in 2026?"),
            ("Engagement Rate Benchmarks for 2026", "What engagement benchmarks matter in 2026?"),
            ("Content Formats Ranked by Engagement", "Which content formats drive the most engagement?"),
            ("Posting Times That Actually Matter", "How much do posting times actually matter?"),
            ("Caption Strategies That Drive Engagement", "What caption strategies increase engagement?"),
            ("Community Building: The Underrated Growth Strategy", "Why is community building the underrated Instagram growth strategy?"),
            ("The Visual Consistency Factor", "How does visual consistency affect engagement?"),
            ("What to Track and When to Pivot", "What should you track and when should you pivot?"),
            ("The Engagement Flywheel", "What does the Instagram engagement flywheel look like?"),
        ],
    },
    "diy-branding-vs-hiring-agency.html": {
        "subtitle": "DIY branding is usually best when budget is tight and speed matters, while agencies make more sense when the business can afford strategic depth and production overhead. This guide compares DIY, agency, and the middle-ground system between them.",
        "cta": "Need the middle ground between doing it yourself and hiring a traditional agency? Start with a free audit.",
        "replacements": [
            ("What DIY Branding Actually Looks Like", "What does DIY branding actually look like?"),
            ("What an Agency Actually Delivers", "What does a traditional agency actually deliver?"),
            ("The Real Cost Comparison", "How do DIY branding and agencies compare on cost?"),
            ("The Hidden Cost of Looking Amateur", "What is the hidden cost of looking amateur?"),
            ("When DIY Branding Is the Right Call", "When is DIY branding the right call?"),
            ("When It's Time to Invest in Professional Branding", "When is it time to invest in professional branding?"),
            ("The Problem with Traditional Agencies", "What is the main problem with traditional agencies?"),
            ("The Middle Ground: AI-Powered Brand Systems", "What does the AI-powered middle ground look like?"),
            ("What About the Quality Gap?", "What about the quality gap between DIY and agency work?"),
            ("The Verdict", "What is the verdict on DIY branding versus hiring an agency?"),
        ],
    },
    "ai-photography-for-food-brands.html": {
        "subtitle": "AI photography works well for food brands when you need recurring social, packaging, and seasonal concept imagery, but exact product truth and packaging details still require guardrails. This guide breaks down what AI can do and where it still misses.",
        "cta": "Need a food-brand visual system that keeps seasonal content moving without monthly shoots? Start with a free audit.",
        "replacements": [
            ("What AI Handles Well for Food Brands", "What does AI handle well for food brands?"),
            ("What AI Cannot Do Yet", "What can AI not do yet for food brands?"),
            ("Prompt Strategies for Appetizing Food Shots", "What prompts create better food-brand imagery?"),
            ("Platform-Specific Requirements", "How do platform requirements change food-brand photography?"),
            ("Seasonal Content Planning", "How should food brands plan seasonal content?"),
            ("The Cost Comparison", "How does the cost compare to traditional food photography?"),
            ("Getting Started", "How should a food brand get started with AI photography?"),
        ],
    },
    "how-to-get-clients-on-instagram.html": {
        "opening": "Getting clients on Instagram requires four things working together: a profile that signals the right offer, content that attracts the right buyer, conversations that move to DM, and a clear path from follower to lead. This guide breaks down that system.",
        "cta": "Need an Instagram pipeline that turns attention into real inquiries? Start with a free audit.",
        "replacements": [
            ("Step 1: Fix Your Profile Before You Do Anything Else", "How should you fix your profile before doing anything else?"),
            ("Step 2: Define Your Content Pillars", "How do you define the right content pillars for client acquisition?"),
            ("Step 3: Master the Formats That Drive Reach", "Which formats drive the most useful reach on Instagram?"),
            ("Step 4: Engagement Strategy That Creates Conversations", "What engagement strategy creates real conversations?"),
            ("Step 5: DM Scripts That Convert Without Being Pushy", "What DM scripts convert without feeling pushy?"),
            ("Step 6: Using AI to Create Content at Scale", "How should you use AI to create client-generating content at scale?"),
            ("Step 7: Converting Followers to Leads and Clients", "How do you convert followers into leads and clients?"),
            ("The Posting Schedule That Wins", "What posting schedule gives Instagram the best chance to convert?"),
            ("Measuring What Matters", "What metrics actually matter when Instagram is meant to drive clients?"),
        ],
    },
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def set_subtitle(text: str, new_text: str) -> str:
    new = f'<p class="article-subtitle">{new_text}</p>'
    return re.sub(r'<p class="article-subtitle"[^>]*>.*?</p>', new, text, count=1, flags=re.S)


def set_opening_paragraph(text: str, new_text: str) -> str:
    pattern = re.compile(
        r'(<h1[^>]*>.*?</h1>\s*(?:<(?:div|time)[^>]*>.*?</(?:div|time)>\s*)*)(<p[^>]*>.*?</p>)',
        re.S,
    )
    new = f"<p>{new_text}</p>"
    return pattern.sub(lambda m: m.group(1) + new, text, count=1)


def set_cta_paragraph(text: str, new_text: str) -> str:
    return re.sub(
        r'(<div class="cta-(?:section|box)"[^>]*>\s*(?:<h[23][^>]*>.*?</h[23]>\s*)?<p>).*?(</p>)',
        rf"\1{new_text}\2",
        text,
        count=1,
        flags=re.S,
    )


def main() -> None:
    updated = []
    missing = []
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

        for old, new in config["replacements"]:
            if old not in text:
                missing.append(f"{filename}: missing pattern {old[:70]!r}")
                continue
            text = text.replace(old, new)

        if "cta" in config:
            new_text = set_cta_paragraph(text, config["cta"])
            if new_text == text:
                missing.append(f"{filename}: CTA not updated")
            text = new_text

        if text != original:
            write(path, text)
            updated.append(filename)

    skip_lines = [
        "# Editorial Skips",
        "",
        "- `blog/small-business-branding-mistakes.html`: thin single-H2 structure plus missing FAQ schema; needs a custom rebuild, not a templated pass.",
        "- `blog/small-business-seo-checklist.html`: checklist format needs a custom FAQ/schema rewrite instead of a straight heading conversion.",
        "- `blog/bakery-instagram-content-ideas.html`: low-rank listicle missing FAQ schema; better handled in a food-cluster batch.",
        "- `blog/restaurant-photography-shot-list.html`: shot-list format should be rebuilt with custom section questions and FAQ schema together.",
    ]
    write(SKIPS_PATH, "\n".join(skip_lines) + "\n")

    print("Updated:")
    for name in updated:
        print(f"  - {name}")
    if missing:
        print("\nMissing:")
        for item in missing:
            print(f"  - {item}")


if __name__ == "__main__":
    main()
