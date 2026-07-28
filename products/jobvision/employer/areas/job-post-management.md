---
id: jobvision.employer.job-post-management
kind: product-area
group: jobvision
product: employer
title: Job Post Management
summary: Describes how Employers create, review, publish, update, pause, close, and manage Job Posts in Jobvision.
status: draft
owner: Employer product team
last_reviewed:
related:
  - jobvision.employer.overview
  - shared.job-post
  - jobvision.candidate.job-post-experience
topics:
  - job-post
  - create-job-post
  - publish-job-post
  - employer
  - recruiting
---

# Job Post Management

## Overview

Job Post Management is the Employer-side Product Area for creating and managing the job opportunities that Candidates see in Jobvision.

This draft establishes the Product Area boundary but does not claim a complete released flow. Current behavior, field requirements, lifecycle states, and permissions still need owner review and production evidence.

## Why this area exists

- Let Employers describe a hiring opportunity
- Prepare and publish a Job Post for Candidates
- Maintain the Job Post as hiring conditions change
- Control whether the opportunity remains available
- Connect a Job Post to Employer-side candidate and application management

## Users and roles

- Recruiter
- HR team member
- Hiring manager
- Employer account administrator

Formal role names and permission differences require verification.

## User outcomes

- Create an accurate Job Post
- Review the content before publication
- Publish the opportunity to Candidates
- Update, pause, close, or reuse a Job Post when appropriate
- Understand the operational state of the Job Post
- Access applications connected to the Job Post

## Entry points

Known or expected entry points include:

- Employer Job Post list
- Create Job Post action
- Job Post detail
- Job Post edit experience
- Candidate or application management linked to a Job Post

Exact navigation and list behavior require review.

## Main concepts

### Job Post

The shared opportunity defined in `shared.job-post`.

### Employer Management State

The operational state and controls shown to Employer users. The exact states are not yet documented.

### Publication

The action or transition that makes an eligible Job Post available to Candidate users.

### Application

A Candidate response connected to a Job Post. The full Application concept and Employer-side management behavior are not yet documented.

## Main flows

### Create a Job Post

1. An authorized Employer user starts a new Job Post.
2. The user provides the opportunity information required by the product.
3. The product validates the entered information.
4. The user saves a draft or continues toward review and publication.

The exact fields, step structure, autosave behavior, and draft rules require verification.

### Review and publish a Job Post

1. The user reviews the Job Post content and publication readiness.
2. The product checks required information and account eligibility.
3. The user confirms publication.
4. On success, the Job Post becomes available to the Candidate product according to shared visibility rules.
5. On failure, the product keeps the Job Post editable and explains the blocking condition.

Publication plans, quotas, moderation, and approval rules are not yet documented.

### Edit a Job Post

1. An authorized user opens an existing Job Post.
2. The product exposes fields that are editable in the current state.
3. The user updates and saves the Job Post.
4. The product communicates whether the change affects visibility or requires another action.

Editing restrictions after publication require evidence.

### Pause or close a Job Post

1. An authorized user chooses to stop or end availability.
2. The product may require confirmation or a reason.
3. Candidate-side availability changes according to the resulting state.
4. Existing applications remain connected to the Employer workflow unless another documented rule applies.

The distinction between pause, close, expire, archive, and delete is not yet established.

### Reuse or duplicate a Job Post

Employers may need to create a new Job Post from an existing one. Whether this is supported and which data is copied require verification.

## Rules

Confirmed only at the current level:

- Employer owns Job Post creation and management behavior.
- Candidate owns discovery, evaluation, and application behavior.
- Shared Job Post definitions and lifecycle facts should be documented once in `shared.job-post`.
- Product-specific publication controls, permissions, and employer operations remain in this Product Area.

Field, quota, publication, moderation, editing, and closure rules are still incomplete.

## Permissions

Potential permission distinctions include:

- Creating a Job Post
- Editing a draft
- Publishing
- Editing after publication
- Pausing or closing
- Duplicating or deleting
- Viewing and managing connected applications

The current repository does not yet define which Employer roles can perform each action.

## States and transitions

The Job Post lifecycle is not yet confirmed. Candidate states that require review include:

```text
Draft
→ Published
→ Paused or Closed
→ Archived or Expired
```

These names are placeholders for investigation, not approved current states.

## Validations

Likely validation areas that require evidence:

- Required Job Post information
- Account permission and eligibility
- Publication quota or plan access
- Field formats and boundaries
- Publication readiness
- State-dependent editing

## Edge cases

- Publication fails after data entry
- Job Post is edited while Candidates are viewing it
- Account plan or quota changes
- Job Post has existing applications when paused or closed
- Duplicate or repeated publish action
- Required company or organizational information is missing
- Employer loses access while editing
- Job Post expires automatically

These cases remain untested in the current repository.

## Related Product Areas

- Employer Account and Access
- Candidate and Application Management
- Employer Products and Plans
- Candidate Job Post Experience

## Known variations

- Available actions may depend on Employer role, account plan, or Job Post state.
- Publication and visibility behavior may vary by product package.
- Different job types may require different information.

## Unknowns and untested behavior

- Canonical Job Post fields
- Exact create and edit flow
- Draft persistence
- Publication eligibility, quota, and moderation
- Exact lifecycle state names
- Editing restrictions after publication
- Pause, close, expire, archive, and delete distinctions
- Connected application behavior after state changes
- Duplicate or reuse behavior

## Sources

- `products/jobvision/employer/overview.md`
- `products/jobvision/overview.md`
- `shared/product-concepts/job-post.md`
- Reviewed Jira, Figma, production, and walkthrough evidence is required before marking this document reviewed
