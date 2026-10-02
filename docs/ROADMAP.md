# End-to-end programme roadmap

Planning baseline: 2026-08-26; sequencing refresh: 2026-08-31; applicability refresh: 2026-10-02. Dates are planning targets, not grantor-approved deadline
changes or public delivery promises. The canonical milestone gates are in
`planning/milestones.yaml`; the canonical executable backlog is `planning/graph.yaml`.
[`ROADMAP-BDD-APPLICABILITY.md`](ROADMAP-BDD-APPLICABILITY.md) is the current behavior,
typed-prerequisite, swimlane, and issue-traceability view. It does not replace the graph.

## Current applicability and immediate execution

Recent component delivery narrows the active plan without completing its acceptance gates:

- RAP claim remediation, default-off browser preflight, the bounded Anchor v2 pilot, and
  the Quasar experimental freeze landed in
  [PR 654](https://github.com/nissan/reddi-agent-protocol/pull/654),
  [PR 663](https://github.com/nissan/reddi-agent-protocol/pull/663),
  [PR 671](https://github.com/nissan/reddi-agent-protocol/pull/671), and
  [PR 674](https://github.com/nissan/reddi-agent-protocol/pull/674).
- Arena's default-off Devnet Assurance preview landed in
  [PR 96](https://github.com/nissan/reddi-arena/pull/96). Its exact merge commit is
  `2eb85056b643b6ee55c0be603ed73f9becee20b4`; it is fixture-backed preview evidence,
  not live, partner-accepted, or production evidence.
- Quasar is historical experimental evidence and is no longer on a product, production,
  deployment, audit, or mainnet critical path. Its retained deployment registry and
  regression surfaces remain relevant to identity/provenance reconciliation only.
- Governing AUDD evidence, remediation decisions, actual Solana/AUDD SPL implementation,
  replayable acceptance evidence, and human/partner approvals remain incomplete.

Phase 0 runs three bounded streams in parallel: this roadmap/BDD applicability refresh,
RAP readiness/leakage audit, and ADL authority/portability audit. The audits can start
against current component authority; their final contract findings join later. Gmail tool
selection remains queued/deferred, and no email connection is required for these public
repository audits. Controlled-live preparation remains separate from execution, and neither
is authorized by this plan.

## Critical path

```mermaid
flowchart LR
  M0["M0 Evidence recovery\n11 Sep 2026"] --> M1["M1 Programme baseline\n25 Sep 2026"]
  M1 --> M2["M2 ADL/RAP/Arena convergence\n30 Oct 2026 (un-rebaselined)"]
  M2 --> M3["M3 Arena for Buzz proof\n11 Dec 2026"]
  M3 --> M4["M4 Quattro Pack alpha\n29 Jan 2027"]
  M4 --> M5["M5 Reddi Machine preview\n26 Mar 2027"]
  M2 --> M6["M6 Lighthouse alpha\n30 Apr 2027"]
  M3 --> M6
  M3 --> M7["M7 Community Season Zero\n25 Jun 2027"]
  M4 --> M7
  M6 --> M7
  M5 --> M8["M8 Production/economic readiness\n24 Sep 2027"]
  M6 --> M8
  M7 --> M8
```

M0 is the only urgent recovery path until the evidence ledger is truthful. The first concrete payment implementation and acceptance evidence after M0 runs on Solana rails with AUDD payments because the captain's active obligations are to Solana Superteam Australia and the AUDD release gates. Product proofs continue only where they do not consume evidence owners, confuse grant truth, or require live value. Mainnet, signing/custody, public grant claims, outreach, deployment, and spend remain separate human gates.

## Captain obligation-driven sequencing

The accepted strategy remains portable: ADL and RAP core contracts are rail-neutral, and x402, MPP, AP2, ACP/UCP, Stripe-style rails, and later chains are comparison fixtures or later adapters. Sequencing is not neutrality. The first implementation and acceptance-evidence profile must satisfy the existing Solana/AUDD obligations before Reddi spends attention on a public cross-standard no-spend proof that would be easier to explain but would not discharge those obligations.

Executable order:

1. **Recover M0 truth:** ECO-000 through ECO-004 recover governing grant text, repository/release/deployment snapshots, current Solana identities and historical/superseded Quasar provenance, adoption/volume definitions, and AUDD issue 615-630 gaps. ECO-005 prepares human-approved remediation and grant communication decisions.
2. **Constrain RAP readiness:** ECO-040 imports current RAP readiness findings, including any evidence that mainnet/live paths are not ready, and isolates Solana, AUDD, x402, MPP/AP2, Nostr, provider, and custody assumptions behind adapters.
3. **Freeze the adapter contract:** ECO-041 versions quote, authorize, submit, observe, settle, refund-or-reverse, reconcile, and redact semantics with explicit custody, finality, fee, refund, chargeback, idempotency, redaction, and offline-verification capabilities.
4. **Implement Solana/AUDD first:** ECO-042 maps current RAP middleware/programs to Solana/AUDD adapter behavior, scopes and lands the SPL mint/token-account/PDA-layout work the SOL-only escrow lacks before the audit that must cover it, adds canonical AUDD/devnet/test fixtures, produces receipts and rail observations, and proves negative cases without live spend. This is on-chain program work, not adapter configuration, and it is why the first implementation is not a quick step.
5. **Bind receipts and Arena evidence:** ECO-045 plus ECO-051/ECO-052 bind job/agreement, actors, Arena evidence, judge/rubric, Solana/AUDD observation, environment, redaction class, and receipt version into replayable audit artifacts.
6. **Deliver and audit AUDD nodes:** ECO-046 reconciles RAP issues 615-630 to the new contract, delivers or cites the retirement of any standards evidence ECO-004 confirmed a governing text still requires, and records implementation, test, devnet, and independent audit evidence without claiming eligible volume, users, live settlement, or grant acceptance before evidence exists.
7. **Prepare acceptance and communication pack:** ECO-047 packages privacy-safe Superteam Australia/AUDD evidence, exception lists, operator approvals, and grant communication drafts behind legal/grantor/publication gates.
8. **Only then broaden public proofs:** ECO-043 and later Buzz/community nodes run the no-spend cross-standard proof against deterministic fake and MPP/AP2/x402/Stripe-style fixtures to demonstrate neutrality without displacing the Solana/AUDD first implementation.

No step authorizes synthetic activity, unapproved live transactions, mainnet claims, publication, or grantor communication.

## Current M0 evidence posture — 2026-08-31

ECO-001 now has a reproducible public GitHub snapshot at
[`evidence/github/ECO-001-2026-08-31.md`](../evidence/github/ECO-001-2026-08-31.md).
That snapshot records default-branch commits, GitHub releases/tags, recent CI,
branch-protection responses, milestones, open PRs, issue counts/status, deployment
API observations, explicit package-evidence gaps, and a 2026-09-01 corrective
primary-source log for release-body, RAP root-package, npm `web`, Omarchy, and x402
provenance details. It proves only those repository/API facts.

M0 can next proceed with:

- ECO-000 source recovery, keeping private grant materials out of this public repository;
- ECO-002 quantitative measures once canonical package names, download windows,
  integration definitions, user/workshop definitions, and privacy-safe exports exist;
- ECO-003 Solana/Quasar identity reconciliation using RAP config and read-only chain evidence;
- ECO-004 commitment-row audit using ECO-000 sources plus ECO-001/ECO-002/ECO-003 evidence.

M0 remains blocked from claiming grant completion, adoption, package publication, live
integration, mainnet readiness, production readiness, or eligible volume until those facts
are proven by the relevant primary sources and approved human gates.

## Milestones and proof outcomes

| Gate | Target | Programme proof | Principal epics |
|---|---:|---|---|
| M0 Evidence Recovery and Grant Truth | 11 Sep 2026 | Every May–July commitment, August target, and AUDD gate has governing text, evidence, gap, owner role, and approved disposition | E00 |
| M1 Programme Baseline and Governance | 25 Sep 2026 | Public control-plane repo, validated graph/projections, research/prompt governance, claim/status views, open-source and community covenants | E01–E02 |
| M2 ADL/RAP/Arena Contract Convergence | 30 Oct 2026 (un-rebaselined; predates the SPL scope) | Portable ADL projection and Agent BOM, rail-neutral RAP lifecycle/events/receipts, first Solana/AUDD implementation and acceptance pack, then contract-tested MPP/AP2/x402 comparison fixtures, multi-runtime conformance, deterministic Arena replay | E03–E05 |
| M3 Reddi Arena for Buzz Proof | 11 Dec 2026 | After Solana/AUDD acceptance evidence is packaged, upstream-compatible sidecar proves no-spend discovery-through-receipt flow with Nostr privacy/trust and usable lifecycle UX | E06 |
| M4 Reddi Pack for Omarchy Quattro Alpha | 29 Jan 2027 | Signed services and thin keyless QML cockpit install, update, roll back, disable, and uninstall on supported Omarchy | E07 |
| M5 Reddi Machine Developer Preview | 26 Mar 2027 | Evidence chooses provisioning/image shape; reproducible first boot, identity/wallet boundary, hardware matrix, updates and recovery work | E08 |
| M6 Lighthouse Hosted Services Alpha | 30 Apr 2027 | Managed relay/Arena/evidence operations meet isolation/SLO/export/OSS-parity gates and have measured unit economics | E09 |
| M7 Community Season Zero and Builder Beta | 25 Jun 2027 | Safe contributor journeys, reciprocal upstream work, recurring build programme, independent contributors and conformance implementations | E10 |
| M8 Production and Economic Readiness | 24 Sep 2027 | Independent review, incident/refund/recovery drills, privacy/supply-chain evidence, support matrix, and explicit production decisions | E11 |

## Historical first-30-day plan: recover and make the programme legible

This section preserves the 2026-08-31 planning snapshot. It is historical sequencing,
not a current calendar commitment; use the applicability catalog and canonical graph for
current status.

### Days 1–5

- ECO-000: recover governing grant/target documents and amendments;
- ECO-001: freeze dated repository, release, package, deployment, and issue evidence;
- ECO-010: create the empty public GitHub repository and publish the validated bootstrap;
- ECO-011/ECO-020: finish CI integrity and research-source review.

### Days 6–12

- ECO-002: calculate npm, integration, workshop, user, and volume measures from authoritative sources;
- ECO-003: reconcile Quasar, legacy Anchor, environment, and program-ID claims;
- ECO-004: audit May–July, August, and AUDD commitments without duplicating RAP 615–630;
- ECO-021: ratify prompt/eval/trace governance.

### Days 13–30

- ECO-005: obtain human dispositions and any grantor communication approval;
- ECO-012–ECO-015: publish issue projections, decisions/claims, status, and review rhythm;
- ECO-022: baseline the prompt roles on real recovery/planning tasks;
- ECO-030/ECO-040/ECO-050: begin the three canonical M2 audits in parallel after M0 evidence ownership is secure.

## Days 31–90: freeze portable seams, then prove Buzz

Three branches proceed with explicit join gates:

1. **ADL branch:** portability gap -> Agent BOM/dependency graph -> projections ->
   prompt/eval/authority profiles -> multi-runtime conformance.
2. **RAP branch:** leakage/readiness audit -> normalized payment adapter -> Solana/AUDD first implementation -> receipt and Arena evidence binding -> AUDD issue 615-630 audit/acceptance pack -> MPP/AP2/x402/Stripe-style comparison fixture.
3. **Arena branch:** canonical ADL -> evaluation bundle -> replay/audit -> adversarial tracks ->
   provider/runtime matrix -> upstream findings loop.

Only after those branches join and the Solana/AUDD acceptance pack exists does the Buzz branch build the public no-spend sidecar and lifecycle UX. This prevents Buzz/Nostr event shapes, Solana identifiers, MPP/AP2/x402 commerce concepts, or a single model provider from becoming accidental ADL/RAP semantics.

## 2027 productization sequence

- Productize the proven services before the Quattro UI; the unsandboxed plugin remains thin.
- Prove install/update/rollback/uninstall before deciding on a custom machine image.
- Build Lighthouse against the same public APIs and conformance fixtures as local/self-hosted.
- Run community programmes only when review, moderation, documentation, and safe no-spend
  paths can support new participants.
- Make production/mainnet decisions last, per product/rail/asset/environment, with explicit
  rollback and claim wording.

## Programme success measures

Delivery is measured by accepted evidence, not issue count. Portfolio measures include:

- commitment evidence coverage and overdue-decision age;
- graph lead time, blocked time, review latency, replay success, and escaped regressions;
- ADL/RAP conformance across independent runtimes and rails;
- independent contributors/implementations and upstream patch acceptance/age;
- clean-machine first success, install/update/recovery success, and support burden;
- Lighthouse availability, evidence durability, export success, support load, margin, and
  open-source parity;
- independently reconciled users, integrations, payments, and grant criteria under their
  exact definitions.

No metric authorizes activity undertaken solely to inflate it.

