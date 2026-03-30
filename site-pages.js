function trackPageEvent(eventName) {
    if (typeof window.plausible === 'function') {
        window.plausible(eventName);
    }
}

function toggleSiteMenu() {
    const button = document.querySelector('.hamburger');
    const nav = document.getElementById('mobileNav');
    if (!button || !nav) return;

    button.classList.toggle('active');
    nav.classList.toggle('active');
    const isOpen = nav.classList.contains('active');
    button.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    document.body.style.overflow = isOpen ? 'hidden' : '';
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('[data-track]').forEach(function(element) {
        element.addEventListener('click', function() {
            trackPageEvent(element.dataset.track);
        });
    });

    const nav = document.getElementById('mobileNav');
    if (nav) {
        nav.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                const button = document.querySelector('.hamburger');
                if (!nav.classList.contains('active')) return;
                nav.classList.remove('active');
                if (button) {
                    button.classList.remove('active');
                    button.setAttribute('aria-expanded', 'false');
                }
                document.body.style.overflow = '';
            });
        });
    }
});
