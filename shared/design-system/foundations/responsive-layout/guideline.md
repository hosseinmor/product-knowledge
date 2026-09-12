---
id: design-system.foundation.responsive-layout
document_type: design-system
collection: design-system
type: foundation
title: Responsive Layout
summary: Canonical guidance for viewport ranges, breakpoint ruler values, content containers, page types, panes, container queries, and responsive testing.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: 2026-09-12
related:
  - design-system.foundation.layout
  - design-system.foundation.responsive-layout-spec
  - design-system.pattern.responsive-layout
  - design-system.reference.tailwind
---

# Responsive Layout

Responsive layout separates four decisions that should not be collapsed into one breakpoint system:

1. **Viewport ranges** — high-level page and navigation structure.
2. **Breakpoint ruler values** — fine-tuning thresholds for specific responsive scenarios.
3. **Content containers** — how far a content region is allowed to grow.
4. **Container queries** — component or pane adaptation based on its own available width.

The model is intentionally close to Primer's responsive foundation because it fits both JobVision's public product and Cando/ATS's multi-region application layouts.

## Viewport ranges

Viewport ranges are the primary semantic states for page-level responsive behavior.

| Range | Width | Major layout regions | Intended use |
|---|---:|---:|---|
| `narrow` | `< 768px` | 1 | Mobile / compact page structure |
| `regular` | `>= 768px` | Up to 2 | Desktop-friendly patterns may begin |
| `wide` | `>= 1400px` | Up to 3 | Optional third region or wide workspace |

Use viewport ranges for navigation affordance, stacking/separating major page regions, persistent panes, and optional third-region behavior.

Entering `regular` does **not** mean every page must immediately become multi-column. A page may keep a compact composition until its own content constraints fit.

## Breakpoint ruler

Breakpoint tokens are shared numeric ruler values. They are not device categories and do not each define a new page mode.

| Token | Value | Tailwind adapter |
|---|---:|---|
| `xsmall` | `320px` | `xs` |
| `small` | `544px` | `sm` |
| `medium` | `768px` | `md` |
| `large` | `1012px` | `lg` |
| `xlarge` | `1280px` | `xl` |
| `xxlarge` | `1400px` | `2xl` |

Use these values to fine-tune behavior when the three viewport ranges are too coarse. A global breakpoint must not be added for a one-off component; use a local media query or container query instead.

## Breakpoint source contract

Breakpoint values have one canonical Design System source of truth. That source generates Design System responsive CSS, Product framework configuration such as Tailwind `screens`, and any other shared runtime adapter.

Do not manually maintain a second set of breakpoint numbers in Product configuration. The Design System package remains framework-agnostic and does not depend on Tailwind. Exact machine-readable source format, generated module format, import path, and build integration are Frontend-owned.

Figma's `Typography breakpoint` collection is a separate design-time mechanism for Fluid Heading size/line-height and must not be treated as the runtime breakpoint scale.

## Content and pane padding

Padding belongs to the content or pane region itself. Do not add a second outer page-padding wrapper around a normal constrained content container.

| Breakpoint | Content padding | Pane padding |
|---|---:|---:|
| `xsmall` | `16px` | `16px` |
| `small` | `16px` | `16px` |
| `medium` | `16px` | `16px` |
| `large` | `16px` | `16px` |
| `xlarge` | `24px` | `16px` |
| `xxlarge` | `24px` | `16px` |

A container's max-width **includes its own horizontal padding**. Example: an `xlarge` container has a maximum outer width of `1280px`; with `24px` padding on both sides, the maximum visually usable inner width is `1232px`.

## Content containers

| Role | Maximum width | Typical use |
|---|---:|---|
| `interstitial` | `320px` | Sign-in, verification, focused single-task screens |
| `medium` | `768px` | Focused forms and narrow content |
| `large` | `1012px` | Settings, larger forms, constrained application pages |
| `xlarge` | `1280px` | Default centered Full page |
| `full` | `100%` | Operational workspace and split layouts that need all available space |

The numeric max-width includes the region's padding.

## Page types

### Full page

Use for ordinary centered pages. Default to `xlarge = 1280px`. Use `medium` or `large` when the task benefits from a narrower form or reading width.

For JobVision, this becomes the preferred replacement direction for the legacy `1140px` page-container convention. Migrate page-by-page rather than changing every old screen blindly.

### Split page

Use for side navigation, filtering, list-detail, persistent panes, and operational workspaces.

Rules:
- pane/navigation width is outside the constrained content max-width;
- the main content may be `full`, `medium`, `large`, or `xlarge`;
- if constrained, center the main content inside the **remaining main region**, not relative to the full viewport;
- in RTL products, persistent primary navigation normally appears on the right;
- use independent scrolling only when the pattern requires it and accessibility remains intact.

#### ATS operational workspace

Candidate Management, data tables, boards, Resume Bank, and similar operational pages should normally use Split page + `full` main content. There is no page-level max-width for the operational workspace. Use container queries for internal panes/components that become constrained.

#### ATS settings and forms

Keep the same Split-page shell, but constrain the main task when useful: `medium` for focused forms and `large` for settings/larger application pages. Center the constrained region inside the remaining main region after navigation/panes are accounted for.

#### JobVision list-detail

Treat Job list-detail as a Split page. The `regular` range begins at `768px`, but this does not force list-detail to split at `768px`. Use a fine-tune threshold such as `large = 1012px` or a container query when the minimum list + detail widths actually fit.

The legacy JobVision threshold around `992px` should migrate toward the shared `large` ruler value only after behavior is validated across the affected width interval.

### Interstitial page

Use for sign-in, verification, focused loading/transition tasks, and similar single-purpose experiences. Default maximum width: `320px`.

## Container queries

Use a container query when a reusable component or pane should react to its own available width rather than the full viewport. Good candidates include candidate cards, result rows, filter bars, toolbars, profile summaries, chart panels, and master-detail subregions inside ATS.

Viewport range and container query may be active at the same time. The page can be in `wide` while a candidate-list pane is still narrow enough to require its compact component composition.

## Reference design and QA widths

### Primary design frames

| Purpose | Width |
|---|---:|
| Compact mobile reference | `390px` |
| Regular-range boundary | `768px` |
| Large fine-tune reference | `1012px` |
| XLarge container reference | `1280px` |
| Primary wide desktop design | `1440px` |

### Responsive QA

Test both sides of meaningful thresholds: `320`, `543`, `544`, `767`, `768`, `1011`, `1012`, `1279`, `1280`, `1399`, `1400`, and `1920px`.

Also test intermediate fluid widths, RTL, text expansion, 200% zoom/reflow, keyboard navigation, and pane open/closed states where applicable.

## Figma contract

Published `Responsive layout` variables:

```text
breakpoint/xsmall      320
breakpoint/small       544
breakpoint/medium      768
breakpoint/large      1012
breakpoint/xlarge     1280
breakpoint/xxlarge    1400

container/interstitial 320
container/medium       768
container/large       1012
container/xlarge      1280

content-padding/default 16
content-padding/wide    24
pane-padding            16
```

The previous experimental `Grid/Base`, `Grid/MD`, `Grid/LG`, and `Grid/XL` styles are not part of the canonical responsive foundation. They remain hidden under `Legacy/Working/*` only to preserve existing bindings during migration.

The Figma page is named **Responsive layout** and documents Full, Split, Interstitial, JobVision, and ATS examples.

## Related documents

- [`spec.md`](spec.md): atomic rules, decision tables, migration rules, and implementation requirements.
- [`patterns.md`](patterns.md): responsive behavior for common product patterns.
- [`examples/README.md`](examples/README.md): expectations for documenting product examples.
