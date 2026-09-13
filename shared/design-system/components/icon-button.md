---
id: design-system.component.icon-button
collection: design-system
type: component
title: Icon Button
summary: Icon Button triggers an action with a single icon when a visible text label would add unnecessary density.
knowledge_state: unverified
document_maturity: draft
related:
  - button
design_status: draft
design_maturity: usable-for-product-testing
---

# Icon Button

## Purpose

Icon Button triggers an action using a single familiar icon. Use it when the action can be understood reliably without a persistent visible text label and space or density makes a text Button unnecessarily heavy.

Icon Button is a separate component from Button. Do not model icon-only actions through a Button `Type` property.

## When to Use

Use Icon Button for compact actions such as common toolbar utilities, close/dismiss actions, overflow menus, edit controls, or other familiar actions where the icon meaning is clear in context.

Use Button when the action needs a visible text label for clarity, emphasis, conversion, confirmation, or safety.

Do not use Icon Button for a destructive final confirmation. Use a labeled destructive Button instead.

## Anatomy

Icon Button contains:

- one square control container;
- one centered icon;
- no visible text label.

The icon is exposed as a single instance-swap property named `Icon`.

## Variants

Canonical Style values:

- Brand
- Primary
- Secondary
- Tertiary
- Ghost
- Danger Tertiary
- Danger Ghost

Brand is available for approved product-defining moments where an icon-only treatment remains understandable.

Danger Primary is intentionally not exposed. Destructive final confirmation requires a visible text label.

## Sizes

Icon Button shares the Button visual size scale:

| Size | Container | Icon |
|---|---:|---:|
| Large | 48px | 18px |
| Medium | 40px | 18px |
| Small | 32px | 18px |
| Extra Small | 28px | 18px |

The container is square at every size.

Icon size remains fixed at 18px for v1 to match the current icon foundation and Button contract.

All sizes use `Radius/Control = 6px`.

## States

Interaction states:

- Enabled
- Hover
- Active
- Focus
- Disabled

Focus uses the shared Focus contract.

Disabled follows the shared disabled semantic model inherited from Button. Do not preserve Brand or Danger chroma merely to communicate the enabled treatment.

Loading is not part of the v1 Icon Button state matrix and remains unresolved.

## Behavior

The default Figma variant is:

`Tertiary / Medium / Enabled`

This keeps the generic insertion point utility-oriented rather than defaulting to Brand or Primary emphasis.

Toggle/selected behavior is outside Icon Button. If an icon control represents persistent selection or on/off state, use or define a dedicated toggle/selection control rather than adding `Selected` to Icon Button.

## Accessibility

Every Icon Button requires an accessible name describing the action.

The accessible name should describe the action, not the visual appearance of the icon.

Tooltip behavior, exceptions, and minimum interactive target-size rules are still under review and must not be inferred from the Figma component alone.

## Product Variations

Brand uses the active product Brand mapping. The semantic meaning of Brand remains consistent with Button.

## Figma Reference

- File: `rROD8ctH9UfPGAMrRrOzHe`
- Page: `🔘 Button`
- Documentation frame: `22685:1411 — Icon Button`
- Component set: `22685:1410 — Icon Button / Default`
- Component key: `f9b7af4bd9afaf768ae955c51ccddd29833c5ca7`
- Matrix: 7 Styles × 4 Sizes × 5 States = 140 variants
- Properties: `Style`, `Size`, `State`, `Icon`

Legacy icon-only Button variants remain in `Legacy / Button` only for backward compatibility. Do not use them for new designs.

## Code Reference

Runtime repository/package and Storybook mapping are not yet registered as canonical sources. Runtime API remains unverified.

## Known Gaps

Still unresolved:

- tooltip requirement and exceptions;
- minimum interactive target versus visual size;
- whether Large should ever use a larger icon after optical review;
- Loading behavior and visual treatment;
- exact runtime API and implementation parity.
