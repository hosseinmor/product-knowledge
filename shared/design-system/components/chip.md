---
id: design-system.component.chip
collection: design-system
type: component
title: Filter Chip
summary: Filter Chip is the canonical compact control for applying filters, either by opening a secondary filter surface or by toggling a filter directly.
knowledge_state: verified
document_maturity: reviewed
design_status: ready-for-dev
design_maturity: handoff-ready
last_reviewed: '2026-09-22'
related:
  - design-system.component.tag
  - design-system.component.badge
  - design-system.component.switch
  - design-system.foundation.radius
  - design-system.accessibility.focus-management
  - design-system.reference.component-mapping
---

# Filter Chip

## Purpose

Filter Chip is a compact interactive control used in filter bars and other dense filtering contexts.

The canonical family has two behavior-specific components:

- **Filter Chip / Trigger** — opens a secondary surface where the user chooses or edits filter values.
- **Filter Chip / Toggle** — applies or removes a filter directly from the chip.

Both share the same visual language, sizing, radius, state model, focus treatment, and RTL rules. They are separate component sets because their interaction contracts are meaningfully different.

## When to Use

Use Filter Chip when:

- users need to scan and operate several filters in a compact horizontal or wrapping group;
- the control represents filtering, not a general application setting;
- a filter either opens a secondary selection surface or can be changed directly with one action;
- applied/selected state should remain visible after interaction.

Typical examples include industry, location, salary, remote-work-only, and similar result-list filters.

## When Not to Use

Do not use Filter Chip for:

- informational metadata or status — use Tag;
- counts or status indicators — use Badge;
- entered/removable values or tokenized input values — use the Tag/Token pattern;
- persisted application settings that take effect immediately — use Toggle;
- arbitrary actions that do not represent filtering — use Button;
- Assist, Suggestion, or Input-chip families solely to mirror another design system taxonomy.

The first canonical version intentionally does **not** introduce separate Assist, Suggestion, or Input Chip families.

## Canonical Figma Model

Canonical file: `[DS] Job Vision NEXT`

### Filter Chip / Trigger

- Component set: `Filter Chip / Trigger`
- Figma node ID: `20783:534`
- Figma component key: `3ba6c8dc36a76632d1569108e024ae47c841a50c`
- Variant properties:
  - `Size = Small / Medium`
  - `Applied = false / true`
  - `State = Default / Hover / Active / Focus / Disabled / Open`
- Content properties:
  - `Label`
  - `Summary`
  - `Show leading icon`

`Applied=true` means that the filter currently has an active value. The optional Summary is shown only when Applied is true.

`Open` is a transient interaction state indicating that the owning secondary surface is open. Open and Applied are independent concepts.

### Filter Chip / Toggle

- Component set: `Filter Chip / Toggle`
- Figma node ID: `20783:128158`
- Figma component key: `5571e8e324b47155d7e9fd384aaea289c2e54d89`
- Variant properties:
  - `Size = Small / Medium`
  - `Selected = false / true`
  - `State = Default / Hover / Active / Focus / Disabled`
- Content properties:
  - `Label`
  - `Show leading icon`

`Selected=true` is the persistent direct-filter state. The selected treatment includes the current selection indicator from the canonical Figma component.

## Anatomy

### Trigger

The Trigger may contain, in logical reading order:

1. optional leading icon;
2. Label;
3. optional Summary when Applied;
4. required trailing chevron/indicator.

The trailing indicator communicates that activating the chip opens another surface. Do not replace it with a remove icon.

### Toggle

The Toggle may contain:

1. optional leading icon;
2. Label;
3. selection indicator when Selected.

Toggle does not expose an Open state because it does not own a secondary surface.

### Icon geometry

Canonical internal icon geometry is `18px`.

Icons use the shared icon library and their foreground color is overridden by the Filter Chip state treatment where required.

## Sizes and Geometry

| Size | Height | Typical use |
|---|---:|---|
| Small | 32px | Dense filter bars; canonical default |
| Medium | 40px | Roomier layouts or when aligned with 40px controls |

Shared geometry:

