# AI Skills

Skills are lightweight execution contracts for recurring AI-assisted work.

They are different from workflows and templates:

```text
Workflow
→ Defines the correct process

Template
→ Defines the required output structure

Skill
→ Activates and orchestrates the workflow and template for a user request
```

## Active skills

```text
product-knowledge-authoring/SKILL.md
→ Turns compact or free-form owner knowledge into a reviewable Product Area or Product Concept using current Product Knowledge, the authoring workflow, and canonical templates

prd-writing/SKILL.md
→ Creates, revises, or reviews a Jira-ready PRD using Product Knowledge, the manifest, `ai/prd-writing.md`, and `templates/jira-prd.md`
```

The previous complex skill model remains available only in:

```text
archive/product-knowledge-v1-2026-07-27
```

## Loading requirement

A repository skill becomes automatic only when the AI environment is configured to discover and load `ai/skills/*/SKILL.md`.

Without that integration, the Skill file is still a valid execution contract, but the user or system instruction must explicitly direct the AI to use it.

## Authoring rules

- Keep each Skill focused on one recurring task.
- Reference the canonical workflow and template instead of duplicating them.
- Define activation and non-activation cases.
- Define required inputs, tool use, stop conditions, validation, and final output.
- Keep human decisions and approval explicit.
- Do not turn repository hierarchy, Jira hierarchy, or release workflow into Skill-specific knowledge models.
