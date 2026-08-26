# Reddi Ecosystem

The Reddi Ecosystem programme coordinates a portable, open agent economy:

- **ADL (Agent Definition Language)** defines agents independently of model provider,
  runtime, operating system, blockchain, token, and payment rail.
- **Reddi Agent Protocol (RAP)** coordinates discovery, negotiation, execution,
  evidence, receipts, judging, settlement, disputes, and reputation.
- **Reddi Arena** is the deterministic proof and competitive learning environment.
- **Reddi Arena for Buzz** projects ADL and RAP into a human-and-agent Nostr workspace.
- **Reddi Pack for Omarchy** provides an optional whole-machine cockpit and service bundle.
- **Reddi Machine** is the eventual reproducible hacker workstation/node distribution.
- **Lighthouse services** are optional managed operations that fund continued open development.

This repository is the portfolio control plane. It does not replace the component
repositories or copy their canonical specifications. It records cross-repository
dependencies, programme milestones, architectural decisions, grant evidence,
research provenance, upstream obligations, and community commitments.

## Current recovery posture

The programme begins with **M0: Evidence Recovery and Grant Truth**. No stale plan or
marketing claim is accepted as complete merely because an artifact or issue exists.
Each claim is classified as `verified`, `partial`, `planned`, `blocked`, `superseded`,
or `unknown`, with a reproducible evidence reference.

Known starting points on 2026-08-26:

| Repository | Canonical responsibility | Audited starting observation |
|---|---|---|
| [nissan/reddiagent-lab](https://github.com/nissan/reddiagent-lab) | ADL v0.2 and companion open specifications | Public; ADL v0.2 is canonical here; implementation findings flow back through its intake |
| [nissan/reddi-agent-protocol](https://github.com/nissan/reddi-agent-protocol) | RAP implementation, receipts, payment/trust adapters, Solana/Quasar proofs | Public; large active product and grant backlog; live/mainnet paths remain approval-gated |
| [nissan/reddi-arena](https://github.com/nissan/reddi-arena) | Arena proof, conformance pressure, competitive environment | Public; at least 72 tests and a 42-node graph were evidenced in merged PRs by 2026-08-16 |
| [block/buzz](https://github.com/block/buzz) | Upstream Nostr workspace used by the proposed Buzz integration | External Apache-2.0 upstream; integration strategy must minimise permanent fork tax |
| [basecamp/omarchy](https://github.com/basecamp/omarchy) | Upstream Linux distribution and Quattro shell | External MIT upstream; Quattro plugins are an optional cockpit, not the RAP runtime |

## Non-negotiable architecture boundaries

1. ADL remains the canonical portable definition; Buzz personas and machine packages are projections.
2. RAP observes and coordinates economic state; payment rails settle value.
3. Solana, AUDD, and x402 are the initial adapters, not permanent protocol assumptions.
4. Stripe and future chains, tokens, stablecoins, or conventional rails use the same adapter contracts.
5. A Nostr event is a signed command or observation, not proof that money moved.
6. Quattro plugins never hold wallet keys and never become the privileged runtime.
7. Local and self-hosted success cannot require Lighthouse services.
8. Mainnet, custody, live spend, and external publication remain explicit human gates.

## How work is organised

- [`docs/ROADMAP.md`](docs/ROADMAP.md) is the human-readable end-to-end roadmap and critical path.
- `planning/graph.yaml` is the canonical cross-repository execution graph.
- `planning/milestones.yaml` defines outcome gates and planning targets.
- `planning/repositories.yaml` records canonical ownership and synchronisation rules.
- `planning/issues/` contains publishable issue specifications generated from the graph.
- `research/` records primary-source evidence and implications, never vendor-news summaries alone.
- `prompts/` contains composable role and loop prompts; prompts are versioned and evaluated artifacts.
- `docs/grants/` separates promises, evidence, gaps, and remediation decisions.
- `docs/community/` records upstream-first and community-building commitments.

Run the portfolio checks with:

```bash
python3 tools/graph_lint.py
python3 tools/research_lint.py
python3 -m unittest discover -s tests -v
```

## Open development and sustainable operation

Specifications, protocol code, conformance tools, adapters, integrations, and the
reference local path are developed in public. Optional paid Lighthouse services make
the ecosystem easier to operate at scale through hosting, updates, evidence retention,
certification, support, and service-level commitments. See
[`OPEN-SOURCE-COVENANT.md`](OPEN-SOURCE-COVENANT.md).

## Status

Bootstrap is locally complete and validated. The public `nissan/reddi-ecosystem` repository
exists; initial publication is waiting for the connected GitHub integration to be granted
contents access to that newly created repository.

## License

Apache-2.0. Third-party projects, specifications, names, and marks retain their own terms.
