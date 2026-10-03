---
name: prd-writing
description: Create, revise, or review a Jira-ready PRD using the approved external Product Knowledge source, repository-owned guidance, the PRD workflow, and Jira template.
---

# PRD Writing

## Activate when

The user asks to create, complete, revise, or review a PRD.

## Required contracts

Read in this order:

```text
product-knowledge-sources.yml
AGENTS.md
ai/prd-writing.md
templates/jira-prd.md
manifest.generated.json
```

The manifest retrieves Content, Design System, and standards only.

## Product context

- JobVision: open <https://docs-jv.jvoffice.ir/> through the internal VPN and
  browser, then load and cite only relevant domains.
- Cando: disclose that no canonical source exists. Use only explicit owner
  input, reviewed evidence, and approved decisions, preserving their authority.
- Never fall back to Git history, deleted repository documents, Figma,
  screenshots, runtime UI, or memory.

## Workflow

1. Determine whether the task creates, revises, or reviews a PRD.
2. Extract problem, evidence, affected users, desired outcome, and constraints.
3. Retrieve the approved product context and relevant repository guidance.
4. Separate canonical truth, approved decisions, evidence, observations,
   intended behavior, assumptions, recommendations, and unknowns.
5. Ask one focused batch of blocking questions when necessary.
6. Draft with every required section in `templates/jira-prd.md`.
7. Validate each product claim and keep unresolved questions visible.
8. Return a Jira-ready artifact for human review.

## Rules

- Do not invent behavior, permission, lifecycle, validation, or fallback.
- Do not treat a PRD as current Product Knowledge.
- Do not update canonical Product Knowledge from this repository.
- Do not claim Jira writes or approval unless they occurred.
- Humans approve scope, product decisions, and the final PRD.
