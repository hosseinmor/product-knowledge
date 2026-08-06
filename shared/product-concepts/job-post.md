---
id: shared.job-post
kind: shared-product-concept
title: Job Post
summary: Defines the shared Job Post concept used by Jobvision Employer and Candidate while keeping product-specific behavior in separate Product Areas.
status: draft
owner: Jobvision product teams
last_reviewed:
related:
  - jobvision.overview
  - jobvision.employer.job-post-management
  - jobvision.candidate.job-post-experience
  - shared.application
  - shared.resume
  - shared.company
topics:
  - job-post
  - job-opportunity
  - employer
  - candidate
  - application
---

# Job Post

## Definition

A Job Post is the shared representation of a job opportunity that an Employer publishes and a Candidate discovers, evaluates, and may apply to.

This document owns only the meaning that is genuinely shared between Jobvision products. Product-specific flows, permissions, presentation, and actions belong in their respective Product Areas.

## Why it matters

Job Post connects the two sides of the Jobvision product group:

```text
Employer creates and manages a Job Post
→ Candidate discovers and evaluates it
→ Candidate may apply
→ Employer receives and manages the resulting application
```

A shared definition reduces duplication and prevents Candidate and Employer documentation from describing the same business concept inconsistently.

## Shared data and attributes

The repository currently confirms only that a Job Post represents a job opportunity and is used by both Employer and Candidate products.

The canonical shared field set is not yet documented. Likely fields such as title, company, location, requirements, employment type, and publication information must not be treated as confirmed until they are reviewed against product behavior and source documents.

## Shared lifecycle

The repository establishes that Employers publish Job Posts and Candidates discover them, but it does not yet establish the complete shared lifecycle or exact state names.

Potential lifecycle stages such as draft, published, paused, closed, or expired require owner review before being documented as current rules.

## Shared rules

Confirmed at the current level:

- Employer owns the creation and management side of the Job Post.
- Candidate owns the discovery, understanding, and application side of the experience.
- Product-specific actions and permissions must not be centralized here.
- Applications connect a Candidate's action to Employer-side recruiting activity.

Rules about visibility, publication eligibility, editing after publication, closure, expiration, and application availability remain unknown.

## Used by products and areas

### Jobvision Employer

`jobvision.employer.job-post-management` owns employer-side creation, management, publication, and status behavior.

### Jobvision Candidate

`jobvision.candidate.job-post-experience` (`Job Details & Evaluation`) owns how Candidates understand and evaluate a Job Post and access actions such as saving, sharing, reporting, or beginning an application.

## Related shared concepts

- `shared.company` owns the shared Company identity related to the Job Post.
- `shared.application` owns the cross-product record created when a Candidate applies to the Job Post.
- `shared.resume` owns the shared Resume meaning and its relationship with an Application where applicable.

The exact cardinality, historical behavior, snapshots, and synchronization among these concepts remain unknown.

## Product-specific variations

The same Job Post may be represented differently because the products serve different users and outcomes:

- Employer needs management controls, operational status, and recruiting context.
- Candidate needs understandable opportunity information and actions such as saving or applying.

Exact differences require Product Area review.

## Unknowns

- Canonical shared fields
- Shared lifecycle and exact state names
- Visibility and eligibility rules
- Relationship with Company
- Relationship with Application
- Editing and publication rules
- Closure, expiration, and reopening behavior
- Differences between public, private, draft, or restricted opportunities

## Sources

- `products/jobvision/overview.md`
- `products/jobvision/employer/overview.md`
- `products/jobvision/candidate/overview.md`
- Additional Jira, Figma, production, analytics, and walkthrough evidence is required before review
