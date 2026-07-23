---
id: accordion
type: component
scope: shared
status: draft
maturity: usable-for-product-testing
source_figma: https://www.figma.com/design/VA5qSyutH4QkLTfimzdUbe/-DS--Job-Vision?node-id=31-2385
source_node: "31:2385"
---

# Accordion

## Purpose

Accordion uses progressive disclosure to organize related content in a compact vertical list. Each item exposes a short title and lets the user show or hide its associated content without navigating away.

Use Accordion when users benefit from scanning several section titles before deciding which details to read.

## Documentation Ownership

This document is the canonical source for:

- Accordion anatomy
- Figma properties and variants
- Size and layout rules
- Interaction behavior and states
- Semantic-token mappings
- Usage and content guidance
- Accessibility requirements

The Figma component remains the source for editable assets and variant construction. This document defines how those variants should be interpreted and used.

## Anatomy

An Accordion consists of one or more Accordion items.

Each item contains:

1. **Item container** — groups the trigger and its content panel.
2. **Header trigger** — the full interactive row that expands or collapses the item.
3. **Title** — describes the content revealed by the item.
4. **Chevron** — indicates the current collapsed or expanded state.
5. **Content panel** — contains the disclosed content.
6. **Optional content slot** — accepts custom content below the main body.
7. **Divider** — separates adjacent items.

The full header row is interactive. The Chevron is only a visual indicator and must not act as a separate control.

## Figma Properties

| Property | Values | Meaning |
|---|---|---|
| `Size` | `Large`, `Medium`, `Small` | Controls the minimum header height through vertical padding |
| `State` | `Enabled`, `Hover`, `Focus`, `Disabled`, `Skeleton` | Represents the current visual or loading state |
| `Alignment` | `Right`, `Left` | Controls which side contains the Chevron |
| `Expanded` | `True`, `False` | Controls panel visibility and Chevron direction |
| `Title text` | Text property | Sets the header label |
| `Content text` | Text property | Sets the primary panel text |
| `Slot` | Boolean | Shows or hides the optional custom-content region |
| `Swap slot` | Instance swap | Replaces the placeholder with another component |

`Alignment` controls the position of the Chevron, not the text direction. Text direction follows the product locale and content.

## Sizes and Layout

### Header

| Size | Minimum height | Horizontal padding | Vertical padding | Chevron | Title–Chevron gap |
|---|---:|---:|---:|---:|---:|
| Large | 48 px | 16 px | 12 px | 16 px | 16 px |
| Medium | 40 px | 16 px | 8 px | 16 px | 16 px |
| Small | 32 px | 16 px | 4 px | 16 px | 16 px |

The title uses the shared `body-01` typography style, currently 14 px with a 24 px line height.

The listed heights are minimums. A long title may wrap and increase the header height. Do not truncate a title when the missing text would make the section unclear.

The component should fill its parent width. The 400 px width shown in the Figma component set is an example width, not a fixed component width.

### Content panel

- Top padding: 8 px
- Bottom padding: 24 px
- Outer-side padding: 16 px
- Chevron-side padding: 48 px
- Gap between the primary content and optional slot: 16 px

The 48 px inset aligns the content with the title rather than the Chevron.

### Target size

Large is the default size for general use and touch-oriented interfaces.

Medium and Small are intended for dense desktop interfaces. If either size is used in a touch context, the implementation must provide an effective target size of at least 44 × 44 px without changing the visible layout.

## States

| State | Background | Foreground | Divider | Behavior |
|---|---|---|---|---|
| Enabled | Transparent | Normal | Visible | Can expand or collapse |
| Hover | `surface-transparent-hover` | Normal | Visible | Pointer feedback on the Header trigger |
| Active | `surface-transparent-active` | Normal | Visible | Press feedback while the trigger is activated |
| Focus | Transparent | Normal | Visible | Shows the keyboard focus ring |
| Disabled | Transparent | Disabled | Structural divider remains visible | Cannot expand or collapse |
| Skeleton | Skeleton treatment | No readable content | Structural divider may remain visible | Non-interactive loading representation |

Disabled has no Hover or Active state.

Skeleton is a loading representation, not an interactive state. It must not receive focus or expose an expandable control until the real content is available.

### Focus status

The current Figma component uses a two-pixel border around the item for Focus. This treatment is temporary and is not the canonical implementation.

The planned Focus treatment must:

- Apply to the Header trigger, not the expanded content panel
- Use a non-layout-affecting `box-shadow` or equivalent focus ring
- Use `focus-default` on normal surfaces
- Use `focus-inverse` on inverse surfaces
- Remain visible in both Light and Dark modes

Exact shadow offset, spread, and layering remain open until the Figma component is updated.

## Expanded and Collapsed Behavior

Expanded is disclosure state, not selection state. Do not use selected, Accent, or Brand tokens to distinguish an expanded item.

### Collapsed

- The Content panel is hidden.
- The Chevron points down.
- The trigger sets `aria-expanded="false"`.

### Expanded

- The Content panel is visible directly below the Header.
- The Chevron points up.
- The trigger sets `aria-expanded="true"`.
- The Header keeps the same Rest, Hover, Active, Focus, and Disabled mappings used when collapsed.

Opening or closing an item must not shift the horizontal alignment of adjacent content.

If expansion is animated, keep the motion short and preserve the user's `prefers-reduced-motion` setting. Do not delay access to content for decorative animation.

## Group Behavior

Each Accordion item owns its own disclosure state.

The current Figma component does not determine whether an Accordion group allows one or multiple items to remain open. The implementation must expose and document the selected group behavior instead of changing it implicitly between screens.

