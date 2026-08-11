---
id: cando.salary.team-compensation
kind: product-area
group: cando
product: salary
title: Team Compensation
summary: Employee compensation records, team search, benchmark-calculation status, and final-salary entry in Cando Salary.
status: reviewed
owner: Cando Salary product owner
last_reviewed: 2026-08-11
related:
  - cando.salary.overview
  - cando.salary.salary-benchmark
  - cando.salary.job-profiles
  - cando.salary.organization-settings
topics: [team, employee, compensation, final-salary, suggested-salary]
---

# Team Compensation

## Overview

Team Compensation is the employee-level workspace for finding team members, maintaining compensation inputs, starting benchmark calculation, reviewing suggested ranges, and recording a final salary. This document reflects one owner-accepted authenticated Production walkthrough.

## Why this area exists

- Keep employee, organization, job, and compensation inputs together
- Compare the employee's 1404 salary, suggested 1405 range, and final 1405 salary
- Make calculation progress and result availability visible

## Users and roles

An authenticated organizational user with visible create, edit, and delete controls was observed. Formal roles and permission boundaries are unknown.

## User outcomes

- Find an employee by personnel code
- Add or edit an employee compensation record
- Start calculation and see when a suggested range becomes available
- Record a final salary and compare it with the prior year's salary

## Entry points

- Product Home, which redirected to Team in the observed session
- Team list
- Employee-detail drawer

## Main concepts

### Employee compensation record

A record combining identity, organization, job-profile, and compensation information for one employee.

### Current salary

The employee's 1404 salary shown as the comparison baseline.

### Suggested salary range

The calculated 1405 range produced after saving sufficient employee inputs. Its formula and authority are unknown.

### Final salary

A separately recorded 1405 amount. In the observed test it was inside the suggested range, so out-of-range behavior is unknown.

### Calculation status

The Team row temporarily showed “در حال محاسبه” before displaying the suggested range.

## Main flows

### Search the team

1. Open Team.
2. Review organizational and compensation columns.
3. Search by personnel code to narrow the list.

Other search semantics were not tested.

### Add an employee and calculate

1. Open the add-employee dialog.
2. Enter identity, organization, and compensation information.
3. Connect the employee to an existing job profile and organization structure.
4. Save and calculate once required selections make the action available.
5. Observe the calculation-in-progress state.
6. Review the resulting suggested salary range.

### Record final salary

1. Open employee detail.
2. Enter the final 1405 salary.
3. Save it.
4. Review the amount and its percentage comparison with the 1404 salary.

## Rules

- Save and calculate remains unavailable until required inputs and selections are supplied.
- Saving a complete observed record starts benchmark calculation.
- Final salary is stored separately from the suggested range.

## Permissions

Create, edit, and delete controls were visible. Role-specific access, field-level restrictions, approval, and audit behavior are unknown.

## States and transitions

```text
Employee form incomplete
→ complete enough to save and calculate
→ calculating
→ suggested range available
→ final salary optionally recorded
```

Failure, retry, stale-result, and recalculation transitions were not observed.

## Validations

The primary action was disabled for an empty form and enabled after required inputs were provided. The complete required/optional matrix and field-level messages were not captured.

## Edge cases

- Search values other than personnel code
- Missing job profile or organization structure
- Calculation delay or failure
- Final salary outside the suggested range
- Editing or clearing final salary
- Duplicate employee or personnel code
- Deleting an employee; the observed deletion appeared to succeed without a second confirmation and is a suspected bug

## Related Product Areas

- [Salary Benchmark](salary-benchmark.md)
- [Job Profiles](job-profiles.md)
- [Organization Settings](organization-settings.md)

## Known variations

Employee benchmark detail varies by model and data availability.

## Unknowns and untested behavior

Roles, permissions, complete validation, calculation retry/failure, employee deletion safeguards, empty state, mobile, network failure, and audit history.

## Sources

- Owner-accepted `WT-2026-008`: E-001, E-002, E-003, and E-005; recorded 2026-08-09 and treated as reviewed 2026-08-11
- `WT-2026-008` suspected bug B-002 remains a suspected bug rather than intended product behavior
