# Agent, graph, loop, and event engineering synthesis

## Decision summary

The programme should build a **prompt foundry inside a verifiable delivery harness**, not
a prompt warehouse. Prompts propose and execute work; typed state, tools, tests, evidence,
independent audit, and human authority determine whether the work advances.

This synthesis turns the primary-source register in `SOURCES.yaml` into programme controls.
The cited work is directional evidence. Every Reddi-specific claim still needs an experiment.

## Adopted engineering model

```text
programme intent
   -> portfolio dependency graph
      -> bounded issue/node contract
         -> context pack + tools + authority
            -> execute observable loop
               -> independent outcome audit
                  -> integrate or rollback
                     -> convert failure into eval + graph update
```

### 1. Repository-local truth and progressive disclosure

OpenAI's harness report and Anthropic's context guidance converge on a practical rule:
agents need a navigable, versioned map and just-in-time access to deeper truth. A giant
prompt becomes stale and consumes the context needed for the task. This repository uses
a short `AGENTS.md`, canonical YAML registers, deep documents, generated issue views, and
linters. Private decisions must be reduced to a safe repository decision record before an
agent can reliably act on them.

### 2. External state beats conversational memory

Long work is represented outside a context window: graph node, acceptance criteria,
dependency status, decisions, evidence, sync log, and next action. Context compaction or
reset may help an individual run, but the checked artifact is the handoff between runs,
models, people, and repositories.

### 3. Manage–execute–audit separation

Planning, production, and evaluation have different failure modes. The manager frames a
bounded node and selects context; the executor changes the target; a read-only auditor
tries to disprove acceptance. The author never supplies the only judgment of its output.
For subjective work, a rubric and independent reviewer are mandatory; for deterministic
work, tests and final environment state outrank narrative confidence.

### 4. Graph engineering is execution control

The portfolio graph records canonical ownership, typed dependencies, human gates, evidence,
and non-overlapping footprints. Graphs are useful where work branches, joins, retries, or
crosses repositories. A linear checklist remains preferable for a single bounded change.
Graph expansion is budgeted: new nodes require a parent, reason, exit gate, and owner role.

An Agent Dependency Graph and Agent Bill of Materials extend this to deployed agents:
model/runtime, system prompt, tools, skills, connectors, data sources, policies, evaluators,
identity, payment authority, and transitive versions should be inspectable and attestable.

### 5. Loop engineering closes on evidence

The default loop is:

`frame -> inspect -> plan -> execute -> verify -> audit -> integrate -> retrospect`

Each pass has a stop condition and output artifact. Repetition without a changed hypothesis,
new evidence, or explicit retry budget is not progress. Failures become a regression case,
tool improvement, context correction, prompt candidate, architectural decision, or new node.

### 6. Event engineering preserves causality and replay

RAP events use stable identity, type, source, subject, time, schema version, correlation,
causation, trace context, authority basis, and redaction class. Producers use transactional
outbox/idempotency patterns where applicable; consumers tolerate replay and ordering limits.
The event log is an observation trail, not automatic business truth. Settlement and external
outcomes must be reconciled to the authoritative system.

### 7. Prompt generation is constrained optimization

GEPA, SePO, SPEAR, and DSPy demonstrate that prompts/modules can be improved using execution
feedback. The safe Reddi lifecycle is:

1. register baseline prompt, dataset version, model/runtime, tools, budget, and metrics;
2. generate candidates in a sandbox from diagnosed failures;
3. score development cases, then locked held-out cases and adversarial/safety cases;
4. compare task success, false claims, policy violations, latency, cost, and variance;
5. require human review for changed authority or public behavior;
6. promote a versioned candidate or automatically roll back on guard-metric regression;
7. retain result summaries and permitted traces, never secrets or hidden reasoning.

No optimizer may edit its own promotion criteria, tool permissions, held-out set, or human gates.

### 8. Multi-agent work is selective

Parallel agents are justified for high-value, independent breadth work such as primary-source
research, cross-repository inventory, or adversarial review. They are a poor default when work
shares the same files, has tight dependencies, or costs more to coordinate than execute. Each
delegation states objective, boundaries, tools, output schema, source policy, and stop condition.
The lead agent validates rather than concatenates results.

### 9. Tools and authority are part of the agent definition

Tool descriptions should be distinct, narrow, token-efficient, typed, and fail closed. Runtime
permissions are capabilities, not prompt suggestions. Irreversible tools require preconditions,
scoped credentials, idempotency, preview/dry-run where possible, and human approval. Model output
is never wallet, payment, release, or publication authority.

### 10. Provider and surface diversity is an evaluation dimension

OpenAI, Anthropic, Gemini/ADK, ByteDance Seed/UI-TARS/DeerFlow, Z.ai GLM, Mistral, and xAI
provide useful but changing implementations. ADL should describe portable intent and harness
requirements; provider profiles supply model-specific prompting, thinking, tool, and context
settings. Conformance runs across at least two materially different model/runtime profiles.

Buzz and Quattro introduce GUI and human-in-the-loop state. Their evaluation suite must include
visual ambiguity, stale UI, malicious content, interrupted workflows, replay, unavailable local
services, and approval recovery—not only happy-path API tests.

## Prompt foundry artifacts

Every prompt package contains:

- manifest: ID, version, purpose, owner, compatible agent/ADL profile;
- contract: inputs, outputs, assumptions, non-goals, completion and stop conditions;
- context recipe: mandatory sources, just-in-time retrieval, freshness requirements;
- tool policy: allowed tools, data boundaries, irreversible actions, escalation;
- eval manifest: development, held-out, adversarial, safety, cost, latency, and variance metrics;
- release record: baseline, candidate result, reviewer, decision, rollback target;
- failure register: observed failure, reproduction, remediation, and regression case.

The first role prompts implement recovery auditor, research scout, synthesis framer, graph
planner, issue writer, node executor, independent auditor, retrospective, prompt optimizer,
grant auditor, upstream steward, community builder, OSS/commercial parity reviewer, and
security/release gate.

## Questions deliberately left for experiments

- Which RAP tasks benefit from graph-shaped reasoning versus a conventional loop?
- When does a specialized judge outperform deterministic verification plus human review?
- Which prompt elements transfer across providers and which require overlays?
- How much parallel research improves evidence quality after accounting for token/cost growth?
- Can an Agent BOM remain complete when tools and connectors are discovered at runtime?
- Which Buzz extension can be upstreamed without imposing RAP semantics on Buzz?
- Is a stock Omarchy provisioning path more reproducible and supportable than a custom image?

Those questions are graph nodes, not assumptions embedded in product marketing.

