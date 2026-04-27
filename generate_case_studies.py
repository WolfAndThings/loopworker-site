#!/usr/bin/env python3
"""
Case Study Image Generator — kie.ai ChatGPT (gpt4o-image)
Simple prompts. No camera locks. No color locks. No logos. Let ChatGPT cook.

Usage:
    python generate_case_studies.py
    python generate_case_studies.py --brand myburger
"""

import os
import time
import argparse
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / "LoopWorker" / ".env")

API_BASE = "https://api.kie.ai/api/v1"
GENERATE_URL = f"{API_BASE}/gpt4o-image/generate"
STATUS_URL = f"{API_BASE}/gpt4o-image/record-info"
KIE_KEY = os.environ.get("KIE_KEY", "")

OUTPUT_DIR = Path(__file__).parent / "images" / "case_studies"
POLL_INTERVAL = 10
MAX_POLLS = 30

PROMPTS = {
    "myburger": [
        {
            "name": "hero_counter",
            "prompt": (
                "A smash burger on a paper-lined red plastic tray at a diner counter, shot from slightly above. "
                "Two toasted brioche buns, melted American cheese dripping over the edges, caramelized onions. "
                "Condensation on a glass bottle next to it. The counter is worn laminate. "
                "Behind the counter, blurred motion of a cook in a black apron. Direct flash catching the cheese shine. "
                "Warm overhead fluorescents. Slight grain, real photograph feel. 2:3 vertical, no text overlays."
            ),
        },
        {
            "name": "social_booth",
            "prompt": (
                "Three friends in their mid-20s crammed into a booth at a burger restaurant, mid-laugh, "
                "two of them holding burgers with both hands. One has sauce on their chin. "
                "Crumpled wax paper, scattered fries, half-empty drinks on the table. Worn red vinyl booth. "
                "Warm overhead light and afternoon sun from the window. Background customers blurred. "
                "Feels like a real candid photo, not posed. 2:3 vertical, no text overlays."
            ),
        },
        {
            "name": "detail_smash",
            "prompt": (
                "Extreme close-up of a spatula pressing a beef patty flat onto a hot griddle. "
                "Grease splattering, visible sear marks, steam rising. "
                "Cook's hand in a black glove partially in frame. Griddle seasoned and darkened from years of use. "
                "Everything behind the patty is a warm golden blur. "
                "Must look like a real photograph. 2:3 vertical, no text overlays."
            ),
        },
        {
            "name": "environmental_storefront",
            "prompt": (
                "Wide shot of a casual burger restaurant storefront at golden hour. "
                "Warm interior light glowing through large windows. "
                "A family approaching the entrance — dad holding the door, kid running ahead. "
                "Parking lot with a couple cars. Golden light hitting the building, long shadows on pavement. "
                "Real and natural, not staged. 2:3 vertical, no text overlays."
            ),
        },
        {
            "name": "action_handoff",
            "prompt": (
                "Medium shot of a counter worker in a black apron sliding a tray of burgers and fries "
                "across the counter toward a customer whose hands are reaching for it. "
                "Worker smiling naturally, not looking at camera. Warm overhead lights, stainless steel behind the counter. "
                "Slight motion blur on the sliding tray. Real photograph energy. 2:3 vertical, no text overlays."
            ),
        },
        {
            "name": "closing_latenight",
            "prompt": (
                "A single half-eaten burger on a tray sitting alone on a table by the window at night. "
                "Outside is dark — streetlights and car headlights blurred. Crumpled napkin and empty drink cup. "
                "The restaurant is warm and slightly empty, end of the night. "
                "One employee wiping down a table in the far background, blurred. "
                "Quiet, real, end-of-day energy. 2:3 vertical, no text overlays."
            ),
        },
    ],
    "marina": [
        {
            "name": "hero_consultation",
            "prompt": (
                "A female patient in her mid-30s sitting in a modern medspa treatment chair, "
                "having a natural conversation with a female aesthetician in a clean white coat. "
                "The aesthetician is gesturing toward the patient's jawline with one hand, holding a tablet in the other. "
                "Bright airy treatment room, large window with diffused natural light. "
                "Both women relaxed and genuine, mid-conversation, not posed. "
                "Skin has visible pores and natural texture. Real photograph. 2:3 vertical, no text overlays."
            ),
        },
        {
            "name": "portrait_patient",
            "prompt": (
                "Tight portrait of a woman in her early 40s, face slightly turned three-quarter angle, "
                "soft closed-lip smile. Thin-strap cream camisole. "
                "Real skin — faint laugh lines, natural brows, light freckles across the nose. "
                "Soft window light from the right. Background is a warm beige wall, out of focus. "
                "She looks healthy, not perfect. Real photograph. 2:3 vertical, no text overlays."
            ),
        },
        {
            "name": "detail_treatment",
            "prompt": (
                "Close-up of a gloved hand holding a syringe near a patient's cheek. "
                "Only the lower half of the patient's face visible — nose to chin. "
                "Light blue nitrile glove, fine needle. Skin is real — visible pores, slight redness nearby. "
                "Bright clinical lighting from above. Clean and precise. "
                "Real photograph. 2:3 vertical, no text overlays."
            ),
        },
        {
            "name": "environmental_reception",
            "prompt": (
                "Wide shot of a modern medspa reception area. Clean white front desk, warm beige accent wall. "
                "A receptionist handing a clipboard to a woman who just arrived — sunglasses on her head, linen blazer. "
                "Bright natural light through large windows. Small floral arrangement on the desk. "
                "Minimal, clean, warm — not sterile. Real photograph. 2:3 vertical, no text overlays."
            ),
        },
        {
            "name": "social_result",
            "prompt": (
                "A woman in her late 30s looking at her reflection in a handheld mirror after a medspa treatment, "
                "gently touching her jawline. Sitting in a treatment chair in a robe. "
                "Expression is subtle satisfaction — quietly pleased, not exaggerated. "
                "A nurse stands slightly behind, arms casually crossed, watching. "
                "Natural and unposed. Real photograph. 2:3 vertical, no text overlays."
            ),
        },
        {
            "name": "stilllife_tools",
            "prompt": (
                "Overhead flat lay of a medspa treatment tray on a white surface. "
                "A syringe, small bottle of filler, nitrile gloves partially unfolded, cotton pad, small glass vial. "
                "Everything real medical-grade. Soft directional light from upper left creating subtle shadows. "
                "Stainless steel tray with a small teal towel folded at one edge. "
                "Clean, precise, clinical but beautiful. Real photograph. 2:3 vertical, no text overlays."
            ),
        },
    ],
    "bouldering": [
        {
            "name": "hero_wall",
            "prompt": (
                "Wide shot of a large indoor bouldering gym during a busy afternoon. "
                "Eight to ten climbers at various heights — some mid-move, some at the base chalking up. "
                "Cool blue and teal wall panels with multicolored holds — orange, yellow, pink, green. "
                "Thick crash mats on the floor. Tall ceilings with exposed beams. "
                "Massive windows flooding the space with natural afternoon light. "
                "Active but relaxed atmosphere. Real photograph. 2:3 vertical, no text overlays."
            ),
        },
        {
            "name": "portrait_climber",
            "prompt": (
                "Medium-tight portrait of a woman in her late 20s at the base of a climbing wall, "
                "looking up at a route with chalk on her hands. Black tank top, olive climbing pants, messy bun. "
                "Chalk bag on her waist. Focused expression — reading the holds before climbing. "
                "Teal wall behind her with orange and yellow holds blurred in the background. "
                "Natural window light. Chalk dust on her forearms. Real photograph. 2:3 vertical, no text overlays."
            ),
        },
        {
            "name": "social_beta",
            "prompt": (
                "Two climbers at the base of a bouldering problem, looking up at the same sequence. "
                "A man in his early 30s pointing at a hold with his chalked hand, a woman in her mid-20s nodding, arms crossed. "
                "Casual climbing clothes. Chalk bags, water bottles, shoes scattered on the mat around their feet. "
                "Other climbers blurred in background. Bright natural light from skylights. "
                "Genuine problem-solving between friends. Real photograph. 2:3 vertical, no text overlays."
            ),
        },
        {
            "name": "action_send",
            "prompt": (
                "A climber mid-move on an overhanging bouldering wall, reaching dynamically for the top hold. "
                "Body fully extended, feet flagging, core engaged. Dramatic overhang angle. "
                "Bright green and orange holds against a dark blue wall panel. "
                "Shot from below looking up. One spotter below with arms raised. "
                "Natural light from windows creating a slight backlit glow. Real photograph. 2:3 vertical, no text overlays."
            ),
        },
        {
            "name": "environmental_space",
            "prompt": (
                "Wide establishing shot of an indoor climbing gym from the entrance looking in. "
                "Massive climbing walls curving around the space covered in multicolored holds. "
                "Yoga studio visible through glass walls on the left. Main bouldering area in center with crash mats. "
                "Fitness area with weights on the right. Tall ceilings, exposed ductwork. "
                "Natural light from floor-to-ceiling windows. Feels like an industrial cathedral built for play. "
                "Real photograph. 2:3 vertical, no text overlays."
            ),
        },
        {
            "name": "closing_rest",
            "prompt": (
                "Two friends sitting on crash mats after climbing, backs against the wall, legs stretched out. "
                "One drinking from a water bottle, the other unlacing climbing shoes. "
                "Chalk dust on their hands and forearms. Gear spread between them. "
                "Late afternoon golden light through the windows. A few climbers still on walls in the blurred background. "
                "Tired, satisfied, social. Real photograph. 2:3 vertical, no text overlays."
            ),
        },
    ],
}


