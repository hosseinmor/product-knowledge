---
id: ats
collection: product
type: product
product: ats
title: ATS
summary: Defines the current known ATS purpose, users, boundaries, capabilities, major journeys, and documented coverage gaps.
knowledge_state: unverified
document_maturity: draft
related:
  - ats.domain.recruitment-request
  - ats.capability.manage-recruitment-request
  - ats.flow.submit-recruitment-request
owner: ats-product
source_refs:
  - product-discussion:ats-recruitment-request-2026
---

# ATS

## Purpose

ATS supports organizational hiring operations by keeping hiring needs, approval requests, jobs, and candidate-resume management in one product area.

The currently documented slice focuses on Recruitment Request: an internal request can be created, submitted through an approval workflow, and then continue into hiring after approval.

This overview is still `unverified` because the full ATS boundary and all production behavior have not yet received a single semantic review.

## Primary Users

Known user groups include:

- Recruiting and HR team members who manage jobs, requests, and candidate resumes
- Request owners or department representatives who declare a hiring need
- Approvers who review a request at configured approval steps
- Account administrators who configure organizational structures and approval workflows

Exact role names, permission inheritance, and differences between customer accounts remain to be verified.

## Product Boundaries

### In scope

The currently known ATS boundary includes:

- Creating and managing Recruitment Requests
- Configuring approval workflows and approvers
- Submitting requests for approval
- Reviewing, approving, and rejecting requests
- Moving an approved request into the hiring phase
- Managing jobs and candidate resumes, including a Kanban-style resume-management view
- Tracking request progress until the approved hiring capacity is fulfilled

### Out of scope

The following areas are not established as ATS responsibilities in this documentation slice:

- Jobseeker-side job discovery and application behavior
- Payroll, onboarding, learning, engagement, and other HR-suite modules
- Organization-wide business rules that are owned by another shared product or Domain

These exclusions describe the current documentation boundary, not a final approved product architecture.

## Main Capabilities

Current known Capabilities include:

- Manage Recruitment Requests
- Configure Recruitment Request approval workflows
- Review and approve Recruitment Requests
- Manage jobs and candidate resumes
- Track hiring progress and request fulfillment

Only `Manage Recruitment Requests` is documented in detail in the current vertical slice.

## Major User Journeys

### Hiring need to active hiring

```text
Request owner identifies a hiring need
→ creates and completes a Recruitment Request
→ selects an applicable approval workflow
→ submits the request
→ configured approvers review the request
→ the approved request enters the hiring phase
→ recruiting work continues until the requested capacity is fulfilled
```

### Configure an approval workflow

```text
Administrator defines the workflow scope
→ adds approval steps
→ assigns one or more approvers to each step
→ makes the workflow available for matching requests
→ later edits follow restrictions when active requests depend on the workflow
```

### Manage candidate resumes for a job

```text
Recruiting user opens a job
→ reviews resumes in a Kanban-style management view
→ moves or updates candidates through the hiring process
```

The candidate-management journey is only known at a high level and requires a dedicated walkthrough and semantic review.

## Key Business Concepts and Domains

Known business concepts include:

- Recruitment Request
- Approval Workflow
- Approval Step
- Approver
- Request Owner
- Hiring Capacity
- Job
- Candidate Resume or Application

The first canonical Domain candidate is `ats.domain.recruitment-request`.

## Integrated Products and Systems

Known integrations and boundaries are not sufficiently documented yet. Organization structure, branches, departments, notifications, job publication, and candidate data may involve other product areas, but ownership must be verified before documenting those relationships.

## Related Decisions

No standalone accepted Decision document is currently linked.

Restrictions on editing approval workflows with active requests may justify a durable Decision after the rationale, alternatives, and approver are formally reviewed.

## Evidence and Source References

This initial slice is based on product-design discussions supplied by the product owner during 2026 about:

- Recruitment Request lifecycle and approval behavior
- Workflow editing restrictions
- ATS job and resume-management structure

The discussion is represented by the metadata source reference `product-discussion:ats-recruitment-request-2026`. It is not a production walkthrough or released implementation record.

## Coverage and Known Gaps

- Recruitment Request concepts and major rules have discussion-level evidence.
- The submit flow has not yet been verified through a complete production walkthrough across roles and account configurations.
- Job and candidate-resume management is documented only at overview level.
- Account-level differences, permission inheritance, notifications, integrations, and error behavior remain incomplete.
- Empty, blocked, invalid, and recovery states are not comprehensively covered.

## Open Questions

- What is the approved top-level ATS product boundary?
- Which roles are formally supported, and how are their permissions derived?
- Which organization, branch, and department concepts are owned by ATS versus shared Domains?
- Which jobs and candidate-management Capabilities should be documented next?
- Which request states and transitions are implemented consistently in production?
