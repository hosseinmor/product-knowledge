# AI Workflows

This directory contains stable instructions for AI-assisted product discovery and documentation.

## Skills

- `product-walkthrough` — systematically explores current product behavior and produces reviewed evidence with explicit coverage and gaps
- `initiative-to-prd` — converts a product initiative into a reviewable PRD using current Product Knowledge
- `product-knowledge-update` — converts released change evidence or reviewed walkthrough findings into reviewable Product Knowledge patches

## Recovery pipeline

```text
Product interaction
→ product-walkthrough
→ temporary output and evidence in product-work
→ human review
→ product-knowledge-update
→ canonical document templates
→ Pull Request
→ human approval
```

A walkthrough does not update Product Knowledge directly. Candidate Capabilities, Flows, Domain rules, and Decisions remain temporary until reviewed and routed to the canonical owner document.

## Delivery pipeline

```text
Current Product Knowledge
→ initiative-to-prd
→ approved delivery work
→ released change
→ product-knowledge-update
→ reviewed Product Knowledge diff
```

Add another skill only when a repeated workflow has materially different inputs, quality gates, or stop conditions that cannot be handled clearly by these skills.
