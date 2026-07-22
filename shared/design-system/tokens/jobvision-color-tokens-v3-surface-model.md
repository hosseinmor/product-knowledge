# Jobvision Color Tokens v3 — Surface Model

> Status: Working draft  
> Theme scope: Light + Dark  
> Implementation target: Tailwind CSS v3  
> CSS variables: Open decision  
> Product variation: Brand override only  
> Experience variation: Productive / Expressive

## Architecture

```text
Primitives
→ Brand
→ Experience
→ Semantic
→ Component
```

Collections and modes:

```text
01 Primitives
- Value

02 Brand
- Jobvision
- Cando

03 Experience
- Productive
- Expressive

04 Semantic
- Light
- Dark

05 Component
- Light
- Dark
```

Components consume Semantic tokens by default. Approved component-specific families, currently Tag, are exposed through Component tokens.

The complete mode-by-mode value graph is defined in `color-token-aliases.md`. This catalog remains the source of truth for token meaning and usage.

---

## Naming decision

All UI backgrounds above `canvas` use the unified `surface-*` family.

Deprecated:

```text
bg-*
fill-*
```

Current:

```text
canvas
surface-*
```

`canvas` remains unprefixed because it is the root page or workspace background.

---

## Primitives

Primitive variables contain raw values only:

```text
color/neutral/*
color/blue/*
color/purple/*
color/red/*
color/green/*
color/emerald/*
color/orange/*
color/yellow/*
color/black-alpha/*
color/white-alpha/*
color/brand/jobvision/*
color/brand/cando/*
```

Rules:

- One mode: `Value`
- Direct values only
- No Light/Dark roles
- No Productive/Expressive roles
- No semantic UI roles

---

## Brand

Modes:

```text
Jobvision
Cando
```

Initial variables:

```text
accent/50
accent/100
accent/200
accent/300
accent/400
accent/500
accent/600
accent/700
accent/800
accent/900
accent/950

content/on-accent
```

All Brand values alias Primitive variables.

Example:

```text
Brand/accent/500

Jobvision → Primitives/color/brand/jobvision/500
Cando     → Primitives/color/brand/cando/500
```

```text
Brand/content/on-accent

Jobvision → Primitives/color/neutral/0
Cando     → Primitives/color/neutral/950
```

No Brand-level `focus` variable is currently defined. Focus remains Semantic and brand-independent until a real brand-specific treatment is approved.

Do not put these in Brand:

```text
surface-brand-emphasis
fg-on-brand
line-brand
canvas
selected
```

---

## Experience

Modes:

```text
Productive
Expressive
```

### Productive

For focused, operational, repetitive, management-oriented experiences such as employer panels, ATS, onboarding, and workflow-heavy tools.

### Expressive

For discovery, browsing, editorial, marketing, and visually prominent experiences such as jobseeker, job pages, company pages, and landing pages.

Initial variables:

```text
canvas/light
canvas/dark
```

Example mappings:

```text
Experience/canvas/light

Productive → Primitives/color/neutral/50
Expressive → Primitives/color/neutral/0
```

```text
Experience/canvas/dark

Productive → Primitives/color/neutral/950
Expressive → Primitives/color/neutral/900
```

These are the current Experience alias mappings. The complete resolution graph is defined in `color-token-aliases.md`.

In the current version, Experience controls environment-level surface decisions such as canvas. It may later expand to typography strategy, density, layout rhythm, or selected component treatments.

---

## Semantic

Modes:

```text
Light
Dark
```

### Canvas

```text
canvas

Light → Experience/canvas/light
Dark  → Experience/canvas/dark
```

Use for root page or workspace background only.

---

## Unified surface family

### Base surfaces

```text
surface-default
surface-inset
surface-muted
surface-inverse
```

- `surface-default`: normal container, card, panel, sheet, modal, or popover
- `surface-inset`: nested recessed region
- `surface-muted`: passive supporting or grouping region
- `surface-inverse`: high-contrast inverted region

