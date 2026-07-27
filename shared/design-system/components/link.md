---
id: design-system.component.link
collection: design-system
type: component
title: Link
summary: Links navigate users to another destination.
knowledge_state: unverified
document_maturity: draft
related: []
---

# Link

## Purpose

Links navigate users to another destination.

## Semantics

Use a native anchor when activating the control changes the current destination.

A Link may visually resemble a Button, but it must preserve:

- Link semantics
- Keyboard behavior
- Destination behavior
- Accessible announcement
- Expected browser behavior

Use Button when the control changes state or performs an operation in the current context.

## Token Roles

```text
link-default
link-hover
link-visited

link-emphasis
link-emphasis-hover

link-inverse
link-inverse-hover
```

- Default is the normal Link role.
- Hover is the pointer-hover state of Default.
- Visited is the persistent state for a destination that has already been opened. Do not use it for pressed/active interaction.
- Emphasis is the higher-emphasis product Link role.
- Inverse adapts Default for `surface-inverse`; it is contextual, not a third Link role.

Figma uses slash-grouped variables such as `link/default` and `link/inverse-hover`. Code uses the flattened names above.

## Button-Styled Links

Button styling does not change the element type.

Examples such as “Read more” and “View all” may use text-link or Button styling depending on hierarchy and context, while remaining Links when they navigate.

## Related Documents

- `button.md`
- `../experience-rules/navigation.md`
