# Product Walkthrough

> Temporary evidence document. Store completed copies in `product-work`, not in Product Knowledge.

## Walkthrough metadata

```yaml
walkthrough_id: walkthrough-id
product: product-id
product_area: area-id
actor: actor-or-role
authentication_state: logged-out | logged-in | mixed
environment: production | staging | local
status: in-progress | ready-for-review | reviewed
reviewer: role-or-person
reviewed_at: YYYY-MM-DD
```

## Scope

### Included areas

### Excluded areas

### Known entry points

### Constraints and safety limits

## Surface inventory

Record discovered pages, navigation items, actions, forms, filters, dialogs, drawers, empty states, error states, authentication gates, permission gates, and external redirects.

## Actions executed

| Step | Starting context | Action | Immediate response | Navigation or state change | Evidence |
|---|---|---|---|---|---|

## Flow observations

For each observed behavior include actor, user outcome, entry point, trigger, preconditions, main path, branches, validations, state transitions, errors, recovery, cancellation, end state, persistence, and return behavior.

## Coverage matrix

Allowed statuses:

```text
observed
blocked
not-tested
not-applicable
unknown
```

| Area or behavior | Actor and access state | Case or branch | Status | Evidence or reason |
|---|---|---|---|---|

## Authentication and permission gates

## Branch and error coverage

Review or explicitly mark these cases when relevant:

- Success
- Empty state
- Validation failure
- Authentication required
- Permission denied
- Cancellation or exit
- Retry and recovery
- Network or server error
- Already completed state
- Duplicate action
- Boundary values
- Refresh, revisit, or return behavior

## Errors and anomalies

## Observed facts

Record only what the walkthrough directly demonstrated.

## Inferences

Label every interpretation that was not directly demonstrated.

## Unknowns

## Blocked areas

## Untested material cases

## Suspected bugs

## Evidence index

| Evidence ID | Type | Location or reference | Supports |
|---|---|---|---|

## Candidate capabilities

Candidates require human review before becoming Product Knowledge.

## Candidate flows

## Candidate domain rules

## Candidate decision questions

## Open questions

## Completeness assessment

State the reviewed scope, material gaps, and confidence. Do not mark the walkthrough complete while material `not-tested`, `blocked`, or `unknown` cases remain undisclosed.

## Human review

- Reviewer:
- Review date:
- Approved observations:
- Rejected or corrected observations:
- Follow-up required:
