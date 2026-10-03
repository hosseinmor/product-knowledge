#!/usr/bin/env python3
"""Validate Product Knowledge source authority and repository boundaries."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "product-knowledge-sources.yml"
JOBVISION_URL = "https://docs-jv.jvoffice.ir/"
FORBIDDEN_ROOTS = (
    "products",
    "shared/product-concepts",
    "shared/product-services",
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


def main() -> int:
    errors: list[str] = []
    try:
        data = yaml.load(SOURCE_PATH.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
    except FileNotFoundError:
        print(f"ERROR missing source authority contract: {SOURCE_PATH}")
        return 1
    except yaml.YAMLError as exc:
        print(f"ERROR invalid YAML in {SOURCE_PATH}: {exc}")
        return 1

    if not isinstance(data, dict):
        print("ERROR source authority contract must be a YAML mapping")
        return 1

    if data.get("repository_role") != "product_content_and_design_system":
        errors.append("repository_role must be product_content_and_design_system")

    products = data.get("products")
    if not isinstance(products, dict):
        errors.append("products must be a mapping")
        products = {}

    jobvision = products.get("jobvision", {})
    if jobvision.get("authority") != "canonical_external":
        errors.append("JobVision authority must be canonical_external")
    if jobvision.get("url") != JOBVISION_URL:
        errors.append(f"JobVision URL must be {JOBVISION_URL}")
    if jobvision.get("repository_fallback") != "forbidden":
        errors.append("JobVision repository fallback must be forbidden")

    cando = products.get("cando", {})
    if cando.get("authority") != "unavailable":
        errors.append("Cando authority must remain unavailable until approved")
    if cando.get("url") is not None:
        errors.append("Cando URL must be null while no canonical source exists")
    if cando.get("repository_fallback") != "forbidden":
        errors.append("Cando repository fallback must be forbidden")
    if not isinstance(cando.get("allowed_inputs"), list) or not cando["allowed_inputs"]:
        errors.append("Cando allowed_inputs must be a non-empty list")

    declared_roots = data.get("forbidden_active_roots")
    if declared_roots != list(FORBIDDEN_ROOTS):
        errors.append("forbidden_active_roots must declare the protected roots exactly")

    for relative in FORBIDDEN_ROOTS:
        root = ROOT / relative
        if root.exists() and any(path.is_file() for path in root.rglob("*")):
            errors.append(f"active Product Knowledge files are forbidden under {relative}/")

    required_references = {
        "AGENTS.md": JOBVISION_URL,
        "README.md": JOBVISION_URL,
        "ai/router.md": JOBVISION_URL,
        "docs/ai-tool-setup.md": JOBVISION_URL,
    }
    for relative, required in required_references.items():
        path = ROOT / relative
        if not path.exists() or required not in path.read_text(encoding="utf-8"):
            errors.append(f"{relative} must reference {required}")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print(
        "Product Knowledge source authority is valid: "
        "JobVision=canonical_external, Cando=unavailable, repository fallback=forbidden"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
