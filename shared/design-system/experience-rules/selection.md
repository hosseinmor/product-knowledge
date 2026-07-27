---
id: design-system.experience-rule.selection
collection: design-system
type: experience-rule
title: Selection
summary: Selected state is not a normal action Button state.
knowledge_state: unverified
document_maturity: draft
related: []
---

# Selection

## Button-Like Selection Controls

Selected state is not a normal action Button state.

Use a separate component such as:

- Toggle Button
- Segmented Control
- Filter Button
- Applied Filter Chip
- Tab
- Selectable Card

## Selected Token Roles

```text
Low-emphasis selected
→ surface-selected-muted

Strong selected or on/checked
→ surface-selected-emphasis + fg-on-color

Selected on inverse
→ surface-selected-inverse + fg-on-inverse

Selected and disabled
→ surface-selected-disabled + fg-on-color-disabled
```

Selected and brand roles must remain separate.

Do not use `surface-brand-emphasis` to represent selected state, even when a product theme makes the two visually similar.

## Related Documents

- `../components/toggle-button.md`
- `../components/button.md`
