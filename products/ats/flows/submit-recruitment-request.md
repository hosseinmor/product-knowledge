---
id: ats.flow.submit-recruitment-request
collection: product
type: flow
product: ats
title: Submit Recruitment Request
summary: Describes the known path, validations, branches, and state transition when a Request Owner submits a draft Recruitment Request for approval.
knowledge_state: unverified
document_maturity: draft
related:
  - ats
  - ats.domain.recruitment-request
  - ats.capability.manage-recruitment-request
owner: ats-product
actors:
  - request-owner
capabilities:
  - ats.capability.manage-recruitment-request
domains:
  - ats.domain.recruitment-request
source_refs:
  - product-discussion:ats-recruitment-request-2026
---

# Submit Recruitment Request

## Scope

This Flow begins when a Request Owner attempts to submit a draft Recruitment Request and ends when the request either enters the first approval step or remains a draft with an explicit blocking condition.

Approver actions after successful submission belong to separate approval and rejection Flows.

## Actor and User Outcome

### Actor

Request Owner

### User outcome

Send a complete hiring request to the appropriate approval process and receive a clear indication that review has started.

## Entry Points

Known entry point:

- Recruitment Request create or edit experience while the request is in Draft

Potential entry points that require verification:

- Request detail page
- Draft row action in the request list
- Resume-later link from a previous incomplete submission

## Trigger

The Request Owner activates the Submit action.

The current documentation does not establish the exact Persian label or whether the action is represented as a page button, step action, or confirmation modal.

## Preconditions

Required known conditions:

- The request exists in Draft.
- The actor has permission to submit it.
- Required request information is complete.
- An applicable Approval Workflow has been selected or resolved.
- The workflow contains a valid first step.
- The active workflow step has at least one valid approver.

The exact required fields and workflow-resolution rules remain unverified.

## Relevant Context

Submission may depend on organizational context such as department and branch. Some customer accounts may not use branches.

The product must not assume that every account has the same organization hierarchy.

## Main Path

1. The Request Owner opens or completes a draft Recruitment Request.
2. The product presents the Submit action when submission is available.
3. The Request Owner activates Submit.
4. The system validates required request fields, actor permission, and applicable workflow readiness.
5. The system associates the request with the applicable Approval Workflow.
6. The system records the submitted request as In review.
7. The first Approval Step becomes active.
8. The product confirms that the request has entered review and shows its current approval progress.

Notification delivery to approvers is expected but has not been verified and is not asserted as a confirmed step.

## Decision Points and Branches

### Required information is incomplete

```text
Validation fails
→ request remains Draft
→ missing or invalid information is identified
→ actor can correct the request and retry
```

### No applicable workflow exists

```text
No workflow matches the selected conditions
→ request remains Draft
→ submission is blocked
→ product explains that no workflow is available for the selected conditions
```

It remains open whether the actor can change organizational fields, request administrator support, or use a default workflow.

### Workflow is structurally invalid

```text
Workflow has no valid first step or approver
→ request remains Draft
→ submission is blocked
→ issue requires correction by an authorized workflow administrator
```

### Actor lacks permission

```text
Permission validation fails
→ no state transition occurs
→ submit action is unavailable or request is rejected by the system
```

The expected UI treatment and recovery path are unverified.

### Concurrent change

A workflow or request may change between page load and submission. The system's conflict resolution and retry behavior are not documented.

## Validations

Known validation categories:

- Required request fields
- Requested capacity and other numeric constraints
- Actor authorization
- Applicable workflow availability
- Approval-step existence
- Valid approver availability
- Current request state

Field-level validation messages and validation timing require production verification.

## State Transitions

Successful submission:

```text
Recruitment Request: Draft → In review
First Approval Step: Inactive → Active
```

Unsuccessful submission:

```text
Recruitment Request: Draft → Draft
```

Whether submission immediately locks every structural request field or only begins restrictions after the first approver action remains a Domain open question.

## Alternate Paths

### Submission confirmation

The product may require confirmation before committing submission. Current discussions do not establish whether this confirmation is mandatory.

### Automatic workflow resolution

The product may resolve the workflow from branch and department rather than requiring manual selection. The resolution algorithm is not documented.

### Account without branch structure

The Flow must continue without requiring branch data when the customer account does not use branches.

## Error and Recovery Paths

### Recoverable validation error

The request remains Draft, entered information is preserved, and the actor can correct the issue and retry.

### Server or network error

Expected safe behavior:

- Do not create an ambiguous duplicate submission.
- Preserve the draft when the state transition is not committed.
- After retry or refresh, show the actual persisted request state.

This behavior is a recommended safety expectation and has not been observed in production.

### Partial submission failure

The system must not show the request as Draft to the owner while activating an approval step for approvers. Transactionality and reconciliation behavior require technical verification.

## Cancellation and Exit Behavior

Before a successful submission, the actor should be able to leave while preserving the Draft according to existing draft-save behavior.

Cancellation after successful submission is not part of this Flow and requires a separate lifecycle rule.

## End States

### Successful

- Recruitment Request is In review.
- First Approval Step is active.
- Actor can see current approval progress.

### Blocked but recoverable

- Recruitment Request remains Draft.
- Blocking validation or workflow issue is visible.
- Actor can correct available issues and retry.

### Blocked by permission or administration

- Recruitment Request remains unchanged.
- Actor cannot resolve the issue without permission or workflow-administration changes.

## Persistence and Return Behavior

Known expectation:

- After successful submission and refresh, the request remains In review.
- After a validation failure, entered draft information should remain available.

Not verified:

- Back-button behavior
- Duplicate browser-tab behavior
- Double-submit protection
- Retry after timeout
- Deep-link return after authentication

## Permissions and Authentication Gates

- The actor must be authenticated.
- The actor must have permission to submit the request.
- A workflow administrator may be required to resolve workflow configuration failures.

Formal permission names and inheritance rules are not documented.

## Related Capability

- `ats.capability.manage-recruitment-request`

## Referenced Domain Rules

See `ats.domain.recruitment-request` for:

- Recruitment Request lifecycle
- Approval-step validity
- Step approval rule
- Editability during review
- Workflow dependency restrictions

## Related Decisions

No accepted standalone Decision document is currently linked.

## Evidence

The Flow is based on product-design discussions about submission, workflow selection, state transition, and the empty state where no workflow matches selected organizational conditions.

No complete production walkthrough has yet verified every branch, role, error state, or persistence behavior.

## Coverage

| Area | Status | Notes |
|---|---|---|
| Actor and desired outcome | observed | Confirmed through product discussion, not production observation |
| Draft-to-review main path | observed | Discussion-level behavior |
| Missing required information | observed | Validation requirement known; field details incomplete |
| No applicable workflow | observed | Empty-state need discussed; resolution behavior unknown |
| Invalid workflow or approver | unknown | Expected constraint, production handling not verified |
| Permission denied | not-tested | Role and UI behavior incomplete |
| Network or server failure | not-tested | Safety expectations are recommendations |
| Persistence after refresh | not-tested | Requires walkthrough |
| Double submission | not-tested | Requires technical and production verification |
| Account without branches | observed | Account variation is known; exact Flow behavior incomplete |

## Unknowns and Untested Cases

- Exact required-field list
- Workflow matching and fallback algorithm
- Submit confirmation behavior
- Notification side effects
- Field-level locking after submission
- Concurrent workflow changes
- Idempotency and duplicate submission
- Network recovery
- Accessibility and keyboard behavior
- Mobile or responsive variation
