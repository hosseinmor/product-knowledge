# Initiative to PRD

## Purpose

Turn a short product initiative brief into a reviewable initiative analysis and Product Requirements Document with minimal manual writing.

AI performs discovery, context gathering, scope structuring, assumption detection, blocking-question prioritization, option comparison, drafting, and consistency checks.

Humans remain responsible for product decisions and final approval.

## Required inputs

- Product identifier
- Initiative identifier
- Short initiative brief
- Access to `manifest.generated.json` and relevant repository knowledge

## Optional inputs

- Jira ticket or Epic
- User research
- Data analysis
- Design references
- Technical notes
- Previous PRDs
- Reviewed walkthrough output

## Required output templates

Use these files as the output contract:

```text
templates/workflows/initiative-template.md
templates/workflows/prd-template.md
templates/workflows/decision-question-template.md
```

Do not redefine or shorten their required structure inside the Skill output.

## Expected workspace

```text
product-work/
└── initiatives/
    └── {initiative-id}/
        ├── initiative.md
        └── prd.md
```

Workflow outputs remain proposed work and are not indexed as canonical Product Knowledge.

## Workflow

### 1. Read the brief

Extract:

- Problem
- Desired outcome
- Initial scope
- Product
- Owner
- Change type

Do not assume the proposed solution or Capability name is correct.

Preserve the original brief in `initiative.md` so later refinements do not replace the initial intent silently.

### 2. Validate repository readiness

Follow `ai/retrieval-rules.md`.

Before discovery:

- Confirm `manifest.generated.json` exists.
- Confirm the committed manifest is current when repository tooling is available.
- Inspect its `summary` and `unindexed` list.
- Stop and report a repository-quality failure when the manifest is missing or stale.
- Surface relevant unindexed or unverified knowledge as a coverage gap.

Do not silently replace manifest discovery with filename globbing.

### 3. Gather the smallest sufficient knowledge set

Use manifest collections and stable IDs to find relevant:

- Product overview
- Capabilities
- Flows
- Domains when stable business constraints matter
- Accepted Decisions when prior rationale matters
- Design System Components, Patterns, foundations, tokens, and accessibility rules
- Content guidance
- Product standards
- Shared Domains

Prefer `knowledge_state: canonical` for intended current truth.

Treat:

```text
observed
→ current evidence whose intended meaning is not confirmed

unverified
→ content or migrated metadata requiring semantic review

deprecated
→ historical context, not current behavior
```

Read Evidence, Coverage, Unknowns, and last verification before presenting knowledge as complete.

### 4. Build `initiative.md`

Copy and complete:

```text
templates/workflows/initiative-template.md
```

Use stable IDs in `Related Product Knowledge`.

Record relevant manifest gaps under `Repository Coverage Gaps`. Do not fill missing product context by inference.

### 5. Identify blocking questions

A blocking question materially changes one or more of:

- Core scope
- Main user flow
- Business rule
- Permission model
- Lifecycle
- Data model
- Technical feasibility

Do not interrupt humans with cosmetic, copy, layout, or low-impact questions.

For each blocking question, copy and complete:

```text
templates/workflows/decision-question-template.md
```

Route decisions to:

- Product behavior or scope → PM
- Interaction or end-to-end journey → Designer
- Technical feasibility or constraint → Tech
- Cross-functional rule → PM + Tech

AI may recommend an option, but must not record it as approved without an explicit human decision.

A working decision is not automatically a canonical Decision document. Preserve it after release only when its rationale is durable under `knowledge-model.md`.

### 6. Apply human decisions

After each answer:

- Record approver, date, rationale, and approved option.
- Update scope and assumptions.
- Resolve contradictions explicitly.
- Remove the item from blocking questions only after resolution.
- Keep deferred questions visible.
- Recheck consistency with repository knowledge.

Do not rewrite the original brief or erase rejected alternatives.

### 7. Generate `prd.md`

Copy and complete:

```text
templates/workflows/prd-template.md
```

Keep these distinctions explicit:

```text
Current behavior
→ Supported by repository knowledge or reviewed evidence

Intended behavior
→ Proposed by the PRD and approved human decisions

Assumption
→ Necessary but not yet confirmed

Open question
→ Unresolved and visible
```

Give functional requirements stable local identifiers.

Reference existing Domain rules by stable ID. Clearly identify new proposed rules that require human approval.

### 8. Validate the PRD

Verify that:

- Every requirement is supported by the brief, repository knowledge, or an approved human decision.
- Assumptions are not written as confirmed rules.
- Current and intended behavior are separated.
- Scope is internally consistent.
- Business rules do not silently conflict with existing Domain documents.
- Permissions and lifecycle transitions are explicit.
- Existing Capabilities are not confused with proposed backlog work.
- Accepted Decisions are respected or explicitly reconsidered.
- Major user-journey impact is identified for the Product overview.
- Design System and content constraints are represented when relevant.
- Repository indexing and coverage gaps remain visible.
- Open questions and deferred items remain visible.
- Product Knowledge impact after release is identified.

### 9. Stop for approval

Present:

- The completed PRD
- Remaining open questions
- Important assumptions
- Conflicts with current repository knowledge
- Repository coverage gaps
- Major risks and dependencies
- Expected Product Knowledge impact after release

Do not mark the PRD approved on behalf of a human.

## Human responsibilities

Humans are responsible for:

- Providing the initial brief
- Answering blocking decisions
- Approving final scope
- Approving the final PRD

## Rules

- Do not invent product decisions.
- Do not hide uncertainty or repository gaps.
- Do not ask non-blocking questions too early.
- Do not create multiple working documents when one `initiative.md` is sufficient.
- Do not update canonical Product Knowledge before release.
- Do not treat a PRD as current product truth.
- Do not treat Jira Epic, Feature, Story, or Task hierarchy as the Product Knowledge structure.
- Do not create standalone Journey, Feature, User Goal, Scenario, Rule, State, Lifecycle, or Subdomain documents.
- Do not duplicate workflow template structures inside this Skill.
