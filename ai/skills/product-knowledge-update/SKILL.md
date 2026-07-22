# Product Knowledge Update

## Purpose

Update canonical Product Knowledge after an approved product change has been released, or after missing current behavior has been recovered through a reviewed walkthrough.

The AI prepares the changes. Humans validate meaning and approve the final diff.

## Inputs

At least one change source:

- Approved PRD
- Released implementation summary
- Reviewed product decision
- Reviewed walkthrough output
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

## Core principle

```text
Source material = evidence and approved change intent
Product Knowledge = permanent canonical understanding
```

Observed production behavior must not automatically become an intended business rule.

## Workflow

### 1. Establish scope

Extract:

- Product
- Feature or capability
- Released change
- Actors and roles
- Scenarios covered
- Source documents
- Release status

Do not update canonical documentation for unreleased work unless the repository explicitly supports future-state documentation.

### 2. Find relevant canonical documents

Read only relevant documents from:

- Shared knowledge
- Product overview
- Feature
- Flow
- Domain
- Journey
- Approved decisions

### 3. Classify each change

Use:

- `confirmed`
- `observed`
- `unknown`
- `suspected-bug`

Route them as follows:

```text
confirmed
→ canonical document patch

observed
→ current behavior note or open question

unknown
→ open question

suspected-bug
→ proposed bug ticket, not a canonical rule
```

### 4. Determine documentation impact

For each relevant document choose:

- `update`
- `no change`
- `review required`
- `new document required`

Use these destinations:

```text
Feature
→ capability, actors, entry points, states, high-level behavior

Flow
→ steps, transitions, validations, alternate paths, errors

Domain
→ stable business rules, permissions, lifecycle constraints, entity relationships

Journey
→ high-level user stages and major cross-feature transitions

Decision
→ durable approved decision requiring historical context

Shared
→ cross-product knowledge whose meaning is consistent across products
```

### 5. Prepare patches

Edit only affected sections.

For every patch include:

- Reason
- Source
- Classification
- Required reviewer

Do not rewrite entire documents unless their structure is fundamentally unusable.

### 6. Stop on sensitive semantic changes

Require explicit human review for:

- New business rules
- Permission changes
- Lifecycle changes
- Entity relationship changes
- Removal of an existing rule
- Change from current to intended behavior
- Generalization from one role or scenario to all users
- Conflicts between PRD and production
- Moving product-specific knowledge into `shared/`

### 7. Present a reviewable diff

Use:

```md
# Product Knowledge Update Proposal

## Scope
## Sources Reviewed
## Documentation Impact
## Proposed Patches
## Open Questions
## Suspected Bugs
## Review Required
## Files With No Change
```

When repository access is available:

```text
create branch
→ edit files
→ show diff
→ wait for approval
→ merge only after human approval
```

### 8. Complete the update

The update is complete when:

- All confirmed changes are reflected in canonical documents
- Unknowns remain visible
- Suspected bugs are not recorded as rules
- Sensitive changes are approved
- No important confirmed knowledge remains only in a PRD or walkthrough output
- The documentation diff is merged

## Human responsibilities

Humans are responsible for:

- Confirming semantic meaning
- Approving business rules and permissions
- Resolving conflicts
- Approving the final documentation diff
