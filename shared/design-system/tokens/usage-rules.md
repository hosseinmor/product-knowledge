---
id: design-system.token.usage-rules
collection: design-system
type: token
title: Token Usage Rules
summary: '> Status: draft'
knowledge_state: unverified
document_maturity: draft
related: []
---

# Token Usage Rules

> Status: draft

## Allowed usage

- Components consume Semantic tokens by default; use an approved Component token only for its documented owner component.
- Select Brand and Semantic Light/Dark modes independently.
- Use Semantic `surface/*` for general UI backgrounds, including the root page/workspace.
- The approved Tag component uses its own `tag/*` color family by exception.
- Test supported Brand × Semantic combinations for accessibility.
- A shared Primitive value does not merge semantic meaning. Choose tokens by role, not by visual color.

## Surface selection

- Ordinary root page, in-flow container, card, panel, or structural sheet → `surface/default`
- Passive lower-emphasis supporting or grouping region → `surface/muted`
- Region behind the local default surface, such as recessed workspace structure or chrome → `surface/inset`
- Surface visually elevated above its immediate parent, such as a menu, popover, dropdown, floating panel, or appropriate dialog → `surface/raised`
- High-contrast inverted region → `surface/inverse`
- Visible neutral interactive treatment with medium emphasis → `surface/neutral-muted`
- High-emphasis neutral operational action → `surface/neutral-emphasis`
- Transparent-at-rest interaction → `surface/transparent-hover/active`
- Transparent interaction on inverse surface → `surface/transparent-inverse-hover/active`
- Persistent selected row/item/container → `surface/selected` and `surface/selected-hover`
- Approved Brand conversion or product-defining moment → `surface/brand*`
- General chromatic interaction/affordance → matching `surface/accent-*`, `fg/accent`, or `line/accent`
- AI-assisted/generated treatment → matching Magic roles
- Destructive action → matching Danger roles
- Validation or system feedback → matching Support muted surface, foreground, and line roles
- Disabled filled control → `surface/disabled + fg/disabled`

`surface/raised` expresses the color role of an elevated layer. Pair it with the approved elevation/shadow token when visible depth is required.

Do not use structural `surface/muted` as an interactive control background. Use `surface/neutral-muted` instead.

## Brand versus Accent

Use Brand when the reason for color is product identity or an approved key product/conversion moment.

Use Accent when the reason for color is general interaction or chromatic affordance.

Examples:

```text
Brand Button at approved conversion
→ surface/brand

Cando link
→ link/default

Selected line Tab indicator
→ line/accent

Saved bookmark
→ fg/accent

Operational Primary Button
→ surface/neutral-emphasis
```

Do not use Brand merely to make an operational action more prominent.

## Selection

Selection is a component state, not a full global color family.

Use Accent for a chromatic selected/current/checked cue when the component anatomy calls for one:

```text
selected line Tab → fg/primary + line/accent
checked checkbox  → surface/accent-emphasis + fg/on-color
saved bookmark    → fg/accent
```

Use the dedicated neutral selected-container surface for persistent selected containers:

```text
selected row/item → surface/selected
selected row/item:hover → surface/selected-hover
```

Do not invent `fg/selected`, `line/selected`, selected emphasis, inverse, disabled, or active families without a repeated cross-component need.

## Links

Default Link is the recognizable chromatic navigation treatment:

```text
link/default
link/hover
```

Use the neutral Subtle Link only when context already makes clickability clear:

```text
link/subtle
link/subtle-hover
```

Typical Subtle contexts include dense ATS UI, navigation, metadata, and “View all” patterns. Do not use Subtle as the normal inline body-copy Link unless another persistent affordance such as underline preserves recognition.

Use the single inverse Link family on `surface/inverse`:

```text
link/inverse
link/inverse-hover
```

Do not use `link/visited` unless a future reviewed product pattern establishes a persistent visited-state need.

## Disabled

Disabled suppresses tone by default.

```text
Brand filled disabled
Primary disabled
Secondary disabled
Danger Filled disabled
→ surface/disabled + fg/disabled
```

Outline disabled treatments use `fg/disabled + line/disabled`; transparent disabled treatments use `fg/disabled`.

Do not create tone-specific disabled colors merely to preserve the original tone. Disabled has no hover or active state.

## Support on inverse surfaces

The inverse Support foreground roles are intentionally narrow:

```text
fg/info-inverse
fg/success-inverse
fg/warning-inverse
fg/error-inverse
```

Use them for colored Support content on `surface/inverse`, such as status icons/text in an inverse Toast. Their existence does not justify Support inverse surfaces or line families.

## Prohibited usage

- Do not consume Primitive or Brand variables directly from ordinary component implementations.
- Do not encode product or mode names into Semantic token names.
- Do not restore `canvas` or an Experience color collection without a new demonstrated need.
- Do not use removed v3 names for new work: `surface/control*`, `surface/emphasis*`, `surface/brand-muted`, `fg/brand`, `line/brand`, expanded `surface/selected-*`, `fg/selected`, `line/selected`, `fg/on-color-disabled`, `link/emphasis*`, or `link/visited`.
- Do not invent hover/active states for passive or disabled surfaces.
- Do not use Tag tokens as a generic palette for other components.

## Fallbacks

- Semantic Light/Dark mappings must resolve the active Brand input when Brand meaning is required.
- A semantic role that does not vary by product may alias a Primitive directly.
- If a proposed value fails accessibility, choose a contrast-safe approved mapping rather than binding a component to an arbitrary Primitive.
- If a future product needs a different Accent hue, add the minimum product-aware alias without changing the public Semantic role names.

## Migration rules

1. Remove the `Experience` collection from the color resolution path.
2. Replace root `canvas` usage with the appropriate structural Surface, normally `surface/default` or `surface/inset` according to hierarchy.
3. Replace `surface/control*` with `surface/neutral-muted*`.
4. Replace `surface/emphasis*` with `surface/neutral-emphasis*`.
5. Replace `surface/brand-emphasis*` with `surface/brand*`; remove `surface/brand-muted`, `fg/brand`, and `line/brand`.
6. Add the approved Accent family and migrate chromatic interaction cues to Accent by meaning.
7. Replace the expanded Selected matrix with `surface/selected` and `surface/selected-hover`; use existing Accent/Neutral roles for other selection presentations.
8. Remove `fg/on-color-disabled`; disabled filled controls use the general disabled treatment.
9. Replace Link `emphasis` with `subtle` using the new direction: Default is chromatic, Subtle is neutral. Remove Visited.
10. Rename Button Accent preset/tone to Brand and update its semantic mappings.
11. Rename Brand collection `accent/* → brand/*` and `content/on-accent → content/on-brand`.
12. Replace product-specific Primitive brand palettes with generic hue palettes during the palette migration.
13. Update Figma and code references together after final alias values and implementation mapping are approved.

See `architecture.md`, `jobvision-color-tokens-v4-surface-model.md`, and `color-token-aliases.md`.