`surface-muted` is non-interactive and has no hover or active states.

### Interactive neutral surface

```text
surface-control
surface-control-hover
surface-control-active
```

Use for neutral controls with a visible background at rest, including Secondary Button, neutral filled Icon Button, Filter Chip, and Segmented Control.

### Neutral emphasis surface

```text
surface-emphasis
surface-emphasis-hover
surface-emphasis-active
```

Use for high-emphasis neutral actions such as Primary Button.

Foreground:

```text
fg-on-emphasis
```

### Transparent interaction states

```text
surface-transparent-hover
surface-transparent-active
```

Use when rest is transparent, such as Tertiary, Ghost, toolbar actions, and lightweight icon controls.

### Brand surfaces

```text
surface-brand-muted
surface-brand-emphasis
surface-brand-emphasis-hover
surface-brand-emphasis-active
```

Example:

```text
surface-brand-emphasis
Light → Brand/accent/600
Dark  → Brand/accent/600
```

Foreground:

```text
fg-on-brand → Brand/content/on-accent
```

### Selected surfaces

```text
surface-selected-muted
surface-selected-muted-hover
surface-selected-muted-active

surface-selected-emphasis
surface-selected-emphasis-hover
surface-selected-emphasis-active
```

Foreground:

```text
fg-on-selected
```

Brand and selected remain separate semantic roles.

### Disabled surface

```text
surface-disabled
```

Disabled state has no hover or active state.

### Danger surfaces

```text
surface-danger-muted
surface-danger-emphasis
surface-danger-emphasis-hover
surface-danger-emphasis-active
```

Danger is for destructive actions. Error is for validation or system conditions.

### Support surfaces

```text
surface-info
surface-success
surface-warning
surface-error
```

Matching roles:

```text
fg-info
fg-success
fg-warning
fg-error

line-info
line-success
line-warning
line-error
```

---

## Foreground

```text
fg-primary
fg-secondary
fg-subtle
fg-disabled
fg-inverse

fg-brand
fg-on-brand
fg-on-emphasis
fg-on-selected

fg-danger
fg-info
fg-success
fg-warning
fg-error
```

Rules:

- `fg-on-brand` is brand-dependent.
- Cando may use a dark foreground on yellow brand surfaces.
- `fg-on-selected` remains separate from `fg-on-brand`.

Deprecated:

```text
fg-on-fill
fg-on-primary
```

---

## Line

```text
line-subtle
line-default
line-strong
line-disabled

line-brand
line-selected
line-danger

line-info
line-success
line-warning
line-error
```

Use `line-*` instead of `border-*` to avoid conflict with Tailwind utilities.

---

## Focus

```text
focus-default
focus-inverse
```

Rules:

- Independent from component tone
- Visible across supported surfaces
- Cando yellow must not be the sole focus indicator
- Dual-layer media focus remains an open decision

Deprecated:

```text
focus
focus-ring
```

---

## Component tokens

Modes:

```text
Light
Dark
```

Component tokens are exceptional, component-owned roles. They may alias Semantic tokens or, when no shared semantic role exists, approved Primitive tokens. Components continue to use Semantic tokens unless an approved component family is documented here and in `component-tokens.md`.

### Tag

Tag colors communicate grouping or categorization, not feedback status. The approved variants are:

```text
neutral
blue
purple
green
orange
```

Each variant provides:

```text
tag-surface-{variant}
tag-surface-{variant}-hover
tag-fg-{variant}
tag-line-{variant}
```

Example:

```text
tag-surface-blue
tag-surface-blue-hover
tag-fg-blue
tag-line-blue
```

Figma variables use slash grouping inside the `05 Component` collection:

```text
tag/surface/blue
tag/surface/blue-hover
tag/fg/blue
tag/line/blue
```

The flattened code names remain `tag-surface-blue`, `tag-surface-blue-hover`, `tag-fg-blue`, and `tag-line-blue`.

