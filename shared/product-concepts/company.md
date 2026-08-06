---
id: shared.company
kind: shared-product-concept
title: Company
summary: Defines the shared Company concept represented in Jobvision Employer and Candidate experiences.
status: draft
owner: Jobvision product teams
last_reviewed:
related:
  - jobvision.overview
  - jobvision.candidate.overview
  - jobvision.employer.overview
  - shared.job-post
topics:
  - company
  - employer
  - candidate
  - company-profile
  - job-post
  - followed-company
  - company-review
---

# Company

## Definition

A Company is the shared representation of an employing organization in Jobvision. Employer-side users manage organization-facing information and recruiting activity, while Candidates encounter the Company through Job Posts, Company information, following, ratings, and reviews.

This concept must remain distinct from an Employer user account, an employer subscription or plan, a legal entity, and a brand unless product evidence confirms they are the same object.

## Why it matters

Company connects employer-managed identity with Candidate trust and discovery:

```text
Employer represents an organization
→ the organization publishes Job Posts
→ Candidate evaluates the Company and its opportunities
→ Candidate may follow, rate, or review the Company
```

A shared definition prevents inconsistent Company identity and relationships across Employer and Candidate products.

## Shared data and attributes

The canonical field set is not yet documented.

Likely information such as name, logo, industry, size, description, locations, verification, public profile, and relationships with Employer accounts and Job Posts must be verified before being treated as confirmed shared attributes.

Ratings, reviews, and follow relationships may be separate entities connected to Company rather than Company attributes.

## Shared lifecycle

The complete shared lifecycle is unknown.

Potential states related to creation, verification, publication, suspension, merging, or archival require owner review. Employer account status and Company visibility may have separate lifecycles.

## Shared rules

Confirmed at the current level:

- Company connects Employer-side organization representation with Candidate-facing information.
- Job Posts relate to a Company.
- Candidate experiences include Company following, ratings, or reviews.
- Product-specific management, permissions, presentation, follow behavior, and review behavior remain in Product Areas.
- Company must not automatically be equated with Employer account, subscription, legal entity, or brand.

Exact ownership, verification, visibility, duplicate handling, and moderation rules remain unknown.

## Used by products and areas

### Jobvision Employer

Employer Product Areas will own Company profile management, organization access, account relationships, and recruiting context.

### Jobvision Candidate

Candidate Product Areas will own viewing and evaluating Company information, following Companies, and creating or consuming ratings and reviews where applicable.

### Job Posts and Applications

Company provides organization context for Job Posts and the Applications related to them. Exact historical behavior if Company information changes requires verification.

## Product-specific variations

- Employer needs editable organization information, access control, and operational context.
- Candidate needs trustworthy public information and signals for evaluating opportunities.
- Ratings, reviews, and follows have Candidate-specific permissions and states that should not be centralized in this concept.

Exact differences require Product Area review.

## Unknowns

- Canonical Company fields
- Company versus Employer account, organization, brand, and legal entity
- Ownership and administrator relationships
- Verification and public-visibility rules
- Duplicate, merge, rename, and archival behavior
- Relationship with locations and branches
- Relationship with Job Posts and historical Applications
- Whether ratings and reviews belong to Company or a separate concept
- Follow relationship and notification behavior
- Moderation and employer response permissions

## Sources

- `products/jobvision/overview.md`
- `products/jobvision/candidate/overview.md`
- `products/jobvision/employer/overview.md`
- `shared/product-concepts/job-post.md`
- Product-owner decision and Candidate product walkthrough on 2026-08-06
- Additional Jira, Figma, production, analytics, and walkthrough evidence is required before review
