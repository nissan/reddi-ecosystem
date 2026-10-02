# Roadmap and BDD applicability catalog

**Applicability snapshot:** 2026-10-02 UTC  
**Authority:** `planning/graph.yaml` remains canonical for cross-repository completion dependencies. Component repositories remain canonical for their semantics and implementation. This catalog is a human-readable applicability, typed-dependency, and behavior view; it does not create a second execution graph.

## How to read this catalog

A merged pull request establishes that its change landed on its reported base branch. It does not by itself establish package publication, deployment, partner acceptance, grant acceptance, controlled-live readiness, production readiness, or mainnet safety.

Applicability classes are deliberately distinct:

| Class | Meaning |
|---|---|
| **delivered-executable** | A named interface or automated behavior exists on the component default branch. The cited executable checks, not this document, establish behavior. |
| **human-acceptance** | Legal, sponsor, operator, grantor, or partner judgment is required; automation can assemble evidence but cannot pass the gate. |
| **historical-superseded** | Retained regression, provenance, or design evidence that is not an active product contract or readiness claim. |
| **proposed** | Planned behavior. Its scenarios are acceptance targets, not implemented or passing tests. |
| **blocked** | Work must not proceed past the named prerequisite or approval. |

Scenario classes are **E** (executable), **H** (human/partner acceptance), and **M** (mixed executable evidence plus human judgment). Status and severity are independent: a critical-consequence live action remains blocked rather than becoming the next engineering task.

## Verified delivery reconciliation

Forge state and merge hashes below were read from the GitHub API through `gh-axi` on 2026-10-02 UTC.

