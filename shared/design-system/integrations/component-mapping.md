---
id: design-system.reference.component-mapping
collection: design-system
type: reference
title: Design-to-Code Component Mapping
summary: Registry contract for mapping stable Figma component identities to runtime components and Storybook; records current verified mappings and gaps.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: '2026-09-19'
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
| Figma variant properties | `Style / Size / State / Loading` |
| Figma content properties | `Button text / Start Icon / End Icon / Swap Start Icon / Swap End Icon` |
| Figma styles | `Brand / Primary / Secondary / Tertiary / Ghost / Danger Primary / Danger Tertiary / Danger Ghost` |
| Figma sizes | `Extra Small 28 / Small 32 / Medium 40 / Large 48` |
| Figma states | `Enabled / Hover / Active / Focus / Disabled` |
| Loading representation | `False / True`, separate from interaction State; uses shared `Loading / Small / Active` component |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer code prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-17 |

The Button design identity and current Figma property model are verified. Runtime API, Storybook identity, and Figma-to-code prop mapping remain deliberately unverified because the owning runtime Design System repository/package and Storybook source are not yet registered. Track that source gap through the integration contract rather than guessing from Figma.


### Icon Button

| Field | Current value |
|---|---|
| DS component | Icon Button |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Icon Button / Default` |
| Figma component key | `f9b7af4bd9afaf768ae955c51ccddd29833c5ca7` |
| Figma node ID | `22685:1410` |
| Figma variant properties | `Style / Size / State` |
| Figma content properties | `Icon` instance swap |
| Figma styles | `Brand / Primary / Secondary / Tertiary / Ghost / Danger Tertiary / Danger Ghost` |
| Figma sizes | `Extra Small 28 / Small 32 / Medium 40 / Large 48` |
| Figma states | `Enabled / Hover / Active / Focus / Disabled` |
| Icon size | Fixed `18px` |
| Tooltip contract | Required for operable Icon Buttons on hover/focus; Tooltip does not replace the accessible name |
| Loading / Selected | Not part of the current Icon Button contract |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer code prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-18 |

The Icon Button design identity and current Figma property model are verified. Its accessible-name, Tooltip, sizing, destructive-action, migration, and state boundaries are defined in `../components/icon-button.md`. Runtime API, Storybook identity, Tooltip composition strategy, and Figma-to-code prop mapping remain deliberately unverified until the owning runtime Design System source is registered.


### Accordion

| Field | Current value |
|---|---|
| DS component | Accordion |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component | `Accordion` |
| Figma component key | `649891c2bfc1413f60f04011bc71a05576d12738` |
| Figma node ID | `22821:129502` |
| Figma content properties | `Items` native SLOT |
| Items Slot | 1+ children, zero gap, preferred/allowed content = `Accordion Item` |
| Default authoring content | 3 Accordion Item instances; count is not fixed |
| Group behavior | Multiple-open default; Single-open explicit runtime option; both allow all-collapsed |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

### Accordion Item

| Field | Current value |
|---|---|
| DS component | Accordion Item / standalone Disclosure |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Accordion Item` |
| Figma component key | `2728144865f9616dd66228719b4fb71936e3062a` |
| Figma node ID | `22794:548` |
| Figma variant properties | `Size / State / Expanded / Indicator position` |
| Variant count | 48 |
| Figma content properties | `Title / Content` |
| Content | Native Figma SLOT with editable default Body text; accepts arbitrary frames/text/component instances |
| Figma sizes | `Large 48 / Medium 40 / Small 32` minimum Trigger heights |
| Figma states | `Enabled / Hover / Focus / Disabled`; Active is runtime-only |
| Indicator position | `Start / End`; in RTL Start=right and End=left |
| Composition | Same Item may be used alone as Disclosure or inside Accordion Items Slot |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

Accordion and Accordion Item design identities, native Slot composition, visual state model, RTL geometry, and current Figma property models are verified. Runtime API, exact DOM/animation implementation, Storybook identity, and Figma-to-code property mapping remain deliberately unverified until the owning runtime Design System source is registered.

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
