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
- `ECO-010` moved from `blocked` to `in-progress`. It can move to `done` only after the
  corrected CI run and public-clone verification pass.

