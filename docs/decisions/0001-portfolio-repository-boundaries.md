# ADR-0001: Portfolio repository boundaries

- Status: accepted for bootstrap
- Date: 2026-08-26
- Decision owner: programme steward
- Review: after M2 or any canonical repository split

## Context

ADL, RAP, and Arena already have active public repositories, histories, issues, tests, and
canonical responsibilities. A new end-to-end programme repository is needed without losing,
copying, or silently superseding that work.

## Decision

`nissan/reddi-ecosystem` owns the cross-repository roadmap, dependency graph, grant evidence
index, research/prompt governance, claims, upstream obligations, and open/commercial covenant.

- `nissan/reddiagent-lab` remains canonical for ADL semantics and conformance.
- `nissan/reddi-agent-protocol` remains canonical for RAP code, adapters, receipts, and proofs.
- `nissan/reddi-arena` remains canonical for Arena rules, fixtures, judges, and replay.
- Buzz and Omarchy remain external upstreams; integration repositories require explicit gates.

GitHub issues are collaboration projections. `planning/graph.yaml` is the canonical portfolio
dependency record. Component implementation issues remain in their component repositories.

## Consequences

The programme gains a single roadmap without flattening ownership. Cross-repository status
requires reconciliation and may lag volatile GitHub state; CI and scheduled review manage that
trade-off. Duplicate issue bodies and local specification forks are prohibited.

