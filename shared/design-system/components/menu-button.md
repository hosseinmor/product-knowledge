---
id: design-system.component.menu-button
collection: design-system
type: component
title: Menu Button
summary: Menu Button opens a replaceable menu of peer actions from one labeled Button trigger without surfacing a separate primary action.
knowledge_state: verified
document_maturity: draft
design_status: ready-for-dev
design_maturity: handoff-ready
last_reviewed: 2026-09-19
source_figma: https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=22930-811
source_node: 22930:811
related:
  - button
  - design-system.component.menu
  - design-system.accessibility.core
  - design-system.accessibility.component-authoring-contract
---

# Menu Button

## Purpose

Menu Button opens a menu of actions from one visible, labeled trigger.

Use it when the available actions are peers and none needs to remain directly executable while the menu is closed.

Use **Combo Button** when one action is dominant enough to stay directly available and the menu contains closely related alternatives.

Menu Button is an action control, not a value-selection control. Use Select or another selection component when the user's choice becomes the current field/control value.

## Component boundary

Menu Button owns:

1. one labeled Button trigger;
2. the disclosure/open state of the attached menu;
3. the chevron that communicates closed/open state;
4. one replaceable native Figma `Menu content` Slot;
5. trigger-to-menu anchoring.

The nested Menu owns menu-item anatomy, menu navigation, item states, grouping, separators, and menu-specific content.

Do not duplicate Menu item behavior inside Menu Button.

## Canonical Figma source

- Figma file: `rROD8ctH9UfPGAMrRrOzHe`
- Component set: `Menu Button / Default`
- Node ID: `22930:811`
- Component key: `166f62776a8c17f3ccdc9f4891892fcd380be68c`
- Matrix: `4 Size × 2 Open = 8 variants`
- Trigger foundation: canonical `Button / Default`
- Menu composition: native `Menu content` SLOT

### Figma properties

| Property | Type | Values / behavior |
|---|---|---|
| `Size` | Variant | `Extra Small / Small / Medium / Large` |
| `Open` | Variant | `False / True` |
| `Menu content` | Native Slot | Replaceable Menu content |
| `Trigger / Button` | Exposed nested instance | Canonical Button content/style/state authoring |

Default Figma state is `Medium / Open=False`.

The nested Button is exposed to keep the outer component matrix small. Do not add Button interaction states to the Menu Button variant matrix.

## Anatomy and geometry

```text
Menu Button
└─ Trigger / Button
   ├─ optional Start icon
   ├─ label
   └─ chevron
└─ Menu content (native Slot; anchored outside trigger layout)
```

Shared rules:

- Trigger radius comes from Button: `6px`.
- Trigger height follows Button Size: `28 / 32 / 40 / 48px`.
- Chevron uses the shared 18px Button icon geometry.
- Closed uses `chevron_down`.
- Open uses `chevron_up`.
- Chevron up/down communicates disclosure state and does not horizontally mirror in RTL.
- Menu content is positioned outside the trigger's Auto Layout flow.
- Opening the Menu must never change trigger width or height.
- Anchored surface gap is **2px**, following the shared contextual-guidance rule.

Runtime positioning may flip/collide based on viewport space. That positioning behavior must not be encoded as extra visual variants on Menu Button.

## Style contract

Default trigger style is **Tertiary**, matching the Design System rule that dropdown/control-like utilities normally use Tertiary.

Approved Menu Button trigger styles for v1:

- `Primary`
- `Tertiary`
- `Ghost`

Do not use:

- `Brand` merely to emphasize a menu;
- `Secondary` as an ad-hoc fourth Menu Button treatment;
- Danger styles for a mixed-action menu.

If every action in a menu is destructive, reconsider the interaction rather than making the menu trigger Danger by default.

The nested Figma Button exposes the full Button API technically; the approved Menu Button style subset above is the design contract and must be enforced in review until a stricter Figma authoring constraint exists.

## Sizes

| Menu Button Size | Trigger height | Current default Menu size |
|---|---:|---|
| Extra Small | 28px | Small — temporary |
| Small | 32px | Small |
| Medium | 40px | Medium |
| Large | 48px | Large |

The current legacy Menu component still uses a 24px Extra Small item size. The new control baseline is 28px. Until Menu is migrated, Extra Small Menu Button temporarily uses the Small Menu size rather than reintroducing a 24px trigger.

This is a dependency gap, not a reason to change the canonical Button size model.

## Open and interaction states

`Open` is a Figma authoring/visual state, not a replacement for runtime popup state management.

### Closed

- Menu Slot hidden.
- Trigger uses its normal interaction state.
- Chevron points down.

### Open

- Menu Slot visible.
- Trigger maps visually to Button `Active`.
- Chevron points up.
- Trigger dimensions remain unchanged.

