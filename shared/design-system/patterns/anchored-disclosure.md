---
id: design-system.pattern.anchored-disclosure
collection: design-system
type: pattern
title: Anchored Disclosure
summary: Composition contract for an actionable trigger and a replaceable floating secondary surface, with Chip filters and software skill-level selection as reference cases.
knowledge_state: verified
document_maturity: draft
design_status: review
related:
  - design-system.component.chip
  - design-system.component.select
  - design-system.component.autocomplete
  - design-system.component.popover
  - design-system.accessibility.forms
  - design-system.audit.field-family-2026-10-17
---

# Anchored Disclosure

> **Status (2026-10-17):** An editable Figma Pattern and two native Slots exist. The Figma composition and variant-override preservation have been tested. Runtime behavior, public API, accessibility implementation, and standalone Chip / Disclosure Open API are still **unverified or pending**. The canonical chip variant set was **not mutated** by this pattern pilot.

- Design file: [Disclosure · Pattern — Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23945-728)
- Pattern component set: `Disclosure / Anchored` (node `23944:770`)
- Pattern Figma page: `Disclosure · Pattern` (node `23944:665`)
- Source trigger: `Chip / Disclosure` (node `20783:534`)
- Source floating surfaces: `Selection Panel` (node `20619:306`) and `Popover / Default` (node `22790:127700`)
- Related work: HOS-30 (Chip), HOS-41 (Field Family)

## Purpose

Anchored Disclosure is a **composition pattern**, not a generic replacement for Select, Autocomplete, Popover, Menu, or Chip. It coordinates an actionable trigger with a temporary secondary surface for compact selection, configuration, or editing.

The trigger and the surfaced task retain their individual component/semantic ownership. In particular, `Chip / Disclosure` is only one possible trigger: some disclosed content is opened by `Chip / Action` (add new value) or the clickable body of `Chip / Removable` (edit committed value without removing it).

Do not create a giant parent control with filter/multi-select/removable/menu flags.

## Figma contract

| Property | Type | Default / notes |
|---|---|---|
| `Open` | Variant, `False / True` | False; controls visible Surface Slot in the Figma specimen |
| `Trigger` | Native SLOT | Defaults to `Chip / Disclosure`; preferred values Chip / Disclosure, Chip / Action, Chip / Removable |
| `Surface` | Native SLOT | Defaults to `Selection Panel / Single`; preferred values Selection Panel or Popover / Default |

The preferred components are suggestions, **not an exclusive allowlist**. A designer can replace the Slot content with another composition that satisfies this pattern, without detaching the source component.

The Pattern has exactly two variants. It intentionally **does not duplicate** the base Chip's Size / State / Applied axes or Selection Panel's Single / Multiple / Filterable axes.

**Validation:** changing `Open=True → False → True` in a temporary instance preserved both a modified trigger label and a custom Surface Slot replacement with Popover. Temporary QA instances were removed.

## Anatomy and overlay rules

```text
Disclosure / Anchored
├── Trigger [SLOT]
│   └── Chip / Disclosure  [default; replaceable]
└── Surface [SLOT]
    └── Selection Panel     [default; replaceable]
```

- In the Figma visual model, a surface is anchored to the trigger with **2px visual separation** and shown as floating content; it must not push siblings in a product form.
- `Open=True` uses an upward disclosure chevron for `Chip / Disclosure` in the Pattern source. `Open=False` uses the default downward chevron. This visual is an **instance-swap override**, not a change to the published Chip's canonical variant matrix.
- The Pattern uses a direct Surface Slot, not a mandatory Popover wrapper.
- `Selection Panel` and `Popover / Default` are both **complete floating shells**. Do not nest the entire Selection Panel inside the Popover shell, or create duplicated border/shadow/elevation.
- The anchor and surface widths need not match. Logical Start means right-aligned in RTL. Responsive placement, flipping, portal layering and viewport collision remain runtime-owned.
- Surface presentation, option rows, header/footer, filtering, draft selection and confirmation come from the supplied surface/pattern, not the Trigger.
- A Slot replacement is a design-time authoring capability; it does **not** imply that all the available surfaces have identical runtime semantics.

