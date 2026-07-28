---
id: design-system.foundation.responsive-layout
document_type: design-system
collection: design-system
type: foundation
title: Responsive Layout
summary: Human-facing guidance for breakpoints, reference screen sizes, grids, containers, adaptive behavior, and responsive testing.
knowledge_state: unverified
document_maturity: draft
related:
  - design-system.foundation.layout
  - design-system.foundation.responsive-layout-spec
  - design-system.pattern.responsive-layout
---

# Responsive Layout

> Status: Draft — requires Design System owner review before being treated as approved guidance.

Responsive layout defines how page structures and reusable components adapt to the space available to them. It separates breakpoint tokens from device labels, reference design frames, page containers, component-level responsiveness, and QA widths.

## Core decisions

- The system uses a mobile-first breakpoint model.
- Breakpoint tokens describe viewport thresholds, not device categories.
- Page-level structural changes use viewport breakpoints.
- Reusable components should use container queries when their behavior depends on their own available width.
- Layouts must remain fluid between breakpoints.
- A global breakpoint is added only when the same threshold is repeatedly needed across products or patterns.

## Breakpoint scale

| Token | Minimum viewport width | Typical role |
|---|---:|---|
| `base` | `0px` | Default styles and compact layouts |
| `sm` | `640px` | Limited compact-layout adaptations |
| `md` | `768px` | Tablet-width and first major layout adaptations |
| `lg` | `1024px` | Full desktop structures and persistent navigation |
| `xl` | `1280px` | Standard wide desktop layouts |
| `2xl` | `1536px` | Very wide screens and max-width control |

Device names are descriptive only. For example, `md` means `viewport >= 768px`; it does not mean “tablet.”

## Reference design and QA widths

### Primary design frames

| Purpose | Width |
|---|---:|
| Mobile design | `390px` |
| Tablet adaptation | `768px` |
| Compact desktop | `1024px` |
| Desktop design | `1440px` |

### QA widths

Test at breakpoint boundaries and representative extremes:

`360`, `640`, `767`, `768`, `1023`, `1024`, `1279`, `1280`, `1535`, `1536`, and `1920px`.

Designing a complete page at every QA width is not required. Designers must define the important adaptations, and implementation must be tested across the full ranges.

## Grid

| Range | Columns | Page margin | Gutter |
|---|---:|---:|---:|
| `base`–`sm` | 4 | `16px` | `16px` |
| `md` | 8 | `24px` | `16px` |
| `lg` and above | 12 | `24–32px` | `24px` |

These values are the initial shared baseline. Product-specific exceptions must be documented where they are required.

## Containers

Breakpoint tokens determine when behavior changes. Containers determine how far content is allowed to grow.

### Product layouts

Data-heavy products such as ATS and employer tools should generally use a fluid page shell. Limit the width of internal reading, form, or settings regions rather than constraining the entire application shell.

Suggested content limits:

| Content type | Suggested maximum width |
|---|---:|
| Reading content | `640–720px` |
| Form content | `720–800px` |
| Settings content | `960px` |
| Tables, boards, and workspaces | Fluid |

### Website and marketing layouts

Marketing and editorial pages may use a centered page container with a maximum width of `1200px` or `1280px`, depending on the page composition.

## Responsive behavior by range

### Base: below `640px`

- Prefer one-column layouts.
- Collapse global navigation where required.
- Do not depend on hover for essential actions.
- Adapt dense tables through prioritization, progressive disclosure, cards, or controlled horizontal scrolling.
- Use `16px` horizontal page padding by default.

### `sm`: `640–767px`

Use this threshold for limited adaptations such as button grouping, simple form columns, or small spacing changes. Avoid major page architecture changes unless product evidence requires them.

### `md`: `768–1023px`

- Introduce meaningful two-column layouts when content supports them.
- Adapt some full-screen sheets into dialogs.
- Reveal secondary information when it remains readable.
- Use an 8-column grid and approximately `24px` page padding.

### `lg`: `1024–1279px`

- Enable persistent side navigation where appropriate.
- Support master-detail or split-view layouts.
- Present complete toolbars and data tables.
- Use the 12-column grid.

### `xl`: `1280–1535px`

Prefer increasing comfort and information density over inventing a new page architecture. Examples include opening a compact sidebar, revealing secondary table columns, or widening panes.

### `2xl`: `1536px` and above

Use max-width constraints and intentional distribution of extra space. Do not allow reading lines, forms, cards, or dialogs to stretch without purpose.

## Viewport breakpoints and container queries

Use viewport breakpoints for page-level structures, including:

- global navigation mode;
- sidebar visibility;
- page grid and page padding;
- number of major panes;
- page-level master-detail behavior.

Use container queries when a reusable component must adapt to the width of its own parent, including:

- cards;
- result rows;
- filter bars;
- toolbars;
- profile summaries;
- chart panels.

## Typography relationship

UI text, labels, body text, and button text should generally use stable type sizes. Fluid typography is more appropriate for large headings, display text, marketing surfaces, and editorial compositions. Typography rules should use a small number of responsive anchors rather than defining a different type size at every breakpoint.

## Related documents

- [`spec.md`](spec.md): atomic rules, decision tables, prohibited patterns, and implementation requirements.
- [`patterns.md`](patterns.md): responsive behavior for common product patterns.
- [`examples/README.md`](examples/README.md): expectations for documenting product examples.
