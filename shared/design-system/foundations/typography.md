---
id: design-system.foundation.typography
collection: design-system
type: foundation
title: Typography
summary: '> Status: structure only'
knowledge_state: unverified
document_maturity: draft
related:
  - design-system.foundation.responsive-layout
---

# Typography

> Status: Draft — the semantic structure and initial values are approved for documentation, but the final font metrics and large-type line heights still require visual validation in Figma and implementation.

Typography uses semantic composite tokens rather than raw font-size values in product and marketing interfaces. Each token defines font size, line height, and weight. Color is applied separately through foreground tokens.

## Naming model

- `type.label.*` is for short control and component text.
- `type.body.*` is for readable text and supporting copy.
- `type.body.compact.*` is for dense, short UI text.
- `type.heading.*` is for fixed headings.
- `type.heading.compact.*` is for headings inside dense UI regions.
- `type.fluid.heading.*`, `type.fluid.paragraph.*`, and `type.fluid.display.*` adapt by responsive mode.
- Size suffixes are shared across fixed families where they refer to the same font size: `xs = 12px`, `sm = 14px`, `md = 16px`, `lg = 18px`, `xl = 20px`, `2xl = 24px`, `3xl = 32px`, and `4xl = 42px`.
- Fluid Heading suffixes match the corresponding fixed Heading size at desktop.
- Fluid Paragraph and Fluid Display have no fixed equivalent, so their suffixes are relative to their own family.
- Do not add `default` to token names. Defaults are documented usage choices, not token identities.

## Font families

The semantic token structure is independent of the font-family choice. Product implementations should alias a product font-family token into these semantic styles.

Current font-family values are not defined in this document.

## Weights

| Semantic weight | Intended value | Use |
|---|---:|---|
| `regular` | `400` | Body and paragraph text |
| `medium` | `500` | Labels and short control text |
| `semibold` | `600` | Small and medium headings |
| `bold` | `700` | Large headings and display text |

Do not create parallel Strong variants for the complete Label family. Components that need stronger emphasis, such as a prominent button, may override the weight at component level after the need is documented.

## Label tokens

| Token | Font size | Line height | Weight |
|---|---:|---:|---|
| `type.label.xs` | `12px` | `18px` | Medium |
| `type.label.sm` | `14px` | `20px` | Medium |
| `type.label.md` | `16px` | `24px` | Medium |

`type.label.sm` is the default label style for standard controls.

Typical use:

- field labels;
- button labels;
- tabs;
- tags and badges;
- short metadata and control text.

## Body tokens

| Token | Font size | Line height | Weight |
|---|---:|---:|---|
| `type.body.xs` | `12px` | `18px` | Regular |
| `type.body.sm` | `14px` | `24px` | Regular |
| `type.body.md` | `16px` | `28px` | Regular |

`type.body.sm` is the default body style for product interfaces.

Typical use:

- descriptions;
- notification copy;
- modal supporting text;
- empty-state copy;
- general multi-line content.

`type.body.xs` may be used for helper text, error messages, timestamps, and secondary metadata. It should not be used for long-form reading.

## Compact Body tokens

| Token | Font size | Line height | Weight |
|---|---:|---:|---|
| `type.body.compact.xs` | `12px` | `16px` | Regular |
| `type.body.compact.sm` | `14px` | `20px` | Regular |
| `type.body.compact.md` | `16px` | `24px` | Regular |

`type.body.compact.sm` is the default compact body style.

Typical use:

- tables;
- menus;
- select options;
- kanban boards;
- dense lists;
- short secondary lines inside compact cards.

Compact Body should be used for short text. Do not use it for paragraphs or extended explanations.

## Compact Heading tokens

| Token | Font size | Line height | Weight |
|---|---:|---:|---|
| `type.heading.compact.sm` | `14px` | `20px` | SemiBold |
| `type.heading.compact.md` | `16px` | `24px` | SemiBold |

Typical use:

- compact card titles;
- menu group titles;
- sidebar section titles;
- headings inside dense components.

## Heading tokens

| Token | Font size | Line height | Weight |
|---|---:|---:|---|
| `type.heading.sm` | `14px` | `22px` | SemiBold |
| `type.heading.md` | `16px` | `24px` | SemiBold |
| `type.heading.lg` | `18px` | `28px` | SemiBold |
| `type.heading.xl` | `20px` | `30px` | SemiBold |
| `type.heading.2xl` | `24px` | `34px` | Bold |
| `type.heading.3xl` | `32px` | `42px` | Bold |
| `type.heading.4xl` | `42px` | `54px` | Bold |

Heading sizes start at `sm` because the smallest fixed Heading is `14px`. The `xs` suffix remains reserved for `12px` styles.

## Responsive modes for fluid typography

Fluid typography uses responsive values by mode. It is not modeled as a public minimum-to-maximum token pair.

Use the responsive layout modes defined by the Design System:

- Mobile: base layout range;
- Tablet: `md` layout range;
- Desktop: `lg` and above.

