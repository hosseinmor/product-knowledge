# Templates

This directory contains approved document shapes used by humans and AI workflows.

## Canonical Product Knowledge templates

```text
product-overview-template.md
capability-template.md
flow-template.md
domain-template.md
decision-template.md
```

These are the only canonical Product Knowledge templates. Journey, Feature, User Goal, Scenario, Rule, State, Lifecycle, and Subdomain templates must not be created.

Major user journeys are documented inside Product overview. Durable product abilities are documented as Capabilities.

## Temporary evidence template

```text
walkthrough-output-template.md
```

This template is used in `product-work` for reviewed walkthrough evidence. It does not create canonical Product Knowledge by itself.

## Workflow output templates

```text
workflows/initiative-template.md
workflows/prd-template.md
workflows/decision-question-template.md
workflows/product-knowledge-update-proposal-template.md
```

These files define temporary, reviewable outputs in `product-work`. They are not indexed in `manifest.generated.json`.

## Difference from Design System templates

```text
templates/
→ Documentation and workflow output shapes

shared/design-system/templates/
→ Canonical reusable UI templates in the Design System collection
```

Design System UI templates use `collection: design-system` and `type: ui-template`. Root workflow templates use `artifact_type` and remain outside the canonical manifest.

## Responsibilities

```text
Template
→ Required metadata, sections, evidence, coverage, and unknowns

Skill
→ Collection workflow, classification, validation, stop conditions, and handoff
```

A Skill should reference an approved template rather than duplicating its full structure in prose.

When a canonical template and an existing product document diverge, update the document deliberately through the Product Knowledge update workflow rather than silently replacing content.
