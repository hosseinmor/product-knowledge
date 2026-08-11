---
id: cando.salary.scenario-analysis
kind: product-area
group: cando
product: salary
title: Scenario Analysis
summary: Creates, recalculates, edits, compares, and deletes alternative compensation scenarios in Cando Salary.
status: reviewed
owner: Cando Salary product owner
last_reviewed: 2026-08-11
related:
  - cando.salary.overview
  - cando.salary.salary-benchmark
  - cando.salary.team-compensation
topics: [scenario, compensation-planning, recalculation, complexity, payment-strategy]
---

# Scenario Analysis

## Overview

Scenario Analysis adds a persistent comparison column based on selected compensation settings, then lets the user edit and recalculate or delete it.

## Why this area exists

- Compare an alternative compensation policy with the primary team result
- Keep a scenario available for later review and editing
- Recalculate comparison results when settings change

## Users and roles

An authenticated user able to create, edit, and delete a test scenario was observed. Formal roles and sharing rules are unknown.

## User outcomes

- Create an alternative scenario
- Apply a complexity factor or payment strategy
- Compare calculated results in a separate column
- Revise and recalculate a scenario
- Remove an obsolete scenario with confirmation

## Entry points

- Scenario Analysis page
- Scenario column and its overflow actions

## Main concepts

### Scenario

A saved set of alternative calculation settings represented as a comparison column.

### Scenario setting

An activated compensation input. Complexity factor and payment strategy were observed.

### Scenario result column

The persisted comparison output produced after saving and calculating a scenario.

### Recalculation

The update of scenario results after edited settings are saved.

## Main flows

### Create and calculate a scenario

1. Start a new scenario.
2. Activate a complexity factor or payment strategy.
3. Save and calculate.
4. Review the new scenario comparison column.

### Edit and recalculate

1. Reopen an existing scenario.
2. Change its setting.
3. Save.
4. Review the recalculated result.

### Delete a scenario

1. Choose delete from the scenario overflow.
2. Review the warning that all scenario information will be removed.
3. Confirm deletion.
4. Observe that the test scenario is removed.

## Rules

- A saved scenario creates a persistent comparison column.
- Saving edits recalculates scenario results.
- Deletion requires confirmation and removes all scenario information.

## Permissions

Create, edit, and delete were available to the observed user. Ownership, sharing, and role-specific restrictions are unknown.

## States and transitions

```text
Draft settings
→ saved and calculated
→ edited
→ recalculated
→ deleted after confirmation
```

## Validations

Required settings, valid ranges, conflicting combinations, and duplicate names were not tested.

## Edge cases

- Multiple filters and settings used together
- Multiple scenarios and ordering
- Calculation failure or partial results
- Concurrent edits
- Deleted-scenario recovery
- Scenario based on changed benchmark data

## Related Product Areas

- [Salary Benchmark](salary-benchmark.md)
- [Team Compensation](team-compensation.md)

## Known variations

Complexity factor and payment strategy were visible settings; only a controlled single-scenario path was tested.

## Unknowns and untested behavior

Setting definitions, combination rules, permissions, sharing, limits, filters, failure behavior, history, and recovery after deletion.

## Sources

- Owner-accepted `WT-2026-008`: E-006 and E-007; recorded 2026-08-09 and treated as reviewed 2026-08-11
