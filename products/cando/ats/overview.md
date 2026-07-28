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
topics:
  - hiring
  - recruitment
  - approval
  - ats
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
- Job Management
- Candidate Management

Recruitment Request and Approval Workflow currently have substantive draft documentation.

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

### Manage candidates for a job

```text
A recruiting user opens a job
→ reviews candidates and resumes
→ moves or updates candidates through the hiring process
```

## Important integrations

Organization structure, branches, departments, notifications, job publication, candidate data, and shared AI services may connect to other product areas. Ownership and behavior require further documentation.

## Known variations

- Some accounts may not use branches.
- Workflow scope and permission models may vary by account.

## Documentation gaps and unknowns

- Approved top-level ATS boundary
- Formal roles and permissions
- Job and candidate-management behavior
- Notifications and integrations
- Empty, error, recovery, and permission states

## Sources

- Product and design discussions about Recruitment Request and ATS job management during 2026
