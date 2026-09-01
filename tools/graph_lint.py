#!/usr/bin/env python3
"""Validate the canonical Reddi Ecosystem programme graph."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return data


def duplicates(values: list[str]) -> list[str]:
    return sorted(value for value, count in Counter(values).items() if count > 1)


def find_cycle(nodes: dict[str, dict[str, Any]]) -> list[str] | None:
    visiting: set[str] = set()
    visited: set[str] = set()
    path: list[str] = []

    def walk(node_id: str) -> list[str] | None:
        if node_id in visiting:
            start = path.index(node_id)
            return path[start:] + [node_id]
        if node_id in visited:
            return None
        visiting.add(node_id)
        path.append(node_id)
        for dependency in nodes[node_id].get("dependsOn", []):
            if not isinstance(dependency, str):
                continue
            if dependency in nodes:
                cycle = walk(dependency)
                if cycle:
                    return cycle
        path.pop()
        visiting.remove(node_id)
        visited.add(node_id)
        return None

    for node_id in nodes:
        cycle = walk(node_id)
        if cycle:
            return cycle
    return None


def text_for(item: dict[str, Any], fields: tuple[str, ...]) -> str:
    parts: list[str] = []
    for field in fields:
        value = item.get(field)
        if isinstance(value, list):
            parts.extend(str(entry) for entry in value)
        elif value is not None:
            parts.append(str(value))
    return "\n".join(parts).lower()


def require_dependency(
    errors: list[str], nodes: dict[str, dict[str, Any]], node_id: str, dependency: str
) -> None:
    node = nodes.get(node_id)
    if not node:
        errors.append(f"missing required planning node {node_id}")
        return
    if dependency not in node.get("dependsOn", []):
        errors.append(f"{node_id}: missing required dependency {dependency}")


REQUIRED_COMPARISON_STANDARDS = ("mpp", "ap2", "x402")
REQUIRED_FIRST_RAIL_PROFILE = "solana-audd"


def lint_obligation_sequence(nodes: dict[str, dict[str, Any]]) -> list[str]:
    """Enforce captain-approved Solana/AUDD-first sequencing."""
    errors: list[str] = []
    for node_id in ("ECO-041", "ECO-042", "ECO-043", "ECO-046", "ECO-047"):
        if node_id not in nodes:
            errors.append(f"missing required planning node {node_id}")
    if errors:
        return errors

    require_dependency(errors, nodes, "ECO-042", "ECO-003")
    require_dependency(errors, nodes, "ECO-042", "ECO-041")
    require_dependency(errors, nodes, "ECO-046", "ECO-042")
    require_dependency(errors, nodes, "ECO-047", "ECO-046")
    for node_id, node in sorted(nodes.items()):
        if node.get("railRole") == "comparison-fixture":
            require_dependency(errors, nodes, node_id, "ECO-047")
    if "ECO-060" in nodes:
        require_dependency(errors, nodes, "ECO-060", "ECO-047")

    adapter_text = text_for(nodes["ECO-041"], ("outcome", "acceptance", "subtasks"))
    for method in (
        "quote",
        "authorize",
        "submit",
        "observe",
        "settle",
        "refund_or_reverse",
        "reconcile",
        "redact",
    ):
        if not re.search(rf"\b{re.escape(method)}\b", adapter_text):
            errors.append(f"ECO-041: adapter contract must cover {method}")

    for node_id, role in (
        ("ECO-041", "rail-neutral-core"),
        ("ECO-042", "first-implementation"),
        ("ECO-043", "comparison-fixture"),
    ):
        if nodes[node_id].get("railRole") != role:
            errors.append(f"{node_id}: railRole must be {role}")
    declared_first = sorted(
        node_id
        for node_id, node in nodes.items()
        if node.get("railRole") == "first-implementation"
    )
    if declared_first != ["ECO-042"]:
        errors.append(
            "exactly one node may declare railRole first-implementation, found "
            + (", ".join(declared_first) or "none")
        )
    for node_id in declared_first:
        if nodes[node_id].get("railProfile") != REQUIRED_FIRST_RAIL_PROFILE:
            errors.append(
                f"{node_id}: first-implementation railProfile must be "
                f"{REQUIRED_FIRST_RAIL_PROFILE}"
            )
    standards = nodes["ECO-043"].get("comparisonStandards")
    if not isinstance(standards, list):
        errors.append("ECO-043: comparisonStandards must be a list")
    else:
        for standard in REQUIRED_COMPARISON_STANDARDS:
            if standard not in standards:
                errors.append(f"ECO-043: comparisonStandards must include {standard}")
    return errors


def lint(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        graph = load_yaml(root / "planning/graph.yaml")
        milestones_data = load_yaml(root / "planning/milestones.yaml")
        repositories_data = load_yaml(root / "planning/repositories.yaml")
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return [str(exc)]

    milestones = {item.get("id") for item in milestones_data.get("milestones", [])}
    repositories = {
        item.get("id") for item in repositories_data.get("repositories", [])
    } | {
        item.get("id") for item in repositories_data.get("plannedRepositories", [])
    }
    statuses = set(graph.get("statusVocabulary", []))
    priorities = set(graph.get("priorityVocabulary", []))
    human_gates = set(graph.get("humanGates", []))
    rail_roles = set(graph.get("railRoleVocabulary", []))
    rail_profiles = set(graph.get("railProfileVocabulary", []))
    epics_list = graph.get("epics", [])
    nodes_list = graph.get("nodes", [])

    if not isinstance(epics_list, list) or not isinstance(nodes_list, list):
        return ["planning/graph.yaml: epics and nodes must be lists"]

    epic_ids = [item.get("id") for item in epics_list]
    node_ids = [item.get("id") for item in nodes_list]
    for value in duplicates(epic_ids):
        errors.append(f"duplicate epic ID: {value}")
    for value in duplicates(node_ids):
        errors.append(f"duplicate node ID: {value}")

    epics = {item.get("id"): item for item in epics_list if item.get("id")}
    nodes = {item.get("id"): item for item in nodes_list if item.get("id")}
    errors.extend(lint_obligation_sequence(nodes))
    children: dict[str, list[str]] = defaultdict(list)

    for epic_id, epic in epics.items():
        for field in ("title", "milestone", "targetRepo", "outcome"):
            if not epic.get(field):
                errors.append(f"{epic_id}: missing {field}")
        if epic.get("milestone") not in milestones:
            errors.append(f"{epic_id}: unknown milestone {epic.get('milestone')}")
        if epic.get("targetRepo") not in repositories:
            errors.append(f"{epic_id}: unknown targetRepo {epic.get('targetRepo')}")

    required = (
        "id", "epic", "type", "title", "milestone", "targetRepo",
        "githubProjection", "status", "priority", "dependsOn", "ownerRole",
        "outcome", "acceptance", "subtasks", "evidenceExpected", "humanGates",
    )
    for node_id, node in nodes.items():
        for field in required:
            if field not in node or node[field] is None:
                errors.append(f"{node_id}: missing {field}")
        epic_id = node.get("epic")
        children[epic_id].append(node_id)
        if epic_id not in epics:
            errors.append(f"{node_id}: unknown epic {epic_id}")
        elif node.get("milestone") != epics[epic_id].get("milestone"):
            errors.append(
                f"{node_id}: milestone {node.get('milestone')} differs from parent {epic_id}"
            )
        if node.get("milestone") not in milestones:
            errors.append(f"{node_id}: unknown milestone {node.get('milestone')}")
        if node.get("targetRepo") not in repositories:
            errors.append(f"{node_id}: unknown targetRepo {node.get('targetRepo')}")
        if node.get("githubProjection") not in {"implementation", "tracker"}:
            errors.append(f"{node_id}: invalid githubProjection")
        if node.get("status") not in statuses:
            errors.append(f"{node_id}: invalid status {node.get('status')}")
        if node.get("priority") not in priorities:
            errors.append(f"{node_id}: invalid priority {node.get('priority')}")
        for list_field, minimum in (
            ("acceptance", 2), ("subtasks", 2), ("evidenceExpected", 1)
        ):
            value = node.get(list_field)
            if not isinstance(value, list) or len(value) < minimum:
                errors.append(f"{node_id}: {list_field} must contain at least {minimum} items")
            elif any(not isinstance(item, str) for item in value):
                errors.append(f"{node_id}: {list_field} must contain only strings")
        for optional_list_field in ("evidenceProduced",):
            if optional_list_field in node:
                value = node.get(optional_list_field)
                if not isinstance(value, list):
                    errors.append(f"{node_id}: {optional_list_field} must be a list")
                elif any(not isinstance(item, str) for item in value):
                    errors.append(f"{node_id}: {optional_list_field} must contain only strings")
        dependencies = node.get("dependsOn", [])
        if not isinstance(dependencies, list):
            errors.append(f"{node_id}: dependsOn must be a list")
        elif any(not isinstance(dependency, str) for dependency in dependencies):
            errors.append(f"{node_id}: dependsOn must contain only strings")
        else:
            for dependency in dependencies:
                if dependency == node_id:
                    errors.append(f"{node_id}: self dependency")
                elif dependency not in nodes:
                    errors.append(f"{node_id}: unknown dependency {dependency}")
        gates = node.get("humanGates", [])
        if not isinstance(gates, list):
            errors.append(f"{node_id}: humanGates must be a list")
        elif any(not isinstance(gate, str) for gate in gates):
            errors.append(f"{node_id}: humanGates must contain only strings")
        else:
            for gate in gates:
                if gate not in human_gates:
                    errors.append(f"{node_id}: unknown human gate {gate}")
        rail_role = node.get("railRole")
        if rail_role is not None and rail_role not in rail_roles:
            errors.append(f"{node_id}: unknown railRole {rail_role}")
        rail_profile = node.get("railProfile")
        if rail_profile is not None:
            if rail_profile not in rail_profiles:
                errors.append(f"{node_id}: unknown railProfile {rail_profile}")
            elif (
                rail_profile == REQUIRED_FIRST_RAIL_PROFILE
                and rail_role != "first-implementation"
            ):
                errors.append(
                    f"{node_id}: railProfile {REQUIRED_FIRST_RAIL_PROFILE} requires "
                    "railRole first-implementation"
                )
        standards = node.get("comparisonStandards")
        if standards is not None:
            if rail_role is None:
                errors.append(
                    f"{node_id}: comparisonStandards requires an explicit railRole"
                )
            if not isinstance(standards, list) or not standards:
                errors.append(f"{node_id}: comparisonStandards must be a non-empty list")
            else:
                for standard in standards:
                    if standard not in rail_profiles:
                        errors.append(
                            f"{node_id}: unknown comparisonStandards entry {standard}"
                        )
                    elif standard == REQUIRED_FIRST_RAIL_PROFILE:
                        errors.append(
                            f"{node_id}: {REQUIRED_FIRST_RAIL_PROFILE} is the first "
                            "implementation profile, not a comparison standard"
                        )
        external = node.get("externalIssue")
        if external and not str(external).startswith("https://github.com/"):
            errors.append(f"{node_id}: externalIssue must be an https GitHub URL")

    for epic_id in epics:
        if not children[epic_id]:
            errors.append(f"{epic_id}: has no nodes")

    cycle = find_cycle(nodes)
    if cycle:
        errors.append("dependency cycle: " + " -> ".join(cycle))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    errors = lint(args.root.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    graph = load_yaml(args.root.resolve() / "planning/graph.yaml")
    print(f"graph valid: {len(graph['epics'])} epics, {len(graph['nodes'])} nodes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
