---
id: button
collection: design-system
type: component
title: Button
summary: Buttons trigger actions.
knowledge_state: unverified
document_maturity: draft
related: []
design_status: draft
design_maturity: usable-for-product-testing
source_guideline: button-guidelines-v0.6.md
---

# Button

## Purpose

Buttons trigger actions.

The Button model has two levels:

1. A small set of named presets that designers select directly in Figma.
2. An internal `tone × appearance` model used to keep the component and implementation structured.

Designers should not need to solve the full internal matrix for each use case.

## Documentation Ownership

This document is the canonical source for:

- Button presets
- Internal Button properties
- Variant selection
- Preset-specific usage rules
- Button state mappings
- Button semantic-token mappings
- Unsupported Button combinations

Detailed cross-component guidance belongs in other documents:

| Topic | Canonical document |
|---|---|
| Hierarchy and Button combinations | `../experience-rules/action-hierarchy.md` |
| Multi-step navigation actions | `../patterns/multi-step-flow.md` |
| Modal action groups | `../patterns/confirmation.md` |
| Destructive flows | `../patterns/destructive-actions.md` |
| Link versus Button semantics | `link.md` and `../experience-rules/navigation.md` |
| Button-like selection controls | `toggle-button.md` and `../experience-rules/selection.md` |
| Buttons over images or video | `../patterns/on-media-controls.md` |
| Product brand differences | `../product-variations/brand-variants.md` |
| General component-token policy | `../tokens/component-tokens.md` |

## Figma Presets

These are the primary Button options exposed to designers.

| Preset | Visual treatment | Role |
|---|---|---|
| Accent | Product `surface-brand-emphasis`, filled | Defined product conversions and special actions |
| Primary | Neutral `surface-emphasis`, filled | Most important operational action in a context |
| Secondary | Neutral `surface-control`, filled | Supporting action with medium emphasis |
| Tertiary | Neutral outline | General, independent, or control-like action |
| Ghost | No persistent fill or border | Low-emphasis action, exit, back, or third action |
| Danger Filled | Red filled | Final confirmation of a destructive action |
| Danger Outline | Red outline | Independent destructive action with medium emphasis |
| Danger Ghost | Red foreground | Low-emphasis destructive entry point or inline remove action |

Not every theoretical `tone × appearance` combination is exposed as a preset.

In the current model, Accent is available only with the strongest appearance.

## Naming Model

`Accent` is the UI preset name.

`brand` is the semantic color role.

`emphasis` is the background prominence.

Therefore:

```text
Accent
→ surface-brand-emphasis
→ fg-on-brand
```

Accent may look different in Jobvision and Cando, while its usage rule remains shared.

## Internal Architecture

### Tone

| Tone | Meaning |
|---|---|
| `accent` | Defined product conversions and special actions, using the active product brand |
| `neutral` | Everyday operational actions |
| `danger` | Destructive actions and potential data loss |

### Appearance

| Appearance | Visual presence |
|---|---|
| `strong` | Filled and high emphasis |
| `subtle` | Neutral filled treatment with lower emphasis |
| `outline` | Border with no persistent fill |
| `ghost` | Transparent treatment with the least visual presence |

### Preset Mapping

| Preset | Tone | Appearance |
|---|---|---|
| Accent | `accent` | `strong` |
| Primary | `neutral` | `strong` |
| Secondary | `neutral` | `subtle` |
| Tertiary | `neutral` | `outline` |
| Ghost | `neutral` | `ghost` |
| Danger Filled | `danger` | `strong` |
| Danger Outline | `danger` | `outline` |
| Danger Ghost | `danger` | `ghost` |

`tone` and `appearance` are internal Button properties. They are not Core token names.

For example:

```text
tone=accent
→ surface-brand-emphasis

appearance=subtle
→ surface-control
```

The current color model does not use a separate `fill` token family. Background prominence is expressed through roles such as `control` and `emphasis`.

## Decision Path

Use this sequence.

### 1. Is the action destructive?

Use the Danger family when the action deletes data, removes access, causes irreversible cancellation, or has another serious consequence.

- Final destructive confirmation → Danger Filled
- Destructive entry point or independent destructive action → Danger Outline or Danger Ghost

A negative verb alone does not make an action destructive. For example, a reversible rejection action is not automatically Danger.

### 2. Is the action a defined product conversion?

Use Accent only when the action belongs to the approved conversion list for the product.

Examples currently allowed by the source guideline:

- Submit a resume
- Sign up
- Create a job at the product's primary entry point
- Purchase or upgrade a package
- Request a demo
- Start a defined key product journey

Being the most important action on a page does not make an action Accent. “Save changes” is usually Primary.

### 3. Is it the most important operational action in this context?

Use Primary.

Examples:

- Save changes
- Submit request
- Confirm
- Continue
- Send for approval
- Create an item when creation is the main goal of the current context

### 4. Is it a supporting action that needs medium emphasis?

Use Secondary.

### 5. Is it independent, general, or control-like?

Use Tertiary.

