#!/usr/bin/env python3
"""
Create / refresh Stripe payment links for LoopWorker Sprint ladder + Systems Retainer.

Usage:
    export STRIPE_SECRET_KEY="sk_live_..."
    python3 create_stripe_links.py

What it does:
    - Reuses existing product IDs from STRIPE_PAYMENT_LINKS.json where possible
    - Creates new prices at $2,500 / $8,500 / $25,000 / $4,500 monthly
    - Creates new payment links pointing at those prices
    - Deactivates OLD active prices on each product (so old links 404)
    - Writes updated payment_links + deprecation markers back to JSON

Run again any time prices change. Idempotent on amount: if a matching active price
already exists, reuses it instead of creating a duplicate.
"""
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

STRIPE_KEY = os.environ.get("STRIPE_SECRET_KEY")
if not STRIPE_KEY:
    sys.exit("ERROR: set STRIPE_SECRET_KEY env var first")

API = "https://api.stripe.com/v1"
HEADERS = {"Authorization": f"Bearer {STRIPE_KEY}"}
LEDGER = Path(__file__).resolve().parent.parent.parent / "Memory" / "Code_Scripts" / "STRIPE_PAYMENT_LINKS.json"

TIERS = [
    {
        "key": "signal-snapshot",
        "name": "Signal Snapshot",
        "description": "48-hour gateway sprint. One signal pulled deep (competitor wall, customer voice, pricing band, proof gap, or channel fit) + one ranked recommendation. PDF.",
        "amount_cents": 75000,
        "recurring": False,
        "redirect_url": "https://www.loopworker.com/thank-you-snapshot.html",
    },
    {
        "key": "sprint-lite",
        "name": "Sprint Lite",
        "description": "5-day focused market intelligence round. One question, evidence behind it.",
        "amount_cents": 250000,
        "recurring": False,
        "redirect_url": "https://www.loopworker.com/thank-you-sprint.html?tier=lite",
    },
    {
        "key": "sprint-pro",
        "name": "Sprint Pro",
        "description": "10-day decision brief connecting competitor wall, customer voice, pricing band, channel map, and ranked action sheet.",
        "amount_cents": 850000,
        "recurring": False,
        "redirect_url": "https://www.loopworker.com/thank-you-sprint.html?tier=pro",
    },
    {
        "key": "sprint-full",
        "name": "Sprint Full",
        "description": "14-day full strategic round for launch, repositioning, pitch-deck clarity, or higher-stakes market moves.",
        "amount_cents": 2500000,
        "recurring": False,
        "redirect_url": "https://www.loopworker.com/thank-you-sprint.html?tier=full",
    },
    {
        "key": "systems-retainer",
        "name": "Systems Retainer",
        "description": "Monthly post-Sprint execution retainer. Positioning, content cadence, channel build, conversion fixes, automation wiring. Month-to-month.",
        "amount_cents": 450000,
        "recurring": True,
        "redirect_url": "https://www.loopworker.com/thank-you-retainer.html",
    },
]


def _call(method, path, data=None):
    body = urllib.parse.urlencode(data, doseq=True).encode() if data else None
    req = urllib.request.Request(f"{API}{path}", data=body, headers=HEADERS, method=method)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def post(path, data):
    return _call("POST", path, data)


def get(path):
    return _call("GET", path)


def load_ledger():
    if LEDGER.exists():
        return json.loads(LEDGER.read_text())
    return {}


def save_ledger(ledger):
    LEDGER.write_text(json.dumps(ledger, indent=2) + "\n")


def find_or_create_product(tier, ledger_entry):
    if ledger_entry and ledger_entry.get("product_id"):
        try:
            prod = get(f"/products/{ledger_entry['product_id']}")
            print(f"  reused product {prod['id']}")
            return prod
        except urllib.error.HTTPError:
            print("  ledger product missing on Stripe, creating new")
    prod = post("/products", {"name": tier["name"], "description": tier["description"]})
    print(f"  created product {prod['id']}")
    return prod


def list_active_prices(product_id):
    return get(f"/prices?product={product_id}&active=true&limit=100").get("data", [])


def deactivate_price(price_id):
    post(f"/prices/{price_id}", {"active": "false"})
    print(f"    deactivated price {price_id}")


