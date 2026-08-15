---
id: group-id.product-id.area-id
kind: product-area
group: group-id
product: product-id
title: Product Area name
summary: One-sentence description used by AI to decide when this Product Area is relevant.
status: draft
owner:
last_reviewed:
related:
  - group-id.product-id.overview
topics: []
---

# {Product Area name}

## Overview

Describe what meaningful product capability, outcome, or business process this Area covers. Do not turn this section into a Flow transcript.

## Boundaries

Boundaries should be consistent with the full documented behavior. AI may derive them after understanding the Area, even though they appear near the beginning for readers.

### Includes

### Does Not Include

## Why This Area Exists

Describe the durable user or business value of this Area, not the history of one initiative.

## Users & Roles

List the main Actors and contextual Roles involved in this Area.

Do not model user states such as Anonymous / Logged-in or Plans / Segments such as Pro / Premium as Roles. Put their behavioral differences in Flow, Permissions, Business Rules, or Known Variations.

## User Outcomes

## Entry Points

Use:

```text
[Surface] → [Action]
```

An Entry Point is the last surface outside the Area plus the action that enters Area behavior. Do not document the whole upstream journey. Multiple Entry Points may lead to the same Flow.

## Main Concepts

List the Concepts needed to understand this Area. Reference canonical Product Concepts when available. Do not redefine a Concept inside the Area.

Use `[Candidate Concept]` when an important Concept appears to need a canonical definition but does not yet have one.

# Product Behavior

## Main Flows

Describe behavior, not screens. Differentiate Flows by behavior rather than by the upstream journey that led to the same behavior.

### {Flow name}

**Goal**  

**Trigger**  

**Preconditions**

- 

**Steps**

1. 
2. 
3. 

**Outcome**  

### Alternate / Conditional Flow — {Condition}

Use for a valid conditional path that can still reach the same Goal. Keep failures in `Error & Recovery`.

## Business Rules

Use for rules that govern behavior in this Area.

Context-independent intrinsic rules of a Product Concept belong in that Concept and should not be duplicated here.

```text
BR-01 — [Rule]
```

- **BR-01** —

### Data Behavior

Use only when product-meaningful data behavior matters, such as persistence, reuse, prefill, synchronization, or retention. Do not document database or API implementation details.

## Permissions

Use:

```text
[Action] → [Allowed Role / Permission / Eligibility]
```

## Relevant State Transitions

Document only business transitions created, used, or controlled by this Area. Canonical State definitions and the full lifecycle belong in the Product Concept.

```text
[State A] → [State B]
Trigger: [Event / Action / Condition]
```

A creation event is not automatically a State Transition. If the initial State is unknown, keep it in `Unknowns & Unverified Behavior` rather than guessing.

## Validation

Document conditions required for an input or action to be valid. Do not describe UI error presentation here.

## Error & Recovery

### {Failure / Error}

**Behavior:**  

**Recovery:**  

Use this section when an operation fails or the normal path cannot continue.

## Edge Cases

Record real, known, unusual domain conditions whose behavior is defined.

Do not classify normal alternate branches, validation conditions, or ordinary retry behavior as Edge Cases. Do not generate hypothetical Edge Cases merely to fill the section.

### {Edge Case}

**Behavior:**  

## Known Variations

Use only when base behavior differs because of a relatively stable context such as Plan, Platform, Location, User Segment, Role, or Organization Type.

Temporary Flow conditions such as incomplete data, authentication checks, or validation failures are not Known Variations.

| Dimension | Context | Variation |
| --- | --- | --- |
|  |  |  |

# Knowledge & References

## Related Knowledge

List Product Areas, Product Concepts, or Services that materially help readers navigate adjacent knowledge.

Do not duplicate semantic relationships between Concepts here; those belong in the Product Concept.

## Unknowns & Unverified Behavior

Do not guess when current behavior is unclear.

### {Unknown}

**What is unclear?**  

**Why is it unverified?**  

**How can it be verified?**  

## Sources & Evidence

List material sources used to write or verify this Area and make source authority clear when useful.

- Production / Walkthrough:
- Figma:
- Existing documentation:
- Jira / PRD:
- Other:
