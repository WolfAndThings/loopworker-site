/* Shared navigation, attribution, and conversion tracking. */
(function () {
  'use strict';

  window.plausible = window.plausible || function () {
    (window.plausible.q = window.plausible.q || []).push(arguments);
  };

  function track(name, props) {
    window.plausible(name, { props: props || {} });
  }

  function initNavigation() {
    var buttons = document.querySelectorAll('.hamburger, .v5-hamburger');
    buttons.forEach(function (button) {
      var menuId = button.getAttribute('aria-controls') || 'mobileNav';
      var menu = document.getElementById(menuId);
      if (!menu) return;

      button.removeAttribute('onclick');
      button.setAttribute('aria-controls', menuId);
      button.setAttribute('aria-expanded', menu.classList.contains('open') ? 'true' : 'false');

      button.addEventListener('click', function () {
        var open = menu.classList.toggle('open');
        button.setAttribute('aria-expanded', open ? 'true' : 'false');
      });

      menu.addEventListener('click', function (event) {
        if (!event.target.closest('a')) return;
        menu.classList.remove('open');
        button.setAttribute('aria-expanded', 'false');
      });

      document.addEventListener('keydown', function (event) {
        if (event.key !== 'Escape' || !menu.classList.contains('open')) return;
        menu.classList.remove('open');
        button.setAttribute('aria-expanded', 'false');
        button.focus();
      });
    });
  }

  function addHidden(form, name, value) {
    if (!value || form.elements[name]) return;
    var input = document.createElement('input');
    input.type = 'hidden';
    input.name = name;
    input.value = value;
    form.appendChild(input);
  }

  function initForms() {
    var params = new URLSearchParams(location.search);
    document.querySelectorAll('form[action*="formspree.io"]').forEach(function (form) {
      addHidden(form, 'landing_page', location.pathname);
      addHidden(form, 'utm_source', params.get('utm_source'));
      addHidden(form, 'utm_medium', params.get('utm_medium'));
      addHidden(form, 'utm_campaign', params.get('utm_campaign'));

      form.addEventListener('submit', function () {
        track('Form Submit', {
          label: form.getAttribute('data-track') || form.getAttribute('name') || 'Unlabelled form',
          page: location.pathname
        });
      });
    });
  }

  function initTrackedClicks() {
    document.addEventListener('click', function (event) {
      var target = event.target.closest('[data-track]');
      if (!target || target.tagName === 'FORM') return;
      track('CTA Click', {
        label: target.getAttribute('data-track'),
        page: location.pathname,
        target: target.getAttribute('href') || target.tagName.toLowerCase()
      });
    });
  }

  function init() {
    initNavigation();
    initForms();
    initTrackedClicks();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
