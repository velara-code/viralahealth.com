// VIRALA website enhancements: appearance switch, mobile menu, header state and gentle reveal motion.
// No network requests, cookies or analytics. The only thing stored is a chosen dark appearance, on this device.
// Content stays fully usable without this script.
(() => {
  const root = document.documentElement;

  // Appearance: light by default on every device; a chosen dark appearance is remembered across pages (see privacy.html)
  const theme = document.querySelector('.theme-toggle');
  const isDark = () => root.dataset.theme === 'dark';
  const labelTheme = () => theme?.setAttribute('aria-pressed', String(isDark()));
  labelTheme();
  theme?.addEventListener('click', () => {
    const dark = !isDark();
    if (dark) root.dataset.theme = 'dark'; else delete root.dataset.theme;
    try { dark ? localStorage.setItem('virala-theme', 'dark') : localStorage.removeItem('virala-theme'); } catch (e) { /* storage blocked: this page only */ }
    labelTheme();
  });

  // Mobile menu: Escape closes and returns focus; Tab stays within the header while open
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#main-nav');
  const label = toggle?.querySelector('span');
  const setOpen = (open, restore = false) => {
    nav?.classList.toggle('open', open);
    toggle?.setAttribute('aria-expanded', String(open));
    if (label) label.textContent = open ? 'Close' : 'Menu';
    document.body.classList.toggle('menu-open', open);
    if (!open && restore) toggle?.focus();
  };
  toggle?.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
  document.addEventListener('keydown', e => {
    if (!nav?.classList.contains('open')) return;
    if (e.key === 'Escape') setOpen(false, true);
    if (e.key === 'Tab') {
      const items = [...document.querySelector('.site-header').querySelectorAll('a, button')].filter(el => el.getClientRects().length);
      const first = items[0], last = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });
  nav?.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setOpen(false)));
  window.matchMedia('(min-width: 901px)').addEventListener?.('change', e => { if (e.matches) setOpen(false); });

  // Header hairline once the page scrolls
  const header = document.querySelector('.site-header');
  const onScroll = () => header?.classList.toggle('scrolled', window.scrollY > 8);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Reveal on scroll; without IntersectionObserver everything is simply shown
  const reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add('in'); io.unobserve(entry.target); }
    }), { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    reveals.forEach(el => io.observe(el));
  } else {
    reveals.forEach(el => el.classList.add('in'));
  }

  root.classList.add('js-ready');
  requestAnimationFrame(() => requestAnimationFrame(() => root.classList.add('nav-ready')));
})();
