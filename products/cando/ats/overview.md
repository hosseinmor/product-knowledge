---
id: cando.ats.overview
kind: product-overview
group: cando
product: ats
title: ATS
summary: Overview of the Cando ATS product, its users, boundaries, main Product Areas, major journeys, and documentation gaps.
status: draft
owner: ATS product team
last_reviewed:
related:
  - cando.overview
  - cando.ats.recruitment-request
  - cando.ats.approval-workflow
  - cando.ats.job-management
topics:
  - hiring
  - recruitment
  - approval
  - ats
  - job-management
  - job-publication
---

# ATS

## What this product is

Cando ATS supports organizational hiring operations by keeping hiring needs, approval requests, jobs, and candidate-resume management in one product.

## Primary users

- Recruiting and HR team members
- Request owners and department representatives
- Approvers
- Account and workflow administrators

Exact role names and permission inheritance still need review.

## Problems it solves

- Structuring internal hiring requests
- Routing requests through approval
- Turning approved needs into hiring work
- Managing jobs and candidate resumes
- Tracking progress against requested hiring capacity

## Product boundaries

### In scope

- Recruitment Requests
- Approval workflows
- Job management
- Candidate and resume management
- Hiring progress and fulfillment

### Out of scope

- Jobvision Candidate job discovery and application experience
- Pulse, Onboarding, and Learning behavior

These boundaries are an initial documentation view and require owner review.

## Main Product Areas

- Recruitment Request
- Approval Workflow
- [Job Management](areas/job-management.md)
- Candidate Management

Recruitment Request and Approval Workflow have substantive draft documentation. Job Management has reviewed documentation for the scope observed in one authenticated account.

## Major user journeys

### Hiring need to active hiring

```text
A hiring need is created
→ the request is completed and submitted
→ approvers review it
→ an approved request enters hiring
→ recruiting continues until the requested capacity is fulfilled
```

### Configure an approval workflow

```text
An authorized administrator defines workflow scope
→ creates ordered approval steps
→ assigns approvers
→ the workflow becomes available for matching Recruitment Requests
```

### Define and manage a job

```text
A recruiting user starts from a new job or a copy
→ defines job information
→ configures the application form
→ configures hiring stages
→ assigns job-level team access
→ manages publication or resume sourcing
→ reviews applications in a stage-aligned candidate board
```

### Manage candidates for a job

```text
A recruiting user opens a job
→ reviews candidates and resumes
→ moves or updates candidates through the hiring process
```

## Important integrations

Organization structure, branches, departments, notifications, job publication, candidate data, and shared AI services may connect to other product areas.

The observed Job Management interface offers publication or resume-sourcing actions for the organization's careers page, JobVision, and other recruiting services. It also presents AI-assisted resume relevance ranking based on match with the job description. Channel behavior and the underlying AI service remain undocumented.

## Known variations

- Some accounts may not use branches.
- Workflow scope and permission models may vary by account.

## Documentation gaps and unknowns

- Approved top-level ATS boundary
- Formal role names, permission inheritance, and job-level access detail
- Complete job lifecycle from draft through publication, closure, and archival
- Job relationship to Recruitment Request and fulfillment
- Save, validation, cancellation, persistence, and recovery behavior across job definition
- Candidate transitions, rejection, restoration, history, and bulk actions
- Publication-channel eligibility, synchronization, moderation, cost, and recovery
- Notification triggers, delivery, and failure behavior
- Automatic-rejection rules, audit, and recovery
- AI-ranking inputs, quality, explainability, configuration, and fallback
- Empty, error, concurrency, and permission states

## Sources

- Product and design discussions about Recruitment Request and ATS job management during 2026
- Reviewed walkthrough evidence package `WT-2026-001`, recorded 2026-08-05 and owner-reviewed 2026-08-06
