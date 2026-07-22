# Jobvision Design System — Color Tokens v2

Status: Working draft  
Model: **Target-first semantic tokens with explicit background prominence**  
Scope: Jobvision candidate experience, Jobvision employer panel, HRCanDo / Kando modules.

---

## 1. Architecture

This version has no separate component-token layer. Tokens are named by visual target, semantic role, optional prominence, and optional interaction state:

```txt
[target]-[role]-[prominence]-[state]
```

Not every token needs every segment. Add a segment only when it communicates a real distinction.

Examples:

```txt
bg-default
bg-muted
bg-muted-hover
bg-brand-muted
bg-brand-emphasis
bg-brand-emphasis-hover
fg-primary
line-error
link-neutral-hover
```

State is always the final segment. Only create a state token when that state has a real shared treatment in the product.

### 1.1 Targets

| Target | Use |
|---|---|
| `bg` | Any background color, from structural surfaces to solid action and status treatments |
| `fg` | Foreground color for text, icons, and `currentColor` SVGs |
| `line` | Border, divider, separator, and accent line |
| `link` | Navigational text color |
| `focus` | Focus indicator color |

`surface` and `fill` are not separate targets in this model. Their former distinction is expressed by background prominence:

```txt
surface-[role] → bg-[role]-muted
fill-[role]    → bg-[role]-emphasis
```

### 1.2 Background prominence

| Modifier | Meaning |
|---|---|
| `default` | The ordinary reference background, without intentional reduction or increase in emphasis |
| `muted` | A low-emphasis background that provides context and normally uses a regular or semantic foreground |
| `emphasis` | A solid, attention-carrying background that normally requires an `fg-on-*` foreground |

Prominence is relative to the same target and role. It is not defined by physical size, component type, lightness, or a fixed primitive step.

Do not create all three modifiers mechanically. A role only receives the levels that have distinct, documented uses.

### 1.3 Neutral foreground hierarchy

Neutral foreground tokens express content hierarchy, not color intensity:

| Token | Use |
|---|---|
| `fg-primary` | Essential content, primary values, labels, and actionable icons |
| `fg-secondary` | Supporting information that improves understanding but is not the main focus |
| `fg-tertiary` | Optional metadata and details that may be skipped on the first scan |

Select the level by content importance, not font size, component type, or a specific primitive value.

- Use `fg-primary` when missing the content would harm understanding or task completion.
- Use `fg-secondary` when the content supports the primary information but is not essential to the main task.
- Use `fg-tertiary` when the content is optional metadata, such as a timestamp or low-priority caption.
- Do not use `fg-tertiary` for body text, form labels, button labels, essential links, errors, or warnings.
- Placeholder, disabled, inverse, semantic, and on-emphasis content use their dedicated tokens.

The hierarchy must remain perceptible in every mode:

```txt
fg-primary > fg-secondary > fg-tertiary
```

### 1.4 Neutral default

When a background token has no semantic role, it is neutral by default:

```txt
bg-muted
bg-emphasis
```

Do not add a redundant `neutral` segment:

```txt
bg-neutral-muted       /* avoid */
bg-neutral-emphasis    /* avoid */
```

Role is included only when it communicates an independent meaning:

```txt
bg-brand-muted
bg-error-emphasis
bg-selected-muted
```

---

## 2. Token catalog

### 2.1 Background — structural and neutral

