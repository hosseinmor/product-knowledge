---
id: design-system.token.frontend-contract
collection: design-system
type: token
title: Frontend Token Contract
summary: Design-side contract for runtime token packaging, public versus internal consumption, alias preservation, naming, and enforcement.
knowledge_state: unverified
document_maturity: draft
related:
  - design-system.token.architecture
last_reviewed: '2026-09-10'
---

# Frontend Token Contract

## Status

This document records the current **Design System-side approved direction** for HOS-7. Frontend review is still required before the runtime implementation contract is considered final.

## Purpose

Define the boundary between Design Tokens and Product frontend code without turning raw values or implementation details into the public Design System API.

## Package scope

Use one shared **logical Design System token distribution** across Products and Appearances rather than Product- or Appearance-specific token forks.

The distribution may generate multiple artifacts by Foundation, audience, or target format, plus an aggregate entry point. Exact npm package boundaries, file names, module formats, and import paths remain Frontend implementation decisions.

The package contract is Foundation-agnostic. Do not impose the Color graph on Typography, Spacing, Radius, Elevation, Motion, or Responsive Layout.

Color currently resolves through its own graph:

```text
Primitive → Semantic
Primitive → Brand → Semantic
Primitive / Semantic / Brand → Component
```

Other Foundations define their own scales, roles, recipes, or generated maps.

### Artifact forms

A Design System contract does not imply that every token becomes a public CSS custom property.

Depending on the owning Foundation, generated artifacts may include:

- runtime CSS custom properties;
- framework-agnostic value maps;
- responsive breakpoint/container maps;
- semantic recipe metadata;
- developer registries and type information;
- framework adapters generated from those canonical artifacts.

For example, Color benefits from runtime custom properties and alias resolution, while breakpoint data is primarily a shared build-time/configuration source and Typography may resolve through a recipe adapter rather than one public custom property per style.

The required invariant is one canonical Design System source per governed decision, not one physical output format for every Foundation.

## Preserve aliases at runtime

The runtime representation should preserve the token alias graph rather than flattening public tokens to final raw values.

Conceptually:

```css
--blue-700: #0053ff;
--brand-default: var(--blue-700);
--surface-brand: var(--brand-default);
```

Do not reduce the public role to a raw value such as:

```css
--surface-brand: #0053ff;
```

when doing so would erase an intentional runtime dependency or Product-aware mapping.

## Consumption audiences

Runtime presence, generated-artifact presence, and Product API visibility are separate concerns.

```text
Exists in generated output ≠ Product-facing API
```

Every governed token/recipe/artifact must be classifiable by its intended consumption audience. Exact metadata field names are Frontend-owned, but generation/tooling must be able to distinguish at least these three contracts deterministically.

### Product-facing Design System API

Product code may directly consume contracts explicitly exposed by their owning Foundation.

Current examples include:

- Semantic Color roles;
- the shared Spacing scale through approved Product tooling;
- public Radius roles;
- approved Typography recipes;
- semantic Elevation recipes;
- responsive breakpoint/container values through generated framework/build adapters.

The owning Foundation determines what is public. Publicness must not be inferred from whether a value happens to exist in Figma or CSS.

### Component implementation API

Approved Component tokens are implementation contracts for their owning Design System component.

Example:

```text
tag/blue/surface
tag/blue/fg
tag/blue/line
```

They may exist in generated output and may be consumed by the Tag implementation, but they are **not** general Product-facing tokens by default.

Product code should consume the Design System component rather than reconstructing it from Component-token recipes. If a Component token repeatedly represents a cross-component Product need, review promotion into the appropriate shared Semantic/Foundation contract.

### Internal resolution dependencies

Primitive and Brand Color tokens are current examples of internal resolution dependencies.

Internal means they may be required in generated/runtime output for alias resolution but are not normal Product or component-authoring APIs.

```text
blue/700       → internal
brand/default  → internal
surface/default → product
tag/blue/surface → component
```

CSS cannot make an already-loaded custom property physically private. API boundaries are therefore enforced through source classification, generated developer surfaces, documentation, and lint/CI rather than through assumed runtime invisibility.

## Primitive consumption policy

