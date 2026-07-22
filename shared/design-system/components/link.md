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

## Button-Styled Links

Button styling does not change the element type.

Examples such as “Read more” and “View all” may use text-link or Button styling depending on hierarchy and context, while remaining Links when they navigate.

## Related Documents

- `button.md`
- `../experience-rules/navigation.md`
