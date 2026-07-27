---
id: design-system.component.toggle-button
collection: design-system
type: component
title: Toggle Button
summary: Toggle Button represents a Button-like control with persistent selected and
  unselected states.
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

## Selected Tokens

- Low-emphasis selected → `surface-selected-muted`
- Strong selected or on/checked → `surface-selected-emphasis` + `fg-on-color`
- Selected on inverse → `surface-selected-inverse` + `fg-on-inverse`
- Selected and disabled → `surface-selected-disabled` + `fg-on-color-disabled`

Do not use Accent or brand tokens as selected-state tokens.

## Not Defined in Button Guideline v0.6

The source guideline does not define:

- Toggle Button anatomy
- Group behavior
- Keyboard model
- Exact states
- Token mapping for unselected rest state
- Sizes

These require a separate component guideline.
