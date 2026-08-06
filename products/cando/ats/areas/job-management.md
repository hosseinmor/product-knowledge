---
id: cando.ats.job-management
kind: product-area
group: cando
product: ats
title: Job Management
summary: Describes how Cando ATS users create, configure, publish, and manage jobs and their candidate pipelines.
status: reviewed
owner: ATS product team
last_reviewed: 2026-08-06
related:
  - cando.ats.overview
  - shared.ai-services.overview
topics:
  - job-management
  - job-definition
  - application-form
  - hiring-pipeline
  - job-publication
  - candidate-management
  - automatic-rejection
  - ai-ranking
---

# Job Management

## Overview

Job Management is the Cando ATS area where recruiting users find jobs, define job-specific information and application settings, configure the hiring pipeline and team access, publish or source candidates, and manage applications for a job.

This document reflects the behavior observed in one authenticated account. It is reviewed for that observed scope; account, plan, role, and untested lifecycle variations remain explicit below.

## Why this area exists

- Keep the definition, application experience, hiring process, team access, and publication settings for a job together
- Help recruiting users find and monitor active, internal, and archived jobs
- Give each job a pipeline-aligned workspace for reviewing applications
- Support candidate sourcing and publication through available channels

## Users and roles

Observed behavior supports an authenticated organizational user who can view jobs and open their configuration and candidate boards.

Job-level team members can be added, and the interface describes this assignment as granting access to that job.

Still unknown:

- Formal role names
- Which roles can create, edit, publish, archive, or manage candidates
- Whether access is inherited from account, department, or organization permissions
- What access is granted to a job-level team member

## User outcomes

- Find a relevant job and understand its operational status
- Start a new job from scratch or copy an existing job
- Define job information and internal management context
- Configure the candidate application form and evaluation questions
- Configure the job's hiring stages and stage-level automation
- Give team members access to the job
- Publish the job or source candidates through available channels
- Review and organize applications in a board aligned with the hiring stages

## Entry points

Observed entry points include:

- Dashboard links and job-related summaries
- The Jobs list at `/jobs`
- Create Job from the Jobs list
- Edit actions on a job card
- The job's candidate-management board

The dashboard can show followed jobs, upcoming work, interview status, and recent recruitment activity with stage counts. Exact dashboard content may depend on role, account configuration, and available data.

## Main concepts

### Job

A hiring workspace with job information, application settings, a hiring pipeline, team access, publication settings, and associated applications.

The relationship between a Job and an approved Recruitment Request is not established by the reviewed walkthrough.

### Job list and card

The Jobs list groups jobs as active, internal, or archived and supports text search, status filtering, sorting, followed-job access, advanced-search entry, and pagination.

A job card can summarize application counts, status, stage counts, publication destinations, department, creator, creation time, and actions such as adding a resume or editing the job. The meaning of every compact stage count was not verified.

### Job definition

Job configuration is organized into five observed steps:

1. Job description
2. Application form
3. Hiring stages
4. Team members
5. Publication

### Application form

The candidate fields and evaluation questions configured for a specific job.

### Hiring pipeline

The job-specific stages used to organize active applications. Observed stage sections include input, evaluation, job offer, and hired.

### Job-level team

Users assigned access to a specific job. The exact permission set is unknown.

### Publication channel

A destination or recruiting service through which the job may be published or candidates may be sourced. Observed options included the organization's careers page, JobVision, and other recruiting services.

### Candidate board

A job-level board that displays active applications in columns aligned with hiring stages and separates in-progress and rejected applications.

## Main flows

### Find and open a job

1. The user opens the Jobs list.
2. They select an active, internal, or archived group.
3. They may search, filter, sort, use advanced-search entry, show followed jobs, or paginate.
4. They review the job card's operational and publication summary.
5. They open the job for configuration or candidate management.

Advanced-search fields and exact search behavior were not tested.

### Start job creation

1. The user chooses Create Job.
2. They choose either to copy an existing job and edit its information or to define a new job from scratch.
3. The product opens the job-definition flow.

The copied fields, conflict behavior, save behavior, and completion requirements were not tested.

### Define job information

The first step can collect:

- Job title
- Advertisement language
- Job category
- Department
- Work location
- Employment type
- Remote-work setting
- Candidate restrictions
- Salary
- Working days
- Experience
- Seniority
- Internship setting
- Job description
- Internal management note

Which fields are required and which are candidate-visible were not tested.

### Configure the application form

1. The user opens the Application Form step for a job.
2. They set candidate fields as required, optional, or hidden.
3. They may add evaluation questions.
4. The interface states that required evaluation questions can be used to automatically reject irrelevant applications.

Automatic rejection logic, thresholds, execution, recovery, and audit behavior were not tested.

### Configure hiring stages

1. The user opens the Hiring Stages step.
2. They review stages organized into input, evaluation, job-offer, and hired sections.
3. They may add an evaluation stage.
4. They may connect an evaluation form and automatic notification to a stage.

