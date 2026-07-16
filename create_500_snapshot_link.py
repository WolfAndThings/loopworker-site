#!/usr/bin/env python3
"""
Create the $500 Visibility Snapshot one-time Stripe Payment Link.

Usage:
    export STRIPE_SECRET_KEY="sk_live_..."
    python3 create_500_snapshot_link.py

Does:
    - Creates product "Visibility Snapshot"
    - Creates a $500 one-time price
    - Creates a payment link
    - Appends entry "visibility-snapshot" to Memory/Code_Scripts/STRIPE_PAYMENT_LINKS.json
    - Prints the URL so you can paste it into 500_snapshot_spec.md
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

PRODUCT_NAME = "Visibility Snapshot"
PRODUCT_DESC = "One-page competitive read for a founder, delivered in 48 hours. Diagnoses where they stand in their category. Useful or free."
AMOUNT_CENTS = 50000  # $500
CURRENCY = "usd"


def post(path, data):
    body = urllib.parse.urlencode(data, doseq=True).encode()
    req = urllib.request.Request(f"{API}{path}", data=body, headers=HEADERS, method="POST")
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def main():
    print("Creating product...")
    product = post("/products", {"name": PRODUCT_NAME, "description": PRODUCT_DESC})
    print(f"  product_id={product['id']}")

    print("Creating price...")
    price = post("/prices", {
        "product": product["id"],
        "unit_amount": AMOUNT_CENTS,
        "currency": CURRENCY,
    })
    print(f"  price_id={price['id']}")

    print("Creating payment link...")
    link = post("/payment_links", {
        "line_items[0][price]": price["id"],
        "line_items[0][quantity]": 1,
    })
    print(f"  url={link['url']}")

    ledger_path = Path("/Users/alexlamb/Desktop/AE_Exports/Memory/Code_Scripts/STRIPE_PAYMENT_LINKS.json")
    ledger = json.loads(ledger_path.read_text())
    ledger["visibility-snapshot"] = {
        "product_id": product["id"],
        "name": PRODUCT_NAME,
        "display_name": "Visibility Snapshot",
        "prices": {f"full_{AMOUNT_CENTS}": {"id": price["id"], "amount": AMOUNT_CENTS, "recurring": False}},
        "links": {f"full_{AMOUNT_CENTS}": link["url"]},
        "current_amount_key": f"full_{AMOUNT_CENTS}",
        "current_link": link["url"],
    }
    ledger_path.write_text(json.dumps(ledger, indent=2))
    print(f"\nAppended 'visibility-snapshot' to {ledger_path.name}")
    print(f"\nPAYMENT LINK: {link['url']}")
    print("\nNext: paste this URL into 500_snapshot_spec.md (replace [STRIPE $500 LINK]).")


if __name__ == "__main__":
    main()
