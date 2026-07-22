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
- Strong selected or on/checked → `surface-selected-emphasis` + `fg-on-selected`

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
