---
id: design-system.governance.ownership
collection: design-system
type: governance
title: Ownership
summary: Defines ownership and review responsibility for shared Design System knowledge, including the accessibility corpus.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: '2026-09-03'
related:
- design-system.governance.documentation-maintenance
- design-system.governance.change-process
- design-system.accessibility.conformance-and-policy
---

# Ownership

## Purpose

Keep canonical Design System knowledge reviewable and maintainable without tying repository structure to team structure.

## Roles

### Design System team

The Design System team is the canonical owner of shared Design System foundations, tokens, components, patterns, governance, and accessibility guidance unless a document explicitly names another owner.

For the operational accessibility corpus, the Design System team owns standards interpretation, cross-document consistency, routing integrity, and approval of canonical changes.

### Product and feature owners

Product teams own product-specific composition, flow policy, business rules, copy, and implementation decisions that use the Design System. A product flow such as Apply + Screening Questions requires a Product/Pattern owner; specialized accessibility documents do not become the owner of product-specific behavior.

### Contributors and reviewers

Designers, engineers, QA, AI agents, and accessibility reviewers may propose changes and evidence. Canonical approval remains with the named owner.

## Process

- Canonical/reviewed Design System documents **SHOULD** identify an owner.
- The 18 operational documents in `shared/design-system/accessibility/` **MUST** identify `Design System team` as owner unless ownership is explicitly reassigned.
- Changing an owner is a governance change and requires owner review through a branch and pull request.
- An absent owner does not make a document invalid for retrieval, but it is a maintenance gap that must be resolved before the document is treated as operationally complete.

## Review Requirements

Owner review is required when a change:
- changes normative Design System behavior;
- changes accessibility requirement levels or standards interpretation;
- changes component/pattern maturity used by AI retrieval;
- changes routing, ownership, deprecation, or release policy.

## Definition of Done

A canonical Design System knowledge change is ownership-ready when:
- the owning document is clear;
- the owner field is populated where required;
- unresolved decisions remain explicit;
- repository validation passes;
- required domain-specific regression gates pass.