| Token | Usage |
|---|---|
| `bg-canvas` | Page or workspace background |
| `bg-default` | Default container, card, or panel background |
| `bg-muted` | Quiet neutral treatment, including a subtle gray control |
| `bg-muted-hover` | Hover state for an element whose rest background is `bg-muted` |
| `bg-muted-active` | Active state for an element whose rest background is `bg-muted` |
| `bg-emphasis` | High-emphasis neutral background, primarily the dark workhorse action |
| `bg-emphasis-hover` | Hover state of `bg-emphasis` |
| `bg-emphasis-active` | Active state of `bg-emphasis` |
| `bg-raised` | Surface intended to lift above its parent; pair with elevation when required |
| `bg-inset` | Recessed or nested area inside a background |
| `bg-transparent-hover` | Hover overlay for an element that is transparent at rest |
| `bg-transparent-active` | Active overlay for an element that is transparent at rest |
| `bg-disabled` | Background for disabled controls |
| `bg-readonly` | Background for read-only fields |
| `bg-inverse` | Inverse background such as a tooltip or dark banner |
| `bg-inverse-muted` | Quieter inverse background |
| `bg-inverse-hover` | Hover treatment on an inverse background |
| `bg-inverse-active` | Active treatment on an inverse background |

### 2.2 Background — selected

| Token | Usage |
|---|---|
| `bg-selected-muted` | Low-emphasis selected item, such as a selected chip or row |
| `bg-selected-muted-hover` | Hover on a low-emphasis selected item |
| `bg-selected-muted-active` | Active state of a low-emphasis selected item |
| `bg-selected-emphasis` | Strong on/checked state, such as a checkbox, radio, or toggle |

Selected treatments are neutral by default in v2 unless a product pattern documents a semantic or categorical reason to use color.

### 2.3 Background — brand, magic, and feedback

| Role | Muted | Emphasis | Interaction states |
|---|---|---|---|
| Brand | `bg-brand-muted` | `bg-brand-emphasis` | `bg-brand-emphasis-hover`, `bg-brand-emphasis-active` |
| Magic | `bg-magic-muted` | `bg-magic-emphasis` | `bg-magic-emphasis-hover`, `bg-magic-emphasis-active` |
| Info | `bg-info-muted` | `bg-info-emphasis` | — |
| Success | `bg-success-muted` | `bg-success-emphasis` | — |
| Warning | `bg-warning-muted` | `bg-warning-emphasis` | — |
| Error | `bg-error-muted` | `bg-error-emphasis` | — |
| Danger | — | `bg-danger-emphasis` | `bg-danger-emphasis-hover`, `bg-danger-emphasis-active` |

`error` communicates a system or validation condition. `danger` communicates a destructive action. They may currently share primitive values but remain separate semantic roles.

Feedback emphasis tokens without interaction states are intended for static badges and indicators. Do not invent hover or active variants until a shared interactive use exists.

### 2.4 Foreground

| Token | Usage |
|---|---|
| `fg-primary` | Essential neutral text and icons |
| `fg-secondary` | Supporting neutral text and icons |
| `fg-tertiary` | Optional metadata and low-priority details |
| `fg-placeholder` | Input placeholder |
| `fg-disabled` | Text and icons on disabled controls |
| `fg-inverse` | Text and icons on `bg-inverse` |
| `fg-on-emphasis` | Shared light foreground on dark chromatic emphasis backgrounds |
| `fg-on-selected` | Foreground on `bg-selected-emphasis` |
| `fg-on-brand` | Foreground on `bg-brand-emphasis`; may be overridden independently per brand |
| `fg-on-warning` | Fixed dark foreground on the light warning emphasis background |
| `fg-brand` | Brand-colored text or icon on a light background |
| `fg-magic` | AI-related text or icon |
| `fg-info` | Informational text or icon |
| `fg-success` | Success text or icon |
| `fg-warning` | Warning text or icon |
| `fg-error` | Error or validation text/icon |
| `fg-danger` | Destructive-action text/icon |

Neutral `bg-emphasis` uses `fg-on-emphasis` unless a future theme requires an independently overridable neutral pairing. `bg-brand-emphasis`, `bg-selected-emphasis`, and `bg-warning-emphasis` retain dedicated foregrounds because their contrast behavior may diverge.

### 2.5 Line

