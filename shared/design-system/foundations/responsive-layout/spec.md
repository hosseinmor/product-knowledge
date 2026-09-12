---
id: design-system.foundation.responsive-layout-spec
document_type: design-system
collection: design-system
type: foundation
title: Responsive Layout Specification
summary: Atomic rules and decision tables for viewport ranges, breakpoint ruler values, containers, page types, and responsive implementation.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: 2026-09-12
related:
  - design-system.foundation.responsive-layout
  - design-system.pattern.responsive-layout
  - design-system.reference.tailwind
---

# Responsive Layout Specification

## Viewport ranges

| Range | Query intent | Major layout regions |
|---|---|---:|
| `narrow` | width below `768px` | 1 |
| `regular` | width at or above `768px` | Up to 2 |
| `wide` | width at or above `1400px` | Up to 3 |

Viewport ranges are the preferred semantic API for high-level page structure.

## Breakpoint ruler

| Token | Value | Tailwind adapter |
|---|---:|---|
| `xsmall` | `320px` | `xs` |
| `small` | `544px` | `sm` |
| `medium` | `768px` | `md` |
| `large` | `1012px` | `lg` |
| `xlarge` | `1280px` | `xl` |
| `xxlarge` | `1400px` | `2xl` |

Breakpoint values are ruler values for fine-tuning. They must not be interpreted as six separate page modes.

Generated runtime artifacts must originate from one canonical Design System source. Tailwind, CSS custom media, or other framework outputs must not re-author these numbers independently.

## Container and padding tokens

| Token | Value |
|---|---:|
| `container/interstitial` | `320px` |
| `container/medium` | `768px` |
| `container/large` | `1012px` |
| `container/xlarge` | `1280px` |
| `container/full` | `100%` |
| `content-padding/default` | `16px` |
| `content-padding/wide` | `24px` |
| `pane-padding` | `16px` |

Content padding is `16px` through `large`, then `24px` at `xlarge` and `xxlarge`. Pane padding remains `16px`.

A numeric container max-width includes its horizontal padding.

## Rules

### RSP-001 — Use viewport ranges for page structure

- **Rule:** Prefer `narrow / regular / wide` for high-level page and navigation adaptations.
- **Requirement:** Do not create a new page mode at every breakpoint ruler value.
- **Example:** Entering `regular` at `768px` permits desktop-friendly patterns but does not force a list-detail split.

### RSP-002 — Breakpoints are ruler values, not devices

- **Rule:** `xsmall / small / medium / large / xlarge / xxlarge` are shared numeric thresholds.
- **Incorrect:** `large = desktop device`.
- **Correct:** `large = 1012px`, usable as a fine-tune threshold when needed.
- **Requirement:** Device labels may appear only as non-normative examples.

### RSP-003 — Fine-tune locally before adding global semantics

- **Rule:** Use the shared breakpoint ruler or a local query for responsive cases not expressed by viewport ranges.
- **Requirement:** Do not add a global breakpoint for one page or component.
- **Fallback:** Prefer a container query when the dependency is the parent region's width.

### RSP-004 — Use container queries for reusable components and panes

- **Rule:** A reusable component should respond to its own container width when viewport width is not a reliable proxy.
- **Includes:** cards, toolbars, result rows, filter bars, candidate panes, chart panels, and master-detail subregions.

### RSP-005 — Keep container width independent from viewport range

- **Rule:** Viewport range determines page structure; container role determines content growth.
- **Requirement:** Do not create a new breakpoint only to impose a max-width.

### RSP-006 — Container max-width includes padding

- **Rule:** Horizontal content padding belongs to the content region itself.
- **Requirement:** Numeric container max-width includes that padding.
- **Incorrect:** `1280px` max-width wrapper plus an additional outer `24px` page padding layer for the same region.
- **Correct:** `1280px` content region whose internal padding is `24px` per side.

### RSP-007 — Use semantic page types

- **Full page:** centered constrained content; default `xlarge = 1280px`.
- **Split page:** pane/sidebar plus main content; main content may be `full / medium / large / xlarge`.
- **Interstitial page:** focused single-task content; default `320px`.

### RSP-008 — Split-page panes are outside main content max-width

- **Rule:** Navigation or pane width does not consume the numeric max-width token of the main content region.
- **Requirement:** If main content is constrained, center it in the remaining main region, not the full viewport.
- **RTL:** Direction is independent from breakpoint logic; persistent primary navigation normally appears on the right in JV RTL products.

### RSP-009 — Operational ATS workspaces use Full main content

- **Rule:** Candidate Management, data tables, boards, Resume Bank, and similar operational ATS pages normally use Split page + `full` main content.
- **Requirement:** Do not impose a page-level max-width on the operational workspace.
- **Requirement:** Use container queries for constrained internal panes/components.

### RSP-010 — Constrain focused ATS tasks

- **Rule:** ATS forms/settings may keep the Split-page shell while constraining the main task.
- **Preferred roles:** `medium = 768px` for focused forms; `large = 1012px` for larger settings/application pages.

