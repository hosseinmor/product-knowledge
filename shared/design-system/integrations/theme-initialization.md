---
id: design-system.reference.theme-initialization
collection: design-system
type: reference
title: Theme Initialization Contract
summary: Defines Product and Appearance resolution, first-paint invariants, hydration continuity, and no-flash requirements for SSR-capable applications.
knowledge_state: unverified
document_maturity: draft
owner: Design System team
last_reviewed: 2026-09-13
related:
  - design-system.product-variation.theme-context
  - design-system.reference.source-of-truth
---

# Theme Initialization Contract

## Status

Design-side runtime contract for HOS-9. Exact framework, storage, DOM, CSS selector, bootstrap-script, and server integration mechanics remain Frontend-owned.

## Purpose

Theme initialization must make the correct Product identity and effective Appearance available for the **first styled paint** and preserve that same effective Theme through hydration.

The Theme dimensions remain independent:

```text
Product    → application/deployment identity
Appearance → resolved light | dark
```

Do not create combined Theme identities such as `jobvision-dark`.

## Appearance preference model

If a user-facing Appearance preference is supported, its logical values are:

```text
light | dark | system
```

Resolved Appearance remains only:

```text
light | dark
```

`system` is a preference source, not a resolved Appearance.

### Resolution precedence

Resolve Appearance in this order:

1. explicit user preference `light` or `dark`;
2. current system/user-agent color-scheme preference when the effective preference is `system` or no explicit preference exists;
3. `light` when system preference cannot be determined.

Invalid or unknown stored preference values are treated as no explicit preference; they do not create additional Theme values.

The Design System does not define where preference is stored or how conflicting storage sources are reconciled. The application must provide one effective preference to initialization.

## Product resolution

Product is not a user preference.

- Product must be known deterministically from application/deployment context before SSR rendering begins.
- Product normally remains stable for the document lifetime.
- The Design System defines no fallback Product.
- An unresolved Product is an application integration/configuration error; do not silently render another Product's identity.

An independently embedded application may own a separate root Theme context when its integration explicitly requires it. Nested Product theming remains outside the general Theme API.

## First-paint invariant

The first styled paint must already use:

- the correct Product identity; and
- the effective Appearance for the current preference context.

A compliant implementation must not intentionally paint a guessed Light or Dark Theme and then correct it after hydration.

The contract does not require one specific technical mechanism. Valid strategies may include:

- server-readable effective preference;
- CSS-native `prefers-color-scheme` resolution for system behavior;
- a minimal pre-paint client bootstrap;
- another mechanism that meets the same first-paint invariant.

Client hints or any other browser capability may be used as an optimization, but the Theme contract must not depend on a non-universal experimental signal.

### User-agent UI

Browser-provided UI such as form controls, scrollbars, and the document canvas should be informed of the effective supported color scheme early enough to avoid a mismatch with application surfaces.

Exact use of HTML metadata, the CSS `color-scheme` property, or another platform mechanism is Frontend-owned.

## Hydration continuity

Hydration must adopt or reconcile with the Theme already effective at first paint.

It must not independently choose a conflicting initial Product or Appearance.

Conceptually:

```text
request / application context
→ Product identity
→ effective Appearance preference
→ first-paint Theme
→ hydration adopts same effective Theme
→ normal runtime Theme updates
```

Theme initialization belongs to the application shell/runtime integration. Individual components must not implement their own flash prevention or initial Product/Appearance detection.

## Runtime changes after initialization

Appearance may change after initialization.

- Explicit `light` ignores later system Light/Dark changes.
- Explicit `dark` ignores later system Light/Dark changes.
- `system` follows the current system/user-agent color-scheme and should react when that preference changes.
- When no explicit preference exists, system behavior follows the same rule as `system`.
- A user changing the preference should update the effective Appearance without requiring component-specific Theme branches.

Persistence timing, cross-device preference sync, account-vs-device policy, and storage technology are Product/Frontend concerns.

## No-flash acceptance criteria

At minimum, validate these cases:

| Scenario | Required first paint |
|---|---|
| Explicit Light preference | Light |
| Explicit Dark preference | Dark |
| System preference + system Dark | Dark |
| System preference + system Light | Light |
| No explicit preference + system Dark | Dark |
| No explicit preference + system Light | Light |
| System preference unavailable | Light fallback |
| Invalid stored Appearance preference | Resolve as no explicit preference |
| Any supported Product | Correct Product identity from first paint |

Also verify:

- hydration does not visibly change the effective Theme;
- system preference changes update Appearance only while effective preference is `system` or absent;
- explicit Light/Dark remains stable when the OS Theme changes;
- native/browser-controlled UI does not visibly contradict the application Theme;
- components do not need individual initialization guards;
- initial Theme correctness is not achieved by globally hiding normal page content until hydration as the default strategy.

## Frontend-owned decisions

This contract intentionally does not define:

- cookie, profile, local-storage, or other preference persistence;
- precedence between multiple storage locations;
- exact SSR framework integration;
- exact root attribute/class names;
- exact CSS selector/scoping strategy;
- inline script versus external bootstrap;
- exact use of `<meta name="color-scheme">`, CSS `color-scheme`, or equivalent platform APIs;
- performance optimizations and caching strategy.

Those choices are valid when they preserve the ThemeContext contract and the first-paint/hydration invariants above.

## Web-platform references

- `prefers-color-scheme` represents a user's Light/Dark system or user-agent preference.
- `color-scheme` and the HTML color-scheme metadata allow the user agent to align browser-provided UI with supported schemes.
