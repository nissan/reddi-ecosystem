# Agent Operating Contract

This repository is optimised for human-directed, agent-executed programme engineering.
Humans own intent, priorities, public claims, money, legal commitments, and irreversible
decisions. Agents research, propose, implement, test, audit, document, and surface gaps.

## Before acting

1. Read `README.md`, `planning/repositories.yaml`, `planning/milestones.yaml`, and
   the relevant node in `planning/graph.yaml`.
2. Follow canonical ownership. Never edit or restate an ADL semantic here; file it in
   `nissan/reddiagent-lab`. Never implement RAP protocol code here; target
   `nissan/reddi-agent-protocol`.
3. Verify dependencies are `done` or an approved human decision explicitly waived them.
4. Resolve the node's evidence, external-action, payment, custody, and upstream boundaries.
5. Claim exactly one executable node and record its expected file/repository footprint.

## Work loop

`frame -> inspect -> plan -> execute -> verify -> independent audit -> integrate -> retrospect`

Each loop must leave:

- an anchor issue or graph node;
- acceptance criteria and explicit non-goals;
- evidence produced by commands, tests, screenshots, traces, or primary sources;
- a Sync Log entry explaining divergence from the plan;
- newly discovered dependencies or follow-up nodes;
- a human decision request where judgment is consequential.

## Graph rules

- `planning/graph.yaml` is canonical; GitHub issues are projections plus collaboration state.
- A node has one parent epic, one target repository, typed dependencies, and a measurable gate.
- `blocked` means stop. Do not work around credentials, approvals, external coordination,
  mainnet gates, upstream consent, or ambiguous ownership.
- Parallel work is allowed only across declared non-overlapping repository/file footprints.
- Rebase before final verification. Prefer one readable history over merge bubbles.
- After every merged PR, revisit parent, blockers, dependents, milestone gate, and roadmap order.

## Research discipline

- Prefer papers, official engineering posts, specifications, repositories, model cards,
  and raw documentation.
- Grade confidence per claim. Record access date and an exact deep link.
- Never ship a quotation, identifier, field, version, benchmark, price, absence claim,
  or negative claim that was not checked against the primary artifact.
- Record limitations and contradictory evidence. `unknown` is an acceptable result.
- Research changes decisions only through an issue, ADR, experiment, or evaluated prompt update.

## Prompt and agent changes

Prompts are executable artifacts, not prose decoration.

- Every material prompt has a purpose, inputs, outputs, tool permissions, stop conditions,
  escalation conditions, eval set, baseline, and version.
- Never promote an automatically optimised prompt from training examples alone.
- Use held-out evaluation, safety/adversarial cases, cost and latency limits, and human review.
- Preserve provider neutrality. Provider-specific optimisations are overlays, not the base ADL.
- Store traces and scored outcomes; do not store hidden reasoning or secrets.

## Safety and money

- Default to fixture, dry-run, localnet, or devnet.
- No private key, seed phrase, bearer token, payment credential, or customer data enters this repo.
- No live payment, wallet signing, mainnet, custody, or external publication without a specific
  human-approved node and recorded evidence.
- Quattro plugins are unsandboxed UI code. They call a narrow local API and never read signer keys.
- Nostr events are not authoritative payment or settlement evidence.

## Upstream citizenship

Before carrying a downstream patch:

1. Search upstream discussions, issues, RFCs, and contribution rules.
2. Open a design discussion before a large change.
3. Prefer generic extension seams over Reddi-specific special cases.
4. Contribute fixes, tests, and documentation upstream where generally useful.
5. Maintain attribution, license notices, an upstream patch register, and a rebase budget.

## Completion gate

A node is not done because code exists. It is done only when acceptance checks pass,
independent review is complete, claims match evidence, graph state is updated, and any
upstream/community obligation is recorded.

## Maintaining this file

Keep this file for knowledge useful to almost every future agent session in this project.
Do not repeat what the codebase already shows; point to the authoritative file or command instead.
Prefer rewriting or pruning existing entries over appending new ones.
When updating this file, preserve this bar for all agents and keep entries concise.
