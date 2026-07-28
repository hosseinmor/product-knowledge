# AI Workflows

This directory contains lightweight instructions for using Product Knowledge in recurring AI-assisted product work.

The active workflows are:

```text
research.md
→ Use internal Product Knowledge before external research or benchmarking

prd-writing.md
→ Turn minimum Jira input, Product Knowledge, and owner decisions into a complete PRD draft

design-start.md
→ Use the approved Jira PRD, Product Knowledge, shared services, and Design System to prepare an initial design draft

product-walkthrough.md
→ Optionally inspect current product behavior when Product Knowledge is missing, incomplete, disputed, or outdated

knowledge-update.md
→ Propose focused Product Knowledge changes for review and manual update by the named owner
```

These files are workflow guidance, not Product Knowledge documents and not mandatory sequential stages.

Use `manifest.generated.json` as the retrieval entry point. Read only the smallest relevant set of Product Group, Product, Product Area, Shared Product Concept, Shared Product Service, Design System, content, and product-standard documents.

The previous skill-based workflow model is preserved only in the archive branch:

```text
archive/product-knowledge-v1-2026-07-27
```

New workflow files should be added only when a repeated need cannot be handled clearly by the existing five workflows.