Until a shared default is approved:

- Use multiple-open behavior when users may need to compare content between sections.
- Use one-open-at-a-time behavior only when space is constrained and comparison is not important.

## Usage

### Use for

- Long supporting information divided into clear sections
- FAQs
- Settings or form sections that users may inspect selectively
- Secondary details that do not need to remain visible at all times

### Do not use for

- A small amount of content that can be shown directly
- The primary action or primary message of a page
- Step-by-step flows where users must complete sections in order
- Tabs or other navigation between separate destinations
- Hiding information required to understand or complete the current task

Avoid deeply nesting Accordions. If content needs multiple disclosure levels, reconsider the information architecture.

## Content Guidance

- Write short, specific titles that describe the hidden content.
- Keep titles unique within the same Accordion group.
- Do not phrase every title as “More information.”
- Do not put the only indication of an error, required action, or important status inside a collapsed panel.
- Custom slot content must follow its own component and token rules; the placeholder appearance in Figma is not part of the Accordion visual specification.

## Semantic Token Mapping

Accordion does not require component-specific color tokens. It consumes Semantic tokens directly.

### Normal surfaces

| Element or state | Figma variable | Code token |
|---|---|---|
| Title | `fg/primary` | `fg-primary` |
| Chevron | `fg/primary` | `fg-primary` |
| Content text | `fg/primary` | `fg-primary` |
| Item divider | `line/muted` | `line-muted` |
| Header Rest | Transparent | Transparent |
| Header Hover | `surface/transparent-hover` | `surface-transparent-hover` |
| Header Active | `surface/transparent-active` | `surface-transparent-active` |
| Disabled title and Chevron | `fg/disabled` | `fg-disabled` |
| Focus ring | `focus/default` | `focus-default` |
| Skeleton body | `skeleton/base` | `skeleton-base` |
| Skeleton highlight | `skeleton/shimmer` | `skeleton-shimmer` |

The divider is structural. It remains `line-muted` when an item is Disabled; `line-disabled` is reserved for a line that belongs to the disabled control itself.

### Inverse surfaces

Use these mappings only when the component is intentionally supported on `surface-inverse`.

| Element or state | Figma variable | Code token |
|---|---|---|
| Title, Chevron, and content | `fg/on-inverse` | `fg-on-inverse` |
| Item divider | `line/inverse` | `line-inverse` |
| Header Hover | `surface/transparent-inverse-hover` | `surface-transparent-inverse-hover` |
| Header Active | `surface/transparent-inverse-active` | `surface-transparent-inverse-active` |
| Focus ring | `focus/inverse` | `focus-inverse` |

## Figma Token Migration

The current Figma component still contains legacy variable names. Update the bindings using this mapping:

| Current binding | Approved binding |
|---|---|
| `fg/fg-primary` | `fg/primary` |
| `fg/fg-disabled` | `fg/disabled` |
| `border-stroke-subtle` | `line/muted` |
| `$border-subtle-01 - Inner/Border top` | Use `line/muted` as the divider color |
| `surface/surface-transparent-hover` | `surface/transparent-hover` |
| `utility/focus-default` | `focus/default` |

Transparent Rest does not need a component-specific token.

The optional Slot's placeholder styles and tokens are outside this migration. Replacement content owns its own Semantic or approved Component tokens.

## Accessibility

### Semantics

- Implement each Header trigger as a native `button`.
- Set `aria-expanded` to reflect the current state.
- Connect the trigger to its Content panel with `aria-controls`.
- Give the panel a stable `id`.
- Associate the panel with its trigger using `aria-labelledby` when the panel needs an accessible region label.
- Treat the Chevron as decorative with `aria-hidden="true"`.
- Place the trigger inside an appropriate heading level when the Accordion represents document sections.

### Keyboard

- `Tab` and `Shift+Tab` move between focusable controls in normal document order.
- `Enter` or `Space` toggles the focused item.
- Focus remains on the Header trigger after expansion or collapse.
- Do not move focus into the panel automatically.

Arrow-key navigation is optional unless the implementation adopts a composite widget model. Do not add it inconsistently across products.

### Disabled items

Avoid a Disabled collapsed item when its content is otherwise unavailable. If users need to read the content but must not change something inside it, keep the Accordion item expandable and disable only the affected inner controls.

### Loading

When Skeleton is shown:

- Do not expose placeholder text to assistive technology.
- Mark the containing region as busy when appropriate.
- Replace Skeleton with the real interactive item when loading completes.

## Figma Implementation Notes

- Component set: `Accordion`
- Source node: `31:2385`
- Current sizes: Large 48 px, Medium 40 px, Small 32 px
- Both `Alignment` values support collapsed and expanded variants.
- Enabled, Hover, Focus, Disabled, and Skeleton variants exist for all three sizes.
- The component's example width is 400 px; production width is responsive.
- Active behavior is defined in this document but does not yet have a dedicated Figma variant.

## Open Decisions

1. Define the final Focus `box-shadow` specification and update the Figma Focus variants.
2. Add a dedicated Active variant to the Figma Component Set or document how it is represented in prototypes.
3. Approve a default group policy for single-open versus multiple-open behavior.
4. Confirm the final typography binding when the shared product typography decision is implemented in Figma.
5. Clean up the optional Slot placeholder without treating it as a blocker for Accordion usage.

## Related Documents

- `../tokens/semantic-tokens.md`
- `../tokens/usage-rules.md`
- `../tokens/color-token-aliases.md`
- `../accessibility/README.md`
