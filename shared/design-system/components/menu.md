---
id: design-system.component.menu
collection: design-system
type: component
title: Menu
summary: Menu is a temporary action/command surface composed from Menu Items, optional grouping, separators, shortcuts, checked state, destructive tone, and submenus.
knowledge_state: verified
document_maturity: reviewed
design_status: ready-for-dev
design_maturity: handoff-ready
last_reviewed: 2026-09-21
source_figma: https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=17332-167748
source_node: 17332:167748
related:
  - design-system.component.menu-button
  - design-system.component.combo-button
  - design-system.accessibility.core
  - design-system.accessibility.component-authoring-contract
---

# Menu

## Purpose

Menu is the canonical temporary **action/command surface**.

Use it for contextual commands that appear on demand from a Menu Button, overflow trigger, Combo Button menu trigger, context action, or another approved disclosure pattern.

Menu is intentionally separate from its trigger. The trigger owns disclosure and anchoring; Menu owns the floating surface, item composition, grouping, menu-specific states, and composite keyboard behavior.

## Component boundary

### Menu vs Select

Use **Select** when choosing an option sets the current value of a field or form control.

Use **Menu** when activating an item executes a command, toggles a command state, opens a submenu, or performs contextual navigation within an application-menu interaction model.

Checkable Menu Items are command state, not a replacement for normal form selection.

### Menu vs Dropdown

`Dropdown` is not the canonical semantic name for this action surface. Classify existing Dropdown patterns by behavior:

- value selection → migrate toward Select/listbox behavior;
- contextual actions → migrate toward Menu;
- generic floating content → use the appropriate Popover/contextual-surface pattern.

Do not create a second action-menu implementation under a Dropdown name.

### Menu vs Overflow Menu

Overflow is a **trigger pattern**, not another menu surface.

New overflow actions should use an approved compact trigger, normally Icon Button/Menu Button behavior, and open the same canonical Menu.

The legacy published Overflow Menu component is retained in Figma only for migration compatibility.

### Menu vs Menu Button / Combo Button

Menu Button and Combo Button own the trigger and open/closed state.

Menu owns action-item anatomy, interaction states, grouping, separators, checked state, shortcut presentation, submenu indicators, destructive tone, and menu composite keyboard semantics.

Do not duplicate Menu Item behavior inside trigger components.

### Menu vs navigation

The v1 canonical Menu is action/command-oriented. Do not use it as the default pattern for persistent site/product navigation, large information architecture, or side navigation.

## Canonical Figma source

### Menu

- Figma file: `rROD8ctH9UfPGAMrRrOzHe`
- Component set: `Menu / Default`
- Node ID: `17332:167748`
- Component key: `5b8278235b0cefb99927a2507739afb15ace8f3b`
- Matrix: `4 Size × 2 Layout = 8 variants`
- Native content property: `Content` SLOT

| Property | Type | Values / behavior |
|---|---|---|
| `Size` | Variant | `Extra Small / Small / Medium / Large`; default `Medium` |
| `Layout` | Variant | `Simple / Complex`; default `Simple` |
| `Content` | Native Slot | Compose Menu Item, Menu Group Label, Menu Divider, and approved Menu content |

### Menu Item

- Component set: `Menu Item / Default`
- Node ID: `17332:167436`
- Component key: `77d84f9c0d0377652a87f13ef915c65412655073`
- Matrix: `4 Size × 5 State × 2 Tone = 40 variants`
- Active anatomy is flat: `Trailing + Label + Leading` are direct children of Menu Item. There is no active nested Menu Item Content component.

| Property | Type | Values / behavior |
|---|---|---|
| `Size` | Variant | `Extra Small / Small / Medium / Large` |
| `State` | Variant | `Default / Hover / Active / Focus / Disabled` |
| `Tone` | Variant | `Default / Danger`; Disabled remains a State and visually overrides Tone |
| `Label` | Text | Single-line item label |
| `Leading` | Boolean | 16px logical Start slot; Menu `Layout` controls this automatically in default composition |
| `Checked` | Boolean | Shows the checked indicator |
| `Show start icon` | Boolean | Shows an optional leading/action icon |
| `Start icon` | Instance swap | Shared icon-library source; consumer must explicitly override icon color |
| `Show shortcut` | Boolean | Shows shortcut metadata |
| `Shortcut` | Text | Shortcut text |
| `Submenu` | Boolean | Shows submenu indicator |