- Radius: `Radius / 6px · Medium`
- Internal gap: `6px`
- Single-line content
- Width: hug content in Figma; available parent width owns layout constraints

Reviewed Small defaults:

- Trigger inline padding: logical start `12px`, logical end `10px`
- Toggle inline padding: `12px` on both sides

Do not use Full/pill radius for Filter Chip. The canonical JobVision control radius is Medium = 6px.

## States

### Trigger states

- **Default** — idle.
- **Hover** — pointer hover.
- **Active** — press/activation feedback.
- **Focus** — keyboard focus-visible treatment.
- **Disabled** — unavailable and non-operable.
- **Open** — owning secondary filter surface is currently open.

### Toggle states

- **Default**
- **Hover**
- **Active**
- **Focus**
- **Disabled**

Selection is modeled independently through `Selected`, not as another interaction State.

### Persistent versus transient state

Keep these concepts separate:

- Trigger `Applied` = persistent filter value exists.
- Trigger `Open` = transient secondary surface visibility.
- Toggle `Selected` = persistent direct-filter state.
- Hover / Active / Focus = transient interaction feedback.

Do not encode Applied or Selected only through transient hover/focus styling.

## Color and Token Contract

Color is semantic state mapping, **not a public variant axis**.

Canonical mappings currently include:

- default unselected: `surface/default + line/default + fg/primary`
- unselected hover: `surface/neutral-muted-hover`
- unselected active: `surface/neutral-muted-active`
- selected/applied default: `surface/selected`
- selected/applied hover: `surface/selected-hover`
- selected/applied active: currently reuses `surface/selected-hover`
- disabled: disabled foreground/line treatment; selected-disabled uses the existing selected-disabled surface token
- focus: preserves the underlying state treatment and adds the shared focus effect

There is currently no dedicated selected-active surface semantic token. Do not create a component-specific chip token solely to manufacture that distinction; revisit the semantic token model if the broader system needs one.

## Focus

Filter Chip uses the shared `Focus/Default` focus treatment.

Rules:

- visible focus is for keyboard focus-visible behavior;
- focus must be rendered as the shared outside ring/effect, not by increasing the component's persistent border thickness;
- parent containers must not clip the focus ring;
- Focus is independent from Applied/Selected state.

Pointer click alone should not force a keyboard-style focus ring when the runtime platform's `:focus-visible` behavior does not require it.

## Content and Long Labels

Keep labels short and scannable.

The canonical chip is single-line. Do not allow label text to wrap inside one chip.

Figma instances hug their content and intentionally do not fake a runtime maximum width. In constrained layouts:

1. the parent/filter-bar layout owns available width;
2. long chip labels remain one line;
3. constrained labels truncate with end ellipsis;
4. the exact runtime maximum width/measurement strategy remains unverified until the runtime source is registered.

Do not encode a second multiline Filter Chip variant.

### Summary

Trigger Summary is supplemental compact state information, for example a selected-count summary.

Rules:

- Summary is visible only when `Applied=true`.
- Do not show placeholder Summary content in an unapplied Trigger.
- Keep Summary short enough that the control remains scannable.
- Detailed selected values belong in the opened filter surface or another appropriate presentation, not as an unbounded chip label.

## Groups, Wrapping, and Responsive Behavior

Filter Chips may be placed next to Button and Search/Input controls in filter bars.

At the group/container level:

- preserve each chip as one intact control;
- allow the **group** to wrap when horizontal space is insufficient;
- use the shared spacing system for inter-control gaps;
- do not stretch individual chips to equal widths by default;
- do not wrap text inside a chip to solve container pressure.

When a filter bar becomes too dense, prefer container-level wrapping, progressive disclosure, or a consolidated filter entry point rather than creating smaller unsupported chip sizes.

## RTL and Direction

Do not create separate RTL variants.

Use logical start/end behavior:

- leading icon stays at logical start;
- Trigger chevron remains at logical trailing end;
- selection indicator follows the reviewed Toggle composition;
- chip groups follow the product's RTL reading/order rules;
- directional icon assets must follow their own mirroring contract.