Stage removal, reordering, transition rules, automation triggers, and failure handling were not tested.

### Configure team access

1. The user opens the Team Members step.
2. They add one or more members to the job.
3. The interface presents this assignment as granting access to the job.

Role selection, permission detail, notification, and the effect of removing a member were not tested.

### Manage publication and sourcing

1. The user opens the Publication step.
2. They review the job status and management-page link.
3. They choose from available publication or resume-sourcing actions.
4. Available destinations may include the organization's careers page, JobVision, and other recruiting services.

Channel eligibility, cost, moderation, synchronization, unpublishing, and failure recovery were not tested.

### Manage applications for a job

1. The user opens the job's candidate board.
2. They switch between in-progress and rejected applications.
3. Active applications appear in hiring-stage columns with counts.
4. They may add a resume, search, filter, sort, open automatic-rejection entry, or view or edit the job.
5. The interface also offers AI-assisted sorting of the most relevant resumes and describes the ranking as based on match with the job description.

Candidate movement, bulk actions, rejection, restoration, concurrent updates, and history were not tested. AI ranking quality, model inputs, explainability, refresh timing, bias, configuration, and override behavior are also unknown.

## Rules

- Job configuration is organized into five steps: Job Description, Application Form, Hiring Stages, Team Members, and Publication.
- Candidate fields can be configured per job as required, optional, or hidden.
- Evaluation questions can be added to a job's application form.
- The interface states that required evaluation questions can support automatic rejection of irrelevant applications; the underlying rule is not verified.
- Evaluation stages can be added to a job's hiring pipeline.
- An evaluation form and automatic notification can be associated with a hiring stage.
- Assigning a team member is presented as granting access to that job; the permission scope is not verified.
- The candidate board follows the job's configured hiring stages at the observed presentation level.
- AI-assisted relevance sorting is presented as ranking resumes by match with the job description; no underlying service behavior is confirmed.

## Permissions

Observed:

- The authenticated user could view the Jobs list and open job configuration and candidate-management pages.
- Job-level team-member assignment is presented as a way to grant access to a job.

Unknown:

- Create, edit, publish, archive, and candidate-action permissions by role
- Job-level permission detail and inheritance
- Department or account scoping
- Administrator override behavior
- Access revocation and audit behavior

## States and transitions

Observed job groupings:

```text
Active
Internal
Archived
```

These labels were observed in the Jobs list, but their complete lifecycle, allowed transitions, and relationship to publication state were not tested.

Observed candidate-board groupings:

```text
In progress
Rejected
```

In-progress applications are displayed in stage columns. Candidate transition, rejection, restoration, and terminal-state rules remain unknown.

## Validations

No validation behavior was executed. Still unknown:

- Required fields in each definition step
- Whether users can skip or revisit steps before the job is saved
- Save, draft, and incomplete-job behavior
- Invalid application-form or pipeline configurations
- Publication eligibility and channel-specific validation
- Duplicate actions and retry behavior
- Validation messages and field focus behavior

## Edge cases

The following cases were not tested:

- Copying a job with unavailable or conflicting settings
- Leaving with unsaved changes, cancelling, refreshing, or returning later
- Removing or reordering a stage with existing applications
- Removing a job-level team member
- Losing permission while a job is open
- Publication or synchronization failure in an external channel
- Automatic rejection of a relevant candidate or restoration after rejection
- Simultaneous candidate updates by multiple users
- AI ranking unavailable, delayed, uncertain, or misleading
- Account or plan without one or more publication channels

## Related Product Areas

- [ATS Overview](../overview.md)
- Candidate Management, which is not yet documented as a separate Product Area
- Recruitment Request; the relationship between an approved request and a job requires verification
- Shared AI Product Services; only the product-specific user-facing ranking behavior is currently documented here

## Known variations

- Jobs can appear in active, internal, or archived groupings in the observed account.
- Available publication and sourcing channels may vary by account, plan, or configuration.
- Dashboard summaries may vary by role, configuration, and data.
- The observed account had jobs with multiple evaluation stages and multiple assigned team members; other accounts may be configured differently.

## Unknowns and untested behavior

- Formal role and permission matrix
- Complete job lifecycle from draft through publication, closure, and archival
- Relationship between Job and Recruitment Request
- Save, validation, cancellation, persistence, and recovery behavior across all five steps
- Candidate-facing application form
- Candidate transition, rejection, restoration, bulk actions, and history
- Evaluation completion and notification delivery
- Publication-channel eligibility, moderation, synchronization, cost, and recovery
- Automatic-rejection rules, thresholds, audit, and recovery
- AI-ranking inputs, quality, explainability, refresh behavior, bias, configuration, and fallback

## Sources

- Reviewed walkthrough evidence package `WT-2026-001`, recorded 2026-08-05 and owner-reviewed 2026-08-06
- Authenticated, read-only observation of `https://newats.hrcando.ir`; no job or candidate data was changed
