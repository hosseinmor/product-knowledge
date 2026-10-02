#!/usr/bin/env python3
"""Validate machine-readable content context contracts and eval cases."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONTEXT_DIR = ROOT / "shared" / "content" / "contexts"
EVAL_DIR = ROOT / "shared" / "content" / "evals"
TERMINOLOGY_PATH = ROOT / "shared" / "content" / "terminology" / "terms.yml"
CASE_ID_RE = re.compile(r"^[a-z][a-z0-9_]*$")
VALID_OBLIGATIONS = {"must", "must_not", "should"}

CONTEXT_SPECS = (
    {
        "name": "jobvision-candidate",
        "label": "JobVision Candidate context",
        "source_path": CONTEXT_DIR / "jobvision-candidate.yml",
        "document_path": CONTEXT_DIR / "jobvision-candidate.md",
        "eval_path": EVAL_DIR / "jobvision-candidate-context-cases.yml",
        "context_id": "content.context.jobvision-candidate",
        "eval_id": "content.eval.jobvision_candidate_context_cases",
        "product": "jobvision.candidate",
        "audience": "jobseeker",
        "rule_prefix": "JVC",
        "evaluation_source": "../evals/jobvision-candidate-context-cases.yml",
        "required_models": (
            "depends_on",
            "source_boundaries",
            "audience_model",
            "voice_model",
            "terminology_model",
            "product_area_routing",
            "claim_model",
        ),
    },
)


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys."""


def construct_unique_mapping(
    loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False
) -> dict[Any, Any]:
    loader.flatten_mapping(node)
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_unique_mapping,
)


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def duplicate_values(values: list[str]) -> list[str]:
    return sorted(value for value, count in Counter(values).items() if count > 1)


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        loaded = yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
    except FileNotFoundError:
        raise SystemExit(f"ERROR missing content context source: {path}")
    except yaml.YAMLError as exc:
        raise SystemExit(f"ERROR invalid YAML in {path}: {exc}") from exc
    if not isinstance(loaded, dict):
        raise SystemExit(f"ERROR {path} must contain a YAML mapping")
    return loaded


def validate_registered_inventory() -> list[str]:
    errors: list[str] = []
    expected_sources = {spec["source_path"].name for spec in CONTEXT_SPECS}
    actual_sources = {
        path.name for path in CONTEXT_DIR.glob("*.yml") if path.is_file()
    }
    expected_docs = {
        spec["document_path"].name for spec in CONTEXT_SPECS
    } | {"README.md"}
    actual_docs = {path.name for path in CONTEXT_DIR.glob("*.md") if path.is_file()}
    for label, expected, actual in (
        ("context source", expected_sources, actual_sources),
        ("context document", expected_docs, actual_docs),
    ):
        missing = sorted(expected - actual)
        unregistered = sorted(actual - expected)
        if missing:
            errors.append(f"missing registered {label}s: {', '.join(missing)}")
        if unregistered:
            errors.append(f"unregistered {label}s: {', '.join(unregistered)}")
    return errors


