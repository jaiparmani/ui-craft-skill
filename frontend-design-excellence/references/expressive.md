# Expressive & Award-Level Design

Read this in **Expressive mode**: launches, portfolios, agency and brand sites, campaign pages, "make it feel premium / award-winning / like Apple / like an Awwwards site". Product-UI rules still apply to anything people must *use* (nav, forms, pricing), but the goal here is different: the page must be **remembered**, not just understood.

## Contents
1. What separates award-level work from "nice"
2. The concept-first brief
3. Reference library — what to study in each
4. Technique catalog
5. Expressive anti-patterns
6. Originality rule
7. Expressive critique

---

## 1. What separates award-level work from "nice"

Look at any Site of the Day and the same five things show up:

1. **A concept, not a template.** The site is *about* one idea and every choice serves it. Bruno Simon's portfolio *is* a toy car you drive; Resn's work treats each page as an experiment. Ask: "what is this site's one idea?"
2. **One signature moment.** A single interaction or scene people screenshot and share — Apple's product rotating as you scroll, a 3D object you can grab, a headline that assembles itself. Spend most of the effort budget here; keep the rest calm.
3. **Typographic courage.** Display type at 10–20vw, tight tracking, clipped by the viewport, mixed with tiny mono labels. Scale contrast does most of the work.
4. **Composition that breaks the grid on purpose.** Asymmetry, overlap, elements bleeding off-canvas, huge negative space — but anchored to a grid so it reads as intentional (see Minimal Gallery work and editorial portfolios).
5. **Craft in the details.** Easing curves, stagger timing, cursor feedback, loading choreography, grain/noise texture, sound design. Nothing jumps; everything has continuity.

Restraint is part of it. Linear and Stripe are award-quality with very little motion: the signature is precision.

## 2. The concept-first brief

Extend the normal 5-line brief with:

- **Concept** — one sentence. "The page is a darkroom: images develop as you scroll." "Every section is a chapter of the product's assembly."
- **Signature moment** — what it is, where it sits (usually hero or the first pinned section), and which technology it needs.
- **Motion personality** — three adjectives (e.g. "weighty, precise, unhurried") that decide easing and duration.
- **Narrative** — the scroll order as a story: hook → reveal → proof → detail → call to action.
- **Fallback** — what reduced-motion users and low-end phones see (it must still be beautiful).

## 3. Reference library — what to study in each

Study for *principles*. Never copy branding, copy, assets or layouts wholesale.

### A. Award-winning visual design
| Site | Study for |
|---|---|
| **Locomotive** (locomotive.ca) | Immersive storytelling, huge kinetic type, smooth scroll, page transitions; they authored Locomotive Scroll |
| **Active Theory** (activetheory.net) | WebGL and 3D scenes, immersive interactions, transitions between scenes |
| **Resn** (resn.co.nz) | Experimental interactions, unexpected layouts, playful "click & hold" discovery |
| **Bruno Simon** (bruno-simon.com) | Playful 3D navigation — the portfolio is a game; Three.js + physics done with charm |

### B. Premium product UI
| Site | Study for |
|---|---|
| **Apple product pages** (apple.com) | Scroll storytelling, product reveals, scrubbed image sequences, whitespace, typographic hierarchy |
| **Linear** (linear.app) | Dark surfaces, perspective product shots, subtle glows, hairline borders, micro-detail |
| **Stripe** (stripe.com) | Typography, animated gradient mesh, layout clarity, diagrams that explain |
| **Raycast** (raycast.com) | Premium dark presentation, dramatic light/blur backgrounds, micro-interactions, keyboard UI |

### C. Experimental & inspiration galleries
| Site | Use for |
|---|---|
| **Godly** (godly.website) | Unusual visual concepts and layouts; browse by motion |
| **Awwwards** (awwwards.com) | Site of the Day archive, judged on design/usability/creativity/content |
| **Codrops** (tympanus.net/codrops) | Practical tutorials and demos of animation techniques — with source code |
| **Minimal Gallery** (minimal.gallery) | Minimalism, editorial composition, restraint |

