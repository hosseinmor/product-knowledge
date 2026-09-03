---
id: button
collection: design-system
type: component
title: Button
summary: Buttons trigger actions and use a small preset hierarchy for Brand, operational, low-emphasis, and destructive actions.
knowledge_state: unverified
document_maturity: draft
related: []
design_status: draft
design_maturity: usable-for-product-testing
source_guideline: button-guidelines-v0.6.md
---

# Button

## Purpose

Buttons trigger actions. Designers choose from a small set of named presets rather than solving an unrestricted style matrix.

## Use / Avoid

Use Button when an action changes state, submits data, confirms a decision, opens an operation, or otherwise performs work in the current context.

Use Link when the primary behavior is navigation to another destination.

Use a dedicated control rather than Button when the interaction represents selection or another specialized behavior, such as Tab, Segmented Control, Toggle Button, Filter Chip, or Icon Button.

## Choices

| Need | Preset |
|---|---|
| Defined product conversion or product-defining entry point | Brand |
| Main operational action | Primary |
| Supporting medium-emphasis action | Secondary |
| General, filter, dropdown, toolbar, or utility action | Tertiary |
| Back, Cancel, Later, or another low-emphasis action | Ghost |
| Final destructive confirmation | Danger Filled |
| Visible independent destructive action | Danger Outline |
| Low-emphasis or inline destructive action | Danger Ghost |

### Brand

Brand is reserved for approved conversion/product moments such as resume submission, sign-up, purchase/upgrade, request-demo, or a major entry into the product's core value.

Being the most important action on a page does not automatically make an action Brand. Everyday operational actions such as Save changes are normally Primary.

Use at most one Brand action in the same action group. Brand and Primary should not compete as equal CTAs in one group.

### Primary

Use for the most important operational action in the current decision region, such as Save, Continue, Confirm, Submit, or Send for approval.

A decision region normally has one strongest operational action.

### Secondary

Use for a supporting action that should remain visible with medium emphasis. Secondary does not mean “the second button.”

Use Tertiary for control-like actions and Ghost for exits such as Back or Cancel.

### Tertiary

Use for filters, sorting, dropdown triggers, export, settings, editing, toolbar actions, and similar independent utilities.

Tertiary is the normal outline treatment for dense operational interfaces such as ATS.

### Ghost

Use for Back, Cancel, Not now, third-or-later actions, and other intentionally low-emphasis operations.

If Ghost still feels too prominent, reconsider placement, copy, or whether the control should be a Link rather than creating another weaker Button style.

### Danger

Use Danger only for destructive intent, not merely negative wording.

- Final destructive confirmation → Danger Filled
- Visible independent destructive action → Danger Outline
- Low-emphasis destructive entry point or inline action → Danger Ghost

A reversible rejection or negative choice is not automatically destructive.

## Behavior and States

### Loading

- The triggering Button may enter Loading after submission.
- Prevent repeated submission while the operation is in progress.
- Keep the Button width stable when practical so surrounding layout does not jump.
- Flow-level rules decide whether competing actions are also disabled; that policy does not belong to Button alone.

### Disabled

Disabled suppresses the original tone. Do not preserve Brand or Danger chroma merely to show what the enabled action would have been.

Conceptual semantic roles:

```text
Filled disabled surface
→ surface/disabled
→ fg/on-disabled

Transparent / outline disabled content
→ fg/disabled

Disabled outline
→ line/disabled
```

The current Figma-facing token may still be named `fg/on-color-disabled`; treat it as the current implementation name for the conceptual `fg/on-disabled` role until the separate naming pass is completed.

Disabled does not replace validation or error guidance. The reason an action is unavailable should be understandable from the surrounding context when that reason matters to task completion.

### Focus

Focus treatment is independent from Button tone. Use the shared Focus contract rather than Brand or Danger color as the sole focus indication.

### Icon-only

An icon-only action is an Icon Button, not a Button preset. It requires its own accessible name and target-size contract.

## Composition and Content

- Prefer one strongest action per action group.
- Do not use Brand merely to create visual emphasis.
- Avoid repeating high-emphasis Buttons across every row/card in dense interfaces.
- Use concise action labels that describe the result of activation.
- If an action navigates rather than performs an operation, use Link semantics even when its visual treatment resembles a Button.

Cross-component action hierarchy belongs in `../experience-rules/action-hierarchy.md`.

## Semantic Mapping

The component consumes shared Semantic color roles; it does not need Button-specific Color tokens.

| Preset | Semantic treatment |
|---|---|
| Brand | `surface/brand` + `fg/on-brand` |
| Primary | `surface/neutral-emphasis` + on-color foreground |
| Secondary | `surface/neutral-muted` + normal foreground |
| Tertiary | transparent + `line/default` + normal foreground |
| Ghost | transparent + normal foreground |
| Danger Filled | `surface/danger-emphasis` + on-color foreground |
| Danger Outline | transparent + `line/danger` + `fg/danger` |
| Danger Ghost | transparent + `fg/danger` |

Hover and Active states follow the corresponding Semantic family. Do not duplicate the complete token state matrix here when it can be resolved from the token system/live implementation.

`surface/muted` is a passive structural surface and must not be used as the Secondary Button background.

## Product Variation

Brand uses the active product Brand mapping: JobVision Blue and Cando Yellow. Brand meaning remains the same across products.

Everyday Cando operational actions remain Neutral even when Brand usage is rare. General chromatic interaction is Accent semantics, not another Button tone.

## Accessibility

- Prefer a native `button` element for Button behavior.
- Preserve native keyboard activation unless a documented platform constraint requires otherwise.
- Every Button needs an accessible name that communicates the action.
- Visible focus must follow the shared Focus contract.
- Loading must not create repeated activation or unexpectedly move focus.
- Disabled, loading, destructive intent, and validation are different concepts; do not collapse them into one state.
- Target size follows the shared Accessibility baseline; exact Button sizing remains unresolved until the size contract is approved.

General keyboard, focus, target-size, contrast, and semantics requirements come from the Accessibility corpus. This section owns only Button-specific behavior.

## Known Gaps

Still unresolved:

- exact Button anatomy;
- size scale, dimensions, spacing, icon size/gap, and radius mapping;
- minimum visual dimensions for each size;
- exact code API;
- final Figma property names;
- final approved Brand use-case list by product;
- whether Modal Cancel has one shared default treatment across products.

These gaps must not be inferred from this document or from legacy screenshots.

## Live References

- Figma: current shared Design System Button component; exact component/property reference still needs to be recorded.
- Storybook / Code: not yet connected as a canonical live reference.

## Related

- `../experience-rules/action-hierarchy.md`
- `../experience-rules/navigation.md`
- `../experience-rules/selection.md`
- `../patterns/multi-step-flow.md`
- `../patterns/confirmation.md`
- `../patterns/destructive-actions.md`
- `../product-variations/brand-variants.md`
- `../tokens/jobvision-color-tokens-v4-surface-model.md`
