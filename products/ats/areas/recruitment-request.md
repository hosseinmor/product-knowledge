# Recruitment Request

Status: Draft
Owner: ATS product team
Last reviewed:

## Overview

Recruitment Request lets an organization turn an internal hiring need into a structured request, route it through an approval process, and continue it into hiring after approval.

The request remains the business record through approval and hiring. It is not the same entity as a Job, although one or more Jobs or hiring activities may help fulfill its requested capacity.

The current document is based on product-design discussions and still needs review against production behavior and current PM intent.

## Users and roles

### Request Owner

Creates and submits the request and follows its progress until the hiring need is fulfilled.

### Approver

Reviews the request at an assigned approval step and approves or rejects it.

### Workflow Administrator

Configures which Approval Workflow applies and maintains approvers without breaking active requests.

### Recruiting or HR user

Turns an approved request into hiring work and tracks progress against requested capacity.

Exact role names, permission inheritance, delegation, and account differences remain incomplete.

## Entry points

Known or expected entry points include:

- Recruitment Request list
- Create Recruitment Request action
- Recruitment Request detail page
- Approval task or notification linking to a request
- Approval Workflow management
- Approved request entry into hiring work

Notification and deep-link behavior are not verified.

## Main concepts

### Recruitment Request

A record of an internal hiring need. It includes requested capacity and the organizational context needed to select or validate an Approval Workflow.

### Approval Workflow

An ordered set of Approval Steps that applies to a request under defined organizational conditions.

### Approval Step

One stage of an Approval Workflow. A step contains one or more Approvers.

### Approver

A user who can approve or reject a request at an active step.

### Requested Capacity

The number of hires needed for the request.

### Fulfillment

The condition in which all requested hiring capacity has been filled.

### Active Request Dependency

A relationship in which an Approval Workflow is already used by an active request.

## Main behavior

```text
Create draft request
→ complete hiring-need information
→ select or resolve an applicable Approval Workflow
→ submit for review
→ progress through Approval Steps
→ approve or reject
→ resubmit after rejection when needed
→ enter hiring after final approval
→ continue until requested capacity is fulfilled
```

## Main flows

### Create a request

The Request Owner creates a Draft and provides the information required to describe the hiring need.

The exact required fields, draft-save behavior, and organizational fields still need documentation.

### Submit a request

**Actor and goal**

The Request Owner wants to send a complete request to the correct approval process and see that review has started.

**Preconditions**

- The request is in Draft.
- The actor has permission to submit it.
- Required information is complete.
- An applicable Approval Workflow has been selected or resolved.
- The workflow has a valid first step and at least one valid Approver.

**Main path**

1. The Request Owner completes the Draft.
2. The product makes the Submit action available.
3. The actor submits the request.
4. The system validates fields, permission, request state, and workflow readiness.
5. The request is associated with the applicable Approval Workflow.
6. The request changes from Draft to In review.
7. The first Approval Step becomes active.
8. The product shows that review has started and displays current progress.

**Important branches**

Incomplete information:

```text
Validation fails
→ request remains Draft
→ missing or invalid information is identified
→ actor corrects it and retries
```

No applicable workflow:

```text
No workflow matches the selected conditions
→ request remains Draft
→ submission is blocked
→ product explains that no workflow is available for the selected conditions
```

Invalid workflow or Approver:

```text
Workflow has no valid first step or Approver
→ request remains Draft
→ submission is blocked
→ an authorized administrator must correct the workflow
```

Permission failure:

```text
Actor lacks submission permission
→ no state transition occurs
→ action is unavailable or rejected
```

**Success outcome**

- The request is In review.
- The first Approval Step is active.
- The Request Owner can see current approval progress.

**Recovery expectations**

- Validation failure should preserve entered Draft information.
- Failed submission should not create an ambiguous duplicate request or approval step.
- Refresh should show the persisted state.

Network, timeout, duplicate-submit, and concurrent-edit behavior have not been verified.

### Approve a request

An Approver acts when the request is at a step assigned to them.

The currently documented rule is that at least one Approver in the active step must approve for the step to be considered approved.

The behavior of other Approvers after the minimum approval condition is met is unknown.

After the final Approval Step, the request enters its hiring phase. It is not replaced by an unrelated entity.

