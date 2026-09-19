---
id: design-system.component.link
collection: design-system
type: component
title: Link
summary: Links navigate users to another destination through Default, Subtle, or Inverse semantic treatments.
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

Use a native anchor when activation changes the current destination. Use Button when the control changes state, submits data, confirms a decision, or otherwise performs work in the current context.

A Link may visually resemble a Button, but Link semantics remain navigation semantics.

## Canonical Figma API

Canonical file: `[DS] Job Vision NEXT`

Component set: `Link / Default`

- Figma file key: `rROD8ctH9UfPGAMrRrOzHe`
- Figma node ID: `22901:125760`
- Figma component key: `93372073ea1f24b1726354518570da662e021ae5`
- Variant count: `72`
- Default variant: `Style=Default, Size=Medium, State=Enabled, Underline=False`

### Variant properties

| Property | Values |
|---|---|
| `Style` | `Default`, `Subtle`, `Inverse` |
| `Size` | `Small`, `Medium`, `Large` |
| `State` | `Enabled`, `Hover`, `Active`, `Focus` |
| `Underline` | `False`, `True` |

### Content properties

| Property | Behavior |
|---|---|
| `Link text` | Visible destination label |
| `Start icon` | Optional boolean; logical Start position |
| `Swap start icon` | Instance swap |
| `End icon` | Optional boolean; logical End position |
| `Swap end icon` | Instance swap |

The canonical set intentionally does **not** expose `Disabled`, `Visited`, `Bold`, or the legacy `Inline` axis.

The pre-v4 component is retained in Figma as `Link / Legacy` only for migration compatibility and must not be used for new designs.

## Sizes and Anatomy

| Size | Label typography |
|---|---|
| Small | Body / Compact / XS — 12/16, Regular 400 |
| Medium | Body / Compact / SM — 14/20, Regular 400 |
| Large | Body / Compact / MD — 16/24, Regular 400 |

Shared anatomy rules:

- Width hugs content by default in the atomic Figma component.
- Label weight is Regular `400`; do not use Bold as a Link variant.
- Start and End icons are optional.
- Icon size is fixed at `18px` across all Link sizes.
- Gap between icon and label is `8px`.
- Start and End are logical positions, not physical left/right positions.
- In RTL, Start is visually on the right and End is visually on the left.
- Do not add decorative background, border, or container styling to create another Link tone.

## Style Selection

### Default

Default is the recognizable chromatic Link treatment.

```text
link/default
link/hover
```

Use it when the destination should remain clearly recognizable as a Link.

### Subtle

Subtle is the intentional neutral, lower-prominence Link treatment.

```text
link/subtle
link/subtle-hover
```

Use it when surrounding context already communicates navigation, for example:

- dense ATS/product UI;
- navigation;
- card metadata;
- breadcrumb-like destinations;
- contextual “View all” or “Learn more” links.

Do not use Subtle as an unadorned inline body-copy Link. Inline links require a persistent non-color affordance such as underline.

### Inverse

```text
link/inverse
link/inverse-hover
```

Use Inverse only on `surface/inverse` or another reviewed inverse surface.

v4 intentionally has one inverse Link treatment rather than separate Default/Subtle inverse families.

## State and Semantic Token Mapping

| Style | Enabled | Hover | Active | Focus foreground | Focus treatment |
|---|---|---|---|---|---|
| Default | `link/default` | `link/hover` | `link/hover` | `link/default` | shared `focus/default` recipe |
| Subtle | `link/subtle` | `link/subtle-hover` | `link/subtle-hover` | `link/subtle` | shared `focus/default` recipe |
| Inverse | `link/inverse` | `link/inverse-hover` | `link/inverse-hover` | `link/inverse` | shared `focus/inverse` recipe |

There is no Link-specific Active color token in v4. Active deliberately reuses the corresponding Hover semantic token rather than introducing another component-only role.

Focus is independent from Link foreground color. Keyboard focus must remain visibly distinguishable from Enabled, Hover, and Active.

The Figma component uses the shared outer Focus effect recipes; implementation should consume the shared Focus contract rather than reproducing Figma effect values as ad-hoc CSS.

## Underline Behavior

`Underline` describes whether the underline is persistent at rest.

