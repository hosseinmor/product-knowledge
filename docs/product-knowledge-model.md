# Simplified Product Knowledge Model

## Product Overview

One overview per product. It explains:

- Product purpose
- Primary users
- Problems the product solves
- Product boundaries
- Main Product Areas
- Major journeys
- Important integrations
- Known documentation gaps

Path:

```text
products/{product}/overview.md
```

## Product Area

A Product Area is a meaningful and relatively independent part of a product that supports one coherent outcome or closely related set of outcomes.

A Product Area usually contains several related flows and owns the product-specific explanation of:

- Users and roles
- Outcomes
- Entry points
- Main concepts
- Main flows
- Rules
- Permissions
- States and transitions
- Validations
- Edge cases
- Relationships with other areas
- Variations
- Unknowns and evidence

A Product Area is not just a page, component, modal, Jira Epic, team, service, or one requested change.

Path:

```text
products/{product}/areas/{area}.md
```

### Splitting a large area

Keep flows in one Product Area document by default. Split only when the document becomes hard to understand or maintain:

```text
products/{product}/areas/{area}/
├── overview.md
└── flows/
    ├── create.md
    ├── submit.md
    └── approve.md
```

Flow files are an optional extension, not a required document type.

## Shared Product Concept

A Shared Product Concept contains a business definition, data model, lifecycle, or rule that has the same meaning in more than one product.

Path:

```text
shared/product-concepts/{concept}.md
```

Shared Product Concepts do not own product-specific user experience.

Example:

```text
shared/product-concepts/job-post.md
→ shared definition, common fields, shared lifecycle, shared rules

products/employer/areas/job-post-management.md
→ create, edit, publish, pause, close, and manage

products/jobseeker/areas/job-post-experience.md
→ view, understand, save, share, evaluate, and apply
```

Create a fully shared Product Area only when outcomes, behavior, rules, ownership, and flows are genuinely the same across products. This should be uncommon.

## Design System

The Design System remains a complete and independent knowledge structure under:

```text
shared/design-system/
```

It owns reusable UI foundations, tokens, components, patterns, accessibility rules, product variations, references, templates, and governance.

## Status and ownership

Every Product Overview, Product Area, and Shared Product Concept should include:

```text
Status: Draft | Reviewed
Owner: person or team
Last reviewed: date
```

`Reviewed` means the owner has reviewed the document as usable current team context. It does not mean every branch and edge case has been tested.

Unknowns, assumptions, variations, and untested behavior must be written explicitly.

## Update rule

AI may identify a gap and propose an exact update. A named owner decides whether the proposal is correct and updates the repository manually through a normal branch and pull request.
