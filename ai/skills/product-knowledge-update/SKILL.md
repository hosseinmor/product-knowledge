# Product Knowledge Update

## Purpose

Update canonical Product Knowledge after an approved product change has been released, or after missing current behavior has been recovered through reviewed evidence.

AI prepares the evidence classification, ownership analysis, patches, metadata changes, and manifest update. Humans validate semantic meaning and approve the final diff.

## Required inputs

For changes arriving from `product-work`, require a versioned handoff created from:

```text
templates/workflows/product-knowledge-handoff-template.yaml
```

The handoff must identify the exact source repository, path, commit, artifact, readiness state, evidence, and known coverage gaps.

At least one reviewed source must support the handoff:

- Approved PRD plus released implementation evidence
- Released implementation summary
- Reviewed product decision
- Reviewed walkthrough output created with `templates/walkthrough-output-template.md`
- Confirmed correction to existing documentation

And:

- Product identifier when product-specific
- Initiative or change identifier
- Access to `manifest.generated.json` and relevant repository knowledge

Optional sources:

- Design specification
- Technical notes
- Release notes
- Screenshots or recordings
- Jira tickets
- QA findings

A confirmed correction made directly in this repository may proceed without a cross-repository handoff when its evidence, reviewer, and affected scope are explicit.

## Required templates

Use canonical document templates when creating or materially restructuring Product Knowledge:

```text
templates/product-overview-template.md
templates/capability-template.md
templates/flow-template.md
templates/domain-template.md
templates/decision-template.md
```

Use these workflow contracts:

```text
templates/workflows/product-knowledge-handoff-template.yaml
templates/workflows/product-knowledge-update-proposal-template.md
```

See `docs/product-work-handoff.md` for readiness, idempotency, completion acknowledgement, and stop conditions.

Do not duplicate or shorten template structures inside this Skill output.

## Core principles

```text
Source material
→ Evidence and approved change intent

Canonical repository knowledge
→ Permanent current understanding after human review
```

- Observed production behavior does not automatically become an intended business rule.
- Every durable fact has one canonical owner.
- Related documents reference or apply owned facts rather than redefining them.
- Missing evidence, incomplete coverage, and repository indexing gaps remain visible.
- A released change updates only the documents whose owned facts changed.
- A handoff routes reviewed evidence; it does not become a source of truth by itself.

## Workflow

### 1. Validate handoff identity and readiness

When a handoff is provided, verify:

- `schema_version` is supported.
- `handoff_id` is stable and unique.
- Product and source artifact type are present.
- Source repository, path, and immutable commit are present.
- Evidence references are accessible.
- A repeated handoff reuses or updates the existing documentation PR rather than creating an unrelated duplicate.

For a released-change handoff, require:

```text
approval_state: approved
release_state: released
```

For a walkthrough handoff, require:

```text
review_state: reviewed
```

Stop when source identity or readiness is missing. Do not use a mutable branch name as the only source identity.

### 2. Establish scope

Extract:

- Product or shared collection
- Capability or affected area
- Released change or reviewed recovery scope
- Actors and roles
- Usage contexts covered
- Source documents and source commit
- Release, approval, or review status
- Affected stable IDs supplied as discovery hints
- Known coverage gaps and suspected bugs

Do not update canonical Product Knowledge for unreleased work.

Affected IDs in the handoff do not authorize editing every listed document. Canonical ownership must still be determined fact by fact.

### 3. Validate source readiness

For release-based updates, require evidence that the approved change is released as current behavior. Record known differences between intended and released behavior.

For walkthrough-based updates, require:

- Explicit scope, actor, role, authentication state, and environment
- Surface and entry-point inventory
- Coverage matrix
- Evidence index
- Separation of observed, inferred, unknown, blocked, and suspected-bug findings
- Visible untested areas
- Human review of the walkthrough output

Do not convert an incomplete raw walkthrough directly into canonical documents.

### 4. Validate repository readiness

Follow `ai/retrieval-rules.md`.

Before selecting documents:

- Confirm `manifest.generated.json` exists.
- Confirm it is current when repository tooling is available.
- Inspect the manifest summary and `unindexed` list.
- Stop when the manifest is missing or stale.
- Surface relevant unindexed or unverified knowledge as a repository coverage gap.

Do not silently replace manifest discovery with filename globbing.

### 5. Find the smallest sufficient knowledge set

Select by collection, product, type, summary, and related IDs.

Relevant Product Knowledge may include:

- Product overview
- Capability
- Flow
- Domain
- Accepted Decision

Relevant shared knowledge may include:

- Design System
- Content
- Product Standard
- Shared Domain

Interpret truth states consistently:

```text
canonical
→ Approved current truth

observed
→ Current evidence whose intended meaning is not confirmed

unverified
→ Content or metadata awaiting semantic confirmation

deprecated
→ Historical context, not current truth
```

### 6. Classify each finding

Use:

```text
confirmed
observed
inferred
unknown
blocked
suspected-bug
```

Route them as follows:

```text
confirmed
→ Candidate canonical patch

observed
→ Evidence; canonical only after intended meaning is confirmed

inferred
→ Assumption or open question, never canonical by itself

unknown | blocked
→ Coverage gap or open question

suspected-bug
→ Proposed bug ticket, not an intended rule
```

Preserve handoff coverage gaps and suspected bugs even when the main released path is understood.

### 7. Determine canonical ownership

For Product Knowledge:

