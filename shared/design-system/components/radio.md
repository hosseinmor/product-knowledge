---
id: design-system.component.radio
collection: design-system
type: component
title: Radio Button
summary: Radio Button is the canonical single-selection control for choosing one option from a mutually exclusive group.
knowledge_state: canonical
document_maturity: reviewed
last_reviewed: '2026-09-19'
related:
  - design-system.reference.component-mapping
  - design-system.accessibility.keyboard-navigation
  - design-system.accessibility.pointer-touch-and-gestures
  - design-system.experience-rule.selection
---

# Radio Button

## Purpose

Radio Button is the canonical control for choosing exactly one option from a mutually exclusive set.

An individual Radio Button belongs to a Radio Group. The group owns the shared decision context, option relationship, and group-level validation content.

## When to Use

Use Radio Button when:

- the user chooses one option from a visible set of mutually exclusive choices;
- comparing the available choices directly is useful;
- the selection model is exclusive rather than independent.

## When Not to Use

Do not use Radio Button when:

- zero or more independent options may be selected; use Checkbox;
- one standalone Boolean value is being controlled; use Checkbox or Toggle depending on commit behavior;
- the options are numerous or better handled by a selection field such as Select;
- the UI is a momentary action rather than a persisted choice.

## Radio Button vs Checkbox vs Radio Card

### Radio Button

Use for a compact mutually exclusive option inside a Radio Group.

Choosing one option replaces the previously selected option in the same group.

### Checkbox

Use for independent Boolean choices or multi-selection.

Checking one Checkbox does not normally uncheck another Checkbox.

### Radio Card

Radio Card uses the same mutually exclusive selection semantics as Radio Button but presents the option on a larger selection surface when the choice needs supporting text, metadata, richer comparison, or a larger visual container.

Radio Card is a presentation pattern boundary, not a different selection model. A Radio Card group must preserve the Radio Group semantics and keyboard/accessibility contract rather than becoming a set of independent clickable cards.

## Anatomy

A Radio Button item contains:

1. **Control slot** — the authored interaction-alignment slot.
2. **Radio mark** — the 18px circular visual control.
3. **Selected dot** — the inner selected-state indicator.
4. **Item label** — the visible option label.

A Radio Group contains:

1. **Group label** — the shared label for the decision.
2. **Options** — a flexible Slot containing Radio Button items.
3. Helper, requirement, and validation content when composed through the owning form/group pattern.

## Figma Property Model

### Radio Button

Canonical component set:

```text
Radio Button / Default
```

Variant axes:

| Property | Values |
|---|---|
| `Selected` | `False`, `True` |
| `State` | `Default`, `Focus`, `Disabled` |

Content properties:

| Property | Type | Default |
|---|---|---|
| `Item label` | Text | `گزینه رادیویی` |
| `Show item label` | Boolean | `True` |

The canonical matrix contains exactly 6 variants.

There is:

- no `Position` axis;
- no `Skeleton` state inside the Radio Button selection matrix;
- no separate `Hover` visual variant;
- no separate `Active` visual variant;
- no Error or Warning Radio Button variant.

Do not add these axes without a reviewed component-contract change.

### Radio Group

Canonical component set:

```text
Radio Group / Default
```

Variant axis:

| Property | Values |
|---|---|
| `Direction` | `Vertical`, `Horizontal` |

Content/composition properties:

| Property | Type | Default |
|---|---|---|
| `Group label` | Text | `عنوان گروه` |
| `Show group label` | Boolean | `True` |
| `Options` | native Figma Slot | three editable example Radio instances |

The default Slot content is an authoring example only. Option count is flexible and is not capped by the component.

## Size and Geometry

Radio Button has one canonical visual size.

| Element | Value |
|---|---:|
| Control slot | 24 × 24 |
| Radio mark | 18 × 18 |
| Selected dot | 6 × 6 |
| Control-to-label gap | 8 |

Do not add Radio Button size variants until a repeated product need requires a second visual size.

The 18px mark is smaller than the interaction target. The item row and visible label participate in the operable target; the target must satisfy the shared pointer/touch minimum.

