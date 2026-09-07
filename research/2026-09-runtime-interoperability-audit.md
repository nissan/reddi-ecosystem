# Runtime interoperability audit: OpenClaw, Firstmate, Hermes, and Buzz

- Snapshot date: 2026-09-07
- Graph owner: ECO-026
- Scope: primary-source architecture and integration-seam audit
- Execution status: source checkouts inspected; adapters and conformance runs not yet implemented

## Immutable source baseline

| Upstream | Audit baseline | Commit | Release policy implication |
|---|---|---|---|
| OpenClaw | `v2026.7.1-2` | `0790d9f593ad30c940ed93b5872a8cf6d6f3cf8c` | Use a stable calendar tag; never use “2.0” as a machine compatibility identifier |
| Firstmate | `main` snapshot | `6d396da7c43f03315873332b2591119a8c780a97` | No stable release was established; pin the full commit and expire results on revision change |
| Hermes Agent | `v2026.8.31` / v0.21.0 | `29112bef099274229cadff79cdff7bf7b99c4b77` | Pin the stable tag and record known packaging/tool limitations separately |
| Buzz Desktop | `desktop-v0.5.22` | `9ceb1f79bbc21785a0a075c40aecb3c058b1ea15` | Pre-1.0/main-first security support requires upgrade smoke tests and a pinned tag/main observation |

These revisions are research baselines, not supported versions. Support requires an adapter run
under ECO-049/ECO-057 and an Arena result under ECO-058.

## System-role classification

| System | Primary role | Native coordination | Durable state | Isolation reality | Best Reddi seam |
|---|---|---|---|---|---|
| OpenClaw | Self-hosted agent Gateway/runtime | Multi-agent routing, sessions, subagents, channels, cron/webhooks | Workspace, sessions, memory, config, Gateway state | Main tools default to host; non-main sessions can use configured sandboxes | Gateway/plugin adapter plus ADL deployment overlay |
| Firstmate | Coding-crew agent distribution | First mate supervises crewmates/secondmates | Disk plus visible backend/task metadata | Git worktrees reduce collisions but are not general OS isolation | Task-intake/delivery adapter and engineering-process pilot |
| Hermes | Persistent learning-agent runtime | Bot Mode, profiles, gateways, subagents, A2A | Per-profile config, memory, sessions, skills, cron, state | Profiles isolate Hermes state, not host filesystem permissions | Profile/gateway/plugin adapter plus explicit sandbox backend |
| Buzz | Human/agent collaboration workspace | Rooms, signed Nostr events, workflows, ACP agents | Relay/community event log, project and workflow state | Community/identity scopes; execution depends on ACP/provider boundary | Sidecar/ACP/MCP lifecycle hooks and ADL/RAP projection |

## Common adapter-operation fit

**Native** means a documented direct seam; **derived** means stable observable state must be
normalized; **gap** requires adapter or upstream work; **N/A** is deliberately outside the role.

| Operation | OpenClaw | Firstmate | Hermes | Buzz |
|---|---|---|---|---|
| `discover` | derived from configured agents/plugins | derived from harness/backends | derived from profiles/descriptions | native agent/profile/community discovery |
| `prepare` | native config/tool/sandbox inspection; effective permission check derived | native project/mode/backend intake; OS authority is a gap | native profile/tool/backend config; effective permission check derived | native membership/workflow/agent config; economic preparation N/A |
| `dispatch` | native Gateway/session/subagent seams | native spawn/intake lifecycle | native profile/gateway/subagent/Bot routing | native workflow/ACP invocation or sidecar command |
| `observe` | native session/tool/task state; normalized evidence gap | native task metadata, watcher state, worktree/PR outcomes | native session/gateway/subagent state; normalized evidence gap | native signed events/workflow state; settlement truth external |
| `message` | native session messaging/steering | native agent-control/supervision | native Bot/group/gateway and subagent steering | native rooms, threads, mentions, DMs |
| `cancel` | controls exist; semantics require tests | stop/recovery paths require mapping | cancellation requires version tests | workflow/agent cancellation remains a test target |
| `collect` | derived from transcript, artifacts and harness result | native PR/merge/report shapes | derived from session/tool outputs | native event/file/git references; evidence should be content-addressed |
| `verify` | plugin/tool/harness checks; authority external | strong PR/test/review seam; verifier external | skills/tools/A2A possible; verifier external | approvals/hooks observable, not economic truth |
| `attest` | gap: deterministic signer outside model text | gap: bind task/worktree/PR evidence | gap: bind profile/session evidence | signatures attest authorship/intent, not execution/settlement |
| `settle` | N/A; RAP/payment adapter owns | N/A | N/A | N/A; project signed RAP observation only |
| `recover` | restart surfaces exist; correlation/replay tests required | strong reconciliation claim; test pinned revision | persistent state exists; test interrupted work/duplicate delivery | event replay exists; workflow/sidecar idempotency requires tests |

