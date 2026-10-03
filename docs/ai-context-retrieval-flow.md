# AI Context Retrieval Flow

## Source gate

```text
AGENTS.md
→ product-knowledge-sources.yml
→ identify product and requested outcome
```

### JobVision

```text
Open https://docs-jv.jvoffice.ir/ through VPN and browser
→ start from the product map
→ load the smallest relevant domains
→ record the source URLs
→ load relevant repository-owned Content and Design System guidance
```

### Cando

```text
No canonical source
→ label explicit owner input / reviewed evidence / approved decisions
→ preserve missing behavior as unknown
→ do not create repository Product Knowledge
```

## Repository retrieval

`manifest.generated.json` indexes only repository-owned guidance:

```text
shared/content/
shared/design-system/
shared/product-standards/
```

The manifest is not a Product Knowledge index. Use it only after product truth
has been sourced or its absence has been disclosed.

## PRD, design, research, and content work

```text
canonical Product Knowledge or explicit authorised input
+ approved product decisions
+ relevant repository guidance selected through the manifest
→ synthesize context
→ expose contradictions and unknowns
→ ask only blocking questions
→ produce the requested artifact
```

Every output keeps these layers separate:

```text
canonical truth
approved decision
reviewed evidence
observed UI or design
hypothesis
recommendation
unknown
```

Figma, screenshots, runtime UI, and walkthroughs can provide evidence but do
not silently establish product policy, lifecycle, permission, validation, or
consequence.
