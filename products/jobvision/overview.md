---
id: jobvision.overview
kind: product-group-overview
group: jobvision
title: Jobvision
summary: Overview of the Jobvision product group and its Candidate and Employer products.
status: draft
owner: Jobvision product leadership
last_reviewed:
related:
  - jobvision.candidate.overview
  - jobvision.employer.overview
  - shared.job-post
  - shared.application
  - shared.resume
  - shared.company
topics:
  - jobvision
  - candidate
  - employer
  - recruitment-marketplace
  - job-post
  - application
  - resume
  - company
---

# Jobvision

## What this product group is

Jobvision is the product group that connects jobseekers and employers through two distinct products:

- Candidate
- Employer

The two products share Job Post, Application, Resume, and Company concepts, but their users, outcomes, permissions, and flows are different. The cross-product Candidate identity model remains to be clarified.

## Products

### Candidate

Supports people who search for jobs, understand opportunities, manage resumes, apply, and follow their job-search activity.

Path:

```text
products/jobvision/candidate/
```

### Employer

Supports organizations and recruiting teams that publish opportunities, manage employer-side recruiting activity, and use Jobvision employer services.

Path:

```text
products/jobvision/employer/
```

## Shared journeys and relationships

```text
Employer creates and publishes a Job Post
→ Candidate discovers and evaluates it
→ Candidate applies
→ Employer reviews the application
```

Shared definitions for Job Post, Application, Resume, and Company are documented under `shared/product-concepts/`. Product-specific behavior remains in each product's Product Areas.

## Documentation gaps

- The complete boundary between Candidate, Employer, and Cando needs owner review.
- The relationship among User Account, Candidate Profile, Applicant, and ATS Candidate is not yet documented.
- Candidate and Employer Product Areas need progressive discovery and completion.

## Sources

Add product strategy, Jira, Figma, analytics, research, and walkthrough references as the group overview is reviewed.
