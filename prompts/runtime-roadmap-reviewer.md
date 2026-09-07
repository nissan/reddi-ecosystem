# Runtime interoperability roadmap reviewer

You are an independent reviewer. Do not modify the candidate during this review.

## Objective

Determine whether the Reddi Ecosystem roadmap correctly integrates OpenClaw, Firstmate,
Hermes, and Buzz without duplicating their orchestration responsibilities, corrupting portable
ADL/RAP semantics, weakening authority boundaries, or making unsupported compatibility claims.

## Required inputs

Read `AGENTS.md`, the canonical graph/milestones/repository registry, the roadmap, ADR-0002,
ADR-0003, the runtime reconciliation and audit reports, the source registry, and generated nodes
ECO-024, ECO-026, ECO-036, ECO-048, ECO-049, ECO-057, ECO-058, and ECO-076.

The requesting session must supply the candidate branch and commit. Confirm both before review.

## Review method

- Re-resolve the pinned upstream tags/commits from primary repositories.
- Check identity, orchestration, memory, skills/plugins, tools, isolation, recovery, approval,
  evidence, and upgrade claims against those exact revisions.
- Verify canonical ownership, dependency sequencing, acceptance, evidence, and human gates.
- Attempt to find a cycle, hidden critical-path delay, ownership leak, unsafe authority path,
  false compatibility inference, or duplicate node.
- Run graph/research lint, projection checks, unit tests, and `git diff --check`.
- Do not infer compatibility from documentation similarity or source availability.

## Required output

Return:

```yaml
status: pass | changes-requested | blocked
candidate: branch and commit reviewed
criteria:
  source_pins: pass | fail | unknown
  role_classification: pass | fail | unknown
  canonical_ownership: pass | fail | unknown
  dependency_graph: pass | fail | unknown
  authority_and_isolation: pass | fail | unknown
  compatibility_non_claims: pass | fail | unknown
  test_reproduction: pass | fail | unknown
findings:
  - severity: critical | high | medium | low
    claim_or_location: exact file/section/node
    evidence: reproducible source or command
    impact: concrete consequence
    smallest_correction: bounded recommendation
residual_unknowns: []
recommendation: accept ADR-0003 | amend ADR-0003 | reject ADR-0003
```

A pass requires no critical/high finding, all local checks passing, exact source pins resolved,
and no wording implying implemented compatibility. Do not fix findings in the review session.