### Underline=False

- Enabled: no underline.
- Hover: underline.
- Active: underline.
- Focus: underline plus the shared focus treatment.

Use this for standalone or contextual links where the surrounding UI already makes the control identifiable as navigation.

### Underline=True

Underline remains visible in Enabled, Hover, Active, and Focus.

Use persistent underline when:

- the Link appears inside running text;
- color alone would not make the Link sufficiently recognizable;
- stronger Link affordance is needed.

For inline body-copy links, persistent underline is the default rule.

## Icons

Icons are optional and must add destination or directional meaning.

- Use logical `Start icon` and `End icon`; do not author physical left/right Link variants.
- Icon size remains `18px` at every Link size.
- Icon-label gap remains `8px`.
- Do not add icons to normal inline sentence links.
- For an external destination, use the current `launch` icon in the logical End slot when an external-destination cue is useful.
- The external-link icon does not by itself define whether the browser opens a new tab.
- Icons are normally decorative when the visible label already communicates the destination; avoid duplicate accessible names.

## Inline and Multiline Authoring

### Runtime behavior

A semantic anchor may wrap naturally when constrained by its containing layout. Do not prevent wrapping globally in the runtime Link implementation.

### Figma authoring boundary

The atomic Figma Link component is optimized for single-line standalone/contextual Links and hugs its content.

Figma does not allow a consumer to override the text node's max-width behavior cleanly inside the current component without introducing an artificial Width axis. v4 therefore does not add a Width variant.

For inline or multiline Link copy in Figma:

1. use a native Text layer;
2. apply the surrounding Body text style;
3. apply the appropriate `link/*` semantic color to the Link range;
4. apply persistent underline to the Link range;
5. preserve native text wrapping.

The Link page Playground contains the canonical native-Text example.

For a long standalone Link that must wrap in a mockup, use the same native-Text recipe rather than detaching the atomic component or adding an ad-hoc width variant.

## Link vs Button

The semantic behavior decides the element type.

### Use Link when

- activation navigates to another page, route, document, or destination;
- the user expects browser Link behavior such as opening the destination from context-menu/browser commands.

### Use Button when

- activation changes state;
- submits or mutates data;
- confirms or cancels an operation;
- opens or controls behavior in the current context.

Button styling does not change the semantic element type. A navigation element may use a reviewed Button visual treatment while remaining an anchor in code.

When a Link visually uses a Button treatment, reuse the Button visual recipe from `button.md`; do not create a parallel `link-button/*` token family.

## Deliberate Exclusions

### Disabled

Disabled is not part of the Link API.

A destination that cannot be navigated to should normally not be presented as an inert Link. Reconsider the information architecture, render non-interactive text, or explain the unavailable destination through the owning pattern rather than creating a disabled-anchor state.

### Visited

`link/visited` is not part of shared v4 because no reviewed product pattern currently requires persistent visited styling.

If a future use case such as visited search results requires it, add it only after pattern-level review rather than through a local component override.

### Bold

Bold is not a Link hierarchy axis. Use the surrounding typography hierarchy and the approved Link semantic roles instead of changing Link weight to create emphasis.

### Legacy Inline axis

The former `Inline=True/False` axis mixed placement semantics with visual styling. v4 replaces it with the explicit `Underline=True/False` visual property and a separate authoring rule for running text.

## RTL

Start and End are logical positions.

```text
LTR: Start · Label · End
RTL: End · Label · Start
```

Do not create separate RTL variants.

Directionality belongs to layout/runtime direction. Icon meaning must remain correct after mirroring or direction changes; directional glyphs should follow the icon-system RTL behavior rather than being manually duplicated inside Link.

## Accessibility and Interaction Contract

- Prefer a native `<a href="…">` for Link behavior.
- Every Link requires an accessible name; normally this is its visible label.
- Preserve expected browser Link behavior.
- Keyboard focus must follow the shared Focus contract and remain visible.
- Do not communicate Link identity through color alone when surrounding context does not already establish clickability.
- Inline body-copy links use a persistent underline.
- Link foreground must meet the applicable text contrast requirement against its current background.
- Focus indication must satisfy the shared focus-appearance contract.
- Standalone Link targets must satisfy the shared target-size/spacing contract; WCAG's inline-text exception applies only to Links that are genuinely inside running text.
- Start/End icons are decorative when the visible label already communicates the destination.
- Do not expose Disabled as a semantic or visual Link state.

