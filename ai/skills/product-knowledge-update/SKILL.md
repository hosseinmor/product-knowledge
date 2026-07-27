# Product Knowledge Update

## Purpose

Update Product Knowledge after an approved product change has been released, or recover missing current behavior from a reviewed Product Walkthrough.

The AI prepares changes. Humans validate meaning and approve the final diff.

## Inputs

At least one reviewed change source:

- Approved PRD plus released implementation evidence
- Released implementation summary
- Reviewed product decision
- Reviewed Product Walkthrough output
- Confirmed correction to existing documentation

And:

- Product identifier
- Initiative, release, correction, or walkthrough identifier
- Access to relevant Product Knowledge

Optional supporting evidence:

- Design specification
- Technical notes
- Release notes
- Screenshots and recordings
- Jira tickets
- QA findings
- Analytics or logs

## Required templates

Use the official document templates in `/templates`:

```text
product-overview-template.md
capability-template.md
flow-template.md
domain-template.md
decision-template.md
```

Do not use or recreate Journey or Feature templates.

When a required section has no established content, write one of:

```text
Unknown
Not yet verified
Not applicable — {reason}
```

Do not silently omit a material section merely because the source is incomplete.

## Core principles

```text
Source material
→ evidence and approved change intent

Product Knowledge
→ durable current understanding
```

- Observed production behavior must not automatically become an intended business rule.
- Inferences from a walkthrough cannot become canonical facts without human confirmation.
- Every durable fact must have one canonical owner.
- Related documents may reference or apply a fact but must not independently redefine it.
- Proposed or unreleased behavior remains in `product-work`.
- Evidence and coverage limits must remain visible in created or updated documents.

## Workflow

### 1. Establish scope and source quality

Extract:

- Product and affected area
- Released change or recovered current behavior
- Actors, roles, authentication states, and environments covered
- Source documents and evidence
- Release or review status
- Material gaps, blocked cases, and untested cases

For a walkthrough source, require:

- `status: reviewed`
- Declared scope and exclusions
- Surface inventory
- Coverage matrix
- Evidence index
- Separation of observed facts, inferences, unknowns, blocked areas, untested cases, and suspected bugs
- Human review notes

A walkthrough that lacks these elements is source material requiring further review, not sufficient input for canonical recovery.

Do not update Product Knowledge for unreleased work unless the repository explicitly supports future-state documentation.

### 2. Find relevant Product Knowledge

Follow `ai/retrieval-rules.md`.

Use the generated manifest when available to discover the smallest sufficient set of documents, then read only relevant documents from:

- Shared knowledge
- Product overview
- Capability
- Flow
- Domain when stable business truth is involved
- Accepted Decision when durable rationale is involved

Check document metadata before using the content:

- Prefer `knowledge_state: canonical`
- Surface `observed` content as unconfirmed
- Ignore `deprecated` content as current behavior
- Use `document_maturity` as a review signal, not as truth status

### 3. Classify every proposed fact

Use:

```text
confirmed
observed
inferred
unknown
blocked
not-tested
suspected-bug
```

Route them as follows:

```text
confirmed
→ eligible for a Product Knowledge patch

observed
→ observed knowledge or a review question; not automatically an intended rule

inferred
→ assumption or review question; never canonical without confirmation

unknown
→ explicit Unknown section or open question

blocked
→ coverage gap and follow-up requirement

not-tested
→ coverage gap; never represented as absent behavior

suspected-bug
→ proposed bug investigation, not a canonical rule
```

A human reviewer must approve promotion from observed or inferred to confirmed.

### 4. Determine canonical ownership

For each confirmed fact, identify one owner:

```text
Product overview
→ product purpose, boundaries, major Capabilities, and major user journeys

Domain
→ stable business rules, permissions, lifecycle constraints, vocabulary, entities, and relationships

Capability
→ durable product ability, actors, user outcomes, entry points, availability, Capability-specific states, and high-level behavior

Flow
→ actor, user outcome, trigger, preconditions, context, steps, branches, validations, transitions, errors, recovery, cancellation, persistence, and end states

Decision
→ durable approved rationale requiring historical context

Shared
→ cross-product knowledge whose meaning and ownership are genuinely consistent
```

Do not create standalone Journey, Feature, User Goal, Scenario, Rule, State, Lifecycle, or Subdomain documents. Represent those concepts inside their owning Product overview, Capability, Flow, or Domain.

For each relevant document choose:

- `update`
- `reference update only`
- `no change`
- `review required`
- `new document required`

