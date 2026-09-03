---
id: design-system.foundation.typography
collection: design-system
type: foundation
title: Typography
summary: Defines the semantic typography model for labels, body text, headings, compact UI, and responsive expressive type.
knowledge_state: unverified
document_maturity: draft
related: []
---

# Typography

## Purpose and Model

Typography uses **semantic composite tokens** so product teams choose text by role rather than repeatedly choosing raw font size, line height, and weight.

Each typography token owns:
- font size;
- line height;
- weight.

Foreground color is separate and comes from semantic color tokens.

The shared families are:

```text
type.label.*
→ short control/component text

type.body.*
→ readable body/supporting text

type.body.compact.*
→ short text in dense UI

type.heading.*
→ fixed headings

type.heading.compact.*
→ headings in dense UI

type.fluid.heading.*
type.fluid.paragraph.*
type.fluid.display.*
→ responsive expressive/editorial type
```

Typography roles are independent from product font-family choice. Product implementations should map the approved JobVision/Cando font family into the shared semantic styles rather than creating parallel semantic scales.

## Usage Rules

### Choose role before size

1. Choose the semantic family from the content role.
2. Use Compact only when text is short and the UI genuinely benefits from higher density.
3. Choose a size inside that family.
4. Do not choose a larger token only to create importance; use the hierarchy of the composition.

### Fixed vs fluid

Use fixed typography for ordinary product UI:
- controls and labels;
- forms;
- tables and boards;
- menus and lists;
- cards and Modals;
- standard product body text.

Use fluid typography for intentionally expressive/page-level content:
- prominent page or marketing headings;
- hero/campaign surfaces;
- editorial lead paragraphs;
- display text.

Do not use Fluid Heading or Display inside a reusable component merely because that component is responsive.

### Compact text

Compact styles reduce line height without changing the semantic purpose of the text. Use them for short content in dense regions such as tables, menus, kanban boards, and compact cards.

Do not use Compact Body for paragraphs or long-form reading.

### Weight and state

Shared semantic weights are:

```text
regular  → 400
medium   → 500
semibold → 600
bold     → 700
```

Do not create parallel typography families for link, error, selected, disabled, or other color/state meanings. Combine the typography role with the appropriate foreground/component semantics instead.

A component-specific typography token requires a real need to vary independently from the shared semantic role; do not create one only to alias an existing typography token.

## Definitions / Scale

The values below are the **current draft scale**. They remain subject to final Persian font-metric and implementation validation.

### Fixed styles

| Token | Size / line height | Weight |
|---|---:|---|
| `type.label.xs` | `12 / 18px` | Medium |
| `type.label.sm` | `14 / 20px` | Medium |
| `type.label.md` | `16 / 24px` | Medium |
| `type.body.xs` | `12 / 18px` | Regular |
| `type.body.sm` | `14 / 24px` | Regular |
| `type.body.md` | `16 / 28px` | Regular |
| `type.body.compact.xs` | `12 / 16px` | Regular |
| `type.body.compact.sm` | `14 / 20px` | Regular |
| `type.body.compact.md` | `16 / 24px` | Regular |
| `type.heading.compact.sm` | `14 / 20px` | SemiBold |
| `type.heading.compact.md` | `16 / 24px` | SemiBold |
| `type.heading.sm` | `14 / 22px` | SemiBold |
| `type.heading.md` | `16 / 24px` | SemiBold |
| `type.heading.lg` | `18 / 28px` | SemiBold |
| `type.heading.xl` | `20 / 30px` | SemiBold |
| `type.heading.2xl` | `24 / 34px` | Bold |
| `type.heading.3xl` | `32 / 42px` | Bold |
| `type.heading.4xl` | `42 / 54px` | Bold |

Current defaults:

```text
standard control label → type.label.sm
standard product body  → type.body.sm
compact product body   → type.body.compact.sm
```

Size suffixes are shared across fixed families where they represent the same font size (`xs=12`, `sm=14`, `md=16`, `lg=18`, `xl=20`, `2xl=24`, `3xl=32`, `4xl=42`). Do not add `default` to token names; defaults are usage guidance rather than token identity.

### Fluid styles

Fluid styles use responsive values by layout mode rather than exposing a public min/max pair.

| Token | Mobile | Tablet | Desktop | Weight |
|---|---:|---:|---:|---|
| `type.fluid.heading.xl` | `18/28` | `18/28` | `20/30` | SemiBold |
| `type.fluid.heading.2xl` | `20/30` | `20/30` | `24/34` | SemiBold |
| `type.fluid.heading.3xl` | `24/34` | `28/38` | `32/42` | Bold |
| `type.fluid.heading.4xl` | `32/42` | `36/46` | `42/54` | Bold |
| `type.fluid.paragraph.sm` | `16/28` | `16/28` | `18/32` | Regular |
| `type.fluid.paragraph.md` | `18/32` | `20/34` | `24/42` | Regular |
| `type.fluid.display.sm` | `32/42` | `40/50` | `48/60` | Bold |
| `type.fluid.display.md` | `40/50` | `48/60` | `60/72` | Bold |
| `type.fluid.display.lg` | `48/60` | `60/72` | `72/86` | Bold |
| `type.fluid.display.xl` | `48/60` | `72/86` | `96/112` | Bold |

Values are `font-size / line-height` in px.

The shared `48/60` Mobile value for Display `lg` and `xl` is intentional: very large desktop hierarchy must not force proportionally huge mobile type.

Whether implementation switches discretely at layout modes or interpolates within a range is still unresolved and must not be inferred from this table.

## Accessibility

Typography must remain usable with the actual supported Persian UI font, mixed Persian/English content, zoom, text-spacing overrides, wrapping, and responsive reflow.

Foundation-specific requirements:
- do not use automatic line height in shared semantic styles;
- keep font size and its token-defined line height together;
- validate dense/compact styles with real Persian text before treating them as stable;
- do not truncate headings or essential text merely to preserve a fixed component height.

General text resize, reflow, contrast, language, and content requirements belong to the Accessibility corpus rather than being duplicated here.

## Product Variations

The semantic typography vocabulary should remain shared between JobVision and Cando.

A product may provide a different approved font-family alias when needed, but that should not automatically create a parallel `type.*` scale. Product-specific metric differences that cannot preserve the shared contract require explicit review.

## Known Gaps

This foundation remains `draft` until these items are resolved or validated:
- final product font-family aliases;
- Persian font metrics across controls and multi-line content;
- `type.heading.sm` (`14/22`) validation;
- large Heading/Display line-height validation;
- final responsive implementation strategy for fluid type;
- canonical machine-readable token/source mapping to Figma and code.

Recommended validation frames include representative Mobile, Tablet, and Desktop widths; exact test frames are implementation/test evidence rather than part of the semantic contract.

## Live References

- Figma / Variables: exact canonical typography-variable link not yet recorded
- Token data / Code: canonical machine-readable implementation source not yet linked
