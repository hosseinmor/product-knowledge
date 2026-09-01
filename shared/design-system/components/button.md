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
- Button Semantic-token mappings
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

| Preset | Visual treatment | Role |
|---|---|---|
| Brand | Product `surface/brand`, filled | Defined product conversions and product-defining entry points |
| Primary | Neutral `surface/neutral-emphasis`, filled | Most important operational action in a context |
| Secondary | Neutral `surface/neutral-muted`, filled | Supporting action with medium emphasis |
| Tertiary | Neutral outline | General, independent, or control-like action |
| Ghost | No persistent fill or border | Low-emphasis action, exit, back, or third action |
| Danger Filled | Red filled | Final confirmation of a destructive action |
| Danger Outline | Red outline | Independent destructive action with medium emphasis |
| Danger Ghost | Red foreground | Low-emphasis destructive entry point or inline remove action |

Not every theoretical `tone × appearance` combination is exposed as a preset.

In v4, Brand is approved only with the strongest appearance. Do not generate Brand Subtle, Brand Outline, or Brand Ghost merely to complete the matrix.

## Naming Model

`Brand` is the UI preset name and the internal tone name for defined product conversions/product-defining moments.

`Accent` is no longer a Button tone or preset. In v4, Accent is a separate Semantic color concept for general chromatic interaction and affordance.

```text
Brand Button
→ surface/brand
→ fg/on-brand
```

Brand may look different in JobVision and Cando while its usage rule remains shared.

## Internal Architecture

### Tone

| Tone | Meaning |
|---|---|
| `brand` | Defined product conversions and product-defining moments using the active product brand |
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
| Brand | `brand` | `strong` |
| Primary | `neutral` | `strong` |
| Secondary | `neutral` | `subtle` |
| Tertiary | `neutral` | `outline` |
| Ghost | `neutral` | `ghost` |
| Danger Filled | `danger` | `strong` |
| Danger Outline | `danger` | `outline` |
| Danger Ghost | `danger` | `ghost` |

`tone` and `appearance` are internal component properties, not Core token names.

## Decision Path

### 1. Is the action destructive?

Use the Danger family when the action deletes data, removes access, causes irreversible cancellation, or has another serious consequence.

- Final destructive confirmation → Danger Filled
- Destructive entry point or independent destructive action → Danger Outline or Danger Ghost

A negative verb alone does not make an action destructive. A reversible rejection action is not automatically Danger.

### 2. Is the action a defined Brand conversion or product-defining entry point?

Use Brand only when the action belongs to the approved conversion/product-moment list.

Examples that may qualify:

- Submit a resume
- Sign up
- Create a job at the product's primary entry point
- Purchase or upgrade a package
- Request a demo
- Start a defined key product journey

Being the most important action on a page does not make an action Brand. “Save changes” is usually Primary.

The same verb may receive different treatment by context. For example, “Create job” at a major entry/empty-state moment may be Brand, while a frequently used “Create job” toolbar action in ATS is operational and should normally be Neutral.

### 3. Is it the most important operational action in this context?

Use Primary.

Examples:

- Save changes
- Submit request
- Confirm
- Continue
- Send for approval
- Create an item when creation is the main operational goal of the current context

### 4. Is it a supporting action that needs medium emphasis?

Use Secondary.

### 5. Is it independent, general, or control-like?

Use Tertiary.

Examples include filters, sorting, dropdown triggers, toolbar actions, export, settings, and general utilities.

### 6. Is it low priority, an exit, a back action, or the third action?

Use Ghost.

## Preset Rules

### Brand

Use for:

- Approved product conversions
- Primary landing-page or campaign CTA when it is a defined product moment
- Entry points into the core value of the product

Do not use for:

- Editing, filtering, export, or settings
- Every create/add action
- Repeated actions inside cards and tables
- Everyday save and confirmation actions
- Generic emphasis

Rules:

- Only one Brand Button is allowed in an action group.
- The same conversion may be repeated in independent sections of a long page.
- Brand and Primary must not compete as equal CTAs in the same action group.
- A brand-colored Button is not justified merely because the product has a Brand color.
- Low frequency of Brand Buttons in dense operational products such as Cando ATS is expected.

### Primary

Use for:

- The most important operational action in a page, dialog, form, or step
- Confirming or submitting the main operational decision

Rules:

- A decision region usually has one Primary.
- Use Primary cautiously inside repeated tables and cards.
- “Continue” in intermediate steps of a multi-step flow is usually Primary.