### RSP-011 — JobVision Full pages default to XLarge

- **Rule:** New ordinary centered JobVision pages should default to `xlarge = 1280px` unless the content benefits from another role.
- **Migration:** Legacy `1140px` containers migrate page-by-page; do not mechanically resize every existing page without visual QA.

### RSP-012 — JobVision list-detail uses Split-page behavior

- **Rule:** List-detail does not automatically split at the start of `regular`.
- **Preferred mechanism:** Use a fine-tune threshold such as `large = 1012px` or a container query when list + detail minimum widths fit.
- **Migration:** Existing ~`992px` behavior should be tested against `1012px`.

### RSP-013 — Remain fluid between thresholds

- **Rule:** Layouts must work throughout every interval, not only at reference widths.
- **Requirement:** No unintended overflow, overlap, inaccessible actions, or accidental horizontal page scrolling.

### RSP-014 — Name variants by behavior

- **Incorrect:** `Card / Tablet`, `Modal / Desktop`.
- **Correct:** `Card / Vertical`, `Card / Horizontal`, `Modal / Dialog`, `Modal / Full-screen`.

### RSP-015 — Do not infer input capability from width

- **Rule:** Width must not be used to assume touch, mouse, hover, or keyboard support.
- **Requirement:** Essential actions must not depend on hover.
- **Requirement:** Pointer/hover refinements use capability media features.

### RSP-016 — Keep RTL independent from responsive thresholds

- **Rule:** Threshold values are direction-independent.
- **Preferred CSS:** logical properties such as `padding-inline`, `margin-inline`, `inset-inline-start`, and `border-inline-end`.

### RSP-017 — Stable UI typography by default

- **Rule:** Body, Label, Button, and ordinary UI text do not receive a new type size at each breakpoint.
- **Requirement:** Use the Typography Foundation; Fluid Heading owns its approved design-time responsive mapping separately.

### RSP-018 — Test boundaries and ranges

Minimum responsive QA widths:

`320`, `543`, `544`, `767`, `768`, `1011`, `1012`, `1279`, `1280`, `1399`, `1400`, and `1920px`.

Also test intermediate widths, content expansion, RTL, 200% zoom/reflow, keyboard navigation, and side pane open/closed states.

## Page-type decision table

| Situation | Preferred page/layout |
|---|---|
| Ordinary centered JobVision page | Full / XLarge |
| Focused form | Full or Split / Medium |
| Settings or larger constrained task | Full or Split / Large |
| ATS data table / Candidate Management / board | Split / Full |
| List-detail | Split; fine-tune split threshold |
| Sign-in / verification / one-task screen | Interstitial |
| Reusable pane/component becomes cramped | Container query |

## Tailwind mapping

Tailwind may map the shared ruler to custom screens:

| DS token | Tailwind key | Value |
|---|---|---:|
| `xsmall` | `xs` | `320px` |
| `small` | `sm` | `544px` |
| `medium` | `md` | `768px` |
| `large` | `lg` | `1012px` |
| `xlarge` | `xl` | `1280px` |
| `xxlarge` | `2xl` | `1400px` |

Tailwind screen keys are an implementation adapter over the breakpoint ruler. They do not replace `narrow / regular / wide` as page-layout semantics.

Exact custom media/variant implementation for viewport ranges and container queries remains Frontend-owned.

## Reference frames

| Purpose | Width |
|---|---:|
| Compact mobile reference | `390px` |
| Regular boundary | `768px` |
| Large fine-tune reference | `1012px` |
| XLarge container reference | `1280px` |
| Primary wide desktop design | `1440px` |

## Migration from current/legacy thresholds

Migration is behavior-led.

| Existing threshold/convention | Shared target direction |
|---|---|
| Bootstrap `576px` | Usually `small = 544px` or a local threshold |
| `768px` | `medium = 768px` |
| JobVision / Bootstrap ~`992px` | Test against `large = 1012px` |
| Bootstrap `1200px` | Usually `xlarge = 1280px` |
| `1400px` | `xxlarge = 1400px` / Wide range |
| JobVision `1140px` container | Migrate page-by-page toward Full / XLarge `1280px` |

Do not change a threshold until navigation, tables, forms, panes, dialogs, content wrapping, and zoom/reflow have been checked across the affected width interval.

## Prohibited patterns

- Do not define page structure with six independent breakpoint modes.
- Do not name global breakpoints after devices.
- Do not add a global breakpoint for one component.
- Do not maintain a second hard-coded breakpoint scale in Product Tailwind configuration.
- Do not add outer page padding around a constrained content container that already owns its horizontal padding.
- Do not include persistent nav/pane width inside the main content max-width token.
- Do not constrain operational ATS workspaces with a global page max-width.
- Do not stretch reading/form content indefinitely on wide screens.
- Do not assume desktop width means hover or mouse.
- Do not design only at 390px and 1440px without checking boundary and intermediate behavior.
