---
id: checkbox
collection: design-system
type: component
title: Checkbox
summary: Checkbox lets users select zero or more independent options or control a single boolean choice.
knowledge_state: unverified
document_maturity: draft
related: []
design_status: draft
design_maturity: design-review
figma_file: https://www.figma.com/design/VA5qSyutH4QkLTfimzdUbe/-DS--Job-Vision
figma_node: 1880:3970
reference_system: Carbon Design System
---

# Checkbox

## Purpose

Checkbox lets users select zero or more independent options or control a single boolean choice.

`Indeterminate` represents a partial group-selection state. It is not a third persisted user choice.

This document records the current Figma review and the changes required before the component can move from design review to a stable shared component.

## Current Review Status

The Figma component was reviewed at node `1880:3970`.

### Already addressed in Figma

- `Group label` is now an independent element in Checkbox Group instead of being owned by the first Checkbox item.
- The Skeleton checkbox control has been visually neutralized and no longer reads as an enabled black control.

### Current observed structure

- Selection variants: `Unchecked`, `Checked`, `Indeterminate`
- State variants: `Enabled`, `Focus`, `Disabled`, `Skeleton`
- Current item properties: `Label`, `Label text`, `Value`, `Value text`, `Indented`
- Visual control wrapper: `24px`
- Visual checkbox mark: approximately `18px`
- Item text gap: `8px`
- Checkbox Group base width: `160px`
- Checkbox Group currently contains five nested Checkbox instances

## Required Changes Before Stable

### 1. Rename item properties

The current naming makes the visible item label look like a data value.

Current:

```text
Label
Label text
Value
Value text
```

Required:

```text
Field label
Field label text
Item label
Item label text
```

Rules:

- `Item label` is the text next to the checkbox and is the actual label of the control.
- If the optional text above a standalone Checkbox remains, call it `Field label` so it cannot be confused with the item label.
- Checkbox Group owns `Group label`; an item-level property must not be reused as the group label.
- If no validated standalone use case needs `Field label`, remove it from the base Checkbox and let the form or group wrapper own that content.

### 2. Add Hover

The current state set has no Hover state.

Add Hover for:

- `Unchecked`
- `Checked`
- `Indeterminate`

Hover must apply to the interactive item row, not only the 18px visual box. Disabled and Skeleton do not receive Hover.

The exact Hover token and visual treatment remain open and must be reviewed against the final Semantic alias values before binding.

### 3. Remove duplicated Skeleton × Selection variants

The current component contains three visually equivalent Skeleton variants:

```text
Skeleton + Unchecked
Skeleton + Checked
Skeleton + Indeterminate
```

Selection has no meaningful effect while content is loading.

Preferred structure:

```text
Interaction state:
Enabled | Hover | Focus | Disabled

Loading:
True | False
```

An alternative is one standalone `Skeleton` variant outside the Selection matrix. Do not maintain separate selection-specific Skeleton visuals.

### 4. Support flexible width and wrapped labels

The base Checkbox Group must not depend on a fixed `160px` width.

Required behavior:

- Group supports `Fill container`.
- Item label can wrap to multiple lines.
- The checkbox aligns with the first line of a multiline label, not the vertical center of the entire text block.
- Long Persian and English labels must be tested.
- The base component must not force `nowrap` on item labels.

The `160px` width may remain only as a documentation example, not as a component constraint.

### 5. Replace the indentation spacer implementation

The current `Indented` property inserts a `20px` spacer inside the row. In Hug layouts this changes intrinsic width rather than creating reliable hierarchy.

Required behavior:

- Apply indentation to the whole row through inline-start padding or a nesting wrapper.
- Do not use an internal spacer as the layout contract.
- If the system supports only one nesting level, `Indented: True | False` is sufficient.
- If multiple levels are needed later, replace the Boolean with an approved hierarchy-level model.

### 6. Expand the interactive target beyond the icon wrapper

The `24px` control wrapper must not be the full clickable target.

Required behavior:

