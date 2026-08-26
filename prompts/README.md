# Prompt foundry

Prompts here are reviewed executable artifacts. They do not grant authority. Runtime
capabilities, repository permissions, signing policy, and human gates remain external controls.

## Common contract

Every role receives a `work_packet` containing:

- node ID, objective, target repository, file/issue footprint, and acceptance criteria;
- canonical sources and freshness requirements;
- dependencies, decisions, assumptions, and non-goals;
- tool/data policy, budget, stop conditions, and human gates;
- required output schema and evidence destination.

Every role returns:

```yaml
status: complete | partial | blocked | rejected
summary: concise outcome
claims:
  - statement: what is asserted
    evidence: exact artifact or source
    confidence: high | medium | low
changes: []
checks: []
risks: []
decisionsRequested: []
followUpNodes: []
syncLog: what changed relative to the work packet
```

The role must stop on missing authority, ambiguous canonical ownership, secrets, unsafe
external action, or a failed prerequisite. It may not reinterpret a human gate as a task.

## Promotion

`catalog.yaml` is the prompt registry. A material change requires a baseline, development
and held-out evaluation, adversarial/safety cases, cost/latency comparison, reviewer, and
rollback version. Provider-specific overlays must not change the base role's authority.

