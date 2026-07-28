---
id: cando.ats.approval-workflow
kind: product-area
group: cando
product: ats
title: Approval Workflow
summary: Explains how Cando ATS defines, scopes, applies, and safely edits approval workflows used by Recruitment Requests.
status: draft
owner: ATS product team
last_reviewed:
related:
  - cando.ats.overview
  - cando.ats.recruitment-request
topics:
  - approval-workflow
  - approval-step
  - approver
  - branch
  - department
  - permissions
---

# Approval Workflow

## Overview

Approval Workflow defines the ordered approval process used by a Recruitment Request. A workflow contains approval steps, and each step contains one or more selected approvers.

The current documentation is based on product and design discussions and still needs production verification.

## Why this area exists

- Route Recruitment Requests to the correct approvers
- Support different organizational conditions such as department or branch
- Keep approval order and responsibilities explicit
- Protect active requests from incompatible workflow edits

## Users and roles

- Workflow Administrator: creates and maintains workflows, steps, and approvers
- Request Owner: selects or receives an applicable workflow when submitting a request
- Approver: acts on a request when their step becomes active

Formal permission names and inheritance require review.

## User outcomes

- Workflow Administrator: configure an approval process that can be safely reused by matching requests
- Request Owner: submit a request through an applicable and valid workflow
- Approver: understand when a request requires their action

## Entry points

Known or expected entry points include:

- Approval Workflow list
- Create Workflow action
- Workflow detail or edit experience
- Recruitment Request create or edit experience when a workflow must be selected or resolved

Exact navigation and page structure require verification.

## Main concepts

### Approval Workflow

An ordered set of approval steps that applies under defined organizational conditions.

### Approval Step

One stage in the workflow. Steps are evaluated in order.

### Approver

A selected user who can approve or reject a request at an active step.

### Workflow Scope

Conditions that determine where a workflow applies. Current discussions include department and branch as possible scope dimensions.

### Active Request Dependency

A workflow has an active dependency when one or more current Recruitment Requests use it.

## Main flows

### Create a workflow

1. An authorized administrator starts a new workflow.
2. The administrator defines the workflow name and applicable organizational conditions.
3. One or more ordered approval steps are added.
4. One or more approvers are assigned to each step.
5. The product validates that the workflow can be used by matching requests.
6. The workflow becomes available for selection or resolution.

Required fields and activation behavior still need verification.

### Apply a workflow to a Recruitment Request

1. A Request Owner completes the organizational conditions required by the request.
2. The product selects or resolves an applicable workflow.
3. Submission is blocked when no applicable valid workflow exists.
4. On successful submission, the first approval step becomes active.

The matching and fallback algorithm is not yet documented.

### Edit a workflow without active requests

When no active request depends on the workflow, the workflow may be fully edited.

The exact actions included in full editing require verification, but current discussions allow structural changes when there are no active dependencies.

### Edit a workflow with active requests

When active requests depend on the workflow:

- Existing steps must not be removed or reordered.
- Existing approvers must not be removed.
- New approvers may be added to existing steps.
- Added approvers apply to dependent active requests.

The product should communicate this restricted edit mode clearly.

## Rules

- A workflow must contain a valid first step before it can be used.
- Every approval step must contain at least one valid approver.
- Approvers are selected users; role-based approvers are not part of the currently documented behavior.
- The current model does not create a separate workflow version for every edit.
- Active request dependencies protect existing workflow structure from removal or reordering.
- Adding approvers is the documented exception when active requests depend on the workflow.
- Submission of a Recruitment Request requires an applicable valid workflow when approval is required.

## Permissions

Known expectations:

- Only authorized workflow administrators can create or edit workflows.
- Approvers can act only on requests at steps assigned to them.
- Administrators have full editing access only when no active request depends on the workflow.

Still unknown:

- Formal administrator role names
- Whether permission is account-wide or scoped
- Delegation behavior
- Administrator override behavior
- What happens when an approver is deactivated or loses access

## States and transitions

A workflow may need states such as draft, active, or inactive, but the current repository does not establish those names or transitions.

For a request using the workflow, approval-step progression is known at a high level:

```text
First step active
→ at least one approver approves
→ next step becomes active
→ final step approved
→ request enters hiring
```

Rejection behavior belongs primarily to the Recruitment Request area.

## Validations

Known validation categories:

- Workflow scope completeness
- At least one approval step
- At least one valid approver per step
- No incompatible structural edit while active requests depend on the workflow
- Applicable workflow availability during request submission

Exact validation timing and messages require verification.

## Edge cases

- No workflow matches the selected department or branch
- More than one workflow matches the same conditions
- An account does not use branches
- An approver is deactivated or loses access
- A workflow is edited while a request is open
- A new approver is added after earlier steps have already completed
- A workflow becomes unavailable between request editing and submission

Most edge cases are currently untested or unspecified.

## Related Product Areas

- Recruitment Request
- Organization and Access
- Notifications

## Known variations

- Some customer accounts have branches; others do not.
- Workflow applicability may depend on department, branch, or both.
- Account permission models may vary.

## Unknowns and untested behavior

- Exact workflow matching and priority rules
- Whether a default workflow exists
- Workflow activation and deactivation states
- Duplicate workflow scope handling
- Step reordering and deletion rules when no active request exists
- Notification and reminder behavior
- Deactivated approver recovery
- Audit history for workflow changes

## Sources

- Product and design discussions about Cando ATS Recruitment Request and workflow-editing behavior during 2026
- Production walkthrough is recommended before marking this document reviewed
