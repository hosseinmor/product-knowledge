---
name: prd-writing
description: Create, revise, or review a Jira-ready PRD using the repository's Product Knowledge, lightweight retrieval manifest, PRD workflow, and Jira PRD template.
---

# PRD Writing

## Purpose

Turn a small amount of product input into a reviewable Jira PRD while minimizing manual writing by the product owner.

AI performs context retrieval, gap detection, blocking-question prioritization, drafting, and consistency checks. Humans remain responsible for product decisions and final approval.

## Activate this skill when

The user asks to:

- Write or complete a PRD
- Turn an idea, Jira item, requirement, or product change into a PRD
- Revise an existing PRD after new decisions
- Review a PRD for missing product behavior, rules, permissions, states, or edge cases

## Do not activate this skill for

- General product questions that do not require a PRD
- External research without a PRD outcome
- Design-only work after a PRD is already approved
- Product Walkthrough execution
- Product Knowledge updates that are not part of creating or reviewing a PRD

Use the relevant workflow under `ai/` for those tasks.

## Required repository sources

Always use these files as contracts rather than copying their full content into this skill:

```text
ai/prd-writing.md
→ Process contract

templates/jira-prd.md
→ Output contract

manifest.generated.json
→ Retrieval entry point
```

Read `README.md` when product hierarchy or repository placement is relevant.

## Minimum input

Obtain these from the Jira item, the conversation, or the user:

- Problem
- Why it matters or supporting evidence
- Affected users
- Desired outcome
- Known constraints

Optional inputs may include:

- Existing Jira description or PRD
- Research and analytics
- Design references
- Technical notes
- Shared Product Service information
- Previous product decisions

Do not require a separate Brief or Initiative document.

## Source priority

Use sources in this order:

1. Current `main` branch Product Knowledge selected through the manifest
2. Explicit decisions supplied or approved by the responsible product owner
3. The current Jira input and linked evidence
4. External research, only when requested or necessary

The archive branch is historical context and must not be treated as current truth unless the user explicitly requests it.

## Workflow

### 1. Load the contracts

Read:

```text
ai/prd-writing.md
templates/jira-prd.md
manifest.generated.json
```

Determine whether the task is to create, revise, or review a PRD.

### 2. Resolve product context

Use the manifest to identify the smallest relevant set of:

- Product Group Overview
- Product Overview
- Product Areas
- Shared Product Concepts
- Shared Product Services
- Product standards and content guidance

Read only documents that materially affect the requested change.

Do not scan the entire repository by default. Do not infer current behavior from filenames or folder names.

### 3. Assess input completeness

Extract the minimum input and mark missing information.

A question is blocking only when its answer can materially change one or more of:

- Core scope
- Main user flow
- Business rule
- Permission model
- State or lifecycle transition
- Validation or destructive behavior
- Shared service behavior or fallback
- Data or technical feasibility
- Success criteria

Ask blocking questions in one focused batch whenever possible. Do not interrupt the user with cosmetic, copy, layout, or low-impact questions.

When useful, recommend an option and explain the trade-off, but do not record it as approved without an explicit human decision.

### 4. Build the current-context summary

Before drafting, distinguish:

```text
Current behavior
→ Supported by current Product Knowledge or linked evidence

Intended behavior
→ Requested by the Jira input or explicitly approved decisions

Assumption
→ Needed for the draft but not confirmed

Open question
→ Unresolved and visible

Recommendation
→ AI proposal, not an approved product decision
```

Surface contradictions, missing Product Knowledge, and relevant Shared Product Service dependencies.

### 5. Stop for blocking decisions

When unresolved blocking questions would make the PRD materially unreliable, present:

- Current context summary
- Blocking questions
- Recommended option when useful
- Consequence of leaving each question unresolved

Wait for the responsible human to decide before producing a final PRD draft.

A partial draft may be produced only when the user explicitly asks for one. Mark unresolved sections clearly.

### 6. Draft the PRD

Use `templates/jira-prd.md` without removing required sections.

For irrelevant conditional sections, state that they are not applicable rather than inventing content. The Shared Service section is required only when the change depends on a cross-product service.

Keep product-specific behavior separate from shared service behavior. Keep current behavior separate from intended behavior.

Do not create an additional Brief, Initiative file, or canonical Product Knowledge document.

### 7. Validate the draft

Before delivery, verify that:

- Every product claim is supported by Product Knowledge, linked evidence, Jira input, or an explicit human decision.
- Assumptions are not presented as confirmed rules.
- Current and intended behavior are clearly separated.
- In-scope and out-of-scope boundaries are consistent.
- Main, alternate, error, cancellation, and recovery flows are covered when relevant.
- Rules, permissions, states, transitions, validations, and destructive actions are explicit.
- Shared Product Service inputs, outputs, limitations, confidence, and fallback are separated from product-specific presentation and thresholds.
- Open questions remain visible.
- Success criteria describe outcomes rather than only implementation completion.
- Related Product Knowledge paths or IDs are listed.

### 8. Deliver for Jira and approval

Return:

1. The Jira-ready PRD using `templates/jira-prd.md`
2. Remaining open questions
3. Important assumptions and recommendations
4. Conflicts or gaps in current Product Knowledge
5. Sources used

Use the template's English section headings. Write the main PRD content in Persian unless the user or Jira item uses another language. Preserve established English canonical entity and product terms when translating them would create ambiguity.

Do not claim the PRD was saved, updated, or approved in Jira unless the corresponding write operation succeeded. Do not approve the PRD on behalf of a human.

## Human responsibilities

Humans are responsible for:

- Providing or confirming the initial problem and desired outcome
- Answering blocking product decisions
- Approving final scope
- Approving the final PRD

## Rules

- Do not invent product behavior or shared-service rules.
- Do not hide uncertainty, contradictions, or repository gaps.
- Do not ask non-blocking questions before producing useful work.
- Do not treat a PRD as current Product Knowledge.
- Do not update canonical Product Knowledge as part of this skill.
- Do not use the archived complex workflow model unless explicitly requested.
- Keep this skill as orchestration; process details belong in `ai/prd-writing.md` and output structure belongs in `templates/jira-prd.md`.
