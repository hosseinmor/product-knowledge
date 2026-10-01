---
id: shared.ai-services.overview
kind: shared-product-service-overview
title: AI Product Services
summary: Overview of shared AI-powered product services used across Jobvision and Cando products.
status: draft
owner: AI product team
last_reviewed: 2026-09-23
related:
  - jobvision.overview
  - cando.overview
  - jobvision.candidate.resume-management
topics:
  - ai
  - machine-learning
  - fit-models
  - matching
  - cross-product-service
---

# AI Product Services

## What this service group is

The AI product team develops product services that can support several Jobvision and Cando products.

The team itself is not a product in the Product Knowledge hierarchy. Team structures may change; the durable knowledge unit is the AI-powered service and the product behavior it enables.

## Placement rule

```text
AI service used by several products
→ shared/product-services/ai/services/

AI behavior specific to one product
→ the relevant product's Product Area

Reusable UI behavior for AI interactions
→ shared/design-system/
```

A product-specific document may name the AI product team as owner or dependency without moving that behavior out of the product.

## Known service candidates

- Fit and matching models
- Scoring and ranking services
- AI-assisted generation or analysis
- Shared intelligence used by several product experiences

Only fit models have been explicitly named as an example so far. Other services should be added as separate documents when their consumers, inputs, outputs, behavior, limitations, and owner are known.

## Product-language map

| Concept | Meaning | Current evidence boundary |
|---|---|---|
| AI technology | The underlying technology or model use | Does not name a product experience |
| AI feature family | A family of AI-assisted capabilities | Does not imply an assistant persona |
| AI assistant | An interaction archetype with independent assistant-like behavior | Use only when the experience behaves like an assistant |
| Resume AI assistant | Candidate-specific experience for AI resume evaluation and improvement | Observed in the current Candidate resume UI |
| Employer assistant | Reminder and automatic-rejection automation for undecided applications | AI use is not established by the name alone |
| External AI screener | Internal external-tool integration associated with rejection screening | Product name and active status remain unverified |

These concepts must not be collapsed into one global assistant. Product-specific
experiences stay in their owning Product Areas; a shared AI service should be
documented only when its consumers, inputs, outputs, limitations, and fallback
behavior are known.

## How products should reference a service

A Product Area should document:

- Why the service is used in that product
- What user-facing behavior depends on it
- What happens when the service is unavailable or uncertain
- Product-specific thresholds, presentation, permissions, and fallback behavior

The shared service document should document:

- Shared purpose
- Products that consume it
- Inputs and outputs
- Shared behavior and limitations
- Quality, confidence, and fallback considerations
- Ownership and dependencies

## Documentation gaps

- Complete inventory of AI product services
- Service owners and consumers
- Shared versus product-specific rules
- Model inputs, outputs, confidence, fallback, and failure behavior
- Privacy, explainability, evaluation, and monitoring expectations

## Sources

Add Jira, technical references, model documentation, evaluation reports, product designs, and owner-reviewed explanations as services are documented.
