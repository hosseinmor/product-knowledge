# Product Knowledge Update

## Purpose

Update Product Knowledge after an approved product change has been released, or after missing current behavior has been recovered through a reviewed walkthrough.

The AI prepares the changes. Humans validate meaning and approve the final diff.

## Inputs

At least one reviewed change source:

- Approved PRD plus released implementation evidence
- Released implementation summary
- Reviewed product decision
- Reviewed walkthrough output created with `templates/walkthrough-output-template.md`
- Confirmed correction to existing documentation

And:

- Product identifier
- Initiative or change identifier
- Access to relevant Product Knowledge

Optional:

- Design specification
- Technical notes
- Release notes
- Screenshots
- Recordings
- Jira tickets
- QA findings

## Required templates

Use these repository templates when creating a document or materially restructuring one:

```text
templates/product-overview-template.md
templates/capability-template.md
templates/flow-template.md
templates/domain-template.md
templates/decision-template.md
```

Do not create custom document shapes that omit required metadata, evidence, coverage, or unknowns.

## Core principles

```text
Source material = evidence and approved change intent
Product Knowledge = permanent canonical understanding
```

- Observed production behavior must not automatically become an intended business rule.
- Every durable fact must have one canonical owner.
- Related documents may reference or apply a fact, but must not independently redefine it.
- Missing evidence and incomplete coverage must remain visible.

## Workflow

### 1. Establish scope

Extract:

- Product
- Capability or affected product area
- Released change or reviewed recovery scope
- Actors and roles
- Usage contexts covered
- Source documents
- Release or review status

Do not update Product Knowledge for unreleased work.

### 2. Validate source readiness

For walkthrough-based updates, require:

- Explicit scope, actor, role, authentication state, and environment
- Surface inventory
- Coverage matrix
- Evidence index
- Separation of observed, inferred, unknown, blocked, and suspected-bug findings
- Visible untested areas
- Human review of the walkthrough output

Do not convert an incomplete raw walkthrough directly into canonical documents.

### 3. Find relevant Product Knowledge

Follow `ai/retrieval-rules.md`.

Read the smallest sufficient set from:

- Product overview
- Capability
- Flow
- Domain when stable business truth is involved
- Accepted Decision when durable rationale is involved
- Shared knowledge when meaning and ownership are genuinely cross-product

Check metadata:

- Prefer `knowledge_state: canonical`
- Surface `observed` content as unconfirmed
- Ignore `deprecated` content as current behavior
- Use `document_maturity` as a review signal, not as truth status

### 4. Classify each finding

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
→ candidate Product Knowledge patch

observed
→ observed evidence; canonical only after intended meaning is confirmed

inferred
→ assumption or open question, never canonical by itself

unknown | blocked
→ coverage gap or open question

suspected-bug
→ proposed bug ticket, not a canonical rule
```

### 5. Determine canonical ownership

```text
Product overview
→ product purpose, boundaries, major Capabilities, and major user journeys

Domain
→ stable business rules, permissions, lifecycle constraints, and entity relationships

Capability
→ product ability, actors, entry points, availability, Capability-specific states, and high-level behavior

Flow
→ actor, user outcome, trigger, preconditions, steps, branches, validations, state transitions, errors, recovery, persistence, and end states

Decision
→ durable approved rationale requiring historical context

Shared
→ cross-product knowledge whose meaning and ownership are consistent across products
```

For each document choose:

- `update`
- `reference update only`
- `no change`
- `review required`
- `new document required`

Do not create standalone Journey, Feature, User Goal, Scenario, Rule, State, Lifecycle, or Subdomain documents.

### 6. Evaluate Decision impact

Create or update a Decision only when the approved rationale is durable, such as when the change:

- Establishes a significant rule or intentional exception
- Changes permission, lifecycle, ownership, or product boundaries
- Resolves a material trade-off between reasonable alternatives
- Is likely to be questioned or reopened later
- Affects several Product Knowledge documents

The Decision records why. The Product overview, Domain, Capability, or Flow still owns current behavior.

When superseding a Decision:

- Mark the previous Decision as superseded
- Set `superseded_by`
- Set `supersedes` on the new Decision
- Preserve historical rationale

### 7. Prepare template-compliant patches

Edit only affected sections.

For every patch record:

- Reason
- Source
- Classification
- Canonical owner
- Required reviewer

When creating or materially updating a file:

- Use the matching template
- Add or validate required frontmatter
- Keep the stable `id`
- Update `related` IDs
- Update `last_verified` only after actual review
- Keep `knowledge_state` separate from `document_maturity`
- Add evidence or source references
- Add Coverage and Unknowns sections where required
- Do not remove untested or blocked cases merely to make the document look complete

### 8. Validate document quality

Before presenting the diff, verify:

- The document uses an approved canonical template
- Required sections are present
- Facts have evidence or an approved source
- Observations and inferences are not mixed
- Unknowns are not written as canonical facts
- Coverage limitations remain explicit
- Rules are stored in the correct canonical owner
- Related documents reference rather than duplicate rules
- Metadata types are limited to `product`, `capability`, `flow`, `domain`, `decision`, and `shared`
- No Journey or Feature template, type, folder, or document has been introduced

### 9. Stop on sensitive semantic changes

Require explicit human review for:

- New or changed business rules
- Permission changes
- Lifecycle changes
- Entity relationship changes
- Removal of an existing rule
- Change from observed behavior to intended behavior
- Generalization from one role, account, or context to all users
- Conflicts between PRD and production
- Moving product-specific knowledge into `shared/`
- Changing canonical ownership
- Accepting, superseding, or deprecating a Decision

### 10. Present a reviewable diff

Use:

```md
# Product Knowledge Update Proposal

## Scope
## Sources Reviewed
## Source Readiness and Coverage
## Documentation Impact
## Canonical Ownership
## Proposed Patches
## Decision Impact
## Metadata and Relationship Changes
## Open Questions
## Blocked and Untested Areas
## Suspected Bugs
## Review Required
## Files With No Change
```

When repository access is available:

```text
create branch
→ edit files
→ rebuild the generated manifest when available
→ show diff
→ wait for approval
→ merge only after human approval
```

### 11. Complete the update

The update is complete when:

- All confirmed changes are reflected in their canonical owner documents
- Related documents reference rather than redefine owned facts
- Unknowns, blocked areas, and meaningful untested cases remain visible
- Suspected bugs are not recorded as rules
- Sensitive changes are approved
- Durable rationale is preserved in Decisions when required
- Metadata and relationships remain valid
- No important confirmed knowledge remains only in a PRD or walkthrough output
- The documentation diff is merged

## Human responsibilities

Humans are responsible for:

- Confirming semantic meaning
- Approving business rules and permissions
- Resolving conflicts
- Accepting coverage limitations
- Approving durable Decisions
- Approving the final documentation diff