Large fluid styles use a compressed scale on Mobile. The mobile value does not continue growing proportionally with every larger desktop token. At the top of the Display scale, multiple tokens may share the same mobile value and separate only at wider modes.

### Fluid Heading

Fluid Heading continues the fixed Heading family. Its desktop value matches the fixed Heading token with the same suffix.

| Token | Mobile | Tablet | Desktop | Weight |
|---|---:|---:|---:|---|
| `type.fluid.heading.xl` | `18/28px` | `18/28px` | `20/30px` | SemiBold |
| `type.fluid.heading.2xl` | `20/30px` | `20/30px` | `24/34px` | SemiBold |
| `type.fluid.heading.3xl` | `24/34px` | `28/38px` | `32/42px` | Bold |
| `type.fluid.heading.4xl` | `32/42px` | `36/46px` | `42/54px` | Bold |

### Fluid Paragraph

Fluid Paragraph has no fixed Paragraph family equivalent. Its size suffixes are relative to the Fluid Paragraph family.

| Token | Mobile | Tablet | Desktop | Weight |
|---|---:|---:|---:|---|
| `type.fluid.paragraph.sm` | `16/28px` | `16/28px` | `18/32px` | Regular |
| `type.fluid.paragraph.md` | `18/32px` | `20/34px` | `24/42px` | Regular |

Typical use:

- lead paragraphs;
- hero supporting copy;
- editorial introductions;
- prominent section descriptions.

Do not use Fluid Paragraph for standard product body text.

### Fluid Display

Fluid Display has no fixed equivalent. Its size suffixes are relative to the Display family.

| Token | Mobile | Tablet | Desktop | Weight |
|---|---:|---:|---:|---|
| `type.fluid.display.sm` | `32/42px` | `40/50px` | `48/60px` | Bold |
| `type.fluid.display.md` | `40/50px` | `48/60px` | `60/72px` | Bold |
| `type.fluid.display.lg` | `48/60px` | `60/72px` | `72/86px` | Bold |
| `type.fluid.display.xl` | `48/60px` | `72/86px` | `96/112px` | Bold |

The shared `48/60px` mobile value for `display.lg` and `display.xl` is intentional. Larger desktop display styles must not force proportionally larger mobile text.

## Usage rules

### Choose by role before size

1. Select the semantic family from the content role.
2. Select Compact only when the text is short and placed in a dense UI region.
3. Select a size within that family.
4. Do not choose a larger token only to make content feel more important; use the documented hierarchy of the surface.

### Fixed versus fluid

Use fixed typography for:

- labels and controls;
- buttons;
- forms;
- tables and boards;
- menus and lists;
- modal and component-level headings;
- standard product body text.

Use fluid typography for:

- page-level expressive headings;
- hero and campaign surfaces;
- marketing and editorial compositions;
- large display text;
- prominent lead paragraphs.

Do not use Fluid Heading or Display inside a reusable component merely because the component is responsive.

### Line-height rules

- Body text uses more generous line height than labels and headings.
- Compact styles reduce line height without changing the corresponding font size.
- Large Heading and Display line heights are intentionally tighter than body text.
- Do not use automatic line height in shared styles.
- Do not change font size without applying the line height defined by the same semantic token.

### Links and states

Link, error, disabled, selected, and helper-text treatments do not create parallel typography families.

Apply:

- a semantic typography token for size, line height, and weight;
- a foreground token for color;
- component or interaction rules for underline and states.

### Component mapping

Components should map to shared semantic typography tokens before introducing component-specific typography tokens.

Initial examples:

| Component role | Typography token |
|---|---|
| Default button label | `type.label.sm` |
| Large button label | `type.label.md` |
| Field label | `type.label.xs` or `type.label.sm`, according to component size |
| Input value | `type.body.compact.sm` |
| Helper or error text | `type.body.xs` |
| Menu item | `type.body.compact.sm` |
| Compact metadata | `type.body.compact.xs` |
| Card title | `type.heading.sm` or `type.heading.compact.sm` |
| Modal title | `type.heading.lg` |
| Page title | `type.heading.2xl` or a documented Fluid Heading |

Create a component-specific typography token only when a component must vary independently across products or themes and cannot safely inherit a shared semantic token.

## Localization and validation

- Validate all styles with the approved Persian UI font before marking the foundation Reviewed.
- Test one-line and multi-line Persian headings, Persian numerals, English text, mixed Persian-English content, and punctuation.
- Check line boxes in buttons, inputs, tags, tables, and menus.
- Test Fluid Heading and Display at the primary design frames: `390px`, `768px`, `1024px`, and `1440px`.
- Verify wrapping and vertical rhythm at responsive boundaries.
- Do not treat the listed line heights as final for implementation until the font-metric validation is complete.

## Open validation items

- Confirm the final product font-family alias.
- Validate the `14/22px` small Heading line height against actual Persian UI examples.
- Validate large Heading and Display line heights with the final font.
- Confirm whether responsive type values should switch discretely at modes or interpolate within the layout ranges in implementation.
