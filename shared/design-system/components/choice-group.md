---
id: design-system.component.choice-group
collection: design-system
type: component
title: Choice Group
summary: Choice Group composes Chip / Selectable items into a labeled single- or multiple-selection group for compact choices.
knowledge_state: verified
document_maturity: reviewed
design_status: ready-for-dev
design_maturity: handoff-ready
last_reviewed: '2026-10-17'
related:
  - design-system.component.chip
  - design-system.component.radio
  - design-system.component.checkbox
  - design-system.reference.component-mapping
---

# Choice Group

## Purpose

Choice Group is the semantic group component for short, compact choices rendered with `Chip / Selectable`.

Use it when the choices are intentionally Chip-shaped, labels are short and scannable, and the group should support either single or multiple selection without introducing a generic mega Chip Group.

Choice Group owns group-level semantics and layout. Each nested Chip owns its own label, size, selected state, and transient interaction state. The Figma component is RTL-first: the group label and item collection align to logical Start (visual right).

## Canonical Figma Model

Canonical file: `[DS] Job Vision NEXT`.

- Page: `Choice Group`, node `23226:9`
- Documentation frame: `Choice Group / Documentation`, node `23226:10`
- Component set: `Choice Group`
- Figma node ID: `23229:133`
- Figma component key: `a96c066c443021689ce6add1a47be745c8aa160b`
- Variant count: `18 = 2 Selection × 3 Layout × 3 State`

### Variant properties

- `Selection = Single / Multiple`
- `Layout = Horizontal / Horizontal wrap / Vertical`
- `State = Default / Error / Warning`

### Content properties

- `Group label`
- `Show group label`
- `Required`
- `Show info`
- `Error message`
- `Warning message`
- exposed nested `Info / Tooltip` instance for tooltip configuration
- native `Items` SLOT

The Items Slot:

- requires at least two children;
- accepts variable item count;
- is restricted to the preferred `Chip / Selectable` component set;
- lets authors add, remove, reorder, and configure real Selectable Chip instances.

`Required` is a Figma authoring property that shows the required asterisk in the shared label anatomy. It does not itself enforce required behavior. Required enforcement and `allow empty` remain runtime/product rules.

`Show info` exposes the label's contextual-info affordance. The nested Tooltip instance is exposed for tooltip configuration; tooltip open/visible behavior is not a Choice Group variant.

Available width is controlled by resizing the Choice Group instance; width is not a variant axis.

Shared presentation details:

- the label row follows the Select/shared field-label anatomy, spans the group width, and aligns to logical Start (visual right in RTL);
- `Group label` uses `Label/SM`;
- `Required` uses the shared required-marker treatment;
- `Info / Tooltip` is optional and independently configurable through the exposed nested instance;
- the group-to-items gap uses the shared `8px` spacing token;
- item spacing also uses the shared `8px` spacing token;
- validation message spacing below `Items` uses the shared `4px` spacing token.

## Ownership Contract

Choice Group owns:

- the shared group label and label affordances;
- group validation `State` and supporting validation copy;
- item relationship;
- selection mode;
- layout and wrapping behavior.

Each `Chip / Selectable` item owns:

- `Label`;
- `Size`;
- `Selected`;
- interaction `State`;
- its own Hover, Active, Focus, Disabled, and selected Accent visuals.

Choice Group adds no duplicate Chip interaction overlay, selected indicator, or Chip-level validation state. Group `Error` / `Warning` is communicated by the supporting message beneath the Items collection.

## Selection Semantics

### Single

Single behaves like a radio-group-style choice set:

- at most one Chip is selected;
- an optional group may start with no selection and may return to no selection;
- a required group must prevent or validate an empty value in product/runtime logic.

`Selection=Single` does not imply `Required`.

### Multiple

Multiple behaves like a checkbox-group-style choice set:

- zero, one, or many Chips may be selected;
- changing one Chip does not automatically select, clear, or mutate another item.

## Label and validation

The Choice Group label follows the same field-label grammar used by Select:

- `Group label` is the visible label copy;
- `Required=true` shows the required asterisk;
- `Show info=true` shows the contextual-info affordance;
- the nested `Info / Tooltip` instance is exposed so tooltip content/configuration can be edited without adding tooltip state to Choice Group.

`State` is group-level validation status:

- `Default` — no validation message;
- `Error` — shows `Error message` below Items using `Body/Compact/XS` + `fg/error`;
- `Warning` — shows `Warning message` below Items using `Body/Compact/XS` + `fg/warning`.

