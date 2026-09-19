---
id: design-system.component.combo-button
collection: design-system
type: component
title: Combo Button
summary: Combo Button keeps one dominant action directly available and exposes closely related alternative actions from a separate menu trigger.
knowledge_state: verified
document_maturity: draft
design_status: ready-for-dev
design_maturity: handoff-ready
last_reviewed: 2026-09-19
source_figma: https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=22932-134187
source_node: 22932:134187
related:
  - button
  - design-system.component.icon-button
  - design-system.component.menu-button
  - design-system.accessibility.core
---

# Combo Button

## Purpose

Combo Button combines:

1. one directly executable **Primary Action**;
2. one separate **Menu Trigger** exposing closely related alternatives.

Use it when one action is sufficiently dominant/common that hiding it inside a menu would add unnecessary friction, but related alternatives still need compact access.

The dominant action must **not** be repeated inside the menu.

Use Menu Button instead when the available actions are peers and none should remain directly executable while closed.

## Component boundary

Combo Button owns:

- composition of the two connected interactive segments;
- shared outer geometry;
- disclosure/open state of the Menu Trigger;
- replaceable Menu content Slot;
- trigger-to-menu anchoring.

The nested Button owns Primary Action behavior/state/loading.

The nested Icon Button owns Menu Trigger interaction styling, accessible-name requirement, and Focus treatment.

The nested Menu owns menu-item behavior and keyboard navigation.

Combo Button is not a generic Button Group. The two controls have fixed roles: one primary action and one menu disclosure.

## Canonical Figma source

- Figma file: `rROD8ctH9UfPGAMrRrOzHe`
- Component set: `Combo Button / Default`
- Node ID: `22932:134187`
- Component key: `c6f34b8a4294241844d10349881d8264b1c072eb`
- Matrix: `3 Style × 4 Size × 2 Open = 24 variants`
- Primary Action foundation: canonical `Button / Default`
- Menu Trigger foundation: canonical `Icon Button / Default`
- Menu composition: native `Menu content` SLOT

### Figma properties

| Property | Type | Values / behavior |
|---|---|---|
| `Style` | Variant | `Primary / Secondary / Tertiary` |
| `Size` | Variant | `Extra Small / Small / Medium / Large` |
| `Open` | Variant | `False / True` |
| `Menu content` | Native Slot | Replaceable shared Menu content |
| `Primary Action / Button` | Exposed nested instance | Button content/state/loading authoring |
| `Menu Trigger / Icon Button` | Internal nested instance | Fixed Menu Trigger; not exposed for direct authoring |

Default Figma state is `Primary / Medium / Open=False`.

Interaction states are intentionally not multiplied into the outer variant matrix; the two segments are separate interactive targets and own their own states.

## Anatomy

RTL-authored visual anatomy:

```text
[ Menu Trigger ][ Primary Action ]
        End              Start
```

Logical anatomy:

1. **Primary Action** — labeled Button at logical Start.
2. **Menu Trigger** — chevron Icon Button at logical End.
3. **Internal boundary** — a 1px visual boundary at the join; it is not a separate layout node and adds no width.
4. **Menu content** — native Slot anchored outside normal control flow.

### Shared geometry

- overall height follows Size: `28 / 32 / 40 / 48px`;
- **0px layout gap** between the two interactive segments; separation is rendered by a 1px internal boundary;
- outer radius: `6px`;
- touching inner corners: `0px`;
- menu-to-control gap: **2px**;
- open Menu never changes Combo Button width or height.

### Internal boundary treatment

There is **no standalone Divider node** and **no layout gap** between Combo Button segments.

- **Primary:** Combo Button owns a locked 1px absolute `Internal Separator` layer using `line/inverse`; the nested Menu Trigger carries no separator stroke override.
- **Secondary:** Combo Button owns a locked 1px absolute `Internal Separator` layer using `line/emphasis`; the nested Menu Trigger carries no separator stroke override.
- **Tertiary:** both segments keep their canonical outer borders, but only the Menu Trigger owns the shared joining edge; the Primary Action removes its touching left edge so the join renders as a single 1px border rather than a doubled border.
- The boundary contributes **0px** to total Combo width.