## States and Semantic Color Mapping

### Unselected / Default

- Radio mark border: `line/default`
- Item label: `fg/primary`
- No selected fill or dot is shown.

### Selected / Default

- Radio mark fill: `surface/accent-emphasis`
- Selected dot: `fg/on-color`
- Item label: `fg/primary`

Selection uses Accent semantics, not Brand or Success semantics.

### Focus

Focus does not replace Selected/Unselected styling.

Use the shared focus treatment:

```text
current Radio visual
+ 1px surface gap
+ 2px focus/default ring
```

Focus must not change component dimensions.

### Disabled / Unselected

- Radio mark border: `line/disabled`
- Item label: `fg/disabled`

### Disabled / Selected

- Radio mark fill: `surface/disabled`
- Selected dot: `fg/disabled`
- Item label: `fg/disabled`

The selected geometry remains visible so Disabled does not erase the persisted choice.

### Hover and Active

The current Radio Button contract does not define separate Hover or Active visual variants.

Do not infer these states from Button, Checkbox, or another component. If a future implementation needs distinct pointer feedback, treat that as a reviewed component-contract change.

## Label and Content Behavior

- The visible item label and Radio control form one logical interaction target.
- Selecting the visible label must select the associated Radio Button.
- Labels may wrap; do not truncate required option meaning with ellipsis.
- When a label wraps, align the Radio control with the first line/top of the text block rather than vertically centering it against the complete multiline label.
- `Show item label=False` is allowed only when another persistent accessible name is provided by the consuming context.
- The group label describes the shared decision; it must not behave as the label of one individual option.

## Radio Group Behavior

- Options are mutually exclusive.
- At most one option in a group is selected at a time.
- Selecting another option replaces the previous selection.
- A group may initially have no selected option when product/form policy allows it.
- Whether a selection is required is a consuming form/product policy, not a new visual Radio variant.
- Validation, requirement indication, helper text, and error messaging belong to the Radio Group/form-field composition.
- An individual Radio Button does not own an Error or Warning visual state.

### Direction

`Vertical` is the default authoring direction because it is easier to scan and accommodates longer labels.

Use `Horizontal` only when:

- the option set is short;
- labels remain concise;
- the available width prevents crowding or ambiguous wrapping.

Direction changes group layout only. It does not create different Radio Button semantics.

## Keyboard and Focus

Radio Group is a composite selection control.

Preserve native radio behavior where the runtime uses native radio inputs. For a custom implementation, follow the established WAI-ARIA Radio Group pattern.

The expected interaction model is:

- `Tab` / `Shift+Tab` enter or leave the Radio Group as one sequential interaction stop;
- when a selected option exists, focus enters on that selected Radio;
- when no option is selected, initial focus follows the chosen native/APG-compatible implementation;
- `Space` selects the focused Radio when it is not already selected;
- Arrow keys move among options and update selection according to the Radio Group pattern;
- Disabled options are not activatable.

Do not implement each Radio Button as an unrelated page-level Tab stop.

Toolbar-nested Radio Groups have a specialized APG interaction model and are outside the current base Radio Group contract.

## Accessibility

### Semantics and accessible name

The production implementation should prefer native radio inputs where the platform control satisfies product behavior.

It must:

- expose Radio/Radio Group semantics;
- expose the selected/checked state programmatically;
- associate each visible option label with its Radio control;
- provide the Radio Group with a persistent accessible name;
- associate group-level helper/error content with the group when present;
- expose Disabled state programmatically.

Exact DOM structure, element nesting, ARIA attributes, event API, and runtime prop names remain **unregistered / unverified** until the owning runtime source is registered.

### Pointer and touch

- The visual mark is 18px, but the operable target is larger.
- The target must be at least 24 × 24 CSS px or satisfy a WCAG-defined exception.
- Clicking/tapping the associated item label must operate the Radio Button.
- Do not make hover the only way to discover or operate Radio functionality.

### Visual accessibility

