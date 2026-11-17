# frontend-design-excellence

A [Claude Code](https://claude.com/claude-code) skill that makes Claude build frontends at the level of top product teams and award-winning studios: from clean, premium product UI (Linear, Stripe, Apple, Raycast quality) to expressive, motion-rich sites with scroll storytelling, kinetic typography, pinned sections, micro-interactions, page transitions and 3D.

**Website:** https://jaiparmani.github.io/ui-craft-skill/

## What it does

First the skill picks a **mode**: Product UI (apps, dashboards, forms), Premium marketing (product and launch pages), or Expressive (portfolios, studio and campaign sites). Then it follows six steps:

1. **Brief.** Audience, the one primary action, density, a single named visual style, and for expressive work a concept and one signature moment.
2. **Tokens.** A closed set of spacing, type, color, radius, shadow and motion values.
3. **Hierarchy.** Size, weight, spacing and contrast first, color last. Every state designed.
4. **Motion plan.** Only motion that shows hierarchy, creates continuity or rewards interaction, built with the right tool: CSS, GSAP, Motion, Lenis, Three.js/React Three Fiber or Lottie.
5. **Render & critique.** Screenshot at 1440, 1024 and 390px, at several scroll positions and with reduced motion; run the checklist; fix; repeat.
6. **Report.** Briefly.

Step 5 is the one that matters: models can't judge a UI from its source code.

It also includes 17 telltale "AI look" patterns with what to do instead, nine visual directions, a reference library of award-winning and premium sites (Locomotive, Active Theory, Resn, Bruno Simon, Apple, Linear, Stripe, Raycast, Godly, Awwwards, Codrops, Minimal Gallery) with what to study in each, recipes for six motion patterns, a tech-stack guide, design tokens, component patterns, a review checklist, and four complete example pages.

## Install

```bash
git clone https://github.com/jaiparmani/ui-craft-skill
```

```bash
cp -r ui-craft-skill/frontend-design-excellence ~/.claude/skills/
```

Then ask Claude Code for any UI. The skill triggers on its own, or type `/frontend-design-excellence`.

## Repository layout

| Path | What it is |
|---|---|
| `frontend-design-excellence/` | The skill itself: `SKILL.md`, `references/`, `examples/`, `assets/`, `evals/` |
| `docs/` | The GitHub Pages website |
| `frontend-design-excellence-workspace/` | Test runs comparing Claude with and without the skill (open `review.html`) |

## Sources

The guidance draws on *Refactoring UI*, *Practical Typography*, Laws of UX, WCAG 2.2, Apple HIG, Material 3, Vercel Geist, Radix, shadcn/ui, and products known for design quality such as Linear and Stripe. The full annotated list is in [`frontend-design-excellence/references/sources.md`](frontend-design-excellence/references/sources.md).

## Test results so far

Three everyday prompts (a pricing page, an admin users table, restyling an ugly signup form) were run with and without the skill. Both passed all 22 objective checks: on everyday screens, Claude without the skill already avoids the obvious mistakes. The difference was in process: every run with the skill screenshotted its own page and fixed real problems it found, which took about 3.8× longer. The next round of tests targets expressive, motion-heavy pages, where the gap is expected to be larger.
