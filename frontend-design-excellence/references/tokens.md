# Design Tokens

Use a closed set of values. When something "needs" 13px, pick 12 or 16. Consistency reads as quality.

A ready-to-use version of everything below is in `assets/tokens.css`.

## Spacing (4px base)

| Token | px | Typical use |
|---|---|---|
| `--space-1` | 4 | icon–text gap, label–input gap |
| `--space-2` | 8 | tight inline groups, chip padding |
| `--space-3` | 12 | button padding-x (sm), table cell |
| `--space-4` | 16 | card padding (dense), field gap |
| `--space-5` | 24 | card padding, form section gap |
| `--space-6` | 32 | between content blocks |
| `--space-7` | 48 | between page sections (app) |
| `--space-8` | 64 | page sections (marketing, mobile) |
| `--space-9` | 96 | marketing sections |
| `--space-10` | 128 | hero padding |

## Type scale

App (14px base, ratio ~1.2): 12 · 13 · 14 · 16 · 20 · 24 · 30
Marketing (16px base, ratio ~1.25): 14 · 16 · 18 · 20 · 24 · 32 · 48 · 64 (use clamp for the largest)

| Role | Size | Weight | Line height | Tracking |
|---|---|---|---|---|
| Display | clamp(40px, 6vw, 72px) | 600–700 | 1.05 | −0.03em |
| H1 (app page title) | 24 | 600 | 1.25 | −0.015em |
| H2 (section) | 18–20 | 600 | 1.3 | −0.01em |
| H3 (card title) | 14–16 | 600 | 1.4 | 0 |
| Body | 14–16 | 400 | 1.55 | 0 |
| Small / meta | 12–13 | 400–500 | 1.45 | 0 |
| Overline | 11–12 | 600 | 1.3 | +0.06em, uppercase |

## Color

Build in OKLCH so lightness steps are perceptually even. Neutral ramp tinted toward the accent hue (chroma 0.005–0.02).

```css
/* Neutral (cool slate, hue 260) */
--n-0:   oklch(1 0 0);
--n-50:  oklch(0.985 0.003 260);
--n-100: oklch(0.967 0.005 260);
--n-200: oklch(0.925 0.008 260);
--n-300: oklch(0.87 0.01 260);
--n-400: oklch(0.71 0.015 260);
--n-500: oklch(0.55 0.018 260);
--n-600: oklch(0.45 0.018 260);
--n-700: oklch(0.37 0.017 260);
--n-800: oklch(0.27 0.014 260);
--n-900: oklch(0.21 0.012 260);
--n-950: oklch(0.15 0.01 260);
```

Semantic aliases — components reference these, never raw ramp values:

| Alias | Light | Dark |
|---|---|---|
| `--bg` | n-0 or n-50 | n-950 |
| `--surface` | n-0 | n-900 |
| `--surface-2` (subtle fill, hover) | n-100 | n-800 |
| `--border` | n-200 | n-800 |
| `--border-strong` | n-300 | n-700 |
| `--text` | n-900 | n-50 |
| `--text-muted` | n-600 | n-400 |
| `--text-subtle` | n-500 (large/meta only) | n-500 |
| `--accent` | accent-600 | accent-400 |
| `--accent-fg` (text on accent) | white | n-950 |
| `--accent-soft` (badge bg) | accent-50/100 | accent-950 at ~60% |

Accent hue suggestions (OKLCH hue): blue 255, indigo 275, violet 295, teal 185, green 150, amber 75, orange 50, red 25, pink 350. **Pick based on the brand and the direction, not "purple because AI".**

Semantic: success green (hue 150), warning amber (hue 75), danger red (hue 25), info blue (hue 255). Each needs a soft bg, a border, and a strong text shade.

## Radius

Pick a personality and stick to it:
- Sharp/technical: 2–4px
- Neutral product (most SaaS): 6–8px controls, 10–12px cards
- Friendly/consumer: 12–16px, pill buttons

Nested radius rule: inner radius = outer radius − padding (so nested corners look concentric).

## Shadows

```css
--shadow-xs: 0 1px 2px oklch(0.2 0.02 260 / 0.06);
--shadow-sm: 0 1px 2px oklch(0.2 0.02 260 / 0.06), 0 1px 3px oklch(0.2 0.02 260 / 0.08);
--shadow-md: 0 2px 4px oklch(0.2 0.02 260 / 0.04), 0 8px 16px -4px oklch(0.2 0.02 260 / 0.10);
--shadow-lg: 0 4px 8px oklch(0.2 0.02 260 / 0.04), 0 24px 48px -12px oklch(0.2 0.02 260 / 0.18);
```

xs: inputs/buttons. sm: cards. md: dropdowns/popovers. lg: modals. In dark mode, rely on borders and lighter surfaces; shadows barely show.

## Sizing

- Control heights: 32px (sm/dense), 36px (default app), 40–44px (marketing / touch)
- Icon sizes: 16 (inline), 20 (nav/buttons lg), 24 (feature)
- Sidebar: 240–272px; collapsed 56–64px
- Content max-widths: prose 65ch; forms 480–640px; app content 1200–1280px; marketing 1120–1200px

## Motion

```css
--ease-out: cubic-bezier(0.22, 1, 0.36, 1);
--ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
--dur-fast: 120ms; --dur: 200ms; --dur-slow: 320ms;
```

## Tailwind mapping

If the project uses Tailwind, its default scale already follows these rules (spacing 1=4px, text-sm=14px, shadow-sm, rounded-lg). Stay on the scale — avoid arbitrary values like `p-[13px]`. Extend `theme.colors` with the semantic aliases so components use `bg-surface text-muted border-border` instead of raw `gray-500`. With shadcn/ui, edit the CSS variables in `globals.css` rather than overriding per component.