The canonical Figma Playground includes RTL examples and wrapping coverage.

## Accessibility Contract

Filter Chip must remain a normal keyboard-operable interactive control.

Shared requirements:

- expose an accessible name that includes the meaningful Label;
- support keyboard activation through the runtime's appropriate native/control semantics;
- show the shared focus-visible treatment for keyboard focus;
- Disabled controls must not perform their action;
- do not communicate Applied/Selected state by color alone.

### Trigger

The runtime must expose that the Trigger controls/opens another surface and must expose its open/closed state to assistive technology using appropriate platform semantics.

When the secondary surface opens, focus management follows the owning surface/popup pattern. Filter Chip itself does not redefine Menu, Popover, Dialog, or Combobox keyboard behavior.

### Toggle

The runtime must expose the direct filter's selected/on state semantically, not only visually.

The exact runtime element/ARIA implementation is deliberately unverified. Do not infer `aria-pressed`, checkbox semantics, or another concrete API solely from the Figma `Selected` property.

## Figma Authoring Rules

- Use `Filter Chip / Trigger` when activation opens a secondary selection/editing surface.
- Use `Filter Chip / Toggle` when activation directly changes a binary filter.
- Prefer Small (32px) in dense filter bars; use Medium (40px) when the surrounding control row uses the roomier control height.
- Keep `Applied` and `Selected` accurate in examples; do not fake persistent state with Hover or Active.
- Show Trigger Summary only when Applied.
- Use the optional leading icon only when it improves recognition; do not add decorative icons mechanically.
- Do not introduce a Color variant.
- Do not use legacy `Control chip`, `_Chip close button`, or other older page artifacts for new work.
- Do not detach the canonical component to reintroduce pill radius or an internal thick focus border.

## Runtime Boundary

The owning JV Design System runtime repository/package is not registered in Design System Knowledge.

The verified Storybook source is also not registered.

Therefore the following remain explicitly unverified:

- exact runtime component/API names;
- exact props/inputs/outputs;
- exact DOM elements and ARIA attribute implementation;
- Trigger popup/surface implementation and focus-transfer details;
- exact selected-state semantic implementation for Toggle;
- exact long-label max-width/truncation algorithm;
- exact framework/Tailwind class implementation;
- Storybook story/docs identifiers;
- Figma-property to code-prop mapping;
- Code Connect mapping.

Do not infer these from Figma property names.

## QA Checklist

Verify:

- both Trigger and Toggle use the 6px Medium radius;
- Small is 32px and Medium is 40px high;
- Trigger unapplied does not show Summary;
- Trigger applied can show Summary;
- Trigger Open is visually distinguishable as the owning surface's open state;
- Toggle Selected remains visible outside hover/focus;
- Default, Hover, Active, Focus, and Disabled treatments are present;
- focus uses the shared outside focus effect and is not clipped;
- Disabled content uses disabled foreground/line treatment;
- labels stay on one line;
- long constrained labels truncate rather than wrap inside the chip;
- a chip group can wrap whole controls at container level;
- RTL leading/trailing anatomy remains correct;
- optional leading icon is correctly recolored/overridden;
- runtime accessible selected/open state is verified when the owning implementation source is registered.

## Legacy

Older Chip-page artifacts remain only for migration/reference.

Do not create new instances from:

- legacy `Control chip` sets;
- legacy close-button/removable-chip constructions;
- other Carbon-derived Chip/Tag artifacts on the page.

Removable values are outside the canonical Filter Chip contract and should migrate to the Tag/Token pattern when that contract is finalized.

## Live References

- Figma file key: `rROD8ctH9UfPGAMrRrOzHe`
- Figma page: `Chip`, node `13500:300199`
- Documentation frame: `Chip / Documentation`, node `23111:553`
- Trigger set node: `20783:534`
- Trigger component key: `3ba6c8dc36a76632d1569108e024ae47c841a50c`
- Toggle set node: `20783:128158`
- Toggle component key: `5571e8e324b47155d7e9fd384aaea289c2e54d89`
- Runtime code: unregistered
- Storybook: unregistered
