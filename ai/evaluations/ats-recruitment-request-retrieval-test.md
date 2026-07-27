# ATS Recruitment Request Retrieval Test

## Purpose

Test whether the repository model can retrieve a useful vertical slice for an Initiative-to-PRD workflow without reading the entire repository or confusing unverified knowledge with canonical truth.

This is an evaluation record, not Product Knowledge and not an approved initiative.

## Test Scenario

Hypothetical brief:

```text
Allow a Request Owner to cancel a Recruitment Request after submission.
```

The scenario was selected because cancellation is explicitly incomplete in the current Domain and Flow. A correct workflow should find current constraints and ask blocking questions rather than invent cancellation behavior.

## Expected Manifest Retrieval

Start from:

```text
product: ats
type: product
id: ats
```

Follow related IDs to:

```text
ats.capability.manage-recruitment-request
ats.domain.recruitment-request
ats.flow.submit-recruitment-request
```

Do not retrieve all Design System or product files by default.

## Retrieved Current Context

### Product overview

`ats` establishes that Recruitment Request is a documented ATS area and that cancellation, permissions, and lifecycle coverage remain incomplete.

### Capability

`ats.capability.manage-recruitment-request` establishes the known actors, high-level lifecycle, approval dependency, and current boundary of the product ability.

### Domain

`ats.domain.recruitment-request` owns lifecycle, workflow dependency, approval, rejection, resubmission, and known editability rules. It explicitly states that cancellation and closure are open.

### Flow

`ats.flow.submit-recruitment-request` establishes the Draft-to-In-review transition and defines cancellation after successful submission as outside the current Flow.

## Required Truth Handling

All four documents are:

```text
knowledge_state: unverified
document_maturity: draft
```

Therefore an agent may use them to identify known discussion-level context and gaps, but must not present cancellation behavior or exact lifecycle rules as approved canonical truth.

## Expected Blocking Questions

A correct Initiative-to-PRD run should ask at least:

1. In which request states is cancellation allowed?
2. Which actors can cancel: Request Owner, administrator, recruiting user, or approver?
3. Is cancellation different from closure or rejection?
4. What happens to active approval steps and pending approver tasks?
5. Can a cancelled request be reopened or resubmitted?
6. What reason, confirmation, audit history, and notification are required?
7. What happens when hiring has already started or capacity is partially fulfilled?
8. Does cancellation affect linked Jobs or candidate activity?

These questions materially affect lifecycle, permission, entity relationships, and product behavior, so they are blocking.

## Expected Output Decision

The workflow should prepare `initiative.md` using `templates/workflows/initiative-template.md`, record repository gaps, and stop before producing an approved PRD until the blocking decisions are answered.

It should not:

- Invent a `Cancelled` state as canonical.
- Assume the Request Owner always has permission.
- Treat cancellation as identical to rejection or closure.
- Update Product Knowledge before release.
- Create a standalone Journey or Rule document.

## Result

The vertical slice supplies enough context to:

- Identify the canonical owner candidates for the change.
- Locate relevant current rules without repository-wide reading.
- Distinguish known behavior from missing behavior.
- Generate focused blocking questions.
- Predict Product Knowledge impact after release.

It does not supply enough verified truth to complete the hypothetical PRD without human decisions. That is the correct result for the current maturity level.

## Product Knowledge Impact After a Future Release

A released cancellation change would likely require review of:

```text
ats.domain.recruitment-request
→ lifecycle, permissions, cancellation rules, entity effects

ats.capability.manage-recruitment-request
→ availability and high-level behavior

new or existing cancellation Flow
→ trigger, confirmation, branches, errors, recovery, end state

ats
→ only when the major journey or product boundary changes

Decision
→ only when the cancellation trade-off has durable rationale
```

## Model Learnings

- The `collection + type + related ID` model retrieves a useful minimal set.
- `unverified` prevents discussion-level content from masquerading as approved truth.
- Explicit Coverage and Open Questions sections materially improve blocking-question quality.
- The next model test should use a reviewed production walkthrough to evaluate branch-level completeness rather than adding more taxonomy.
