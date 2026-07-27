---
id: ats.capability.manage-recruitment-request
collection: product
type: capability
product: ats
title: Manage Recruitment Request
summary: Describes the known ATS ability to create, submit, review, and continue an internal hiring request through approval and hiring.
knowledge_state: unverified
document_maturity: draft
related:
  - ats
  - ats.domain.recruitment-request
  - ats.flow.submit-recruitment-request
owner: ats-product
actors:
  - request-owner
  - approver
  - workflow-administrator
domains:
  - ats.domain.recruitment-request
source_refs:
  - product-discussion:ats-recruitment-request-2026
---

# Manage Recruitment Request

## Purpose and Value

This Capability lets an organization turn an internal hiring need into a structured Recruitment Request, route it through the required approval process, and continue it into hiring after approval.

It reduces informal approval coordination and keeps the request, approval progress, hiring capacity, and eventual fulfillment connected.

This document is `unverified` because the complete released behavior and all supported account configurations have not yet been semantically reviewed.

## Actors and User Outcomes

### Request Owner

Wants to declare a hiring need, complete required information, submit it to the correct approvers, and follow it until hiring is fulfilled.

### Approver

Wants to review the request at the appropriate step and approve or reject it with sufficient context.

### Workflow Administrator

Wants to configure which approval process applies and maintain approvers without breaking active requests.

### Recruiting or HR User

Wants an approved request to become actionable hiring work and to track progress against requested capacity.

## Entry Points

Known or expected entry points include:

- Recruitment Request list
- Create Recruitment Request action
- Recruitment Request detail page
- Approval task or notification linking to a request
- Approval Workflow management
- Approved request entry into hiring work

Only the request-detail and submit behavior are represented in the current Flow slice. Notification and deep-link behavior remain unverified.

## Availability and Permissions

Known availability rules:

- A Request Owner can create a draft when their account permits Recruitment Requests.
- Submission requires a complete request and an applicable approval workflow.
- Approvers can act only at an active step assigned to them.
- Workflow administrators can fully edit workflows without active dependencies.
- When active requests depend on a workflow, administrators can add approvers but cannot remove or restructure existing approval steps.

Exact role definitions and account-level permission checks remain incomplete.

## High-Level Behavior

```text
Create draft request
→ complete hiring-need information
→ select or resolve the applicable approval workflow
→ submit for review
→ progress through approval steps
→ approve or reject
→ resubmit after rejection when needed
→ enter hiring after final approval
→ track hiring until requested capacity is fulfilled
```

The request remains the durable business entity through approval and hiring. It should not be documented as a temporary form that disappears after approval.

## Included Flows

Documented:

- `ats.flow.submit-recruitment-request`

Required next Flows:

- Create Recruitment Request
- Approve Recruitment Request
- Reject Recruitment Request
- Resubmit rejected Recruitment Request
- Close or cancel Recruitment Request
- Edit Approval Workflow with active requests
- Fulfill requested hiring capacity

## Capability-Specific States

The Capability presents or acts on Domain lifecycle states including:

- Draft
- In review
- Rejected
- Approved or Hiring
- Fulfilled

The precise UI labels and whether `Approved` is separately persisted from `Hiring` remain unverified.

Capability-level interface states also include:

- Editable versus locked request
- Actionable approval step versus read-only history
- Available versus unavailable workflow
- Complete versus validation-blocked submission

## Capability-Specific Rules

- Submission is unavailable until required request information is complete.
- An applicable Approval Workflow is required when the request must be approved.
- At least one approver's approval is sufficient to approve the active step under the currently documented rule.
- Rejection requires a reason.
- A rejected request can be resubmitted without mandatory field changes.
- Structural request editing becomes restricted after an approver acts.
- Active workflow dependencies restrict editing to adding approvers.

Stable business rules are owned by `ats.domain.recruitment-request`; this Capability describes how the product ability exposes and applies them.

## Boundaries and Exclusions

Included:

- Internal hiring-need request management
- Approval routing and step progress
- Transition into hiring
- Capacity and fulfillment context

Not established in this Capability:

- Detailed Job creation and publication
- Candidate-resume Kanban behavior
- Interview scheduling
- Offer management
- Employee onboarding
- Payroll or workforce administration

Those areas may be separate ATS or HR-suite Capabilities and require their own documentation.

## Dependencies

Known dependencies include:

- Organization users and access control
- Branch and department structure when workflow scope uses them
- Approval Workflow configuration
- Notification delivery for approval tasks
- Job and hiring execution after approval
- Candidate or hire records used to calculate fulfillment

Canonical ownership for several of these dependencies remains open.

## Related Domain Rules

See `ats.domain.recruitment-request` for:

- Step approval
- Rejection reason
- Request lifecycle
- Resubmission
- Workflow editing with active request dependencies
- Requested-capacity fulfillment

## Related Decisions

No accepted standalone Decision document is currently linked.

## Evidence

This Capability is derived from 2026 product-design discussions about Recruitment Request creation, approval, workflow maintenance, and hiring transition.

It has not yet been verified through all supported roles, account structures, branches, departments, or production error conditions.

## Coverage

Covered at discussion level:

- Purpose and actor outcomes
- Major lifecycle
- Submission dependency on completeness and workflow
- Approval and rejection rules
- Workflow editing restriction
- Transition into hiring and fulfillment concept

Not yet tested or confirmed:

- Exact entry points and notification behavior
- Field-level editability by lifecycle state
- Permission inheritance
- Empty, invalid, and error states
- Cancellation and closure
- Partial fulfillment
- Multiple Jobs per request
- Deactivated approvers

## Unknowns and Open Questions

- Which fields and sections are required for submission?
- Is the applicable workflow selected manually, resolved automatically, or both?
- What happens when no workflow matches the selected organizational conditions?
- Can a Request Owner edit or withdraw a request during review?
- How are approval reminders, escalations, and delegated approvers handled?
- What data establishes request fulfillment?
