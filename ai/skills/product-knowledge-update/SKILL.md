# Product Knowledge Update

## Purpose

Update canonical Product Knowledge after an approved product change has been released, or after missing current behavior has been recovered through reviewed evidence.

AI prepares the evidence classification, ownership analysis, patches, metadata changes, and manifest update. Humans validate semantic meaning and approve the final diff.

## Required inputs

At least one reviewed change source:

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

## Required templates

Use canonical document templates when creating or materially restructuring Product Knowledge:

```text
templates/product-overview-template.md
templates/capability-template.md
templates/flow-template.md
templates/domain-template.md
templates/decision-template.md
```

Use this temporary output template for the review proposal:

```text
templates/workflows/product-knowledge-update-proposal-template.md
```

Do not duplicate or shorten the proposal structure inside this Skill output.

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

## Workflow

### 1. Establish scope

Extract:

- Product or shared collection
- Capability or affected area
- Released change or reviewed recovery scope
- Actors and roles
- Usage contexts covered
- Source documents
- Release or review status

Do not update canonical Product Knowledge for unreleased work.

### 2. Validate source readiness

For release-based updates, require evidence that the change is released or otherwise approved as current behavior.

For walkthrough-based updates, require:

- Explicit scope, actor, role, authentication state, and environment
- Surface and entry-point inventory
- Coverage matrix
- Evidence index
- Separation of observed, inferred, unknown, blocked, and suspected-bug findings
- Visible untested areas
- Human review of the walkthrough output

Do not convert an incomplete raw walkthrough directly into canonical documents.

### 3. Validate repository readiness

Follow `ai/retrieval-rules.md`.

Before selecting documents:

- Confirm `manifest.generated.json` exists.
- Confirm it is current when repository tooling is available.
- Inspect the manifest summary and `unindexed` list.
- Stop when the manifest is missing or stale.
- Surface relevant unindexed or unverified knowledge as a repository coverage gap.

Do not silently replace manifest discovery with filename globbing.

### 4. Find the smallest sufficient knowledge set

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

### 5. Classify each finding

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

### 6. Determine canonical ownership

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

### 7. Evaluate Decision impact

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

### 8. Prepare the update proposal

Copy and complete:

```text
templates/workflows/product-knowledge-update-proposal-template.md
```

For every proposed patch record:

- Stable document ID
- Canonical owner
- Changed fact
- Reason
- Source
- Classification
- Required reviewer
- Proposed diff

Do not rewrite entire documents unless their structure is fundamentally unusable.

### 9. Prepare template-compliant patches

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

### 10. Validate document and repository quality

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

### 11. Stop on sensitive semantic changes

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

### 12. Present a reviewable diff

When repository access is available:

```text
Create a dedicated branch
→ edit only affected files
→ regenerate the manifest
→ run strict validation
→ present the semantic and metadata diff
→ wait for explicit human approval
→ merge after approval
```

### 13. Complete the update

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
- Do not hide repository indexing or coverage gaps.
- Do not duplicate canonical facts.
- Do not create custom document shapes that omit required metadata or quality sections.
- Do not duplicate workflow template structures inside this Skill.
