# Design Principles

Distilled mainly from *Refactoring UI* (Wathan & Schoger), *Practical Typography* (Butterick), Laws of UX (Yablonski), and the public guidance of Apple HIG, Material 3, and Vercel Geist. See `sources.md`.

## Contents
1. Hierarchy
2. Layout & spacing
3. Typography
4. Color
5. Depth & surfaces
6. Imagery & icons
7. Motion
8. Interaction states
9. Accessibility (non-negotiable)
10. UX laws worth remembering

---

## 1. Hierarchy

Every screen has a ranking: what must be seen first, second, and what can be ignored until needed. Decide it explicitly.

- **Three levers, in order of subtlety:** color/contrast (lightest touch) → weight → size. Try the subtler lever first. A secondary label often needs only `color: var(--text-muted)`, not a smaller size.
- **De-emphasize to emphasize.** If the primary element doesn't stand out, quiet everything around it rather than inflating it.
- **Labels are secondary to values.** In a stat "Revenue: $48,210", the number is the content; the label is small and muted. Often you can drop the label entirely if the format is self-explanatory (an email address, a date).
- **Semantics ≠ visual weight.** An `<h1>` doesn't have to be huge; a section title in an app can be 14px semibold. Style to the hierarchy, not the tag.
- **Buttons follow action importance:** primary (solid accent), secondary (outline or neutral fill), tertiary (text/ghost). Destructive gets red only at the point of confirmation, or when it's the primary action of a dedicated screen.

## 2. Layout & spacing

- **Start with too much whitespace, then remove.** Cramped is the more common failure.
- **Spacing encodes relationships.** The gap between a label and its input (4–8px) must be clearly smaller than between two fields (16–24px), which is smaller than between sections (32–64px). Ambiguous spacing = ambiguous grouping.
- **Use a scale, not a ruler.** Choose from the scale (4, 8, 12, 16, 24, 32, 48, 64, 96, 128). Adjacent scale values should differ by ≥25% so differences are visible.
- **Don't fill the screen just because it's there.** A form 480px wide in a 1440px viewport is correct. Give content its natural width; constrain with `max-width`.
- **Grids are tools, not rules.** A 12-column grid helps marketing pages; app UIs often work better with fixed sidebars (240–280px) plus fluid content.
- **Align to a few strong edges.** Fewer distinct left edges = calmer layout. Check that text in different blocks shares the same left edge.
- **Optical alignment beats mathematical.** Icons with text, play triangles, and quotation marks often need a 1–2px nudge.
- **Density by context:** marketing 96–160px between sections; app pages 24–48px; tables 8–12px row padding.

## 3. Typography

- **Base size:** 16px for content/marketing; 14px is fine for dense apps; never body below 13px.
- **Line height inversely to size:** body 1.5–1.65; UI labels 1.3–1.45; large headings 1.05–1.2.
- **Letter-spacing:** tighten large headings (−0.01 to −0.03em); loosen small all-caps labels (+0.04 to +0.08em). Never all-caps body text.
- **Line length:** 45–75 characters (`max-width: 65ch`).
- **Weights:** use 2–3. Avoid 300 and below for UI text on screens — too thin. Headings 600–700; labels 500; body 400.
- **Pairings:** one family is often enough. If pairing, contrast them clearly (serif display + sans body; grotesk + mono for technical). Don't pair two similar sans-serifs.
- **Numbers in tables/dashboards:** `font-variant-numeric: tabular-nums;` so columns align.
- **Text color, not opacity, for hierarchy** on solid backgrounds — but on colored/tinted backgrounds, use a tint of that background's hue rather than gray.
- **Avoid widows in headlines:** `text-wrap: balance;` for headings, `text-wrap: pretty;` for paragraphs.
- **Fluid type for marketing:** `font-size: clamp(2.25rem, 1.5rem + 3vw, 4.5rem);` (see Utopia in sources).

## 4. Color

