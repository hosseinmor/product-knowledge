---
id: design-system.component.autocomplete
collection: design-system
type: component
title: Autocomplete
summary: Typed-query-assisted single selection using a text field and shared Selection Panel; its free-text acceptance policy is unresolved.
knowledge_state: verified
document_maturity: draft
design_status: needs-family-reconciliation
related:
- design-system.component.select
- design-system.component.search
- design-system.component.text-input
- design-system.accessibility.forms
- design-system.audit.field-family-2026-10-17
---

# Autocomplete

> **Source status:** The Figma construction below is verified against live Job Vision NEXT on 2026-10-17. The selection/value model and exact runtime API remain **unverified** until separately decided and registered.

## Purpose

Autocomplete combines editable query input with a list of relevant candidate options. It is the component for **typing to find a value** when a direct Select menu would be harder to scan.

Do not use it as a synonym for:

- Search, which captures a query to retrieve/filter content and does **not** own a suggestion popup in its base component;
- Select, which chooses a value from options but does not necessarily expose an editable query field;
- Text Input, which accepts ordinary free text without suggestion/selection behavior;
- Menu, which represents commands/actions rather than committed field data.

The **free-text policy is TBD**: whether an unmatched string may be committed, or only listed options are valid, must be explicit per approved design contract. Never infer it from the existence of a text cursor or list.

## Verified Figma source

- File: [DS · Job Vision NEXT](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT)
- Component set: `Autocomplete / Single`, node `23861:24`.
- 24 variants = 3 Size × 8 State.
- `Size`: Small, Medium (default), Large.
- `State`: Default, Hover, Focus, Error, Error focus, Disabled, Read only, Read only focus.
- `Filled`: Boolean Figma-only authoring property controlling placeholder vs shown Value.
- `Placeholder` and `Value`: separate preserved text properties.
- `Show label`, `Show helper`, `Show leading icon`, `Leading icon`, `Show clear`, `Open`, `Show chevron`.
- The shared `_Field Label` / `_Field Helper` / `_Field Error` architecture from Text Input is retained.
- Popup is a `Selection Panel` instance with `Selection = Single`, and shared Option rows. This is a visual reuse, not proof of a runtime component dependency.

## Anatomy

```text
Autocomplete / Single
├── Field label (Label, Required, optional Info)
├── Field + Selection Panel
│   ├── Editable Control
│   │   ├── Leading icon slot
│   │   ├── Query / Value content
│   │   ├── Clear action (conditional)
│   │   └── Chevron (optional)
│   └── Selection Panel (floating / overlay)
└── Supporting text (Helper or Error)
```

The Clear and Chevron actions are distinct visual affordances. Their actual focus/activation and accessible-name behavior must be defined, not inferred from the presence of icons.

## Dimensions and visual state

| Size | Control height | Common radius |
|---|---:|---:|
| Small | 32px | 6px |
| Medium | 40px | 6px |
| Large | 48px | 6px |

- Medium is the default.
- Border-only treatment; no filled visual background as a control style.
- Leading/trailing glyphs are RTL-semantic (leading on the right, trailing on the left).
- Focus Effect Style uses the shared visible 2px ring + 1px offset; focus and error coexist in Error focus.
- Error uses a 2px border and textual error.
- Read only and Read only focus are distinct from Disabled.
- Selection Panel uses the shared 12px floating shell and a 2px gap to the trigger.
- Helper/Error region remains outside the input border and must stay programmatically associated with the control, even if visually occluded by an overlay.

## Query, result and selection model

The design must distinguish:

1. **Query text** — what the user has typed for filtering.
2. **Highlighted option** — currently active suggestion (keyboard or pointer) without implying selection.
3. **Committed value** — chosen entity/value, which may have an ID distinct from display label.
4. **Displayed value** — user-readable presentation after selection.

The current Figma `Filled` boolean shows a sample populated state; it is **not** evidence that one runtime `value` variable is sufficient for all four concepts.

The panel already supports Results, Empty and Error as shared visual modes. If remote query is supported, loading, fetch errors, no-results, stale response, debouncing, minimum length and caching responsibilities should be defined between component mechanism and consuming Product. Their exact algorithms are not established in Figma.

## Accessibility and keyboard contract

Preserve a meaningful accessible label independent of placeholder; expose textual error/support via programmatic description and invalid relation.

A custom editable combobox should support predictable typing, option navigation, active-option announcements, explicit commit, Escape close, focus return, and a non-trapping Tab sequence. For an actual custom widget, implement the approved combobox/listbox semantics appropriate to the chosen value model; do not invent the precise DOM structure in Knowledge before registering runtime.

The panel must remain usable under zoom/reflow, and clear/chevron hit targets must work in RTL and mixed-script content. Disabled makes all relevant actions inert; readonly must not imply a hidden editable mode.

## Open decisions / HOS-41

- Whether value mode is **selection-only** or **free-text plus suggestion**.
- Whether `Show chevron` signals all-options dropdown behavior, and when this duplicates Select rather than supporting Autocomplete.
- Whether choosing an option immediately commits or may require separate confirmation in specialized product cases.
- Whether query and committed value reset each other on Clear / reopen.
- Minimum characters, async filtering, no-results, keyboard and dynamic announcement behavior.
- Shared Selection Panel ownership versus Autocomplete-specific result list, including overlay/Helper layering.
- Exact Angular/Storybook API and tested accessibility behavior remain unregistered.

## Related

- [Field Family audit](../audits/field-family-2026-10-17.md)
- [Select](select.md)
- [Text Input](text-input.md)
- [Search](search.md)
- [Accessible Forms](../accessibility/forms.md)
