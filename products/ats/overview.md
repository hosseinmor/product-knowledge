# ATS

**Status:** Draft
**Owner:** ATS product team
**Last reviewed:**

## What this product is

ATS supports organizational hiring operations by keeping hiring needs, approval requests, jobs, and candidate-resume management in one product area.

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

- Jobseeker-side job discovery and application experience
- Payroll, onboarding, learning, and other HR-suite modules

These boundaries are an initial documentation view and require owner review.

## Main Product Areas

- Recruitment Request
- Approval Workflow
- Job Management
- Candidate Management

Only Recruitment Request currently has substantive documentation.

## Major user journeys

### Hiring need to active hiring

```text
A hiring need is created
→ the request is completed and submitted
→ approvers review it
→ an approved request enters hiring
→ recruiting continues until the requested capacity is fulfilled
```

### Manage candidates for a job

```text
A recruiting user opens a job
→ reviews candidates and resumes
→ moves or updates candidates through the hiring process
```

## Important integrations

Organization structure, branches, departments, notifications, job publication, and candidate data may connect to other product areas. Ownership and behavior require further documentation.

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