def generate_image(prompt: str) -> str | None:
    headers = {"Authorization": f"Bearer {KIE_KEY}", "Content-Type": "application/json"}
    payload = {"prompt": prompt, "size": "2:3", "isEnhance": False}

    r = requests.post(GENERATE_URL, headers=headers, json=payload, timeout=30)
    r.raise_for_status()
    data = r.json()
    if data.get("code") != 200:
        print(f"    API error: {data.get('msg')}")
        return None

    task_id = data.get("data", {}).get("taskId")
    if not task_id:
        print("    No task ID")
        return None

    print(f"    Task: {task_id}")

    for i in range(MAX_POLLS):
        time.sleep(POLL_INTERVAL)
        sr = requests.get(f"{STATUS_URL}?taskId={task_id}", headers=headers, timeout=15)
        info = sr.json().get("data", {}).get("info", {})

        if info.get("result_urls"):
            return info["result_urls"][0]

        status = info.get("status", "").lower()
        if status in ("failed", "error"):
            print(f"    Failed: {info.get('message', 'unknown')}")
            return None

        if info.get("successFlag") is True:
            urls = info.get("result_urls") or info.get("resultImageUrl")
            if urls:
                return urls if isinstance(urls, str) else urls[0]

        print(f"    Poll {i+1}/{MAX_POLLS}...")

    print("    Timeout")
    return None