- Selected state must retain a geometric cue through the inner dot; color is not the only cue.
- Focus uses the shared visible Focus role.
- Essential boundary/state indicators must satisfy the shared non-text contrast contract in supported themes.
- Disabled styling must not erase which option is selected.

### Accessibility testing

Test at minimum:

- keyboard: group entry/exit, Arrow navigation, Space selection, and Disabled behavior;
- focus: visible Focus in Selected and Unselected states;
- semantics: group name, item labels, selected state, and Disabled state are exposed;
- pointer: both control and associated visible label operate the option; target contract is met;
- content: Persian and English multiline labels reflow without clipping;
- RTL: visual order and directional behavior are validated in an actual RTL context;
- visual state: Selected remains distinguishable without relying on color alone.

## RTL

RTL is the primary authored direction in the canonical Figma component.

Conceptually:

```text
Control = logical inline-start
Label   = logical inline-end
```

Therefore in RTL the control appears on the right and the label on the left.

Runtime direction should use logical layout/mirroring rather than adding a `Position=Start/End` or RTL/LTR variant axis.

Do not blindly reverse keyboard Left/Right behavior solely because the interface is RTL. Preserve native/platform behavior or the established Radio Group interaction model and validate it in RTL.

## Loading

Loading is not a Radio Button selection state.

If a screen needs a loading placeholder for an unresolved option set, use the owning loading/Skeleton pattern around the content rather than multiplying `Selected × Loading` Radio variants.

A loading placeholder is non-interactive and must not be exposed as a real selectable Radio option.

## Product Variations

JobVision and Cando share the same Radio Button and Radio Group contract.

Product and Appearance differences resolve through the Theme/token architecture rather than through product-specific Radio variants.

## Figma Reference

Canonical editable source:

- Figma file key: `rROD8ctH9UfPGAMrRrOzHe`
- Page: `Radio button `
- Page node: `435:1`
- Documentation frame: `22967:127038`

Radio Button:

- Component set: `Radio Button / Default`
- Component set node: `22971:244`
- Component key: `00c8bbdee0d9d7513833cf1f0864c65d5ad651ef`
- Variant count: `6 = 2 Selected × 3 State`

Radio Group:

- Component set: `Radio Group / Default`
- Component set node: `22973:345`
- Component key: `197d21203e078fca69206e6a9cdbb339248cb5e2`
- Variant count: `2 Direction`
- Options composition: native Figma Slot

Legacy Radio Button/Group construction remains on the page inside `Archive / Legacy radio button` — node `1880:6095` — for migration reference. It is not the canonical source.

## Code Reference

- Code repository/package: **Unregistered**
- Runtime component/API: **Unverified**
- Storybook: **Unregistered**
- Figma-property → runtime-prop mapping: **Unverified**
- Code Connect: **No registered mapping**

Do not infer runtime prop names, event names, DOM structure, or Storybook identifiers from Figma property names.

## Known Gaps

- Runtime component/API and Storybook identity are not registered.
- Exact Figma-to-runtime property mapping is not registered.
- Exact runtime DOM/native-control strategy must be verified against the owning implementation when it is registered.
- Specialized toolbar-contained Radio Group behavior is outside the current base contract.
- Legacy product instances may still require migration to the canonical Radio Button and Radio Group.

## Benchmark References

The current contract was reviewed against:

- WAI-ARIA Authoring Practices — Radio Group Pattern: https://www.w3.org/WAI/ARIA/apg/patterns/radio/
- Carbon Design System — Radio button: https://carbondesignsystem.com/components/radio-button/usage/
- Primer — Radio: https://primer.style/product/components/radio/
- Primer — RadioGroup accessibility: https://primer.style/product/components/radio-group/accessibility/

External systems are references, not owning runtime sources for JV.

## Related Guidance

- `checkbox.md`
- `switch.md`
- `../experience-rules/selection.md`
- `../accessibility/keyboard-navigation.md`
- `../accessibility/pointer-touch-and-gestures.md`
- `../accessibility/focus-management.md`
- `../integrations/component-mapping.md`