### Reject a request

Rejecting a request requires a reason.

The exact UI, notification behavior, and resulting state history still need documentation.

### Resubmit a rejected request

The Request Owner may resubmit a rejected request without being forced to change its fields. The rejection reason should remain relevant context for the next review.

### Edit during review

The discussion-level rule is:

```text
Request submitted
→ editable until the first approval action
→ structurally locked after an approval or rejection action
```

The exact fields that remain editable at each stage are unknown.

### Continue into hiring and fulfillment

After final approval, the request enters hiring. The request is fulfilled when all requested capacity has been filled.

The relationship between a request, multiple Jobs, partial fulfillment, and individual hires needs review.

### Cancel or close a request

Cancellation and closure are not yet defined. The allowed actors, states, reasons, downstream effects, and reopen behavior remain open questions.

## Rules and constraints

- Submission requires complete information and an applicable Approval Workflow.
- At least one Approver's approval is sufficient for the active step under the current discussion-level rule.
- Rejection requires a reason.
- A rejected request can be resubmitted without mandatory field changes.
- Structural editing becomes restricted after an Approver acts.
- Final approval moves the request into hiring.
- The request is fulfilled when requested hiring capacity is filled.
- Role-based Approver selection is not part of the currently documented behavior; Approvers are selected users.

### Editing an Approval Workflow with active requests

When active requests depend on a workflow:

- Existing Approval Steps must not be removed or reordered.
- Existing Approvers must not be removed.
- New Approvers may be added to existing steps.
- Added Approvers apply to dependent active requests.

When no active request depends on the workflow, it may be fully edited.

The current model does not create a separate workflow version for each edit.

## Permissions

Known expectations:

- A Request Owner can create and submit a request when information is complete and the account permits it.
- An Approver can act only at an active step assigned to them.
- A Workflow Administrator can fully edit workflows without active dependencies.
- With active dependencies, the administrator can add Approvers but cannot remove or restructure existing steps.

Not yet established:

- Formal role names
- Account-level permission inheritance
- Delegation
- Administrator overrides
- Cancellation and closure permission
- Behavior when an Approver is deactivated or loses access

## States and transitions

Known lifecycle:

```text
Draft
→ In review
→ Approved
→ Hiring
→ Fulfilled
```

Rejection path:

```text
In review
→ Rejected
→ Resubmitted
→ In review
```

The exact naming and persistence of Approved versus Hiring must be verified. Cancellation, closure, archival, and partial-fulfillment states are undefined.

## Validations

Known validation categories include:

- Required request fields
- Requested capacity and numeric constraints
- Actor authorization
- Current request state
- Applicable workflow availability
- Approval-step existence
- Valid Approver availability

Field-level messages and validation timing are not documented.

## Edge cases and variations

- Some customer accounts do not use branches.
- Workflow selection may depend on department, branch, or other organizational context.
- No matching workflow may exist for the selected conditions.
- A workflow may change between page load and submission.
- An Approver may be deactivated while requests are active.
- A request may be fulfilled through more than one Job or hiring activity.
- Partial fulfillment, cancellation, closure, and archival are not defined.
- Notification, activity history, and audit-log behavior are incomplete.
- Server error, timeout, retry, double submission, and multi-tab behavior are untested.

## Related Product Areas

- Approval Workflow — separate document not yet created
- Job Management — separate document not yet created
- Candidate Management — separate document not yet created

## Related shared concepts and rules

Organization, branch, department, user account, access, and notification concepts may need shared documentation after ownership is clarified.

## Design references

Add links to the relevant ATS Figma pages and shared Design System components and patterns as they are reviewed.

## Unknowns and untested cases

- Exact required-field list
- Workflow matching and fallback logic
- Manual versus automatic workflow selection
- Field-level editability by state
- Notification and reminder behavior
- Approval delegation and escalation
- Approved versus Hiring state persistence
- Cancellation and closure
- Partial fulfillment and multiple Jobs
- Deactivated Approvers
- Network recovery and duplicate submission
- Accessibility, keyboard, mobile, and responsive behavior

## Sources

This document consolidates the previous Recruitment Request Capability, Domain, and Submit Flow documents. Their source was a set of 2026 product-design discussions, not a complete production walkthrough.
