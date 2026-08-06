---
id: shared.application
kind: shared-product-concept
title: Application
summary: Defines the shared Application concept that connects Candidate-side submission and tracking with Employer-side recruiting management.
status: draft
owner: Jobvision product teams
last_reviewed:
related:
  - jobvision.overview
  - jobvision.candidate.overview
  - jobvision.employer.overview
  - shared.job-post
  - shared.resume
topics:
  - application
  - job-application
  - candidate
  - employer
  - job-post
  - resume
  - recruiting
---

# Application

## Definition

An Application is the shared representation of a Candidate applying to a specific Job Post. It connects Candidate-side submission and progress tracking with Employer-side receipt and recruiting management.

This concept is distinct from the Apply flow. The shared concept owns the cross-product meaning and relationships of an Application; submission, tracking, review, permissions, and presentation remain in their respective Product Areas.

## Why it matters

Application connects the two sides of the Jobvision product group:

```text
Candidate applies to a Job Post
→ an Application is created
→ Candidate follows its progress
→ Employer receives and manages it
```

A shared definition prevents Candidate and Employer documentation from describing the same recruiting record inconsistently.

## Shared data and attributes

The repository currently supports the core relationship between Candidate action, a Job Post, and Employer-side recruiting activity.

The canonical field set is not yet documented. Candidate identity, Job Post, submission time, source, attached Resume or Resume version, answers, and status must be verified before being treated as confirmed shared attributes.

## Shared lifecycle

The complete lifecycle and exact state names are not yet documented.

Potential stages such as started, submitted, viewed, under review, progressed, rejected, withdrawn, or hired require owner review against Candidate, Employer, and ATS behavior.

## Shared rules

Confirmed at the current level:

- An Application relates Candidate action to a specific Job Post.
- Candidate-side submission and tracking behavior belongs in Candidate Product Areas.
- Employer-side review and recruiting management belongs in Employer Product Areas.
- Shared data, relationships, and lifecycle must not be redefined independently by each product.

Rules about duplicate applications, withdrawal, reapplication, deletion, visibility, status synchronization, and retention remain unknown.

## Used by products and areas

### Jobvision Candidate

Candidate Product Areas will own starting and submitting an Application, validation and eligibility, confirmation, progress tracking, and Candidate-visible states.

### Jobvision Employer

Employer Product Areas will own receiving, viewing, evaluating, progressing, rejecting, and otherwise managing Applications.

### Cando ATS

Whether a Jobvision Application is transferred, copied, synchronized, or represented as another ATS entity requires verification.

## Product-specific variations

The same Application may be represented differently because each product supports different users and decisions:

- Candidate needs submission feedback and understandable progress.
- Employer needs recruiting context, evaluation controls, and operational states.
- ATS may require pipeline-specific data and lifecycle behavior.

Exact variations require Product Area and integration review.

## Unknowns

- Canonical shared fields
- Exact lifecycle and state ownership
- Draft versus submitted Application
- Duplicate-application and reapplication rules
- Withdrawal and deletion behavior
- Relationship with the current Resume and any submitted Resume snapshot
- Relationship with screening questions and answers
- Visibility and retention rules
- Synchronization or mapping with Cando ATS
- Behavior when the related Job Post closes, expires, or is removed

## Sources

- `products/jobvision/overview.md`
- `products/jobvision/candidate/overview.md`
- `products/jobvision/employer/overview.md`
- `shared/product-concepts/job-post.md`
- Product-owner decision during Candidate Product Area mapping on 2026-08-06
- Additional Jira, Figma, production, analytics, and walkthrough evidence is required before review