- The whole row, including the item label, toggles the Checkbox.
- The interaction area remains usable in touch layouts without enlarging the visual checkbox mark.
- Exact minimum touch-target dimensions are not yet approved in the shared system and remain an open accessibility decision.

### 7. Bind checked states to v4 selection/Accent semantics

Checked and Indeterminate are selection states, but v4 does not use a full global Selected color family. The Checkbox state uses Accent as its chromatic cue.

Approved direction:

```text
Checked or Indeterminate
→ surface/accent-emphasis + fg/on-color

Checked or Indeterminate + Disabled
→ surface/disabled + fg/disabled
```

The check or indeterminate mark geometry continues to communicate the persisted state when Disabled; the color treatment becomes the shared Disabled treatment.

Rules:

- Do not use Brand semantics to represent Checked state.
- Accent is the visual cue; the component state remains `Checked` or `Indeterminate`.
- Focus remains independent from selection styling and uses the shared Focus role.
- The exact Unchecked border token is not approved in this review and must not be guessed.
- Figma vector assets should be replaced with Semantic variable bindings where the component model allows it.

See `../experience-rules/selection.md`.

## When to Use

Use Checkbox for:

- Selecting multiple independent options
- Opting into or out of a single optional choice
- Parent selection that can summarize partial child selection through Indeterminate

## When Not to Use

Do not use Checkbox for:

- One mutually exclusive choice from a set; use Radio
- An immediate persistent on/off setting when Switch semantics are required
- Button-like selected actions; use the appropriate selection component

## Anatomy

A Checkbox item contains:

1. Checkbox control
2. Item label
3. Optional field label, only if the standalone use case remains approved
4. Optional indentation applied to the row

A Checkbox Group contains:

1. Independent group label
2. Two or more Checkbox items
3. Optional helper, error, or requirement content when added through the form-field pattern

## Figma Property Model

### Proposed designer-facing properties

| Property | Values | Notes |
|---|---|---|
| `Selection` | `Unchecked`, `Checked`, `Indeterminate` | Keep |
| `State` | `Enabled`, `Hover`, `Focus`, `Disabled` | Add Hover |
| `Loading` | `True`, `False` | Preferred replacement for Skeleton state multiplication |
| `Item label` | text | Rename from `Value text` |
| `Show item label` | Boolean | Hide only when another accessible labeling mechanism exists |
| `Field label` | text | Keep only if a validated standalone use case exists |
| `Show field label` | Boolean | Do not use as Group label |
| `Indented` | Boolean | Implement with inline-start padding, not Spacer |

### Checkbox Group properties

| Property | Values | Notes |
|---|---|---|
| `Group label` | text | Independent from all items |
| `Show group label` | Boolean | Keep |
| Item visibility | Boolean per slot, or documented manual composition | Fixed hidden slots are a Figma implementation detail, not a product rule |

## Variants

The supported selection variants are:

- Unchecked
- Checked
- Indeterminate

No Brand, success, warning, or danger Checkbox variants are defined.

Checked state communicates selection, not Brand emphasis or validation status.

## Sizes

The current design uses:

- `24px` control wrapper
- approximately `18px` visual checkbox
- `8px` gap between control and item label

These values are current Figma observations, not a finalized shared size scale.

No additional Checkbox size variants should be introduced until a repeated product need is validated.

## States

### Enabled

The item is interactive and can toggle between Unchecked and Checked.

### Hover

Required but not yet represented in Figma.

Hover must communicate that the whole item row is interactive without changing layout.

### Focus

- Focus must be keyboard-visible.
- Focus treatment must not change component dimensions.
- Use the shared `focus/default` role on normal surfaces.
- Focus is independent from Checked and Indeterminate styling.

### Disabled

- Disabled items do not toggle.
- Disabled styling applies to both control and item label.
- Disabled does not receive Hover or Active treatment.
- Disabled suppresses tone; checked geometry may remain visible while the color treatment becomes neutral Disabled.
- Disabled must not be used as a substitute for explaining validation requirements.

