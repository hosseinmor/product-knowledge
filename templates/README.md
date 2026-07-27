# Product Knowledge Templates

These templates define the required shape of Product Knowledge documents and temporary walkthrough output.

## Canonical Product Knowledge templates

- `product-overview-template.md`
- `capability-template.md`
- `flow-template.md`
- `domain-template.md`
- `decision-template.md`

Use these templates when creating or materially restructuring Product Knowledge. Keep required frontmatter and section headings unless a section is genuinely not applicable. Write `Not applicable`, `Unknown`, or `Not yet verified` instead of silently omitting material information.

Journey, Feature, User Goal, Scenario, Rule, State, Lifecycle, and Subdomain are not standalone Product Knowledge document types. Major user journeys belong inside the Product overview. Rules, states, lifecycles, user outcomes, and usage context belong inside their owning documents.

## Temporary evidence template

- `walkthrough-output-template.md`

Walkthrough output is temporary source material. Copy this template into `product-work/walkthroughs/{walkthrough-id}/output.md`. Do not store completed walkthrough output under `products/` and do not treat candidate Capabilities, Flows, or rules as canonical before human review.

## Template ownership

`knowledge-model.md` defines meaning and canonical ownership. These templates define document shape. AI skills define the process used to collect evidence and create or update documents.
