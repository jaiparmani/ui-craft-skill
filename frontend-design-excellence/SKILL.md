---
name: frontend-design-excellence
description: Design and build frontends at the level of top product teams and award-winning studios — from clean, premium product UI (Linear, Stripe, Apple, Raycast quality) to expressive, motion-rich, Awwwards-style sites with scroll storytelling, kinetic typography, pinned sections, micro-interactions, page transitions and 3D. Use this skill whenever you create or restyle ANY user-facing UI or website: landing pages, launch pages, portfolios, agency sites, dashboards, admin panels, forms, React/Vue/Svelte/Next.js components, HTML/CSS prototypes, Tailwind layouts, animations (GSAP, Motion/Framer Motion, Lenis, Three.js, React Three Fiber, Lottie). Also use it when the user says a UI "looks bad", "looks generic", "looks like AI made it", wants it "premium", "award-winning", "like Apple/Linear/Stripe", "more alive", "animated", or asks for a redesign — even if they never say "design".
---

# Frontend Design Excellence

Your default frontend instincts produce a recognizable "AI look": centered everything, a purple-to-blue gradient hero, Inter at three sizes, emoji as icons, cards with drop shadows, and — when asked for motion — every block fading up the same way. This skill replaces those defaults with the process great designers and studios follow: **pick the mode, decide the concept, constrain with tokens, build hierarchy, plan motion, then render the result and critique it.**

The single biggest lever is the critique step. You cannot judge a UI from its source code — render it and look at it.

## Step 0 — Pick the mode

| Mode | For | Goal | Read |
|---|---|---|---|
| **Product UI** | Apps, dashboards, admin, settings, forms, docs, checkout | Clarity, speed, density, convention | `principles.md`, `components.md`, `tokens.md` |
| **Premium product marketing** | SaaS/product landing pages, pricing, launch pages | Product UI clarity + a few precise, memorable moments (Linear, Stripe, Raycast, Apple) | all of the above + `motion.md` |
| **Expressive** | Portfolios, agency/brand/campaign sites, award submissions, "make it unforgettable" | A concept and a signature moment people remember (Locomotive, Active Theory, Resn) | `expressive.md`, `motion.md`, `tech-stack.md` |

When unsure: apps are Product UI; marketing pages are Premium; anything the user calls creative, immersive, award-winning or experimental is Expressive. Usable parts (nav, forms, pricing tables) always follow Product UI rules, whatever the mode.

## Workflow

### 1. Brief (before any code)

State briefly, in your reasoning or to the user:

1. **Who & what job** — who uses this and the one thing they come to do.
2. **Primary action** — the one element that should win visually.
3. **Density** — airy marketing, compact app, or dense data tool.
4. **Aesthetic direction** — ONE named direction from `references/aesthetics.md`, or the existing brand. Commit; mixed directions look accidental.
5. **Constraints** — existing design system, framework, brand, dark mode, accessibility, performance budget.

Premium and Expressive add (details in `references/expressive.md`):

6. **Concept** — one sentence the whole page serves.
7. **Signature moment** — the one scene or interaction people will remember, and where it sits.
8. **Motion personality** — three adjectives that set easing and timing ("precise, quiet, quick").

If the project has a design system (Tailwind config, CSS variables, shadcn/ui, MUI, an existing motion library), **use it and match it**. Read a couple of existing screens first.

### 2. Tokens before layout

A closed set of values; nothing outside them. Ready-made scales in `references/tokens.md`, starter file `assets/tokens.css`.
- Spacing on a 4px scale; ~6 type sizes; 2–3 weights; one tinted neutral ramp + one accent ramp + semantic colors; 1–2 radii; 2–3 shadow levels.
- Motion tokens too: 3 durations and 2–3 easing curves derived from the motion personality.

### 3. Build hierarchy first

Make the eye land on the right thing with **size, weight, spacing and contrast** alone; add color last. Rules (detail in `references/principles.md`, patterns in `references/components.md`):
- Hierarchy through de-emphasis; proximity groups things; left-align by default; body text ≤ 65ch.
- One primary button per view. Real content, never lorem ipsum. Design every state: hover, focus-visible, active, disabled, loading, empty, error, overflow.
- Icons from one real set (Lucide, Heroicons, Phosphor, Tabler). Never emoji as UI icons.
- Expressive mode: typographic courage (display type at 10–20vw), deliberate grid-breaking anchored to a grid, generous negative space.

### 4. Plan motion (skip for static product screens beyond basic transitions)

