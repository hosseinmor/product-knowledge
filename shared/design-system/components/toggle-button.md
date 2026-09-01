---
id: design-system.component.toggle-button
collection: design-system
type: component
title: Toggle Button
summary: Toggle Button represents a Button-like control with persistent selected and unselected states.
knowledge_state: unverified
document_maturity: draft
related: []
---

# Toggle Button

## Purpose

Toggle Button represents a Button-like control with persistent selected and unselected states.

It is separate from the action Button component because selected state represents a value, mode, or choice rather than completion of a one-time action.

## Selection Model

Document whether the control supports:

- Independent on/off selection
- Single selection within a group
- Multiple selection within a group

## v4 Selection Semantics

Selection is a component state, not a complete global color family.

Do not bind every Toggle Button to one universal selected token. Choose the treatment according to the component anatomy and required emphasis.

Possible approved directions include:

```text
Chromatic checked/on treatment
→ surface/accent-emphasis + fg/on-color

Strong neutral current/exclusive treatment
→ surface/neutral-emphasis + fg/on-color

Selected container treatment when appropriate
→ surface/selected + fg/primary
```

A selected/on Toggle Button may use Accent as its visual cue, but Accent itself does not mean Selected.

Disabled suppresses tone:

```text
Disabled filled control
→ surface/disabled + fg/disabled
```

Do not use Brand semantics to represent selected/on state merely because Brand and Accent share Blue in JobVision.

The exact default mapping for Toggle Button remains a component-level design decision and must be validated with the final anatomy rather than inferred from the old v3 Selected matrix.

See `../experience-rules/selection.md`.

## Not Yet Defined

The shared guideline does not yet define:

- Toggle Button anatomy
- Group behavior
- Keyboard model
- Exact states
- Default mapping for unselected rest state
- Whether the default selected treatment is Accent or strong Neutral
- Sizes

These require a separate component guideline.
