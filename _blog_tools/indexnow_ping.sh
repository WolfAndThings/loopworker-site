#!/usr/bin/env bash
# Tell Bing, Yandex, Naver, Seznam and Yep to re-crawl the site.
# Google does NOT participate in IndexNow — use Search Console for Google.
#
# Run after any deploy that changes titles, descriptions, pricing or llms.txt.
# Usage:  ./_blog_tools/indexnow_ping.sh            (submits every sitemap URL)
#         ./_blog_tools/indexnow_ping.sh /pricing.html /faq.html   (specific paths)
set -euo pipefail
cd "$(dirname "$0")/.."

HOST="www.loopworker.com"
KEY_FILE=".indexnow-key"

if [[ ! -f "$KEY_FILE" ]]; then
  echo "No $KEY_FILE. The hosted key is the <48-hex>.txt file in the repo root." >&2
  exit 1
fi
KEY="$(cat "$KEY_FILE")"

if [[ ! -f "$KEY.txt" ]]; then
  echo "Key file $KEY.txt missing from repo root. IndexNow will reject the batch." >&2
  exit 1
fi

PAYLOAD="$(mktemp)"
trap 'rm -f "$PAYLOAD"' EXIT

python3 - "$KEY" "$HOST" "$@" > "$PAYLOAD" <<'PY'
import json, re, sys
from pathlib import Path

key, host, *paths = sys.argv[1:]
if paths:
    urls = [f"https://{host}{p if p.startswith('/') else '/' + p}" for p in paths]
else:
    urls = re.findall(r"<loc>(.*?)</loc>", Path("sitemap.xml").read_text())

json.dump({
    "host": host,
    "key": key,
    "keyLocation": f"https://{host}/{key}.txt",
    "urlList": urls,
}, open(1, "w"))
print(f"submitting {len(urls)} urls", file=sys.stderr)
PY

curl -sS -w "\nHTTP %{http_code}\n" -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json; charset=utf-8" \
  --data-binary @"$PAYLOAD"

echo "200 or 202 means accepted. 422 usually means the key file did not validate."
