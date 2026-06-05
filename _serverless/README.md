# LoopWorker · Stripe Capture Worker

Tiny Cloudflare Worker that accepts site form POSTs + creates Stripe Customer objects. Stripe becomes the CRM.

## Why this exists

- Site is static HTML on GitHub Pages — can't safely embed `sk_live_...` Stripe key in client code
- This Worker holds the key as a secret + acts as middleman
- Form submit → Worker → Stripe Customer.create → redirect to deliverable
- Every form capture lands in Stripe Customers (searchable + taggable + webhookable)

## Why Stripe as CRM

- All captures + paid customers in one place
- Tag by source via metadata (which tool / page / asset captured them)
- Webhook on `customer.created` → fire downstream automation (Beehiiv, Zapier, etc)
- Future Sprint purchases auto-attach to the same Customer ID
- Free, scales, native to your billing system

## Deploy steps

### 1. Install Wrangler

```bash
npm install -g wrangler
wrangler login
```

### 2. Deploy the Worker

```bash
cd _serverless
wrangler deploy
```

Worker deploys to `loopworker-stripe-capture.{your-subdomain}.workers.dev` (Cloudflare gives you the URL).

### 3. Set the Stripe secret

```bash
wrangler secret put STRIPE_SECRET_KEY
# Paste sk_live_... when prompted
```

The secret is encrypted + never logged.

### 4. (Optional) Custom domain

In Cloudflare dashboard → Workers & Pages → loopworker-stripe-capture → Triggers → Add Custom Domain:
- Add `capture.loopworker.com` as a route
- DNS auto-configures
- Now endpoint is `https://capture.loopworker.com/capture`

OR keep the `*.workers.dev` URL. Works fine.

### 5. Update form snippet endpoint

In `/_serverless/form-snippet.html` (and any pages using it), set:
```js
const WORKER_URL = 'https://loopworker-stripe-capture.{your-subdomain}.workers.dev/';
```

## Usage from site

Form POST body:
```json
{
  "email": "alex@example.com",
  "name": "Alex Lamb",
  "source": "pricing-band-finder",
  "metadata": {
    "ba_score": "73",
    "category": "saas"
  }
}
```

Worker response:
```json
{
  "ok": true,
  "customer_id": "cus_...",
  "redirect_url": "https://www.loopworker.com/resources/field-manual.html?from=pricing-band"
}
```

Site JS reads `redirect_url` + navigates. Done.

## CORS

Worker accepts requests from:
- `https://www.loopworker.com`
- `https://loopworker.com`

For local dev, uncomment localhost line in `ALLOWED_ORIGINS` array in `cloudflare-worker.js`.

## Webhook → Beehiiv (downstream nurture)

After capture lands in Stripe, fire automation:

### Option A: Stripe → Zapier → Beehiiv (no code)

1. Stripe Dashboard → Developers → Webhooks → Add endpoint
2. URL: Zapier webhook URL
3. Event: `customer.created`
4. In Zapier:
   - Trigger: Webhook receives
   - Action: Beehiiv "Create Subscriber" with email + metadata-tag

### Option B: Stripe → another Worker → Beehiiv API (free, no Zapier)

Build a second Worker subscribed to Stripe webhook → calls Beehiiv create-subscriber API directly. Adds ~50 lines of code, saves $20/mo Zapier.

## Cost

Cloudflare Workers free tier: 100,000 requests/day. You won't hit it.
Stripe Customer creation: free.
Total ongoing cost: $0.

## Testing locally

```bash
wrangler dev
```

Runs Worker at `http://localhost:8787`. Update form snippet temporarily, hit submit, watch Stripe Test Mode for the new Customer.

## Security notes

- `sk_live_...` is only stored as Worker secret (encrypted at rest)
- CORS whitelist enforces only your site can POST
- Email regex validation
- Rate limiting: Cloudflare auto-applies on free tier (10 req/sec per IP burst)
- For tighter abuse protection, add Turnstile (Cloudflare's free CAPTCHA) to forms