def download(url: str, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    with open(path, "wb") as f:
        f.write(r.content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--brand", help="myburger, marina, or bouldering")
    args = parser.parse_args()

    if not KIE_KEY:
        print("ERROR: KIE_KEY not found")
        return

    brands = [args.brand] if args.brand else list(PROMPTS.keys())
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    total = sum(len(PROMPTS[b]) for b in brands)
    done = 0
    ok = 0

    print(f"\n{'='*50}")
    print(f"CASE STUDY IMAGES — SIMPLE PROMPTS")
    print(f"Brands: {', '.join(brands)} | Total: {total}")
    print(f"{'='*50}\n")

    for brand in brands:
        brand_dir = OUTPUT_DIR / brand
        brand_dir.mkdir(parents=True, exist_ok=True)

        for p in PROMPTS[brand]:
            done += 1
            name = p["name"]
            out_path = brand_dir / f"{name}.png"

            if out_path.exists():
                print(f"[{done}/{total}] {brand}/{name} — exists, skipping")
                ok += 1
                continue

            print(f"[{done}/{total}] {brand}/{name}")
            url = generate_image(p["prompt"])

            if url:
                download(url, out_path)
                print(f"    Saved: {out_path}")
                ok += 1
            else:
                print("    FAILED")

            if done < total:
                time.sleep(5)

    print(f"\n{'='*50}")
    print(f"Done: {ok}/{total}")
    print(f"Images: {OUTPUT_DIR}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
