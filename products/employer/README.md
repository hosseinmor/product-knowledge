# EMPLOYER Product Knowledge

Use this directory for product-specific Product Knowledge.

Default structure:

```text
employer/
├── product-overview.md
├── capabilities/
├── flows/
├── domains/
└── decisions/
```

`product-overview.md`, `capabilities/`, and `flows/` form the default documentation set.

Create Domain and Decision documents only when their additional responsibility is needed.

Major user journeys live inside `product-overview.md`. Do not create a `journeys/` folder or standalone Journey documents.

Actors, user outcomes, usage contexts, triggers, preconditions, rules, states, and lifecycles live inside their owning Product overview, Capability, Flow, or Domain documents rather than in separate folders.

Shared cross-product knowledge should be referenced from `../../shared/`.
