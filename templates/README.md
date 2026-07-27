# Templates

The active Product Knowledge model uses these simple templates:

```text
product-group-overview.md
product-overview.md
product-area.md
shared-product-concept.md
shared-product-service.md
jira-prd.md
```

## Product Knowledge templates

- `product-group-overview.md` describes a product group such as Jobvision or Kando and lists its products.
- `product-overview.md` describes one product and its main Product Areas.
- `product-area.md` describes one meaningful part of a product, including its flows, rules, permissions, states, validations, and edge cases.
- `shared-product-concept.md` describes a business concept or rule that is genuinely shared across products.
- `shared-product-service.md` describes a durable cross-product service, such as an AI fit or matching service.

These templates include lightweight YAML frontmatter for the AI retrieval manifest:

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

After creating or updating an indexed document, run:

```bash
python scripts/generate_manifest.py generate
python scripts/generate_manifest.py check
```

## Jira PRD template

`jira-prd.md` defines the minimum structure AI should use when helping a PM complete a PRD in Jira. The PRD is not stored in this repository.

## Design System templates

```text
shared/design-system/templates/
```

These are reusable UI templates and remain part of the Design System structure. They are different from the Product Knowledge document templates in this directory.

## Update rule

AI may propose document updates, but the named owner reviews and applies them through a normal branch and pull request. The regenerated manifest is included in the same pull request.