def validate_context(
    data: dict[str, Any], spec: dict[str, Any], known_term_ids: set[str]
) -> tuple[list[str], dict[str, str]]:
    label = spec["label"]
    errors: list[str] = []
    for field in (
        "schema_version",
        "id",
        "document_id",
        "title",
        "status",
        "language",
        "product",
        "audience",
        "evaluation_source",
    ):
        if not nonempty_string(data.get(field)):
            errors.append(f"{label}: `{field}` must be a non-empty string")
    if data.get("id") != spec["context_id"]:
        errors.append(f"{label}: `id` must be `{spec['context_id']}`")
    if data.get("document_id") != spec["context_id"]:
        errors.append(f"{label}: `document_id` must match the context id")
    if data.get("product") != spec["product"]:
        errors.append(f"{label}: `product` must be `{spec['product']}`")
    if data.get("audience") != spec["audience"]:
        errors.append(f"{label}: `audience` must be `{spec['audience']}`")
    if data.get("evaluation_source") != spec["evaluation_source"]:
        errors.append(
            f"{label}: `evaluation_source` must be "
            f"`{spec['evaluation_source']}`"
        )

    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append(f"{label}: `sources` must be a non-empty list")
        sources = []
    source_ids: list[str] = []
    for index, source in enumerate(sources):
        location = f"{label}.sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{location} must be a mapping")
            continue
        source_id = source.get("id")
        if not nonempty_string(source_id):
            errors.append(f"{location}.id must be a non-empty string")
        else:
            source_ids.append(source_id)
    duplicate_sources = duplicate_values(source_ids)
    if duplicate_sources:
        errors.append(f"{label}: duplicate source ids: {', '.join(duplicate_sources)}")
    known_sources = set(source_ids)

    term_decisions = data.get("term_decisions")
    if not isinstance(term_decisions, list) or not term_decisions:
        errors.append(f"{label}: `term_decisions` must be a non-empty list")
        term_decisions = []
    concept_ids: list[str] = []
    for index, decision in enumerate(term_decisions):
        location = f"{label}.term_decisions[{index}]"
        if not isinstance(decision, dict):
            errors.append(f"{location} must be a mapping")
            continue
        concept_id = decision.get("concept_id")
        if not nonempty_string(concept_id):
            errors.append(f"{location}.concept_id must be a non-empty string")
        else:
            concept_ids.append(concept_id)
            location = concept_id
            if concept_id not in known_term_ids:
                errors.append(f"{location}: unknown terminology concept id")
        preferred = decision.get("preferred")
        if not isinstance(preferred, dict) or not preferred:
            errors.append(f"{location}: preferred must be a non-empty mapping")
        elif not all(
            nonempty_string(key) and nonempty_string(value)
            for key, value in preferred.items()
        ):
            errors.append(f"{location}: preferred must map non-empty labels")
    duplicate_concepts = duplicate_values(concept_ids)
    if duplicate_concepts:
        errors.append(
            f"{label}: duplicate term decision concept ids: "
            + ", ".join(duplicate_concepts)
        )

    rules = data.get("rules")
    if not isinstance(rules, list) or not rules:
        errors.append(f"{label}: `rules` must be a non-empty list")
        rules = []
    rule_pattern = re.compile(rf"^{re.escape(spec['rule_prefix'])}-[0-9]{{3}}$")
    rule_ids: list[str] = []
    rule_keys: list[str] = []
    obligations: dict[str, str] = {}
    for index, rule in enumerate(rules):
        location = f"{label}.rules[{index}]"
        if not isinstance(rule, dict):
            errors.append(f"{location} must be a mapping")
            continue
        rule_id = rule.get("id")
        if not nonempty_string(rule_id) or not rule_pattern.fullmatch(rule_id):
            errors.append(f"{location}.id must match {spec['rule_prefix']}-000")
        else:
            rule_ids.append(rule_id)
            location = rule_id
        rule_key = rule.get("key")
        if not nonempty_string(rule_key):
            errors.append(f"{location}: missing non-empty `key`")
        else:
            rule_keys.append(rule_key)
        obligation = rule.get("obligation")
        if obligation not in VALID_OBLIGATIONS:
            errors.append(
                f"{location}: obligation must be one of "
                f"{sorted(VALID_OBLIGATIONS)}"
            )
        elif nonempty_string(rule_id) and rule_pattern.fullmatch(rule_id):
            obligations[rule_id] = obligation
        if not nonempty_string(rule.get("statement")):
            errors.append(f"{location}: missing non-empty `statement`")
        evidence = rule.get("evidence")
        if not isinstance(evidence, list) or not evidence:
            errors.append(f"{location}: evidence must be a non-empty list")
        elif not all(nonempty_string(source_id) for source_id in evidence):
            errors.append(f"{location}: evidence must contain only source ids")
        else:
            unknown = sorted(set(evidence) - known_sources)
            if unknown:
                errors.append(
                    f"{location}: unknown evidence source ids: {', '.join(unknown)}"
                )

    duplicate_rules = duplicate_values(rule_ids)
    if duplicate_rules:
        errors.append(f"{label}: duplicate rule ids: {', '.join(duplicate_rules)}")
    duplicate_keys = duplicate_values(rule_keys)
    if duplicate_keys:
        errors.append(f"{label}: duplicate rule keys: {', '.join(duplicate_keys)}")

    for field in spec["required_models"]:
        if not isinstance(data.get(field), dict) or not data[field]:
            errors.append(f"{label}: `{field}` must be a non-empty mapping")
    if not isinstance(data.get("unknowns"), list) or not data["unknowns"]:
        errors.append(f"{label}: `unknowns` must be a non-empty list")
    return errors, obligations


