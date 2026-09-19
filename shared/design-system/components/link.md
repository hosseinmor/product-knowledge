---
id: design-system.component.link
collection: design-system
type: component
title: Link
summary: Links navigate users to another destination through a minimal standalone component and an inline native-text recipe.
knowledge_state: verified
document_maturity: draft
related: []
design_status: ready-for-dev
design_maturity: handoff-ready
last_reviewed: '2026-09-19'
---

# Link

## Purpose

Links navigate users to another destination.

Use native anchor semantics when activation changes the current destination. Use Button when the control changes state, submits data, confirms a decision, or otherwise performs work in the current context.

## Authoring Model

v4 deliberately separates two use cases:

### Standalone Link

Use the canonical Figma component when the Link is a standalone/contextual control.

Component set: `Link / Default`

### Inline Link

When a Link appears inside running text, do **not** insert the atomic Link component into the sentence.

Use a native Text layer and style only the Link range with:

- the appropriate `link/*` semantic color;
- a persistent underline;
- the typography inherited from the surrounding text.

This keeps inline Links naturally multiline and lets them follow any surrounding Body typography without creating Size or Underline variants on the standalone component.

## Canonical Figma API

Canonical file: `[DS] Job Vision NEXT`

- Figma file key: `rROD8ctH9UfPGAMrRrOzHe`
- Component set: `Link / Default`
- Figma node ID: `22915:125435`
- Figma component key: `185633dee3397a6e143c8c4acf2471cac65911d7`
- Variant count: `12`
- Default variant: `Style=Default, State=Enabled`

### Variant properties

| Property | Values |
|---|---|
| `Style` | `Default`, `Subtle`, `Inverse` |
| `State` | `Enabled`, `Hover`, `Active`, `Focus` |

### Content properties

| Property | Behavior |
|---|---|
| `Link text` | Visible destination label |
| `End icon` | Optional boolean |
| `Swap end icon` | Instance swap |

The canonical component intentionally has **no** Size, Underline, Start icon, Visited, Disabled, or Bold axis/property.

The pre-v4 component is retained in Figma as `Link / Legacy` only for migration compatibility and must not be used for new designs.

## Typography and Anatomy

Standalone Link uses one typography recipe:

```text
Body / Compact / SM
14 / 20
Regular 400
```

Rules:

- width hugs content in the atomic Figma component;
- text weight is always Regular `400`;
- one optional End icon is supported;
- icon size is fixed at `18px`;
- icon-label gap is `8px`;
- no Start icon is exposed;
- do not create visual hierarchy by changing Link weight or font size.

Why there is no Size axis:

- standalone Links should normally match the product's default compact Body scale;
- inline Links inherit the typography of the surrounding Text;
- removing Size prevents an unnecessary `3×` expansion of the standalone component matrix.

## Style Selection

### Default

Default is the recognizable chromatic Link treatment.

```text
Enabled / Focus → link/default
Hover / Active → link/hover
```

Use it when the destination should remain clearly recognizable as a Link.

### Subtle

Subtle is the lower-prominence neutral Link treatment.

```text
Enabled / Focus → link/subtle
Hover / Active → link/subtle-hover
```

Use when surrounding context already communicates navigation, for example:

- dense ATS/product UI;
- navigation;
- card metadata;
- breadcrumb-like destinations;
- contextual “View all” or “Learn more” links.

Do not use Subtle as an unadorned inline body-copy Link.

### Inverse

Use Inverse only on `surface/inverse` or another reviewed inverse surface.

```text
Enabled / Focus → link/inverse
Hover / Active → link/inverse-hover
```

Focus composes with the shared `focus/inverse` treatment.

## State Behavior

Standalone Link behavior:

| State | Foreground | Underline | Focus treatment |
|---|---|---|---|
| Enabled | style rest token | No | No |
| Hover | style hover token | Yes | No |
| Active | style hover token | Yes | No |
| Focus | style rest token | Yes | shared focus recipe |

Default and Subtle use the shared default focus recipe. Inverse uses the shared inverse focus recipe.

There is no Link-specific Active color token; Active reuses the relevant hover semantic token.

### Figma underline implementation

Figma normalizes native Text-decoration across component variants, so the canonical component uses a **Figma-only responsive 1px underline helper** inside the label wrapper:

- opacity `0` in Enabled;
- opacity `1` in Hover, Active, and Focus;
- width follows the current Link text automatically;
- component height remains `20px`.

This helper is a design-authoring implementation detail.

### Runtime underline implementation

Runtime code should use real text decoration:

```text
Enabled → no text-decoration
Hover / Active / Focus → underline
```

Do not reproduce the Figma helper rectangle in application code.

Inline Links remain persistently underlined in all states.

## Icons

The standalone component supports only an optional End icon.

Use an End icon when it adds destination or navigation meaning.

Examples:

- external destination → `launch`;
- reviewed directional/destination cue where an icon materially improves comprehension.

Rules:

- no Start icon;
- no icon for ordinary inline sentence Links;
- icon is normally decorative when the visible label already communicates the destination;
- the icon uses the same semantic foreground color as the Link text;
- icon size is `18px`;
- icon-label gap is `8px`.

The external-link icon does not define whether the browser opens a new tab.

## Inline and Multiline Links

Inline Links are authored as native Text ranges in Figma.

Recipe:

1. use the surrounding Text style;
2. select the Link range;
3. apply the appropriate `link/*` semantic color;
4. apply persistent underline;
5. preserve normal wrapping.

