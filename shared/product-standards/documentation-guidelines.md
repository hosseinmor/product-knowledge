# Documentation Guidelines

## Product Knowledge document types

- Product overview
- Capability
- Flow
- Domain
- Decision
- Shared knowledge when ownership and meaning are genuinely cross-product

Journey and Feature are not Product Knowledge document types. Major user journeys live inside the Product overview. Use Capability for durable product abilities.

User outcomes, usage contexts, rules, states, lifecycles, and Subdomains are not standalone document types.

## Official templates

Use the matching file in `/templates` when creating or materially restructuring Product Knowledge.

Required sections must not be silently omitted. Use `Unknown`, `Not yet verified`, or `Not applicable — {reason}` when the available evidence does not support content.

## Writing principles

- Describe approved current product behavior
- Separate current, observed, inferred, proposed, and deprecated information
- Connect material facts to evidence or reviewed sources
- Keep coverage limits and unknowns visible
- Keep stable business truth in Domain documents
- Keep durable product abilities in Capability documents
- Keep context-specific behavior in Flow documents
- Keep major user journeys in Product overview
- Keep durable rationale in Decision documents
- Give every durable fact one canonical owner
- Reference owned facts rather than duplicating them
- Preserve open questions and historical rationale

## Knowledge state and document maturity

Use separate fields:

```yaml
knowledge_state: canonical | observed | deprecated
document_maturity: draft | reviewed | stable
```

Proposed or unreleased behavior remains in `product-work`.

## Evidence recovery

Product interaction should use `ai/skills/product-walkthrough/SKILL.md` and `templates/walkthrough-output-template.md`.

Walkthrough output remains temporary until human review. Observations and inferences do not become canonical automatically.

## Shared vs product-specific

Use `shared/` only when meaning, rules, and ownership are genuinely consistent across products. Do not move product-specific knowledge into `shared/` merely to avoid duplication.
