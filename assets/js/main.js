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