| Token | Usage |
|---|---|
| `line-muted` | Quiet divider or hairline |
| `line-default` | Default border for cards, fields, and containers |
| `line-emphasis` | Emphasized border, separator, or indicator |
| `line-disabled` | Border for disabled controls |
| `line-selected` | Selected border or indicator |
| `line-inverse` | Border on inverse backgrounds |
| `line-brand` | Brand accent line |
| `line-magic` | AI-related accent line |
| `line-info` | Informational border or accent |
| `line-success` | Success border or accent |
| `line-warning` | Warning border or accent |
| `line-error` | Error border or accent |
| `line-danger` | Border in a destructive-action context |

### 2.6 Link

| Token | Usage |
|---|---|
| `link-default` | Standard recognizable link color |
| `link-default-hover` | Hover state of the standard link |
| `link-neutral` | Neutral link whose affordance comes from underline or context |
| `link-neutral-hover` | Hover state of the neutral link |
| `link-inverse` | Link on an inverse background |
| `link-inverse-hover` | Hover state of an inverse link |

Use `fg-*` for static text and icons. Use `link-*` for navigational text actions.

### 2.7 Focus and miscellaneous

| Token | Usage |
|---|---|
| `focus-default` | Brand-independent default focus ring |
| `focus-inverse` | Focus ring on inverse backgrounds |
| `overlay` | Scrim behind modal or menu layers |
| `scrim` | Darker scrim treatment |
| `skeleton-default` | Default loading skeleton block |
| `skeleton-muted` | Quieter or nested loading skeleton block |

### 2.8 Categorical colors

Categorical tokens are reusable across tags, chips, labels, filters, and metadata markers. They communicate grouping, not feedback status.

Available variants:

```txt
neutral
blue
purple
green
orange
```

Each variant provides:

```txt
bg-categorical-{variant}
bg-categorical-{variant}-hover
fg-categorical-{variant}
line-categorical-{variant}
```

Example:

```txt
bg-categorical-blue
bg-categorical-blue-hover
fg-categorical-blue
line-categorical-blue
```

Only interactive categorical elements use the hover token. Static tags and labels must not show a hover treatment.

---

## 3. Source CSS tokens

