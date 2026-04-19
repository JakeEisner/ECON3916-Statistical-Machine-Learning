/* ── NAV: active link + scroll shadow ───────── */
const sections = document.querySelectorAll('section[id]');
const navLinks  = document.querySelectorAll('.nav-links a');
const navbar    = document.getElementById('navbar');

const navIO = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (!e.isIntersecting) return;
    navLinks.forEach(a => a.classList.toggle('active', a.getAttribute('href') === `#${e.target.id}`));
  });
}, { rootMargin: '-40% 0px -55% 0px' });

sections.forEach(s => navIO.observe(s));

window.addEventListener('scroll', () => {
  navbar.style.boxShadow = scrollY > 20 ? '0 4px 32px rgba(10,13,20,.09)' : 'none';
}, { passive: true });

/* ── SCROLL REVEAL ──────────────────────────── */
const revealIO = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('in');
      revealIO.unobserve(e.target);
    }
  });
}, { threshold: 0.08 });

document.querySelectorAll('.reveal').forEach(el => revealIO.observe(el));

/* ── SKILL BAR ANIMATION ────────────────────── */
const barIO = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.querySelectorAll('.skill-bar').forEach(bar => bar.classList.add('in'));
      barIO.unobserve(e.target);
    }
  });
}, { threshold: 0.2 });

const skillsSection = document.querySelector('.skills-bars');
if (skillsSection) barIO.observe(skillsSection);

/* ── PROJECT FILTER ─────────────────────────── */
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    const filter = btn.dataset.filter;
    document.querySelectorAll('.proj-card').forEach(card => {
      const tags = card.dataset.tags || '';
      card.classList.toggle('hidden', filter !== 'all' && !tags.includes(filter));
    });
  });
});
