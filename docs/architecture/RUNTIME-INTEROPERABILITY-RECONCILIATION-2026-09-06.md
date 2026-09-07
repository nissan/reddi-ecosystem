# Runtime interoperability roadmap reconciliation

- Audit date: 2026-09-06
- Scope: Buzz, OpenClaw, Firstmate, Hermes, ADL, RAP, Arena, Quattro, and the ecosystem graph
- Status: roadmap reconciliation complete 2026-09-07; independent review and executable conformance remain open

## Result

The existing roadmap already establishes portable runtime/model profiles, ADL deployment
projections, RAP adapters and event/receipt boundaries, Arena multi-runtime evaluation, a
sidecar-first Buzz proof, and thin Quattro packaging. Buzz is explicitly integrated.

OpenClaw, Firstmate, and Hermes were not named in the canonical graph, source register,
milestones, or generated issues. Their compatibility was therefore architectural intent rather
than a testable programme commitment. No current repository evidence supports claiming that RAP
is compatible with any version of those three projects.

## Coverage classification

| Area | Existing coverage | Classification | Required correction |
|---|---|---|---|
| Portable runtime abstraction | ADR-0002, ECO-024, ECO-030–035 | Planned, generic | Add named upstream audit, version pins, adapter operations, and capability levels |
| Buzz/Nostr | M3, E06, ECO-060–065 | Explicitly planned | Preserve sidecar-first path; join only after M2 execution/evidence proof |
| OpenClaw | No named graph/source entry before this audit | Missing | Treat Gateway/plugin/subagent surfaces as first general-purpose reference runtime |
| Firstmate | No named graph/source entry before this audit | Missing | Pilot worktree crew discipline, then test a coding-runtime adapter |
| Hermes | No named graph/source entry before this audit | Missing | Test durable profiles, memory separation, skills, gateways, and recovery |
| Runtime evidence | ECO-044–045 and ECO-054 | Partial | Add runtime/harness/session/tool provenance and crash reconciliation |
| Quattro packaging | M4/E07 | Planned | Package only adapters that pass versioned conformance; keep cockpit keyless |
| Compatibility claims | ECO-024 | Partial | Publish exact tested versions and supported/experimental/unsupported/unknown states |

## Existing nodes to preserve

- ECO-024 owns the portfolio compatibility matrix.
- ECO-030–035 own canonical ADL portability, Agent BOM, projections, authority, and conformance.
- ECO-040 and ECO-044–045 own RAP boundary, event/replay, evidence, and receipt work.
- ECO-050–055 own Arena evaluation and runtime/harness comparisons.
- ECO-060–065 own the Buzz architecture and sidecar proof.
- ECO-071 and later packaging nodes remain downstream of proven contracts.

## Newly opened gap

ECO-026 owns the primary-source and integration-seam audit. It must produce canonical follow-up
issues in the component repositories rather than implementing ADL, RAP, or Arena semantics here.

The 2026-09-07 continuation resolved immutable research baselines and added the derived graph
nodes ECO-036, ECO-048, ECO-049, ECO-057, ECO-058, and ECO-076. Detailed source findings and
current non-support states are in `research/2026-09-runtime-interoperability-audit.md`.

The expected follow-up split is:

1. `reddiagent-lab`: runtime execution-profile schema and projection fixtures;
2. `reddi-agent-protocol`: runtime adapter interface, mock, event/evidence binding, and reference adapters;
3. `reddi-arena`: cross-runtime scenarios and conformance scorecards;
4. `reddi-ecosystem`: source/version matrix, dependency graph, upstream policy, and packaging gates.

## Compatibility claim policy

Until executable evidence exists, public wording is limited to:

> Reddi is designed for runtime interoperability. OpenClaw, Firstmate, and Hermes are planned
> reference adapter targets; compatibility has not yet been verified.

A compatibility claim requires a pinned upstream version or revision, declared conformance
level, run record, effective-authority comparison, known limitations, and review date.

## Immediate execution sequence

1. Complete ECO-026 with pinned upstream release and extension-seam evidence.
2. Accept or amend ADR-0003.
3. File the canonical runtime adapter and projection issues in RAP and ADL repositories.
4. Implement the deterministic mock before any named adapter.
5. Prove OpenClaw first, then Firstmate and Hermes, against shared fixtures.
6. Add the proven adapters to Arena's matrix and only then package them through Quattro.

## Non-claims and remaining uncertainty

This audit did not execute or install the upstream runtimes, inspect unpublished APIs, or prove
their security boundaries. “OpenClaw 2.0” is not used as a compatibility identifier; the audit
will record the exact calendar-versioned release tested. No external issue, pull request,
repository creation, or upstream contact is authorized by this document.
