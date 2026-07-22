# Semantic Tokens

> Status: draft

Semantic tokens define stable interface roles. Their meaning does not change when the active Experience mode changes.

## Experience Resolution

Semantic tokens are resolved through the active Experience mode before they are consumed by components:

```text
semantic role
+ Productive or Expressive mode
+ optional product override
= resolved component value
```

A mode may change an approved reference or visual expression, but it must not change the role's meaning. Productive and Expressive therefore share the same semantic families and state model.

Mode is not included in the semantic token name. Do not duplicate the semantic catalog into `productive-*` and `expressive-*` token families.

See `architecture.md` for mode definitions and selection rules.

## Surface

## Foreground

## Line

## Fill

## Support

Support meaning is invariant across Experience modes. Success, warning, error, and information must not be restyled in a way that changes or weakens their meaning.

## Tag

## Focus

Focus must remain clearly visible and meet the same accessibility requirements in Productive and Expressive modes.
