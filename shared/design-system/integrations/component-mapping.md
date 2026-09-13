---
id: design-system.reference.component-mapping
collection: design-system
type: reference
title: Design-to-Code Component Mapping
summary: Registry contract for mapping stable Figma component identities to runtime components and Storybook; records current verified mappings and gaps.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: '2026-09-13'
related:
  - design-system.reference.figma
  - design-system.reference.code
  - design-system.reference.storybook
---

# Design-to-Code Component Mapping

This registry prevents AI and humans from guessing runtime component APIs from Figma names.

A mapping is considered verified only when both sides are supported by their owning live sources.

## Mapping fields

For each mapped component record:

```text
Design System component
Figma file key
Figma component key
Figma node ID
Code repository
Code package
Runtime component/API identifier
Figma property → code prop mapping
Storybook stable story/docs identifier
Mapping mechanism
Last verified
Known mismatch/gap
```

`Mapping mechanism` may be Figma Code Connect or another explicit registry. The mechanism is less important than having a stable, reviewable mapping.

## Current mapping registry

### Button

| Field | Current value |
|---|---|
| DS component | Button |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Button / Default` |
| Figma component key | `be5d0d9cd5fdd02f9d7afa1e371c2f2a23acb329` |
| Figma node ID | `1854:1776` |
| Figma properties | `Style / Type / Size / State` + text/icon properties |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-13 |

The Button entry is deliberately incomplete. It proves the design identity is known while making the runtime gap explicit.

## Rules

- Figma property labels do not automatically become code prop names.
- Figma variant options do not prove equivalent runtime enums/states exist.
- A code component with a similar display name is not a verified mapping by name alone.
- Storybook title/path similarity is not enough; link it to the owning code component.
- Record meaningful mismatches rather than forcing one-to-one parity.
- Component mapping should be maintained as integration metadata, not copied into every component guideline.

## Mapping priority

When runtime sources become available, map high-usage foundation components first:

```text
Button
Text Input
Select / Dropdown
Checkbox / Radio
Modal
Menu / Popover / Tooltip
Tabs
Tag
Data Table
```

Then expand based on product usage and migration risk.
