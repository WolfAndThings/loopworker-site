/* LoopWorker v6 scroll reveal
 * Cards rise into place as they enter the viewport, staggered per row/group.
 * Class .rv is only ever added by this script, so with JS off nothing is hidden.
 * Respects prefers-reduced-motion. Add `<script defer src="/v6-reveal.js"></script>`.
 */
(function () {
  'use strict';
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (!('IntersectionObserver' in window)) return;

  var sel = '.q-card, .read-doc, .tier, .step, .prod, .guarantee, .a-item, .stakes-row, .faq-item, .email-card';
  var els = [].slice.call(document.querySelectorAll(sel));
  if (!els.length) return;

  // stagger siblings that share a parent
  var groups = new Map();
  els.forEach(function (el) {
    var p = el.parentNode;
    var n = groups.get(p) || 0;
    el.style.transitionDelay = Math.min(n * 70, 420) + 'ms';
    groups.set(p, n + 1);
    el.classList.add('rv');
  });

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.add('in');
        io.unobserve(e.target);
      }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

  els.forEach(function (el) { io.observe(el); });
})();