## State machine and accessibility boundaries

Distinguish three dimensions:

1. `Open` — temporary popup visibility, owned by the Pattern/runtime.
2. `Applied` — whether a Filter Disclosure trigger represents a committed criterion, owned by `Chip / Disclosure`.
3. `Selected` / `Value` — selection or domain data owned by the Panel/feature.

`Open` must not automatically imply `Applied`. `Hover` and `Focus` are not substitutes for `Open`.

Runtime requirements to verify:

- Real trigger semantics (normally a keyboard-operable button), `aria-expanded` and the applicable relationship with the popup.
- Enter/Space activation when appropriate, Escape dismissal, outside dismissal rules, and focus return.
- For a listbox: proper option navigation, selected versus highlighted state, and accessible announcements.
- For a form-like Popover: tab sequence, initial focus strategy, validation/error message association; do not trap focus by default in non-modal surfaces.
- Mobile fallback to a larger surface such as a bottom sheet when the floating popup cannot remain usable.
- The trigger may change capability on commit (Action → Removable); the product must manage focus/announcements at that transition.
- Runtime implementation must not infer its DOM or Angular public API solely from Figma.

## Playground cases

### A. Faceted industry filter

`Chip / Disclosure` with `Applied=true`, `Label=صنعت`, `Summary=۲` → `Selection Panel / Multiple`.

The panel owns option selection and any Confirm/Clear behavior. A change inside the panel is not committed to Applied state unless the owning product policy says so.

### B. Software + level lifecycle

Before commit:

`Chip / Action: + Microsoft Word` → opens `Selection Panel / Single` (header `انتخاب سطح مهارت`, options `مقدماتی`, `متوسط`, `پیشرفته`).

After a valid level is committed:

`Chip / Removable: Microsoft Word · متوسط ×`

- Click/tap on body opens the same level-selection surface to edit the committed level.
- `×` removes the committed software and must be a separately operable action.
- Body activation and Remove are separate keyboard-accessible targets; avoid invalid nested-button DOM.
- `Chip / Disclosure` is not automatically the right name for the *software* trigger; Action and Removable are purposeful exceptions.

For now the skill level uses a **configured Selection Panel**; do not create a new `Skill Level Picker` component unless repeat product needs and distinct functionality justify it.

### C. Custom task/parameter editor

`Chip / Disclosure` → `Popover / Default` in the Surface Slot. Popover itself owns its `Content` Slot for arbitrary content (e.g. a compact range picker). Use existing component variables/shadow; do not nest full floating shells.

## Open decisions / follow-ups

- HOS-30: decide whether the published standalone `Chip / Disclosure` should gain a native `Open` authoring property, and how to implement the open indicator while protecting 30 existing variant identities and instances. The Pattern already provides an independent Open variant and correctly oriented default/open chevrons. **Do not claim the standalone Chip property has been shipped.**
- Decide whether `Show summary` means `Applied` must be true, or whether summary and Applied remain independent authoring dimensions.
- Define focus return when the Trigger itself changes from Action to Removable on commit.
- Verify actual Angular/Storybook `open` binding, overlay positioning, typeahead/selection ownership, keyboard, zoom, long RTL option text, and mobile fallback.
- Add separate pattern-level QA for Select/Autocomplete uses where their own typed/selected semantics determine opening; do not wrap Select in Anchored Disclosure merely because it exposes a popup.

## QA summary

- [x] Native Trigger and Surface Slot on both Open variants
- [x] Existing Chip, Selection Panel, and Popover reused as linked instances
- [x] Native preferred options for three Chip trigger capabilities and two floating surfaces
- [x] Selection Panel / Multiple industry example
- [x] Software add/edit examples using Action and Removable
- [x] Customized Skill Level options inside existing Selection Panel
- [x] Popover replacement example
- [x] Open state shows/hides Surface and changes default disclosure arrow in Pattern
- [x] Variant-toggle preserves custom trigger content and custom Surface Slot content
- [x] Visual QA screenshot taken and verified
- [ ] Standalone canonical Chip Open authoring API and migration
- [ ] Real runtime interaction, keyboard and accessibility QA
- [ ] Production responsive overlay/focus behavior
