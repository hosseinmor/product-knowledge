# Optional Product Walkthrough

## Purpose

Use a bounded walkthrough to fill gaps in a Product Area document when current behavior is missing, outdated, disputed, or poorly understood.

A walkthrough is optional. It is not required before every PRD or design task, and it does not automatically establish intended product rules.

## Use it when

- a Product Area is undocumented or too incomplete;
- PM and Design disagree about current behavior;
- AI reports important unknowns;
- an old Area is about to be redesigned;
- production appears different from the existing document.

## Scope before starting

Record:

```text
Product
Product Area
Actor or role
Account or permission level
Authentication state
Environment
Known entry points
Excluded areas
```

Do not generalize beyond this scope.

## Walkthrough steps

1. Read the existing Product Overview and Product Area.
2. Inventory pages, entry points, actions, forms, states, and gates in scope.
3. Follow important actions through their outcome.
4. Check the main path and meaningful branches such as empty, validation, cancellation, permission, and recovery.
5. Record evidence such as routes, screenshots, recordings, and visible system responses.
6. Separate:

```text
Observed
Inferred
Unknown
Blocked
Not tested
Suspected bug
```

7. Summarize suggested changes to the Product Area document.
8. Ask the Area owner to review the findings.
9. The owner manually updates the Product Area when the finding is accepted.

## Output

A lightweight walkthrough note should contain:

```text
Scope
Surfaces and entry points checked
Observed main behavior
Important branches and states
Evidence
Unknowns and untested cases
Suspected bugs
Suggested Product Knowledge updates
Reviewer notes
```

## Rules

- Do not treat every page or action as a Product Area.
- Do not treat UI text alone as proof of a business rule.
- Do not hide incomplete coverage.
- Do not update Product Knowledge automatically.
