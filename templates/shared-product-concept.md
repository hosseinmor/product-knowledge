---
id: shared.concept-id
kind: shared-product-concept
title: Product Concept name
summary: One-sentence description used by AI to decide when this Product Concept is relevant.
status: draft
owner:
last_reviewed:
related: []
topics: []
---

# {Product Concept name}

## Definition

Define what this Concept is in business/product terms. Do not describe one Product Area's behavior with it.

## Boundaries

### Includes

### Does Not Include

Use boundaries to prevent neighboring Concepts from being conflated.

## Business Meaning

Explain why the Concept matters in the product/domain and what role it plays across Areas.

## Attributes

Include the business/product-meaningful attributes needed to understand the Concept. Do not limit this section to only a few "key" fields when other attributes materially define the Concept.

Exclude implementation-only database IDs, cache keys, serialization fields, and other technical properties unless they have direct product meaning.

| Attribute | Meaning | Values / Notes |
| --- | --- | --- |
|  |  |  |

Attribute existence and meaning belong here. Context-dependent requiredness, validation, or editability belongs in the relevant Product Area.

## Relationships

Document semantic business relationships and cardinality when meaningful.

Examples:

- Application belongs to Candidate
- Application is for Job Post

Do not turn this into a technical ERD.

## Business Rules

Document intrinsic, context-independent rules of the Concept.

Rules that only apply in a specific Flow or Product Area belong in that Area and should not be duplicated here.

## States & Lifecycle

When the Concept has a business lifecycle, define canonical States, their business meaning, and the main lifecycle or transition model here.

Do not add UI states. Do not invent States when the canonical model is unknown.

## Types / Variations

Use only for business-semantic variants that have distinct meaning, rules, or behavior.

If a difference is simply a value of an Attribute, keep it under `Attributes` instead of creating a separate Type.

## Used In Product Areas (AI-maintained)

Derive this section from Product Areas that reference the Concept in `Main Concepts`. The owner should not need to maintain this list manually.

## Terminology / Aliases

List important alternative names, legacy terms, or product-facing labels that could otherwise create ambiguity.

## Unknowns & Unverified Behavior

Do not guess missing attributes, relationships, rules, lifecycle, or variants.

### {Unknown}

**What is unclear?**  

**Why is it unverified?**  

**How can it be verified?**  

## Sources & Evidence

List material sources used to define or verify this Concept and make source authority clear when useful.