Direct Primitive use is not a Product-code escape hatch.

When a public token is insufficient:

```text
recurring semantic need
→ add or refine a Semantic token

stable component-owned need
→ add an approved Component token

truly temporary exceptional case
→ explicitly documented exception with a migration path
```

Do not normalize raw Primitive usage by allowing unrestricted lint-disable comments.

## Enforcement model

Do not rely on CSS visibility to enforce API boundaries. Enforce them from the token source and developer tooling.

The canonical source should carry machine-readable consumption classification or an equivalent capability.

The exact metadata field/schema is an implementation decision; the required capability is that generation/tooling can distinguish Product-facing, Component-implementation, and Internal contracts deterministically.

From the same source, tooling should be able to generate or validate:

```text
runtime CSS
→ all dependencies required for resolution

Product-facing registry / developer surface
→ Product-facing contracts only

Component implementation registry
→ owning-component contracts only, when such a registry is useful

framework adapters such as Tailwind
→ only the Product-facing subset approved by the owning Foundation

lint / CI allowlist
→ Product-facing API for Product code
```

### Lint/CI guardrail

Product repositories should reject direct internal token use where practical.

Conceptually:

```text
--surface-default      allowed
--fg-primary           allowed
--tag-blue-surface     blocked in ordinary Product code

--neutral-100          blocked
--blue-700             blocked
--brand-default        blocked
```

Design System build code may consume Internal dependencies as required by an owning Foundation. Design System component implementation may additionally consume the Component-implementation contracts owned by that component.

## CSS custom-property namespace

Keep generated CSS custom-property names close to the canonical token vocabulary, but reserve one explicit Design System namespace.

Canonical Design-side contract:

```text
surface/default     → --jvds-surface-default
fg/primary          → --jvds-fg-primary
line/accent         → --jvds-line-accent
brand/brand-default → --jvds-brand-default
palette/blue/700    → --jvds-blue-700
```

Rules:

- all CSS custom properties generated by the Design System use the `--jvds-` namespace;
- `jvds` identifies Design System ownership, not Product identity;
- Product code must not define new Product-owned custom properties inside the reserved `--jvds-*` namespace;
- canonical token names and Figma variable names do not gain the `jvds` segment;
- do not add a redundant `color-` segment;
- Product, Appearance, and API visibility do not enter the custom-property name.

```text
Product     → jobvision / cando
Appearance  → light / dark
API status  → public / internal
```

Those are context or policy, not token meaning.

The namespace solves global CSS collision and ownership concerns without coupling the public token vocabulary to a Product or Theme context. Exact selector/scoping mechanics and generated file organization remain Frontend-owned.

This decision applies specifically to CSS custom properties. Exact naming transforms for other generated formats may follow their platform conventions while preserving the same canonical token identity.

## Product and Appearance

Do not publish separate bundles such as `tokens-jobvision`, `tokens-cando`, `tokens-light`, or `tokens-dark` as the primary model merely to represent Theme combinations.

The intended model is:

```text
one token system
+
independent Product context
+
independent Appearance context
→ resolved public tokens
```

Exact selector, attribute, class, and initialization mechanics remain outside this document until the related frontend Theme contracts are reviewed.

## Deferred to follow-up implementation work

- Exact package name and physical file layout.
- Exact CSS selector/attribute/class mechanism for Product and Appearance scoping.
- Exact token metadata schema used to encode public/internal visibility.
- Exact lint implementation and repository integration.
- Tailwind utility naming and preset generation.
- Exact output format used by each non-Color Foundation where its runtime adapter is still under review.
- SSR Appearance persistence, precedence, and no-flash initialization.

## Frontend review questions

Frontend review should explicitly confirm or revise:

1. Can one shared package preserve the alias graph without unacceptable payload or loading complexity?
2. Is keeping Primitive and Brand at runtime while treating them as internal API practical in the current stack?
3. Can public/internal consumption be enforced through generated registries plus lint/CI?
4. Is the reserved `--jvds-*` CSS namespace compatible with current legacy applications and build tooling?
5. What exact CSS scoping mechanism should resolve independent Product and Appearance dimensions?
