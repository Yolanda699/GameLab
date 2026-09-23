document.addEventListener('DOMContentLoaded', () => {
  // Mobile nav
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', () => links.classList.toggle('open'));
    links.querySelectorAll('a').forEach(a => a.addEventListener('click', () => links.classList.remove('open')));
  }

  // Reveal on scroll
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }), { threshold: 0.08 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));

  // Work filters (home)
  const filters = document.querySelectorAll('.filter');
  filters.forEach(btn => btn.addEventListener('click', () => {
    filters.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const f = btn.dataset.filter;
    document.querySelectorAll('.work-group').forEach(g => {
      g.hidden = !(f === 'all' || g.dataset.cat === f);
    });
  }));

  // Scrollspy for nav + project TOC
  const spyLinks = [...document.querySelectorAll('.nav-links a[href^="#"], .toc a[href^="#"]')];
  const targets = spyLinks.map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean);
  if (targets.length) {
    const spy = () => {
      const y = window.scrollY + window.innerHeight * 0.3;
      let current = null;
      targets.forEach(t => { if (t.offsetTop <= y) current = t.id; });
      spyLinks.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + current));
      const activeToc = document.querySelector('.toc a.active');
      if (activeToc && window.innerWidth < 980) {
        const ol = activeToc.closest('ol');
        if (ol) ol.scrollTo({ left: activeToc.offsetLeft - 24, behavior: 'smooth' });
      }
    };
    window.addEventListener('scroll', spy, { passive: true });
    spy();
  }

  // Dropdown menus (tap to toggle on touch)
  document.querySelectorAll('.has-menu > a').forEach(a => a.addEventListener('click', e => {
    if (window.innerWidth > 860 && !a.parentElement.classList.contains('open') && matchMedia('(hover: none)').matches) {
      e.preventDefault(); a.parentElement.classList.add('open');
    }
  }));
  document.addEventListener('click', e => {
    document.querySelectorAll('.has-menu.open').forEach(m => { if (!m.contains(e.target)) m.classList.remove('open'); });
  });

  // Tabs (professional work + skills); data-tabs groups buttons with panels
  document.querySelectorAll('[data-tabs]').forEach(group => {
    const id = group.dataset.tabs;
    const btns = group.querySelectorAll('.tab');
    const panels = document.querySelectorAll(`[data-panel-of="${id}"]`);
    btns.forEach((b, i) => b.addEventListener('click', () => {
      btns.forEach(x => { x.classList.remove('active'); x.setAttribute('aria-selected', 'false'); });
      panels.forEach(p => p.classList.remove('active'));
      b.classList.add('active'); b.setAttribute('aria-selected', 'true');
      panels[i].classList.add('active');
    }));
  });

  // Carousels
  document.querySelectorAll('.carousel').forEach(c => {
    const track = c.querySelector('.track');
    const slides = track.querySelectorAll('.slide');
    const count = c.querySelector('.count');
    const idx = () => Math.round(track.scrollLeft / track.clientWidth);
    const upd = () => { if (count) count.textContent = `${idx() + 1} / ${slides.length}`; };
    c.querySelector('.prev')?.addEventListener('click', () => track.scrollBy({ left: -track.clientWidth, behavior: 'smooth' }));
    c.querySelector('.next')?.addEventListener('click', () => {
      if (idx() >= slides.length - 1) track.scrollTo({ left: 0, behavior: 'smooth' });
      else track.scrollBy({ left: track.clientWidth, behavior: 'smooth' });
    });
    track.addEventListener('scroll', upd, { passive: true });
    upd();
  });

  // Audio players (one plays at a time)
  let current = null;
  const stopCurrent = () => { if (current) { current.audio.pause(); current.btn.classList.remove('on'); current.btn.textContent = current.btn.dataset.label || '▶'; current = null; } };
  document.querySelectorAll('[data-audio]').forEach(btn => {
    const audio = new Audio(btn.dataset.audio);
    audio.preload = 'none';
    const row = btn.closest('.track-row');
    const bar = row?.querySelector('.bar i');
    const t = row?.querySelector('.t');
    const fmt = s => isFinite(s) ? `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}` : '';
    audio.addEventListener('timeupdate', () => {
      if (bar && audio.duration) bar.style.width = (audio.currentTime / audio.duration * 100) + '%';
      if (t) t.textContent = fmt(audio.currentTime) + ' / ' + fmt(audio.duration);
    });
    audio.addEventListener('ended', stopCurrent);
    btn.addEventListener('click', () => {
      if (current && current.audio === audio) { stopCurrent(); return; }
      stopCurrent();
      audio.currentTime = 0; audio.play();
      btn.classList.add('on'); if (!btn.dataset.label) btn.textContent = '❚❚';
      current = { audio, btn };
    });
  });

  // Lightbox for project images
  const imgs = [...document.querySelectorAll('.fig img, .gallery img, .slide img, .matrow img')];
  if (!imgs.length) return;
  const lb = document.createElement('div');
  lb.className = 'lightbox';
  lb.innerHTML = '<button class="x" aria-label="Close">✕</button><button class="prev" aria-label="Previous">‹</button><img alt=""><div class="cap"></div><button class="next" aria-label="Next">›</button>';
  document.body.appendChild(lb);
  const lbImg = lb.querySelector('img'), cap = lb.querySelector('.cap');
  let idx = 0;
  const show = i => {
    idx = (i + imgs.length) % imgs.length;
    const im = imgs[idx];
    lbImg.src = im.dataset.full || im.src;
    lbImg.alt = im.alt;
    const fc = im.closest('figure')?.querySelector('figcaption');
    cap.textContent = fc ? fc.textContent : im.alt;
    lb.classList.add('open');
    document.body.style.overflow = 'hidden';
  };
  const close = () => { lb.classList.remove('open'); document.body.style.overflow = ''; };
  imgs.forEach((im, i) => im.addEventListener('click', () => show(i)));
  lb.querySelector('.x').addEventListener('click', close);
  lb.querySelector('.prev').addEventListener('click', e => { e.stopPropagation(); show(idx - 1); });
  lb.querySelector('.next').addEventListener('click', e => { e.stopPropagation(); show(idx + 1); });
  lb.addEventListener('click', e => { if (e.target === lb) close(); });
  document.addEventListener('keydown', e => {
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') show(idx - 1);
    if (e.key === 'ArrowRight') show(idx + 1);
  });
});