## Development Contract

The runtime API should expose semantic authoring inputs equivalent to the Figma contract, but interaction pseudo-states should normally be implemented through the platform/CSS rather than application props.

Expected conceptual API:

```text
Link
- style: default | subtle | inverse
- size: sm | md | lg
- underline: boolean
- startIcon?: icon
- endIcon?: icon
- href / destination
- children / label
```

Implementation requirements:

- native anchor semantics for navigation;
- sizes: Small = 12/16, Medium = 14/20, Large = 16/24;
- text weight: 400;
- icon size: 18px;
- icon-label gap: 8px;
- logical Start/End icon placement;
- default style: Default;
- default size: Medium;
- default underline: false for standalone/contextual Link;
- Hover/Active use the style's hover semantic token;
- Focus keeps the rest foreground and composes the shared focus treatment;
- when `underline=false`, Hover/Active/Focus add underline;
- when `underline=true`, underline remains persistent;
- do not expose `visited`, `disabled`, or `bold` component variants;
- do not force `white-space: nowrap` globally; runtime Links may wrap in constrained layouts;
- do not duplicate semantic Link tokens as component-local colors.

Figma `State` exists to document visual states; code should not require authors to pass `hover`, `active`, or `focus` as public props.

The exact framework class architecture remains a frontend implementation decision until the runtime Design System repository/package is registered.

## QA Checklist

Verify:

- all three Styles resolve to the approved semantic Link tokens;
- Small / Medium / Large use 12/16, 14/20, and 16/24 Regular typography;
- icons remain 18px with an 8px gap at every size;
- Start/End positions work logically in RTL;
- Underline=False adds underline on Hover, Active, and Focus;
- Underline=True remains underlined in every state;
- Focus uses the correct shared default/inverse treatment;
- no Disabled, Visited, Bold, or legacy Inline variants are reintroduced;
- external-link examples use the logical End slot;
- inline body-copy links have a persistent underline;
- native Text inline/multiline authoring preserves wrapping in Figma;
- runtime anchors can wrap naturally;
- keyboard focus is visible;
- standalone targets satisfy the shared target-size/spacing contract;
- navigation semantics remain Link semantics even when a Button visual treatment is used.

## Legacy Migration

Figma retains `Link / Legacy` only for migration.

Map old usage as follows:

```text
Inline=True
→ Underline=True, or native Text when the Link is inside running copy

Bold=True
→ remove; use surrounding typography hierarchy

Visited
→ remove unless a future reviewed pattern explicitly requires it

Disabled
→ remove and revisit the UX / availability model

Icon
→ logical Start Icon or End Icon
```

Do not create new instances of `Link / Legacy`.

## Open Items

Runtime implementation remains unverified until the owning Design System repository/package and Storybook source are registered.

Still requiring frontend/runtime verification:

- exact runtime component/API identifier;
- exact Angular/Tailwind authoring pattern;
- Storybook stable story/docs identifier;
- exact Figma-property → code-prop mapping;
- Code Connect or equivalent mapping mechanism.

These are integration gaps. The Link design, visual state model, Figma API, token mapping, RTL behavior, inline/multiline authoring boundary, and accessibility contract are otherwise verified.

## Live References

- Figma file: `[DS] Job Vision NEXT`
- Figma component set: `Link / Default`
- Figma node ID: `22901:125760`
- Figma component key: `93372073ea1f24b1726354518570da662e021ae5`
- Figma default: `Style=Default, Size=Medium, State=Enabled, Underline=False`
- Figma Playground: same Link page, including Default, Underlined, icon, External, Subtle, Focus/RTL, Inverse, and native Text inline/multiline examples
- Storybook / Code: not yet connected as a canonical live reference

## Related Documents

- `button.md`
- `../accessibility/focus-management.md`
- `../accessibility/pointer-touch-and-gestures.md`
- `../accessibility/color-and-contrast.md`
- `../experience-rules/navigation.md`
- `../integrations/component-mapping.md`
- `../tokens/semantic-tokens.md`