### Composition helpers

| Component | Node ID | Component key | Role |
|---|---|---|---|
| `Menu Group Label / Default` | `23038:129820` | `ae3dbe7236e339083cccd60ad047306201c0f6c6` | Optional non-interactive group heading |
| `Menu Divider / Default` | `23038:129822` | `8cb217e111f87fa16785890815d769083ac7e5ec` | Optional non-interactive group separator |

Grouping is Menu composition. Divider/group properties do not belong on every Menu Item.

## Anatomy

Logical item anatomy is implemented directly in Menu Item:

1. **Start / Leading** — optional checked indicator or optional start/action icon.
2. **Label** — one clear primary label.
3. **End / Trailing** — optional shortcut metadata or submenu indicator.

Do not introduce a nested content component for this anatomy.

Authoring constraints:

- `Layout=Simple` is for menus where no item uses a leading icon/check indicator; the leading column collapses completely.
- `Layout=Complex` reserves a 16px logical Start column across every item. Use it when any item in the menu uses a Start icon, checked/selection indicator, or another approved leading visual. Default Figma authoring content shows the shared Start icon; individual items may hide or swap it.
- In a Complex Menu, an item with no visible leading visual keeps the 16px slot empty so labels remain aligned with neighboring items.
- Checked indicator and ordinary Start icon are normally mutually exclusive.
- Shortcut metadata and Submenu indicator are normally mutually exclusive.
- Do not use trailing metadata to repeat a submenu's selected value.
- Group labels and dividers are non-interactive.

## Size and density

Menu Size aligns 1:1 with the trigger/control baseline. The canonical default is `Medium` (40px) for both Menu and Menu Item.

| Size | Menu Item height |
|---|---:|
| Extra Small | 28px |
| Small | 32px |
| Medium | 40px |
| Large | 48px |

Shared item geometry:

- Complex leading column: fixed `16px`; Simple leading column: collapsed;
- Leading and Trailing containers are transparent and must not add their own background fill;
- icon-library components intentionally keep a fixed base color; Menu Item consumers must explicitly override icon color rather than inherit the library default;
- horizontal padding: `12px`;
- item radius: Control radius `6px`;
- label: `Body/Compact/SM` = 14/20 Regular;
- item icons: `16px`.

Menu shell geometry:

- default width: `200px`;
- minimum width: `160px`;
- maximum width: `320px`;
- shell padding: `4px`;
- shell radius: Surface radius `12px`;
- shell fill: `surface/raised`;
- elevation: `Shadow/Floating`.

The 320px maximum is the JV v1 authoring ceiling so Persian labels and trailing metadata have more usable space than the legacy menu.

## Width, wrapping, and long labels

Menu Items are single-line.

- Do not wrap the primary label.
- Long labels use ending ellipsis.
- Increase Menu width only within `160–320px` before relying on truncation.
- Shortcut/submenu metadata keeps its own End space and must not overlap the label.
- Essential meaning must not exist only in the truncated suffix; rewrite the label or provide equivalent accessible context.
- Menu may be wider than its trigger, but must never resize the trigger.

## Supported item types

### Standard action

Default treatment for ordinary commands.

### Danger action

Use `Tone=Danger` for destructive or difficult-to-reverse commands.

Danger is a **content tone**, not an interaction state. Hover and Active continue to use the shared neutral interaction overlays. Prefer destructive items at the end of a group/list where practical.

### Disabled action

Use `State=Disabled`. Disabled visually wins over Default/Danger tone and cannot activate.

### Checked action

Use `Checked=True` for persistent command/toggle state inside a Menu. A menu containing checked/selectable items uses `Layout=Complex` so selected and unselected labels stay aligned.

The check indicator is the persistent state cue. v1 does not add a separate selected-background state axis. Runtime uses `menuitemcheckbox` or `menuitemradio` semantics only when the interaction truly represents checkable/radio command state.

### Submenu trigger

Use `Submenu=True`. The submenu indicator occupies logical End. In the RTL-authored JV source it points left, toward the submenu opening direction.

