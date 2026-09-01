# Programme sync log

This log records material divergence between the canonical programme graph and its
GitHub execution projections. Newest entries appear first.

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
- Expected footprint: `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/ROADMAP.md`, `docs/architecture/PORTFOLIO.md`, `docs/architecture/ADAPTER-BOUNDARIES.md`, `docs/decisions/0002-adapter-and-projection-first.md`, `docs/grants/AUDIT-2026-08.md`, `docs/grants/commitments.yaml`, `planning/graph.yaml`, `planning/milestones.yaml`, `planning/repositories.yaml`, `research/SOURCES.yaml`, `tools/graph_lint.py`, `tools/research_lint.py`, `tools/project_issues.py`, `tests/test_graph_lint.py`, `tests/test_project_issues.py`, `tests/test_research_lint.py`, `research/2026-08-31-market-technical-refresh-record.md`, and regenerated `planning/issues/**` projections. `AGENTS.md` gained a maintenance bar and `CLAUDE.md` imports it so the operating contract has one canonical location for every agent runtime. `tools/research_lint.py` now requires a non-empty `acceptanceArtifacts` list on every commitment so the canonical ledger cannot again carry acceptance artifacts for only part of the obligations. The graph schema moved to `schemaVersion: 2` because `railRole`, `railProfile`, `comparisonStandards`, and `railFieldTypes` expand the canonical graph contract; `tools/graph_lint.py` and `tools/project_issues.py` now assert that version and the generated issue index prints it. The graph gained a `railRoleVocabulary` with `railRole` and `comparisonStandards` node fields so `tools/graph_lint.py` enforces Solana/AUDD-first sequencing structurally instead of by matching English prose, and `tools/project_issues.py` projects those fields. A `railProfile` field pins the first-implementation node to `solana-audd` so no later standard can inherit that role, `docs/decisions/0002-adapter-and-projection-first.md` records the 2026-08-31 amendment instead of silently restating a 2026-08-26 decision, and the AUDD-2026-M1 x402 obligation stays unconditional until a re-read of the governing text is recorded as evidence. ECO-004 now owns that re-read, ECO-046 owns delivering or citing the retirement of any obligation-required standards evidence, and ECO-047 must name the owning node for every obligation it leaves blocked or unknown, so no restored obligation reaches the acceptance binder ownerless. AUDD issues 616-619 were re-read at 2026-09-01 and each ledger row's gaps and acceptanceArtifacts now transcribe its governing text, including the Langfuse audit trail, transaction signatures, non-secret wallet authority metadata, and operator runbook that no artifact list previously named; ECO-046 declares the ECO-005 disposition it acts on and owns delivering every artifact its governing issue names. RAP readiness PR #646 was re-read at 2026-09-01: its S-1 SOL-only escrow gap and S-2 unimplemented fee now constrain ECO-042 explicitly, so the first implementation is planned as on-chain SPL work landed before its audit rather than as adapter configuration. The refresh report itself is now registered as a source and ADR-0002 records its high-confidence contrary recommendation, that a second materially different fixture is needed earlier, as knowingly overridden by the obligation argument. M2 keeps its 2026-10-30 date but records that the date predates the SPL scope and awaits a maintainer re-baseline. The refresh report is recorded in-repository as a provenance, digest, and cited-excerpt record so the source register stays checkable from a fresh clone, and the acceptance-pack ordering is now pinned to every node carrying the comparison-fixture rail role rather than to ECO-043 by name. The graph records the semantics of its own `railRole`, `railProfile`, and `comparisonStandards` fields under `railFieldTypes`, mirroring `dependencyEdgeTypes`, so the sequencing rules `tools/graph_lint.py` enforces are legible in the canonical file instead of only when the linter fails. Declaring `railProfile` now requires an explicit `railRole` on the same node, so a rail commitment cannot skip the acceptance-pack ordering by omitting its role. `docs/grants/commitments.yaml` and `research/SOURCES.yaml` moved to `schemaVersion: 2` because the required `acceptanceArtifacts` field and the `repo:` source location form changed their contracts, and `tools/research_lint.py` now asserts the schema version of every registry it loads so those numbers stay a reliable signal. `planning/milestones.yaml` and `planning/repositories.yaml` moved to `schemaVersion: 2` for the same reason, because `sequencingRevisedAt`, `targetDateBasis`, `prohibitedShortcuts`, and `observedEvidence` expand their contracts, and `tools/graph_lint.py` now asserts the schema version of every planning registry it loads so the convention holds across all four registries this branch changed.
- Divergence from the 2026-08-26 plan: the broad no-spend cross-standard public proof no longer runs in parallel with or before the obligation path. The graph now requires Solana rails with AUDD payments, RAP readiness import, receipt/Arena evidence, AUDD issue 615-630 delivery, and a Superteam Australia/AUDD acceptance binder before MPP/AP2/x402-style public comparison proofs.
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
