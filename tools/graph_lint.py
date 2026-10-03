#!/usr/bin/env python3
"""Validate the canonical Reddi Ecosystem programme graph."""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_REGISTRY_SCHEMA_VERSIONS = {
    "planning/graph.yaml": 2,
    "planning/milestones.yaml": 2,
    "planning/repositories.yaml": 2,
}


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
        dependencies = nodes[node_id].get("dependsOn", [])
        if not isinstance(dependencies, list):
            dependencies = []
        for dependency in dependencies:
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


def require_dependency(
    errors: list[str], nodes: dict[str, dict[str, Any]], node_id: str, dependency: str
) -> None:
    node = nodes.get(node_id)
    if not node:
        errors.append(f"missing required planning node {node_id}")
        return
    dependencies = node.get("dependsOn")
    if not isinstance(dependencies, list):
        return
    if dependency not in dependencies:
        errors.append(f"{node_id}: missing required dependency {dependency}")


def require_human_gates(
    errors: list[str], nodes: dict[str, dict[str, Any]], node_id: str, gates: tuple[str, ...]
) -> None:
    declared = nodes[node_id].get("humanGates")
    if not isinstance(declared, list):
        return
    for gate in gates:
        if gate not in declared:
            errors.append(f"{node_id}: missing required human gate {gate}")


TECHNICAL_SPLIT_HUMAN_GATES = {
    "ECO-043": (
        "legal-or-grantor-communication", "privacy-publication", "live-payment",
        "paid-service-or-spend", "external-publication",
    ),
    "ECO-046": (
        "live-payment", "mainnet", "signing-or-custody", "privacy-publication",
        "legal-or-grantor-communication", "paid-service-or-spend",
        "production-release", "external-publication",
    ),
    "ECO-060": ("upstream-contact", "repo-creation"),
}
REQUIRED_COMPARISON_STANDARDS = ("mpp", "ap2", "x402")
REQUIRED_FIRST_RAIL_PROFILE = "solana-audd"
REQUIRED_ADAPTER_METHODS = (
    "quote",
    "authorize",
    "submit",
    "observe",
    "settle",
    "refund_or_reverse",
    "reconcile",
    "redact",
)


