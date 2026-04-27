#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).parent
BLOG_DIR = ROOT / "blog"


PAGES = {
    "restaurant-social-media-strategy.html": {
        "subtitle": "A restaurant social media strategy works when one platform gets owned first, content pillars are repeated consistently, staff contributions are simple, and performance is judged by reservations and foot traffic instead of vanity metrics. This guide lays out that system.",
        "cta": "Need a restaurant content system that actually drives covers instead of random posting? Start with a free audit.",
        "replacements": [
            ("Platform Priority: Where to Focus First", "Which platform should a restaurant focus on first?"),
            ("The 5 Content Pillars for Restaurants", "What content pillars should a restaurant post consistently?"),
            ("Posting Frequency and Best Times", "How often should a restaurant post and when?"),
            ("Engagement Tactics That Work for Restaurants", "What engagement tactics actually work for restaurants?"),
            ("Monthly Content Calendar Template", "What should a monthly restaurant content calendar look like?"),
            ("Staff Involvement Strategy", "How should restaurant staff contribute to content?"),
            ("What Metrics Actually Matter for Restaurants", "What metrics actually matter for restaurant social media?"),
            ("Common Mistakes Restaurants Make on Social Media", "What restaurant social media mistakes should you avoid?"),
        ],
    },
    "restaurant-menu-photography.html": {
        "subtitle": "Restaurant menu photography works best as a one-day production system: plan the shot list, control the light, standardize angles and styling, then edit and organize the files so every dish can keep selling across menus, delivery apps, and social media. This guide walks through that workflow.",
        "cta": "Need a menu photo library that sells every item instead of just your hero dishes? Start with a free audit.",
        "replacements": [
            ("Step 1: Plan the Shoot Before You Cook", "How should you plan a menu photoshoot before the kitchen starts cooking?"),
            ("Step 2: The Lighting Setup", "What lighting setup works best for restaurant menu photography?"),
            ("Step 3: Angles by Dish Type", "What camera angles work best for each type of dish?"),
            ("Step 4: Plating and Styling for the Camera", "How should you plate and style dishes for the camera?"),
            ("Step 5: Camera Settings (Phone or DSLR)", "What camera settings should you use for menu photography?"),
            ("Step 6: Backgrounds and Surfaces", "What backgrounds and surfaces work best for menu photos?"),
            ("Step 7: The Editing Workflow", "What editing workflow keeps menu photos consistent?"),
            ("Step 8: Organizing the Photo Library", "How should you organize a restaurant photo library?"),
            ("Step 9: Using Your Menu Photos", "Where should you use menu photos after the shoot?"),
            ("The Complete Shoot Day Timeline", "What does a complete menu shoot day timeline look like?"),
            ("Common Mistakes to Avoid", "What menu photography mistakes should you avoid?"),
        ],
    },
    "ai-photography-prompt-formulas.html": {
        "subtitle": "AI photography prompts work best when they describe the subject, environment, lighting, camera language, and one believable detail instead of vague quality words. These formulas turn that structure into repeatable templates you can reuse across generators.",
        "cta": "Need prompt templates that produce usable brand visuals instead of obvious AI filler? Start with a free audit.",
        "replacements": [
            ("Formula 1: Product Hero Shot", "What prompt formula works for a product hero shot?"),
            ("Formula 2: Lifestyle Scene", "What prompt formula works for a lifestyle scene?"),
            ("Formula 3: Flat Lay", "What prompt formula works for a flat lay?"),
            ("Formula 4: Food / Menu", "What prompt formula works for food or menu photography?"),
            ("Formula 5: Interior / Space", "What prompt formula works for interiors or spaces?"),
            ("Formula 6: Portrait / Headshot", "What prompt formula works for portraits or headshots?"),
            ("Formula 7: Behind-the-Scenes", "What prompt formula works for behind-the-scenes images?"),
            ("Formula 8: Detail / Texture", "What prompt formula works for detail or texture shots?"),
            ("Formula 9: Environmental / Exterior", "What prompt formula works for environmental or exterior shots?"),
            ("Formula 10: Social Proof / UGC Style", "What prompt formula works for social-proof or UGC-style images?"),
            ("The Anti-AI Word List", "Which prompt words make AI images look fake?"),
            ("Camera + Film Stock Cheat Sheet", "Which camera and film stock references should you use in prompts?"),
            ("Putting It All Together", "How do you combine these prompt formulas into one workflow?"),
        ],
    },
    "ai-photography-for-salons-barbershops.html": {
        "opening": "AI photography for salons and barbershops works when it fills the gaps between real client transformations: brand visuals, promo content, Google profile images, seasonal campaigns, and social posts that would otherwise never get produced consistently. This guide explains where it helps and where it does not replace real work.",
        "cta": "Need a salon visual system that fills Instagram and Google without constant reshoots? Start with a free audit.",
        "replacements": [
            ("The Real Problem with Salon Photography", "What is the real problem with salon and barbershop photography?"),
            ("What AI Photography Actually Looks Like for Salons", "What does AI photography actually look like for salons and barbershops?"),
            ("Social Media Content That Runs on Autopilot", "How can salon social media content run on autopilot?"),
            ("Google Business Profile: The Photos Most Salons Ignore", "Which Google Business Profile photos do salons usually ignore?"),
            ("Building a Visual Brand System for Your Salon", "How do you build a visual brand system for a salon?"),
            ("What AI Photography Cannot Replace", "What can AI photography not replace for salons?"),
            ("Getting Started: A Practical Roadmap", "What is the practical roadmap for getting started?"),
        ],
    },
    "ai-video-production-for-brands.html": {
        "opening": "AI video production is now practical for brands that need Reels, promos, demos, and ad creative at a pace traditional production cannot support. The real advantage is not novelty. It is building a repeatable pipeline that turns briefs, scripts, images, voiceover, and editing into publishable video faster and cheaper.",
        "cta": "Need a brand video system that can produce promos and social clips without traditional production delays? Start with a free audit.",
        "replacements": [
            ("The AI Video Landscape in 2026", "What does the AI video landscape look like in 2026?"),
            ("Four Video Types Every Brand Needs", "What video types does every brand need?"),
            ("The Production Pipeline: How It All Connects", "How should an AI video production pipeline fit together?"),
            ("The Engagement Case for Video", "Why does video outperform static content on engagement?"),
            ("What AI Video Cannot Do (Yet)", "What can AI video not do yet?"),
            ("Getting Started: The Minimum Viable Video System", "What is the minimum viable AI video system for a brand?"),
        ],
    },
    "bright-airy-food-photography.html": {
        "subtitle": "Bright and airy food photography depends on soft directional light, light surfaces, disciplined styling, and repeatable editing, not just raising exposure until the image looks washed out. This guide breaks down the exact setup that creates that clean editorial look.",
        "cta": "Need food photography that feels bright, consistent, and actually appetizing across every channel? Start with a free audit.",
        "replacements": [
            ("Natural Light: The Only Light Source You Need", "Why is natural light the best light source for bright food photography?"),
            ("Backgrounds and Surfaces", "What backgrounds and surfaces work best for bright food photography?"),
            ("Camera Settings", "What camera settings should you use for bright food photography?"),
            ("Step-by-Step Lightroom Editing", "How should you edit bright food photos in Lightroom?"),
            ("Foods That Work Best in Bright Photography", "Which foods work best with a bright and airy style?"),
            ("Overhead vs. Angle: When to Use Each", "When should you shoot overhead versus at an angle?"),
            ("Common Mistakes", "What bright food photography mistakes should you avoid?"),
        ],
    },
    "dark-moody-food-photography.html": {
        "subtitle": "Dark and moody food photography works when you control a single light source, deepen shadows intentionally, choose darker props and surfaces, and edit for drama without muddying the food. This guide shows how to build that look from capture through export.",
        "cta": "Need darker editorial food photos that still make the dish look worth ordering? Start with a free audit.",
        "replacements": [
            ("The One-Light Setup", "What one-light setup creates dark and moody food photography?"),
            ("Background Materials", "What background materials work best for dark food photography?"),
            ("Camera Settings", "What camera settings should you use for dark food photography?"),
            ("Composition for Dark Photography", "How should you compose dark food photography?"),
            ("Step-by-Step Lightroom Editing", "How should you edit dark food photos in Lightroom?"),
            ("Foods That Work Best in Dark Photography", "Which foods work best with a dark and moody style?"),
            ("Common Mistakes", "What dark food photography mistakes should you avoid?"),
        ],
    },
    "linkedin-personal-brand-guide.html": {
        "subtitle": "A LinkedIn personal brand grows when the profile is positioned clearly, content formats are chosen deliberately, posting cadence is sustainable, and engagement turns visibility into real conversations. This guide explains how to make LinkedIn produce business, not just impressions.",
        "cta": "Need a personal brand system that turns LinkedIn visibility into inbound leads? Start with a free audit.",
        "replacements": [
            ("Profile Optimization Checklist", "How should you optimize a LinkedIn profile for a personal brand?"),
            ("Content Types That Work on LinkedIn", "What content types work best on LinkedIn?"),
            ("Posting Cadence and Timing", "How often should you post on LinkedIn and when?"),
            ("The Engagement Strategy", "What engagement strategy helps a LinkedIn personal brand grow?"),
            ("Converting Connections to Clients", "How do you convert LinkedIn connections into clients?"),
        ],
    },
    "personal-brand-content-plan.html": {
        "subtitle": "A personal brand content plan works when LinkedIn, Instagram, and email each do a different job across a 90-day cycle: build positioning, prove consistency, and convert attention into inquiries. This guide lays out that sequence for coaches and consultants.",
        "cta": "Need a 90-day personal brand content system instead of random posting bursts? Start with a free audit.",
        "replacements": [
            ("The Personal Brand Content Stack: LinkedIn + Instagram + Email", "What content stack should power a personal brand?"),
            ("Days 1-30: Foundation", "What should happen in days 1 to 30 of a personal brand content plan?"),
            ("Days 31-60: Consistency", "What should happen in days 31 to 60 of a personal brand content plan?"),
            ("Days 61-90: Conversion", "What should happen in days 61 to 90 of a personal brand content plan?"),
            ("20 Content Ideas for Coaches and Consultants", "What content ideas work for coaches and consultants?"),
            ("The Authority Stack: How Each Piece Builds on the Last", "How does the authority stack build over time?"),
            ("Headshot and Brand Photo Checklist", "What should a headshot and brand photo checklist include?"),
        ],
    },
    "email-subject-lines-small-business.html": {
        "subtitle": "Small-business email subject lines get opened when they promise specific value, match the email type, and create just enough curiosity or urgency without reading like spam. This guide groups 75 examples by scenario so the pattern is obvious.",
        "cta": "Need your email strategy tied to stronger offers and better conversion paths, not just better subject lines? Start with a free audit.",
        "replacements": [
            ("The 4 Formulas Behind Every Great Subject Line", "What formulas make email subject lines work?"),
            ("Welcome Emails (1-10)", "What welcome email subject lines get opened?"),
            ("Promotional / Sale Emails (11-22)", "What promotional or sale subject lines work best?"),
            ("Abandoned Cart (23-32)", "What abandoned-cart subject lines bring shoppers back?"),
            ("Newsletter / Content (33-45)", "What newsletter and content subject lines get more opens?"),
            ("Re-Engagement (46-55)", "What re-engagement subject lines wake up inactive subscribers?"),
            ("Seasonal and Holiday (56-63)", "What seasonal and holiday subject lines stand out?"),
            ("Product Launch (64-70)", "What product-launch subject lines create urgency?"),
            ("Social Proof and Testimonial (71-75)", "What social-proof and testimonial subject lines build trust?"),
            ("A/B Testing: How to Find Your Best Subject Lines", "How should you A/B test email subject lines?"),
            ("What NOT to Do (Spam Triggers and Mistakes)", "What email subject line mistakes should you avoid?"),
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