Motion must **communicate hierarchy, create continuity, or reward interaction** — otherwise cut it. Read `references/motion.md` for the six patterns (scroll storytelling, pinned sections, kinetic type, micro-interactions, parallax, page transitions) with recipes, and `references/tech-stack.md` to choose tools:
- **Default toolkit: CSS + GSAP + Motion.** Lenis for smooth scroll on expressive pages. Three.js / React Three Fiber only when 3D *is* the concept. Lottie for designer-made vector animation.
- Vary motion by element role; one thing moves at a time; animate only transform/opacity/clip-path.
- Always honor `prefers-reduced-motion` and keep content visible without JS.

### 5. Render, look, critique, fix (mandatory)

Open the result in a browser and screenshot it: the browser pane / preview tools, Claude in Chrome, headless Chrome, or Playwright (commands in `references/review-checklist.md`). Check ~1440px, ~1024px and ~390px, plus dark mode if supported. For motion, screenshot several scroll positions and animation frames, then again with reduced motion emulated (see `motion.md` §6). Check the console for errors — a failed CDN load silently kills all animation.

Critique honestly against `references/review-checklist.md` (and the expressive critique in `expressive.md` when relevant). Assume there are three problems; find and fix them; re-screenshot. If you truly cannot render, say so to the user and treat it as a degraded mode.

### 6. Report

Say which mode and direction you chose, the concept/signature moment if any, and what you checked visually. Briefly.

## The anti-slop list

| Tell | Do instead |
|---|---|
| Purple/indigo → blue/pink gradient hero | Solid or subtly textured background; color reserved for accent and CTA. A gradient must be on-brand and crafted (Stripe's mesh), not default |
| Everything centered | A left-aligned grid with a clear reading edge (center only short hero/empty-state content) |
| Every block in a card with a shadow; cards in cards | Spacing and quiet dividers; one level of containment |
| Emoji as icons | One consistent SVG icon set |
| Three identical feature cards | Alternating rows, bento with varied sizes, or the product shown working |
| Pure #000 on #fff; gray text on color | Near-black on tinted off-white; tint text toward its background |
| Glows, glass and giant shadows everywhere | Hairline borders, soft low-opacity elevation; one glow at most, with purpose |
| Rainbow of accents | One accent; semantic colors only for meaning |
| "Unlock your potential" copy | Specific, concrete copy |
| Bold everywhere | 500–600 for labels/headings, 400 for body |
| Focus outline removed | Visible `:focus-visible` ring |
| Inter by default, unconsidered | Type chosen for the direction and paired on purpose |
| Placeholder as label | A real `<label>` |
| Every section fades up the same way | Motion varied by role: masks for type, scale/clip for media, stagger for lists |
| Scroll-jacking, motion everywhere, 3D blob for its own sake | Native scroll in control, one thing moving at a time, 3D only when it carries the concept |

## Reference files — read when relevant

- `references/principles.md` — hierarchy, spacing, type, color, depth, states, accessibility. Any non-trivial UI.
- `references/tokens.md` — scales and CSS variables. New UI without a design system.
- `references/aesthetics.md` — named directions with fonts and palettes, product and expressive. Step 1.
- `references/components.md` — component patterns and page recipes. Product UI and Premium.
- `references/expressive.md` — what makes award-level work, concept-first brief, reference library (Locomotive, Active Theory, Resn, Bruno Simon, Apple, Linear, Stripe, Raycast, Godly, Awwwards, Codrops, Minimal Gallery), technique catalog, expressive critique. Premium and Expressive.
- `references/motion.md` — timing, easing, the six motion patterns with code, CSS-native motion, accessibility, performance, how to review motion. Any animation.
- `references/tech-stack.md` — when to use CSS, GSAP, Motion, Lenis, Three.js, R3F, Lottie, View Transitions; setup snippets and docs. Before adding any library.
- `references/review-checklist.md` — the critique checklist and screenshot commands. Always, at step 5.
- `references/sources.md` — books, design systems, studios and galleries behind the rules.

## Examples — study before building something similar

Single-file pages demonstrating the rules. Adapt patterns; don't copy wholesale.

- `examples/dashboard.html` — Product UI: app shell, KPI row, chart, table, states, dark mode.
- `examples/settings-form.html` — Product UI: labels, validation, sections, sticky save bar.
- `examples/landing.html` — Premium marketing, Editorial direction: asymmetric hero, product visual, pricing.
- `examples/motion-launch.html` — Expressive: GSAP + ScrollTrigger + Lenis with kinetic type, a pinned sequence, parallax, a horizontal gallery, magnetic CTA, and a full reduced-motion fallback.
- `examples/before-after.md` — typical AI output vs. the corrected version, with reasoning.
