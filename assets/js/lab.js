/* ==========================================================================
   Shader Lab: prints the compiled GLSL, highlights it, and lets visitors
   edit it live. The <pre> is filled from the same <script> tag the WebGL
   runtime compiles, so the page can never show stale code.
   ========================================================================== */
(() => {
  'use strict';

  const KW = 'attribute|uniform|varying|const|precision|highp|mediump|lowp|if|else|for|while|return|break|continue|discard|void|struct|in|out|inout';
  const TY = 'float|int|bool|vec2|vec3|vec4|mat2|mat3|mat4|sampler2D';
  const FN = 'sin|cos|tan|asin|acos|atan|pow|exp|exp2|log|log2|sqrt|inversesqrt|abs|sign|floor|ceil|fract|mod|min|max|clamp|mix|step|smoothstep|length|distance|dot|cross|normalize|reflect|refract|faceforward|texture2D|radians|degrees';
  const GL = 'gl_FragColor|gl_FragCoord|gl_Position|gl_PointSize';

  const RE = new RegExp(
    '(\\/\\/[^\\n]*)' +                       // 1 line comment
    '|(\\/\\*[\\s\\S]*?\\*\\/)' +             // 2 block comment
    '|(#[^\\n]*)' +                           // 3 preprocessor
    '|\\b(' + GL + ')\\b' +                   // 4 gl_ builtins
    '|\\b(' + KW + ')\\b' +                   // 5 keywords
    '|\\b(' + TY + ')\\b' +                   // 6 types
    '|\\b(' + FN + ')(?=\\s*\\()' +           // 7 builtin functions
    '|\\b(\\d+\\.?\\d*(?:e[-+]?\\d+)?)\\b' +  // 8 numbers
    '|\\b(u_[A-Za-z_]\\w*)\\b',               // 9 uniforms
    'g');

  const CLS = { 1: 'c', 2: 'c', 3: 'p', 4: 'g', 5: 'k', 6: 't', 7: 'f', 8: 'n', 9: 'u' };

  const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

  function highlight(src) {
    return esc(src).replace(RE, (m, ...g) => {
      for (let i = 0; i < 9; i++) if (g[i] !== undefined) return `<span class="${CLS[i + 1]}">${m}</span>`;
      return m;
    });
  }

  function init() {
    // 1. Fill every code block from its shader source
    document.querySelectorAll('pre.glsl[data-src]').forEach(pre => {
      const el = document.getElementById(pre.dataset.src);
      if (!el) return;
      pre.dataset.original = el.textContent.trim();
      pre.innerHTML = highlight(pre.dataset.original);
    });

    // Only fade the bottom edge and offer "scroll for the rest" when the
    // listing actually overflows its box; otherwise it is just empty space.
    const marks = () => document.querySelectorAll('pre.glsl[data-src]').forEach(pre => {
      const wrap = pre.closest('.code-wrap');
      if (wrap) wrap.classList.toggle('overflows', pre.scrollHeight - pre.clientHeight > 4);
    });
    marks();
    addEventListener('resize', marks, { passive: true });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(marks);

    // 2. Copy
    document.querySelectorAll('[data-copy]').forEach(btn => {
      btn.addEventListener('click', async () => {
        const el = document.getElementById(btn.dataset.copy);
        if (!el) return;
        try {
          await navigator.clipboard.writeText(el.textContent.trim());
          const was = btn.innerHTML;
          btn.innerHTML = '<i class="fa-solid fa-check"></i> Copied';
          setTimeout(() => { btn.innerHTML = was; }, 1600);
        } catch (e) { /* clipboard blocked; ignore */ }
      });
    });

    // 3. Live editing
    document.querySelectorAll('[data-edit]').forEach(btn => {
      const id = btn.dataset.edit;
      const wrap = btn.closest('.code-wrap');
      const pre = wrap.querySelector('pre.glsl');
      const ta = wrap.querySelector(`[data-editor="${id}"]`);
      const err = wrap.querySelector(`[data-err="${id}"]`);
      const canvas = document.querySelector(`canvas[data-shader="${id}"]`);
      let timer = null;

      const setError = msg => {
        if (!msg) { err.hidden = true; wrap.classList.remove('has-error'); return; }
        err.textContent = msg;
        err.hidden = false;
        wrap.classList.add('has-error');
      };

      btn.addEventListener('click', () => {
        const editing = wrap.classList.toggle('editing');
        if (editing) {
          ta.value = pre.dataset.original;
          ta.hidden = false;
          pre.hidden = true;
          ta.style.height = Math.min(pre.scrollHeight || 480, 620) + 'px';
          btn.innerHTML = '<i class="fa-solid fa-rotate-left"></i> Reset';
          ta.focus();
        } else {
          // Reset back to the shipped shader
          ta.hidden = true;
          pre.hidden = false;
          setError(null);
          btn.innerHTML = '<i class="fa-solid fa-pen"></i> Edit live';
          if (canvas && canvas.__gl) canvas.__gl.compile(pre.dataset.original);
        }
      });

      ta.addEventListener('input', () => {
        clearTimeout(timer);
        timer = setTimeout(() => {
          if (!canvas || !canvas.__gl) return;
          const problem = canvas.__gl.compile(ta.value);
          setError(problem);
          if (!problem) canvas.__gl.start();
        }, 260);
      });

      // Tab inserts two spaces instead of leaving the field
      ta.addEventListener('keydown', e => {
        if (e.key !== 'Tab') return;
        e.preventDefault();
        const s = ta.selectionStart, t = ta.selectionEnd;
        ta.value = ta.value.slice(0, s) + '  ' + ta.value.slice(t);
        ta.selectionStart = ta.selectionEnd = s + 2;
        ta.dispatchEvent(new Event('input'));
      });
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
