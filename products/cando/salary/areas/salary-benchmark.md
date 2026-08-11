---
id: cando.salary.salary-benchmark
kind: product-area
group: cando
product: salary
title: Salary Benchmark
summary: Suggested compensation results and the model-level inputs, weights, sources, percentiles, ranges, and insufficient-data states behind them.
status: reviewed
owner: Cando Salary product owner
last_reviewed: 2026-08-11
related:
  - cando.salary.overview
  - cando.salary.team-compensation
  - cando.salary.scenario-analysis
topics: [salary-benchmark, compensation-model, percentile, range, payment-strategy, complexity]
---

# Salary Benchmark

## Overview

Salary Benchmark presents a suggested salary result and the model-level information available to explain it. The observed presentation claims are owner-accepted; the calculation internals were not audited.

## Why this area exists

- Give compensation users a suggested salary range for an employee
- Expose the visible factors and model sections behind a result
- Make insufficient benchmark data explicit

## Users and roles

An authenticated organizational user viewing an employee with a calculated result was observed. Access and configuration permissions are unknown.

## User outcomes

- Review suggested and final compensation together
- Understand visible payment-strategy and complexity inputs
- Inspect model sections, weights, sources, and percentile or range values
- Recognize when a model has insufficient data

## Entry points

- Employee-detail drawer after calculation
- Team row's suggested-range result
- Scenario Analysis for alternative calculations

## Main concepts

### Benchmark result

The suggested compensation output shown as a 1405 range for an employee.

### Benchmark model

A visible section contributing information to the benchmark explanation. Model ownership, formulas, and aggregation are unknown.

### Model weight

A displayed weight associated with a benchmark model or section. Its exact mathematical effect is not established.

### Benchmark source

The named data source shown for a model where available. Source freshness, quality, and governance were not audited.

### Percentile and range

Values displayed within model detail when available. Their statistical definition and mapping to the final suggestion are unknown.

### Payment strategy and complexity

Visible benchmark inputs that can also be activated in Scenario Analysis. Definitions and allowed values require owner review.

### Insufficient data

A model-level state indicating that enough data was not available to show its normal values.

## Main flows

### Review benchmark detail

1. Open an employee with a calculated result.
2. Review suggested and final salary.
3. Inspect payment strategy and complexity.
4. Review each model's visible weight, source, and percentile or range values.
5. Note models that report insufficient data.

## Rules

- Benchmark detail may contain multiple model sections.
- A model may show values or an insufficient-data message.
- The visible weight and source should not be interpreted as a confirmed calculation rule until owner review.

## Permissions

Viewing was observed. Model-edit access and role boundaries were not tested.

## States and transitions

```text
No result visible
→ calculating
→ result available
```

At model level:

```text
Values available | insufficient data
```

## Validations

No calculation-model validation was tested.

## Edge cases

- One or all models lacking data
- Conflicting model suggestions
- Zero or changed weights
- Stale source data
- Recalculation after employee, job-profile, organization, or model changes
- Calculation timeout or failure

## Related Product Areas

- [Team Compensation](team-compensation.md)
- [Scenario Analysis](scenario-analysis.md)

## Known variations

The observed employee had model sections with percentile or range values and one section with insufficient data.

## Unknowns and untested behavior

Formulas, source governance, statistical definitions, model weights, refresh timing, retry, explainability, approval, overrides, and configuration changes.

## Sources

- Owner-accepted `WT-2026-008`: E-003 and E-004; recorded 2026-08-09 and treated as reviewed 2026-08-11
