# Component & Page Patterns

## Contents
- Buttons
- Form fields
- Tables
- Navigation (sidebar, top bar, tabs)
- Cards & lists
- Stats / KPI tiles
- Empty, loading, error states
- Modals, popovers, toasts
- Page recipes: app shell, dashboard, settings, landing, auth, pricing

---

## Buttons
- Sizes: 32 / 36 / 44px tall. Padding-x ≈ 1.25–1.5× the height's padding-y ratio — e.g. 36px tall → `padding: 0 14px`.
- Variants: **primary** (accent fill, `--accent-fg` text), **secondary** (surface + 1px border + shadow-xs), **ghost** (no border, hover fill `--surface-2`), **destructive** (red; usually in confirmations).
- Label: verb-first, specific ("Create project", not "Submit"). Weight 500.
- Icon + label gap 6–8px; icon 16px.
- Loading: keep width, swap label for spinner + "Saving…", disable.
- Hover: darken fill one ramp step; press: translateY(0.5px) or one more step. Transition 120ms.
- Group order: primary on the right in dialogs/forms (or left in left-aligned page headers — be consistent).

## Form fields
- Label above input, 13–14px weight 500, 6px gap. Optional fields marked "(optional)" rather than required ones starred — or the reverse, consistently.
- Help text below in `--text-muted` 13px; error text replaces/augments it in danger color with an icon.
- Input: 36–40px tall, 1px `--border-strong`, radius matches buttons, `--surface` bg, inner shadow-xs optional. Focus: border → accent + 3px ring at accent/20%.
- Width matches expected content (zip code field shouldn't be 600px).
- Group related fields in sections with a heading and a one-line description; two-column layout (description left, fields right) works well for settings pages.
- Validate on blur, not on every keystroke. Keep the submit enabled and show errors on submit rather than a mysteriously disabled button.
- Checkbox/radio: label clickable, 16px control, 8px gap. Toggles for instant-apply settings; checkboxes for settings saved with a button.

## Tables
- Left-align text, right-align numbers, `tabular-nums`. Header 12px weight 500 `--text-muted`, optionally uppercase with tracking.
- Row height 40–48px (comfortable) or 32–36px (dense). Horizontal dividers only — no vertical grid lines.
- Primary column (name) gets weight 500 and `--text`; others `--text-muted` unless they're the key value.
- Status as soft badges with a dot. Actions in a trailing `⋯` menu, revealed or always visible (don't hide critical actions on hover only for touch users).
- Sticky header for long tables; truncate long text with ellipsis + `title`.
- Include: sort indicators, an empty state, pagination or "Load more", selected-row bulk-action bar.

## Navigation
- **Sidebar (apps):** 240–272px, `--surface` or `--bg` with right border. Items 32–36px, 16px icon + 14px label, active state = `--surface-2` fill + `--text` color + optional accent icon; inactive = `--text-muted`. Group with small overline headings. Workspace/user switcher at top or bottom.
- **Top bar (marketing):** 64–72px, logo left, 3–5 links center or left, CTA right (one primary, one ghost "Sign in"). Sticky with backdrop blur + border appearing on scroll.
- **Tabs:** underline style for page sections; segmented control for switching views of the same data.
- **Breadcrumbs** for depth > 2.
- **Command palette (⌘K)** is a strong touch for power tools.

## Cards & lists
- Use cards for **independent, repeating** objects (projects, products). Don't card-ify page sections.
- Card padding 16–24px; title 14–16px semibold; meta muted; one primary action or the whole card clickable (not both).
- Lists of similar items: rows with dividers beat a grid of cards for scanability.
- Hover on clickable cards: border-strong or shadow-sm → shadow-md, 150ms.

## Stats / KPI tiles
- Label (13px muted) → value (24–32px semibold, tabular) → delta (13px, green/red with ▲▼ or arrow icon, plus "vs last month" muted).
- 3–4 per row max. Don't put icons in colored circles on every tile — it's noise.
- A tiny sparkline is fine if the data is real-shaped.

## Empty, loading, error states
- **Empty:** short headline ("No invoices yet"), one sentence of why/what, one primary action, optional simple illustration or icon at muted color. Centered within its container is OK here.
- **Loading:** skeleton blocks matching the final layout, shimmer subtle or none. Spinners only for short actions.
- **Error:** what went wrong in plain language, what the user can do, a retry button. Never just "Error".
- **First-run:** treat as onboarding — checklist or sample data.

## Modals, popovers, toasts
- Modal: 400–560px wide, radius 12px, shadow-lg, overlay at neutral-950/40–60%. Title 18px semibold, body muted, actions right-aligned at bottom. Esc closes, focus trapped, focus returns.
- Prefer inline editing or side sheets over modals for complex forms.
- Popover/dropdown: shadow-md, 1px border, 4–6px padding, items 32px.
- Toast: bottom-right (desktop), short message + optional undo, 4–6s, don't stack more than 3.

---

## Page recipes

### App shell
Sidebar (fixed) + main column. Main: page header (title 20–24px semibold, one-line description muted, actions right) → 24–32px gap → content. Content max-width ~1200px or full-bleed for tables.

### Dashboard
1. Page header with date range picker on the right.
2. KPI row (3–4 tiles), single bordered container split by dividers OR separate tiles.
3. One primary chart (2/3 width) + a supporting list (1/3), e.g. "Top customers".
4. A table of recent activity.
Avoid: 9 charts of random data, donut charts with 8 slices, gauges. Charts: muted gridlines, no chart borders, direct labels over legends where possible, one highlight color.

### Settings
Left: section nav (General, Members, Billing, API keys). Right: sections with heading + description, fields grouped, a sticky bottom save bar that appears when there are unsaved changes. Danger zone at bottom, red border-left or outlined section.

### Landing page
1. Nav. 2. Hero: headline (specific benefit, ≤10 words), subhead (1–2 lines, muted), primary + secondary CTA, **a real product visual**. Left-aligned hero with the visual to the right or below often beats centered. 3. Logo strip (muted, grayscale). 4. 2–3 feature sections with alternating text/visual, or a bento grid with varying tile sizes — not three identical icon cards. 5. Testimonial with a real-feeling name/role/photo. 6. Pricing. 7. FAQ. 8. Final CTA. 9. Footer with columns.

### Auth (sign in / sign up)
Narrow centered card (360–400px) or split screen (form left, brand/testimonial right). Logo, title, social buttons, divider "or", fields, primary full-width button, small secondary link. That's it.

### Pricing
3 tiers max visible; highlight the recommended one with a border-accent and a small badge, not by making it huge. Monthly/annual toggle with savings shown. Feature list with check icons; the differentiating features listed first.
