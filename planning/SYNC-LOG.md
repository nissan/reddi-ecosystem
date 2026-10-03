# Programme sync log

This log records material divergence between the canonical programme graph and its
GitHub execution projections. Newest entries appear first.

## 2026-10-03 — portfolio planning and governance reconciliation

- Claimed one bounded planning increment under `ECO-014`, with expected footprint in
  `planning/`, the roadmap/portfolio/grant documentation, generated projections,
  governance/contributor/PR-template surfaces, tests, and sanitized synchronization
  evidence. No component implementation, repository setting, branch-protection, live,
  payment, signing, deployment, release, partner-contact, or issue-close/reopen action is
  in scope.
- Baseline verified: this branch began at merged ecosystem
  [`bc1f5acc80b459f4bf770c759290d208638d73f2`](https://github.com/nissan/reddi-ecosystem/commit/bc1f5acc80b459f4bf770c759290d208638d73f2),
  the squash merge of [ecosystem PR 25](https://github.com/nissan/reddi-ecosystem/pull/25).
- The 623-row independent issue evaluation was treated as issue-body evidence, not as a
  source-code correctness review. Its final coverage and hypothesis corrections supersede
  interim severity. No stale epic was automatically classified as a High defect and no
  close/reopen proposal was executed.
- Implemented approved direction: E12 and ECO-016–019 add planned M1 security/trust,
  privacy/evidence, supply-chain, glossary/ownership, and documentation baselines. M4–M7
  consumers now depend on the relevant early baseline rather than M8 production-readiness
  nodes. ECO-110–115 retain deeper enforcement, drills, independent audit, and production
  decisions; no baseline is marked complete. Graph lint now rejects any node whose milestone
  depends on a node in a later milestone, preventing the inversion from returning.
- ECO-046 now owns bounded technical Solana/AUDD evidence for RAP issues 620–630 and
  evidence packets [632](https://github.com/nissan/reddi-agent-protocol/issues/632)–[635](https://github.com/nissan/reddi-agent-protocol/issues/635).
  ECO-047 separately owns eligibility, partner/grant acceptance, communication, live and
  publication gates. ECO-043 and the E06 architecture mapping may follow ECO-046, while
  the public Buzz sidecar ECO-062 still depends on ECO-047. This is technical no-spend
  decoupling, not a grant or live-action waiver. ECO-043, ECO-046, and ECO-060 keep their
  original human gates: local static, fixture, and localnet no-spend/no-contact work may
  proceed, while devnet signing, live promotion, upstream contact, repository creation, and
  every other gated action still require the listed approvals.
- The RAP v0.1 no-new-SPL-program decision versus proposed SPL mint/token-account/PDA
  layout work remains unresolved. ECO-040 now requires a bounded canonical RAP ADR or
  semantic disposition; this increment does not invent the answer.
- Lab Buzz issues [419](https://github.com/nissan/reddiagent-lab/issues/419)–[433](https://github.com/nissan/reddiagent-lab/issues/433)
  map into E06 for reuse and ownership classification. Closed design work is preserved at
  its evidenced plan/spec or implementation scope and is not declared live.
- [`GOVERNANCE.md`](../GOVERNANCE.md#delivery-and-merge-policy) is the one canonical
  delivery policy: permitted green validation plus two fresh independent Claude-family
  and Codex explicit `GO` verdicts on one unchanged full SHA; non-author,
  permission-respecting review; stale-verdict invalidation; critical/high current-cycle
  fixes; deduplicated issue-backed medium/low deferrals acknowledged by reviewers; and a
  no-progress checkpoint/escalation rule. It records process, not asserted settings or
  automated enforcement. Firstmate alone has conditional merge authority.
- Task routing now distinguishes deterministic scripts, lowest-adequate narrow work,
  moderate substantive work, and high-reasoning risk/ambiguity work. Dispatch checks
  current provenance, short-window and weekly quota/pace/reset/runway, reserves review
  capacity, respects the three-active-per-provider-family cap, and treats unknown quota as
  uncertainty. No scheduler or control plane was added.
- Historical milestone dates remain present for provenance. Every date is visibly
  unconfirmed; M0 and M1 are overdue pending evidence-backed re-estimation. No fabricated
  GitHub milestone date was created.
- Documentation is a cross-cutting milestone gate and ECO-019 is the minimal portfolio
  owner task. [`docs/PORTFOLIO-PLAN.md`](../docs/PORTFOLIO-PLAN.md) supplies the glossary,
  ownership/trust-boundary and technical-versus-external Mermaid diagrams plus textual
  explanations. RAP [issue 679](https://github.com/nissan/reddi-agent-protocol/issues/679)
  owns the receipt/authority/refusal/replay guide; existing lab
  [issue 206](https://github.com/nissan/reddiagent-lab/issues/206) and Buzz issues 419–433
  were reused rather than duplicated for ADL/Buzz indexes and component guidance.
- Dependency semantics reuse supported fields: HT/EV use `dependsOn`, EX uses
  `externalIssue`, AP uses `humanGates`, and RS stays milestone/prose sequencing. The graph
  and linter do not add an unconsumed per-edge field.
- Grant ledger references lab [issue 406](https://github.com/nissan/reddiagent-lab/issues/406)
  and RAP issues 632–635 as unresolved obligations. Issue or packet existence is not
  release, visibility, submission, eligible activity, partner acceptance, or grant
  acceptance.

## 2026-10-02 — ECO-014 roadmap and BDD applicability refresh

- Claimed executable node `ECO-014` only. Expected footprint: `README.md`,
  `docs/ROADMAP.md`, a proportionate behavior/applicability catalog under `docs/`,
  current authority/evidence annotations in `planning/repositories.yaml`, the stale
  Quasar identity wording in `planning/graph.yaml`, generated issue projections, and
  this Sync Log entry.
- Captain-approved execution waives ECO-014's incomplete ECO-004/ECO-012/ECO-013
  prerequisites only for this bounded applicability reconciliation. The refresh does
  not claim ECO-014 complete, publish a status service, or bypass those dependencies
  for later acceptance.
- Current `gh-axi` evidence confirmed RAP pull requests
  [654](https://github.com/nissan/reddi-agent-protocol/pull/654),
  [663](https://github.com/nissan/reddi-agent-protocol/pull/663),
  [671](https://github.com/nissan/reddi-agent-protocol/pull/671), and
  [674](https://github.com/nissan/reddi-agent-protocol/pull/674) merged to `main` at
  their recorded 40-character merge commits. Arena pull request
  [96](https://github.com/nissan/reddi-arena/pull/96) merged at exact commit
  `2eb85056b643b6ee55c0be603ed73f9becee20b4`; an interim longer SHA was rejected.
- `ECO-003` now preserves frozen Quasar deployment/provenance evidence while removing
  the stale implication that Quasar remains on a product, deployment, audit,
  production, or mainnet progression path. This changes portfolio applicability only;
  RAP remains the authority for implementation and deployment registry semantics.
  Existing [ecosystem issue 7](https://github.com/nissan/reddi-ecosystem/issues/7)
  retains its older projected title until a separately approved GitHub projection sync;
  no remote issue was changed by this work.
- The typed HT/EV/EX/AP/RS view is explanatory: existing `dependsOn` and `humanGates`
  remain the machine-consumed graph fields. No chronology was added as a hard edge, and no
  existing edge was removed. The catalog reconciles every listed blocker and unlock to
  `dependsOn`; the replay join to ECO-046 is shown only as proposed sequencing.
- Captain-approved audit-only waiver: the read-only gap-audit portions of `ECO-040` and
  `ECO-030` may start before their unmet `ECO-001` (in-progress) and `ECO-020`
  (in-progress) dependencies are done. Both edges stay in the graph. The waiver does not
  cover node completion, contract freeze, acceptance, implementation, or any dependent
  node; initial audit findings are inputs only.
- Follow-up join: after the parallel RAP readiness and ADL portability audits, revisit
  the graph once for verified blockers, canonical issue links, and semantic contract
  joins. Medium/low findings remain separate issue-backed maintenance work.
- No email connection, partner contact, publication, package release, deployment,
  wallet/key operation, signing, transaction, live activation, or grant-acceptance
  claim occurred.

## 2026-09-01 — ECO-001 replacement publication path

- Claimed graph node `ECO-001` only. Expected footprint: public GitHub evidence under
  `evidence/github/`, graph/status and generated issue projection metadata under
  `planning/`, focused validation changes under `tools/` and `tests/`, and narrow status
  references in README, roadmap, grant audit, repository registry, and research sources.
- Started replacement branch `fm/ecosystem-m0-republication` from clean current
  `origin/main` at `7d41cc4646fa1377932ba490c9708b73f198360d`; that name was never
  published because the local gate refused it as a non-fast-forward, so this head is
  published on `fm/ecosystem-m0-republication-v2` instead, with no remote branch forced
  or rewritten. Current main matched the preserved base, so no concurrent authoritative
  Solana/AUDD registry, graph, grant, or upstream-URL changes had to be overwritten. Preserved commit `edf81be` and no-mistakes
  run `01M1D1TQF1P8V6PSENE45K4FGX` remain read-only evidence and were not reset, deleted,
  or continued.
- Reconstructed the ECO-001 public GitHub/API snapshot for `reddi-ecosystem`,
  `reddiagent-lab`, `reddi-agent-protocol`, and `reddi-arena` in
  [`evidence/github/ECO-001-2026-08-31.md`](../evidence/github/ECO-001-2026-08-31.md),
  retaining raw transcripts and adding corrective 2026-09-01 primary-source transcript
  entries for RAP root `package.json`, release-body claims, npm `web`, Omarchy repository
  metadata plus direct `manual/32-shell-plugins.md` contents, and x402 metadata.
- `ECO-001` remains `in-progress`: the snapshot covers default branches, releases/tags,
  recent CI, branch-protection responses, milestones, open PRs, issue counts/status,
  GitHub deployment metadata, and explicit package-evidence gaps, but component clean
  reruns and authorized package/registry exports remain open.
- Corrected new canonical upstream references from `basecamp/omarchy` to
  `omacom/omarchy`; for x402, GitHub API metadata supports `x402-foundation/x402` as the
  source repository for new roadmap references while preserving `coinbase/x402` as an
  active development fork/provenance reference. No separate transfer/succession
  announcement was captured.
- Footprint divergence: the increment also adds a `Maintaining this file` section to
  `AGENTS.md` and a two-line `CLAUDE.md` that imports it, so Claude-family sessions read the
  same operating contract as every other agent instead of an unmaintained second copy. This is
  outside the ECO-001 evidence footprint declared above and is recorded here as an accepted
  divergence; it changes agent instructions only and no graph, evidence, or grant semantics.
- No GitHub issues, milestones, labels, releases, packages, deployments, live payments,
  mainnet actions, or other remote state were created or modified for this increment.

## 2026-08-31 — Solana/AUDD-first obligation sequencing refresh

- Claimed executable node: `ECO-014` planning/status refresh, with an approved captain-scoped waiver to update prerequisite graph and roadmap artifacts before ECO-004/ECO-012 are complete because this change prevents incorrect downstream sequencing.
- Expected footprint: `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/ROADMAP.md`, `docs/architecture/PORTFOLIO.md`, `docs/architecture/ADAPTER-BOUNDARIES.md`, `docs/decisions/0002-adapter-and-projection-first.md`, `docs/grants/AUDIT-2026-08.md`, `docs/grants/commitments.yaml`, `planning/graph.yaml`, `planning/milestones.yaml`, `planning/repositories.yaml`, `research/SOURCES.yaml`, `research/2026-08-31-market-technical-refresh-record.md`, `tools/graph_lint.py`, `tools/research_lint.py`, `tools/project_issues.py`, `tests/test_graph_lint.py`, `tests/test_project_issues.py`, `tests/test_research_lint.py`, and regenerated `planning/issues/**` projections.
- Initial divergence from the 2026-08-26 plan: the broad no-spend cross-standard public proof no longer runs in parallel with or before the obligation path. The graph now requires Solana rails with AUDD payments, RAP readiness import, receipt/Arena evidence, AUDD issue 615-630 delivery, and a Superteam Australia/AUDD acceptance binder before MPP/AP2/x402-style public comparison proofs.
- Operating-contract housekeeping: `AGENTS.md` gained a maintenance bar and `CLAUDE.md` imports it so the operating contract has one canonical location for every agent runtime.
- Grant ledger contract: `tools/research_lint.py` now requires a non-empty `acceptanceArtifacts` list on every commitment so the canonical ledger cannot carry acceptance artifacts for only part of the obligations. `docs/grants/commitments.yaml` moved to `schemaVersion: 2`, and `tools/research_lint.py` asserts that version.
- Research source contract: `research/SOURCES.yaml` moved to `schemaVersion: 2` because the source register now supports a repository-contained `repo:` source record with path, digest, provenance, access date, cited excerpts, conclusions, and limitations. The external-source rule remains HTTPS-only.
- Planning registry contract: `planning/graph.yaml`, `planning/milestones.yaml`, and `planning/repositories.yaml` moved to `schemaVersion: 2`; `tools/graph_lint.py` asserts all three versions, and `tools/project_issues.py` asserts graph schema version 2 and prints it in the generated issue index.
- Rail planning fields: the graph added `railRoleVocabulary`, `railProfileVocabulary`, and `railFieldTypes`; `tools/graph_lint.py` enforces Solana/AUDD-first sequencing structurally instead of by matching English prose, and `tools/project_issues.py` projects the new fields. `ECO-041` declares its normalized operations in `adapterMethods`, so contradictory prose cannot satisfy the contract. `ECO-042` is explicitly pinned as the single `first-implementation` node with `railProfile: solana-audd`; `comparisonStandards` and `railProfile` require explicit `railRole`; no comparison fixture can list `solana-audd`; and every comparison-fixture node must depend on `ECO-047`.
- Decision record handling: `docs/decisions/0002-adapter-and-projection-first.md` records a dated amendment instead of silently restating the 2026-08-26 decision.
- AUDD governing text: AUDD issues 616-619 were re-read at 2026-09-01, and the AUDD ledger rows now transcribe their named gaps and acceptance artifacts, including x402 challenge/response proof, successful Solana AUDD payment evidence, transaction signatures, Langfuse trace/audit references, non-secret wallet authority metadata, and operator runbook. The AUDD-2026-M1 x402 obligation stays unconditional until a re-read of the governing text records otherwise.
- Grant sequencing: ECO-004 owns governing-text re-reads; ECO-046 owns delivering or retaining obligation-required standards evidence unless an ECO-005 retirement disposition already exists; ECO-047 must name the owning node for every obligation it leaves blocked or unknown and must re-stamp any binder or grantor communication if later comparison work changes the adapter contract or receipt semantics.
- RAP readiness incorporation: RAP readiness PR #646 was re-read at 2026-09-01. Its S-1 SOL-only escrow and S-2 unimplemented fee findings constrain ECO-042 explicitly. The first approved path is now direct, non-custodial AUDD SPL `TransferChecked` observed by RAP, while any future Quasar AUDD custody is a separate gated workstream requiring account-layout, PDA, instruction/client mirror, deployment, security, and audit rework.
- Market-refresh handling: the 2026-08-31 market/technical refresh is registered through an in-repository provenance/digest record. ADR-0002 records its high-confidence contrary recommendation that a second materially different fixture is needed earlier, and explains the obligation-based reason for knowingly sequencing Solana/AUDD first.
- Schedule handling: M2 keeps the old target date only as un-rebaselined historical planning data; `planning/milestones.yaml` and `docs/ROADMAP.md` now state that the date predates the SPL/foundation/audit scope and awaits maintainer re-estimation.
- Non-goals: no ADL semantic changes, no RAP implementation code, no GitHub issue mutation, no external communication, no spend, no signing/custody, no deployment, no live/mainnet claim, and no assertion that acceptance evidence already exists.
- Follow-up nodes: `ECO-047` packages privacy-safe acceptance evidence and communication gates; `ECO-043` and `ECO-060` now depend on it before broader no-spend rail-neutral/Buzz demonstrations.

## 2026-08-26 — Public bootstrap and first CI diagnosis

- Human gates `repo-creation` and `external-publication` were satisfied by the repository
  owner, including explicit approval to publish the reviewed grant, payment, security,
  operational, Lighthouse, research, prompt, and generated-planning artifacts.
- The connected GitHub App gained `admin` and `push` access to
  `nissan/reddi-ecosystem` after the local bootstrap had already been committed.
- Because the empty-repository connector requires a parent for low-level commits, GitHub
  received a one-file initialization commit followed by the complete bootstrap commit.
  The complete GitHub tree `52b103077e27c3f181a4ca6937da26ff267f259a` exactly matched
  the locally validated 140-file tree.
- The first GitHub Actions run failed before project checks because `setup-python` cache
  discovery did not recognize the non-default `requirements-dev.txt` filename. The
  workflow now declares that dependency path explicitly; no project validation failed.
- Corrected GitHub Actions run
  [`32980617673`](https://github.com/nissan/reddi-ecosystem/actions/runs/32980617673)
  passed. A fresh public clone independently passed graph lint, research/grant/prompt
  registry lint, deterministic issue projection checks, and all eight unit tests.
- The default `main` branch and repository rulesets were reviewed through GitHub's public
  API. The branch is currently unprotected and no rulesets exist; hardening remains M1
  governance work and is not represented as a completed protection claim.
- `ECO-010` moved to `done`. `ECO-011` remains `in-progress` because the wider CI
  integrity acceptance contract extends beyond a single passing bootstrap run.