def lint_obligation_sequence(nodes: dict[str, dict[str, Any]]) -> list[str]:
    """Enforce captain-approved Solana/AUDD-first sequencing."""
    errors: list[str] = []
    for node_id in (
        "ECO-016", "ECO-017", "ECO-018", "ECO-041", "ECO-042", "ECO-043",
        "ECO-046", "ECO-047", "ECO-060", "ECO-062",
    ):
        if node_id not in nodes:
            errors.append(f"missing required planning node {node_id}")
    if errors:
        return errors

    require_dependency(errors, nodes, "ECO-042", "ECO-003")
    require_dependency(errors, nodes, "ECO-042", "ECO-004")
    require_dependency(errors, nodes, "ECO-042", "ECO-041")
    require_dependency(errors, nodes, "ECO-046", "ECO-042")
    require_dependency(errors, nodes, "ECO-047", "ECO-046")
    for node_id, node in sorted(nodes.items()):
        if node.get("railRole") == "comparison-fixture":
            require_dependency(errors, nodes, node_id, "ECO-046")
    require_dependency(errors, nodes, "ECO-060", "ECO-046")
    require_dependency(errors, nodes, "ECO-062", "ECO-047")
    for node_id, gates in TECHNICAL_SPLIT_HUMAN_GATES.items():
        require_human_gates(errors, nodes, node_id, gates)

    early_baselines = {
        "ECO-070": "ECO-016",
        "ECO-071": "ECO-018",
        "ECO-075": "ECO-017",
        "ECO-084": "ECO-018",
        "ECO-085": "ECO-017",
        "ECO-091": "ECO-016",
        "ECO-092": "ECO-017",
        "ECO-093": "ECO-016",
        "ECO-095": "ECO-017",
        "ECO-103": "ECO-017",
    }
    for node_id, baseline_id in early_baselines.items():
        require_dependency(errors, nodes, node_id, baseline_id)

    adapter_methods = nodes["ECO-041"].get("adapterMethods")
    if not isinstance(adapter_methods, list):
        errors.append("ECO-041: adapterMethods must be a list")
    else:
        for method in REQUIRED_ADAPTER_METHODS:
            if method not in adapter_methods:
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

    for relative, registry in (
        ("planning/graph.yaml", graph),
        ("planning/milestones.yaml", milestones_data),
        ("planning/repositories.yaml", repositories_data),
    ):
        expected = EXPECTED_REGISTRY_SCHEMA_VERSIONS[relative]
        if registry.get("schemaVersion") != expected:
            errors.append(f"{relative}: schemaVersion must be {expected}")

    milestone_items = milestones_data.get("milestones", [])
    milestones = {item.get("id") for item in milestone_items}
    milestone_order = {
        item.get("id"): index for index, item in enumerate(milestone_items)
        if item.get("id")
    }
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
            elif list_field != "evidenceExpected" and any(
                not item.rstrip().endswith(".") for item in value
            ):
                errors.append(
                    f"{node_id}: {list_field} entries must be complete sentences "
                    "ending with a period"
                )
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
                else:
                    dependency_milestone = nodes[dependency].get("milestone")
                    node_milestone = node.get("milestone")
                    if (
                        dependency_milestone in milestone_order
                        and node_milestone in milestone_order
                        and milestone_order[dependency_milestone]
                        > milestone_order[node_milestone]
                    ):
                        errors.append(
                            f"{node_id}: milestone {node_milestone} cannot depend on "
                            f"later {dependency} in {dependency_milestone}"
                        )
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
        if rail_role is not None and (
            not isinstance(rail_role, str) or rail_role not in rail_roles
        ):
            errors.append(f"{node_id}: unknown railRole {rail_role}")
        rail_profile = node.get("railProfile")
        standards = node.get("comparisonStandards")
        adapter_methods = node.get("adapterMethods")
        for field, value in (
            ("railProfile", rail_profile),
            ("comparisonStandards", standards),
        ):
            if value is not None and rail_role is None:
                errors.append(f"{node_id}: {field} requires an explicit railRole")
        if rail_profile is not None:
            if not isinstance(rail_profile, str) or rail_profile not in rail_profiles:
                errors.append(f"{node_id}: unknown railProfile {rail_profile}")
            elif (
                rail_profile == REQUIRED_FIRST_RAIL_PROFILE
                and rail_role != "first-implementation"
            ):
                errors.append(
                    f"{node_id}: railProfile {REQUIRED_FIRST_RAIL_PROFILE} requires "
                    "railRole first-implementation"
                )
        if standards is not None:
            if not isinstance(standards, list) or not standards:
                errors.append(f"{node_id}: comparisonStandards must be a non-empty list")
            else:
                for standard in standards:
                    if not isinstance(standard, str) or standard not in rail_profiles:
                        errors.append(
                            f"{node_id}: unknown comparisonStandards entry {standard}"
                        )
                    elif standard == REQUIRED_FIRST_RAIL_PROFILE:
                        errors.append(
                            f"{node_id}: {REQUIRED_FIRST_RAIL_PROFILE} is the first "
                            "implementation profile, not a comparison standard"
                        )
        if "adapterMethods" in node:
            if not isinstance(adapter_methods, list) or not adapter_methods:
                errors.append(f"{node_id}: adapterMethods must be a non-empty list")
            else:
                valid_methods = []
                for method in adapter_methods:
                    if method not in REQUIRED_ADAPTER_METHODS:
                        errors.append(f"{node_id}: unknown adapter method {method}")
                    elif isinstance(method, str):
                        valid_methods.append(method)
                for method in duplicates(valid_methods):
                    errors.append(f"{node_id}: duplicate adapter method {method}")
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
