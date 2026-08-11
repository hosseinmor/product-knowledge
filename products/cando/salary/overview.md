---
id: cando.salary.overview
kind: product-overview
group: cando
product: salary
title: Salary
summary: Overview of Cando Salary and its compensation benchmarking, planning, job-profile, reporting, and organization-configuration areas.
status: reviewed
owner: Cando Salary product owner
last_reviewed: 2026-08-11
related:
  - cando.overview
  - cando.salary.team-compensation
  - cando.salary.salary-benchmark
  - cando.salary.scenario-analysis
  - cando.salary.job-profiles
  - cando.salary.organization-settings
topics:
  - compensation
  - salary-benchmark
  - team
  - scenario-analysis
  - job-profile
  - organization-settings
---

# Salary

## What this product is

Cando Salary supports an organization in reviewing employee compensation, calculating suggested salary ranges, recording final salaries, comparing alternative compensation scenarios, maintaining job profiles, and configuring the organization structures used by those workflows.

This document is limited to behavior observed in one authenticated Production organization in `WT-2026-008`. The package's E-001 through E-010 claims are treated as owner-accepted for this reconciliation.

## Primary users

- Authenticated organizational users who can view compensation data
- Users who can create or edit employee compensation records, scenarios, job profiles, or organization settings

Formal role names and the permission matrix were not identified.

## Problems it solves

- Comparing current, suggested, and final employee compensation
- Explaining benchmark inputs and insufficient-data outcomes
- Modeling compensation alternatives without replacing the primary result
- Standardizing job titles and generating editable job-profile content
- Keeping departments and business lines usable as organizational inputs

## Product boundaries

### In scope

- Team compensation records
- Salary benchmark results and inputs
- Scenario analysis
- Job profiles
- Organization structure settings
- Team and management report entry points

### Out of scope or not established

- Payroll execution and payment
- Formal performance management
- Recruiting and applicant tracking
- Benchmark model ownership, external data collection, and calculation internals
- Cross-product data synchronization

## Main Product Areas

- [Team Compensation](areas/team-compensation.md)
- [Salary Benchmark](areas/salary-benchmark.md)
- [Scenario Analysis](areas/scenario-analysis.md)
- [Job Profiles](areas/job-profiles.md)
- [Organization Settings](areas/organization-settings.md)

Reporting was observed as an entry point, but the available evidence is not sufficient to define it as an independent Product Area.

## Major user journeys

### Add an employee and calculate a benchmark

```text
Enter identity, organization, and compensation information
→ connect the employee to organization structure and a job profile
→ save and calculate
→ wait while calculation is in progress
→ review the suggested salary range
→ optionally record a final salary
```

### Compare a scenario

```text
Create a scenario
→ activate a complexity factor or payment strategy
→ save and calculate a comparison column
→ edit and recalculate if needed
→ delete with confirmation when no longer needed
```

### Create a job profile

```text
Enter the organization's job title and seniority
→ select a standard job title
→ confirm creation
→ review the suggested, editable profile and requirements
```

## Important integrations

The relationship among employee records, job profiles, departments, business lines, benchmark models, and report generation is visible in the product. System boundaries, data ownership, external benchmark sources, and connections to other Cando products remain unknown.

## Known variations

- A benchmark model can provide percentile or range values, or show that it lacks sufficient data.
- Scenario settings can use a complexity factor or a payment strategy; combinations were not tested.
- Organization structures may or may not have employees assigned to them.

## Documentation gaps and unknowns

- Owner, formal roles, permissions, and plan variations
- Benchmark formulas, weights, sources, timing, retry, and failure handling
- Required and optional fields for employee and job-profile creation
- Empty, error, unauthenticated, mobile, and responsive states
- Report generation and download behavior
- Organization-profile and calculation-model updates
- Integration and synchronization with other Cando products

## Sources

- Owner-accepted walkthrough evidence package `WT-2026-008`, recorded 2026-08-09 and treated as reviewed 2026-08-11; accepted evidence IDs: E-001 through E-010
