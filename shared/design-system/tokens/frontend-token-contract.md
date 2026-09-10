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

## Package model

Use one shared token package for JobVision and Cando rather than separate Product- or Appearance-specific packages.

Conceptual layers:

```text
Token package
├── Primitive   internal runtime dependency
├── Brand       internal runtime dependency
├── Semantic    public Product API
└── Component   public only for approved component-owned contracts
```

A layered generated output with one aggregate entry point is the preferred implementation shape. Exact package names and file names remain an implementation detail for Frontend review.

Runtime load/dependency order may be:

```text
Primitive
→ Brand
→ Semantic
→ Component
```

This ordering does not mean Brand or Component are mandatory hops in every alias path.

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

## Public versus internal API

Runtime presence and Product API visibility are separate concerns.

```text
Exists at runtime ≠ Public Product API
```

### Internal

Primitive and Brand tokens are internal runtime dependencies.

Internal means they are:

- available where required for alias resolution;
- not documented as the normal Product-code API;
- not exposed through normal public token registries or generated developer interfaces;
- not mapped to normal Product Tailwind utilities;
- blocked from direct Product-code consumption by lint/CI where practical;
- not covered by the same public compatibility guarantee as Semantic and approved Component tokens.

Internal does **not** mean the CSS custom property is physically inaccessible once loaded in the document.

### Public

Product code normally consumes:

- Semantic tokens;
- approved Component tokens when the component has a reviewed component-owned token contract.

Example:

```css
.card {
  background: var(--surface-muted);
  color: var(--fg-primary);
}
```

Product code should not normally consume:

```css
.card {
  background: var(--neutral-50);
  color: var(--brand-default);
}
```

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

The token source should carry machine-readable API visibility metadata or an equivalent classification:

```text
blue/700
→ internal

brand/default
→ internal

surface/default
→ public

tag/neutral/surface
→ public
```

The exact metadata field/schema is an implementation decision; the required capability is that generation/tooling can distinguish public from internal tokens deterministically.

From the same source, tooling should be able to generate or validate:

```text
runtime CSS
→ all dependencies required for resolution

public token registry / developer surface
→ Semantic + approved Component only

Tailwind mapping
→ public tokens only

lint / CI allowlist
→ public Product API only
```

### Lint/CI guardrail

Product repositories should reject direct internal token use where practical.

Conceptually:

```text
--surface-default      allowed
--fg-primary           allowed
--tag-blue-surface     allowed

--neutral-100          blocked
--blue-700             blocked
--brand-default        blocked
```

Design System implementation/build code may consume internal layers as required by the alias graph.

## Naming direction

Keep runtime token names as close as practical to the canonical token vocabulary.

Current Design-side direction:

```text
surface/default     → --surface-default
fg/primary          → --fg-primary
line/accent         → --line-accent
brand/brand-default → --brand-default
pallete/blue/700    → --blue-700
```

Do not add a redundant global `jvds-` prefix or a `color-` segment by default.

Do not encode these dimensions in token names:

```text
Product     → jobvision / cando
Appearance  → light / dark
API status  → public / internal
```

They are context or policy, not token meaning.

### Naming tradeoff

Unprefixed CSS custom properties have a higher collision risk with legacy or Product-owned variables. The current Design-side preference accepts that tradeoff only if the Design System vocabulary is authoritative inside the intended application scope. Frontend must validate this assumption before finalizing the naming/scoping contract.

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
- Final decision on whether prefixless custom properties are safe across current legacy applications.
- Exact token metadata schema used to encode public/internal visibility.
- Exact lint implementation and repository integration.
- Tailwind utility naming and preset generation.
- SSR Appearance persistence, precedence, and no-flash initialization.

## Frontend review questions

Frontend review should explicitly confirm or revise:

1. Can one shared package preserve the alias graph without unacceptable payload or loading complexity?
2. Is keeping Primitive and Brand at runtime while treating them as internal API practical in the current stack?
3. Can public/internal consumption be enforced through generated registries plus lint/CI?
4. Are unprefixed names such as `--surface-default` safe within the target app scopes, or is one short global prefix required for collision safety?
5. What exact CSS scoping mechanism should resolve independent Product and Appearance dimensions?
