/* ==========================================================================
   Minimal WebGL runtime for the shader studies on this site.
   No libraries: one full-screen triangle, one fragment shader per canvas.
   The GLSL lives in <script type="x-shader/x-fragment"> tags so the exact
   source that compiles is also the source shown on the page.
   ========================================================================== */
(() => {
  'use strict';

  const VERT = `attribute vec2 a_pos;
void main() { gl_Position = vec4(a_pos, 0.0, 1.0); }`;

  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /** Parse `uniform float u_name;` declarations so controls can bind by name. */
  function declaredUniforms(src) {
    const out = [];
    const re = /uniform\s+(float|vec2|vec3|vec4|int)\s+([A-Za-z_]\w*)\s*;/g;
    let m;
    while ((m = re.exec(src))) out.push({ type: m[1], name: m[2] });
    return out;
  }

  class ShaderCanvas {
    constructor(canvas, source) {
      this.canvas = canvas;
      this.source = source;
      this.uniforms = Object.create(null);   // name -> number | number[]
      this.locs = Object.create(null);
      this.time = 0;
      this.last = 0;
      this.running = false;
      this.visible = false;
      this.mouse = { x: 0.5, y: 0.5, tx: 0.5, ty: 0.5 };
      this.dpr = Math.min(window.devicePixelRatio || 1, canvas.dataset.dpr ? +canvas.dataset.dpr : 1.5);
      this.error = null;

      const opts = { antialias: false, alpha: true, premultipliedAlpha: false, depth: false, stencil: false };
      this.gl = canvas.getContext('webgl', opts) || canvas.getContext('experimental-webgl', opts);
      if (!this.gl) { this.fail('WebGL is not available in this browser.'); return; }

      const gl = this.gl;
      this.quad = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, this.quad);
      gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);

      const err = this.compile(source);
      if (err) this.fail('Shader failed to compile.');
      if (err) console.error('[gl] ' + (canvas.dataset.shader || '') + '\n' + err);
      this.resize();

      this.onResize = () => this.resize();
      window.addEventListener('resize', this.onResize, { passive: true });

      canvas.addEventListener('pointermove', e => {
        const r = canvas.getBoundingClientRect();
        this.mouse.tx = (e.clientX - r.left) / r.width;
        this.mouse.ty = 1 - (e.clientY - r.top) / r.height;
      }, { passive: true });
      canvas.addEventListener('pointerleave', () => { this.mouse.tx = 0.5; this.mouse.ty = 0.5; }, { passive: true });

      // Only burn frames while the canvas is actually on screen.
      this.io = new IntersectionObserver(entries => {
        this.visible = entries[0].isIntersecting;
        this.visible ? this.start() : this.stop();
      }, { threshold: 0.01 });
      this.io.observe(canvas);

      document.addEventListener('visibilitychange', () => {
        document.hidden ? this.stop() : (this.visible && this.start());
      });
    }

    fail(msg) {
      this.error = msg;
      const holder = this.canvas.closest('.gl-stage') || this.canvas.parentElement;
      if (holder && !holder.querySelector('.gl-fallback')) {
        const d = document.createElement('div');
        d.className = 'gl-fallback';
        d.textContent = msg;
        holder.appendChild(d);
      }
    }

    /** Compile a fragment shader. Returns null on success, or the error log. */
    compile(source) {
      const gl = this.gl;
      if (!gl) return 'no context';
      const vs = gl.createShader(gl.VERTEX_SHADER);
      gl.shaderSource(vs, VERT); gl.compileShader(vs);

      const fs = gl.createShader(gl.FRAGMENT_SHADER);
      gl.shaderSource(fs, source); gl.compileShader(fs);
      if (!gl.getShaderParameter(fs, gl.COMPILE_STATUS)) {
        const log = gl.getShaderInfoLog(fs) || 'Unknown compile error';
        gl.deleteShader(vs); gl.deleteShader(fs);
        return log.trim();
      }

      const prog = gl.createProgram();
      gl.attachShader(prog, vs); gl.attachShader(prog, fs); gl.linkProgram(prog);
      gl.deleteShader(vs); gl.deleteShader(fs);
      if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) {
        const log = gl.getProgramInfoLog(prog) || 'Link error';
        gl.deleteProgram(prog);
        return log.trim();
      }

      if (this.program) gl.deleteProgram(this.program);
      this.program = prog;
      this.source = source;
      this.locs = Object.create(null);
      gl.useProgram(prog);
      const loc = gl.getAttribLocation(prog, 'a_pos');
      gl.bindBuffer(gl.ARRAY_BUFFER, this.quad);
      gl.enableVertexAttribArray(loc);
      gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
      this.declared = declaredUniforms(source);
      this.render(0);
      return null;
    }

    loc(name) {
      if (!(name in this.locs)) this.locs[name] = this.gl.getUniformLocation(this.program, name);
      return this.locs[name];
    }

    set(name, value) { this.uniforms[name] = value; if (!this.running) this.render(this.time); }

    resize() {
      const c = this.canvas;
      const w = Math.max(1, Math.round(c.clientWidth * this.dpr));
      const h = Math.max(1, Math.round(c.clientHeight * this.dpr));
      if (c.width !== w || c.height !== h) {
        c.width = w; c.height = h;
        if (this.gl) this.gl.viewport(0, 0, w, h);
        if (!this.running) this.render(this.time);
      }
    }

    render(t) {
      const gl = this.gl;
      if (!gl || !this.program) return;
      gl.useProgram(this.program);
      gl.uniform2f(this.loc('u_resolution'), this.canvas.width, this.canvas.height);
      gl.uniform1f(this.loc('u_time'), t);
      gl.uniform2f(this.loc('u_mouse'), this.mouse.x, this.mouse.y);
      for (const k in this.uniforms) {
        const v = this.uniforms[k], l = this.loc(k);
        if (l === null) continue;
        if (Array.isArray(v)) {
          if (v.length === 2) gl.uniform2fv(l, v);
          else if (v.length === 3) gl.uniform3fv(l, v);
          else gl.uniform4fv(l, v);
        } else gl.uniform1f(l, v);
      }
      gl.drawArrays(gl.TRIANGLES, 0, 3);
    }

    frame(now) {
      if (!this.running) return;
      const dt = this.last ? Math.min((now - this.last) / 1000, 0.05) : 0;
      this.last = now;
      this.time += dt;
      this.mouse.x += (this.mouse.tx - this.mouse.x) * 0.08;
      this.mouse.y += (this.mouse.ty - this.mouse.y) * 0.08;
      this.render(this.time);
      this.raf = requestAnimationFrame(this.boundFrame);
    }

    start() {
      if (this.running || !this.program) return;
      if (reduced) { this.render(3.0); return; }   // one still frame, no motion
      this.running = true;
      this.last = 0;
      this.boundFrame = this.boundFrame || (n => this.frame(n));
      this.raf = requestAnimationFrame(this.boundFrame);
    }

    stop() {
      this.running = false;
      if (this.raf) cancelAnimationFrame(this.raf);
    }
  }

  /* ---------------------------------------------------------------- boot */

  function sourceFor(canvas) {
    const el = document.getElementById(canvas.dataset.shader);
    return el ? el.textContent.trim() : null;
  }

  const instances = [];

  function boot() {
    document.querySelectorAll('canvas[data-shader]').forEach(canvas => {
      const src = sourceFor(canvas);
      if (!src) return;
      const inst = new ShaderCanvas(canvas, src);
      canvas.__gl = inst;
      instances.push(inst);

      // Bind range controls that live in the same study block.
      const scope = canvas.closest('[data-study]') || document;
      scope.querySelectorAll('input[type=range][data-uniform]').forEach(input => {
        const name = input.dataset.uniform;
        const out = scope.querySelector(`[data-readout="${name}"]`);
        const apply = () => {
          inst.set(name, parseFloat(input.value));
          if (out) out.textContent = parseFloat(input.value).toFixed(2);
        };
        input.addEventListener('input', apply);
        apply();
      });
    });
  }

  window.ShaderCanvas = ShaderCanvas;
  window.__shaderInstances = instances;

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