```css
:root {
  /* Background — structural and neutral */
  --bg-canvas: var(--color-neutral-50);
  --bg-default: #ffffff;

  --bg-muted: var(--color-neutral-100);
  --bg-muted-hover: var(--color-neutral-200);
  --bg-muted-active: var(--color-neutral-300);

  --bg-emphasis: var(--color-neutral-950);
  --bg-emphasis-hover: var(--color-neutral-800);
  --bg-emphasis-active: var(--color-neutral-700);

  --bg-raised: #ffffff;
  --bg-inset: var(--color-neutral-100);
  --bg-transparent-hover: rgb(0 0 0 / 0.04);
  --bg-transparent-active: rgb(0 0 0 / 0.08);

  --bg-disabled: var(--color-neutral-100);
  --bg-readonly: var(--color-neutral-50);

  --bg-inverse: var(--color-neutral-950);
  --bg-inverse-muted: var(--color-neutral-900);
  --bg-inverse-hover: rgb(255 255 255 / 0.08);
  --bg-inverse-active: rgb(255 255 255 / 0.12);

  /* Background — selected */
  --bg-selected-muted: var(--color-neutral-100);
  --bg-selected-muted-hover: var(--color-neutral-200);
  --bg-selected-muted-active: var(--color-neutral-300);
  --bg-selected-emphasis: var(--color-neutral-950);

  /* Background — brand, magic, and feedback */
  --bg-brand-muted: var(--color-brand-50);
  --bg-brand-emphasis: var(--color-brand-600);
  --bg-brand-emphasis-hover: var(--color-brand-700);
  --bg-brand-emphasis-active: var(--color-brand-800);

  --bg-magic-muted: var(--color-violet-50);
  --bg-magic-emphasis: var(--color-violet-600);
  --bg-magic-emphasis-hover: var(--color-violet-700);
  --bg-magic-emphasis-active: var(--color-violet-800);

  --bg-info-muted: var(--color-sky-50);
  --bg-info-emphasis: var(--color-sky-600);
  --bg-success-muted: var(--color-emerald-50);
  --bg-success-emphasis: var(--color-emerald-600);
  --bg-warning-muted: var(--color-amber-50);
  --bg-warning-emphasis: var(--color-amber-500);
  --bg-error-muted: var(--color-red-50);
  --bg-error-emphasis: var(--color-red-600);

  --bg-danger-emphasis: var(--color-red-600);
  --bg-danger-emphasis-hover: var(--color-red-700);
  --bg-danger-emphasis-active: var(--color-red-800);

  /* Foreground */
  --fg-primary: var(--color-neutral-950);
  --fg-secondary: var(--color-neutral-700);
  --fg-tertiary: var(--color-neutral-500);
  --fg-placeholder: var(--color-neutral-400);
  --fg-disabled: var(--color-neutral-400);
  --fg-inverse: #ffffff;

  --fg-on-emphasis: #ffffff;
  --fg-on-selected: #ffffff;
  --fg-on-brand: #ffffff;
  --fg-on-warning: var(--color-neutral-950);

  --fg-brand: var(--color-brand-600);
  --fg-magic: var(--color-violet-700);
  --fg-info: var(--color-sky-700);
  --fg-success: var(--color-emerald-700);
  --fg-warning: var(--color-amber-700);
  --fg-error: var(--color-red-700);
  --fg-danger: var(--color-red-700);

  /* Line */
  --line-muted: var(--color-neutral-200);
  --line-default: var(--color-neutral-300);
  --line-emphasis: var(--color-neutral-400);
  --line-disabled: var(--color-neutral-200);
  --line-selected: var(--color-neutral-950);
  --line-inverse: rgb(255 255 255 / 0.18);

  --line-brand: var(--color-brand-300);
  --line-magic: var(--color-violet-200);
  --line-info: var(--color-sky-300);
  --line-success: var(--color-emerald-300);
  --line-warning: var(--color-amber-300);
  --line-error: var(--color-red-300);
  --line-danger: var(--color-red-300);

  /* Link */
  --link-default: var(--color-blue-600);
  --link-default-hover: var(--color-blue-700);
  --link-neutral: var(--fg-primary);
  --link-neutral-hover: var(--fg-secondary);
  --link-inverse: var(--color-blue-300);
  --link-inverse-hover: var(--color-blue-200);

  /* Focus and miscellaneous */
  --focus-default: var(--color-neutral-950);
  --focus-inverse: #ffffff;
  --overlay: rgb(0 0 0 / 0.48);
  --scrim: rgb(0 0 0 / 0.64);
  --skeleton-default: var(--color-neutral-200);
  --skeleton-muted: var(--color-neutral-100);

  /* Categorical */
  --bg-categorical-neutral: var(--color-neutral-100);
  --bg-categorical-neutral-hover: var(--color-neutral-200);
  --fg-categorical-neutral: var(--color-neutral-700);
  --line-categorical-neutral: var(--color-neutral-200);

  --bg-categorical-blue: var(--color-blue-50);
  --bg-categorical-blue-hover: var(--color-blue-100);
  --fg-categorical-blue: var(--color-blue-700);
  --line-categorical-blue: var(--color-blue-200);

  --bg-categorical-purple: var(--color-purple-50);
  --bg-categorical-purple-hover: var(--color-purple-100);
  --fg-categorical-purple: var(--color-purple-700);
  --line-categorical-purple: var(--color-purple-200);

  --bg-categorical-green: var(--color-emerald-50);
  --bg-categorical-green-hover: var(--color-emerald-100);
  --fg-categorical-green: var(--color-emerald-700);
  --line-categorical-green: var(--color-emerald-200);

  --bg-categorical-orange: var(--color-orange-50);
  --bg-categorical-orange-hover: var(--color-orange-100);
  --fg-categorical-orange: var(--color-orange-700);
  --line-categorical-orange: var(--color-orange-200);
}
```