Hover, Active, Focus, and Disabled are owned by the exposed nested Button rather than duplicated on the outer Menu Button set.

### Disabled

A disabled Menu Button:

- does not open the menu;
- uses Button Disabled semantics/tokens;
- must not expose the Menu as another focus target.

### Loading

Menu Button has **no top-level Loading state**.

Opening a menu is not normally an asynchronous operation. If menu content itself is loading, open the menu normally and represent loading inside `Menu content`.

Do not replace the trigger with a spinner merely because menu data is pending.

## Menu Slot contract

`Menu content` is a native Figma Slot.

The default Slot content is the current shared Menu component. Designers may replace/configure the Menu content without detaching Menu Button.

Rules:

- keep Menu content action-oriented;
- use shared Menu/Menu Item anatomy rather than custom rows;
- keep the Menu anchored to the trigger;
- preserve the 2px trigger-to-surface gap;
- menu width may exceed trigger width;
- do not make the Menu determine trigger width;
- do not place Menu in the trigger's normal layout flow.

## RTL

Use logical Start/End behavior.

In RTL:

- label remains right-to-left;
- optional Start icon is on the logical Start side;
- chevron remains logical End;
- menu alignment/flip follows the contextual-surface positioning system;
- chevron up/down does not mirror horizontally.

Runtime implementation should use logical positioning rather than hard-coded left/right assumptions.

## Accessibility and keyboard contract

Follow the WAI-ARIA Menu Button pattern.

Trigger:

- use native Button semantics where possible;
- expose `aria-haspopup="menu"` or equivalent;
- expose `aria-expanded="true|false"`;
- `aria-controls` may reference the Menu when useful;
- visible label provides the accessible name;
- preserve visible Focus treatment.

Keyboard:

- `Enter` or `Space` opens the menu and moves focus into it;
- `ArrowDown` may open and focus the first item;
- `ArrowUp` may open and focus the last item;
- once open, Menu owns its standard keyboard navigation;
- `Escape` closes the Menu and returns focus to the trigger.

The exact focus-management implementation is runtime-owned, but resulting behavior must satisfy this contract.

External reference:
- https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/

## Benchmark decisions

Current external systems reinforce the component boundary:

- Carbon defines Menu Button for actions of equal importance and separates it from Combo Button.
- Fluent 2 describes Menu Button as a button that toggles a menu without surfacing a primary action.
- WAI-ARIA APG defines Menu Button semantics and keyboard interaction.

Carbon currently permits Primary, Tertiary, and Ghost Menu Button styles. That aligns with the approved JV v1 style subset.

JV intentionally differs from Carbon sizing at Extra Small: JV controls use 28px, not Carbon's 24px.

References:
- https://carbondesignsystem.com/components/menu-buttons/usage/
- https://fluent2.microsoft.design/components/web/react/core/button/usage
- https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/

## Runtime boundary

Runtime source and Storybook identity are currently unregistered.

Therefore this document does not assert:

- exact Angular component name;
- exact input/prop names;
- controlled vs uncontrolled open-state API naming;
- portal implementation;
- collision/flip library;
- animation timing;
- Storybook story ID.

Conceptually runtime must support:

```text
Menu Button
- approved trigger style
- size
- visible label
- optional Start icon
- disabled
- menu content
- open/close state management
```

Do not expose application props for hover/focus pseudo-states.

## QA checklist

Verify:

- set contains exactly 8 variants: `4 Size × 2 Open`;
- each variant contains one exposed canonical Button trigger;
- each variant contains one native `Menu content` Slot;
- Extra Small / Small / Medium / Large trigger heights are 28 / 32 / 40 / 48;
- opening changes chevron and Active treatment without changing trigger dimensions;
- Menu content is outside normal trigger layout;
- trigger-to-menu gap is 2px;
- default trigger style is Tertiary;
- approved style subset is respected;
- Disabled cannot open;
- no top-level Loading state is introduced;
- RTL logical geometry is correct;
- Focus remains visible;
- keyboard behavior follows Menu Button + Menu patterns;
- Extra Small uses temporary Small Menu content until Menu sizing is migrated.

## Known gaps

- current shared Menu Extra Small is still 24px and must be migrated to the 28px control baseline;
- runtime component/API and Storybook are unregistered;
- exact overlay/collision implementation is unverified;
- the exposed nested Button technically allows Style/Size/State overrides that can conflict with the outer Menu Button contract; review must keep nested Size aligned with the outer Size and use only the approved trigger-style subset until the Figma authoring model is tightened.

## Related

- `button.md`
- `combo-button.md`
- `../experience-rules/contextual-guidance.md`
- `../accessibility/core.md`
- `../accessibility/component-accessibility-authoring-contract.md`
- `../accessibility/focus-management.md`
- `../integrations/component-mapping.md`
