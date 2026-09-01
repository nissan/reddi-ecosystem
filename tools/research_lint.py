#!/usr/bin/env python3
"""Validate research, prompt, and grant evidence registries."""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
REPO_LOCATION_PREFIX = "repo:"


def load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return data


def duplicate_errors(kind: str, values: list[str]) -> list[str]:
    return [
        f"duplicate {kind} ID: {value}"
        for value, count in Counter(values).items()
        if count > 1
    ]


def lint(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        research = load(root / "research/SOURCES.yaml")
        prompts = load(root / "prompts/catalog.yaml")
        grants = load(root / "docs/grants/commitments.yaml")
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return [str(exc)]

    sources = research.get("sources", [])
    source_ids = [item.get("id") for item in sources]
    errors.extend(duplicate_errors("source", source_ids))
    for source in sources:
        source_id = source.get("id", "<missing-source-id>")
        for field in ("publisher", "kind", "published", "url", "relevance"):
            if field not in source or source[field] in (None, ""):
                errors.append(f"{source_id}: missing source field {field}")
        location = str(source.get("url", ""))
        if location.startswith(REPO_LOCATION_PREFIX):
            relative = location[len(REPO_LOCATION_PREFIX):]
            target = (root / relative).resolve()
            if root.resolve() not in target.parents:
                errors.append(
                    f"{source_id}: {location} resolves outside the repository"
                )
            elif not target.is_file():
                errors.append(f"{source_id}: {location} does not name an existing file")
        elif not location.startswith("https://"):
            errors.append(
                f"{source_id}: source URL must use https or {REPO_LOCATION_PREFIX}"
            )

    catalog = prompts.get("prompts", [])
    prompt_ids = [item.get("id") for item in catalog]
    errors.extend(duplicate_errors("prompt", prompt_ids))
    for prompt in catalog:
        prompt_id = prompt.get("id", "<missing-prompt-id>")
        for field in ("file", "purpose", "tools"):
            if not prompt.get(field):
                errors.append(f"{prompt_id}: missing prompt field {field}")
        file_name = prompt.get("file")
        if file_name and not (root / "prompts" / file_name).is_file():
            errors.append(f"{prompt_id}: missing prompt file prompts/{file_name}")

    statuses = set(grants.get("statusVocabulary", []))
    commitments = grants.get("commitments", [])
    commitment_ids = [item.get("id") for item in commitments]
    errors.extend(duplicate_errors("commitment", commitment_ids))
    for commitment in commitments:
        commitment_id = commitment.get("id", "<missing-commitment-id>")
        for field in (
            "source", "promise", "due", "status", "evidence", "gaps",
            "acceptanceArtifacts", "ownerRole",
        ):
            if field not in commitment or commitment[field] is None:
                errors.append(f"{commitment_id}: missing commitment field {field}")
        if commitment.get("status") not in statuses:
            errors.append(f"{commitment_id}: invalid status {commitment.get('status')}")
        if not isinstance(commitment.get("evidence"), list):
            errors.append(f"{commitment_id}: evidence must be a list")
        if not isinstance(commitment.get("gaps"), list):
            errors.append(f"{commitment_id}: gaps must be a list")
        artifacts = commitment.get("acceptanceArtifacts")
        if artifacts is not None and (not isinstance(artifacts, list) or not artifacts):
            errors.append(
                f"{commitment_id}: acceptanceArtifacts must be a non-empty list"
            )
    return sorted(errors)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    errors = lint(args.root.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("research, prompt, and grant registries valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())