Submenu placement, collision, hover-open timing, and portal behavior are runtime-owned.

## Grouping and separators

Use `Menu Group Label / Default` when a visible group name improves comprehension. Use `Menu Divider / Default` between meaningful groups, not between every item.

Runtime grouping must preserve semantic grouping. Visible group labels provide the group accessible name; separators are non-focusable and non-interactive.

## Visual states and tokens

### Container

| Role | Token / style |
|---|---|
| Background | `surface/raised` |
| Elevation | `Shadow/Floating` |
| Radius | Surface `12px` |

### Standard Menu Item

| State / element | Treatment |
|---|---|
| Default background | Transparent |
| Hover background | `surface/transparent-hover` |
| Active background | `surface/transparent-active` |
| Label / actionable icon | `fg/primary` — explicit override on icon instances |
| Secondary shortcut metadata | `fg/secondary` |
| Disabled content | `fg/disabled` |
| Focus | shared `Focus/Default` non-layout-affecting ring |
| Divider | `line/muted` |

### Danger Menu Item

| State / element | Treatment |
|---|---|
| Default content | `fg/danger` — explicit override on icon instances |
| Hover background | `surface/transparent-hover` |
| Active background | `surface/transparent-active` |
| Hover / Active content | remains `fg/danger` |

Do not use a solid danger-filled row for normal Menu Hover/Active feedback.

## Focus

Focus uses the shared `Focus/Default` effect and must not change item dimensions. Do not use a layout-affecting border.

Runtime should show the focus treatment for keyboard navigation under the shared `:focus-visible` contract.

## Interaction

- Opening a trigger reveals Menu without changing trigger dimensions.
- Activating an enabled terminal command normally executes it and closes the Menu.
- `Escape` closes and returns focus to the invoking trigger/context.
- Clicking outside closes the Menu.
- `Tab` / `Shift+Tab` close the Menu and move focus out rather than walking through Menu Items.
- A submenu item opens its nested Menu rather than executing a terminal command.

A checkable command may remain open while toggling several related options when the product flow requires it. That choice is runtime/product-owned and must not be inferred from Figma.

## Keyboard and accessibility contract

JV Menu follows the WAI-ARIA application-menu interaction model.

### Roles

- container: `role="menu"`;
- ordinary item: `role="menuitem"`;
- checkable item: `role="menuitemcheckbox"` or `role="menuitemradio"`;
- checked state: `aria-checked`;
- disabled item: `aria-disabled="true"`;
- submenu trigger: expose submenu relationship and expanded state;
- divider: separator semantics and not focusable;
- groups: appropriate group semantics and accessible group naming.

### Opening and focus

When opened from a Menu Button, overflow trigger, or Combo Button, move focus into Menu and normally focus the first Menu Item.

### Inside Menu

- `ArrowDown` / `ArrowUp` move among Menu Items.
- `Home` / `End` move to first / last Menu Item.
- Printable-character typeahead moves to the next matching item.
- `Enter` activates a terminal item; on a submenu trigger it opens the submenu.
- `Space` activates/toggles according to item role.
- `Escape` closes the current Menu/submenu and returns focus to its invoker.
- `Tab` / `Shift+Tab` close the Menu and move focus out.
- Disabled Menu Items remain discoverable in arrow-key navigation but cannot activate, following WAI-ARIA APG Menu convention.
- Group labels and separators are skipped because they are not Menu Items.

Submenu Left/Right keyboard behavior follows the standard Menu pattern and active document direction. Runtime must mirror directional behavior under RTL rather than hard-code LTR assumptions.

The exact focus implementation—roving `tabindex` versus `aria-activedescendant`—is runtime-owned. The resulting behavior above is the contract.

## RTL

Figma is authored for RTL.

- Start = right;
- End = left;
- checked/start icon = logical Start;
- shortcut/submenu indicator = logical End;
- label is right-aligned;
- submenu chevron points toward submenu opening direction.

Runtime uses logical positioning/document direction. In LTR, Start/End and submenu direction mirror naturally.

## Placement and collision boundary

Menu owns visual surface, content, width limits, and menu semantics.

The trigger/overlay runtime owns anchor reference, preferred placement, collision detection, flip/shift behavior, viewport padding, portal/layer strategy, and dismissal wiring.

