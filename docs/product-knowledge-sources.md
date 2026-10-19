# Product Knowledge source authority

This repository is not the canonical Product Knowledge store. It contains the
Product Content System, Design System knowledge, reusable product standards,
and AI workflows that consume product truth from the approved source.

The machine-readable contract is
[`product-knowledge-sources.yml`](../product-knowledge-sources.yml).

## JobVision

Canonical Product Knowledge lives at:

<https://docs-jv.jvoffice.ir/>

The site requires the company's internal VPN and a browser session. Start from
its product map and load only the relevant domains. The site's glossary,
open-question index, and technical-debt index are part of the same knowledge
surface.

If the site is inaccessible, stop product-claim work or ask the user for the
relevant source material. Do not substitute deleted repository documents,
memory, Figma, screenshots, or observed UI.

## Cando

Canonical Product Knowledge lives at:

<https://docs-cd.jvoffice.ir/>

Use that site for established Cando product meaning and current behavior. Access
to the internal source must be verified in the current execution environment
before relying on it.

If the site is inaccessible or does not establish a material claim, preserve the
limitation or uncertainty explicitly. Reviewed walkthrough evidence, direct
observation, implementation evidence, approved decisions, and explicit owner
input may still support bounded investigation, but they do not silently replace
canonical Cando Product Knowledge. Do not use JobVision Product Knowledge,
Content Contexts, Figma, screenshots, or observed UI as a canonical fallback
for Cando.

## Repository boundary

Active Product Knowledge must not be stored under the following paths:

```text
products/
shared/product-concepts/
shared/product-services/
```

Historical files remain recoverable through Git history and archive refs. Do
not restore them to `main` as a fallback or place them in an indexed `legacy/`
directory.

## Claim handling

Keep these states separate in every workflow:

```text
canonical Product Knowledge
→ approved product decision
→ reviewed evidence
→ observed UI or design
→ hypothesis
→ recommendation
```

Only the first two can establish current product behavior. Reviewed evidence
can support a decision but does not silently become canonical truth. Missing
knowledge stays visible as an unknown or blocking question.