def validate_evals(
    data: dict[str, Any], obligations: dict[str, str], spec: dict[str, Any]
) -> list[str]:
    label = f"{spec['name']} evals"
    errors: list[str] = []
    for field in ("schema_version", "id", "context_id", "language"):
        if not nonempty_string(data.get(field)):
            errors.append(f"{label}: `{field}` must be a non-empty string")
    if data.get("id") != spec["eval_id"]:
        errors.append(f"{label}: `id` must be `{spec['eval_id']}`")
    if data.get("context_id") != spec["context_id"]:
        errors.append(f"{label}: `context_id` must match the context id")

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + [f"{label}: `cases` must be a non-empty list"]

    case_ids: list[str] = []
    covered: set[str] = set()
    known_rules = set(obligations)
    has_valid = False
    has_invalid = False
    for index, case in enumerate(cases):
        location = f"{label}.cases[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{location} must be a mapping")
            continue
        case_id = case.get("id")
        if not nonempty_string(case_id) or not CASE_ID_RE.fullmatch(case_id):
            errors.append(f"{location}.id must use snake_case")
        else:
            case_ids.append(case_id)
            location = case_id
        if not isinstance(case.get("context"), dict) or not case["context"]:
            errors.append(f"{location}: context must be a non-empty mapping")
        if not isinstance(case.get("content"), dict) or not case["content"]:
            errors.append(f"{location}: content must be a non-empty mapping")

        expected = case.get("expected")
        if not isinstance(expected, dict) or not isinstance(
            expected.get("valid"), bool
        ):
            errors.append(f"{location}: expected.valid must be a boolean")
            continue
        checked = expected.get("checked_rules")
        violations = expected.get("violations")
        if not isinstance(checked, list) or not checked:
            errors.append(f"{location}: checked_rules must be a non-empty list")
            checked = []
        elif not all(nonempty_string(rule_id) for rule_id in checked):
            errors.append(f"{location}: checked_rules must contain only rule ids")
            checked = [rule_id for rule_id in checked if nonempty_string(rule_id)]
        if not isinstance(violations, list):
            errors.append(f"{location}: violations must be a list")
            violations = []
        elif not all(nonempty_string(rule_id) for rule_id in violations):
            errors.append(f"{location}: violations must contain only rule ids")
            violations = [
                rule_id for rule_id in violations if nonempty_string(rule_id)
            ]
        duplicate_checked = duplicate_values(checked)
        if duplicate_checked:
            errors.append(
                f"{location}: duplicate checked rule ids: "
                + ", ".join(duplicate_checked)
            )
        duplicate_violations = duplicate_values(violations)
        if duplicate_violations:
            errors.append(
                f"{location}: duplicate violation ids: "
                + ", ".join(duplicate_violations)
            )
        unknown = sorted((set(checked) | set(violations)) - known_rules)
        if unknown:
            errors.append(f"{location}: unknown rule ids: {', '.join(unknown)}")
        if not set(violations).issubset(set(checked)):
            errors.append(f"{location}: violations must be included in checked_rules")
        if expected["valid"]:
            has_valid = True
            if violations:
                errors.append(f"{location}: valid case cannot declare violations")
        else:
            has_invalid = True
            if not violations:
                errors.append(
                    f"{location}: invalid case requires at least one violation"
                )
        covered.update(checked)

    duplicate_cases = duplicate_values(case_ids)
    if duplicate_cases:
        errors.append(f"{label}: duplicate case ids: {', '.join(duplicate_cases)}")
    if not has_valid or not has_invalid:
        errors.append(f"{label}: include at least one valid and one invalid case")
    blocking_rules = {
        rule_id
        for rule_id, obligation in obligations.items()
        if obligation in {"must", "must_not"}
    }
    missing_coverage = sorted(blocking_rules - covered)
    if missing_coverage:
        errors.append(
            f"{label}: blocking rules without coverage: "
            + ", ".join(missing_coverage)
        )
    return errors


def main() -> int:
    errors = validate_registered_inventory()
    terminology = load_yaml(TERMINOLOGY_PATH)
    terms = terminology.get("terms")
    if not isinstance(terms, list) or not terms:
        print("ERROR terminology: `terms` must be a non-empty list")
        return 1
    known_term_ids = {
        term.get("id")
        for term in terms
        if isinstance(term, dict) and nonempty_string(term.get("id"))
    }
    summaries: list[str] = []
    for spec in CONTEXT_SPECS:
        context = load_yaml(spec["source_path"])
        evals = load_yaml(spec["eval_path"])
        context_errors, obligations = validate_context(context, spec, known_term_ids)
        errors.extend(context_errors)
        errors.extend(validate_evals(evals, obligations, spec))
        summaries.append(
            f"{spec['name']}={len(obligations)} rules/"
            f"{len(evals.get('cases', []))} cases"
        )
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print(
        "Content context contracts are valid: "
        f"{len(CONTEXT_SPECS)} contexts; " + ", ".join(summaries)
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