Do not implement this as positive spacing or as a standalone/shared Divider component. In Figma, filled styles use the Combo-owned absolute `Internal Separator` visual layer; it is outside layout flow and adds no width. The two hit targets remain visually connected while retaining a clear internal boundary.

## Style contract

JV v1 supports:

- **Primary** — default; strongest operational treatment.
- **Secondary** — medium-emphasis split action when Primary would overstate hierarchy.
- **Tertiary** — control-like/utility treatment in dense operational interfaces.

JV v1 deliberately excludes:

- Brand;
- Ghost;
- all Danger styles.

Brand is reserved for approved product-defining/conversion moments and should not be generalized to a split operational control.

Danger split controls create ambiguity about whether only the default action or all alternatives are destructive; use a clearer dedicated destructive action/menu pattern instead.

Ghost provides insufficient structural definition for a connected two-target control in the current visual model.

### Benchmark note

External systems are not uniform about split/combo emphasis:

- Carbon currently restricts Combo Button to Primary.
- Fluent 2 defines Split Button by behavior: a dominant visible action plus additional actions in a menu.
- Material UI demonstrates Split Button as a ButtonGroup composition and its ButtonGroup supports standard button variants.
- Atlassian's SplitButton history has supported more than one appearance.

JV keeps Primary/Secondary/Tertiary because its canonical Button hierarchy needs lower-emphasis operational split actions in dense products such as ATS, while still keeping the set constrained and semantically explicit.

References:
- https://carbondesignsystem.com/components/menu-buttons/usage/
- https://fluent2.microsoft.design/components/web/react/core/button/usage
- https://mui.com/material-ui/react-button-group/
- https://atlassian.design/components/button/split-button

## Sizes

| Size | Height | Menu Trigger | Current default Menu size |
|---|---:|---:|---|
| Extra Small | 28px | 28×28 | Small — temporary |
| Small | 32px | 32×32 | Small |
| Medium | 40px | 40×40 | Medium |
| Large | 48px | 48×48 | Large |

Primary Action uses the same Button Size.

The current legacy Menu Extra Small remains 24px, so the 28px Combo Button temporarily uses Small Menu content until Menu is migrated.

## Open and interaction states

### Closed

- Menu Slot hidden.
- Menu Trigger in normal Enabled/interaction state.
- Trigger icon is `chevron_down`.
- Primary Action state is independent.

### Open

- Menu Slot visible.
- Menu Trigger maps visually to Icon Button `Active`.
- Trigger icon is `chevron_up`.
- Primary Action keeps its own state.
- Width and height do not change.

`Open` is a Figma authoring/visual state. Runtime may use controlled or uncontrolled disclosure state; exact API naming remains unverified.

## Independent segment behavior

The two segments are separate focus and activation targets.

### Primary Action

- behaves like a normal Button;
- `Enter` / `Space` execute the dominant action;
- action state/loading does not automatically imply that the Menu is open.

### Menu Trigger

- opens/closes the Menu;
- follows Menu Button semantics;
- receives a meaningful accessible name;
- follows the Icon Button Tooltip contract;
- Open state applies only to this segment.

Do not make the entire combined rectangle one hit target.

## Loading

Combo Button has no outer Loading axis.

Loading belongs to the nested Primary Action because that is the segment executing the dominant operation.

When Primary Action is loading:

- preserve total Combo width and height;
- preserve Button loading behavior/focus as defined by Button;
- suppress repeated activation of the Primary Action;
- Menu Trigger may remain available when its alternatives are still valid.

If the in-progress operation makes all alternatives invalid or unsafe, disable the whole Combo at the flow level.

Do not convert the Menu Trigger to a spinner.

## Disabled

Normal whole-control Disabled behavior disables both segments and closes/prevents the menu.

Partial disable is allowed only when semantics are intentional:

- Primary Action unavailable;
- alternative actions in Menu remain valid;
- Menu Trigger remains operable and clearly understandable.

Do not partially disable merely for visual hierarchy.

## Menu Slot contract

`Menu content` is a native Figma Slot.

Rules:

- use shared Menu/Menu Item components;
- do not repeat the dominant Primary Action in the menu;
- keep alternatives closely related to the dominant action;
- keep Menu outside the Combo's layout flow;
- preserve the 2px anchored-surface gap;
- Menu may be wider than the Combo;
- Menu width must not resize the Combo.

