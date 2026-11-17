# Aesthetic Directions

Pick exactly one direction per project (or follow the existing brand). Each is a coherent bundle of type, color, radius, density, and detail. Mixing them is what makes UIs look accidental.

Fonts listed are free (Google Fonts / Fontsource / Vercel) unless noted. Load at most 2 families and only the weights you use.

---

## 1. Precise Product (Linear, Vercel, Raycast)
**Use for:** dev tools, SaaS apps, dashboards, anything "serious software".
- **Type:** Inter, Geist, or IBM Plex Sans; Geist Mono / JetBrains Mono for code & IDs. Tight heading tracking.
- **Color:** near-monochrome neutrals (cool, hue ~260); one restrained accent (blue, indigo, or violet). Dark mode is first-class.
- **Shape:** 6–8px radius, 1px hairline borders, minimal shadows.
- **Density:** compact; 14px base; 32–36px controls.
- **Details:** keyboard shortcut hints (`⌘K`), subtle hover fills, monospaced numbers, crisp 1px dividers.

## 2. Editorial (Stripe Press, Medium-era magazines, Substack premium)
**Use for:** content sites, blogs, portfolios, thoughtful marketing pages, docs.
- **Type:** a serif for display (Fraunces, Newsreader, Source Serif 4, Instrument Serif) + a clean sans for UI (Inter, Geist). Large, confident headlines; generous body (17–19px).
- **Color:** warm off-white paper (`oklch(0.985 0.008 85)`), deep ink text, one rich accent (oxblood, forest, deep blue).
- **Shape:** low radius (0–6px), rules/lines instead of cards.
- **Density:** airy; long measure discipline (65ch).
- **Details:** asymmetry, pull quotes, small caps overlines, hanging punctuation.

## 3. Warm Friendly (Notion, Airbnb, Duolingo-lite)
**Use for:** consumer apps, onboarding, productivity for non-technical users, education.
- **Type:** rounded or humanist sans — Nunito Sans, Figtree, Plus Jakarta Sans, DM Sans.
- **Color:** warm neutrals (stone, hue ~60), a cheerful but not neon accent (coral, green, sunflower), soft tinted section backgrounds.
- **Shape:** 12–16px radius, pill buttons, soft shadows.
- **Density:** comfortable; 16px base; 40–44px controls.
- **Details:** friendly microcopy, illustrations used sparingly, generous empty states.

## 4. Swiss / Brutalist-lite (Teenage Engineering, Are.na, agency sites)
**Use for:** portfolios, creative tools, events, products that want to feel bold and opinionated.
- **Type:** grotesk — Space Grotesk, Neue Montreal (paid), Archivo, Inter Tight; huge display sizes; mono for metadata.
- **Color:** stark black/white or off-white + one loud spot color (signal orange, electric blue, acid yellow).
- **Shape:** 0 radius, thick rules, visible grid.
- **Density:** variable — dramatic scale contrast between huge headlines and tiny labels.
- **Details:** uppercase mono labels, numbered sections, grid-aligned everything.

## 5. Premium Dark (Apple product pages, Arc, high-end fintech)
**Use for:** launches, premium products, media apps.
- **Type:** SF Pro / Inter Display / Geist, large and light-ish (500) on dark.
- **Color:** deep near-black (`oklch(0.14 0.01 270)`), layered surfaces, one luminous accent; a single soft glow at most.
- **Shape:** 12–20px radius on large media cards.
- **Density:** very airy, cinematic.
- **Details:** large product imagery, subtle gradient borders, restrained motion on scroll.

## 6. Data-Dense Pro (Bloomberg-lite, Retool, Datadog, spreadsheets)
**Use for:** internal tools, admin panels, analytics, ops consoles.
- **Type:** Inter or IBM Plex Sans at 13px; tabular numbers mandatory; IBM Plex Mono for IDs.
- **Color:** neutral; semantic colors carry meaning (status, deltas); accent only for selection/focus.
- **Shape:** 4–6px radius, tight borders.
- **Density:** very compact; 28–32px rows; sticky headers; zebra or hover rows.
- **Details:** right-aligned numbers, inline sparklines, filters as chips, bulk actions bar.

## 7. Soft Modern / Fintech (Mercury, Ramp, Wise)
**Use for:** finance, B2B products that need trust and warmth.
- **Type:** Inter / Geist / Manrope; large numerals for balances.
- **Color:** light warm-cool neutrals, one deep trustworthy accent (navy, deep green, ink purple).
- **Shape:** 10–12px radius, soft layered shadows.
- **Density:** medium.
- **Details:** clean charts, clear money formatting, calm success states.

## 8. Immersive Studio (Active Theory, Bruno Simon, Resn)
**Use for:** agency/studio sites, campaigns, portfolios where the experience *is* the message.
- **Type:** a distinctive display face (wide/condensed grotesk like Unbounded, Syne, Space Grotesk, or a mono like JetBrains Mono for HUD-style labels) at extreme scale; tiny uppercase labels.
- **Color:** dark stage (`oklch(0.12 0.01 260)`) or one saturated full-bleed color; light comes from the 3D scene or imagery.
- **Shape:** minimal chrome — corner-anchored nav, thin pills, little else.
- **Density:** one idea per screen.
- **Motion:** the signature is a WebGL/3D scene or a playful interaction (drag, hold, drive); transitions between scenes instead of page loads.
- **Must:** a fast static fallback, a skip/contents path, and readable text over the scene.

## 9. Kinetic Editorial (Locomotive, editorial portfolios, Minimal Gallery)
**Use for:** studio sites, case studies, culture/brand storytelling.
- **Type:** huge grotesk or high-contrast serif headlines (Inter Tight, Neue Montreal-like grotesks, Instrument Serif, Fraunces) that run off the viewport; refined small text.
- **Color:** off-white paper or near-black, plus one accent or full-bleed imagery.
- **Shape:** rules and hairlines, no cards; asymmetric grid with big negative space.
- **Motion:** smooth scroll (Lenis), mask-revealed lines, marquees, image clip/scale reveals, sticky stacking sections, page transitions.
- **Details:** grain overlay, numbered sections, custom cursor with a label on media.

---

## Choosing quickly

| Building… | Default direction |
|---|---|
| SaaS dashboard / dev tool | Precise Product |
| Internal admin / analytics | Data-Dense Pro |
| Landing page for a dev tool | Precise Product (dark) or Swiss |
| Landing page for a consumer app | Warm Friendly |
| Blog / docs / personal site | Editorial |
| Finance / banking | Soft Modern |
| Product launch / premium hardware | Premium Dark |
| Portfolio / creative studio | Kinetic Editorial, Swiss or Immersive Studio |
| Campaign / award-submission / experiential site | Immersive Studio or Kinetic Editorial |
| Premium product launch | Premium Dark or Precise Product + scroll storytelling |

If the user gives a reference ("like Linear", "like Stripe"), study what makes that product distinctive (see `sources.md`) and match the *principles* (spacing rhythm, type choices, restraint) — don't clone their branding, logos, or copy.
