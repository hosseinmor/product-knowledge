---
id: jobvision.candidate.job-post-experience
kind: product-area
group: jobvision
product: candidate
title: Job Details & Evaluation
summary: Describes how Candidates understand and evaluate a specific Job Post, use supporting information and actions, and decide whether to save, share, or begin applying.
status: draft
owner: Candidate product team
last_reviewed:
related:
  - jobvision.candidate.overview
  - shared.job-post
  - jobvision.employer.job-post-management
topics:
  - job-post
  - job-discovery
  - save-job
  - share-job
  - apply
  - candidate
---

# Job Details & Evaluation

## Overview

Job Details & Evaluation is the Candidate-side Product Area for understanding and evaluating a specific job opportunity and deciding whether to save, share, or begin applying.

This draft is intentionally high-level because the current repository does not yet contain a complete production walkthrough or reviewed specification for the Candidate Job Post experience.

## Relationship to the shared Job Post concept

`shared.job-post` owns the definition, canonical shared attributes, relationships, and lifecycle of a Job Post across Candidate and Employer products.

This Product Area owns the Candidate-specific outcomes, presentation, permissions, states, and flows for understanding and evaluating one Job Post. It may expose actions such as saving, sharing, reporting, or beginning an application, while the detailed submission and post-submission journeys belong in their own Candidate Product Areas.

Employer-specific creation, publication, editing, and management behavior remains in `jobvision.employer.job-post-management`.

## Why this area exists

- Help Candidates understand a job opportunity
- Present the information needed to evaluate relevance and fit
- Provide actions such as saving, sharing, and applying
- Connect Job Post discovery to the application journey

## Users and roles

- Candidate or jobseeker viewing a Job Post
- Authenticated Candidate using personalized or application-related actions
- Unauthenticated visitor when public Job Posts are accessible

Authentication and permission differences require verification.

## User outcomes

- Understand the role, employer, requirements, and context of an opportunity
- Decide whether the opportunity is relevant
- Save or share the Job Post when needed
- Apply when eligible and interested
- Understand what happens after applying

## Entry points

Known or expected entry points include:

- Job search results
- Recommended jobs
- Saved jobs
- Shared or external links
- Application history
- Notifications or campaigns

The complete list and deep-link behavior require review.

## Main concepts

### Job Post

The shared opportunity defined in `shared.job-post`.

### Candidate Action

An action such as saving, sharing, or applying that is specific to the Candidate experience.

### Application

The Candidate's submission or expression of interest connected to a Job Post. The complete Application concept is not yet documented.

## Main flows

### View and understand a Job Post

1. The Candidate opens a Job Post.
2. The product presents opportunity and employer information.
3. The Candidate reviews requirements, context, and available actions.
4. The Candidate decides whether to leave, save, share, or apply.

The exact information hierarchy and required fields are not yet documented.

### Save a Job Post

1. The Candidate chooses Save.
2. Authentication may be required.
3. The Job Post becomes available in a saved-jobs experience.

Persistence, duplicate action, removal, and unavailable-post behavior require verification.

### Share a Job Post

1. The Candidate chooses Share.
2. The product exposes one or more sharing methods.
3. The shared link should resolve to the intended Job Post when available.

The exact methods and unavailable-link behavior are unknown.

### Apply to a Job Post

1. The Candidate chooses Apply.
2. Eligibility, authentication, and required application information are checked.
3. The Candidate completes or confirms the application.
4. The product communicates success or a blocking condition.
5. The resulting Application becomes available to the Employer side.

The detailed Application flow belongs in a future Application Management Product Area.

## Rules

Confirmed only at the current level:

- Candidate-side Job Post behavior must use the shared Job Post concept without owning employer management rules.
- Applying creates a connection between the Candidate and Employer recruiting experience.
- Authentication, eligibility, and application-state rules must remain explicit when documented.

Visibility, save, share, application, and personalization rules require owner review.

## Permissions

Potential permission distinctions include:

- Public viewing versus authenticated viewing
- Saving or applying while unauthenticated
- Applying with an incomplete or unavailable resume
- Viewing personalized insights or premium information

None of these distinctions are fully documented yet.

## States and transitions

The Candidate experience may need to represent states such as:

- Available to view
- Saved or not saved
- Eligible or blocked from applying
- Not applied, applying, applied, or previously applied
- Job Post unavailable, closed, or expired

Exact state names and transitions require verification and must align with `shared.job-post` and future Application documentation.

## Validations

Likely validation areas that require evidence:

- Authentication
- Candidate profile or resume readiness
- Job Post availability
- Duplicate application
- Required application questions or information
- Eligibility or account restrictions

## Edge cases

- Job Post becomes unavailable while open
- Candidate opens an old or shared link
- Candidate has already applied
- Save or apply action is repeated
- Authentication interrupts the flow
- Resume or profile is incomplete
- Application fails after partial progress
- Premium or AI insight is unavailable or uncertain

These cases remain untested in the current repository.

## Related Product Areas

- Job Search
- Application Management
- Resume Management
- Premium Insights
- Employer Job Post Management

## Known variations

- Authentication state may change available actions.
- Premium or AI-powered insights may add product-specific behavior.
- Mobile and desktop presentations may differ.

## Unknowns and untested behavior

- Canonical information hierarchy
- Exact save and share behavior
- Authentication gates
- Application eligibility and required data
- Duplicate application handling
- Job Post unavailable and expired states
- Return behavior after login or application
- Accessibility and responsive behavior

## Sources

- `products/jobvision/candidate/overview.md`
- `products/jobvision/overview.md`
- `shared/product-concepts/job-post.md`
- A bounded production walkthrough and reviewed Jira/Figma sources are required before marking this document reviewed
