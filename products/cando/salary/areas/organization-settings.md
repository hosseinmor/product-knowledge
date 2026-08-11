---
id: cando.salary.organization-settings
kind: product-area
group: cando
product: salary
title: Organization Settings
summary: Organization profile and structure settings, including departments and business lines used by Cando Salary.
status: reviewed
owner: Cando Salary product owner
last_reviewed: 2026-08-11
related:
  - cando.salary.overview
  - cando.salary.team-compensation
topics: [organization-settings, department, business-line, referential-integrity]
---

# Organization Settings

## Overview

Organization Settings maintains organization information and the departments and business lines referenced by employee records. The walkthrough tested deletion guards for structures with assigned employees but did not save organization-profile or calculation-model changes.

## Why this area exists

- Maintain structures used to classify employees
- Prevent deletion from leaving assigned employees without a valid structure
- Provide organization-level configuration entry points

## Users and roles

An authenticated user with visible create, edit, and delete controls was observed. Administrator roles and configuration permissions are unknown.

## User outcomes

- View organization settings
- Create or edit departments and business lines
- Understand why an in-use structure cannot be deleted
- Move employees before retrying deletion

## Entry points

- Settings
- Department configuration
- Business-line configuration

## Main concepts

### Organization profile

Organization-level information visible in Settings. Actual changes were deliberately not saved.

### Department

An organizational unit that can be assigned to employees.

### Business line

An organizational classification that can be assigned to employees.

### Assigned employee

An employee record referencing a department or business line.

### Deletion guard

A rule blocking deletion of a structure that still has assigned employees and directing the user to move those employees elsewhere.

## Main flows

### Attempt to delete an in-use structure

1. Open department or business-line settings.
2. Choose delete for a structure with assigned employees.
3. Observe that deletion is blocked.
4. Follow the guidance to transfer employees to another unit before trying again.

Empty-structure deletion was not tested.

## Rules

- A department with assigned employees cannot be deleted in the observed flow.
- A business line with assigned employees cannot be deleted in the observed flow.
- The product directs the user to move assigned employees to another unit first.

## Permissions

Create, edit, and delete controls were visible. Exact administrative permissions and field-level access are unknown.

## States and transitions

```text
Structure has assigned employees
→ deletion blocked
→ employees moved elsewhere (instructed, not tested)
→ deletion may become available (not tested)
```

## Validations

Deletion dependency was validated by the product. Naming, uniqueness, hierarchy, required fields, and empty-structure deletion were not tested.

## Edge cases

- Empty department or business line
- Moving many employees before deletion
- Last available structure
- Concurrent assignments during deletion
- Structure referenced by scenarios, reports, or historical results
- Unsaved organization-profile or model changes

## Related Product Areas

- [Team Compensation](team-compensation.md)

## Known variations

Both department and business-line structures exhibited the same observed in-use deletion guard.

## Unknowns and untested behavior

Creation and editing rules, hierarchy, uniqueness, bulk transfer, empty deletion, organization-profile saving, calculation-model settings, permissions, and audit history.

## Sources

- Owner-accepted `WT-2026-008`: E-009; recorded 2026-08-09 and treated as reviewed 2026-08-11