Examples include filters, sorting, dropdown triggers, toolbar actions, and general utilities.

### 6. Is it low priority, an exit, a back action, or the third action?

Use Ghost.

## Preset Rules

## Accent

### Use for

- Predefined product conversions
- Primary landing-page or campaign CTA
- Moments where the user enters the core value of the product

### Do not use for

- Editing, filtering, export, or settings
- Every create or add action
- Repeated actions inside cards and tables
- Everyday save and confirmation actions

### Rules

- Only one Accent is allowed in an action group.
- The same conversion may be repeated in independent sections of a long page.
- Accent and Primary must not compete as two equal CTAs in the same action group.
- For a secondary landing or hero CTA, use Tertiary for an independent alternative and Ghost for supporting information or a lower-emphasis route.
- A brand-colored Button is not automatically Accent.

## Primary

### Use for

- The most important operational action in a page, dialog, form, or step
- Confirming or submitting the main decision

### Rules

- A decision region usually has one Primary.
- Use Primary cautiously inside repeated tables and cards.
- “Continue” in intermediate steps of a multi-step flow is usually Primary.

## Secondary

### Use for

- A supporting action that must remain visible without becoming the main priority
- A medium-emphasis action in an empty state, card, or editorial context

Examples:

- Use template
- View result
- Preview
- Add item in an empty state

### Rules

- Secondary does not mean “the second Button.”
- Use Ghost for Cancel, Back, or Later.
- Use Tertiary for control-like actions and dropdown triggers.

## Tertiary

### Use for

- Filters, sorting, and dropdown triggers
- Export, settings, editing, and general utilities
- An independent action below the main CTA
- Toolbar and header controls

### Rules

- Tertiary is the default outline action in ATS and product panels.
- When a page contains too many Tertiary Buttons, move lower-priority actions to Ghost.
- Do not use Tertiary for the main submit or confirmation action.

## Ghost

### Use for

- Cancel, Back, and Not now
- More information or supporting navigation
- The third action and later actions
- Low-emphasis toolbar actions

### Rules

- Ghost remains a complete Button with hit area, hover, focus, pressed, and disabled states.
- Its default text and icon use `fg-primary`.
- Do not create another lower-emphasis Ghost variant. Reconsider placement, copy, or whether the control should be a Link.
- Do not use Ghost where the action is likely to be missed.

## Danger

### Danger Filled

Use only for the final confirmation of a destructive action, usually in a confirmation dialog.

### Danger Outline

Use for a visible independent destructive action that is not yet the final confirmation.

### Danger Ghost

Use for a low-emphasis destructive entry point, inline action, or menu item.

### Rules

- Danger Filled is not the default Danger treatment.
- A low-risk and undoable action may use a neutral treatment.
- Rare destructive actions should generally be placed in an overflow menu.

## Surface Model

Surface context does not determine the Button preset by itself.

Relevant background roles:

| Token | Role |
|---|---|
| `canvas` | Root page or workspace background; not used by Button itself |
| `surface-default` | Normal container, card, or panel background |
| `surface-muted` | Passive, calm, non-interactive grouping region |
| `surface-control` | Visible neutral interactive background; source for Secondary |
| `surface-emphasis` | High-emphasis neutral background; source for Primary |
| `surface-transparent-hover` / `surface-transparent-active` | States for Tertiary and Ghost |

`surface-muted` is passive and intentionally has no interaction states. It must not be used as the Secondary Button background.

`surface-control` is for controls with a visible rest background, including Secondary Button and other filled neutral controls.

Context convention:

| Context | More common choice |
|---|---|
| Dense, tool-oriented UI such as ATS | Tertiary for independent neutral actions |
| Editorial and consumer pages | Secondary for medium-emphasis actions |

The nature of the control takes priority over the product context:

- Dropdown, filter, toolbar → Tertiary
- Medium-emphasis standalone action → Secondary
- Exit or lightweight action → Ghost

## States and Behavior

### Loading

- After submit, the triggered Button enters Loading.
- The Button width must not change.
- Repeated submission is blocked until the request finishes.
- In multi-step flows, Back and competing actions are disabled while submission is in progress.

### Disabled

- Disabled does not replace validation or error guidance.
- The reason must be understandable from context or helper text.
- When the user can enable the Button through a simple action, place guidance near the relevant input or section.
- Disabled has no hover or active state.
- Danger styling becomes neutral when disabled because the disabled state takes priority over destructive tone.

### Focus

- Focus ring is independent from the Button variant color.
- Use `focus-default` on normal backgrounds.
- Use `focus-inverse` on inverse backgrounds.
- Focus must remain visible on every supported background.
- Cando brand yellow must not serve as the only focus indicator.

### Icon-only

Icon-only controls are not standard Buttons. Use Icon Button.

Every Icon Button without visible text needs an accessible name. Tooltip does not replace an accessible name.

## Semantic Token Mapping

### Filled and Subtle

