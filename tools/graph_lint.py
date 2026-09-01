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
        else:
            for dependency in dependencies:
                if dependency == node_id:
                    errors.append(f"{node_id}: self dependency")
                elif dependency not in nodes:
                    errors.append(f"{node_id}: unknown dependency {dependency}")
        gates = node.get("humanGates", [])
        if not isinstance(gates, list):
            errors.append(f"{node_id}: humanGates must be a list")
        else:
            for gate in gates:
                if gate not in human_gates:
                    errors.append(f"{node_id}: unknown human gate {gate}")
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

