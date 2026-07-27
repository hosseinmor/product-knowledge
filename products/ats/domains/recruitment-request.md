---
id: ats.domain.recruitment-request
collection: product
type: domain
product: ats
title: Recruitment Request
summary: Defines the known Recruitment Request, approval workflow, approver, lifecycle, permission, and workflow-editing rules in ATS.
knowledge_state: unverified
document_maturity: draft
related:
  - ats
  - ats.capability.manage-recruitment-request
  - ats.flow.submit-recruitment-request
owner: ats-product
source_refs:
  - product-discussion:ats-recruitment-request-2026
---

# Recruitment Request

## Purpose and Boundaries

The Recruitment Request Domain represents an organization's internal hiring need and the approval process that must occur before or alongside recruiting work.

A Recruitment Request is not the same entity as a Job. After approval, the request continues into a hiring phase where one or more Jobs and hiring activities may fulfill its requested capacity.

The current document is `unverified`: it records discussion-level product decisions that still require a semantic review against production and current PM intent.

## Vocabulary

### Recruitment Request

A record of an internal hiring need. It includes the requested capacity and the organizational context needed to select or validate an approval workflow.

### Request Owner

The user responsible for creating and submitting the Recruitment Request and following its progress.

### Approval Workflow

An ordered set of approval steps that applies to a Recruitment Request under defined organizational conditions.

### Approval Step

One stage of an Approval Workflow. A step contains one or more approvers.

### Approver

A user who can approve or reject a Recruitment Request at an active approval step.

### Requested Capacity

The number of hires needed for the request.

### Fulfillment

The condition in which all requested hiring capacity has been filled.

### Active Request Dependency

A relationship in which an Approval Workflow is already used by a request whose lifecycle is still active.

## Entities and Relationships

```text
Recruitment Request
→ owned by one Request Owner
→ uses one applicable Approval Workflow when approval is required
→ has one requested hiring capacity
→ progresses through Approval Steps
→ may be fulfilled through one or more hiring activities or Jobs

Approval Workflow
→ contains ordered Approval Steps
→ each step contains one or more Approvers
→ may be scoped by organizational conditions such as department or branch
→ may be referenced by multiple active Recruitment Requests
```

The exact relationship between Recruitment Request and Job is not fully verified. The current model assumes the approved request remains the owner of capacity and fulfillment while Jobs support recruiting execution.

## Business Rules and Invariants

### Step approval

At least one approver in the active Approval Step must approve for the step to be considered approved.

Whether additional approvers may still act after the minimum approval condition is met has not been verified.

### Rejection reason

Rejecting a Recruitment Request requires a reason.

### Resubmission

A Request Owner may resubmit a rejected request without being forced to change its fields. The rejected reason remains relevant context for the next review.

### Editability during review

The discussion-level rule is:

```text
Request submitted
→ editable until the first approval-step action occurs
→ structurally locked after an approval or rejection action
```

The exact set of fields that remain editable at each stage must be verified.

### Approval to hiring

After final approval, the Recruitment Request enters a hiring phase. This is a lifecycle transition of the request rather than creation of an unrelated replacement entity.

### Fulfillment

A Recruitment Request is fulfilled when all requested hiring capacity has been filled.

### Workflow changes with active dependencies

When an Approval Workflow has active Recruitment Requests:

- Existing approval structure must not be removed or reordered.
- Existing approvers must not be removed.
- New approvers may be added to existing steps.
- Added approvers apply to dependent active requests.

When no active request depends on the workflow, the workflow may be fully edited.

The user experience may expose this as a restricted edit mode rather than a separate workflow version.

### Workflow versioning

The current model does not create a separate workflow version for each edit. Restrictions protect active requests from incompatible structural changes.

### Role-based approvers

Selecting an approver by organizational role is not part of the currently documented behavior. Approvers are represented as selected users.

## Permissions

Known permission expectations:

- Request Owner can create and submit their request when required information is complete.
- An Approver can act only when the request is at a step assigned to them.
- Workflow administrators can edit unrestricted workflows.
- Workflow administrators can only add approvers when active request dependencies restrict editing.

The repository does not yet establish:

- Formal role names
- Account-level permission inheritance
- Delegation behavior
- Whether administrators can override request lifecycle restrictions
- Whether a Request Owner can cancel or close a request in every state

## States and Lifecycle

The known lifecycle is represented at this level:

```text
Draft
→ In review
→ Approved
→ Hiring
→ Fulfilled
```

A request may also be rejected during review:

```text
In review
→ Rejected
→ Resubmitted
→ In review
```

The exact naming and persistence of `Approved` versus `Hiring` must be verified. Product discussions indicate that approval changes the request into its hiring phase rather than ending the request.

Cancellation, closure, archival, and partial-fulfillment states remain open.

## Approved Exceptions

The known intentional exception to locked workflow editing is adding an approver to an existing step while active requests depend on the workflow.

This exception should be preserved as a Domain rule and may warrant a canonical Decision document after its rationale and alternatives are formally reviewed.

## Related Capabilities

- `ats.capability.manage-recruitment-request`
- Configure Recruitment Request approval workflow — not yet documented as a separate Capability
- Review and approve Recruitment Request — not yet documented as a separate Capability
- Track request fulfillment — not yet documented as a separate Capability

## Related Flows

- `ats.flow.submit-recruitment-request`
- Reject Recruitment Request — not yet documented
- Resubmit rejected Recruitment Request — not yet documented
- Edit workflow with active requests — not yet documented

## Related Decisions

No accepted standalone Decision document is currently linked.

## Evidence

The rules in this draft were supplied in product-design discussions about ATS Recruitment Request behavior during 2026.

They have not yet been checked through a complete production walkthrough, release evidence, or a reviewed PRD-to-release update cycle.

## Coverage and Known Gaps

- Core entities and major approval rules are covered at discussion level.
- Organizational scoping by branch and department is incomplete.
- Permissions have not been verified across account roles.
- Cancellation, closure, partial fulfillment, and archival are incomplete.
- Notifications, activity history, and audit-log ownership are not documented.
- Error and recovery behavior belongs in supporting Flows and remains incomplete.

## Open Questions

- What are the exact canonical request state names?
- Which fields remain editable before and after the first approver action?
- Does approval immediately enter `Hiring`, or is `Approved` a separately persisted state?
- How are several Jobs or hires aggregated into request fulfillment?
- What happens to active requests when an approver is deactivated or loses access?
- How do branch and department scoping rules select an applicable workflow?
- Which user can close or cancel a request, and under which conditions?