def find_or_create_price(tier, product_id):
    existing = list_active_prices(product_id)
    for p in existing:
        if p["unit_amount"] != tier["amount_cents"]:
            continue
        if tier["recurring"] and (not p.get("recurring") or p["recurring"]["interval"] != "month"):
            continue
        if not tier["recurring"] and p.get("recurring"):
            continue
        print(f"  reused price {p['id']}  (${tier['amount_cents']/100:.0f}{'/mo' if tier['recurring'] else ''})")
        return p, existing
    payload = {
        "product": product_id,
        "unit_amount": tier["amount_cents"],
        "currency": "usd",
    }
    if tier["recurring"]:
        payload["recurring[interval]"] = "month"
    price = post("/prices", payload)
    print(f"  created price {price['id']}  (${tier['amount_cents']/100:.0f}{'/mo' if tier['recurring'] else ''})")
    return price, existing


def create_payment_link(price_id, redirect_url=None):
    payload = {
        "line_items[0][price]": price_id,
        "line_items[0][quantity]": 1,
    }
    if redirect_url:
        payload["after_completion[type]"] = "redirect"
        payload["after_completion[redirect][url]"] = redirect_url
    link = post("/payment_links", payload)
    print(f"  created payment link {link['url']}" + (f"  →  {redirect_url}" if redirect_url else ""))
    return link


def update_payment_link_redirect(link_id, redirect_url):
    """Update an existing Payment Link's after_completion redirect."""
    try:
        post(f"/payment_links/{link_id}", {
            "after_completion[type]": "redirect",
            "after_completion[redirect][url]": redirect_url,
        })
        print(f"  updated redirect on {link_id} → {redirect_url}")
        return True
    except urllib.error.HTTPError as e:
        print(f"  WARN: could not update redirect on {link_id}: {e}")
        return False


def link_id_from_url(url):
    """Extract Payment Link ID from buy.stripe.com URL by querying list endpoint."""
    # Stripe URLs don't expose the plink_ ID directly; fetch list + match by URL
    data = get("/payment_links?limit=100").get("data", [])
    for plink in data:
        if plink.get("url") == url:
            return plink["id"]
    return None


def main():
    ledger = load_ledger()
    for tier in TIERS:
        print(f"\n=== {tier['name']} ===")
        ledger_entry = ledger.get(tier["key"], {})
        product = find_or_create_product(tier, ledger_entry)
        price, existing = find_or_create_price(tier, product["id"])
        amount_key = f"full_{tier['amount_cents']}" + ("_monthly" if tier["recurring"] else "")

        # Reuse existing link if price unchanged + ledger has matching link
        existing_link = ledger_entry.get("links", {}).get(amount_key)
        redirect_url = tier.get("redirect_url")
        if existing_link and ledger_entry.get("current_amount_key") == amount_key:
            print(f"  reused payment link {existing_link}")
            link_url = existing_link
            # Update redirect if specified + differs from ledger
            if redirect_url and ledger_entry.get("redirect_url") != redirect_url:
                link_id = link_id_from_url(existing_link)
                if link_id:
                    update_payment_link_redirect(link_id, redirect_url)
        else:
            # Deactivate other active prices (kill stale links)
            for p in existing:
                if p["id"] != price["id"]:
                    deactivate_price(p["id"])
            link = create_payment_link(price["id"], redirect_url=redirect_url)
            link_url = link["url"]

        entry = ledger.get(tier["key"], {})
        entry["product_id"] = product["id"]
        entry["name"] = tier["name"]
        entry.setdefault("prices", {})[amount_key] = {"amount": tier["amount_cents"], "recurring": tier["recurring"]}
        entry.setdefault("links", {})[amount_key] = link_url
        entry["current_amount_key"] = amount_key
        entry["current_link"] = link_url
        if redirect_url:
            entry["redirect_url"] = redirect_url
        ledger[tier["key"]] = entry

    save_ledger(ledger)
    print(f"\n✓ Ledger updated at {LEDGER}")
    print("\nCurrent links:")
    for tier in TIERS:
        print(f"  {tier['key']:20s}  {ledger[tier['key']]['current_link']}")


if __name__ == "__main__":
    main()