---

## 4. Tailwind v4 mapping

Source tokens keep their target prefix. This produces slightly longer but unambiguous utilities such as `text-fg-primary` and `border-line-default`.

```css
@theme inline {
  --color-bg-canvas: var(--bg-canvas);
  --color-bg-default: var(--bg-default);
  --color-bg-muted: var(--bg-muted);
  --color-bg-muted-hover: var(--bg-muted-hover);
  --color-bg-muted-active: var(--bg-muted-active);
  --color-bg-emphasis: var(--bg-emphasis);
  --color-bg-emphasis-hover: var(--bg-emphasis-hover);
  --color-bg-emphasis-active: var(--bg-emphasis-active);
  --color-bg-raised: var(--bg-raised);
  --color-bg-inset: var(--bg-inset);
  --color-bg-transparent-hover: var(--bg-transparent-hover);
  --color-bg-transparent-active: var(--bg-transparent-active);
  --color-bg-disabled: var(--bg-disabled);
  --color-bg-readonly: var(--bg-readonly);
  --color-bg-inverse: var(--bg-inverse);
  --color-bg-inverse-muted: var(--bg-inverse-muted);
  --color-bg-inverse-hover: var(--bg-inverse-hover);
  --color-bg-inverse-active: var(--bg-inverse-active);

  --color-bg-selected-muted: var(--bg-selected-muted);
  --color-bg-selected-muted-hover: var(--bg-selected-muted-hover);
  --color-bg-selected-muted-active: var(--bg-selected-muted-active);
  --color-bg-selected-emphasis: var(--bg-selected-emphasis);

  --color-bg-brand-muted: var(--bg-brand-muted);
  --color-bg-brand-emphasis: var(--bg-brand-emphasis);
  --color-bg-brand-emphasis-hover: var(--bg-brand-emphasis-hover);
  --color-bg-brand-emphasis-active: var(--bg-brand-emphasis-active);
  --color-bg-magic-muted: var(--bg-magic-muted);
  --color-bg-magic-emphasis: var(--bg-magic-emphasis);
  --color-bg-magic-emphasis-hover: var(--bg-magic-emphasis-hover);
  --color-bg-magic-emphasis-active: var(--bg-magic-emphasis-active);
  --color-bg-info-muted: var(--bg-info-muted);
  --color-bg-info-emphasis: var(--bg-info-emphasis);
  --color-bg-success-muted: var(--bg-success-muted);
  --color-bg-success-emphasis: var(--bg-success-emphasis);
  --color-bg-warning-muted: var(--bg-warning-muted);
  --color-bg-warning-emphasis: var(--bg-warning-emphasis);
  --color-bg-error-muted: var(--bg-error-muted);
  --color-bg-error-emphasis: var(--bg-error-emphasis);
  --color-bg-danger-emphasis: var(--bg-danger-emphasis);
  --color-bg-danger-emphasis-hover: var(--bg-danger-emphasis-hover);
  --color-bg-danger-emphasis-active: var(--bg-danger-emphasis-active);

  --color-fg-primary: var(--fg-primary);
  --color-fg-secondary: var(--fg-secondary);
  --color-fg-tertiary: var(--fg-tertiary);
  --color-fg-placeholder: var(--fg-placeholder);
  --color-fg-disabled: var(--fg-disabled);
  --color-fg-inverse: var(--fg-inverse);
  --color-fg-on-emphasis: var(--fg-on-emphasis);
  --color-fg-on-selected: var(--fg-on-selected);
  --color-fg-on-brand: var(--fg-on-brand);
  --color-fg-on-warning: var(--fg-on-warning);
  --color-fg-brand: var(--fg-brand);
  --color-fg-magic: var(--fg-magic);
  --color-fg-info: var(--fg-info);
  --color-fg-success: var(--fg-success);
  --color-fg-warning: var(--fg-warning);
  --color-fg-error: var(--fg-error);
  --color-fg-danger: var(--fg-danger);

  --color-line-muted: var(--line-muted);
  --color-line-default: var(--line-default);
  --color-line-emphasis: var(--line-emphasis);
  --color-line-disabled: var(--line-disabled);
  --color-line-selected: var(--line-selected);
  --color-line-inverse: var(--line-inverse);
  --color-line-brand: var(--line-brand);
  --color-line-magic: var(--line-magic);
  --color-line-info: var(--line-info);
  --color-line-success: var(--line-success);
  --color-line-warning: var(--line-warning);
  --color-line-error: var(--line-error);
  --color-line-danger: var(--line-danger);

  --color-link-default: var(--link-default);
  --color-link-default-hover: var(--link-default-hover);
  --color-link-neutral: var(--link-neutral);
  --color-link-neutral-hover: var(--link-neutral-hover);
  --color-link-inverse: var(--link-inverse);
  --color-link-inverse-hover: var(--link-inverse-hover);
  --color-focus-default: var(--focus-default);
  --color-focus-inverse: var(--focus-inverse);
  --color-overlay: var(--overlay);
  --color-scrim: var(--scrim);
  --color-skeleton-default: var(--skeleton-default);
  --color-skeleton-muted: var(--skeleton-muted);

  --color-bg-categorical-neutral: var(--bg-categorical-neutral);
  --color-bg-categorical-neutral-hover: var(--bg-categorical-neutral-hover);
  --color-fg-categorical-neutral: var(--fg-categorical-neutral);
  --color-line-categorical-neutral: var(--line-categorical-neutral);
  --color-bg-categorical-blue: var(--bg-categorical-blue);
  --color-bg-categorical-blue-hover: var(--bg-categorical-blue-hover);
  --color-fg-categorical-blue: var(--fg-categorical-blue);
  --color-line-categorical-blue: var(--line-categorical-blue);
  --color-bg-categorical-purple: var(--bg-categorical-purple);
  --color-bg-categorical-purple-hover: var(--bg-categorical-purple-hover);
  --color-fg-categorical-purple: var(--fg-categorical-purple);
  --color-line-categorical-purple: var(--line-categorical-purple);
  --color-bg-categorical-green: var(--bg-categorical-green);
  --color-bg-categorical-green-hover: var(--bg-categorical-green-hover);
  --color-fg-categorical-green: var(--fg-categorical-green);
  --color-line-categorical-green: var(--line-categorical-green);
  --color-bg-categorical-orange: var(--bg-categorical-orange);
  --color-bg-categorical-orange-hover: var(--bg-categorical-orange-hover);
  --color-fg-categorical-orange: var(--fg-categorical-orange);
  --color-line-categorical-orange: var(--line-categorical-orange);
}
```

