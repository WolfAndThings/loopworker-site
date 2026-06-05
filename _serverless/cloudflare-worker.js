/**
 * LoopWorker · Stripe Customer Create Proxy
 *
 * Cloudflare Worker. Accepts POST from site form, creates Stripe Customer.
 * Returns success or error. CORS-enabled for www.loopworker.com.
 *
 * Deploy: `wrangler deploy` (after wrangler login + secret set).
 * Secret: wrangler secret put STRIPE_SECRET_KEY  (paste sk_live_...)
 *
 * Endpoint: POST /capture
 * Body: { email, name?, source, metadata? }
 * Response: { ok: true, customer_id, redirect_url } | { ok: false, error }
 */

const ALLOWED_ORIGINS = [
  'https://www.loopworker.com',
  'https://loopworker.com',
  // Add localhost for dev:
  // 'http://localhost:8770',
];

const REDIRECTS = {
  'field-manual':            'https://www.loopworker.com/resources/field-manual.html?from=stripe',
  'pricing-band-finder':     'https://www.loopworker.com/resources/field-manual.html?from=pricing-band',
  'channel-mix-diagnoser':   'https://www.loopworker.com/resources/field-manual.html?from=channel-mix',
  'brand-audit-score':       'https://www.loopworker.com/resources/field-manual.html?from=brand-audit',
  'roi-calculator':          'https://www.loopworker.com/resources/field-manual.html?from=roi-calc',
  'consulting-comparison':   'https://www.loopworker.com/resources/field-manual.html?from=consulting-comp',
  'saas-pricing-report':     'https://www.loopworker.com/resources/field-manual.html?from=saas-report',
  'comp-report':             'https://www.loopworker.com/resources/field-manual.html?from=comp-report',
  'hub-page':                'https://www.loopworker.com/resources/field-manual.html?from=hub',
  'home':                    'https://www.loopworker.com/resources/field-manual.html?from=home',
  'default':                 'https://www.loopworker.com/resources/field-manual.html',
};

function corsHeaders(origin) {
  const allowed = ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
  return {
    'Access-Control-Allow-Origin': allowed,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
  };
}

async function createStripeCustomer({ email, name, source, metadata, env }) {
  const body = new URLSearchParams();
  body.append('email', email);
  if (name) body.append('name', name);
  body.append('description', `LoopWorker lead · source: ${source || 'unknown'}`);
  body.append('metadata[source]', source || 'unknown');
  body.append('metadata[captured_at]', new Date().toISOString());
  body.append('metadata[lead_type]', 'email_capture');
  if (metadata && typeof metadata === 'object') {
    for (const [k, v] of Object.entries(metadata)) {
      body.append(`metadata[${k}]`, String(v));
    }
  }

  const resp = await fetch('https://api.stripe.com/v1/customers', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${env.STRIPE_SECRET_KEY}`,
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body,
  });

  const data = await resp.json();
  if (!resp.ok) {
    throw new Error(data.error?.message || 'Stripe API error');
  }
  return data;
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin') || '';
    const headers = corsHeaders(origin);

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers });
    }

    if (request.method !== 'POST') {
      return new Response(JSON.stringify({ ok: false, error: 'Method not allowed' }), {
        status: 405,
        headers: { ...headers, 'Content-Type': 'application/json' },
      });
    }

    let payload;
    try {
      payload = await request.json();
    } catch {
      return new Response(JSON.stringify({ ok: false, error: 'Invalid JSON' }), {
        status: 400,
        headers: { ...headers, 'Content-Type': 'application/json' },
      });
    }

    const { email, name, source, metadata } = payload;

    if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      return new Response(JSON.stringify({ ok: false, error: 'Invalid email' }), {
        status: 400,
        headers: { ...headers, 'Content-Type': 'application/json' },
      });
    }

    try {
      const customer = await createStripeCustomer({ email, name, source, metadata, env });
      const redirect_url = REDIRECTS[source] || REDIRECTS['default'];
      return new Response(JSON.stringify({
        ok: true,
        customer_id: customer.id,
        redirect_url,
      }), {
        status: 200,
        headers: { ...headers, 'Content-Type': 'application/json' },
      });
    } catch (err) {
      return new Response(JSON.stringify({ ok: false, error: err.message }), {
        status: 500,
        headers: { ...headers, 'Content-Type': 'application/json' },
      });
    }
  },
};