Current Light mappings, carried forward from the v2 categorical family:

| Variant | Surface | Hover | Foreground | Line |
|---|---|---|---|---|
| Neutral | `color/neutral/100` | `color/neutral/200` | `color/neutral/700` | `color/neutral/200` |
| Blue | `color/blue/50` | `color/blue/100` | `color/blue/700` | `color/blue/200` |
| Purple | `color/purple/50` | `color/purple/100` | `color/purple/700` | `color/purple/200` |
| Green | `color/emerald/50` | `color/emerald/100` | `color/emerald/700` | `color/emerald/200` |
| Orange | `color/orange/50` | `color/orange/100` | `color/orange/700` | `color/orange/200` |

Rules:

- Only interactive Tags use `tag-surface-{variant}-hover`.
- Static Tags, labels, and metadata markers do not show hover treatment.
- Tag colors must not communicate information, success, warning, or error. Use the matching Semantic support tokens for feedback status.
- Tag tokens are owned by the Tag component and must not be reused as a general categorical palette by unrelated components.
- Light and Dark alias mappings are defined in `color-token-aliases.md`.

---

## Button mapping

| Preset | Rest | Hover | Active | Foreground |
|---|---|---|---|---|
| Accent | `surface-brand-emphasis` | `surface-brand-emphasis-hover` | `surface-brand-emphasis-active` | `fg-on-brand` |
| Primary | `surface-emphasis` | `surface-emphasis-hover` | `surface-emphasis-active` | `fg-on-emphasis` |
| Secondary | `surface-control` | `surface-control-hover` | `surface-control-active` | `fg-primary` |
| Danger Filled | `surface-danger-emphasis` | `surface-danger-emphasis-hover` | `surface-danger-emphasis-active` | `fg-on-emphasis` |

| Preset | Rest | Hover | Active | Foreground | Line |
|---|---|---|---|---|---|
| Tertiary | transparent | `surface-transparent-hover` | `surface-transparent-active` | `fg-primary` | `line-default` |
| Danger Outline | transparent | `surface-transparent-hover` | `surface-transparent-active` | `fg-danger` | `line-danger` |

| Preset | Rest | Hover | Active | Foreground |
|---|---|---|---|---|
| Ghost | transparent | `surface-transparent-hover` | `surface-transparent-active` | `fg-primary` |
| Danger Ghost | transparent | `surface-transparent-hover` | `surface-transparent-active` | `fg-danger` |

Disabled:

```text
Filled  → surface-disabled + fg-disabled
Outline → transparent + fg-disabled + line-disabled
Ghost   → transparent + fg-disabled
```

---

## Deprecated token mapping

```text
bg-*                    → surface-* or canvas
fill-brand              → surface-brand-emphasis
fill-primary            → surface-emphasis
fill-secondary          → surface-control
fill-danger             → surface-danger-emphasis
fill-disabled           → surface-disabled

surface-hover           → surface-transparent-hover
surface-active          → surface-transparent-active
surface-muted-hover     → surface-control-hover
surface-muted-active    → surface-control-active

fg-on-primary           → fg-on-emphasis
fg-on-fill              → role-specific foreground

focus                   → focus-default
```

---

## Figma application examples

```text
Jobvision public page
Brand      → Jobvision
Experience → Expressive
Semantic   → Light
```

```text
Jobvision employer panel
Brand      → Jobvision
Experience → Productive
Semantic   → Light
```

```text
Cando ATS
Brand      → Cando
Experience → Productive
Semantic   → Light or Dark
```

---

## Open decisions

1. Final opaque Primitive scale values
2. CSS variables adoption
3. Tailwind v3 implementation mapping
4. Dual-layer focus treatment for media
5. Whether Experience expands beyond canvas in the first implementation
6. Whether inverse surfaces require shared hover and active roles
7. Accessibility approval of the current alias mappings before promotion from working draft to stable
