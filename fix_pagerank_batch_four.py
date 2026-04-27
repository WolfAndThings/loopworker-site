#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).parent
BLOG_DIR = ROOT / "blog"


PAGES = {
    "flat-lay-photography-guide.html": {
        "subtitle": "A strong flat lay comes from choosing one composition grid, limiting props to a purpose, and keeping the edit consistent across the whole frame. This guide breaks down the exact layouts, surfaces, and workflow that make flat lays look intentional.",
        "cta": "Need flat lays, product shots, and brand visuals built into one repeatable system? Start with a free audit.",
        "replacements": [
            ("The 5 Composition Grids", "What composition grids work best for flat lay photography?"),
            ("Camera Setup: Getting Directly Overhead", "How do you get the camera directly overhead for a flat lay?"),
            ("Props by Industry", "What props work best for flat lays in each industry?"),
            ("Surfaces &amp; Backgrounds Ranked by Cost", "Which surfaces and backgrounds work best for flat lays?"),
            ("Step-by-Step Shooting Process", "What is the step-by-step flat lay shooting process?"),
            ("Phone Editing Workflow (Lightroom Mobile)", "What is a simple Lightroom Mobile workflow for flat lays?"),
            ("7 Common Flat Lay Mistakes", "What mistakes make flat lays look amateur?"),
            ("10 Flat Lay Layout Templates", "What flat lay layout templates should you try?"),
        ],
    },
    "iphone-photography-settings-product-photos.html": {
        "opening": "The best iPhone setup for product photos uses a neutral camera configuration, locked exposure, simple side lighting, and a short editing pass that keeps the product believable. This guide gives the exact settings and measurements to copy.",
        "cta": "Need consistent product imagery without manually rebuilding the shot every time? Start with a free audit.",
        "replacements": [
            ("Before You Touch the Camera App", "What should you change before opening the Camera app?"),
            ("Exact Camera App Settings for the Shot", "What exact Camera app settings should you use for product photos?"),
            ("The Exact Lighting Setup (Household Items Only)", "What lighting setup works with only household items?"),
            ("Composition Rules with Exact Measurements", "What composition rules and measurements improve iPhone product photos?"),
            ("Editing in iPhone Photos App (Exact Slider Values)", "What slider values work in the iPhone Photos app?"),
            ("Editing in Lightroom Mobile (Free Version) — Exact Values", "What exact Lightroom Mobile values work for product photos?"),
            ("Editing in Lightroom Mobile (Free Version) &mdash; Exact Values", "What exact Lightroom Mobile values work for product photos?"),
            ("Background Removal (30 Seconds, No Apps)", "How do you remove the background in 30 seconds without extra apps?"),
            ("Common Mistakes That Ruin iPhone Product Photos", "What mistakes ruin iPhone product photos?"),
            ("When to Skip All of This and Use AI Instead", "When should you skip iPhone shooting and use AI instead?"),
        ],
    },
    "customer-referral-program-ideas.html": {
        "subtitle": "A good referral program makes word of mouth repeatable by choosing the right incentive, asking at the right moment, and tracking the result without adding much overhead. These 12 ideas are organized by the kind of reward you want to offer.",
        "cta": "Need referrals, reviews, and follow-up working as one customer-growth system? Start with a free audit.",
        "replacements": [
            ("Discount-Based Referral Programs", "Which discount-based referral programs work for service businesses?"),
            ("Cash-Based Referral Programs", "Which cash-based referral programs work for service businesses?"),
            ("Experience-Based Referral Programs", "Which experience-based referral programs work best?"),
            ("Community-Based Referral Programs", "Which community-based referral programs work best?"),
            ("Contest-Based Referral Programs", "Which contest-based referral programs work best?"),
            ("How to Ask for Referrals (Without Being Weird)", "How should you ask for referrals without sounding weird?"),
            ("Tracking Without Software", "How can you track referrals without extra software?"),
        ],
    },
    "shopify-store-photography-guide.html": {
        "subtitle": "Shopify product photography needs to do three jobs at once: prove the product, reduce buyer hesitation, and stay technically compliant for search and shopping feeds. This guide covers the image stack, the specs, and the SEO details that matter.",
        "cta": "Need product photos, alt text, and listing visuals built into a conversion system instead of handled piece by piece? Start with a free audit.",
        "replacements": [
            ("Shopify Image Specifications: The Technical Requirements", "What image specs should Shopify product photos use?"),
            ("The 7 Images Every Shopify Listing Needs", "What 7 images does every Shopify listing need?"),
            ("Lifestyle Photography That Actually Converts", "What lifestyle photography actually converts on Shopify?"),
            ("Collection Page Strategy: Visual Merchandising Online", "How should you handle visual merchandising on Shopify collection pages?"),
            ("SEO Alt Text: The Traffic Driver You're Ignoring", "How should you write Shopify image alt text for SEO?"),
            ("File Naming: Another Free SEO Win", "How should you name image files for Shopify SEO?"),
            ("DIY Product Photography Setup: $150 Budget", "What does a $150 DIY Shopify product-photo setup look like?"),
            ("Image Optimization for Page Speed", "How should you optimize Shopify images for page speed?"),
            ("Google Shopping Image Requirements", "What image requirements does Google Shopping enforce?"),
            ("Common Shopify Photography Mistakes", "What Shopify photography mistakes hurt conversion?"),
            ("AI-Enhanced Product Photography", "How can AI enhance Shopify product photography?"),
        ],
    },
    "med-spa-before-after-photos.html": {
        "subtitle": "Before-and-after photos build trust when the setup is standardized, the lighting is controlled, the consent process is clear, and the results are presented without exaggeration. This guide shows how to make that system repeatable inside a med spa.",
        "cta": "Need before-and-after content, compliance, and social posting turned into one repeatable system? Start with a free audit.",
        "replacements": [
            ("Why Before-and-After Photos Matter More Than Any Other Content", "Why do before-and-after photos matter so much for med spas?"),
            ("Set Up a Dedicated Photo Station", "How should a med spa set up a dedicated photo station?"),
            ("Lighting Rules", "What lighting rules keep before-and-after photos consistent?"),
            ("Angles and Positioning", "How should you standardize angles and positioning?"),
            ("Consent: Getting It Right", "How should med spas handle photo consent correctly?"),
            ("What to Show (and What Not to Show)", "What should a med spa show and avoid in before-and-after photos?"),
            ("How to Post Before-and-After Photos", "How should med spas post before-and-after photos?"),
            ("Building a System That Runs Itself", "How do you build a before-and-after system that runs itself?"),
        ],
    },
    "med-spa-instagram-content-ideas.html": {
        "subtitle": "The best med spa Instagram content usually falls into five buckets: results, education, behind-the-scenes proof, social proof, and objection handling. These 25 ideas are grouped so your team can batch them instead of inventing posts from scratch.",
        "cta": "Need med spa Instagram content tied to a real booking system instead of random posting? Start with a free audit.",
        "replacements": [
            ("Before &amp; After Content (Ideas 1-5)", "What before-and-after content should a med spa post in ideas 1 to 5?"),
            ("What before-and-after content should a med spa post? (Ideas 1-5)", "What before-and-after content should a med spa post in ideas 1 to 5?"),
            ("Educational Content (Ideas 6-12)", "What educational Instagram content should a med spa post in ideas 6 to 12?"),
            ("What educational Instagram content should a med spa post? (Ideas 6-12)", "What educational Instagram content should a med spa post in ideas 6 to 12?"),
            ("Behind the Scenes (Ideas 13-17)", "What behind-the-scenes Instagram content should a med spa post in ideas 13 to 17?"),
            ("What behind-the-scenes Instagram content should a med spa post? (Ideas 13-17)", "What behind-the-scenes Instagram content should a med spa post in ideas 13 to 17?"),
            ("Social Proof (Ideas 18-21)", "What social proof content should a med spa post in ideas 18 to 21?"),
            ("What social proof content should a med spa post? (Ideas 18-21)", "What social proof content should a med spa post in ideas 18 to 21?"),
            ("FAQ and Myth-Busting (Ideas 22-25)", "What FAQ and myth-busting content should a med spa post in ideas 22 to 25?"),
            ("What FAQ and myth-busting content should a med spa post? (Ideas 22-25)", "What FAQ and myth-busting content should a med spa post in ideas 22 to 25?"),
        ],
    },
    "med-spa-marketing-ideas.html": {
        "subtitle": "The highest-leverage med spa marketing ideas usually start with Google Business Profile, reviews, before-and-afters, referrals, and follow-up before you spend meaningfully on ads. This guide organizes 15 ideas by budget so you can stage them in the right order.",
        "cta": "Need the local marketing stack, content system, and booking flow aligned for your med spa? Start with a free audit.",
        "replacements": [
            (
                '<div class="idea-card fade-up">\n        <div class="idea-num">Strategy #1 &mdash; Free</div>',
                '<h2 class="fade-up">What free med spa marketing ideas should you start with?</h2>\n\n    <div class="idea-card fade-up">\n        <div class="idea-num">Strategy #1 &mdash; Free</div>',
            ),
            (
                '<div class="idea-card fade-up">\n        <div class="idea-num">Strategy #6 &mdash; Free-$20/mo</div>',
                '<h2 class="fade-up">What low-cost med spa marketing ideas should you add next?</h2>\n\n    <div class="idea-card fade-up">\n        <div class="idea-num">Strategy #6 &mdash; Free-$20/mo</div>',
            ),
            (
                '<div class="idea-card fade-up">\n        <div class="idea-num">Strategy #12 &mdash; $100-500/mo</div>',
                '<h2 class="fade-up">What paid med spa marketing ideas should you scale once the basics work?</h2>\n\n    <div class="idea-card fade-up">\n        <div class="idea-num">Strategy #12 &mdash; $100-500/mo</div>',
            ),
        ],
    },
    "med-spa-social-media-strategy.html": {
        "subtitle": "A med spa social strategy works when platform choice, content pillars, DM response time, and booking handoff are treated as one system instead of separate tasks. This guide breaks down that system in practical terms.",
        "cta": "Need your med spa social content connected to DMs, reviews, and bookings instead of managed in fragments? Start with a free audit.",
        "replacements": [
            ("Why Most Med Spa Social Media Fails", "Why does most med spa social media fail?"),
            ("Choose Your Platforms (And Ignore the Rest)", "Which platforms should a med spa focus on?"),
            ("The 5 Content Pillars for Med Spas", "What content pillars should a med spa use on social media?"),
            ("Posting Frequency That Actually Works", "How often should a med spa post on social media?"),
            ("The DM-to-Booking System", "How should a med spa turn DMs into bookings?"),
            ("Educational Content That Books Appointments", "What educational content books appointments for med spas?"),
            ("Measuring What Matters", "What social media metrics matter for a med spa?"),
        ],
    },
    "email-marketing-for-small-business.html": {
        "subtitle": "Email marketing for a small business works best when list growth, welcome automation, campaign cadence, and segmentation are all planned before the first newsletter goes out. This guide shows how to set that system up from zero.",
        "cta": "Need email, content, and automation working together instead of as separate tools? Start with a free audit.",
        "replacements": [
            ("Why Email Still Beats Social Media", "Why does email still beat social media for small businesses?"),
            ("Choosing a Platform: The 2026 Landscape", "Which email platform should a small business choose in 2026?"),
            ("Building Your List from Scratch", "How should a small business build an email list from scratch?"),
            ("The Welcome Sequence: Your First 5 Emails", "What should be in a first 5-email welcome sequence?"),
            ("Newsletter vs. Promotional: Finding the Balance", "How do you balance newsletter and promotional emails?"),
            ("Using AI to Write Emails Faster", "How should you use AI to write emails faster?"),
            ("Automation Sequences Beyond Welcome", "What automation sequences should you build after the welcome series?"),
            ("Segmentation Basics", "What segmentation basics matter for a small business?"),
            ("Metrics That Actually Matter", "What email metrics actually matter?"),
            ("Common Mistakes That Kill Email Lists", "What mistakes kill small business email lists?"),
            ("The Setup Timeline: Week by Week", "What should an email marketing setup timeline look like?"),
        ],
    },
    "facebook-ads-small-business-guide.html": {
        "subtitle": "Facebook and Instagram ads work for small businesses when campaign structure, audience layering, creative testing, and tracking are set up before budget scale. This guide shows the framework that keeps spend disciplined.",
        "cta": "Need paid social, creative, and conversion tracking aligned before you scale spend? Start with a free audit.",
        "replacements": [
            ("The Campaign Structure That Works", "What Facebook campaign structure works for small businesses?"),
            ("Audience Targeting: The Three Layers", "How should a small business layer Facebook audiences?"),
            ("Creative Formats That Work", "What creative formats work best in Facebook and Instagram ads?"),
            ("Budget Tiers: What's Realistic", "What budget tiers are realistic for a small business?"),
            ("The Meta Pixel: Install It Now", "Why should you install the Meta Pixel immediately?"),
            ("Ad Copy Templates", "What ad copy templates work for Facebook ads?"),
            ("Common Mistakes", "What Facebook ad mistakes waste the most money?"),
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
