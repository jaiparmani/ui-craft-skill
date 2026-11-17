# Motion

A beautiful website isn't necessarily an animated one. Animation earns its place when it does one of three jobs:

1. **Communicates hierarchy** — what to look at first, what belongs together (stagger order = reading order).
2. **Creates continuity** — where something came from and went to (shared elements, transitions).
3. **Rewards interaction** — feedback that makes the interface feel alive (press, hover, drag).

If an animation does none of these, remove it.

## Contents
1. Timing, easing, choreography
2. The six patterns (with recipes)
3. CSS-native motion (use first when it's enough)
4. Accessibility
5. Performance
6. How to review motion

---

## 1. Timing, easing, choreography

| Kind | Duration | Easing |
|---|---|---|
| Hover / press feedback | 100–160ms | `ease-out` |
| Small UI (menus, toggles, tooltips) | 160–240ms | `cubic-bezier(.22,1,.36,1)` (expo-ish out) |
| Panels, modals, cards entering | 280–420ms | out for enter, in for exit (exit ~70% of enter) |
| Hero / editorial reveals | 700–1200ms | `power3.out` / `power4.out` / `expo.out` |
| Scroll-scrubbed | tied to scroll | `none` (linear) inside the timeline; let scroll be the easing; `scrub: 0.5–1` for smoothing |

- **Choreograph, don't broadcast.** Sequence: container → headline → supporting text → media → CTA. Stagger 40–90ms for list items, 15–30ms per character/word for type.
- **Motion personality** from the brief decides curves: *precise* = short, expo out; *weighty* = longer, power4 out, slight overshoot never; *playful* = springs, small overshoot (`back.out(1.4)`).
- **Distance matters:** move 16–40px for UI, 60–120% of the element for masked type reveals. Large travel + short duration feels cheap.
- **Animate the right properties:** `transform` and `opacity` (plus `clip-path`, `filter` sparingly). Never `top/left/width/height` per frame.

## 2. The six patterns

### 2.1 Scroll-triggered storytelling (Apple product pages)
Elements enter, scale, reveal or transition as the user scrolls. For launches and long-form landing pages.
```js
gsap.registerPlugin(ScrollTrigger);
gsap.utils.toArray('[data-reveal]').forEach(el => {
  gsap.from(el, { yPercent: 20, autoAlpha: 0, duration: 1, ease: 'power3.out',
    scrollTrigger: { trigger: el, start: 'top 85%', once: true } });
});
// Product reveal tied to scroll position
gsap.timeline({ scrollTrigger: { trigger: '.hero', start: 'top top', end: '+=120%', scrub: 1, pin: true } })
  .from('.product', { scale: 0.7, yPercent: 15 })
  .to('.hero-title', { autoAlpha: 0, yPercent: -30 }, 0);
```

### 2.2 Pinned sections (GSAP ScrollTrigger demos)
A section stays fixed while its content changes — feature walkthroughs, sequential steps.
```js
const steps = gsap.utils.toArray('.step');
const tl = gsap.timeline({ scrollTrigger: { trigger: '.features', pin: true, start: 'top top',
  end: () => '+=' + steps.length * window.innerHeight * 0.8, scrub: 0.6, snap: 1 / (steps.length - 1) } });
steps.forEach((s, i) => { if (i) tl.from(s, { autoAlpha: 0, y: 40 }).to(steps[i - 1], { autoAlpha: 0, y: -40 }, '<'); });
```
On phones, consider unpinning (`ScrollTrigger.matchMedia` / `gsap.matchMedia`) and stacking the steps.

### 2.3 Kinetic typography (Awwwards, Codrops)
Text reveals by word, line or character, through clipping and masks.
```js
// GSAP SplitText (free since GSAP 3.13)
const split = SplitText.create('.headline', { type: 'lines,words', mask: 'lines' });
gsap.from(split.lines, { yPercent: 110, duration: 1, ease: 'expo.out', stagger: 0.08 });
```
No-library version: wrap each line in `<span class="line"><span>…</span></span>`, `.line{overflow:hidden;display:block}`, animate the inner span from `translateY(110%)`. Keep the real text in the DOM (screen readers read it once; don't split into aria-hidden noise without an `aria-label`).

### 2.4 Micro-interactions (Linear, Raycast)
Magnetic buttons, custom cursors, hover transitions, animated icons, responsive feedback.
```js
// Magnetic button
document.querySelectorAll('[data-magnetic]').forEach(btn => {
  const x = gsap.quickTo(btn, 'x', { duration: 0.4, ease: 'power3' });
  const y = gsap.quickTo(btn, 'y', { duration: 0.4, ease: 'power3' });
  btn.addEventListener('pointermove', e => { const r = btn.getBoundingClientRect();
    x((e.clientX - r.left - r.width / 2) * 0.3); y((e.clientY - r.top - r.height / 2) * 0.3); });
  btn.addEventListener('pointerleave', () => { x(0); y(0); });
});
```
Only on `(hover: hover) and (pointer: fine)`. In React prefer Motion: `<motion.button whileHover={{ scale: 1.02 }} whileTap={{ scale: 0.98 }} />`.

### 2.5 Parallax (creative agency portfolios)
Foreground and background move at different speeds for depth. Keep differences subtle (10–30%).
```js
gsap.utils.toArray('[data-speed]').forEach(el => gsap.to(el, {
  yPercent: (1 - parseFloat(el.dataset.speed)) * 100, ease: 'none',
  scrollTrigger: { trigger: el.closest('section'), start: 'top bottom', end: 'bottom top', scrub: true } }));
```
CSS-only alternative: scroll-driven animations (§3).

### 2.6 Page transitions (Locomotive, Active Theory)
Shared elements, route transitions, smooth loading and continuity between pages.
- **Multi-page sites:** View Transitions API — `@view-transition { navigation: auto; }` plus `view-transition-name: hero-img` on the shared element on both pages.
- **SPA / React:** Motion `AnimatePresence` + `layoutId` for shared elements; Next.js App Router supports the View Transitions API via `useTransition`/experimental flags, or animate with Motion.
- Keep transitions under ~600ms; never block navigation waiting for an animation.

## 3. CSS-native motion (use first when it's enough)

```css
/* Scroll-driven reveal, no JS (Chromium & Safari 26+; degrade gracefully elsewhere) */
@supports (animation-timeline: view()) {
  .reveal { animation: reveal linear both; animation-timeline: view(); animation-range: entry 0% cover 30%; }
  @keyframes reveal { from { opacity: 0; transform: translateY(40px); } }
}
/* Enter animation for elements added to the DOM / popovers */
.toast { transition: opacity .2s, transform .2s; @starting-style { opacity: 0; transform: translateY(8px); } }
```
Also: `transition` for every hover/focus state, `@keyframes` for marquees and loaders.

## 4. Accessibility

- Honor `prefers-reduced-motion: reduce`: replace movement with instant states or simple opacity fades; disable smooth scroll, parallax, pinning and autoplaying sequences. With GSAP use `gsap.matchMedia()`:
```js
const mm = gsap.matchMedia();
mm.add('(prefers-reduced-motion: no-preference)', () => { /* all motion here */ });
```
- Content must be visible without JS and before animations run: set initial hidden states from JS (`gsap.set`/`from`), not in CSS, or gate them under a `.js` class.
- No flashing more than 3 times per second. Autoplaying motion longer than 5s needs a pause control (WCAG 2.2.2).
- Keyboard and screen-reader paths must work with pinned/horizontal sections: focus moves into view naturally; nothing becomes unreachable.
- Smooth scrolling must not break anchor links, `Tab` scrolling, or find-in-page.

## 5. Performance

- Animate `transform`/`opacity`; promote with `will-change` only during the animation.
- Use one rAF loop (GSAP ticker) — let Lenis run on it (see `tech-stack.md`).
- Lazy-init heavy scenes (Three.js) with IntersectionObserver; pause rendering when offscreen; cap `devicePixelRatio` at 2.
- Compress media: AVIF/WebP images, short muted `<video playsinline>` loops instead of GIFs, image sequences as WebP sprites or canvas.
- Avoid layout shift: reserve space for animated media; don't animate in content that pushes layout.
- Target 60fps on a mid-range phone. If it stutters, remove layers before adding optimizations.

## 6. How to review motion

You can't watch a video, so review motion as a series of frames and measurements:
- **Scroll frames:** take screenshots at several scroll positions (e.g. `window.scrollTo` then screenshot, or headless Chrome at different `#anchors`). Every frame should be a good composition — no half-revealed limbo.
- **Timeline frames:** for intro animations, screenshot at t=0, mid, and end (pause with `gsap.globalTimeline.pause()` and `seek()`), or temporarily set durations long.
- **Reduced motion:** emulate `prefers-reduced-motion: reduce` (DevTools / Playwright `reducedMotion: 'reduce'`) and screenshot again; the page must be complete.
- **Console:** no errors (CDN failures silently kill every animation).
- **Mobile:** check that pinning/parallax are simplified or disabled and nothing overflows.