### Secondary

Use for:

- A supporting action that must remain visible without becoming the main priority
- A medium-emphasis action in an empty state, card, or editorial context

Examples:

- Use template
- View result
- Preview
- Add item in an empty state

Rules:

- Secondary does not mean “the second Button.”
- Use Ghost for Cancel, Back, or Later.
- Use Tertiary for control-like actions and dropdown triggers.

### Tertiary

Use for:

- Filters, sorting, and dropdown triggers
- Export, settings, editing, and general utilities
- An independent action below the main CTA
- Toolbar and header controls

Rules:

- Tertiary is the default outline action in ATS and product panels.
- When a page contains too many Tertiary Buttons, move lower-priority actions to Ghost.
- Do not use Tertiary for the main submit or confirmation action.

### Ghost

Use for:

- Cancel, Back, and Not now
- More information or supporting navigation-like actions that still perform an operation
- The third action and later actions
- Low-emphasis toolbar actions

Rules:

- Ghost remains a complete Button with hit area, hover, focus, active, and disabled states.
- Its default text and icon use `fg/primary`.
- Do not create another lower-emphasis Ghost variant. Reconsider placement, copy, or whether the control should be a Link.

### Danger

Danger Filled is reserved for the final confirmation of a destructive action, usually in a confirmation dialog.

Danger Outline is for a visible independent destructive action that is not yet the final confirmation.

Danger Ghost is for a low-emphasis destructive entry point, inline action, or menu item.

Rules:

- Danger Filled is not the default Danger treatment.
- A low-risk and undoable action may use a neutral treatment.
- Rare destructive actions should generally be placed in an overflow menu.

## Surface Model

Relevant v4 surface roles:

| Token | Role |
|---|---|
| `surface/default` | Normal page/container/card/panel surface |
| `surface/muted` | Passive, non-interactive grouping surface |
| `surface/neutral-muted` | Visible neutral interactive background; source for Secondary |
| `surface/neutral-emphasis` | High-emphasis neutral interactive background; source for Primary |
| `surface/brand` | Defined Brand conversion/product moment |
| `surface/transparent-hover` / `surface/transparent-active` | States for Tertiary and Ghost |

`surface/muted` is passive and must not be used as the Secondary Button background.

Context convention:

| Context | More common choice |
|---|---|
| Dense, tool-oriented UI such as ATS | Tertiary for independent neutral actions |
| Editorial and consumer pages | Secondary for medium-emphasis standalone actions |

The nature of the control takes priority over product context:

- Dropdown, filter, toolbar → Tertiary
- Medium-emphasis standalone action → Secondary
- Exit or lightweight operation → Ghost

## States and Behavior

### Loading

- After submit, the triggered Button enters Loading.
- The Button width must not change.
- Repeated submission is blocked until the request finishes.
- In multi-step flows, Back and competing actions are disabled while submission is in progress.

### Disabled

- Disabled does not replace validation or error guidance.
- The reason must be understandable from context or helper text.
- Disabled has no hover or active state.
- Disabled suppresses tone. Brand, Neutral, and Danger filled Buttons all use the general disabled treatment.
- Danger styling becomes neutral when disabled because disabled state takes priority over destructive tone.

### Focus

- Focus ring is independent from Button tone.
- Use `focus/default` on normal backgrounds.
- Use `focus/inverse` on inverse backgrounds.
- Cando yellow must not serve as the sole focus indicator.

### Icon-only

Icon-only controls are not standard Buttons. Use Icon Button.

Every Icon Button without visible text needs an accessible name. Tooltip does not replace an accessible name.

## Semantic Token Mapping

### Filled and Subtle

| Preset | Background | Hover | Active | Foreground |
|---|---|---|---|---|
| Brand | `surface/brand` | `surface/brand-hover` | `surface/brand-active` | `fg/on-brand` |
| Primary | `surface/neutral-emphasis` | `surface/neutral-emphasis-hover` | `surface/neutral-emphasis-active` | `fg/on-color` |
| Secondary | `surface/neutral-muted` | `surface/neutral-muted-hover` | `surface/neutral-muted-active` | `fg/primary` |
| Danger Filled | `surface/danger-emphasis` | `surface/danger-emphasis-hover` | `surface/danger-emphasis-active` | `fg/on-color` |

### Outline

