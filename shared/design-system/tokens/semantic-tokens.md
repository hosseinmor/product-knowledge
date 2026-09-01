---
id: design-system.token.semantic-tokens
collection: design-system
type: token
title: Semantic Tokens
summary: '> Status: draft'
knowledge_state: unverified
document_maturity: draft
related: []
---

# Semantic Tokens

> Status: draft

Semantic tokens are the default Color interface consumed by components. Their role meaning remains stable across Brand modes and Light/Dark themes.

## Resolution

```text
Primitive Value
→ Brand: Jobvision or Cando
→ Semantic: Light or Dark
→ Component
```

This is the Color-token resolution path. Non-color foundations are not required to follow the same graph.

Brand provides product-identity inputs where required. Semantic may also alias generic Primitive hue scales directly when a role does not vary by product. Components do not consume Brand directly.

## Surface

Structural surfaces:

```text
surface/default
surface/muted
surface/inset
surface/raised
surface/inverse
```

Interactive neutral surfaces:

```text
surface/neutral-muted
surface/neutral-muted-hover
surface/neutral-muted-active

surface/neutral-emphasis
surface/neutral-emphasis-hover
surface/neutral-emphasis-active
```

Transparent interaction states:

```text
surface/transparent-hover
surface/transparent-active
surface/transparent-inverse-hover
surface/transparent-inverse-active
```

Persistent neutral selected containers:

```text
surface/selected
surface/selected-hover
```

Brand:

```text
surface/brand
surface/brand-hover
surface/brand-active
```

Accent:

```text
surface/accent-muted
surface/accent-muted-hover
surface/accent-muted-active

surface/accent-emphasis
surface/accent-emphasis-hover
surface/accent-emphasis-active
```

Magic:

```text
surface/magic-muted
surface/magic-emphasis
surface/magic-emphasis-hover
surface/magic-emphasis-active
```

Danger:

```text
surface/danger-muted
surface/danger-emphasis
surface/danger-emphasis-hover
surface/danger-emphasis-active
```

Support:

```text
surface/info-muted
surface/success-muted
surface/warning-muted
surface/error-muted
```

Disabled:

```text
surface/disabled
```

`canvas`, `surface/floating`, the v3 `surface/control*` and `surface/emphasis*` names, `surface/brand-muted`, and the expanded v3 Selected surface matrix are removed in v4.

### Surface meanings

- `surface/default` is the ordinary base content surface and default root page/workspace surface.
- `surface/muted` is passive lower-emphasis structure and has no interaction states.
- `surface/inset` is behind `surface/default` in the local hierarchy and may represent recessed regions, workspace chrome, or structural backdrops.
- `surface/raised` is elevated relative to its parent and includes menus, popovers, dropdowns, floating panels, and appropriate dialogs. Elevation/shadow remains separate.
- `surface/neutral-muted` is a visible neutral interactive treatment; it is not interchangeable with structural `surface/muted`.
- `surface/neutral-emphasis` is the strong neutral interactive treatment used by operational Primary actions.
- `surface/selected` is specifically a neutral persistent selected-container background, not a general Selected color family.
- `surface/selected-hover` is only for selected containers that **remain interactive while selected**, such as a selected menu/list/tree/navigation item. It is not a universal selected state. A selected Tab that no longer has an interaction on the selected item does not need selected-hover styling.
- `surface/brand` is reserved for product identity and approved key product/conversion moments.
- Accent communicates chromatic interaction/affordance and may be used by component selection states when a colored cue is appropriate.
- `surface/accent-muted*` is the tonal interactive Accent treatment for patterns such as applied filters, selected tonal chips, and actionable/promotional banners where the reason for the color is interaction or emphasis rather than system feedback.
- Magic surfaces are reserved for AI-assisted/generated experiences. Typical uses include AI entry cards, AI sections, AI chips, and AI actions when the treatment is explicitly communicating the AI capability.
- `surface/danger-muted` is for destructive-intent callouts or pre-action warning regions. It does not represent a system error.

The `bg-*` and `fill-*` families remain deprecated.

## Foreground

Use `fg/*` for text and icons.

General hierarchy and input roles:

```text
fg/primary
fg/secondary
fg/tertiary
fg/placeholder
fg/disabled
```

Role boundaries:

- `fg/primary`: essential/default readable content, such as primary titles, body content, input values, menu-item labels, and the main readable content of a component.
- `fg/secondary`: supporting readable content that contributes to understanding, such as supporting descriptions, field labels, company/location context, and helper text when no dedicated semantic requirement exists.
- `fg/tertiary`: auxiliary low-priority metadata that may visually recede during scanning, such as timestamps, passive counts, character counters, and other non-essential metadata. Do not use it merely to make arbitrary text lighter.
- `fg/placeholder`: placeholder content in input-like controls.
- `fg/disabled`: unavailable control/content styling. Disabled is not a substitute for read-only styling.

Contextual foregrounds:

```text
fg/on-inverse
fg/on-brand
fg/on-color
```

Colored semantics:

```text
fg/accent
fg/magic
fg/danger

fg/info
fg/success
fg/warning
fg/error
```

Colored Support content on inverse surfaces:

```text
fg/info-inverse
fg/success-inverse
fg/warning-inverse
fg/error-inverse
```

`fg/brand`, `fg/selected`, and `fg/on-color-disabled` are not part of v4. Disabled filled controls suppress tone and use `surface/disabled + fg/disabled`.

## Line