Validation messaging does not recolor or change nested Chip state. `Chip / Selectable` continues to own Selected, Hover, Active, Focus, and Disabled visuals.

`Required` is a visual/authoring indicator in Figma. The product/runtime layer still owns whether an empty value is allowed, when validation runs, and how required state is announced programmatically.

## Layout

### Horizontal

Use for short options that fit in one row. In the RTL-first Figma master, the item collection aligns to logical Start (visual right), and the canonical default slot content is authored in right-to-left visual order.

### Horizontal wrap

Resize the group to define available width. Whole Chips wrap to additional rows; do not introduce a separate width variant.

Figma native Auto Layout has no RTL wrap-flow primitive. The Figma master therefore right-aligns the wrapped collection and keeps RTL-oriented authoring examples, while the runtime must own true RTL line flow and preserve logical option/DOM order when wrapping.

### Vertical

Use when labels or available inline space make a horizontal row harder to scan. Items align to logical Start (visual right in RTL).

Vertical item spacing is the shared `8px` spacing token.

## RTL

Do not create an RTL variant.

- Choice Group is authored RTL-first in Figma.
- `Group label` is full-width and right-aligned.
- Horizontal and wrapped item collections align to logical Start (visual right).
- Vertical items align to logical Start (visual right).
- Canonical horizontal Figma slot content is authored in right-to-left visual order so the default component reads correctly.
- Each nested Chip keeps its own RTL anatomy.
- Runtime RTL flow must preserve logical option/DOM order; resizing and wrapping must not reverse semantic reading order.
- Figma native wrap is a representational limitation, not the runtime behavior contract.

## Accessibility Contract

Expose one accessible group relationship and one accessible group label when a visible or programmatic label is available.

- Single uses radio-group-like selection and keyboard semantics.
- Multiple uses checkbox-group-like selection semantics.
- Item labels remain the accessible names of the individual choices.
- Required semantics and the current Error/Warning supporting message must be programmatically associated with the group at runtime; exact ARIA wiring remains unverified.
- Disabled belongs to an individual Chip unless the entire surrounding form/group is disabled.
- Focus visuals come from `Chip / Selectable`; Choice Group does not draw a second focus treatment.

The exact DOM elements, ARIA roles, event API, roving-focus implementation, and framework integration remain unverified until the owning runtime Design System source is registered.

Do not infer runtime prop names from Figma property names.

## Boundaries

### Use Choice Group

Use for compact, scannable choices where Chip-shaped controls are intentional and labels are short.

### Use Radio Group

Use for mutually exclusive form answers where conventional radio affordance and form semantics are primary.

### Use Checkbox Group

Use for independent form answers where conventional checkbox affordance and form semantics are primary.

### Use SelectBox / Select

Use for long lists, rich option content, search, or constrained screen space.

Do not create a generic public Chip Group, Filter Group, or Input Group. Compose those patterns from the correct primitives and document them separately.

## Runtime Boundary

The owning JV Design System runtime repository/package and verified Storybook source are not registered in Design System Knowledge.

Therefore these remain unverified:

- exact runtime component/API;
- DOM/ARIA implementation;
- keyboard event implementation details;
- props/inputs/outputs;
- Storybook identity;
- Figma-to-code property mapping;
- Code Connect mapping.

## QA Checklist

Verify:

- exactly eighteen parent variants: `2 Selection × 3 Layout × 3 State`;
- `Selection = Single / Multiple`;
- `Layout = Horizontal / Horizontal wrap / Vertical`;
- `State = Default / Error / Warning`;
- `Required` and `Show info` correctly control the label affordances;
- the nested Info/Tooltip instance remains exposed for tooltip configuration;
- Default shows no validation message; Error uses `Error message` + `fg/error`; Warning uses `Warning message` + `fg/warning`;
- Error/Warning supporting copy uses `Body/Compact/XS` and stays RTL/right-aligned;
- Items Slot contains at least two real `Chip / Selectable` instances;
- width is controlled by resizing the group, not by a variant;
- Required enforcement / allow-empty and tooltip open behavior remain runtime-owned;
- item visual states remain owned by `Chip / Selectable` and are not recolored by group validation;
- Single never has more than one selected Chip;
- Multiple never auto-clears another Chip;
- Group label is `Label/SM`, full-width, and right-aligned in RTL;
- root and item gaps consume the shared `8px` spacing token;
- horizontal/wrap collections align to visual right and canonical horizontal default content is authored RTL-first;
- vertical items align to visual right;
- runtime RTL reading/DOM order remains logical even when wrapping.
