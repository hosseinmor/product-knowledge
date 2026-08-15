# AI Workflows and Skills

This directory contains lightweight instructions for recurring AI-assisted product work that depends on canonical Product Knowledge.

## Entry and routing

Use the repository-level entry point and router:

```text
AGENTS.md
→ Tool-agnostic bootstrap and repository rules

ai/router.md
→ Detects the requested outcome and selects the appropriate Skill or workflow
```

After one-time tool setup, a user should only need to describe the problem or provide files and state the desired outcome. The AI environment should read `AGENTS.md` and route the request without requiring the user to paste a long prompt.

See [`../docs/ai-tool-setup.md`](../docs/ai-tool-setup.md) for repository-connected, file-upload, and plain-chat capability modes.

## Workflows

The active workflows are:

```text
product-knowledge-authoring.md
→ Turn compact or free-form owner knowledge into a structured Product Area or Product Concept review draft

research.md
→ Use internal Product Knowledge before external research or benchmarking

prd-writing.md
→ Turn minimum Jira input, Product Knowledge, and owner decisions into a complete PRD draft

design-start.md
→ Use the approved Jira PRD, Product Knowledge, shared services, and Design System to prepare an initial design draft

knowledge-update.md
→ Apply reviewed and approved Product Knowledge changes through the normal repository update process
```

Workflow files define the correct process. They are not Product Knowledge documents and are not mandatory sequential stages.

Product walkthrough capture and evidence review are maintained separately in `hosseinmor/product-walkthrough`. Product Knowledge authoring does not require complete walkthrough coverage when the responsible owner can provide current product knowledge, but sparse evidence must never be treated as permission to invent missing behavior.

## Skills

The active lightweight Skills are:

```text
skills/product-knowledge-authoring/SKILL.md
→ Turns short owner input into a reviewable Product Area or Product Concept and routes facts to the correct canonical owner

skills/prd-writing/SKILL.md
→ Activates and orchestrates PRD creation, revision, or review
```

The Product Knowledge Authoring Skill uses:

```text
ai/product-knowledge-authoring.md
→ Authoring and classification process contract

templates/product-area.md
→ Product Area output contract

templates/shared-product-concept.md
→ Product Concept output contract

manifest.generated.json
→ Product Knowledge retrieval
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

Automatic Skill activation requires a one-time connection between the AI environment and `AGENTS.md`. The repository itself cannot force an unrelated tool to discover its instructions.

See [`skills/README.md`](skills/README.md) for the distinction between Skills, workflows, and templates.

## Retrieval

Use `manifest.generated.json` as the retrieval entry point. Read only the smallest relevant set of Product Group, Product, Product Area, Shared Product Concept, Shared Product Service, Design System, content, and product-standard documents.

## Archived model

The previous complex skill-based workflow model is preserved only in:

```text
archive/product-knowledge-v1-2026-07-27
```

The active Skills do not restore the old Initiative workspace, release handoff, or complex document taxonomy.

Add a new workflow or Skill only when a repeated need cannot be handled clearly by the existing set.
