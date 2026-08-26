#!/usr/bin/env python3
"""Generate deterministic, reviewable issue specifications from planning/graph.yaml."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]


def load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def digest(item: dict[str, Any]) -> str:
    raw = json.dumps(item, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def bullets(items: list[str], checkbox: bool = False) -> str:
    prefix = "- [ ]" if checkbox else "-"
    return "\n".join(f"{prefix} {item}" for item in items) or "- None"


def node_markdown(node: dict[str, Any], epics: dict[str, dict[str, Any]]) -> str:
    dependency_links = [f"[{item}](../nodes/{item}.md)" for item in node["dependsOn"]]
    external = node.get("externalIssue")
    source_hash = digest(node)
    lines = [
        f"# [{node['id']}] {node['title']}",
        "",
        "> Generated from `planning/graph.yaml`; edit the graph, not this file.  ",
        f"> Source hash: `{source_hash}`",
        "",
        "## Delivery contract",
        "",
        f"- Epic: [{node['epic']}](../epics/{node['epic']}.md) — {epics[node['epic']]['title']}",
        f"- Milestone: `{node['milestone']}`",
        f"- Target repository: `{node['targetRepo']}`",
        f"- Projection: `{node['githubProjection']}`",
        f"- Status / priority: `{node['status']}` / `{node['priority']}`",
        f"- Owner role: {node['ownerRole']}",
        f"- Dependencies: {', '.join(dependency_links) if dependency_links else 'none'}",
    ]
    if external:
        lines.append(f"- Existing canonical issue: {external}")
    lines += [
        "",
        "## Outcome",
        "",
        node["outcome"],
        "",
        "## Tasks and subtasks",
        "",
        bullets(node["subtasks"], checkbox=True),
        "",
        "## Acceptance criteria",
        "",
        bullets(node["acceptance"], checkbox=True),
        "",
        "## Required evidence",
        "",
        bullets(node["evidenceExpected"], checkbox=True),
        "",
        "## Human gates",
        "",
        bullets(node["humanGates"]) if node["humanGates"] else "- None beyond normal review.",
        "",
        "## Non-goals and completion",
        "",
        "- This projection does not move canonical component ownership into this repository.",
        "- This issue does not authorize secrets, signing, spend, mainnet, outreach, or publication beyond the listed gates.",
        "- Completion requires acceptance evidence, independent audit, graph update, and recorded upstream/community obligations.",
        "",
    ]
    return "\n".join(lines)


def epic_markdown(epic: dict[str, Any], nodes: list[dict[str, Any]]) -> str:
    source_hash = digest({"epic": epic, "nodes": [item["id"] for item in nodes]})
    lines = [
        f"# [{epic['id']}] {epic['title']}",
        "",
        "> Generated from `planning/graph.yaml`; edit the graph, not this file.  ",
        f"> Source hash: `{source_hash}`",
        "",
        f"- Milestone: `{epic['milestone']}`",
        f"- Default target repository: `{epic['targetRepo']}`",
        "",
        "## Outcome",
        "",
        epic["outcome"],
        "",
        "## Child issues",
        "",
    ]
    for node in nodes:
        lines.append(
            f"- [{node['id']} — {node['title']}](../nodes/{node['id']}.md) "
            f"(`{node['status']}`, `{node['priority']}`, `{node['targetRepo']}`)"
        )
    lines.append("")
    return "\n".join(lines)


def generate(root: Path = ROOT, check: bool = False) -> list[str]:
    graph = load(root / "planning/graph.yaml")
    output = root / "planning/issues"
    expected: dict[Path, str] = {}
    epics = {item["id"]: item for item in graph["epics"]}
    by_epic = {epic_id: [] for epic_id in epics}
    for node in graph["nodes"]:
        by_epic[node["epic"]].append(node)
        expected[output / "nodes" / f"{node['id']}.md"] = node_markdown(node, epics)
    for epic_id, epic in epics.items():
        expected[output / "epics" / f"{epic_id}.md"] = epic_markdown(epic, by_epic[epic_id])

    index = [
        "# Generated issue specifications",
        "",
        "These files are deterministic projections of `planning/graph.yaml`. The graph is canonical.",
        "Do not edit generated files by hand.",
        "",
        f"- {len(epics)} epics",
        f"- {len(graph['nodes'])} issues",
        "",
        "## Epics",
        "",
    ]
    for epic in graph["epics"]:
        index.append(f"- [{epic['id']} — {epic['title']}](epics/{epic['id']}.md)")
    index.append("")
    expected[output / "README.md"] = "\n".join(index)

    if check:
        drift: list[str] = []
        actual_files = set(output.rglob("*.md")) if output.exists() else set()
        for path, content in expected.items():
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                drift.append(str(path.relative_to(root)))
        for path in actual_files - set(expected):
            drift.append(str(path.relative_to(root)))
        return sorted(drift)

    if output.exists():
        shutil.rmtree(output)
    for path, content in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    drift = generate(args.root.resolve(), check=args.check)
    if drift:
        for path in drift:
            print(f"OUT OF DATE: {path}")
        return 1
    if args.check:
        print("generated issue specifications are current")
    else:
        print("generated issue specifications updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