When attached to Menu Button or Combo Button, preserve the shared **2px** trigger-to-surface gap. Do not create placement variants in Menu.

## Benchmarks used

The v1 contract was reviewed against WAI-ARIA APG Menu/Menu Button, Primer ActionMenu/ActionList, Carbon Menu, and Radix Dropdown Menu.

Primer treats leading visuals as optional and recommends them only when they improve scanability. Carbon similarly distinguishes ordinary options from selectable options and reserves leading space where selection alignment requires it. JV captures that authoring distinction at the Menu level with `Layout=Simple / Complex`.

JV deliberately differs from Carbon Extra Small sizing: JV uses the shared 28px control baseline rather than Carbon's 24px menu option.

References:

- https://www.w3.org/WAI/ARIA/apg/patterns/menubar/
- https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/
- https://primer.style/product/components/action-menu/
- https://primer.style/product/components/action-list/
- https://carbondesignsystem.com/components/menu/style/
- https://www.radix-ui.com/primitives/docs/components/dropdown-menu

## Runtime boundary

Runtime component source, package/API, Storybook identity, and Code Connect mapping are currently unregistered.

Therefore this document does **not** assert exact Angular component/tag name, prop/event names, DOM nesting, focus-management technique, portal library, collision engine, submenu timing, animation timing, or Storybook story ID.

Implementation must satisfy this design/accessibility contract, but exact runtime API details remain unverified until an owning source is registered.

## Legacy / migration

Figma retains three published legacy assets only so old instances remain resolvable:

- `Legacy / Menu Item Content` — key `3c4735684b5eb1146dab273119bcc59dbceee8aa`; deprecated after flattening Menu Item;
- `Legacy / Keyboard shortcut` — key `e2113c87df4d0d02d41477f4c706fb6b30a6437a`;
- `Legacy / Overflow menu` — key `89d20a2413e0b877ce2d9c358ce75bb903155bfb`.

Do not use them in new designs.

The old Menu `Function=Simple/Complex` semantics are retired. The current `Layout=Simple/Complex` axis is intentionally narrower: it controls only whether the 16px leading column is collapsed or reserved. Legacy item Divider/Spacer/Indented booleans, 24px Extra Small size, and Danger-as-state are also retired.

## QA checklist

Verify:

- Menu has exactly `4 Size × 2 Layout = 8` variants and one native `Content` Slot, with `Medium + Simple` as the default variant;
- Menu Item has exactly `4 Size × 5 State × 2 Tone = 40` variants, with `Medium + Default + Default Tone` as the default variant;
- Menu Item anatomy is flat (`Trailing + Label + Leading`) with no active nested Menu Item Content component;
- heights are `28 / 32 / 40 / 48`; 
- Menu width is within `160–320px`; 
- shell uses `surface/raised + Shadow/Floating + 12px radius`; 
- item radius is 6px and horizontal padding 12px;
- long labels are single-line with ending ellipsis;
- Hover / Active / Focus / Disabled use semantic treatments;
- Danger is Tone, not State;
- Simple collapses the leading column completely; Complex reserves exactly 16px across items and default Figma content shows a Start icon;
- any menu containing a Start icon or checked/selection indicator uses Complex layout, including blank reserved slots on neighboring items;
- Leading and Trailing containers remain transparent in every Tone;
- every Menu Item icon has an explicit semantic color override: Default → `fg/primary`, Danger → `fg/danger`, Disabled → `fg/disabled`; after any icon swap, verify the override is still present;
- Checked / Start icon and Shortcut / Submenu authoring constraints are respected;
- groups/dividers are composed at Menu level;
- RTL Start/End anatomy and submenu direction are correct;
- real instances can replace Menu Slot content without detaching;
- Menu Button and Combo Button sizes map 1:1 to Menu size, including Extra Small;
- disabled items cannot activate;
- keyboard behavior follows the Menu composite contract;
- runtime API facts remain unverified where no owning source exists.

## Related documents

- `menu-button.md`
- `combo-button.md`
- `select.md`
- `../experience-rules/contextual-guidance.md`
- `../accessibility/core.md`
- `../accessibility/component-accessibility-authoring-contract.md`
- `../accessibility/focus-management.md`
- `../integrations/component-mapping.md`
