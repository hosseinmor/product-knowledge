---
id: cando.salary.job-profiles
kind: product-area
group: cando
product: salary
title: Job Profiles
summary: Maps organization job titles to standard titles and creates suggested, editable job-profile content and requirements.
status: reviewed
owner: Cando Salary product owner
last_reviewed: 2026-08-11
related:
  - cando.salary.overview
  - cando.salary.team-compensation
  - cando.salary.salary-benchmark
topics: [job-profile, job-title, standard-title, seniority, requirements]
---

# Job Profiles

## Overview

Job Profiles maps an organization's job title and seniority to a standard job title, then creates a suggested profile with requirements and editable content.

## Why this area exists

- Normalize organization-specific job titles against a standard title
- Produce a reusable profile for employee and compensation workflows
- Give users a suggested starting point that can be edited

## Users and roles

An authenticated user created one real job profile at the user's request. Creation and editing permissions by role are unknown.

## User outcomes

- Preserve the organization's own title
- Select seniority and a standard job title
- Create and review suggested requirements and profile content
- Edit generated content where necessary

## Entry points

- Job-title or Job Profile area
- Employee creation's job-profile selection

## Main concepts

### Organization job title

The title used by the organization for the role.

### Seniority

The selected level associated with the job profile. Allowed values and effect are unknown.

### Standard job title

The normalized title selected during creation. Suggestion and matching rules are unknown.

### Job profile

The created record containing suggested requirements and other editable content.

### Suggested content

Content generated or populated after creation. The source, generation method, review status, and refresh behavior are unknown.

## Main flows

### Create a job profile

1. Enter the organization's job title.
2. Select seniority.
3. Select a standard job title.
4. Confirm creation.
5. Review the suggested job profile, requirements, and editable content.

## Rules

- Creation requires an organization title, seniority, and a standard job title in the observed flow.
- The created profile supplies suggested requirements and editable content.
- No automatic title-matching or content-generation rule is confirmed.

## Permissions

Creation was available. View, edit, delete, approval, and publishing permissions are unknown.

## States and transitions

```text
Creation input
→ standard title selected
→ creation confirmed
→ suggested editable profile available
```

Draft, reviewed, approved, archived, and deleted states were not established.

## Validations

Duplicate-title behavior, required field messages, invalid combinations, and content validation were not tested.

## Edge cases

- No suitable standard title
- Multiple possible standard titles
- Duplicate organization title and seniority
- Generated content missing or unsuitable
- Standard taxonomy changes after creation
- Profile in use by employees when edited or deleted

## Related Product Areas

- [Team Compensation](team-compensation.md)
- [Salary Benchmark](salary-benchmark.md)

## Known variations

Only one title and selected seniority were tested.

## Unknowns and untested behavior

Matching and generation rules, taxonomy ownership, required fields, edit persistence, lifecycle, deletion safeguards, permissions, and benchmark recalculation after changes.

## Sources

- Owner-accepted `WT-2026-008`: E-008; recorded 2026-08-09 and treated as reviewed 2026-08-11