Runtime anchors may wrap naturally in constrained layouts. Do not force `white-space: nowrap` globally on Links.

For a long standalone Link that must wrap in a design mockup, use the same native-Text recipe rather than detaching the atomic component or introducing a Width/Size variant.

## Link vs Button

Use Link when activation navigates to another page, route, document, anchor, email, phone target, or external resource.

Use Button when activation changes state, mutates data, confirms/cancels an operation, or otherwise performs work in the current context.

A navigation element may use a reviewed Button visual treatment while remaining an anchor semantically. Do not create a parallel `link-button/*` token family.

## Deliberate Exclusions

### Size

No standalone Size axis. Standalone uses 14/20; inline inherits surrounding typography.

### Underline property

No author-facing Underline toggle.

- standalone underline behavior is state-driven;
- inline underline is persistent by definition.

### Start icon

Not part of the current Link contract. Destination cues belong in the optional End slot.

### Disabled

Disabled is not part of the Link API. If a destination is unavailable, reconsider whether it should be rendered as an interactive Link at all.

### Visited

Visited is not part of shared v4 because no reviewed product pattern currently requires persistent visited styling.

### Bold

Bold is not a Link hierarchy axis. Use surrounding typography hierarchy and semantic Link roles instead.

## RTL

Do not create separate RTL variants.

The single optional icon represents the logical destination/end cue. Runtime layout should place it at the logical End according to direction.

In the current RTL product authoring context, the End icon appears to the left of the Persian label.

Directional glyphs must follow the icon-system RTL behavior rather than being manually duplicated inside Link.

## Accessibility and Interaction Contract

- Prefer native `<a href="…">` semantics for navigation.
- Every Link requires an accessible name; normally this is its visible label.
- Preserve expected browser Link behavior.
- Keyboard focus must follow the shared Focus contract and remain visibly distinct.
- Inline body-copy Links use persistent underline.
- Standalone Links without a persistent underline rely on approved Link color/context at rest and add underline on Hover, Active, and Focus.
- Link foreground must meet applicable text contrast against its background.
- Do not expose Disabled as a Link state.
- End icons are decorative when the visible label already communicates the destination.
- Standalone targets must follow the shared target-size/spacing contract; the inline-text exception applies only to genuine running-text Links.

## Development Contract

Expected conceptual API:

```text
Link
- style: default | subtle | inverse
- endIcon?: icon
- href / destination
- children / label
```

Implementation requirements:

- native anchor semantics for navigation;
- typography: 14/20, weight 400 for the standalone component;
- icon size: 18px;
- icon-label gap: 8px;
- optional End icon only;
- default style: Default;
- Enabled has no underline;
- Hover and Active use the style hover token and underline;
- Focus keeps the style rest foreground, adds underline, and composes the shared focus treatment;
- no public `size`, `underline`, `startIcon`, `visited`, `disabled`, or `bold` Link variants;
- runtime Links may wrap naturally;
- interaction pseudo-states should normally be CSS/platform behavior, not public application props;
- do not duplicate Link semantic tokens as component-local colors.

The exact framework/class architecture remains unverified until the runtime Design System source is registered.

## QA Checklist

Verify:

- exactly 12 Figma variants: 3 Style × 4 State;
- only `Style` and `State` are variant axes;
- only `Link text`, `End icon`, and `Swap end icon` are content properties;
- standalone typography is 14/20 Regular;
- End icon is 18px with 8px gap;
- Enabled underline helper opacity is 0;
- Hover / Active / Focus underline helper opacity is 1;
- underline width follows Link text overrides;
- Focus uses the correct default/inverse focus treatment;
- all semantic Link color bindings resolve correctly;
- no Size, Underline, Start icon, Visited, Disabled, Bold, or legacy Inline axes are reintroduced;
- inline body-copy Links use native Text with persistent underline;
- inline/multiline authoring preserves wrapping;
- runtime anchors can wrap naturally;
- keyboard focus is visible.

## Legacy Migration

Figma retains `Link / Legacy` only for migration.

```text
Inline=True
→ native Text + link token + persistent underline

Bold=True
→ remove; use surrounding typography hierarchy

Small / Large standalone Link
→ migrate to canonical 14/20 standalone Link unless the use case is actually inline text

Visited
→ remove unless a future reviewed pattern explicitly requires it

Disabled
→ remove and revisit the availability/UX model

Icon
→ optional End icon
```

Do not create new instances of `Link / Legacy`.

## Open Items

Runtime implementation remains unverified until the owning Design System repository/package and Storybook source are registered.

Still requiring runtime verification:

- exact runtime component/API identifier;
- exact Angular/Tailwind authoring pattern;
- Storybook stable story/docs identifier;
- exact Figma-property → code-prop mapping;
- Code Connect or equivalent mapping mechanism.

## Live References

- Figma file: `[DS] Job Vision NEXT`
- Figma component set: `Link / Default`
- Figma node ID: `22915:125435`
- Figma component key: `185633dee3397a6e143c8c4acf2471cac65911d7`
- Figma default: `Style=Default, State=Enabled`
- Figma Playground: Default, Hover/underline, End icon, External, Subtle, Focus, Inverse, and native Text inline/multiline examples
- Storybook / Code: not yet connected as a canonical live reference

## Related Documents

- `button.md`
- `../accessibility/focus-management.md`
- `../accessibility/pointer-touch-and-gestures.md`
- `../accessibility/color-and-contrast.md`
- `../experience-rules/navigation.md`
- `../integrations/component-mapping.md`
- `../tokens/semantic-tokens.md`