| Outcome | Applicability | Current evidence | Boundary / missing behavior |
|---|---|---|---|
| Honest RAP Assurance positioning | delivered-executable for claim controls; older marketplace wording is historical-superseded | [RAP PR 654](https://github.com/nissan/reddi-agent-protocol/pull/654), merged to `main` as `084b06ca75a1cd1d1b2f5da569dc8a254b47f111` | No publication, deployment, payment, audit, or production claim follows. Historical BDD remains regression/provenance until classified by the RAP audit. |
| Browser-wallet Tier 1 preflight | delivered-executable, default-off and offline | [RAP PR 663](https://github.com/nissan/reddi-agent-protocol/pull/663), merged as `528ba83af5ec2a8aa8369a5dc7b1b9a745a0e4d4` | No wallet inspection, signing, RPC, transaction, validator, funding, official AUDD observation, or live enablement. Open maintenance issues [656](https://github.com/nissan/reddi-agent-protocol/issues/656)–[662](https://github.com/nissan/reddi-agent-protocol/issues/662) and [664](https://github.com/nissan/reddi-agent-protocol/issues/664) stay off the critical path absent a new critical/high finding. |
| Anchor v2 bounded comparison | delivered-executable alpha pilot | [RAP PR 671](https://github.com/nissan/reddi-agent-protocol/pull/671), merged as `3d34ce1286146deeed86892eafda77f8416c154c` | One default-off `update_agent` comparison is not adoption, full parity, audit evidence, deployment, or production readiness. Issues [665](https://github.com/nissan/reddi-agent-protocol/issues/665), [666](https://github.com/nissan/reddi-agent-protocol/issues/666), [667](https://github.com/nissan/reddi-agent-protocol/issues/667), [669](https://github.com/nissan/reddi-agent-protocol/issues/669), [670](https://github.com/nissan/reddi-agent-protocol/issues/670), and [672](https://github.com/nissan/reddi-agent-protocol/issues/672) are maintenance follow-ups. |
| Quasar retirement from current critical paths | delivered decision; retained artifacts are historical-superseded | [RAP PR 674](https://github.com/nissan/reddi-agent-protocol/pull/674), merged as `801d0d1cb980b25448f400d6290b006e77a7a33d` | Stable Anchor 1.1.2 is the current in-repository authority; Anchor v2 is alpha. Retained commands/workflows are not readiness. Issues [673](https://github.com/nissan/reddi-agent-protocol/issues/673), [675](https://github.com/nissan/reddi-agent-protocol/issues/675), [676](https://github.com/nissan/reddi-agent-protocol/issues/676), [677](https://github.com/nissan/reddi-agent-protocol/issues/677), and [678](https://github.com/nissan/reddi-agent-protocol/issues/678) complete retirement hygiene. |
| Arena playable dry-run and Devnet Assurance preview | delivered-executable, bounded/default-off | [Arena PR 96](https://github.com/nissan/reddi-arena/pull/96), merged as `2eb85056b643b6ee55c0be603ed73f9becee20b4` | The exact GitHub merge SHA is 40 hexadecimal characters; no longer value seen in interim notes is authoritative. No external enablement, official AUDD payment, wallet/signing, live value, production, or mainnet proof. Arena's generated five-phase roadmap is explicitly superseded by its README. |
| Canonical ADL v0.2 | delivered-executable specification/schema baseline | [`reddiagent-lab` canonical spec](https://github.com/nissan/reddiagent-lab/blob/main/specs/ADL-v0.2.md) and schema; component README names GitHub issues as planned-work authority | Agent BOM, portable overlays, and explicit authority contracts remain proposed. Arena findings [440](https://github.com/nissan/reddiagent-lab/issues/440), [443](https://github.com/nissan/reddiagent-lab/issues/443), [444](https://github.com/nissan/reddiagent-lab/issues/444), [445](https://github.com/nissan/reddiagent-lab/issues/445), [446](https://github.com/nissan/reddiagent-lab/issues/446), [450](https://github.com/nissan/reddiagent-lab/issues/450), and [451](https://github.com/nissan/reddiagent-lab/issues/451) were open when checked. |
| Solana/AUDD delivery and acceptance | proposed/blocked | RAP [issue 615](https://github.com/nissan/reddi-agent-protocol/issues/615) and [issue 621](https://github.com/nissan/reddi-agent-protocol/issues/621) were open; [readiness PR 646](https://github.com/nissan/reddi-agent-protocol/pull/646) remained open and reported four blocking gates | Fixture/program delivery, package publication, deployment, eligible activity, partner acceptance, grant acceptance, and production readiness are separate. No recent merge closes the governing-evidence or approval gates. |

The verified component authorities are unchanged: ADL semantics belong to `nissan/reddiagent-lab`; RAP implementation, receipts, adapters, and Solana evidence belong to `nissan/reddi-agent-protocol`; Arena rules and implementation belong to `nissan/reddi-arena`; this repository owns only the cross-repository graph and portfolio evidence.

## Outcome swimlanes

| Lane | Outcome | Accountable role(s) | Current state | Completion condition |
|---|---|---|---|---|
| **SL-TRUTH** | Obligations and claims are reconciled against governing and partner evidence. | programme lead; grant auditor; evidence lead; legal/partner approver | P0; governing evidence incomplete | Every material promise has source, environment, evidence, gap, owner, status, and approved disposition. Private correspondence is represented only by approved derived facts. |
| **SL-ASSURE** | Paid-work evidence is replayable above replaceable payment rails. | RAP protocol steward; payments lead; receipt/evidence lead | P0; read-only RAP gap audit may start under an audit-only waiver (`ECO-001` unmet); ECO-040 completion and contract freeze stay blocked | Leakage/readiness audit, normalized adapter, Solana/AUDD fixture/devnet implementation, versioned events, receipt verifier, and refusal/reconciliation/redaction evidence satisfy their graph nodes. |
| **SL-PORT** | Agent identity, dependencies, budgets, and human authority stay portable and inspectable. | ADL specification, tooling, and authority stewards | P0; read-only ADL gap audit may start under an audit-only waiver (`ECO-020` unmet); ECO-030 completion stays blocked | Canonical ADL dispositions, Agent BOM, overlays, authority semantics, and conformance evidence land in ADL Lab. |
| **SL-PROVE** | Outcomes can be deterministically reproduced and independently audited without irreversible actions. | Arena maintainer; evaluation/reliability/safety leads | bounded preview delivered; full replay proposed | Canonical ADL import, versioned evaluation bundle, read-only replay/audit, adversarial tracks, and structured upstream findings pass in Arena. |
| **SL-SAFE** | Experimental/test surfaces remain default-off, truthful, and maintainable. | RAP safety/toolchain maintainers | delivered baseline plus P2/P3 maintenance | Browser, Anchor, and Quasar follow-ups are triaged against current `main`; critical/high defects block the affected delivery, while medium/low defects remain linked backlog tickets. |
| **SL-EXPERIENCE** | Contributors can understand assurance using no-spend paths. | Arena product/DX lead; contributor steward | dry-run and local preview delivered; promotion gated | Clean quickstart, receipt/tamper/replay examples, accessibility evidence, and publication approval exist. This does not imply grant/live acceptance. |
| **SL-INTEGRATE** | Proven contracts project into Buzz, Quattro, and Lighthouse without semantic forks. | Buzz, Linux security/packaging, and Lighthouse leads | proposed and downstream-blocked | Relevant M2 contracts and evidence complete before sidecar, keyless local API, package, or hosted work claims readiness. |
| **SL-LIVE** | Real value/users are permitted only within explicit authority and support boundaries. | programme sponsor; security/legal/operator/partner authorities | blocked | Preparation pack is complete, then a separate action-specific execution approval names asset, environment, cap, expiry, monitoring, and rollback. No global authorization is inferred. |

## Typed dependency tree

Type legend: **HT** hard technical prerequisite; **EV** evidence prerequisite; **EX** external party/source prerequisite; **AP** human approval prerequisite; **RS** recommended sequencing only. `planning/graph.yaml` remains the completion-DAG authority. Every node ID in the **Blocked by** and **Unlocks** columns is an exact `dependsOn` edge from that graph, shown with its 2026-10-02 status when unmet. Entries labelled **audit-only waiver**, **proposed**, or **RS** are not graph edges. This view explains prerequisite semantics and does not turn chronology into a technical edge.

| Item | Completion condition | Blocked by | Unlocks |
|---|---|---|---|
| **P0-APP** roadmap/BDD applicability refresh ([ECO-014 issue](https://github.com/nissan/reddi-ecosystem/issues/14)) | Current delivery, historical coverage, proposals, issue links, typed prerequisites, and Quasar status are reconciled without changing component semantics. | Graph: `ECO-004` (planned), `ECO-012` (planned), `ECO-013` (planned), all unmet. Captain waiver covers only this bounded applicability refresh, not ECO-014 completion. Current forge/component evidence (**EV**). | Graph: `ECO-015`. Clear prioritization for all lanes (**RS**); no technical or live unlock. |
| **P0-RAP-AUDIT** RAP readiness/leakage audit (`ECO-040`) | Findings classify core semantics, adapter leakage, migration debt, and explicit non-goals, with canonical RAP owners. | Graph: `ECO-001` (in-progress, unmet). **Audit-only waiver:** the Captain allowed only the read-only gap audit to start before `ECO-001` is done. The waiver does not cover ECO-040 completion, contract freeze, acceptance, or implementation. Governing facts are still required for final obligation binding (**EV**). | Graph: `ECO-041`, `ECO-044`, `ECO-060`, `ECO-110`. All stay blocked until ECO-040 itself is done. |
| **P0-ADL-AUDIT** ADL portability/authority audit (`ECO-030`) | Each gap is existing semantics, profile/extension, canonical proposal, or non-ADL concern. | Graph: `ECO-020` (in-progress, unmet). **Audit-only waiver:** the Captain allowed only the read-only gap audit to start before `ECO-020` is done. The waiver does not cover ECO-030 completion, contract freeze, acceptance, or implementation. | Graph: `ECO-031`, `ECO-032`, `ECO-033`, `ECO-034`, `ECO-050`, `ECO-060`. All stay blocked until ECO-030 itself is done. |
| **T1-GOV** governing-source and obligation reconciliation (`ECO-000`–`ECO-004`) | Every obligation has governing text or `unknown`, exact evidence/gap, owner, and review. | Graph: `ECO-002` needs `ECO-000`, `ECO-001`; `ECO-003` needs `ECO-001`; `ECO-004` needs `ECO-000`, `ECO-002`, `ECO-003`. Official and partner sources (**EX/EV**); Workspace evidence only where necessary (**EV**). | Graph: `ECO-005`, `ECO-014`, `ECO-042`, `ECO-046`, `ECO-104` (from `ECO-004`); `ECO-040` (from `ECO-001`); `ECO-042` (from `ECO-003`). Human dispositions and exact AUDD acceptance scope (**EV**). |
| **T1-GMAIL** Workspace correspondence route (no graph node) | A supported read-only tool is selected; later, human OAuth identifies `nissan@redditech.com.au` and complete relevant threads can be reviewed without mutation. | Tool selection (**HT**); human sign-in/admin consent (**AP**). | Additional governing evidence (**EV**). Personal Gmail is **RS** only and is not required for AUDD review. |
| **T1-DISPOSITION** remediation/communication decision (`ECO-005`) | Each material gap is approved to prove, remediate, renegotiate, disclose, or retire. | Graph: `ECO-004` (planned, unmet). Legal/grantor authority (**AP/EX**). | Graph: `ECO-046`, `ECO-047`. Communication only under its own approval. |
| **T2-CONTRACT** normalized RAP adapter/authority/events/receipt contracts (`ECO-041`, `ECO-044`, `ECO-045`) | Versioned interfaces, deterministic fake adapter, authority negatives, replay semantics, and migration plan exist. | Graph: `ECO-041` needs `ECO-040` and `ECO-034` (ADL authority); `ECO-044` needs `ECO-040`; `ECO-045` needs `ECO-041`, `ECO-044`. The audit-only waivers do not apply here. | Graph: `ECO-042`, `ECO-046`, `ECO-053`, `ECO-090` (from `ECO-041`); `ECO-052`, `ECO-061` (from `ECO-044`); `ECO-046`, `ECO-051`, `ECO-090`, `ECO-092`, `ECO-114` (from `ECO-045`). |
| **T3-AUDD** Solana/AUDD first implementation (`ECO-042`) | SPL mint/token-account/account-layout/mirror work and fixture/devnet positive/negative/reconciliation/redaction evidence pass, with no live claim. | Graph: `ECO-003` (identity registry), `ECO-004` (governing evidence), `ECO-041` (adapter contract). | Graph: `ECO-046`. Replay fixture evidence (**proposed**, see T3-REPLAY). |
| **T3-REPLAY** Arena replay/read-only audit (`ECO-051`, `ECO-052`) | Versioned bundles produce criterion-level pass/fail/unknown and reject tamper, absence, order, version, and authority failures. | Graph: `ECO-051` needs `ECO-033`, `ECO-045`, `ECO-050`; `ECO-052` needs `ECO-044`, `ECO-051`. **Proposed:** an integration join with T3-AUDD fixtures. | Graph: `ECO-052`, `ECO-053`, `ECO-054`, `ECO-063` (from `ECO-051`); `ECO-047`, `ECO-054`, `ECO-055`, `ECO-103` (from `ECO-052`). **Proposed:** replay evidence feeding ECO-046 (**RS**, not a graph edge). |
| **T4-AUDD-DELIVERY** reconcile RAP 615–630 (`ECO-046`) | Every governing criterion has the named implementation/evidence artifact or an owned gap; implementation and acceptance remain separate. | Graph: `ECO-004`, `ECO-005`, `ECO-041`, `ECO-042`, `ECO-045`. **Proposed:** replay evidence from T3-REPLAY (**RS**); the graph has no `ECO-051`/`ECO-052` edge here. | Graph: `ECO-047`, `ECO-115`. |
| **T4-BINDER** Superteam/AUDD binder (`ECO-047`) | Privacy-safe binder maps obligations to versions, environments, artifacts, reviews, gaps, owners, and partner disposition. | Graph: `ECO-005`, `ECO-046`, `ECO-052` (replay/read-only audit). Partner/legal acceptance where required (**EX/AP**). | Graph: `ECO-043`, `ECO-060`. No live authorization. |
| **T5-LIVE-PREP** controlled-live exception preparation (no single graph node) | Governing alignment, accepted asset/environment, caps/authorities, RPC, audit, legal/operator/partner evidence, monitoring, rollback, and privacy controls are assembled. | T1-GOV and T4-BINDER (**EV/EX**); security/legal/operator/partner inputs (**EX/AP**). | One action-specific execution decision (**AP**) only. |
| **T5-LIVE-EXEC** any signing, deployment, transaction, or live/mainnet/value-bearing action (no single graph node) | The exact action has final scoped approval and all preparation evidence remains current. | T5-LIVE-PREP (**EV**); explicit action approval (**AP**). | Only the named action and resulting evidence. It does not establish grant or production acceptance. |

`P0-APP` and the read-only gap-audit portions of `P0-RAP-AUDIT` and `P0-ADL-AUDIT` can run in parallel under the bounded Captain waivers above. Initial audit findings are inputs only. `ECO-040` and `ECO-030` stay `planned` in the graph until `ECO-001` and `ECO-020` are done and their own acceptance passes, and nothing they unlock starts early. Gmail tool selection is queued/deferred; no connection is part of this plan increment. Controlled-live preparation and execution are separate gates.

## Prioritized phased execution

### Phase 0 — reconcile applicability and start bounded audits

Parallel work IDs: `redditech-roadmap-bdd-refresh`, `rap-assurance-readiness-gap-audit`, and `adl-authority-portability-gap-audit`.

- Refresh verified current applicability now; later RAP/ADL audit findings join through a follow-up graph review rather than blocking this refresh.
- Permit only the read-only gap-audit portions of `ECO-040` and `ECO-030` to start against current component authority, under the Captain's audit-only waiver of their unmet `ECO-001` and `ECO-020` edges. Do not wait for private correspondence to identify architectural leakage or portability gaps. Node completion still requires those dependencies.
- Queue Gmail tool selection only. Do not connect email or treat personal Gmail as an AUDD prerequisite.
- Completion: this catalog and roadmap agree with current forge/component evidence; audits have canonical owners and explicit join points; no component semantics, graph dependency, or live state changed.

### Phase 1 — recover and decide obligation truth

- Complete `ECO-000`–`ECO-004`; use Workspace correspondence only after tool selection and human consent where public/governing sources are insufficient.
- Obtain `ECO-005` dispositions from the responsible human/external authorities.
- Completion: obligations are verified, partial, blocked, or unknown with sources and owners; no proposal is presented as acceptance.

### Phase 2 — freeze portable assurance contracts

- Complete RAP audit/adapter/events/receipts and ADL portability/BOM/overlay/authority classifications in their canonical repositories.
- Join the independent audit streams only where a frozen contract actually requires both.
- Completion: versioned contracts, deterministic fixtures, malicious authority negatives, migration plan, and canonical issue dispositions exist.

### Phase 3 — implement Solana/AUDD and replay proof

- Implement the actual SPL/account-layout path before the audit that must cover it.
- Integrate normalized receipt evidence with Arena replay/read-only audit on exact versions and digests.
- Completion: fixture/devnet happy and refusal paths pass and produce environment-scoped evidence; no live, package, deployment, partner, or production claim is inferred.

### Phase 4 — package acceptance evidence, then broaden proof

- Reconcile RAP issues 615–630 and assemble the independent, privacy-safe binder.
- Only after the approved Solana/AUDD-first sequence, schedule a materially different no-spend comparison fixture and downstream Buzz work.
- Completion: each criterion has accepted evidence or an explicit owned gap/disposition. Public communication still needs its own approval.

### Maintenance queue

- Browser issues 656–662/664, Anchor issues 665–667/669/670/672, and Quasar issues 673/675–678 remain separately ticketed.
- Reconcile each ticket against current final `main` immediately before implementation. Critical/high evidence blocks the affected delivery; medium/low findings remain separate issue-backed follow-ups and do not silently consume critical-path capacity.

## BDD story and scenario catalog

Unless a scenario cites delivered executable behavior above, it is **proposed** and must not be reported as implemented or passing. Human scenarios are acceptance procedures, not automatable assertions.

### ST-01 — Truthful obligation state

**As a programme sponsor, I want to maintain an evidence-backed obligation register, so that remediation and grant statements never outrun governing facts.**

- **SC-01A [M, proposed]:** Given governing sources, repository evidence, and acceptance authority are identified, When an obligation is reconciled, Then its promise, date, environment, evidence, gap, owner, and status have privacy-safe citations.
- **SC-01B [E, proposed]:** Given an obligation lacks governing or acceptance evidence, When its status is calculated, Then it remains `unknown`, `partial`, or `blocked` rather than becoming `done` from an issue or pull request.
- **SC-01C [E, proposed]:** Given implementation is merged but publication, deployment, or partner acceptance is absent, When status is rendered, Then those states remain separate.

### ST-02 — Read-only governing correspondence

**As a grant auditor, I want to review Workspace AUDD correspondence through a named read-only identity, so that governing facts can be verified without altering mail or mixing accounts.**

- **SC-02A [M, proposed/deferred]:** Given a supported tool and human-approved `nissan@redditech.com.au` OAuth session, When complete official threads and attachments are reviewed, Then dates, senders, provenance, extracted facts, and unknowns are recorded privately.
- **SC-02B [E, proposed]:** Given the account is personal, implicit, unverified, or cannot retrieve complete threads read-only, When AUDD review is requested, Then the workflow refuses and names the Workspace prerequisite.
- **SC-02C [M, proposed]:** Given a message proposes a requirement without accepted authority, When it is classified, Then it remains proposal or unknown rather than binding acceptance.

### ST-03 — Rail-neutral assurance

**As a paid-work integrator, I want to use a versioned rail-neutral assurance contract, so that RAP can bind work evidence without pretending to be the payment rail.**

- **SC-03A [E, proposed]:** Given a deterministic adapter fixture, When quote, authorize, submit, observe, settle, refund-or-reverse, reconcile, and redact run, Then normalized records and a verifiable receipt are emitted with namespaced rail fields.
- **SC-03B [E, proposed]:** Given wrong asset, network, payee, amount, expiry, duplicate, partial result, or unsupported refund, When verification runs, Then it fails closed with no settlement-success claim.
- **SC-03C [E, proposed]:** Given transfer proof lacks work evidence, When RAP Assurance evaluates the job, Then payment is not reported as proof that work succeeded.

### ST-04 — Solana/AUDD first implementation

**As a Solana/AUDD acceptance reviewer, I want to evaluate an AUDD-on-Solana adapter in bounded fixture and devnet modes, so that obligation evidence tests actual asset semantics without unauthorized live value.**

- **SC-04A [E, proposed]:** Given canonical environment, mint, token-program, decimals, payee, and authority fixture data, When a valid bounded transfer and work evidence are observed, Then environment-scoped normalized evidence and a receipt are emitted.
- **SC-04B [E, proposed]:** Given mainnet, an unapproved mint, wrong account/PDA layout, replay, or missing approval, When the path is invoked, Then it refuses before signing or submission.
- **SC-04C [E, proposed]:** Given fixture or unverified devnet evidence, When it is exported, Then it cannot claim official AUDD observation, eligible grant activity, controlled-live settlement, or production readiness.

### ST-05 — Replayable independent audit

**As a third-party auditor, I want to replay versioned job, evidence, judgment, and receipt bundles, so that I can verify outcomes without rerunning paid or irreversible actions.**

- **SC-05A [E, proposed]:** Given a complete versioned bundle, When read-only replay runs, Then every criterion returns pass, fail, or unknown with deterministic artifact and digest references.
- **SC-05B [E, proposed]:** Given evidence is missing, altered, out of order, replayed, stale, wrong-environment, or version-incompatible, When replay runs, Then the exact failure is reported without mutating evidence.
- **SC-05C [E, proposed]:** Given a provider or dependency is unavailable, When a criterion cannot be reproduced, Then the result is `unknown` rather than a fabricated pass or fail.

### ST-06 — Default-off browser preparation

**As a development operator, I want to run a bounded default-off browser-wallet preflight, so that a future manual test is constrained before a signer or network can be reached.**

- **SC-06A [E, delivered baseline]:** Given the PR 663 offline contract and preconditions, When deterministic preflight checks run through their component-owned interfaces, Then no signing, RPC, transaction, or wallet access is required.
- **SC-06B [E, proposed hardening]:** Given approval is expired, overlong, reused, endpoint-mismatched, or mainnet-ambiguous, When preflight runs, Then it refuses before signer or network access.
- **SC-06C [E, proposed hardening]:** Given fixture-only transfer data, When evidence copy is produced, Then it cannot be represented as observed official settlement.

### ST-07 — Honest Anchor v2 comparison

**As a protocol maintainer, I want to reproduce a bounded Anchor v2 comparison against the stable reference, so that adoption decisions use symmetric evidence rather than alpha enthusiasm.**

- **SC-07A [E, delivered baseline]:** Given PR 671's isolated default-off pilot, When its component-owned comparison checks run, Then evidence remains scoped to one `update_agent` comparison against stable Anchor 1.1.2.
- **SC-07B [E, proposed hardening]:** Given locked dependencies and symmetric feature profiles, When stable and alpha builds/tests run, Then exact artifacts, state, metadata, sizes, and compute evidence are reproducible.
- **SC-07C [E, proposed hardening]:** Given asymmetric or incomplete coverage, When results render, Then the limitation is explicit and no parity, audit, adoption, or production claim is emitted.

### ST-08 — Quasar historical boundary

**As a protocol operator, I want to isolate frozen Quasar surfaces as unmistakably historical, so that retained evidence cannot be mistaken for a supported deployment path.**

- **SC-08A [E, delivered policy]:** Given PR 674's freeze, When current product authority is resolved, Then stable Anchor 1.1.2 is authoritative, Anchor v2 is alpha, and Quasar is excluded from product and production critical paths.
- **SC-08B [E, proposed hardening]:** Given a normal product command attempts to select Quasar or a stale deployment, When it resolves its target, Then it fails before signer, RPC, or instruction construction.
- **SC-08C [M, proposed hardening]:** Given historical benchmark or deployment material, When it is shown to a reviewer, Then provenance, limitations, and superseded status are visible and a passing regression does not imply readiness.

### ST-09 — Portable agent authority

**As a deployment operator, I want to inspect dependencies, budgets, and human authority in ADL profiles, so that deployment projections cannot silently grant payment, signing, or publication power.**

- **SC-09A [E, proposed]:** Given a canonical ADL definition and deployment overlay, When effective authority and Agent BOM are generated, Then dependencies, permissions, budgets, expiry, approval, and provenance are deterministic.
- **SC-09B [E, proposed]:** Given an overlay adds keys, unlimited spend, self-approval, or a forbidden capability, When validation runs, Then conformance rejects it with an actionable path.
- **SC-09C [E, proposed]:** Given provider/runtime differences, When conformance compares them, Then differences appear as declared capability evidence rather than hidden semantic branches.

### ST-10 — Controlled-live governance

**As a production sponsor, I want to separate controlled-live preparation and execution with explicit gates, so that technical readiness never self-authorizes real value or public claims.**

- **SC-10A [H, proposed/blocked]:** Given governing alignment, accepted asset and environment, authorities and caps, RPC, audit, legal/operator/evidence/partner acceptance, and a reviewed exception pack, When one exact action is evaluated, Then any approval names scope, expiry, monitoring, and rollback.
- **SC-10B [E, proposed/blocked]:** Given any required input or explicit action approval is absent, When live execution is requested, Then execution remains blocked and no wallet, signing, transaction, or deployment occurs.
- **SC-10C [H, proposed/blocked]:** Given a controlled-live action succeeds technically, When grant or production claims are considered, Then those claims remain pending until the named acceptance authority accepts the evidence.

## Story traceability

| Stories | Canonical graph/issues | Delivered interfaces/evidence | Remaining completion evidence |
|---|---|---|---|
| ST-01, ST-02 | `ECO-000`–`ECO-005`; ecosystem issues [4](https://github.com/nissan/reddi-ecosystem/issues/4), [5](https://github.com/nissan/reddi-ecosystem/issues/5), [6](https://github.com/nissan/reddi-ecosystem/issues/6), [7](https://github.com/nissan/reddi-ecosystem/issues/7), [8](https://github.com/nissan/reddi-ecosystem/issues/8), and [9](https://github.com/nissan/reddi-ecosystem/issues/9) were open when checked | ECO-001 public snapshot only; no email work in this increment | Governing-source hashes/register, discrepancy ledger, second-person review, human dispositions, privacy approval. |
| ST-03 | `ECO-040`, `ECO-041`, `ECO-044`, `ECO-045`; RAP [issue 338](https://github.com/nissan/reddi-agent-protocol/issues/338) | Claim boundary in PR 654; current local/no-spend package surfaces are component evidence, not acceptance | Audit, interface/ADR, deterministic suite, receipt vectors, replay/tamper/redaction tests. |
| ST-04 | `ECO-042`, `ECO-046`; RAP [issue 621](https://github.com/nissan/reddi-agent-protocol/issues/621) | Guardrails in PR 663 and Arena PR 96 | SPL layout/mirror record, fixture/devnet conformance, negative/reconciliation/redaction evidence, applicable independent audit. |
| ST-05 | `ECO-045`, `ECO-051`, `ECO-052`, `ECO-053` | Arena dry-run and bounded preview | Versioned replay bundle, read-only audit report, tamper/absence/order/version/unavailable-provider negatives. |
| ST-06 | RAP issues 656–662 and 664 | RAP PR 663 | Focused offline public-interface tests for each ticket; no broad signing/network validation. |
| ST-07 | RAP issues 665–667, 669, 670, 672 | RAP PR 671 | Locked build/IDL evidence, exact state and invalid-path tests, symmetric profile report, immutable CI provenance. |
| ST-08 | RAP issues 673, 675–678 | RAP PR 674 | Command/workflow inventory, offline refusal checks, terminology and provenance review. |
| ST-09 | `ECO-030`–`ECO-035`; ADL issues 440, 443–446, 450, 451 | Canonical ADL v0.2 spec/schema/examples | Canonical dispositions, positive/malicious overlays, BOM vectors, authority and cross-runtime conformance. |
| ST-10 | `ECO-047`, `ECO-111`, `ECO-114`, `ECO-115` | Approval boundaries only | Scoped signed decision, audit/security/legal/operator/partner evidence, monitored rehearsal, rollback and incident evidence. |

## Severity versus delivery priority

| Risk/work | Severity if wrong | Delivery priority now |
|---|---|---|
| Missing or ambiguous governing AUDD evidence | High claim/evidence risk | **P0** critical path |
| RAP adapter/authority/receipt contracts | High architecture and financial-integrity risk | **P0** audit now; freeze after audit join |
| Solana/AUDD SPL implementation and refusal paths | High if used for value | **P0** after evidence/contract prerequisites |
| Replay/read-only audit | High evidence-integrity risk | **P0** join gate |
| Ungated live execution | Critical | **Blocked**, not authorized work |
| Browser, Anchor, and Quasar deferred findings | Currently medium/low based on bounded/default-off posture | **P2/P3** issue-backed maintenance; re-triage before work |

A newly verified critical/high defect blocks the affected delivery. Medium/low findings require exact issue URLs and remain separate backlog follow-ups; they are not silently folded into this planning delivery.

## Explicit non-goals and follow-up join

This refresh does not connect email, communicate with a partner, publish a package, deploy software, inspect or create keys, sign, submit a transaction, activate a live path, claim grant acceptance, or declare production readiness. It does not rewrite ADL, RAP, or Arena semantics.

When the parallel RAP and ADL audits complete, perform one follow-up graph review to import verified blockers, canonical issue links, and contract join points. Do not convert audit chronology into hard dependencies. If either audit discovers a real semantic prerequisite that invalidates this catalog, stop the dependent work and amend the canonical graph through normal review.
