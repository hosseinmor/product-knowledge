# Templates

The repository uses two kinds of templates:

```text
Owner intake
→ Lightweight input used to capture human product knowledge

Canonical output
→ Final Product Knowledge or Jira structure produced after AI classification and review
```

## Owner intake template

```text
product-area-owner-input.md
```

`product-area-owner-input.md` is a lightweight, owner-facing document for capturing current knowledge about one Product Area without requiring the owner to understand the canonical Product Area or Product Concept schema.

It is **not canonical Product Knowledge** and is not indexed by the manifest. AI uses it as input, asks only material follow-up questions, then maps the knowledge into `product-area.md` and relevant Product Concepts.

Because Owner Input is intentionally structure-light, it should remain useful even if the canonical Product Knowledge model is revised later.

## Canonical Product Knowledge templates

```text
product-group-overview.md
product-overview.md
product-area.md
shared-product-concept.md
shared-product-service.md
```

- `product-group-overview.md` describes a product group such as Jobvision or Cando and lists its products.
- `product-overview.md` describes one product and its main Product Areas.
- `product-area.md` describes one meaningful capability, outcome, or business process in a product. It owns contextual behavior: flows, rules, permissions, validations, relevant state transitions, errors/recovery, and variations.
- `shared-product-concept.md` is the canonical Product Concept template for a business entity, actor, or concept whose definition, attributes, relationships, intrinsic rules, or lifecycle need an independent definition across Product Areas. Promoted concepts are currently stored under `shared/product-concepts/`.
- `shared-product-service.md` describes a durable cross-product service, such as an AI fit or matching service.

Mental model:

```text
Product Area
→ Where behavior happens

Product Concept
→ What a business thing means and what is intrinsically true about it
```

Do not duplicate canonical Concept definitions or intrinsic rules inside Product Areas. Product Areas reference Concepts and document what happens to them in that context.

Canonical templates include lightweight YAML frontmatter for the AI retrieval manifest:

```text
id
kind
group when relevant
product when relevant
title
summary
status
owner
last_reviewed
related
topics
```

Keep `summary` short and specific. Use `topics` for terms AI is likely to search. Use `related` only for direct relationships that materially help retrieval.

After creating or updating an indexed canonical document, run:

```bash
python scripts/generate_manifest.py generate
python scripts/generate_manifest.py check
```

The Owner Input template does not require manifest regeneration because it is not an indexed Product Knowledge document.

## Jira PRD template

`jira-prd.md` defines the minimum structure AI should use when helping complete a PRD in Jira. The PRD is not stored in this repository.

## Design System templates

```text
shared/design-system/templates/
```

These are reusable UI templates and remain part of the Design System structure. They are different from the Product Knowledge document templates in this directory.

## Update rule

AI may create a review draft or propose document updates, but the named owner reviews and approves canonical Product Knowledge changes through a normal branch and pull request. The regenerated manifest is included in the same pull request whenever indexed documents change.