If you have web access and the user names one of these, look at it before designing. If not, rely on the summaries above.

## 4. Technique catalog

Pick 2–4 per project. Implementation recipes are in `motion.md`; library choice in `tech-stack.md`.

| Technique | Effect | Typical build |
|---|---|---|
| Oversized clipped headline | Confidence, editorial scale | CSS `font-size: clamp(64px, 14vw, 240px)`, `overflow: hidden` |
| Line/word mask reveal | Type that "arrives" | GSAP SplitText or manual spans + `clip-path`/`overflow:hidden` + `yPercent` |
| Marquee / infinite text band | Energy, rhythm | CSS `@keyframes` translateX on duplicated content |
| Pinned feature sequence | Explain step by step | GSAP ScrollTrigger `pin: true` + timeline `scrub` |
| Horizontal scroll section | Gallery / timeline | Pin container, tween inner `x` to `-(scrollWidth - innerWidth)` |
| Scroll-scrubbed product reveal | Apple-style hero | Image-sequence on `<canvas>` or a transform/scale timeline with `scrub` |
| Stacking cards | Chapters | `position: sticky` cards with increasing `top`, scale previous on scroll |
| Parallax layers | Depth | `yPercent` at different rates with ScrollTrigger, or CSS scroll-driven animation |
| Magnetic button / custom cursor | Tactile reward | pointermove → gsap.quickTo x/y; cursor follower with `mix-blend-mode: difference` |
| Animated gradient mesh | Stripe-like warmth | Canvas/WebGL shader, or layered blurred radial gradients animated slowly |
| Grain / noise overlay | Analog richness | SVG `feTurbulence` as a fixed overlay at 4–8% opacity |
| 3D object / scene | Signature moment | Three.js or R3F; only when 3D *is* the concept |
| Page transitions | Continuity | View Transitions API, or GSAP timeline on route change; shared-element morphs |
| Image hover distortion | Playful gallery | WebGL plane with displacement shader (Codrops has many recipes) |

## 5. Expressive anti-patterns

- **Everything fades up the same way.** Uniform `opacity 0 → 1, y 40 → 0` on every block is the motion equivalent of Inter-everywhere. Vary by role: headlines mask-reveal, images scale/clip, lists stagger, numbers count.
- **Scroll-jacking that fights the user.** Smooth scroll is fine; hijacking wheel/keys so a flick moves one slide is not. Native scroll position must stay in control.
- **3D blob for its own sake.** A floating gradient sphere that means nothing. 3D must carry the concept.
- **Loading screens without a reason.** Only if real assets must preload, and keep it under ~2s with progress.
- **Custom cursors that hide usability.** Keep the system cursor on inputs and text; never hide focus states.
- **Motion everywhere at once.** One thing moves at a time; the eye can only follow one.
- **Unreadable art direction.** Text over busy imagery without scrim; 10px light-gray captions.
- **Desktop-only experience.** The phone version must still tell the story (often simplified: no pinning, fewer layers).

## 6. Originality rule

References teach principles. Never recreate a specific site's look, logo, copy, characters, 3D assets or exact layout, even renamed. Combine principles into something new that fits the user's own concept and brand.

## 7. Expressive critique (in addition to `review-checklist.md`)

- [ ] Can you state the concept in one sentence, and does every section serve it?
- [ ] Is there exactly one signature moment, and is it actually impressive at 1440px *and* 390px?
- [ ] Scrub through the page at 0%, 25%, 50%, 75%, 100% scroll: is every frame a good composition, with no half-revealed limbo states?
- [ ] Does motion vary by element role, or does everything fade up identically?
- [ ] With `prefers-reduced-motion: reduce` emulated, is the page complete and still beautiful?
- [ ] Is the main thread calm: no layout-property animation, no jank when scrolling fast? (Check DevTools Performance or watch for stutter.)
- [ ] Does the first screen render meaningful content within ~1s, even before animations run?
- [ ] Would a jury remember it tomorrow? If not, push the signature moment further — not more effects elsewhere.
