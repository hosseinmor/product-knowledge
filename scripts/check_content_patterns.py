#!/usr/bin/env python3
"""Validate machine-readable product voice, content patterns, and evals."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
VOICE_PATH = ROOT / "shared" / "content" / "product-voice.yml"
ERROR_PATH = ROOT / "shared" / "content" / "patterns" / "errors.yml"
EVAL_PATH = ROOT / "shared" / "content" / "evals" / "error-cases.yml"
CONFIRMATION_PATH = ROOT / "shared" / "content" / "patterns" / "confirmations.yml"
CONFIRMATION_EVAL_PATH = (
    ROOT / "shared" / "content" / "evals" / "confirmation-cases.yml"
)
EMPTY_STATE_PATH = ROOT / "shared" / "content" / "patterns" / "empty-states.yml"
EMPTY_STATE_EVAL_PATH = (
    ROOT / "shared" / "content" / "evals" / "empty-state-cases.yml"
)
NOTIFICATION_PATH = ROOT / "shared" / "content" / "patterns" / "notifications.yml"
NOTIFICATION_EVAL_PATH = (
    ROOT / "shared" / "content" / "evals" / "notification-cases.yml"
)
RULE_ID_RE = re.compile(r"^(VOICE|ERR|CNF|EST|NTF)-[0-9]{3}$")
CASE_ID_RE = re.compile(r"^[a-z][a-z0-9_]*$")
VALID_OBLIGATIONS = {"must", "must_not", "should"}
TONE_DIMENSIONS = {"clarity", "warmth", "encouragement", "brand_expression"}


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"ERROR missing content source: {path}")
    except yaml.YAMLError as exc:
        raise SystemExit(f"ERROR invalid YAML in {path}: {exc}") from exc
    if not isinstance(loaded, dict):
        raise SystemExit(f"ERROR {path} must contain a YAML mapping")
    return loaded


def duplicate_values(values: list[str]) -> list[str]:
    return sorted(value for value, count in Counter(values).items() if count > 1)


def validate_rules(
    rules: Any, prefix: str, source_ids: set[str] | None = None
) -> tuple[list[str], set[str]]:
    errors: list[str] = []
    if not isinstance(rules, list) or not rules:
        return [f"{prefix}: `rules` must be a non-empty list"], set()

    rule_ids: list[str] = []
    for index, rule in enumerate(rules):
        location = f"{prefix}.rules[{index}]"
        if not isinstance(rule, dict):
            errors.append(f"{location} must be a mapping")
            continue
        rule_id = rule.get("id")
        if not nonempty_string(rule_id) or not RULE_ID_RE.fullmatch(rule_id):
            errors.append(
                f"{location}.id must match VOICE-000, ERR-000, CNF-000, EST-000, or NTF-000"
            )
        else:
            rule_ids.append(rule_id)
            location = rule_id
        if rule.get("obligation") not in VALID_OBLIGATIONS:
            errors.append(
                f"{location}: obligation must be one of {sorted(VALID_OBLIGATIONS)}"
            )
        if not nonempty_string(rule.get("statement")):
            errors.append(f"{location}: missing non-empty `statement`")
        if source_ids is not None:
            evidence = rule.get("evidence")
            if not isinstance(evidence, list) or not evidence:
                errors.append(f"{location}: evidence must be a non-empty list")
            else:
                unknown = sorted(set(evidence) - source_ids)
                if unknown:
                    errors.append(
                        f"{location}: unknown evidence source ids: {', '.join(unknown)}"
                    )

    duplicates = duplicate_values(rule_ids)
    if duplicates:
        errors.append(f"{prefix}: duplicate rule ids: {', '.join(duplicates)}")
    return errors, set(rule_ids)


def validate_voice(data: dict[str, Any]) -> tuple[list[str], set[str], set[str]]:
    errors: list[str] = []
    for field in ("schema_version", "id", "title", "language"):
        if not nonempty_string(data.get(field)):
            errors.append(f"voice: top-level `{field}` must be a non-empty string")

    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("voice: `sources` must be a non-empty list")
        sources = []
    source_ids = {
        item.get("id")
        for item in sources
        if isinstance(item, dict) and nonempty_string(item.get("id"))
    }
    if len(source_ids) != len(sources):
        errors.append("voice: every source requires a unique non-empty id")

    if not isinstance(data.get("source_derived"), dict):
        errors.append("voice: `source_derived` must be a mapping")

    model = data.get("operational_model")
    if not isinstance(model, dict):
        errors.append("voice: `operational_model` must be a mapping")
        model = {}
    dimensions = model.get("dimensions")
    if not isinstance(dimensions, dict) or set(dimensions) != TONE_DIMENSIONS:
        errors.append(
            "voice: operational dimensions must be exactly "
            + ", ".join(sorted(TONE_DIMENSIONS))
        )
        dimensions = {}

    allowed_levels: dict[str, set[str]] = {}
    for dimension in TONE_DIMENSIONS:
        definition = dimensions.get(dimension, {})
        levels = definition.get("levels") if isinstance(definition, dict) else None
        if not isinstance(levels, list) or not levels:
            errors.append(f"voice: dimension `{dimension}` requires non-empty levels")
            allowed_levels[dimension] = set()
        else:
            allowed_levels[dimension] = set(levels)

    profiles = model.get("tone_profiles")
    if not isinstance(profiles, dict) or not profiles:
        errors.append("voice: `tone_profiles` must be a non-empty mapping")
        profiles = {}
    for profile_id, profile in profiles.items():
        if not isinstance(profile, dict):
            errors.append(f"voice: tone profile `{profile_id}` must be a mapping")
            continue
        for dimension in TONE_DIMENSIONS:
            value = profile.get(dimension)
            if value not in allowed_levels.get(dimension, set()):
                errors.append(
                    f"voice: tone profile `{profile_id}` has invalid `{dimension}` level"
                )

    rule_errors, rule_ids = validate_rules(
        data.get("rules"), "voice", source_ids=source_ids
    )
    errors.extend(rule_errors)
    return errors, set(profiles), rule_ids


def validate_error_pattern(
    data: dict[str, Any], tone_profiles: set[str]
) -> tuple[list[str], dict[str, str]]:
    errors: list[str] = []
    for field in ("schema_version", "id", "title", "language", "goal"):
        if not nonempty_string(data.get(field)):
            errors.append(f"error pattern: top-level `{field}` must be a non-empty string")
    if data.get("tone_profile") not in tone_profiles:
        errors.append("error pattern: `tone_profile` must reference a known voice profile")

    rule_errors, rule_ids = validate_rules(data.get("rules"), "error pattern")
    errors.extend(rule_errors)
    obligations = {
        rule["id"]: rule["obligation"]
        for rule in data.get("rules", [])
        if isinstance(rule, dict)
        and rule.get("id") in rule_ids
        and rule.get("obligation") in VALID_OBLIGATIONS
    }

    anatomy = data.get("anatomy")
    if not isinstance(anatomy, dict) or not nonempty_string(anatomy.get("pattern")):
        errors.append("error pattern: anatomy requires a non-empty `pattern`")
    if not isinstance(data.get("placement"), dict) or not data["placement"]:
        errors.append("error pattern: `placement` must be a non-empty mapping")
    if not isinstance(data.get("templates"), dict) or not data["templates"]:
        errors.append("error pattern: `templates` must be a non-empty mapping")
    return errors, obligations


def validate_confirmation_pattern(
    data: dict[str, Any], tone_profiles: set[str]
) -> tuple[list[str], dict[str, str]]:
    errors: list[str] = []
    for field in ("schema_version", "id", "title", "language", "goal"):
        if not nonempty_string(data.get(field)):
            errors.append(
                f"confirmation pattern: top-level `{field}` must be a non-empty string"
            )
    for field in ("tone_profile", "destructive_tone_profile"):
        if data.get(field) not in tone_profiles:
            errors.append(
                f"confirmation pattern: `{field}` must reference a known voice profile"
            )

    rule_errors, rule_ids = validate_rules(
        data.get("rules"), "confirmation pattern"
    )
    errors.extend(rule_errors)
    obligations = {
        rule["id"]: rule["obligation"]
        for rule in data.get("rules", [])
        if isinstance(rule, dict)
        and rule.get("id") in rule_ids
        and rule.get("obligation") in VALID_OBLIGATIONS
    }

    anatomy = data.get("anatomy")
    if not isinstance(anatomy, dict) or not nonempty_string(
        anatomy.get("title_pattern")
    ):
        errors.append(
            "confirmation pattern: anatomy requires a non-empty `title_pattern`"
        )
    if not isinstance(data.get("decision_model"), dict) or not data["decision_model"]:
        errors.append("confirmation pattern: `decision_model` must be a non-empty mapping")
    if not isinstance(data.get("placement"), dict) or not data["placement"]:
        errors.append("confirmation pattern: `placement` must be a non-empty mapping")
    if not isinstance(data.get("templates"), dict) or not data["templates"]:
        errors.append("confirmation pattern: `templates` must be a non-empty mapping")
    return errors, obligations


def validate_empty_state_pattern(
    data: dict[str, Any], tone_profiles: set[str]
) -> tuple[list[str], dict[str, str]]:
    errors: list[str] = []
    for field in ("schema_version", "id", "title", "language", "goal"):
        if not nonempty_string(data.get(field)):
            errors.append(
                f"empty-state pattern: top-level `{field}` must be a non-empty string"
            )
    if data.get("tone_profile") not in tone_profiles:
        errors.append(
            "empty-state pattern: `tone_profile` must reference a known voice profile"
        )

    rule_errors, rule_ids = validate_rules(
        data.get("rules"), "empty-state pattern"
    )
    errors.extend(rule_errors)
    obligations = {
        rule["id"]: rule["obligation"]
        for rule in data.get("rules", [])
        if isinstance(rule, dict)
        and rule.get("id") in rule_ids
        and rule.get("obligation") in VALID_OBLIGATIONS
    }

    anatomy = data.get("anatomy")
    if not isinstance(anatomy, dict) or not nonempty_string(
        anatomy.get("message_pattern")
    ):
        errors.append(
            "empty-state pattern: anatomy requires a non-empty `message_pattern`"
        )
    if not isinstance(data.get("taxonomy"), dict) or not data["taxonomy"]:
        errors.append("empty-state pattern: `taxonomy` must be a non-empty mapping")
    if (
        not isinstance(data.get("action_selection"), dict)
        or not data["action_selection"]
    ):
        errors.append(
            "empty-state pattern: `action_selection` must be a non-empty mapping"
        )
    if not isinstance(data.get("templates"), dict) or not data["templates"]:
        errors.append("empty-state pattern: `templates` must be a non-empty mapping")
    return errors, obligations


def validate_notification_pattern(
    data: dict[str, Any], tone_profiles: set[str]
) -> tuple[list[str], dict[str, str]]:
    errors: list[str] = []
    for field in ("schema_version", "id", "title", "language", "goal"):
        if not nonempty_string(data.get(field)):
            errors.append(
                f"notification pattern: top-level `{field}` must be a non-empty string"
            )

    pattern_profiles = data.get("tone_profiles")
    if not isinstance(pattern_profiles, dict) or not pattern_profiles:
        errors.append("notification pattern: `tone_profiles` must be a non-empty mapping")
    else:
        required_severities = {"info", "success", "warning", "error"}
        if set(pattern_profiles) != required_severities:
            errors.append(
                "notification pattern: tone profiles must map exactly info, success, warning, and error"
            )
        unknown_profiles = sorted(set(pattern_profiles.values()) - tone_profiles)
        if unknown_profiles:
            errors.append(
                "notification pattern: unknown tone profiles: "
                + ", ".join(unknown_profiles)
            )

    rule_errors, rule_ids = validate_rules(
        data.get("rules"), "notification pattern"
    )
    errors.extend(rule_errors)
    obligations = {
        rule["id"]: rule["obligation"]
        for rule in data.get("rules", [])
        if isinstance(rule, dict)
        and rule.get("id") in rule_ids
        and rule.get("obligation") in VALID_OBLIGATIONS
    }

    for field in ("severity_model", "presentation_model", "action_model"):
        if not isinstance(data.get(field), dict) or not data[field]:
            errors.append(
                f"notification pattern: `{field}` must be a non-empty mapping"
            )
    anatomy = data.get("anatomy")
    if not isinstance(anatomy, dict) or not nonempty_string(
        anatomy.get("message_pattern")
    ):
        errors.append(
            "notification pattern: anatomy requires a non-empty `message_pattern`"
        )
    if not isinstance(data.get("templates"), dict) or not data["templates"]:
        errors.append("notification pattern: `templates` must be a non-empty mapping")
    return errors, obligations


def validate_evals(
    data: dict[str, Any],
    pattern_id: str,
    obligations: dict[str, str],
    eval_label: str,
) -> list[str]:
    errors: list[str] = []
    if data.get("pattern_id") != pattern_id:
        errors.append(f"{eval_label}: `pattern_id` must match the pattern id")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + [f"{eval_label}: `cases` must be a non-empty list"]

    case_ids: list[str] = []
    covered: set[str] = set()
    has_valid = False
    has_invalid = False
    known_rules = set(obligations)

    for index, case in enumerate(cases):
        location = f"{eval_label}.cases[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{location} must be a mapping")
            continue
        case_id = case.get("id")
        if not nonempty_string(case_id) or not CASE_ID_RE.fullmatch(case_id):
            errors.append(f"{location}.id must use snake_case")
        else:
            case_ids.append(case_id)
            location = case_id
        if "message" in case:
            if not isinstance(case.get("message"), str):
                errors.append(f"{location}: message must be a string")
        elif "content" in case:
            if not isinstance(case.get("content"), dict) or not case["content"]:
                errors.append(f"{location}: content must be a non-empty mapping")
        else:
            errors.append(f"{location}: requires `message` or `content`")

        expected = case.get("expected")
        if not isinstance(expected, dict) or not isinstance(expected.get("valid"), bool):
            errors.append(f"{location}: expected.valid must be a boolean")
            continue
        checked = expected.get("checked_rules")
        violations = expected.get("violations")
        if not isinstance(checked, list) or not checked:
            errors.append(f"{location}: checked_rules must be a non-empty list")
            checked = []
        if not isinstance(violations, list):
            errors.append(f"{location}: violations must be a list")
            violations = []
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
                errors.append(f"{location}: invalid case requires at least one violation")
        covered.update(checked)

    duplicates = duplicate_values(case_ids)
    if duplicates:
        errors.append(f"{eval_label}: duplicate case ids: {', '.join(duplicates)}")
    if not has_valid or not has_invalid:
        errors.append(f"{eval_label}: include at least one valid and one invalid case")

    blocking_rules = {
        rule_id
        for rule_id, obligation in obligations.items()
        if obligation in {"must", "must_not"}
    }
    missing_coverage = sorted(blocking_rules - covered)
    if missing_coverage:
        errors.append(
            f"{eval_label}: blocking rules without coverage: "
            + ", ".join(missing_coverage)
        )
    return errors


def main() -> int:
    voice = load_yaml(VOICE_PATH)
    error_pattern = load_yaml(ERROR_PATH)
    error_evals = load_yaml(EVAL_PATH)
    confirmation_pattern = load_yaml(CONFIRMATION_PATH)
    confirmation_evals = load_yaml(CONFIRMATION_EVAL_PATH)
    empty_state_pattern = load_yaml(EMPTY_STATE_PATH)
    empty_state_evals = load_yaml(EMPTY_STATE_EVAL_PATH)
    notification_pattern = load_yaml(NOTIFICATION_PATH)
    notification_evals = load_yaml(NOTIFICATION_EVAL_PATH)

    errors, tone_profiles, voice_rules = validate_voice(voice)
    pattern_errors, obligations = validate_error_pattern(error_pattern, tone_profiles)
    errors.extend(pattern_errors)
    errors.extend(
        validate_evals(
            error_evals, error_pattern.get("id", ""), obligations, "error evals"
        )
    )
    notification_errors, notification_obligations = validate_notification_pattern(
        notification_pattern, tone_profiles
    )
    errors.extend(notification_errors)
    errors.extend(
        validate_evals(
            notification_evals,
            notification_pattern.get("id", ""),
            notification_obligations,
            "notification evals",
        )
    )
    empty_state_errors, empty_state_obligations = validate_empty_state_pattern(
        empty_state_pattern, tone_profiles
    )
    errors.extend(empty_state_errors)
    errors.extend(
        validate_evals(
            empty_state_evals,
            empty_state_pattern.get("id", ""),
            empty_state_obligations,
            "empty-state evals",
        )
    )
    confirmation_errors, confirmation_obligations = validate_confirmation_pattern(
        confirmation_pattern, tone_profiles
    )
    errors.extend(confirmation_errors)
    errors.extend(
        validate_evals(
            confirmation_evals,
            confirmation_pattern.get("id", ""),
            confirmation_obligations,
            "confirmation evals",
        )
    )

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print(
        "Content patterns are valid: "
        f"{len(tone_profiles)} tone profiles, {len(voice_rules)} voice rules, "
        f"{len(obligations)} error rules, {len(error_evals['cases'])} error cases, "
        f"{len(confirmation_obligations)} confirmation rules, "
        f"{len(confirmation_evals['cases'])} confirmation cases, "
        f"{len(empty_state_obligations)} empty-state rules, "
        f"{len(empty_state_evals['cases'])} empty-state cases, "
        f"{len(notification_obligations)} notification rules, "
        f"{len(notification_evals['cases'])} notification cases"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
