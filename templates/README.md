# Templates

The active Product Knowledge model uses four simple templates:

```text
product-overview.md
product-area.md
shared-product-concept.md
jira-prd.md
```

## Product Knowledge templates

- `product-overview.md` describes one product and its main Product Areas.
- `product-area.md` describes one meaningful part of a product, including its flows, rules, permissions, states, validations, and edge cases.
- `shared-product-concept.md` describes a business concept or rule that is genuinely shared across products.

## Jira PRD template

`jira-prd.md` defines the minimum structure AI should use when helping a PM complete a PRD in Jira. The PRD is not stored in this repository.

## Design System templates

```text
shared/design-system/templates/
```

These are reusable UI templates and remain part of the Design System structure. They are different from the Product Knowledge document templates in this directory.

## Update rule

AI may propose document updates, but the named owner reviews and applies them through a normal branch and pull request.