## Identity and evidence lineage

The portable evidence chain is:

`RAP job → adapter → runtime instance → agent → parent task/session → delegated task/session → harness/model → tool → artifact → verifier → settlement observation → receipt`

No runtime may collapse this into a self-asserted “agent completed” field. Evidence records
identifiers and digests when available, explicit `unknown` otherwise, and never stores secrets or
hidden reasoning.

- OpenClaw Gateway identity is not automatically every configured agent's economic identity.
  An embedded Codex harness may own continuation/compaction while OpenClaw owns channel,
  approval, dynamic-tool, and transcript projection state.
- Firstmate's first mate and crewmates are execution roles, not RAP buyer/seller/judge identities.
  Branches, worktrees, PRs, and reports are evidence references, not settlement authority.
- Hermes profiles provide separate Hermes homes and durable personas but do not enforce host
  filesystem boundaries. Shared memory is an explicit external dependency and policy.
- Buzz Nostr keys provide authorship/community identity. Signed events remain intent or
  observation until runtime, verifier, and payment evidence is bound.

## Derived canonical work

- ECO-036 adds the ADL runtime execution profile: capabilities, version constraints, tools,
  skills/plugins, harness, isolation, delegation, budgets, memory policy, approvals, cancellation,
  recovery, evidence, and attestation. Vendor configuration remains an overlay visible in Agent BOM.
- ECO-048 defines RAP adapter operations, normalized errors/idempotency and a deterministic mock.
- ECO-049 validates OpenClaw first because it is already used in the local Reddi operating lab;
  this is validation convenience, not protocol preference.
- ECO-057 validates contrasting Firstmate coding-delivery and Hermes durable-agent profiles.
- ECO-058 makes Arena the owner of published compatibility levels and canonical scenarios.
- ECO-076 prevents Quattro packaging from outrunning adapter conformance.

## Arena compatibility levels

| Level | Required proof |
|---|---|
| L0 Describe | Parse projection and expose capability/version/authority metadata |
| L1 Execute | Accept a fixture job and return bounded artifacts |
| L2 Observe | Stream normalized lifecycle/evidence with lineage |
| L3 Verify | Support external judgment without self-approval |
| L4 Settle | Bind verified outcome to fixture/devnet settlement/refund/receipt |
| L5 Recover | Reconcile interruption, duplicates, version drift and restart without double action |

## Risks and mandatory negative evidence

| Risk | Required test |
|---|---|
| Prompt/skill claims authority | Denial against coded approval and signer boundary |
| Profile/worktree/session mistaken for sandbox | Effective-permission probe and hostile cross-boundary fixture |
| Restart repeats action/payment | Idempotency and crash-at-each-transition replay |
| Private memory enters public receipt | Canary/redaction test across profile, transcript and evidence exporter |
| Harness differs from reported runtime | Layered provenance assertion and missing-field failure |
| Upstream silently changes semantics | Pin/digest mismatch failure and expired compatibility record |
| Buzz event treated as settlement truth | Conflicting Nostr/payment observation resolved by authoritative adapter |
| Agent self-verifies or judge colludes | Independent verifier authority and adversarial Arena track |

## Compatibility status

| System | Status | Highest justified level | Reason |
|---|---|---|---|
| OpenClaw | planned reference adapter | none | Source seam mapped; no RAP adapter execution |
| Firstmate | planned adapter/process pilot | none | No RAP task/evidence binding execution |
| Hermes | planned reference adapter | none | No isolated profile/gateway execution |
| Buzz | explicit M3 integration target | none | Sidecar proof remains blocked on M2 |

The audit is ready for independent review, but ECO-026 remains `in-progress` until a reviewer
confirms the source mapping, graph split, non-claims, and dependency correctness. No fork,
upstream contact, live payment, or external compatibility claim is authorized.
