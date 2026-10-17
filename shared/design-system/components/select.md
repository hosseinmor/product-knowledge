---
id: design-system.component.select
collection: design-system
type: component
title: Select
summary: A bounded form selection control for predefined options, with single/multiple variants and a shared selection panel.
knowledge_state: verified
document_maturity: draft
design_status: needs-family-reconciliation
related:
- design-system.component.text-input
- design-system.component.autocomplete
- design-system.accessibility.forms
- design-system.audit.field-family-2026-10-17
---

# Select

> **Source status:** The concrete Figma anatomy/axes below were checked against live Job Vision NEXT on 2026-10-17. The field-family alignment changes are **proposals**, not shipped runtime facts. [HOS-41 audit](../audits/field-family-2026-10-17.md).

## Purpose and boundaries

Select commits a value from a **defined option set**, not arbitrary free text. Use `Select / Single` for one committed value, `Select / Multiple` for multiple committed values.

- For open text: use Text Input.
- For a query that searches content: use Search.
- For typing to narrow and select suggestions: use Autocomplete; a filterable Selection Panel does not automatically make Select an autocomplete input.
- For an actions/commands popup with no field value: use Menu.
- For free-standing discrete choices when the options should remain always visible: use Choice Group / Radio / Checkbox as appropriate.

## Figma source and present authoring API

File: [DS · Job Vision NEXT](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT)

| Asset | Node ID | Role |
|---|---|---|
| Select / Single | `20552:3939` | canonical single selector |
| Select / Multiple | `23742:5660` | canonical multiple selector |
| Selection Panel | `20619:306` | shared popup panel |
| Option | `20613:21` | shared option row |
| Option Group Header | `20614:46` | grouped option heading |
| Select All | `20614:126920` | multi-select bulk selection |
| Multiple summary | `23797:6384` | collapsed multiple-value summary |

Observed top-level Select / Single and Multiple share:

- `Size`: Small, Medium, Large (**live default Large**; proposed family default Medium).
- `State`: Default, Hover, Focus, Disabled, Error, Warning, Read only, Read only focus.
- `Filled`: `False / True` **VARIANT axis** (live; not a recommended runtime prop).
- `Label`, `Helper`, `Show label`, `Mandatory`, `Show helper`;
- `Leading icon`, `Trailing icon`, `Show leading icon`, `Show clear`;
- `Error message`, `Warning message`, `Open`.

Both sets currently have **48 variants** each (3 Size × 8 State × 2 Filled). Changing the Filled axis is a migration, not a trivial one-property rename.

## Anatomy

```text
Select
├── Label row            (label + mandatory indication)
├── Field + Selection Panel
│   ├── Field            (control, content, actions, optional leading)
│   └── Selection Panel  (popup, normally visually overlaid)
└── Supporting           (helper / error / warning, depending on state)
```

The shared Selection Panel has:

- `Selection = Single / Multiple`;
- `Content state = Results / Empty / Error`;
- `Filterable = False / True`;
- authoring properties for `Grouped`, `Select all`, `Show header`, `Show footer`, `Show clear all`, `Panel title`, messages and options.

`Option` separately models `Selection = Single / Multiple`, `State = Default / Hover / Focus / Disabled` and `Selected = True / False`. Option focus/highlight and committed selection are distinct semantics.

## Geometry and RTL

| Size | Control height | Intended common radius |
|---|---:|---:|
| Small | 32px | 6px |
| Medium | 40px | 6px |
| Large | 48px | 6px |

Observed medium control: 40px, 6px radius, 1px default border; error border 2px; shared Focus Effect Style. Popup 12px radius, 2px visual gap beneath trigger, with floating elevation.

In RTL, the user-facing leading adornment is on the **right** and the trailing disclosure/clear affordance on the **left**. Directional glyphs must honor icon rules; labels, content and helper/error should remain right-aligned. Mixed Persian/Latin selected values must not invert affordance meaning.

## State ownership

- **Default / Hover / Focus:** common border/focus semantics. Focus is visible independently of selection/open state.
- **Error:** textual message and error border, not border color alone. **Error focus combination is missing as an explicit Figma state** at time of audit; reconcile under HOS-41.
- **Warning:** live legacy state. Before propagating to other fields, approve the warning semantics/ownership across Form and Product.
- **Disabled:** no interactive opening, selecting, or clear action; programmatically unavailable.
- **Read only:** keep committed value readable and distinct from Disabled; whether the popup/clear action is hidden or inert depends on approved readonly selection semantics. `Read only focus` exists in live Figma.
- **Filled:** means placeholder vs selection content in Figma, not a filled-background style and not a public runtime interaction state.
- **Open:** visual popup condition, orthogonal to focus/value/validation. Popup should not push surrounding form layout unintentionally.

## Accessibility and runtime boundary

Select requires a meaningful accessible name, associated helper/error, programmatic required/invalid/disabled support as applicable, keyboard navigability, discoverable selected values, and distinguishable highlighted/focused versus selected options.

Native `select` versus custom trigger/listbox and exact ARIA roles **must follow the registered runtime implementation**. Do not assert that the production widget uses a particular DOM pattern, focus routing, controlled API, or virtualization solely from the Figma construction.

When using a custom popup, its keyboard/focus behavior, Escape/Enter/Arrow handling, announcements, multi-select select-all semantics and external overlay positioning must be verified by runtime QA.

## HOS-41 reconciliation — proposed, not yet approved

1. Align Field label/helper/error architecture with Text Input and Autocomplete while keeping the public Select directly insertable.
2. Rename `Mandatory` to `Required` only with safe override migration.
3. Add a comprehensible `Error focus` representation preserving both red error and keyboard focus.
4. Consider converting `Filled` from a variant axis into a Boolean authoring property, preserving existing instance values and overrides.
5. Move default Size to Medium if product usage/regression supports it.
6. Decide whether Warning belongs in the shared field family or an adjacent form-level pattern.
7. Test popup/Helper overlay with open, error and readonly states, including mobile and RTL.

## Related source

- [Field Family audit](../audits/field-family-2026-10-17.md)
- [Text Input](text-input.md)
- [Search](search.md)
- [Accessible Forms](../accessibility/forms.md)
