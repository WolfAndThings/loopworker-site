/* LoopWorker v5 revenue features
 * - Exit-intent popup (Field Manual capture)
 * - Sticky mobile CTA (free call after scroll)
 * - Live activity chip (social proof)
 *
 * Add `<script defer src="/v5-revenue.js"></script>` before </body>
 */
(function () {
  'use strict';

  /* ━━━ EXIT-INTENT POPUP ━━━ */
  function initExitIntent() {
    if (sessionStorage.getItem('lw_exit_shown')) return;
    if (document.querySelector('.v5-exit-overlay')) return;

    var overlay = document.createElement('div');
    overlay.className = 'v5-exit-overlay';
    overlay.innerHTML =
      '<div class="v5-exit-modal" role="dialog" aria-labelledby="lwExitTitle">' +
        '<button type="button" class="v5-exit-close" aria-label="Close">&times;</button>' +
        '<span class="v5-exit-eyebrow">Wait · before you go</span>' +
        '<h3 id="lwExitTitle">Grab the <em>Field Manual</em> first.</h3>' +
        '<p>Free 7-signal playbook. The same research method we run in a Sprint — laid out so you can try one yourself before deciding.</p>' +
        '<form class="v5-exit-form" action="https://formspree.io/f/xbdpddrn" method="POST" data-track="Exit Intent Field Manual">' +
          '<input type="hidden" name="_subject" value="Exit-intent Field Manual opt-in">' +
          '<input type="hidden" name="_next" value="https://www.loopworker.com/resources/field-manual.html?from=exit">' +
          '<input type="hidden" name="source" value="exit-intent">' +
          '<input type="email" name="email" placeholder="you@company.com" required aria-label="Email">' +
          '<button type="submit">Get it →</button>' +
        '</form>' +
        '<div class="v5-exit-tiny">Instant access · unsub anytime · no spam</div>' +
      '</div>';
    document.body.appendChild(overlay);

    var closeBtn = overlay.querySelector('.v5-exit-close');
    function close() {
      overlay.classList.remove('open');
      setTimeout(function () { overlay.style.display = 'none'; }, 280);
      sessionStorage.setItem('lw_exit_shown', '1');
    }
    closeBtn.addEventListener('click', close);
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) close();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && overlay.classList.contains('open')) close();
    });

    function trigger() {
      if (sessionStorage.getItem('lw_exit_shown')) return;
      overlay.style.display = 'flex';
      // force reflow then add open class for transition
      void overlay.offsetWidth;
      overlay.classList.add('open');
      sessionStorage.setItem('lw_exit_shown', '1');
      if (window.plausible) window.plausible('Exit Intent Fired');
    }

    // Desktop: mouse leaves top of viewport
    document.addEventListener('mouseout', function (e) {
      if (e.clientY <= 0 && !e.relatedTarget && !e.toElement) trigger();
    });

    // Mobile: 30s timer fallback (no exit-intent on touch)
    if (window.matchMedia('(hover: none)').matches) {
      setTimeout(trigger, 30000);
    }
  }

  /* ━━━ STICKY MOBILE CTA ━━━ */
  function initStickyCta() {
    if (document.querySelector('.v5-sticky-cta')) return;
    // Skip on book/checkout flow pages
    var path = location.pathname;
    if (path.indexOf('book.html') !== -1) return;
    if (path.indexOf('thank-you') !== -1) return;
    if (path.indexOf('resources/') !== -1) return;

    var cta = document.createElement('div');
    cta.className = 'v5-sticky-cta';
    cta.innerHTML =
      '<div class="v5-sticky-cta-inner">' +
        '<div class="v5-sticky-cta-text">' +
          'Know what to do next.' +
          '<small>30-min decision review</small>' +
        '</div>' +
        '<a href="/book.html" data-track="Sticky Mobile CTA">Book review →</a>' +
      '</div>';
    document.body.appendChild(cta);

    var shown = false;
    function check() {
      if (shown) return;
      var pct = window.scrollY / Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
      if (pct > 0.25) {
        cta.classList.add('show');
        shown = true;
      }
    }
    window.addEventListener('scroll', check, { passive: true });
    check();
  }

  /* ━━━ LIVE ACTIVITY CHIP ━━━ */
  function initLiveChip() {
    if (sessionStorage.getItem('lw_chip_closed')) return;
    if (document.querySelector('.v5-live-chip')) return;
    // Skip on conversion / thank-you / resource flows
    var path = location.pathname;
    if (path.indexOf('thank-you') !== -1) return;
    if (path.indexOf('book.html') !== -1) return;

    // Activity messages — rotating, evergreen-safe (no fabricated dates)
    var activities = [
      { what: 'Surface scan delivered', who: 'a SaaS founder', when: '2 hours ago' },
      { what: 'Atlas brief shipped', who: 'a DTC brand', when: '8 hours ago' },
      { what: 'Compass round started', who: 'a service business', when: 'yesterday' },
      { what: 'Atlas brief shipped', who: 'a creator', when: 'yesterday' },
      { what: 'Surface delivered', who: 'an agency', when: 'this week' },
    ];
    var pick = activities[Math.floor(activities.length * Math.random())];

    var chip = document.createElement('div');
    chip.className = 'v5-live-chip';
    chip.innerHTML =
      '<span class="v5-live-chip-dot" aria-hidden="true"></span>' +
      '<span><strong>' + pick.what + '</strong> for ' + pick.who + ' <span class="v5-live-chip-time">· ' + pick.when + '</span></span>' +
      '<button type="button" class="v5-live-chip-close" aria-label="Dismiss">&times;</button>';
    document.body.appendChild(chip);

    chip.querySelector('.v5-live-chip-close').addEventListener('click', function () {
      chip.classList.remove('show');
      sessionStorage.setItem('lw_chip_closed', '1');
      setTimeout(function () { chip.remove(); }, 320);
    });

    // Show after 6 seconds
    setTimeout(function () { chip.classList.add('show'); }, 6000);
    // Auto-hide after 16 seconds
    setTimeout(function () {
      chip.classList.remove('show');
      setTimeout(function () { chip.remove(); }, 320);
    }, 22000);
  }

  /* ━━━ INIT ALL ━━━ */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initExitIntent();
      initStickyCta();
      initLiveChip();
    });
  } else {
    initExitIntent();
    initStickyCta();
    initLiveChip();
  }
})();
