# ATS

Status: Draft
Owner: ATS product team
Last reviewed:

## What this product is

ATS supports organizational hiring operations by keeping hiring needs, approval requests, jobs, and candidate-resume management in one product.

The currently documented knowledge is strongest around Recruitment Request. The broader ATS boundary still needs review.

## Primary users

Known users include:

- Recruiting and HR team members who manage jobs, requests, and candidate resumes
- Request owners or department representatives who declare a hiring need
- Approvers who review a request at configured approval steps
- Account administrators who configure organizational structures and approval workflows

Exact role names, permission inheritance, and account differences are not fully documented.

## Problems it solves

- Structure and route internal hiring needs
- Coordinate request approval
- Turn approved requests into hiring work
- Manage jobs and candidate resumes
- Track hiring progress against requested capacity

## Product boundaries

### In scope

Current known areas include:

- Recruitment Request
- Approval Workflow
- Job Management
- Candidate Management
- Hiring progress and request fulfillment

### Out of scope

This overview does not cover:

- Jobseeker-side job discovery and application behavior
- Payroll, onboarding, learning, engagement, and other HR-suite modules
- Shared organization or identity rules whose ownership belongs outside ATS

These exclusions describe the current documentation boundary, not a final approved architecture.

## Main Product Areas

### Recruitment Request

Create, submit, review, approve, reject, resubmit, and track an internal hiring request through approval and hiring.

See `areas/recruitment-request.md`.

### Approval Workflow

Configure workflow scope, approval steps, and approvers. This Area still needs a dedicated document.

### Job Management

Create and manage recruiting work for a job. This Area still needs a dedicated document.

### Candidate Management

Review and manage candidate resumes, including the known Kanban-style resume-management view. This Area still needs a dedicated document.

## Major user journeys

### Hiring need to active hiring

```text
Request owner identifies a hiring need
→ creates and completes a Recruitment Request
→ uses an applicable Approval Workflow
→ submits the request
→ approvers review it
→ the approved request enters hiring
→ recruiting continues until requested capacity is fulfilled
```

### Configure an Approval Workflow

```text
Administrator defines workflow scope
→ adds approval steps
→ assigns approvers
→ makes the workflow available for matching requests
→ later edits follow restrictions when active requests depend on it
```

### Manage candidate resumes for a job

```text
Recruiting user opens a job
→ reviews resumes in a Kanban-style view
→ moves or updates candidates through the hiring process
```

## Relationships with other products

Organization structure, branches, departments, notifications, job publication, and candidate data may connect ATS with other products or shared concepts. Their ownership still needs review.

## Known gaps and open questions

- What is the approved top-level ATS boundary?
- Which roles are formally supported, and how are permissions derived?
- Which organization, branch, and department concepts are shared?
- Which Job and Candidate Management behavior should be documented next?
- Which request states and transitions are implemented consistently in production?

## Sources

This initial content comes from 2026 product-design discussions about Recruitment Request, Approval Workflow restrictions, and ATS job and resume management. It has not yet been validated through a complete production walkthrough.
