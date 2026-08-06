---
id: shared.resume
kind: shared-product-concept
title: Resume
summary: Defines the shared Resume concept managed by Candidates and consumed in Jobvision recruiting experiences.
status: draft
owner: Jobvision product teams
last_reviewed:
related:
  - jobvision.overview
  - jobvision.candidate.overview
  - jobvision.employer.overview
  - shared.application
topics:
  - resume
  - candidate
  - employer
  - application
  - professional-profile
  - recruiting
---

# Resume

## Definition

A Resume is the shared representation of a Candidate's professional background used in Jobvision recruiting experiences. Candidate owns building and maintaining the Resume experience, while Employer-side recruiting may consume a representation of it.

This concept owns only the meaning, relationships, and lifecycle that are genuinely shared across products. Resume creation, editing, completeness guidance, visibility, access, and presentation stay in their respective Product Areas.

## Why it matters

Resume connects Candidate-managed professional information with recruiting decisions:

```text
Candidate builds and updates a Resume
→ Candidate may use it when applying
→ Employer may view a Resume representation
→ recruiting activity may depend on that representation
```

A shared definition is especially important for distinguishing the current editable Resume from the version associated with an Application.

## Shared data and attributes

The canonical field set is not yet documented.

Likely categories such as identity and contact information, work experience, education, skills, languages, preferences, attachments, completeness, and visibility must be verified before being treated as confirmed shared attributes.

## Shared lifecycle

The complete lifecycle and state model are unknown.

The repository does not yet establish whether Resume states include incomplete, complete, published, hidden, archived, or versioned, or whether those labels are shared across products.

## Shared rules

Confirmed at the current level:

- Candidate manages Resume information in the Candidate product.
- Resume information may be used in application and employer-side recruiting experiences.
- Product-specific editing, validation, permissions, visibility, and presentation must remain in Product Areas.
- The relationship between a current Resume and the Resume representation attached to an Application must be explicit.

Whether an Application stores a frozen snapshot, a live reference, a generated document, or a combination remains unknown.

## Used by products and areas

### Jobvision Candidate

Candidate Product Areas will own Resume creation, editing, completion, preview, export, visibility, and selection during application where applicable.

### Jobvision Employer

Employer Product Areas will own access to and use of Resume information in Candidate and Application management, subject to verified permissions and visibility rules.

### Cando ATS

Whether Resume data is transferred, copied, synchronized, or separately maintained in Cando ATS requires verification.

## Product-specific variations

- Candidate needs editable structured information, guidance, preview, and control.
- Employer needs a recruiting-oriented representation with appropriate access.
- An Application may need a stable historical representation even after Candidate edits the current Resume.
- ATS may use a separate normalized candidate profile or document.

Exact differences require product and integration review.

## Unknowns

- Canonical shared fields
- Resume ownership and identity model
- Current Resume versus Application Resume snapshot
- Versioning and historical behavior
- Visibility and privacy rules
- Multiple Resume or language variants
- Generated file versus structured-data relationship
- Export and download rules
- Employer access before and after application
- Synchronization or mapping with Cando ATS
- Deletion and retention behavior

## Sources

- `products/jobvision/overview.md`
- `products/jobvision/candidate/overview.md`
- `products/jobvision/employer/overview.md`
- `shared/product-concepts/application.md`
- Product-owner decision during Candidate Product Area mapping on 2026-08-06
- Additional Jira, Figma, production, analytics, and walkthrough evidence is required before review
