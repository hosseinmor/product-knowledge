#!/usr/bin/env python3
"""Validate machine-readable content component contracts and eval cases."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
COMPONENT_DIR = ROOT / "shared" / "content" / "components"
EVAL_DIR = ROOT / "shared" / "content" / "evals"
BUTTON_PATH = COMPONENT_DIR / "button.yml"
BUTTON_DOC_PATH = COMPONENT_DIR / "button.md"
BUTTON_EVAL_PATH = EVAL_DIR / "button-content-cases.yml"
COMPONENT_PATHS = (BUTTON_PATH,)
COMPONENT_DOC_PATHS = (BUTTON_DOC_PATH,)
EVAL_PATHS = (BUTTON_EVAL_PATH,)
RULE_ID_RE = re.compile(r"^BTN-[0-9]{3}$")
CASE_ID_RE = re.compile(r"^[a-z][a-z0-9_]*$")
VALID_OBLIGATIONS = {"must", "must_not", "should"}


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
        raise SystemExit(f"ERROR missing content component source: {path}")
    except yaml.YAMLError as exc:
        raise SystemExit(f"ERROR invalid YAML in {path}: {exc}") from exc
    if not isinstance(loaded, dict):
        raise SystemExit(f"ERROR {path} must contain a YAML mapping")
    return loaded


def validate_registered_inventory() -> list[str]:
    errors: list[str] = []
    expected_sources = {path.name for path in COMPONENT_PATHS}
    actual_sources = {
        path.name for path in COMPONENT_DIR.glob("*.yml") if path.is_file()
    }
    expected_docs = {path.name for path in COMPONENT_DOC_PATHS} | {"README.md"}
    actual_docs = {
        path.name for path in COMPONENT_DIR.glob("*.md") if path.is_file()
    }
    for label, expected, actual in (
        ("component source", expected_sources, actual_sources),
        ("component document", expected_docs, actual_docs),
    ):
        missing = sorted(expected - actual)
        unregistered = sorted(actual - expected)
        if missing:
            errors.append(f"missing registered {label}s: {', '.join(missing)}")
        if unregistered:
            errors.append(f"unregistered {label}s: {', '.join(unregistered)}")
    return errors


def validate_component(data: dict[str, Any]) -> tuple[list[str], dict[str, str]]:
    errors: list[str] = []
    for field in (
        "schema_version",
        "id",
        "title",
        "status",
        "language",
        "goal",
        "tone_profile",
        "evaluation_source",
    ):
        if not nonempty_string(data.get(field)):
            errors.append(f"button component: `{field}` must be a non-empty string")
    if data.get("id") != "content.component.button":
        errors.append("button component: `id` must be `content.component.button`")
    if data.get("tone_profile") != "button_or_menu_label":
        errors.append(
            "button component: `tone_profile` must be `button_or_menu_label`"
        )
    if data.get("evaluation_source") != "../evals/button-content-cases.yml":
        errors.append(
            "button component: `evaluation_source` must be "
            "`../evals/button-content-cases.yml`"
        )

    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("button component: `sources` must be a non-empty list")
        sources = []
    source_ids: list[str] = []
    for index, source in enumerate(sources):
        location = f"button component.sources[{index}]"
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
        errors.append(
            "button component: duplicate source ids: "
            + ", ".join(duplicate_sources)
        )
    known_sources = set(source_ids)

    rules = data.get("rules")
    if not isinstance(rules, list) or not rules:
        errors.append("button component: `rules` must be a non-empty list")
        rules = []
    rule_ids: list[str] = []
    rule_keys: list[str] = []
    obligations: dict[str, str] = {}
    for index, rule in enumerate(rules):
        location = f"button component.rules[{index}]"
        if not isinstance(rule, dict):
            errors.append(f"{location} must be a mapping")
            continue
        rule_id = rule.get("id")
        if not nonempty_string(rule_id) or not RULE_ID_RE.fullmatch(rule_id):
            errors.append(f"{location}.id must match BTN-000")
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
        elif nonempty_string(rule_id) and RULE_ID_RE.fullmatch(rule_id):
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
        errors.append(
            "button component: duplicate rule ids: " + ", ".join(duplicate_rules)
        )
    duplicate_keys = duplicate_values(rule_keys)
    if duplicate_keys:
        errors.append(
            "button component: duplicate rule keys: " + ", ".join(duplicate_keys)
        )

    for field in (
        "depends_on",
        "source_boundaries",
        "label_model",
        "component_selection",
        "state_model",
    ):
        if not isinstance(data.get(field), dict) or not data[field]:
            errors.append(f"button component: `{field}` must be a non-empty mapping")
    if not isinstance(data.get("unknowns"), list) or not data["unknowns"]:
        errors.append("button component: `unknowns` must be a non-empty list")
    return errors, obligations


def validate_evals(
    data: dict[str, Any], obligations: dict[str, str]
) -> list[str]:
    errors: list[str] = []
    for field in ("schema_version", "id", "component_id", "language"):
        if not nonempty_string(data.get(field)):
            errors.append(f"button evals: `{field}` must be a non-empty string")
    if data.get("id") != "content.eval.button_content_cases":
        errors.append(
            "button evals: `id` must be `content.eval.button_content_cases`"
        )
    if data.get("component_id") != "content.component.button":
        errors.append("button evals: `component_id` must match the component id")

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + ["button evals: `cases` must be a non-empty list"]

    case_ids: list[str] = []
    covered: set[str] = set()
    known_rules = set(obligations)
    has_valid = False
    has_invalid = False

    for index, case in enumerate(cases):
        location = f"button evals.cases[{index}]"
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
        errors.append(
            "button evals: duplicate case ids: " + ", ".join(duplicate_cases)
        )
    if not has_valid or not has_invalid:
        errors.append("button evals: include at least one valid and one invalid case")
    blocking_rules = {
        rule_id
        for rule_id, obligation in obligations.items()
        if obligation in {"must", "must_not"}
    }
    missing_coverage = sorted(blocking_rules - covered)
    if missing_coverage:
        errors.append(
            "button evals: blocking rules without coverage: "
            + ", ".join(missing_coverage)
        )
    return errors


def main() -> int:
    errors = validate_registered_inventory()
    button = load_yaml(BUTTON_PATH)
    evals = load_yaml(BUTTON_EVAL_PATH)
    component_errors, obligations = validate_component(button)
    errors.extend(component_errors)
    errors.extend(validate_evals(evals, obligations))
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print(
        "Content component contracts are valid: "
        f"1 component, {len(button['sources'])} sources, "
        f"{len(obligations)} rules, {len(evals['cases'])} eval cases"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
