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

Major user journeys normally live inside `product-overview.md`. Add an optional `journeys/` folder only when a complex end-to-end journey requires independent documentation and ownership.

Actors, user outcomes, triggers, preconditions, rules, states, and lifecycles live inside their owning Product overview, Capability, Flow, or Domain documents rather than in separate folders.

Shared cross-product knowledge should be referenced from `../../shared/`.