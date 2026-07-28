---
id: design-system.foundation.responsive-layout-spec
document_type: design-system
collection: design-system
type: foundation
title: Responsive Layout Specification
summary: Atomic rules and decision tables for responsive layout behavior, implementation, and AI retrieval.
knowledge_state: unverified
document_maturity: draft
related:
  - design-system.foundation.responsive-layout
  - design-system.pattern.responsive-layout
---

# Responsive Layout Specification

> Status: Draft — this file is optimized for precise retrieval and implementation. The Design System owner must review it before approval.

## Breakpoint tokens

| Token | Minimum width | Maximum width |
|---|---:|---:|
| `base` | `0px` | `639px` |
| `sm` | `640px` | `767px` |
| `md` | `768px` | `1023px` |
| `lg` | `1024px` | `1279px` |
| `xl` | `1280px` | `1535px` |
| `2xl` | `1536px` | None |

```css
--breakpoint-sm: 40rem;
--breakpoint-md: 48rem;
--breakpoint-lg: 64rem;
--breakpoint-xl: 80rem;
--breakpoint-2xl: 96rem;
```

## Rules

### RSP-001 — Mobile-first implementation

- **Rule:** Base styles must represent the narrowest supported layout.
- **Requirement:** Base styles must not require a minimum-width media query.
- **Requirement:** Wider layouts must progressively add or adapt structure.
- **Exception:** A documented legacy constraint may temporarily use another model during migration.

### RSP-002 — Breakpoints are not devices

- **Rule:** Breakpoint tokens describe viewport thresholds only.
- **Incorrect:** `md = tablet`.
- **Correct:** `md starts at 768px`.
- **Requirement:** Device labels may appear only as non-normative examples.

### RSP-003 — Use viewport queries for page structure

- **Rule:** Page-level structural changes must use viewport breakpoints.
- **Includes:** global navigation, persistent sidebars, page grids, page padding, major panes, and page-level master-detail behavior.

### RSP-004 — Use container queries for reusable components

- **Rule:** A reusable component should use a container query when its layout depends on its own available width rather than the viewport.
- **Includes:** cards, filter bars, toolbars, result rows, profile summaries, and chart panels.
- **Exception:** A component tied permanently to one page region may use the page breakpoint when the dependency is explicit and documented.

### RSP-005 — Remain fluid between breakpoints

- **Rule:** Layouts must work throughout every range, not only at reference frame widths.
- **Requirement:** Content must not overflow, overlap, become unreachable, or create unintended horizontal scrolling between thresholds.

### RSP-006 — Add global breakpoints conservatively

- **Rule:** Do not add a global breakpoint for one page or component.
- **Requirement:** A proposed global breakpoint must solve a repeated need across multiple products, patterns, or components.
- **Fallback:** Use a local media query or container query for isolated behavior.

### RSP-007 — Name variants by behavior

- **Rule:** Component variants must describe behavior or composition, not device categories.
- **Incorrect:** `Card / Tablet`, `Modal / Desktop`.
- **Correct:** `Card / Vertical`, `Card / Horizontal`, `Modal / Dialog`, `Modal / Full-screen`.

### RSP-008 — Do not infer input capability from width

- **Rule:** Viewport width must not be used to assume touch, mouse, hover, or keyboard availability.
- **Requirement:** Essential actions must not depend on hover.
- **Requirement:** Pointer- or hover-specific refinements must use the relevant capability media features.

### RSP-009 — Keep RTL independent from breakpoint logic

- **Rule:** Breakpoint thresholds are direction-independent.
- **Requirement:** Directional spacing and positioning must use logical properties.
- **Preferred properties:** `padding-inline`, `margin-inline`, `inset-inline-start`, `border-inline-end`.

### RSP-010 — Separate containers from breakpoints

- **Rule:** Breakpoints determine behavior changes; containers determine content growth limits.
- **Requirement:** Do not create a new breakpoint only to impose a content maximum width.

### RSP-011 — Use stable UI type sizes by default

- **Rule:** Body text, labels, buttons, and common UI text should not receive a new size at every breakpoint.
- **Requirement:** Fluid type is reserved primarily for large headings, display text, marketing, and editorial contexts.

### RSP-012 — Test boundaries and ranges

- **Rule:** Responsive QA must include both sides of each meaningful breakpoint.
- **Minimum QA widths:** `360`, `640`, `767`, `768`, `1023`, `1024`, `1279`, `1280`, `1535`, `1536`, and `1920px`.
- **Requirement:** Also test content expansion, RTL, zoom, and keyboard navigation where applicable.

## Reference frames

| Purpose | Width |
|---|---:|
| Primary mobile design | `390px` |
| Tablet adaptation | `768px` |
| Compact desktop adaptation | `1024px` |
| Primary desktop design | `1440px` |

Reference frames are design and communication aids. They do not replace testing across intermediate widths.

## Grid specification

| Range | Columns | Margin | Gutter |
|---|---:|---:|---:|
| `base`–`sm` | 4 | `16px` | `16px` |
| `md` | 8 | `24px` | `16px` |
| `lg` and above | 12 | `24–32px` | `24px` |

## Suggested content containers

| Token or role | Suggested maximum width |
|---|---:|
| Reading content | `640–720px` |
| Form content | `720–800px` |
| Settings content | `960px` |
| Standard marketing page | `1200–1280px` |
| Wide marketing page | `1440px` |
| Data workspace | Fluid |

These values remain draft until validated against existing products.

## Decision table

| Situation | Preferred mechanism |
|---|---|
| Global navigation changes with viewport | Viewport breakpoint |
| Sidebar becomes persistent | Viewport breakpoint |
| Number of major page panes changes | Viewport breakpoint |
| Card changes because its parent becomes narrow | Container query |
| Toolbar wraps based on its own region | Container query |
| Display heading scales gradually | Fluid value such as `clamp()` |
| One component requires an isolated threshold | Local query |
| The same threshold recurs across products | Consider a global token |
| Content must stop expanding | Max-width container |

## Prohibited patterns

- Do not create one breakpoint per device or screen model.
- Do not use `mobile`, `tablet`, or `desktop` as normative breakpoint token names.
- Do not expose breakpoint names as component variant semantics.
- Do not assume a desktop-width viewport has hover support.
- Do not assume a compact viewport is touch-only.
- Do not require hover to discover or perform an essential action.
- Do not add a global breakpoint without repeated cross-product evidence.
- Do not design only at `390px` and `1440px` without checking intermediate behavior.
- Do not stretch reading text, forms, dialogs, or cards indefinitely on wide screens.

## Migration from Bootstrap breakpoints

Existing products may still use Bootstrap thresholds. Migration must be behavior-led rather than a blind numeric replacement.

| Existing Bootstrap threshold | Target shared threshold |
|---:|---:|
| `576px` | Review case by case; usually `640px` or a local threshold |
| `768px` | `768px` |
| `992px` | `1024px` |
| `1200px` | `1280px` |
| `1400px` | Review case by case; usually `1536px` or a container limit |

Before changing a threshold, verify navigation, tables, forms, sidebars, dialogs, and content wrapping throughout the affected width range.
