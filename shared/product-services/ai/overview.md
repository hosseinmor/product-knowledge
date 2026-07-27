---
id: shared.ai-services.overview
kind: shared-product-service-overview
title: AI Product Services
summary: Overview of shared AI-powered product services used across Jobvision and Kando products.
status: draft
owner: AI product team
last_reviewed:
related:
  - jobvision.overview
  - kando.overview
topics:
  - ai
  - machine-learning
  - fit-models
  - matching
  - cross-product-service
---

# AI Product Services

## What this service group is

The AI product team develops product services that can support several Jobvision and Kando products.

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
