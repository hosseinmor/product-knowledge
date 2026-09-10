---
id: design-system.product-variation.theme-context
collection: design-system
type: product-variation
title: Theme Context
summary: Defines Product and Appearance as independent shared Design System theme dimensions and their ownership boundaries.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.token.product-overrides
  - design-system.token.architecture
  - design-system.reference.code
last_reviewed: '2026-09-10'
---

# Theme Context

Theme is a shared Design System context and mapping mechanism. It is **not** an additional token layer.

The current context has two independent dimensions:

```text
Product    → JobVision | Cando
Appearance → Light | Dark
```

Do not encode them as combined theme identities such as `jobvision-dark` or `cando-light`.

## Resolved contexts

The current supported combinations are:

```text
JobVision Light
→ Product: JobVision
→ Appearance: Light

JobVision Dark
→ Product: JobVision
→ Appearance: Dark

Cando Light
→ Product: Cando
→ Appearance: Light

Cando Dark
→ Product: Cando
→ Appearance: Dark
```

For Color in the current Figma model these dimensions resolve independently:

```text
Product    → 02 Brand: JobVision | Cando
Appearance → 03 Semantic: light | dark
             04 Component: Light | Dark
```

The Figma collection model is a design representation of the same logical dimensions; runtime implementation does not need to mirror Figma collection structure exactly.

## Theme scope

In v1, Theme resolves at the application/document root.

- **Product** is root-level application/deployment identity and is normally stable for the document lifetime.
- **Appearance** is root-level runtime state and may change between Light and Dark.
- Nested Product Theme is not part of the general Design System API.
- Nested Appearance Theme is not part of the general Design System API.

A locally dark or inverse region inside a Light page should use Semantic roles such as `surface/inverse`, not a nested Dark Appearance context.

A JobVision-branded region inside Cando should use explicit identity such as the JobVision logo, name, or another approved branded composition rather than changing Product for a subtree.

An independently embedded application or microfrontend may define its own root Theme contract when a real integration requires it. This does not make nested Theme a general-purpose composition pattern.

## Runtime ownership

Responsibility is intentionally separated:

```text
App / deployment
→ owns Product identity

Application shell / Theme service
→ owns Appearance preference and resolution
→ applies the resolved Theme context at the root

Design System / token runtime
→ consumes the resolved context
→ resolves Theme-aware token values
→ does not own user preference persistence or product business logic

Components
→ consume Semantic or approved Component tokens
→ do not branch on Product or Appearance for normal styling
```

Product should not expose a general user-facing runtime switch. In ordinary applications it is known from the application/deployment context and remains stable.

Appearance may change at runtime. When it changes, token resolution should update without components carrying separate Product- or Dark-specific styling branches for normal Design System Color.

## Resolved Appearance versus preference

Resolved Appearance is only:

```text
light | dark
```

If the product supports a user preference such as:

```text
light | dark | system
```

`system` is a **preference/source**, not a third resolved Appearance value. It must resolve to Light or Dark before the final Theme context reaches token resolution.

Preference storage, precedence, server visibility, and no-flash initialization are separate runtime concerns and are not defined here.

## Foundation participation

ThemeContext is shared across the Design System, but Theme awareness is opt-in per Foundation. A Foundation consumes only the dimensions that materially affect its contract.

Current participation:

| Foundation | Product | Appearance | Current rule |
|---|---|---|---|
| Color | Yes | Yes | Product may affect Brand; Appearance resolves Light/Dark Semantic and Component Color. |
| Typography | No | No | Invariant for current scope. |
| Spacing | No | No | Invariant for current scope. |
| Radius | No | No | Invariant for current scope. |
| Elevation | No | No | Invariant for current scope; add Appearance dependence only if a validated need emerges. |
| Motion | No | No | Invariant for current scope. |

Do not create Product or Appearance modes for a Foundation merely because ThemeContext contains those dimensions.

If a future Foundation genuinely varies by Product or Appearance, it may consume the existing ThemeContext dimension without introducing a parallel foundation-specific ThemeContext.

## Future dimensions

Do not assume High Contrast is a third Appearance value. If future accessibility requirements need both Light/Dark and Standard/High Contrast combinations, Contrast should be evaluated as an independent dimension rather than forcing it into Appearance.

Do not add that dimension until a concrete product and accessibility contract requires it.

## Component rule

Normal component styling must resolve through Semantic or approved Component tokens:

```text
Component
→ Semantic / approved Component token
→ Theme-aware resolution
```

Avoid component logic such as:

```text
if Product is Cando → choose yellow primitive
if Appearance is Dark → choose dark primitive
```

Such branching belongs in the Theme/token mapping contract, not in ordinary component styling.

Business behavior may still legitimately depend on Product; this document governs Design System theming, not product-feature logic.

## Deferred implementation contracts

This document intentionally does not define:

- exact DOM attribute or class names;
- CSS variable names, package structure, or scoping;
- Tailwind utility mappings;
- Appearance preference persistence and precedence;
- SSR resolution and no-flash initialization.

Those are owned by the frontend token package, Tailwind, and SSR Theme integration contracts.