Runtime overlay positioning, collision, and portal behavior remain implementation-owned.

## RTL

Use logical Start/End semantics.

In RTL:

- Primary Action is on the right — logical Start.
- Menu Trigger is on the left — logical End.
- the 1px internal boundary remains at the join without becoming a separate Divider element.
- chevron up/down does not horizontally mirror.
- menu positioning uses logical alignment and viewport collision rules.

In LTR the physical order reverses naturally: Primary Action left, Menu Trigger right.

Do not hard-code left/right semantics into the runtime API.

## Accessibility and keyboard contract

Combo Button contains two Button semantics, not one composite tab stop.

### Primary Action

Follow the Button contract:

- native Button semantics where possible;
- visible label is the accessible name;
- `Enter` and `Space` activate;
- visible Focus;
- Loading/Disabled semantics from Button.

### Menu Trigger

Follow Menu Button + Icon Button contracts:

- native Button semantics where possible;
- meaningful accessible name such as “More [action] options” in the current product language;
- Tooltip label on hover/focus;
- `aria-haspopup="menu"`;
- `aria-expanded="true|false"`;
- optional `aria-controls` linking to Menu;
- `Enter` / `Space` open and move focus into Menu;
- optional ArrowDown/ArrowUp opening behavior may follow WAI-ARIA APG;
- `Escape` in Menu closes and returns focus to the Menu Trigger.

Focus order follows DOM order and language direction requirements without creating an artificial roving-focus composite.

If visible menu-item wording omits shared context from the primary action label, accessible labels/descriptions must still communicate the full action meaning.

External references:
- https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/
- https://www.w3.org/WAI/ARIA/apg/patterns/button/

## Runtime boundary

Runtime source and Storybook identity are currently unregistered.

Do not infer exact props from Figma labels.

Conceptually runtime must support:

```text
Combo Button
- style: primary | secondary | tertiary
- size
- primary action label/content
- primary action handler
- primary action loading/disabled state
- menu-trigger accessible name
- menu content
- whole-control disabled policy
- open/close state management
```

Exact Angular structure, prop names, class architecture, popup implementation, and Storybook identifiers remain unverified.

The implementation may compose shared Button, Icon Button, and Menu primitives internally if it can preserve the connected-group radius/internal-boundary/focus behavior.

## QA checklist

Verify:

- exactly 24 variants: `3 Style × 4 Size × 2 Open`;
- each variant contains an exposed canonical Primary Action Button and an internal canonical Menu Trigger Icon Button;
- each variant contains one native Menu Slot;
- heights are 28 / 32 / 40 / 48;
- Open/Closed width is identical for every Style/Size;
- outer corners are 6px and touching corners are 0;
- no standalone Divider node exists;
- the two segments use 0px layout gap;
- Primary renders a Combo-owned locked 1px `line/inverse` absolute separator layer; Secondary renders the same structure with `line/emphasis`;
- Tertiary renders one shared 1px joining border edge with no doubled touching border;
- Open changes only Menu Trigger active treatment/chevron;
- Primary Action remains independently interactive;
- Loading on Primary Action does not move/resize the control;
- whole-control Disabled suppresses both targets;
- Menu is outside normal layout and uses 2px anchor gap;
- Primary Action is not duplicated in Menu;
- both focus targets show visible focus;
- Menu Trigger has accessible name and Tooltip;
- RTL/LTR segment ordering follows logical Start/End;
- Extra Small uses temporary Small Menu until Menu is migrated.

## Known gaps

- current shared Menu Extra Small is still 24px;
- runtime component/API, code repository/package, and Storybook are unregistered;
- exact overlay/collision implementation is unverified;
- exact partial-disabled runtime API is intentionally not specified;
- executable keyboard/screen-reader behavior must be verified when the runtime component exists;
- the exposed nested Primary Action Button still technically allows Style/Size overrides that can diverge from the outer Combo axes; the Menu Trigger is now internal/not exposed, so this authoring risk is limited to the Primary Action until its content/loading properties are promoted individually.

## Related

- `button.md`
- `icon-button.md`
- `menu-button.md`
- `../experience-rules/contextual-guidance.md`
- `../accessibility/core.md`
- `../accessibility/component-accessibility-authoring-contract.md`
- `../accessibility/focus-management.md`
- `../integrations/component-mapping.md`