Update the canonical owner first. Update references or local applications only where needed.

### 5. Determine document shape and completeness

Create new documents from the official template for their type.

For every created or materially updated document verify:

- Required frontmatter exists
- `id` is stable and repository-wide
- `type` is one of product, capability, flow, domain, decision, or shared
- `knowledge_state` and `document_maturity` are separate
- `related` uses stable IDs
- Evidence and source references support material facts
- Coverage states what was and was not verified
- Unknowns remain explicit
- No template section is filled with invented content

A document can be:

```yaml
knowledge_state: canonical
document_maturity: draft
```

when confirmed facts are current but coverage or documentation remains incomplete.

### 6. Evaluate Decision impact

A working decision, Jira item, meeting outcome, or PRD statement does not automatically require a canonical Decision document.

Create or update a Decision only when the approved rationale is durable, such as when the change:

- Establishes a significant rule or intentional exception
- Changes permissions, lifecycle, ownership, or product boundaries
- Resolves a material trade-off between reasonable alternatives
- Is likely to be questioned or reopened later
- Affects several Product Knowledge documents

The Decision records why. The Product overview, Domain, Capability, or Flow still owns the resulting current behavior.

When a new Decision replaces an old one:

- Mark the previous Decision as `superseded`
- Reference the new Decision with `superseded_by`
- Reference the previous Decision from the new one with `supersedes`
- Preserve historical rationale

### 7. Prepare patches

Edit only affected sections unless the existing document uses an obsolete structure that prevents correct ownership or coverage.

For every patch record:

- Reason
- Source and evidence
- Classification
- Canonical owner
- Coverage impact
- Required reviewer

When a file is created or materially updated:

- Use the official template
- Keep or assign its stable `id`
- Update `related` IDs
- Update `last_verified` only when the content was actually reviewed
- Keep `knowledge_state` separate from `document_maturity`
- Preserve Unknowns and known coverage gaps

### 8. Stop on sensitive semantic changes

Require explicit human review for:

- New or changed business rules
- Permission changes
- Lifecycle changes
- Entity relationship changes
- Removal of an existing rule
- Promotion from observed or inferred to canonical
- Generalization from one actor, role, state, or environment to all users
- Conflicts between PRD, walkthrough evidence, implementation, and existing Product Knowledge
- Moving product-specific knowledge into `shared/`
- Changing canonical ownership
- Accepting, superseding, or deprecating a Decision
- Claiming complete coverage while material gaps remain

### 9. Validate before opening a PR

Run this quality gate:

```text
[ ] Every changed fact has a source and classification
[ ] Every confirmed fact has one canonical owner
[ ] Inferences are not written as current truth
[ ] Unknown, blocked, and not-tested cases remain visible
[ ] New documents use official templates
[ ] Journey and Feature document types are absent
[ ] Metadata and related IDs are valid
[ ] Evidence and coverage sections are present where required
[ ] Product behavior and design-system behavior are not mixed
[ ] No unrelated files are changed
```

Do not open a documentation PR as complete when this gate fails. Present the failure and required follow-up instead.

### 10. Present a reviewable diff

Use:

```md
# Product Knowledge Update Proposal

## Scope
## Sources and Evidence Reviewed
## Source Quality and Coverage
## Fact Classification
## Documentation Impact
## Canonical Ownership
## Proposed Patches
## Decision Impact
## Metadata and Relationship Changes
## Unknowns and Untested Cases
## Suspected Bugs
## Review Required
## Files With No Change
```

When repository access is available:

```text
create branch
→ edit only affected files
→ rebuild the generated manifest when tooling exists
→ validate templates, metadata, evidence, and coverage
→ show diff
→ wait for human approval
→ merge only after approval
```

### 11. Complete the update

The update is complete when:

- All confirmed changes are reflected in their canonical owner documents
- Related documents reference rather than redefine owned facts
- Inferences are absent from canonical truth unless confirmed
- Unknowns and coverage limits remain visible
- Suspected bugs are not recorded as rules
- Sensitive changes are approved
- Durable rationale is preserved in Decisions when required
- Metadata and relationships remain valid
- No important confirmed knowledge remains only in a PRD or walkthrough output
- The documentation diff is merged

## Human responsibilities

Humans are responsible for:

- Confirming semantic meaning and intended behavior
- Reviewing walkthrough evidence and coverage
- Promoting observations or inferences to confirmed facts
- Approving business rules, permissions, and lifecycle meaning
- Resolving conflicts
- Approving durable Decisions
- Approving the final documentation diff