| Preset | Background | Hover | Active | Foreground |
|---|---|---|---|---|
| Accent | `surface-brand-emphasis` | `surface-brand-emphasis-hover` | `surface-brand-emphasis-active` | `fg-on-brand` |
| Primary | `surface-emphasis` | `surface-emphasis-hover` | `surface-emphasis-active` | `fg-on-color` |
| Secondary | `surface-control` | `surface-control-hover` | `surface-control-active` | `fg-primary` |
| Danger Filled | `surface-danger-emphasis` | `surface-danger-emphasis-hover` | `surface-danger-emphasis-active` | `fg-on-color` |

### Outline

| Preset | Background | Hover | Active | Foreground | Line |
|---|---|---|---|---|---|
| Tertiary | transparent | `surface-transparent-hover` | `surface-transparent-active` | `fg-primary` | `line-default` |
| Danger Outline | transparent | `surface-transparent-hover` | `surface-transparent-active` | `fg-danger` | `line-danger` |

### Ghost

| Preset | Background | Hover | Active | Foreground |
|---|---|---|---|---|
| Ghost | transparent | `surface-transparent-hover` | `surface-transparent-active` | `fg-primary` |
| Danger Ghost | transparent | `surface-transparent-hover` | `surface-transparent-active` | `fg-danger` |

### Disabled

| Appearance | Background | Foreground | Line |
|---|---|---|---|
| Accent / Primary / Secondary / Danger Filled | `surface-disabled` | `fg-disabled` | — |
| Tertiary / Danger Outline | transparent | `fg-disabled` | `line-disabled` |
| Ghost / Danger Ghost | transparent | `fg-disabled` | — |

### Focus

- Normal background → `focus-default`
- Inverse background → `focus-inverse`

### Mapping Rules

- Accent is a UI name, not a token name.
- Primary uses neutral emphasis.
- Secondary uses `surface-control`, not `surface-muted`.
- Tertiary and Ghost are transparent at rest.
- Danger Filled uses `surface-danger-emphasis`, not an Error token.
- Error represents validation or system conditions. Danger represents destructive actions.
- `fg-on-brand` must be independently overridable in Cando to preserve contrast on the yellow brand background.

## Link Versus Button

Semantics are separate from appearance:

```text
Changes state or performs an operation
→ button

Navigates to another destination
→ link
```

A Link may look like a Button while retaining Link semantics and accessibility behavior.

Detailed guidance belongs in `link.md` and `../experience-rules/navigation.md`.

## Controls That Are Not Button Presets

The following are separate components or patterns:

- Tab
- Segmented Control
- Filter Button
- Applied Filter Chip
- Toggle Button
- Selected state
- Link
- Selectable Card

Selected styling comes from selected tokens, not Accent or other Button presets.

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

Selected and brand roles must remain separate even when they look similar in a product theme.

## Intentionally Unsupported Presets

The current model intentionally excludes:

- Accent Outline
- Accent Ghost as a general preset
- Secondary Ghost as a separate preset
- Positive or Success Button
- Ghost over media
- The full unrestricted `tone × appearance` matrix

A new preset requires a repeated, generalizable use case validated in real product flows.

## Product Variations

- Accent uses the active product's brand mapping.
- Accent meaning remains the same across products.
- `fg-on-brand` may be overridden independently from the brand background.
- The official Accent conversion list must be documented per product.

See `../product-variations/brand-variants.md`.

## Open Questions

1. Complete the official Accent use-case list for each product.
2. Test Secondary in ATS, especially in empty states and independent actions.
3. Review the rules after at least three real flows:
   - Create or edit job
   - Recruitment request
   - Resume submission or package purchase
4. Resolve the remaining On-media control and focus questions in the dedicated pattern.
5. Decide whether modal Cancel is always Ghost or whether some products consistently use Tertiary.

## Not Defined in v0.6

The source guideline does not yet define:

- Exact Button anatomy
- Size scale
- Dimensions and spacing
- Minimum target size
- Icon size and gap
- Radius mapping
- Exact code API
- Figma property names beyond the internal `tone × appearance` model

These sections must be added through a separate reviewed decision rather than inferred.

## Quick Reference

| Need | Preset |
|---|---|
| Defined brand conversion | Accent |
| Main operational action | Primary |
| Supporting medium-emphasis action | Secondary |
| General, filter, dropdown, or toolbar action | Tertiary |
| Back, Cancel, Later, or third action | Ghost |
| Final destructive confirmation | Danger Filled |
| Independent destructive action | Danger Outline |
| Low-emphasis or inline destructive action | Danger Ghost |

The most important action is not automatically Accent. Accent must come from the approved product conversion list.

In every action group, only one action should have the strongest visual emphasis.

## Related Documents

- `../experience-rules/action-hierarchy.md`
- `../experience-rules/navigation.md`
- `../experience-rules/selection.md`
- `../patterns/multi-step-flow.md`
- `../patterns/confirmation.md`
- `../patterns/destructive-actions.md`
- `../patterns/on-media-controls.md`
- `link.md`
- `icon-button.md`
- `toggle-button.md`
- `../tokens/component-tokens.md`
- `../product-variations/brand-variants.md`
