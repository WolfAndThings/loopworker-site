/**
 * LoopWorker · Stripe Webhook → Beehiiv Subscriber Forwarder
 *
 * Second Cloudflare Worker. Subscribes to Stripe webhook events.
 * Forwards customer.created → Beehiiv API to add subscriber with source tag.
 *
 * Saves ~$20/mo vs Zapier. ~80 lines.
 *
 * Deploy: separate Worker. See README.md.
 *
 * Secrets needed:
 *   STRIPE_WEBHOOK_SECRET  (whsec_...) — get from Stripe Dashboard → Webhooks → endpoint
 *   BEEHIIV_API_KEY        (bh_pk_...) — Beehiiv Settings → API
 *   BEEHIIV_PUBLICATION_ID (pub_...)   — Beehiiv URL: /p/{publication_id}/...
 */

async function verifyStripeSignature(body, signature, secret) {
  // Stripe-Signature: t=<timestamp>,v1=<sig>
  const parts = Object.fromEntries(
    signature.split(',').map(p => {
      const [k, v] = p.split('=');
      return [k, v];
    })
  );
  if (!parts.t || !parts.v1) return false;

  const signedPayload = `${parts.t}.${body}`;
  const enc = new TextEncoder();
  const key = await crypto.subtle.importKey(
    'raw',
    enc.encode(secret),
    { name: 'HMAC', hash: 'SHA-256' },
    false,
    ['sign']
  );
  const sigBuf = await crypto.subtle.sign('HMAC', key, enc.encode(signedPayload));
  const expectedSig = [...new Uint8Array(sigBuf)]
    .map(b => b.toString(16).padStart(2, '0'))
    .join('');

  return expectedSig === parts.v1;
}

async function addBeehiivSubscriber({ email, source, metadata, env }) {
  const url = `https://api.beehiiv.com/v2/publications/${env.BEEHIIV_PUBLICATION_ID}/subscriptions`;
  const body = {
    email,
    reactivate_existing: true,
    send_welcome_email: true,
    utm_source: source || 'capture',
    custom_fields: Object.entries(metadata || {}).map(([k, v]) => ({ name: k, value: String(v) })),
  };

  const resp = await fetch(url, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${env.BEEHIIV_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
  });

  if (!resp.ok) {
    const err = await resp.json().catch(() => ({}));
    throw new Error(`Beehiiv API ${resp.status}: ${err.message || resp.statusText}`);
  }
  return resp.json();
}

export default {
  async fetch(request, env) {
    if (request.method !== 'POST') {
      return new Response('Method not allowed', { status: 405 });
    }

    const signature = request.headers.get('Stripe-Signature');
    if (!signature) {
      return new Response('Missing Stripe-Signature', { status: 400 });
    }

    const body = await request.text();
    const valid = await verifyStripeSignature(body, signature, env.STRIPE_WEBHOOK_SECRET);
    if (!valid) {
      return new Response('Invalid signature', { status: 401 });
    }

    let event;
    try {
      event = JSON.parse(body);
    } catch {
      return new Response('Invalid JSON', { status: 400 });
    }

    // Only handle customer.created events from email captures (not Sprint purchases)
    if (event.type !== 'customer.created') {
      return new Response(JSON.stringify({ ok: true, skipped: event.type }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const customer = event.data.object;
    const isLead = customer.metadata?.lead_type === 'email_capture';
    if (!isLead) {
      // Sprint buyer or other — let a different automation handle these
      return new Response(JSON.stringify({ ok: true, skipped: 'not a lead capture' }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    try {
      await addBeehiivSubscriber({
        email: customer.email,
        source: customer.metadata.source,
        metadata: customer.metadata,
        env,
      });
      return new Response(JSON.stringify({ ok: true, beehiiv: 'subscribed', email: customer.email }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      });
    } catch (err) {
      // Log via 5xx so Stripe retries
      return new Response(JSON.stringify({ ok: false, error: err.message }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' },
      });
    }
  },
};
