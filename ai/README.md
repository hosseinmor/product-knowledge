# AI Workflows and Skills

This directory contains lightweight instructions for recurring AI-assisted product work.

## Workflows

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

Workflow files define the correct process. They are not Product Knowledge documents and are not mandatory sequential stages.

## Skills

The first active lightweight Skill is:

```text
skills/prd-writing/SKILL.md
→ Activates and orchestrates PRD creation, revision, or review
```

The PRD Skill uses:

```text
ai/prd-writing.md
→ Process contract

templates/jira-prd.md
→ Output contract

manifest.generated.json
→ Product Knowledge retrieval
```

A Skill becomes automatic only when the AI environment is configured to discover and load `ai/skills/*/SKILL.md`. Otherwise, the user or system instruction must explicitly direct the AI to use the Skill.

See [`skills/README.md`](skills/README.md) for the distinction between Skills, workflows, and templates.

## Retrieval

Use `manifest.generated.json` as the retrieval entry point. Read only the smallest relevant set of Product Group, Product, Product Area, Shared Product Concept, Shared Product Service, Design System, content, and product-standard documents.

## Archived model

The previous complex skill-based workflow model is preserved only in:

```text
archive/product-knowledge-v1-2026-07-27
```

The active PRD Skill does not restore the old Initiative workspace, release handoff, or complex document taxonomy.

Add a new workflow or Skill only when a repeated need cannot be handled clearly by the existing set.