### Skeleton

- Skeleton is non-interactive.
- Selection is irrelevant while Skeleton is displayed.
- The label placeholder and control placeholder should read as one loading item.
- Skeleton must not appear enabled or focusable.

## Behavior

- Clicking or tapping the item label toggles the associated Checkbox.
- The label and control are one interaction target.
- Group label does not toggle a child item.
- Indeterminate is normally calculated from child selection state rather than stored as an independent end-user value.
- Disabled and Skeleton items do not respond to pointer or keyboard activation.

The exact parent-click behavior for an Indeterminate Checkbox is not yet defined in this document.

## Checkbox Group

- Group label belongs to the group wrapper.
- Items remain independent unless product logic defines a parent-child relationship.
- The group must support a variable number of items.
- Fixed hidden instances in Figma are an authoring convenience and must not be treated as a maximum product count.
- Group width follows its container.
- Group item labels may wrap independently.

## Content Guidelines

- Item labels should state the option clearly without requiring the user to infer what the checked state means.
- Avoid using only “Yes” or “No” when the surrounding statement is not persistent and visible.
- Keep labels concise, but allow wrapping instead of truncating required meaning.
- Group label should describe the shared decision represented by the items.

## Accessibility

- Implementation should use a native checkbox input where possible.
- Visible item text must be programmatically associated with the control.
- Indeterminate must expose a mixed state, such as `aria-checked="mixed"` where applicable.
- A labeled group should use group semantics such as `fieldset` and `legend` when appropriate.
- Keyboard focus must remain visible in every selection state.
- The entire visible item row should be operable as the checkbox label.
- Removing visible item text requires another accessible name; placeholder or tooltip text is not sufficient.

## Product Variations

Checkbox is a shared control.

Product Brand color must not change the semantic meaning of Checked or Indeterminate. The checked treatment uses shared Accent semantics in v4; currently Accent resolves to the same Blue Primitive family in JobVision and Cando.

## Figma Reference

- File: `-DS- Job Vision`
- Node: `1880:3970`
- Component Set: `Checkbox / Productive` — node `3193:29303`
- Group: `Checkbox group / Productive` — node `3200:36969`
- External reference noted in Figma: Carbon Design System Checkbox

## Code Reference

Not defined yet.

The code API must preserve:

- Selection state
- Mixed or Indeterminate state
- Disabled state
- Loading or Skeleton state
- Programmatic label association
- Group semantics

## Migration Checklist

- [x] Move Group label out of the first Checkbox item
- [x] Neutralize the Skeleton checkbox visual
- [ ] Rename `Value` to `Item label`
- [ ] Rename or remove the standalone top `Label`
- [ ] Add Hover for all interactive selection variants
- [ ] Collapse Skeleton into one non-selection-specific state
- [ ] Replace fixed group width with flexible container behavior
- [ ] Enable multiline item labels
- [ ] Align the control with the first line of multiline labels
- [ ] Replace the `20px` indentation Spacer with inline-start padding or nesting
- [ ] Make the full item row interactive
- [ ] Bind Checked and Indeterminate to `surface/accent-emphasis + fg/on-color`
- [ ] Bind Disabled to the shared `surface/disabled + fg/disabled` treatment
- [ ] Confirm the Unchecked border token
- [ ] Confirm exact touch-target dimensions
- [ ] Add the code reference after implementation exists

## Known Gaps

- Hover visual treatment and token mapping are not approved yet.
- Exact minimum touch-target dimensions are not approved yet.
- The Unchecked border token is not approved yet.
- The standalone `Field label` use case still needs validation.
- Parent-click behavior from Indeterminate is not yet defined.
- The final Figma property implementation for Loading versus Skeleton remains to be selected.
- No code reference exists yet.

## Related Documents

- `../experience-rules/selection.md`
- `../tokens/jobvision-color-tokens-v4-surface-model.md`
- `../tokens/component-tokens.md`
- `button.md`
- `radio.md`
- `switch.md`
