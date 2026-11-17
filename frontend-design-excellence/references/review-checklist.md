# Visual Review Checklist

Run this against a **screenshot**, not the code. Take screenshots at ~1440px and ~390px wide (and dark mode if supported). Be a harsh critic: assume there are at least three problems and find them.

## How to get a screenshot
- **Built-in browser / preview tools:** open the file or dev server URL, take a screenshot.
- **Claude in Chrome:** navigate to the file:// or localhost URL.
- **Headless Chrome (no install needed if Chrome exists):** `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars --window-size=1440,900 --screenshot=/abs/shot.png file:///abs/path/index.html` (Linux: `google-chrome` or `chromium`). A tall height like `1440,3000` captures more of a long page, but it also inflates `100vh`/`100svh` sections, so use a realistic height (900) when judging heroes. Add `--force-prefers-reduced-motion` to check the reduced-motion version, and `--virtual-time-budget=4000` to let intro animations finish. Then Read the PNG. Headless Chrome won't go narrower than ~500px, so for a phone check write a small wrapper page with `<iframe src="index.html" style="width:390px;height:844px;border:0">` and screenshot that at 500px wide (or use Playwright, which supports 390px directly).
- **Playwright CLI:** `npx -y playwright screenshot --viewport-size=1440,900 --full-page file:///abs/path/index.html shot.png` (mobile: `--viewport-size=390,844`). Then read the PNG.
- Interactive states: hover/focus a few elements via the browser tool, or temporarily add the state class.

## 1. The squint test (5 seconds)
- [ ] Blur your eyes: is the most important thing the most visually prominent?
- [ ] Is there exactly one primary action per view?
- [ ] Can you tell what the page is for within 5 seconds?

## 2. Spacing & alignment
- [ ] Gaps within groups are clearly smaller than gaps between groups.
- [ ] Shared left edges line up across sections; nothing is 2px off.
- [ ] Nothing feels cramped — especially card padding, button padding, table cells.
- [ ] Nothing floats in a sea of space either (unconstrained widths on large screens).
- [ ] All values come from the spacing scale.

## 3. Typography
- [ ] ≤ 6 sizes, ≤ 3 weights in use.
- [ ] Body lines ≤ ~75 characters.
- [ ] Headlines don't end in a single orphaned word; large headings have tightened tracking.
- [ ] Numbers in tables/stats are tabular and right-aligned.
- [ ] No all-caps body text; no ultra-thin weights.

## 4. Color & contrast
- [ ] Accent is used sparingly (≤ ~10% of the screen) and consistently means "interactive/primary".
- [ ] Muted text still passes 4.5:1 (check placeholder and meta text especially).
- [ ] Neutrals are tinted, not dead gray; backgrounds aren't pure #000.
- [ ] Semantic colors only where they carry meaning.
- [ ] Dark mode (if present) isn't just inverted; elevated surfaces are lighter.

## 5. Surfaces & depth
- [ ] No card-in-card; no unnecessary boxes around sections.
- [ ] Shadows are subtle and consistent; borders are 1px and low contrast.
- [ ] Radii are consistent; nested radii look concentric.

## 6. Content & copy
- [ ] Realistic content (no lorem ipsum, no "Item 1, Item 2").
- [ ] Copy is specific; button labels are verbs.
- [ ] Long strings, zero values, and empty lists have been considered.

## 7. States
- [ ] Hover, focus-visible, active, disabled designed for buttons, links, inputs.
- [ ] Empty, loading, and error states exist for data views.
- [ ] Form validation errors are visible, near the field, and in text (not color alone).

## 8. Responsiveness
- [ ] At 390px: no horizontal scroll, tap targets ≥ 44px, nav collapses sensibly, tables scroll or reflow.
- [ ] At 1440px+: content constrained, no comically wide lines or stretched buttons.
- [ ] Check the in-between width too (~1024px): logo strips, nav links and multi-column rows are what break there.
- [ ] Text never touches the viewport edge. Common cause: a section class using `padding: 96px 0` shorthand that silently overrides the container's side padding — use `padding-block` for vertical section spacing.
- [ ] Page width equals viewport width at 390px (check `document.documentElement.scrollWidth`). Common cause: a grid column of `1fr` containing a `<pre>`, code block or long URL — `1fr` won't shrink below its content. Use `minmax(0, 1fr)` and give long code its own `overflow-x: auto`.
- [ ] Short UI strings (tabs, buttons, toolbar labels) never wrap mid-label; use `white-space: nowrap` and shorter copy.

## 9. Motion (if anything animates)
- [ ] Each animation communicates hierarchy, creates continuity, or rewards interaction. Cut the rest.
- [ ] Motion varies by role (type, media, lists differ); one thing moves at a time.
- [ ] Screenshots at several scroll positions show good compositions, no half-revealed limbo.
- [ ] With reduced motion emulated, the page is complete and still looks designed.
- [ ] Content is visible if JS or a CDN fails; console has no errors.
- [ ] Only transform/opacity/clip-path animate; no stutter on fast scroll; pinning and parallax are simplified on phones.

## 10. Anti-slop scan
- [ ] No emoji icons, no default purple-blue gradient hero, no three identical feature cards, no glow soup, no identical fade-up on every section.
- [ ] Icons from one set with consistent stroke and size.
- [ ] It looks like it belongs to *this* product/brand, not a template.

## Output of the review
Write down the 3–5 most impactful problems you saw, fix them, re-screenshot, and confirm. Only stop when the remaining issues are minor.