| Preset | Background | Hover | Active | Foreground | Line |
|---|---|---|---|---|---|
| Tertiary | transparent | `surface/transparent-hover` | `surface/transparent-active` | `fg/primary` | `line/default` |
| Danger Outline | transparent | `surface/transparent-hover` | `surface/transparent-active` | `fg/danger` | `line/danger` |

### Ghost

| Preset | Background | Hover | Active | Foreground |
|---|---|---|---|---|
| Ghost | transparent | `surface/transparent-hover` | `surface/transparent-active` | `fg/primary` |
| Danger Ghost | transparent | `surface/transparent-hover` | `surface/transparent-active` | `fg/danger` |

### Disabled

| Appearance | Background | Foreground | Line |
|---|---|---|---|
| Brand / Primary / Secondary / Danger Filled | `surface/disabled` | `fg/disabled` | — |
| Tertiary / Danger Outline | transparent | `fg/disabled` | `line/disabled` |
| Ghost / Danger Ghost | transparent | `fg/disabled` | — |

There is no `fg/on-color-disabled` in v4 because filled disabled Buttons no longer preserve their original colored surface.

### Mapping Rules

- Brand is a Button preset/tone and maps to Brand semantics.
- Accent is not a Button preset in v4.
- Primary uses Neutral Emphasis.
- Secondary uses `surface/neutral-muted`, not structural `surface/muted`.
- Tertiary and Ghost are transparent at rest.
- Danger Filled uses Danger, not Error.
- `fg/on-brand` must remain independently resolvable in Cando to preserve contrast on yellow Brand surfaces.

## Link Versus Button

```text
Changes state or performs an operation
→ Button

Navigates to another destination
→ Link
```

A Link may look like a Button while retaining Link semantics and accessibility behavior.

## Controls That Are Not Button Presets

The following are separate components or patterns:

- Tab
- Segmented Control
- Filter Button
- Applied Filter Chip
- Toggle Button
- Selected/current/checked state
- Link
- Selectable Card

Selection styling follows `../experience-rules/selection.md`. Do not model selection as Brand Button state.

## Intentionally Unsupported Presets

The current model intentionally excludes:

- Brand Subtle
- Brand Outline
- Brand Ghost as a general preset
- Generic Accent Button
- Secondary Ghost as a separate preset
- Positive or Success Button
- Ghost over media
- The full unrestricted `tone × appearance` matrix

A new preset requires a repeated, generalizable use case validated in real product flows.

## Product Variations

- Brand uses the active product's Brand mapping: JobVision Blue, Cando Yellow.
- Brand usage meaning remains the same across products.
- `fg/on-brand` may resolve independently from the Brand background.
- Everyday Cando ATS actions remain Neutral even if Brand usage becomes rare.
- General chromatic interaction in both products uses Accent semantics, not Brand Button styling.

See `../product-variations/brand-variants.md`.

## Open Questions

1. Complete the official Brand Button use-case list for each product.
2. Test Secondary in ATS, especially in empty states and independent actions.
3. Review the hierarchy after at least three real flows:
   - Create or edit job
   - Recruitment request
   - Resume submission or package purchase
4. Resolve remaining on-media control and focus questions in the dedicated pattern.
5. Decide whether modal Cancel is always Ghost or whether some products consistently use Tertiary.

## Not Yet Defined

- Exact Button anatomy
- Size scale
- Dimensions and spacing
- Minimum target size
- Icon size and gap
- Radius mapping
- Exact code API
- Final Figma property names beyond the internal `tone × appearance` model

These sections must be added through a separate reviewed decision rather than inferred.

## Quick Reference

| Need | Preset |
|---|---|
| Defined Brand conversion / product-defining entry point | Brand |
| Main operational action | Primary |
| Supporting medium-emphasis action | Secondary |
| General, filter, dropdown, or toolbar action | Tertiary |
| Back, Cancel, Later, or third action | Ghost |
| Final destructive confirmation | Danger Filled |
| Independent destructive action | Danger Outline |
| Low-emphasis or inline destructive action | Danger Ghost |

The most important action is not automatically Brand. Brand must come from the approved product conversion/product-moment list.

In every action group, only one action should have the strongest visual emphasis.

## Related Documents

- `../experience-rules/action-hierarchy.md`
- `../experience-rules/navigation.md`
- `../experience-rules/selection.md`
- `../patterns/multi-step-flow.md`
- `../patterns/confirmation.md`
- `../patterns/destructive-actions.md`
- `../product-variations/brand-variants.md`
- `../tokens/jobvision-color-tokens-v4-surface-model.md`
