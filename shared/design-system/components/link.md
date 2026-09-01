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

## Variants and Token Roles

### Default

Default is the recognizable chromatic Link treatment.

```text
link/default
link/hover
```

It is the safe default for inline links and other contexts where the link must remain independently recognizable.

Default currently resolves from the shared Blue Primitive family in both JobVision and Cando. It remains a dedicated Link semantic rather than aliasing `fg/accent` directly.

### Subtle

Subtle is the intentional neutral lower-prominence Link treatment.

```text
link/subtle
link/subtle-hover
```

Use it when context already communicates clickability, for example:

- Dense ATS/product UI
- Navigation
- Card metadata
- Breadcrumb-like destinations
- “View all” and similar contextual navigation

Do not use Subtle as the normal inline body-copy Link unless another persistent cue such as underline makes the link recognizable without color.

### Inverse

```text
link/inverse
link/inverse-hover
```

Inverse adapts Link for `surface/inverse`. v4 intentionally has one inverse treatment rather than separate Default/Subtle inverse families.

## Focus

Link does not own a separate focus-color family. Focus composes with the current Link variant:

```text
Default Link → focus/default
Subtle Link  → focus/default
Inverse Link → focus/inverse
```

Focus must remain keyboard-visible and must not be represented only by changing the Link foreground color.

## Removed v3 Roles

```text
link/visited
link/emphasis
link/emphasis-hover
```

Visited is not part of the shared v4 API because no current repeated product pattern requires persistent visited styling. It may be added later if a reviewed use case such as visited search results requires it.

The former Emphasis role is replaced by Subtle with the hierarchy reversed: Default is chromatic; Subtle is the neutral reduced-emphasis variant.

## Button-Styled Links

Button styling does not change the element type.

Examples such as “Read more” and “View all” may use text-Link or Button styling depending on hierarchy and context, while remaining Links when they navigate.

When a Link visually uses a Button treatment, reuse the selected Button visual recipe from `button.md` rather than creating a parallel Link-specific Button color mapping. Link continues to own navigation semantics and accessibility behavior; Button remains the canonical owner of the visual preset/state recipe.

No `link-button/*` Color-token family is approved.

## Related Documents

- `button.md`
- `../experience-rules/navigation.md`
- `../tokens/semantic-tokens.md`
