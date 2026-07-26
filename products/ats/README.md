# ATS Product Knowledge

Use this directory for product-specific canonical documentation.

Default structure:

```text
ats/
├── product-overview.md
├── capabilities/
├── flows/
├── domains/
└── decisions/
```

`product-overview.md`, `capabilities/`, and `flows/` form the default documentation set.

Create Domain and Decision documents only when their additional responsibility is needed.

Major user journeys live inside `product-overview.md`. Do not create a `journeys/` folder in the default Product Knowledge structure.

Actors, user outcomes, triggers, preconditions, rules, states, and lifecycles live inside their owning Product overview, Capability, Flow, or Domain documents rather than in separate folders.

Shared cross-product knowledge should be referenced from `../../shared/`.