/* ==========================================================================
   Atmosphere: paper grain, scroll progress, nav state.
   Kept in its own scope so it runs on every page regardless of content.
   ========================================================================== */
(() => {
  'use strict';

  const boot = () => {
    // Film grain
    const grain = document.createElement('div');
    grain.className = 'grain';
    grain.setAttribute('aria-hidden', 'true');
    document.body.appendChild(grain);

    // Scroll progress
    const bar = document.createElement('div');
    bar.className = 'scroll-progress';
    bar.setAttribute('aria-hidden', 'true');
    document.body.appendChild(bar);

    const nav = document.querySelector('.nav');
    let ticking = false;
    const onScroll = () => {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(() => {
        const h = document.documentElement.scrollHeight - window.innerHeight;
        bar.style.width = (h > 0 ? (window.scrollY / h) * 100 : 0) + '%';
        if (nav) nav.classList.toggle('scrolled', window.scrollY > 24);
        ticking = false;
      });
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();

/* Prompt lab: swapping the city changes only the two subject tokens, which is
   the point the surrounding copy is making. */
(() => {
  const lab = document.querySelector('.promptlab');
  if (!lab) return;
  const city = lab.querySelector('.pl-city'), subj = lab.querySelector('.pl-subj');
  lab.querySelectorAll('.pl-place').forEach(b => b.addEventListener('click', () => {
    lab.querySelectorAll('.pl-place').forEach(x => x.classList.remove('on'));
    b.classList.add('on');
    city.textContent = b.dataset.place;
    subj.textContent = b.dataset.subj;
    [city, subj].forEach(el => { el.classList.remove('swap'); void el.offsetWidth; el.classList.add('swap'); });
  }));
})();

/* Hero material orb: each preset is a full material definition, the way an
   instance off a master material would be. No sliders; these are the values. */
(() => {
  const canvas = document.getElementById('orb');
  if (!canvas) return;
  const stage = canvas.closest('.orb-stage');
  const btns = [...document.querySelectorAll('.orb-presets button')];
  if (!btns.length) return;

  // gl.js boots on DOMContentLoaded too; wait until the instance exists.
  const ready = fn => canvas.__gl ? fn(canvas.__gl) : setTimeout(() => ready(fn), 60);

  ready(gl => {
    const apply = b => {
      gl.set('u_base', b.dataset.base.split(',').map(Number));
      gl.set('u_rough', +b.dataset.rough);
      gl.set('u_metal', +b.dataset.metal);
      gl.set('u_detail', +b.dataset.detail);
      gl.set('u_coat', +b.dataset.coat);
    };
    btns.forEach(b => b.addEventListener('click', () => {
      btns.forEach(x => x.classList.remove('on'));
      b.classList.add('on');
      apply(b);
    }));
    apply(document.querySelector('.orb-presets button.on') || btns[0]);
  });

  const seen = () => stage && stage.classList.add('touched');
  canvas.addEventListener('pointerdown', seen, { once: true });
  canvas.addEventListener('pointermove', seen, { once: true });
})();