- **Build ramps, not single colors.** You need ~9–11 shades of neutral and accent (50→950). Pick in OKLCH/HSL so lightness steps are even. Radix Colors and Tailwind's palette are excellent ready-made ramps.
- **Tint your neutrals.** Pure gray (#888) looks dead. Shift neutrals slightly toward the brand hue (cool blue-gray for tech, warm stone for editorial).
- **60-30-10:** ~60% background neutrals, ~30% secondary surfaces/text, ≤10% accent. Accent used everywhere stops meaning anything.
- **Semantic colors are reserved:** green = success, amber = warning, red = danger/destructive, blue = info/links. Don't use red as a brand accent in an app that also needs error states unless you differentiate clearly.
- **Contrast:** body text ≥ 4.5:1, large text & UI components ≥ 3:1 (WCAG 2.2 AA). Muted text is where you'll fail — check it.
- **Don't rely on color alone** for status; pair with an icon or text.
- **Dark mode is not inversion.** Use dark neutral surfaces (not #000; e.g. oklch(0.18 0.01 260)), lighten elevated surfaces instead of darkening them, desaturate and slightly lighten accents, and reduce shadow use in favor of borders.
- **Soft backgrounds for badges:** accent-100 background + accent-800 text, not saturated fill + white.

## 5. Depth & surfaces

- **Elevation communicates layering**, not decoration. Flat page < raised card < dropdown < modal.
- **Shadows:** combine a tight, darker shadow with a large, faint one. Keep alpha low (0.04–0.12). Light comes from above: positive y-offset.
- **Borders vs. shadows:** in dense apps prefer 1px borders in neutral-200 (light) / neutral-800 (dark). Use a shadow *or* a border on a card, rarely both at full strength.
- **Fewer containers.** Before wrapping content in a card, ask whether spacing alone groups it. Separate list items with dividers or spacing, not boxes.
- **Backgrounds create sections.** Alternating a subtle surface color (neutral-50) is gentler than borders for large page sections.

## 6. Imagery & icons

- **One icon family**, consistent stroke width (1.5–2px) and size (16px inline with 14px text, 20px in nav).
- **Icons support labels; they rarely replace them.** Icon-only buttons need `aria-label` and a tooltip.
- **Show the product.** Real screenshots or a well-built UI mock beats abstract blobs and stock illustrations.
- **Images on text:** add an overlay or gradient scrim to guarantee contrast.
- **Avatars:** fallback to initials on a tinted background; never a broken image.

## 7. Motion

- **Purpose:** feedback (press), continuity (where did that come from), attention (something changed). Not decoration.
- **Durations:** 100–150ms for hover/press, 200–250ms for small transitions, 300–400ms for larger panels. Ease-out for entering, ease-in for exiting.
- **Animate transform and opacity**, not layout properties.
- **Respect `prefers-reduced-motion`.**
- Skeletons over spinners for content loading longer than ~300ms.

## 8. Interaction states

Every interactive element needs: default, hover, `:focus-visible`, active/pressed, disabled, and where relevant loading, selected, and error. Data views need: loading (skeleton), empty (explain + primary action), error (what happened + retry), partial/overflow (truncation with title tooltip, pagination). Missing states are the #1 tell of a UI that was never really used.

## 9. Accessibility (non-negotiable)

- Semantic HTML: `<button>` for actions, `<a>` for navigation, `<label for>` on every input, landmark elements (`header`, `nav`, `main`).
- Visible focus ring: `outline: 2px solid var(--accent); outline-offset: 2px;` on `:focus-visible`.
- Hit targets ≥ 24×24px (WCAG 2.2), ideally 40–44px on touch.
- Contrast per §4. Test muted text and placeholder text.
- Don't disable zoom; support 200% text zoom without breaking.
- Errors: announce with text near the field, link via `aria-describedby`.

## 10. UX laws worth remembering (Laws of UX)

- **Hick's law** — more choices, slower decisions. Trim options; progressive disclosure.
- **Fitts's law** — big, close targets are faster. Primary actions large and near the user's focus.
- **Jakob's law** — users expect your UI to work like others they know. Don't reinvent nav, forms, or tables.
- **Miller / chunking** — group information into chunks (phone numbers, card numbers, sections).
- **Aesthetic-usability effect** — polished UIs are perceived as easier to use. Polish is functional.
- **Doherty threshold** — respond within ~400ms; show optimistic UI or progress otherwise.
- **Von Restorff** — the one different thing gets noticed. Use this for exactly one thing per screen.
