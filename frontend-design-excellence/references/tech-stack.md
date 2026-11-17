# Motion & 3D Tech Stack

Don't force one library onto every project. **Default toolkit: CSS + GSAP + Motion.** Add Lenis for smooth scroll on expressive pages. Reach for Three.js / React Three Fiber only when the experience genuinely benefits from 3D.

## Decision table

| Need | Use | Why |
|---|---|---|
| Hover, focus, simple enter/exit, marquees | **CSS** transitions/keyframes, `@starting-style`, scroll-driven animations | Zero JS, best performance |
| Complex timelines, pinned scrolling, scroll storytelling, text splitting | **GSAP** + ScrollTrigger (+ SplitText) | Industry standard, precise sequencing, all plugins free since 3.13 |
| React transitions, gestures, layout animations, shared elements, exit animations | **Motion** (`motion/react`, formerly Framer Motion) | Declarative, `layout`/`layoutId`, `AnimatePresence`, springs |
| Smooth scrolling | **Lenis** | Light, keeps native scroll semantics, plays well with ScrollTrigger |
| 3D scenes, shaders, WebGL effects (vanilla) | **Three.js** | The standard WebGL library |
| 3D in React | **React Three Fiber** + **drei** | Declarative scenes, helpers for controls, text, loaders |
| Designer-made vector animations (icons, illustrations) | **Lottie** (`lottie-web` or `@lottiefiles/dotlottie-web`) | After Effects → JSON, tiny, crisp |
| Multi-page route transitions | **View Transitions API** | Native, progressive enhancement |

Rules of thumb:
- In a React app, use Motion for component/UI motion and GSAP for scroll storytelling; don't animate the same element with both.
- Don't add GSAP for a single hover effect, and don't add Three.js for a gradient blob (a CSS/Canvas gradient will do).
- Match what the project already has. If it ships Framer Motion, keep using it.

## Setup snippets

Pinned versions below are known-good; newer minor versions are fine.

### Plain HTML (CDN)
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lenis@1.3.4/dist/lenis.css">
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/SplitText.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.3.4/dist/lenis.min.js"></script>
<script>
  gsap.registerPlugin(ScrollTrigger, SplitText);
  const mm = gsap.matchMedia();
  mm.add('(prefers-reduced-motion: no-preference)', () => {
    const lenis = new Lenis({ lerp: 0.1 });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(t => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
    // ...timelines here...
    return () => lenis.destroy();
  });
</script>
```

### npm / bundlers
```bash
npm i gsap lenis motion
```
```js
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { SplitText } from 'gsap/SplitText';
import Lenis from 'lenis';
import 'lenis/dist/lenis.css';
```

### React: GSAP
```bash
npm i gsap @gsap/react
```
```jsx
import { useGSAP } from '@gsap/react';
useGSAP(() => { gsap.from('.card', { y: 40, autoAlpha: 0, stagger: 0.06 }); }, { scope: containerRef });
```
`useGSAP` handles cleanup on unmount (important in React 18/19 strict mode).

### React: Motion
```jsx
import { motion, AnimatePresence } from 'motion/react';
<AnimatePresence mode="popLayout">
  {open && <motion.div key="panel" initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: 8 }} transition={{ type: 'spring', bounce: 0, duration: 0.35 }} />}
</AnimatePresence>
<motion.img layoutId={`photo-${id}`} />   // shared-element transition
```
Use `useReducedMotion()` to simplify.

### Three.js (ES module from CDN)
```html
<script type="importmap">{ "imports": { "three": "https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.min.js" } }</script>
<script type="module">
  import * as THREE from 'three';
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  // pause the render loop when the canvas is offscreen (IntersectionObserver)
</script>
```

### React Three Fiber
```bash
npm i three @react-three/fiber @react-three/drei
```
```jsx
<Canvas dpr={[1, 2]} camera={{ position: [0, 0, 5], fov: 45 }}>
  <Suspense fallback={null}><Model /></Suspense>
  <Environment preset="city" />
</Canvas>
```
Provide a static image fallback for no-WebGL and reduced-motion users.

### Lottie
```html
<script src="https://cdn.jsdelivr.net/npm/lottie-web@5.12.2/build/player/lottie_light.min.js"></script>
```
Prefer `.lottie` (dotLottie) files for size. Never autoplay long loops without a pause option.

## Documentation
- GSAP & ScrollTrigger — gsap.com/docs/v3/Plugins/ScrollTrigger, gsap.com/docs/v3/Plugins/SplitText, demos at gsap.com/demos
- Motion for React — motion.dev/docs/react
- Lenis — github.com/darkroomengineering/lenis
- Three.js — threejs.org/docs, threejs.org/examples
- React Three Fiber — r3f.docs.pmnd.rs, drei at drei.docs.pmnd.rs
- LottieFiles — developers.lottiefiles.com
- View Transitions — developer.chrome.com/docs/web-platform/view-transitions
- CSS scroll-driven animations — scroll-driven-animations.style
