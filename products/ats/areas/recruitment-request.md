---
id: ats.recruitment-request
kind: product-area
product: ats
title: Recruitment Request
summary: Explains how ATS creates, submits, approves, rejects, resubmits, and fulfills an internal hiring request.
status: draft
owner: ATS product team
last_reviewed:
related:
  - ats.overview
topics:
  - recruitment-request
  - approval-workflow
  - hiring-capacity
  - permissions
  - lifecycle
---

# Recruitment Request

## Overview

Recruitment Request represents an organization's internal hiring need and its approval process before or during recruiting work.

The request is not the same entity as a Job. After approval, it continues into a hiring phase where one or more jobs and hiring activities may fulfill its requested capacity.

## Why this area exists

- Structure internal hiring needs
- Route requests through the correct approval process
- Keep approval progress, hiring capacity, and fulfillment connected
- Reduce informal coordination between request owners, approvers, and recruiting teams

## Users and roles

- Request Owner: creates, submits, and follows a request
- Approver: approves or rejects at an active step
- Workflow Administrator: configures workflows and approvers
- Recruiting or HR User: acts on approved requests during hiring

Formal role names and permission inheritance require review.

## User outcomes

- Request Owner: submit a complete hiring need and track its progress
- Approver: review and decide with sufficient context
- Workflow Administrator: maintain applicable approval workflows without breaking active requests
- Recruiting User: continue an approved request into hiring and track fulfillment

## Entry points

Known or expected entry points include:

- Recruitment Request list
- Create Recruitment Request action
- Recruitment Request detail
- Approval notification or task
- Approval Workflow management
- Approved request entry into hiring work

## Main concepts

### Recruitment Request

A record of an internal hiring need.

### Approval Workflow

An ordered set of approval steps that applies under defined organizational conditions.

### Approval Step

One stage of the workflow with one or more approvers.

### Requested Capacity

The number of hires needed.

### Fulfillment

The request is fulfilled when all requested hiring capacity has been filled.

## Main flows

### Create and submit a request

1. The Request Owner creates or opens a draft.
2. Required hiring-need information is completed.
3. The product resolves or selects an applicable approval workflow.
4. The user submits the request.
5. Required fields, permissions, workflow readiness, and approvers are validated.
6. On success, the request enters review and the first approval step becomes active.
7. On failure, the request remains a draft and shows the blocking issue.

### Approve a request

1. An approver opens a request at their active step.
2. They review the request and approve it.
3. Under the currently documented rule, approval by at least one approver is sufficient to approve the step.
4. The next step becomes active, or final approval moves the request into hiring.

Detailed behavior after minimum approval is reached still needs verification.

### Reject a request

1. An active approver chooses Reject.
2. A rejection reason is required.
3. The request becomes rejected.
4. The Request Owner can review the reason and resubmit.

### Resubmit a rejected request

The Request Owner may resubmit without being forced to change request fields. The rejection reason remains relevant context for the next review.

### Continue into hiring

After final approval, the request enters a hiring phase. It remains the business entity that owns requested capacity and fulfillment.

### Edit an approval workflow with active requests

When active requests depend on a workflow:

- Existing steps must not be removed or reordered.
- Existing approvers must not be removed.
- New approvers may be added to existing steps.
- Added approvers apply to dependent active requests.

When no active request depends on the workflow, the workflow may be fully edited.

## Rules

- Submission requires complete request information and an applicable valid workflow.
- The active step must have at least one valid approver.
- At least one approver's approval is sufficient for the step under the current known rule.
- Rejection requires a reason.
- Rejected requests can be resubmitted without mandatory changes.
- Structural request editing becomes restricted after an approver acts.
- Active workflow dependencies restrict workflow editing to adding approvers.
- The current model does not create a new workflow version for each edit.
- Approvers are selected users; role-based approvers are not part of the currently documented behavior.

## Permissions

Known expectations:

- Request Owners can create and submit when required information is complete.
- Approvers can act only at steps assigned to them.
- Workflow Administrators can fully edit unrestricted workflows.
- When active requests depend on a workflow, administrators can only add approvers.

Still unknown:

- Formal role names
- Permission inheritance
- Delegation
- Administrator override behavior
- Cancellation and closure permissions

## States and transitions

Known high-level lifecycle:

```text
Draft
→ In review
→ Approved / Hiring
→ Fulfilled
```

Rejection path:

```text
In review
→ Rejected
→ Resubmitted
→ In review
```

The exact naming and persistence of Approved versus Hiring need verification. Cancellation, closure, archival, and partial fulfillment are not documented yet.

## Validations

Known validation categories:

- Required request fields
- Requested capacity and numeric constraints
- Actor authorization
- Applicable workflow availability
- Approval-step existence
- Valid approver availability
- Current request state

## Edge cases

- No workflow matches selected organizational conditions
- Workflow has no valid first step or approver
- Account does not use branches
- Approver is deactivated or loses access
- Workflow changes while the request is open
- Network or server failure during submission
- Duplicate submission
- Multiple jobs or hires contribute to fulfillment
- Partial fulfillment

Most of these cases are still untested or unspecified.

## Related Product Areas

- Approval Workflow
- Job Management
- Candidate Management
- Organization and access concepts

## Known variations

- Some customer accounts have branches; others do not.
- Workflow applicability may depend on department, branch, or other organization conditions.

## Unknowns and untested behavior

- Exact required fields
- Workflow matching and fallback algorithm
- Notification behavior
- Field-level editability by state
- Cancellation and closure
- Partial fulfillment
- Multiple Jobs per request
- Persistence, retry, and duplicate-action behavior
- Permission differences across account types

## Sources

- Product and design discussions about ATS Recruitment Request behavior during 2026
- Production walkthrough is still recommended to verify branches, permissions, and persistence
