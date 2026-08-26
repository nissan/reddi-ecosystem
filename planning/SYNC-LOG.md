# Programme sync log

This log records material divergence between the canonical programme graph and its
GitHub execution projections. Newest entries appear first.

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