```text
line/muted
line/default
line/emphasis
line/disabled
line/inverse

line/accent
line/magic
line/danger

line/info
line/success
line/warning
line/error
```

Neutral line roles:

- `line/muted`: subtle structural separation such as low-emphasis dividers.
- `line/default`: normal control/container boundary.
- `line/emphasis`: stronger neutral interactive boundary when a control needs additional prominence, for example a Text Input hover/focus border when the focus ring remains a separate `focus/*` treatment.
- `line/disabled`: boundary of a disabled control.
- `line/inverse`: neutral boundary on an inverse surface.

Use `line/accent` for chromatic indicators such as the selected indicator of a line Tab when the component calls for an Accent cue. `line/brand` and `line/selected` are removed.

Keep `line` rather than `border` as the source-token family to avoid collision with implementation utility naming.

## Selection

Selection is a component state rather than a parallel global color family.

A selected/current/checked/on/applied component may express its state with existing Semantic roles according to anatomy:

```text
selected line Tab → fg/primary + line/accent
checked checkbox  → surface/accent-emphasis + fg/on-color
saved bookmark    → fg/accent
selected row      → surface/selected + fg/primary
applied filter    → surface/accent-muted* + appropriate foreground/line
```

Only persistent neutral selected-container backgrounds receive dedicated global tokens: `surface/selected` and, when that selected container remains interactive, `surface/selected-hover`.

Do not infer a selected-hover state for components whose selected item is not interactive, such as a current Tab when activating it again has no meaningful action.

## Brand and Accent

Brand and Accent are separate semantics even when JobVision maps both to the same Blue Primitive family.

```text
Brand  → identity + approved key conversion moments
Accent → chromatic interaction / affordance
```

Cando demonstrates the distinction clearly: Brand resolves to Yellow while Accent resolves to Blue.

An actionable Accent banner or applied filter may use Accent Muted. A passive informational/system message uses Support Info instead. The distinction is meaning, not merely the fact that both may appear blue.

## Magic

Magic communicates an AI-assisted, AI-generated, or explicitly magical product capability. It is a shared Semantic family because the same AI meaning may appear across multiple component types, including cards/sections, chips/labels, icons, outlines, and actions.

```text
surface/magic-muted
→ subtle AI container/chip/section treatment

surface/magic-emphasis*
→ strong interactive AI action or entry point

fg/magic
→ AI icon, label, or inline emphasis

line/magic
→ AI-specific outline or indicator when the anatomy needs a line
```

Magic must not be used merely because purple is visually attractive and must not replace Brand, Accent, Selected, or Support semantics.

## Danger and Error

Danger and Error may share the Red Primitive family while representing different meanings:

```text
Danger → destructive intent/action
Error  → validation failure or system/problem state
```

Examples:

```text
“This action permanently deletes the job.”
→ Danger

“Saving failed. Try again.”
→ Error
```

Danger is not a fifth standard Notification severity. Standard system feedback remains Info / Success / Warning / Error. Use Danger for destructive actions and destructive-intent callouts, including `surface/danger-muted` where a pre-action warning region is required.

## Support

Information, success, warning, and error meanings are invariant across products and themes.

Only muted Support surfaces are approved globally. The baseline inline-notification recipe can use:

```text
surface/{severity}-muted
fg/{severity}          # status icon/content
line/{severity}        # only when the notification anatomy uses a semantic border
fg/primary             # title/main readable content
fg/secondary           # supporting description
```

The inverse Support foregrounds are intentionally narrow. Use them for colored Support content on `surface/inverse`, such as the status icon/text of an inverse Toast:

```text
surface/inverse
fg/on-inverse
fg/{info|success|warning|error}-inverse
```

Their existence does not imply Support inverse surfaces or inverse line families.

## Focus

```text
focus/default
focus/inverse
```

Focus remains independent from Brand and Accent and must remain visible across supported products, themes, and surfaces.

## Link

```text
link/default
link/hover

link/subtle
link/subtle-hover

link/inverse
link/inverse-hover
```

- Default is the recognizable chromatic link.
- Subtle is the intentional neutral lower-prominence link for contexts where clickability is already clear.
- Inverse adapts Link for `surface/inverse`; one inverse treatment is approved in v4.
- Link remains an independent semantic family even when it resolves to the same Blue Primitive family as Accent.

`link/visited`, `link/emphasis`, and `link/emphasis-hover` are removed in v4. Visited may return only when a real product pattern requires it.

## Utility roles

```text
overlay/default
skeleton/base
skeleton/shimmer
```

`overlay/default` is a backdrop/scrim role, not a Surface.

The previous `highlight/default` and `highlight/inverse` proposals are removed. A future text/search highlighting pattern must establish a concrete semantic contract before shared Highlight tokens are introduced.

## Component-owned exception

Categorical Tag colors are component-owned rather than Semantic. Use the approved `tag/surface/*`, `tag/fg/*`, and `tag/line/*` families documented in `component-tokens.md`. They communicate grouping, not information, success, warning, or error.

The Tag family is retained for now; its exact variant/state matrix should be validated when the Tag component is reviewed rather than expanded by convention.

## Source of truth

`jobvision-color-tokens-v4-surface-model.md` is the canonical v4 Color-token catalog and defines shared token meaning, deprecations, and open implementation decisions.

Component recipe ownership remains with the corresponding component guideline. In particular, `../components/button.md` is the canonical owner of Button presets, states, and Semantic-token mappings; the v4 Color catalog may summarize Button mapping only as an integration example.

Mode-by-mode alias targets and unresolved values are recorded in `color-token-aliases.md`.