```text
Product overview
→ Product purpose, boundaries, main Capabilities, and major user journeys

Domain
→ Stable business rules, permissions, lifecycle constraints, and entity relationships

Capability
→ Durable product ability, actors, entry points, availability, Capability-specific states, and high-level behavior

Flow
→ Actor, outcome, trigger, preconditions, steps, branches, validations, transitions, errors, recovery, persistence, and end states

Decision
→ Durable approved rationale requiring historical context
```

For shared collections:

```text
Design System
→ Reusable foundations, tokens, Components, Patterns, accessibility, variations, and governance

Content
→ Cross-product content guidance

Product Standard
→ Cross-product product or documentation rules

Shared Domain
→ Stable business concepts and rules genuinely shared by products
```

For each affected document choose:

- `update`
- `reference update only`
- `no change`
- `review required`
- `new document required`

Do not create standalone Journey, Feature, User Goal, Scenario, Rule, State, Lifecycle, or Subdomain documents.

### 8. Evaluate Decision impact

Create or update a canonical Decision only when the approved rationale is durable, such as when the change:

- Establishes a significant rule or intentional exception
- Changes permission, lifecycle, ownership, or product boundaries
- Resolves a material trade-off between reasonable alternatives
- Is likely to be questioned or reopened later
- Affects several canonical documents

A Decision records why. The Product overview, Domain, Capability, Flow, or shared document still owns the resulting current truth.

When superseding a Decision:

- Mark the previous Decision as superseded.
- Set `superseded_by` on the previous Decision.
- Set `supersedes` on the new Decision.
- Preserve historical rationale.

### 9. Prepare the update proposal

Copy and complete:

```text
templates/workflows/product-knowledge-update-proposal-template.md
```

For every proposed patch record:

- Stable document ID
- Canonical owner
- Changed fact
- Reason
- Source commit or evidence reference
- Classification
- Required reviewer
- Proposed diff

Record the `handoff_id` so retries can find the same proposal and PR.

Do not rewrite entire documents unless their structure is fundamentally unusable.

### 10. Prepare template-compliant patches

When creating or materially updating a file:

- Use the matching canonical template.
- Preserve its stable ID.
- Use the common `collection` and `type` metadata envelope.
- Update `related` IDs through manifest-resolvable identifiers.
- Update `last_verified` only after actual review.
- Keep `knowledge_state` separate from `document_maturity`.
- Add evidence or source references.
- Preserve Coverage and Unknowns sections where required.
- Do not remove blocked or untested cases merely to make the document appear complete.

### 11. Validate document and repository quality

Before presenting the final diff, run:

```bash
python scripts/knowledge.py generate
python scripts/knowledge.py check --strict
```

Verify that:

- Every indexable document has the common metadata envelope.
- Collection and type are compatible.
- IDs are unique.
- Related IDs resolve through the manifest.
- A scaffold is not canonical.
- Canonical documents contain substantive owned facts.
- Facts have evidence or an approved source.
- Observations and inferences are separated.
- Unknowns are not written as canonical facts.
- Coverage limitations remain explicit.
- Rules are stored in the correct canonical owner.
- No obsolete Journey or Feature type, template, or folder is introduced.
- `manifest.generated.json` is current and has no unexplained indexing regression.

### 12. Stop on sensitive semantic changes

Require explicit human review for:

- New or changed business rules
- Permission changes
- Lifecycle changes
- Entity relationship changes
- Removal of an existing rule
- Change from observed or unverified behavior to canonical intended behavior
- Generalization from one role, account, environment, or context to all users
- Conflicts between PRD and production
- Moving product-specific knowledge into a shared collection
- Changing canonical ownership
- Accepting, superseding, or deprecating a Decision

### 13. Present a reviewable diff

When repository access is available:

```text
Create or reuse a dedicated branch for the handoff
→ edit only affected files
→ regenerate the manifest
→ run strict validation
→ present the semantic and metadata diff
→ wait for explicit human approval
→ merge after approval
```

Do not write directly to `main`.

### 14. Acknowledge completion to the source

After merge, update the source handoff when source-repository access is available:

```yaml
repository_update:
  status: completed
  pull_request: URL
  merge_commit: full-commit-sha
  completed_at: YYYY-MM-DD
```

If the source repository is unavailable, report that acknowledgement remains pending. Do not claim an end-to-end completed lifecycle.

### 15. Complete the update

The update is complete when:

- Confirmed changes are reflected in their canonical owners.
- Related documents reference rather than redefine owned facts.
- Unknowns, blocked areas, and meaningful untested cases remain visible.
- Suspected bugs are not recorded as intended rules.
- Sensitive changes have explicit approval.
- Durable rationale is preserved in Decisions when required.
- Metadata and relationships pass strict validation.
- The generated manifest is current.
- No important confirmed knowledge remains only in a PRD or walkthrough output.
- The documentation diff is merged.
- The source handoff is acknowledged, or the missing source access is explicitly reported.

## Human responsibilities

Humans are responsible for:

- Confirming semantic meaning
- Approving business rules and permissions
- Resolving conflicts
- Accepting coverage limitations
- Approving durable Decisions
- Approving the final documentation diff

## Rules

- Do not update canonical knowledge before release.
- Do not turn observation or inference into intended truth without approval.
- Do not hide source, repository-indexing, or coverage gaps.
- Do not duplicate canonical facts.
- Do not create custom document shapes that omit required metadata or quality sections.
- Do not duplicate workflow template structures inside this Skill.
- Do not create duplicate PRs for the same `handoff_id`.
