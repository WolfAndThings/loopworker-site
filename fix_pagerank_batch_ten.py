#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).parent
BLOG_DIR = ROOT / "blog"


PAGES = {
    "phone-photography-lighting-hacks.html": {
        "subtitle": "Good phone photography starts with light control, not expensive gear. These 10 setups show how to shape light with ordinary household items so product shots, headshots, and food photos look more intentional immediately.",
        "cta": "Need stronger brand photos from the gear you already have? Start with a free audit.",
        "replacements": [
            ("Setup 1: The Window Side Light", "What does the window side-light setup look like?"),
            ("Setup 2: Window + White Poster Board Reflector", "How does a white poster-board reflector improve window light?"),
            ("Setup 3: Aluminum Foil Reflector", "When should you use an aluminum foil reflector?"),
            ("Setup 4: Bedsheet Window Diffuser", "How do you use a bedsheet as a window diffuser?"),
            ("Setup 5: Desk Lamp Side Light", "How should you use a desk lamp as side light?"),
            ("Setup 6: Phone Flashlight as Key Light", "Can a phone flashlight work as a key light?"),
            ("Setup 7: Laptop Screen as Soft Light", "When does a laptop screen work as soft light?"),
            ("Setup 8: Bathroom Light Bar", "How can a bathroom light bar help phone photography?"),
            ("Setup 9: White Wall Bounce", "How do you use a white wall to bounce light?"),
            ("Setup 10: Black Paper Negative Fill", "How does black paper create negative fill?"),
            ("Quick Reference Table", "Which lighting setup should you use in each situation?"),
        ],
    },
    "smartphone-food-photography-mistakes.html": {
        "subtitle": "Most smartphone food-photo problems come from a small set of repeated mistakes: bad light, wrong angle, poor timing, or sloppy cleanup. This guide breaks each one down so you can fix the photo before you waste time editing it.",
        "cta": "Need food content that actually makes the dish look worth ordering? Start with a free audit.",
        "replacements": [
            ("Mistake #1: Shooting Under Overhead Lights", "Why do overhead lights ruin smartphone food photos?"),
            ("Mistake #2: Using the Flash", "Why should you avoid flash in food photography?"),
            ("Mistake #3: Wrong Angle for the Dish", "How do you choose the right angle for each dish?"),
            ("Mistake #4: Too Far From the Food", "How close should you get to the food?"),
            ("Mistake #5: Dirty Plate Rims", "Why do dirty plate rims matter in food photos?"),
            ("Mistake #6: Shooting Cold Food", "Why should you shoot food while it is fresh?"),
            ("Mistake #7: Over-Editing", "How do you avoid over-editing food photos?"),
            ("Mistake #8: Using the Front-Facing Camera", "Why should you avoid the front-facing camera?"),
            ("Mistake #9: Digital Zoom", "Why is digital zoom a mistake for food photos?"),
            ("Mistake #10: Cluttered Background", "How do you fix a cluttered food-photo background?"),
            ("Mistake #11: Not Locking Exposure", "Why should you lock exposure on a phone camera?"),
            ("Mistake #12: One Shot and Done", "Why should you never stop at one shot?"),
        ],
    },
    "social-media-not-working-small-business.html": {
        "subtitle": "When small-business social media is not working, the issue is usually structural: weak hooks, inconsistent cadence, no CTA, the wrong content mix, or a feed that looks incoherent. This guide helps you diagnose which problem is actually blocking results.",
        "cta": "Need a clearer diagnosis before you keep posting into the void? Start with a free audit.",
        "replacements": [
            ("Problem #1: Your Hooks Are Weak", "Are your hooks too weak to stop the scroll?"),
            ("Problem #2: You Never Ask for Anything", "Are you forgetting to ask viewers to do anything?"),
            ("Problem #3: You Post in Bursts, Then Disappear", "Are you posting in bursts instead of consistently?"),
            ("Problem #4: Your Content Mix Is Wrong", "Is your content mix pushing people away?"),
            ("Problem #5: Your Feed Looks Like 5 Different Businesses", "Does your feed look like five different businesses?"),
            ("How Many of These Apply to You?", "How many of these problems apply to your business?"),
        ],
    },
    "ai-photography-for-interior-designers.html": {
        "subtitle": "AI photography helps interior designers fill portfolio gaps, pitch future-state concepts, and maintain a steady content pipeline without waiting for every new project to be fully shot. This guide shows where it adds leverage and where it cannot replace real project photography.",
        "cta": "Need a steadier interior-design content pipeline without waiting on the next installed project? Start with a free audit.",
        "replacements": [
            ("The Content Problem in Interior Design", "What content problem do interior designers actually have?"),
            ("What AI Photography Does Well for Designers", "What does AI photography do well for interior designers?"),
            ("What AI Cannot Do for Interior Designers", "What can AI not do for interior designers?"),
            ("Prompt Strategies for Interior Photography", "What prompt strategies work for interior-design imagery?"),
            ("A Social Content Calendar for Interior Designers", "What should an AI-assisted content calendar look like for interior designers?"),
            ("The Competitive Advantage", "What competitive advantage does AI photography create for designers?"),
        ],
    },
    "ai-photography-for-wedding-vendors.html": {
        "subtitle": "AI photography gives wedding vendors more editorial content between real events, which matters when the business depends on a constant stream of fresh visuals for Pinterest, Instagram, venue listings, and sales collateral. This guide shows how to use it without confusing it for documentary wedding coverage.",
        "cta": "Need wedding-brand visuals that keep marketing moving between real events? Start with a free audit.",
        "replacements": [
            ("Why Wedding Vendors Need Endless Visual Content", "Why do wedding vendors need so much visual content?"),
            ("Content Types by Vendor Category", "What content types matter for each wedding vendor category?"),
            ("What AI Generates Well vs. What Needs Real Photos", "What can AI generate well and what still needs real photos?"),
            ("Pinterest Strategy with AI Content", "How should wedding vendors use AI content on Pinterest?"),
            ("Seasonal Content Planning", "How should wedding vendors plan seasonal content?"),
            ("The Cost Savings", "What does AI change on cost for wedding vendors?"),
            ("Making It Work", "How should a wedding vendor actually make AI content work?"),
        ],
    },
    "small-business-social-media-mistakes.html": {
        "subtitle": "Most small-business social media mistakes are not creative failures. They are operational ones: no plan, weak copy, inconsistent posting, missing CTAs, and visuals that never become recognizable. This guide shows how to spot and fix each one.",
        "cta": "Need to fix the structural mistakes that keep your social media from converting? Start with a free audit.",
        "replacements": [
            ("Mistake #1: Posting Without a Plan", "What happens when you post without a plan?"),
            ("Mistake #2: No Hook in the First Line", "Why does a missing hook kill performance?"),
            ("Mistake #3: Generic, Forgettable Captions", "Why do generic captions hurt social media results?"),
            ("Mistake #4: Inconsistent Posting", "What does inconsistent posting do to growth?"),
            ("Mistake #5: Only Posting Promotions", "Why is posting only promotions a mistake?"),
            ("Mistake #6: Ignoring DMs and Comments", "Why do ignored DMs and comments hurt social media?"),
            ("Mistake #7: No Call-to-Action", "What happens when you forget a call to action?"),
            ("Mistake #8: Chasing Followers Over Customers", "Why should you prioritize customers over follower count?"),
            ("Mistake #9: Copying Big Brand Strategies", "Why does copying big-brand strategy fail for small businesses?"),
            ("Mistake #10: Not Using Video", "Why is avoiding video a mistake?"),
            ("Mistake #11: No Visual Consistency", "What does a lack of visual consistency signal?"),
        ],
    },
    "headshot-tips-small-business.html": {
        "subtitle": "Small-business headshots do not have to mean booking a photographer for every person immediately. This guide shows when DIY works, when AI is useful, and when paying a pro is actually the smarter move.",
        "cta": "Need team photos that look consistent across LinkedIn, your website, and Google? Start with a free audit.",
        "replacements": [
            ("The DIY Headshot: $0", "How do you take a DIY headshot for free?"),
            ("Camera Settings for Headshots", "What camera settings work best for headshots?"),
            ("Editing Headshots", "How should you edit headshots?"),
            ("AI Headshot Generators", "When do AI headshot generators make sense?"),
            ("Hiring a Photographer: What to Expect", "What should you expect when hiring a photographer for headshots?"),
            ("Platform-Specific Requirements", "What headshot requirements matter by platform?"),
            ("Team Headshot Day: 10+ People in 2 Hours", "How do you run a team headshot day efficiently?"),
        ],
    },
    "call-to-action-examples.html": {
        "subtitle": "Calls to action work when the ask matches the platform, the stage of intent, and the exact next step you want someone to take. This guide organizes 50 CTA examples so you can stop defaulting to the same weak closing line everywhere.",
        "cta": "Need stronger content and landing pages so your CTA has something worth clicking? Start with a free audit.",
        "replacements": [
            ("The Psychology Behind CTAs That Work", "What makes a CTA actually work?"),
            ("Instagram CTAs (Bio, Caption, Story)", "What CTA examples work on Instagram?"),
            ("Website CTAs (Hero, Popup, Footer)", "What CTA examples work on websites?"),
            ("Email CTAs (Subject, Body, Button)", "What CTA examples work in email?"),
            ("Facebook CTAs", "What CTA examples work on Facebook?"),
            ("LinkedIn CTAs", "What CTA examples work on LinkedIn?"),
            ("Landing Page CTAs", "What CTA examples work on landing pages?"),
            ("Button Text vs. Link Text vs. Caption CTA", "How should button text, link text, and caption CTAs differ?"),
            ("A/B Testing Your CTAs", "How should you A/B test CTAs?"),
            ("What NOT to Do", "What CTA mistakes should you avoid?"),
        ],
    },
    "ai-photography-for-med-spas.html": {
        "opening": "AI photography helps med spas fill the content gap between what is safe to show, what patients will consent to, and what the brand still needs for social, staff, facility, and campaign marketing. This guide shows where it solves the privacy and production problem and where it still cannot replace real outcomes.",
        "cta": "Need a med spa visual system that respects privacy but still gives marketing enough to publish? Start with a free audit.",
        "replacements": [
            ("The Content Problem Every Med Spa Faces", "What content problem does every med spa face?"),
            ("Why AI Photography Solves the Patient Privacy Problem", "How does AI photography help with patient privacy?"),
            ("Treatment Room and Facility Photography", "How should med spas use AI for facility and treatment-room visuals?"),
            ("Staff Headshots and Team Presentation", "How should med spas handle staff headshots and team presentation?"),
            ("Social Media Content for Med Spas", "What social media content should a med spa build with AI?"),
            ("What AI Photography Cannot Do for Med Spas", "What can AI photography not do for med spas?"),
            ("Building Your Med Spa Visual System", "How do you build a med spa visual system?"),
            ("Cost Comparison: Traditional vs. AI Photography", "How does AI compare to traditional photography on cost?"),
            ("Common Mistakes to Avoid", "What med spa AI-photography mistakes should you avoid?"),
            ("Getting Started", "How should a med spa get started with AI photography?"),
        ],
    },
    "branding-checklist-small-business.html": {
        "opening": "A branding checklist helps a small business turn something vague into a sequence: foundation first, then visual identity, then digital presence, then content. This guide organizes the work so you can build a recognizable brand without guessing what comes next.",
        "cta": "Need help turning a loose brand into a usable system across website, visuals, and content? Start with a free audit.",
        "replacements": [
            ("Phase 1: Brand Foundation", "What should a small business complete in brand foundation?"),
            ("Phase 2: Visual Identity", "What should a small business complete in visual identity?"),
            ("Phase 3: Digital Presence", "What should a small business complete in digital presence?"),
            ("Phase 4: Content System", "What should a small business complete in its content system?"),
            ("How to Work Through This Checklist", "How should you work through a branding checklist?"),
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
