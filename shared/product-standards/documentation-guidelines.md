---
id: standard.documentation
collection: product-standard
type: documentation-guideline
title: Documentation Guidelines
summary: Defines canonical document types, metadata states, ownership, and writing
  rules for Product Knowledge.
knowledge_state: canonical
document_maturity: reviewed
related: []
owner: product-knowledge
last_verified: 2026-07-27
---

# Documentation Guidelines

## Canonical Product Knowledge types

```text
Product overview
Capability
Flow
Domain
Decision
```

Product overview, Capability, and Flow form the default documentation set. Create Domain and Decision documents only when their additional responsibility is needed.

Journey and Feature are not canonical document types, templates, or folders. Major user journeys live inside the Product overview. Durable product abilities are documented as Capabilities.

User outcome, Scenario, Rule, State, Lifecycle, Validation, and Error are structured content inside their owning documents, not standalone types.

## Shared collections

The repository also indexes these shared knowledge collections:

```text
design-system
content
product-standard
shared-domain
```

Each collection has its own allowed document types. `shared` is placement and ownership, not a catch-all type.

## Writing principles

- Describe approved current behavior and rules.
- Separate current, observed, unverified, proposed, and deprecated knowledge.
- Keep stable business rules and lifecycles in Domain documents.
- Keep durable product abilities and boundaries in Capability documents.
- Keep step-by-step behavior, branches, validation, persistence, and recovery in Flow documents.
- Keep major user journeys in Product overview.
- Keep durable rationale in Decision documents while updating the document that owns resulting current behavior.
- Give every durable fact one canonical owner.
- Reference related documents by stable ID rather than redefining owned facts.
- Preserve evidence, coverage limitations, untested cases, and open questions.
- Do not infer complete coverage from one role, environment, authentication state, or happy path.

## Metadata

All indexable documents use the common envelope:

```yaml
id:
collection:
type:
title:
summary:
knowledge_state:
document_maturity:
related: []
```

Product documents also require `product`.

Allowed truth states:

```text
canonical
observed
unverified
deprecated
```

Allowed maturity states:

```text
scaffold
draft
reviewed
stable
```

A scaffold cannot be canonical. A canonical document must contain substantive owned facts.

Legacy `status` and `maturity` fields must not be used as substitutes for `knowledge_state` and `document_maturity`.

## Manifest and validation

- Generate `manifest.generated.json` from frontmatter.
- Resolve `related` IDs through the manifest.
- Treat manifest `unindexed` entries as repository coverage gaps.
- Run repository validation before merging documentation changes.
- Do not silently fall back to filename-based discovery when the manifest is missing or stale.

## Shared vs product-specific

Use `shared/` only when meaning, rules, and ownership are genuinely consistent across products. Product-specific exceptions remain with the product unless they do not change the shared definition.
