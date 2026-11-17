# Sources

The rules in this skill are drawn from these. When you need more depth, or the user names a product to emulate, use this list. If you have web access, fetching the relevant page is worthwhile for unfamiliar territory, but the essentials are already summarized in the other reference files.

## Books & guides (the foundations)

| Source | What to take from it |
|---|---|
| **Refactoring UI** — Adam Wathan & Steve Schoger (refactoringui.com) | The most practical source for developers: hierarchy through de-emphasis, spacing scales, "start with too much whitespace", color ramps, shadows, fewer borders. Most of `principles.md` §1–5 comes from here. Schoger's "UI tips" threads show before/after fixes. |
| **Practical Typography** — Matthew Butterick (practicaltypography.com) | Line length, line spacing, point size, font choice, the case against system-font defaults. Free online. |
| **Laws of UX** — Jon Yablonski (lawsofux.com) | Psychology-backed heuristics: Hick, Fitts, Jakob, Miller, Doherty, aesthetic-usability. |
| **Don't Make Me Think** — Steve Krug | Clarity, conventions, scanning behavior. |
| **The Design of Everyday Things** — Don Norman | Affordances, signifiers, feedback, mapping. |
| **Every Layout** — Heydon Pickering & Andy Bell (every-layout.dev) | Robust intrinsic CSS layout primitives (Stack, Cluster, Sidebar, Switcher). |
| **Inclusive Components** — Heydon Pickering (inclusive-components.design) | Accessible patterns for toggles, tabs, menus, cards, notifications. |
| **Nielsen Norman Group articles** (nngroup.com) | Research-backed guidance on forms, tables, navigation, empty states, error messages. |
| **WCAG 2.2** (w3.org/WAI/WCAG22/quickref) | Contrast, focus visibility, target sizes. |

## Design systems (read their docs for patterns and tokens)

| System | Why it's worth studying |
|---|---|
| **Apple Human Interface Guidelines** (developer.apple.com/design) | Platform conventions, typography, clarity/deference/depth. Essential for iOS/macOS. |
| **Material Design 3** (m3.material.io) | Thorough component specs, state layers, color roles, tonal palettes. Essential for Android. |
| **Vercel Geist** (vercel.com/geist) | Precise Product aesthetic: Geist type, gray scale, restrained color, dense controls. |
| **GitHub Primer** (primer.style) | Dense product UI done well; excellent docs on accessibility and content. |
| **Atlassian Design System** (atlassian.design) | Enterprise patterns; great content/voice guidelines. |
| **Shopify Polaris** (polaris.shopify.com) | Admin/merchant UI; strong guidance on forms, empty states, and copy. |
| **IBM Carbon** (carbondesignsystem.com) | Data-dense enterprise UI, data visualization guidelines. |
| **Radix UI + Radix Colors** (radix-ui.com, radix-ui.com/colors) | Accessible primitives; a 12-step color system where each step has a documented purpose. |
| **shadcn/ui** (ui.shadcn.com) | The de-facto modern React component baseline; CSS-variable theming. Good default if starting a React project. |
| **Tailwind CSS docs + Tailwind UI / Catalyst** (tailwindcss.com, tailwindui.com) | Spacing/type/color scales; high-quality reference layouts by the Refactoring UI authors. |
| **Open Props** (open-props.style) | Pre-built CSS custom property tokens — easy starting point for vanilla CSS. |

## Products known for craft (study the principles, never copy branding)

| Product | What it does well |
|---|---|
| **Linear** (linear.app) | Dense, fast, keyboard-first, beautiful dark mode, restrained color, subtle motion. |
| **Stripe** (stripe.com, Stripe Dashboard, Stripe Docs) | Marketing polish, clear docs layout, data tables, financial formatting. |
| **Vercel** (vercel.com) | Monochrome precision, hairline borders, crisp typography. |
| **Raycast** (raycast.com) | Command palette UX, dark premium marketing. |
| **Notion** (notion.so) | Warm friendly minimalism, content-first. |
| **Mercury** (mercury.com) | Trustworthy fintech, soft modern aesthetic. |
| **Arc / The Browser Company** | Playful premium, bold color with restraint in UI chrome. |
| **Apple product pages** (apple.com) | Cinematic scale, typographic hierarchy, imagery. |
| **Things 3** | Calm native app polish, spacing, micro-interactions. |

## Studios & award-level sites (study principles; see `expressive.md` for what to take from each)

| Site | Known for |
|---|---|
| **Locomotive** (locomotive.ca) | Immersive storytelling, typography, transitions |
| **Active Theory** (activetheory.net) | WebGL, 3D, immersive interactions |
| **Resn** (resn.co.nz) | Experimental interactions, unexpected layouts |
| **Bruno Simon** (bruno-simon.com) | Playful 3D interactions, creative navigation |

## Motion documentation
- GSAP ScrollTrigger (gsap.com/docs/v3/Plugins/ScrollTrigger) and demos (gsap.com/demos)
- Motion for React (motion.dev/docs/react)
- Lenis (github.com/darkroomengineering/lenis)
- Three.js (threejs.org), React Three Fiber (r3f.docs.pmnd.rs)
- LottieFiles (lottiefiles.com, developers.lottiefiles.com)
- Codrops tutorials (tympanus.net/codrops) — practical animation techniques with source

## Galleries for real-world examples

- **Awwwards** (awwwards.com) — Site of the Day archive; high-quality inspiration judged by a jury.
- **Godly** (godly.website) — unusual visual concepts and layouts, filterable by motion.
- **Minimal Gallery** (minimal.gallery) — minimalism, editorial composition, restraint.
- **Codrops** (tympanus.net/codrops) — experiments and animation techniques.

- **Mobbin** (mobbin.com) — huge library of real app screens by flow (onboarding, settings, checkout).
- **Refero** (refero.design) — searchable real web UI references.
- **Land-book** (land-book.com), **Lapa Ninja** — landing page inspiration.
- **SaaS Landing Page** (saaslandingpage.com), **Page Flows** (pageflows.com) — SaaS patterns and flows.
- **Dribbble / Behance** — use cautiously; many shots are not real, usable products.

## Tools

- **Fonts:** Google Fonts, Fontsource (npm), Vercel Geist (npm `geist`), Bunny Fonts (privacy-friendly).
- **Icons:** Lucide (lucide.dev), Heroicons, Phosphor, Tabler, Radix Icons.
- **Color:** OKLCH picker (oklch.com), Radix Colors, Tailwind palette, Huemint, Leonardo (Adobe, contrast-based ramps).
- **Contrast checking:** WebAIM Contrast Checker, APCA calculator.
- **Type scale:** Utopia (utopia.fyi) for fluid type & space; typescale.com.
- **Shadows:** Josh Comeau's shadow palette generator (joshwcomeau.com/shadow-palette).
- **Screenshots for review:** Playwright, the browser pane, or Claude in Chrome.

## Related writing worth knowing
- Josh W. Comeau — CSS and design-engineering articles (shadows, gradients, layout).
- Anthropic's frontend-design skill guidance — argues for committing to a bold, specific aesthetic direction and avoiding generic "AI slop" defaults (overused fonts, purple gradients, predictable layouts).
- Rauno Freiberg — "Invisible Details of Interaction Design" (rauno.me) — micro-interaction craft.
- Emil Kowalski — animation and component craft (emilkowal.ski).
