---
id: design-system.governance.documentation-maintenance
collection: design-system
type: governance
title: Documentation Maintenance
summary: Defines Design System documentation trust and maturity metadata.
knowledge_state: canonical
document_maturity: draft
related: []
---

# Documentation Maintenance

## Purpose

Design System documents use separate metadata for **trust** and **completeness**. These dimensions must not be collapsed into one status.

A document may contain owner-reviewed, canonical guidance while still being structurally incomplete. Conversely, a well-filled document may still contain unverified claims.

## Trust: `knowledge_state`

`knowledge_state` describes the authority of the claims that are currently present in the document.

Current Design System convention:

```text
unverified
→ the present claims have not yet been owner-reviewed as current shared guidance

canonical
→ the present claims/rules have been owner-reviewed and are the current shared guidance
```

`canonical` does **not** mean that every possible section is complete, every implementation value is finalized, or every explicit Open Question/TBD is resolved. Explicit gaps remain gaps.

A phrase such as “canonical source” or “canonical owner” describes **documentation ownership/source-of-truth location**, not automatically the document's `knowledge_state`. A document can be the designated owner of a topic while its current contents are still draft or unverified.

## Completeness: `document_maturity`

`document_maturity` describes how complete the document is for its intended scope.

Current Design System convention:

```text
scaffold
→ structure or partial evidence only; major component/pattern sections are still missing

draft
→ substantive guidance exists, but meaningful parts of the contract remain incomplete or open

reviewed / stable
→ use only when the document has passed the corresponding Design System review and is complete enough for its declared scope
```

Trust and maturity are independent. For example:

```text
knowledge_state: canonical
document_maturity: scaffold
```

means:

> The guidance that is present is owner-reviewed and authoritative for its stated scope, but the overall component/pattern specification is still incomplete.

This combination is appropriate for a component document that contains a reviewed Color mapping stress test while anatomy, sizing, keyboard behavior, or implementation details are still missing.

## Section-scoped evidence

When only one part of an incomplete document has been reviewed, make that scope explicit in the prose. Do not describe the entire component as approved merely because one mapping or architecture check was reviewed.

Preferred wording:

```text
Reviewed Color architecture evidence
Reviewed mapping direction
Owner-reviewed rule for the stated scope
```

Avoid ambiguous wording such as:

```text
Approved component
Approved specification
```

unless the whole corresponding contract has actually passed review.

## Manifest status

`manifest.generated.json` exposes a lightweight `draft` / `reviewed` retrieval status. It is a derived index field and does not replace `knowledge_state` or `document_maturity`.

Use the source document metadata and explicit scope notes when deciding how much authority to assign to a document.

## Process

1. Keep canonical claims, explicit gaps, observations, and open decisions distinguishable.
2. Update `knowledge_state` when the authority of the present claims changes.
3. Update `document_maturity` when the completeness of the document changes.
4. Do not upgrade maturity merely because one section was reviewed.
5. Do not leave owner-reviewed normative guidance labeled `unverified` when the document's present claims have been explicitly accepted.
6. Regenerate `manifest.generated.json` after indexed documentation changes.

## Review Requirements

Before setting `knowledge_state: canonical`, verify that:

- The responsible owner has reviewed the present normative claims.
- Contradictions with the current canonical owner documents have been resolved or explicitly recorded.
- Unknowns and deferred decisions remain visibly marked rather than silently filled.

Before moving a document out of `scaffold`, verify that the document has substantive coverage beyond one isolated evidence section.

## Definition of Done

Documentation is maintainable when a newcomer can tell, without oral context:

- Which document owns the topic
- Which claims are current shared guidance
- Which parts are incomplete
- Which decisions are intentionally deferred
- Which implementation details remain open
