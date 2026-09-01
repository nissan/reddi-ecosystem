# Programme sync log

This log records material divergence between the canonical programme graph and its
GitHub execution projections. Newest entries appear first.

## 2026-09-01 — ECO-001 replacement publication path

- Claimed graph node `ECO-001` only. Expected footprint: public GitHub evidence under
  `evidence/github/`, graph/status and generated issue projection metadata under
  `planning/`, focused validation changes under `tools/` and `tests/`, and narrow status
  references in README, roadmap, grant audit, repository registry, and research sources.
- Started replacement branch `fm/ecosystem-m0-republication` from clean current
  `origin/main` at `7d41cc4646fa1377932ba490c9708b73f198360d`; current main matched the
  preserved base, so no concurrent authoritative Solana/AUDD registry, graph, grant, or
  upstream-URL changes had to be overwritten. Preserved commit `edf81be` and no-mistakes
  run `01M1D1TQF1P8V6PSENE45K4FGX` remain read-only evidence and were not reset, deleted,
  or continued.
- Reconstructed the ECO-001 public GitHub/API snapshot for `reddi-ecosystem`,
  `reddiagent-lab`, `reddi-agent-protocol`, and `reddi-arena` in
  [`evidence/github/ECO-001-2026-08-31.md`](../evidence/github/ECO-001-2026-08-31.md),
  retaining raw transcripts and adding a corrective 2026-09-01 primary-source transcript
  for RAP root `package.json`, release-body claims, npm `web`, Omarchy, and x402 metadata.
- `ECO-001` remains `in-progress`: the snapshot covers default branches, releases/tags,
  recent CI, branch-protection responses, milestones, open PRs, issue counts/status,
  GitHub deployment metadata, and explicit package-evidence gaps, but component clean
  reruns and authorized package/registry exports remain open.
- Corrected new canonical upstream references from `basecamp/omarchy` to
  `omacom/omarchy`; for x402, GitHub API metadata supports `x402-foundation/x402` as the
  source repository for new roadmap references while preserving `coinbase/x402` as an
  active development fork/provenance reference. No separate transfer/succession
  announcement was captured.
- No GitHub issues, milestones, labels, releases, packages, deployments, live payments,
  mainnet actions, or other remote state were created or modified for this increment.

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
