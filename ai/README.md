# AI Workflows

This directory contains stable instructions for AI-assisted product discovery and documentation.

The repository uses three core skills:

- `product-walkthrough`
- `initiative-to-prd`
- `product-knowledge-update`

Their responsibilities are distinct:

```text
product-walkthrough
→ Inspect current product behavior and produce reviewed evidence with explicit coverage gaps

initiative-to-prd
→ Use current Product Knowledge to prepare proposed product change documentation

product-knowledge-update
→ Convert released or reviewed evidence into canonical Product Knowledge patches
```

Templates define the required document shape. Skills define the workflow, evidence rules, validation, and stop conditions.

New skills should be added only when a repeated workflow cannot be handled clearly by these three skills.