Example usage:

```html
<!-- Neutral secondary action -->
<button class="bg-bg-muted hover:bg-bg-muted-hover active:bg-bg-muted-active text-fg-primary">
  ذخیره پیش‌نویس
</button>

<!-- Neutral high-emphasis action -->
<button class="bg-bg-emphasis hover:bg-bg-emphasis-hover active:bg-bg-emphasis-active text-fg-on-emphasis">
  ادامه
</button>

<!-- Subtle selected chip -->
<button class="bg-bg-selected-muted hover:bg-bg-selected-muted-hover text-fg-primary border border-line-selected">
  انتخاب‌شده
</button>

<!-- Static error message -->
<div class="bg-bg-error-muted text-fg-error border border-line-error">
  تکمیل این فیلد الزامی است.
</div>
```

The duplicated `bg-bg-*` segment is the cost of retaining target-aware source names in Tailwind's generic color namespace. If shorter utilities become important, introduce an explicit Tailwind alias layer; do not weaken the source-token names.

---

## 5. Experience, context, brand, and theme layers

Experience is resolved before product-specific context, brand, or theme overrides. Productive is the default mapping represented by the values in this document. Expressive may override a documented subset of these semantic values; when no Expressive mapping exists, it falls back to Productive. Experience does not change token names or semantic meaning.

