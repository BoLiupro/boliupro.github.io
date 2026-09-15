const toggle = document.querySelector('.nav-toggle');
const navigation = document.querySelector('.main-nav');
if (toggle && navigation) {
  const close = () => { toggle.setAttribute('aria-expanded', 'false'); navigation.classList.remove('is-open'); };
  document.documentElement.classList.add('has-js');
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    navigation.classList.toggle('is-open', open);
  });
  navigation.addEventListener('click', event => { if (event.target.closest('a')) close(); });
  document.addEventListener('keydown', event => { if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') { close(); toggle.focus(); } });
  document.addEventListener('click', event => { if (!event.target.closest('.header-inner')) close(); });
  window.matchMedia('(min-width: 761px)').addEventListener('change', close);
}

// Native horizontal scrolling also works with JavaScript disabled.
document.querySelectorAll('.preview-section').forEach(section => {
  const track = section.querySelector('.preview-track');
  const buttons = [...section.querySelectorAll('[data-scroll]')];
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const update = () => {
    const end = Math.max(0, track.scrollWidth - track.clientWidth);
    buttons.forEach(button => {
      button.disabled = Number(button.dataset.scroll) < 0
        ? track.scrollLeft <= 1 : track.scrollLeft >= end - 1;
    });
  };
  const scroll = direction => track.scrollBy({
    left: direction * track.clientWidth,
    behavior: reducedMotion.matches ? 'instant' : 'smooth'
  });
  buttons.forEach(button => button.addEventListener('click', () => scroll(Number(button.dataset.scroll))));
  track.addEventListener('scroll', update, { passive: true });
  track.addEventListener('keydown', event => {
    if (event.target !== track) return;
    if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
      event.preventDefault();
      scroll(event.key === 'ArrowRight' ? 1 : -1);
    }
  });
  if ('ResizeObserver' in window) new ResizeObserver(update).observe(track);
  else window.addEventListener('resize', update, { passive: true });
  update();
});
