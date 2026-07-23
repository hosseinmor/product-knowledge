---
id: menu
type: component
scope: shared
status: draft
maturity: usable-for-product-testing
source_figma: https://www.figma.com/design/VA5qSyutH4QkLTfimzdUbe/-DS--Job-Vision?node-id=306-857
source_node: "306:857"
---

# Menu

## Purpose

Menu presents a temporary list of actions or destinations in a layer positioned above the current interface. Overflow Menu is the compact trigger pattern that opens this list.

Use Menu when the user needs a small set of contextual choices without leaving the current screen.

## Anatomy

A Menu consists of:

1. **Trigger** — opens and closes the Menu.
2. **Menu container** — the floating layer that groups the items.
3. **Menu item** — one action or destination.
4. **Optional start or end icon** — supports recognition or communicates a secondary property.
5. **Optional divider** — separates meaningful groups.
6. **Optional danger item** — communicates a destructive action.

The container and items are separate surface roles. The container owns the raised surface and elevation. Items remain transparent at rest and add interaction overlays within that container.

## Container Surface

Use `surface-raised` for the Menu container.

```text
Menu container background → surface-raised
Menu depth                → approved menu elevation or shadow
```

`surface-raised` is a color role, not a shadow token. Both are required when the Menu needs visible depth:

- In Light mode, `surface-raised` may match `surface-default`; elevation creates most of the visual separation.
- In Dark mode, `surface-raised` resolves lighter than `surface-default`, so a floating layer remains distinguishable even when a dark shadow is weak or invisible.

Do not use `canvas` for the Menu container. `canvas` belongs only to the root page or workspace.

Do not use `surface-default` for floating menus, popovers, dropdowns, or similar elevated layers. Reserve `surface-default` for ordinary in-flow containers and structural surfaces.

## Menu Item Color Mapping

### Standard item

| Element or state | Figma variable | Code token |
|---|---|---|
| Rest background | Transparent | Transparent |
| Hover background | `surface/transparent-hover` | `surface-transparent-hover` |
| Active background | `surface/transparent-active` | `surface-transparent-active` |
| Label and actionable icon | `fg/primary` | `fg-primary` |
| Disabled label and icon | `fg/disabled` | `fg-disabled` |
| Focus indicator | `focus/default` | `focus-default` |
| Divider | `line/muted` | `line-muted` |

The item must not receive `surface-raised` or `surface-default` at rest. The Menu container already provides the surface; the item is an interaction layer inside it.

### Danger item

| Element or state | Figma variable | Code token |
|---|---|---|
| Rest background | Transparent | Transparent |
| Rest label and icon | `fg/danger` | `fg-danger` |
| Hover background | `surface/transparent-hover` | `surface-transparent-hover` |
| Active background | `surface/transparent-active` | `surface-transparent-active` |
| Hover and Active label/icon | `fg/danger` | `fg-danger` |

A destructive item should not become a solid danger-filled row on Hover. Filled danger treatment is reserved for a high-emphasis destructive action, not ordinary Menu feedback.

## Focus

Focus uses a non-layout-affecting ring on the full Menu item:

- Normal raised surface → `focus-default`
- Intentionally inverse Menu → `focus-inverse`

Do not use a layout-affecting border for keyboard Focus.

## Elevation

Apply the shared Menu elevation independently from the background color. The exact shadow value remains owned by the elevation-token specification.

Rules:

- Do not encode the shadow inside `surface-raised`.
- Do not use a darker or lighter primitive directly to simulate elevation.
- Do not remove the raised color role merely because the Light mapping currently equals `surface-default`.
- Validate the Menu against both its page background and any parent container in Light and Dark modes.

## Figma Token Migration

The current Figma Menu at node `306:857` uses legacy or incorrect bindings. Update them using this mapping:

| Current binding or treatment | Approved binding or treatment |
|---|---|
| Menu container `canvas` | `surface/raised` |
| Item Rest white/background layer | Transparent |
| `background-or-layer-hover` | `surface/transparent-hover` |
| `background-or-layer-active` | `surface/transparent-active` |
| Item label `fg/fg-secondary` | `fg/primary` |
| Disabled label `fg/fg-disabled` | `fg/disabled` |
| Divider legacy binding | `line/muted` |
| Focus border | Non-layout-affecting ring using `focus/default` |
| Solid filled Danger Hover | Transparent interaction background + `fg/danger` |

Keep the existing Menu shadow until the shared elevation-token document replaces it. Changing the color binding does not remove the need for elevation.

## Interaction

- Opening the trigger displays the Menu above surrounding content.
- Clicking or tapping an enabled item performs its action and normally closes the Menu.
- `Escape` closes the Menu and returns focus to its trigger.
- Clicking outside closes the Menu.
- Disabled items do not perform an action and do not receive Hover or Active treatment.
- Avoid keeping a Menu open after navigation or after an action that changes the relevant context.

## Accessibility

- Use a native button for an action item and a native link for navigation.
- Give the trigger an accessible name and expose its expanded state.
- Move focus into the Menu when it opens when using an application-menu interaction model.
- Support arrow-key movement between enabled items when implementing `role="menu"` and `role="menuitem"`.
- Skip disabled items during arrow-key navigation.
- Keep visible focus on every keyboard-reachable item.
- Ensure the Menu is not clipped by parent overflow and remains perceivable at supported zoom levels.

Do not apply ARIA menu roles to a simple list of links unless the full application-menu keyboard model is implemented. Native link and button semantics are preferable for ordinary website navigation lists.

## Usage

Use Menu for:

- Contextual actions on a row, card, record, or object
- Overflow actions that do not fit in the primary layout
- Compact selection among a small set of destinations or commands

Do not use Menu for:

- Primary actions that should remain visible
- Long forms or complex multi-step tasks
- Large navigation structures that need persistent orientation
- Content that requires comparison while the layer is closed

## Open Decisions

1. Finalize the shared Menu elevation token and map the current Figma shadow to it.
2. Confirm whether Danger items keep `fg-danger` during Hover and Active across every product theme after contrast testing.
3. Confirm the default keyboard model for action menus versus ordinary navigation lists.
4. Update the Figma component bindings after `surface/raised` is added to the Semantic collection.

## Related Documents

- `../tokens/jobvision-color-tokens-v3-surface-model.md`
- `../tokens/color-token-aliases.md`
- `../tokens/semantic-tokens.md`
- `../tokens/usage-rules.md`