After Experience resolution, three independent axes may override semantic token values:

| Axis | Selector | Purpose |
|---|---|---|
| Context | `[data-context="app"]` | Employer and ATS applications with a gray workspace and lifted cards |
| Brand | `[data-theme="kando"]` | Kando/HRCanDo brand ramp and contrast pairings |
| Theme | `.dark` | Dark-theme values and contrast pairings |

Each override layer redefines only the semantic tokens that change. See `architecture.md` and `usage-rules.md` for Experience selection, accessibility, and fallback rules.

### 5.1 App context

Override the structural background ladder together rather than changing only the canvas:

```txt
bg-canvas
bg-default
bg-muted
bg-inset
```

Directly nested structural backgrounds must remain distinguishable at the point of use. Values may repeat globally, but a parent and its direct child must not visually collapse into one layer.

### 5.2 Kando brand

Kando's yellow brand requires coordinated overrides:

- `bg-brand-emphasis` and its interaction states use the yellow ramp.
- `fg-on-brand` becomes dark.
- `fg-brand` and `line-brand` use contrast-safe darker steps rather than raw yellow.
- `bg-brand-muted` uses a low-emphasis yellow treatment.
- Link, focus, warning, feedback, and categorical families remain brand-independent.

### 5.3 Dark mode

- Structural backgrounds map to dark neutrals.
- `fg-primary`, `fg-secondary`, and `fg-tertiary` map to light neutrals while retaining their hierarchy.
- Neutral lines become visible on dark backgrounds.
- `bg-emphasis` and `bg-selected-emphasis` may flip to light neutral values; their paired foregrounds must flip with them.
- Dark chromatic emphasis backgrounds continue to use `fg-on-emphasis`.
- Transparent interaction overlays switch from black alpha to white alpha.

Keep the Tailwind mapping declared with `@theme inline` so runtime context, brand, and mode overrides resolve at the point of use.

---

## 6. Migration map

| v1 | v2 |
|---|---|
| `canvas` | `bg-canvas` |
| `surface` | `bg-default` |
| `surface-muted` | `bg-muted` |
| `surface-muted-{state}` | `bg-muted-{state}` |
| `surface-hover/active` | `bg-transparent-hover/active` |
| `surface-selected-{state}` | `bg-selected-muted-{state}` |
| `surface-{semantic}` | `bg-{semantic}-muted` |
| `fill-primary-{state}` | `bg-emphasis-{state}` |
| `fill-{semantic}` | `bg-{semantic}-emphasis` |
| `fill-selected` | `bg-selected-emphasis` |
| `surface-disabled`, `fill-disabled` | `bg-disabled` |
| `fg-on-fill` | `fg-on-emphasis` |
| `line-subtle` | `line-muted` |
| `line-strong` | `line-emphasis` |
| `link` | `link-default` |
| `link-hover` | `link-default-hover` |
| `link-quiet-{state}` | `link-neutral-{state}` |
| `focus` | `focus-default` |
| `skeleton` | `skeleton-default` |
| `skeleton-subtle` | `skeleton-muted` |
| `tag-surface-{variant}-{state}` | `bg-categorical-{variant}-{state}` |
| `tag-fg-{variant}` | `fg-categorical-{variant}` |
| `tag-line-{variant}` | `line-categorical-{variant}` |

The v1 catalog contains 105 source tokens. The v2 catalog contains 103 source tokens: the two disabled background targets merge into `bg-disabled`, and the former role-specific neutral foreground pairings consolidate into `fg-on-emphasis`.
