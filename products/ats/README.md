# ATS Product Knowledge

Use this directory for ATS-specific Product Knowledge.

```text
ats/
├── product-overview.md
├── capabilities/
├── flows/
├── domains/
└── decisions/
```

`product-overview.md`, `capabilities/`, and `flows/` form the default documentation set. Create Domain and Decision documents only when their additional responsibility is needed.

Major user journeys live inside `product-overview.md`. Do not create Journey or Feature documents or folders.

Create and materially restructure documents from the matching files in `../../templates/`. Keep evidence, coverage, unknowns, and untested material cases visible rather than filling gaps with inference.

Actors, user outcomes, usage contexts, triggers, preconditions, rules, states, and lifecycles live inside their owning Product overview, Capability, Flow, or Domain documents.

Shared cross-product knowledge should be referenced from `../../shared/`.
