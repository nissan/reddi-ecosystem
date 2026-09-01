# ADR-0002: Portable core, adapters, and projections first

- Status: accepted direction; contracts remain M2 work
- Date: 2026-08-26
- Amended: 2026-08-31, 2026-09-01
- Decision owner: programme steward
- Review: M2 convergence gate

## Context

The first concrete payment implementation and acceptance-evidence profile uses Solana rails with AUDD payments for Solana Superteam Australia and AUDD obligations, while the product must support x402, MPP, AP2, other chains, assets/tokens, payment protocols, Stripe-style rails, model providers, runtimes, clients, and operating environments over time.

## Decision

ADL defines the portable agent. RAP defines the portable economic-work lifecycle. Environment products and providers are adapters or projections. The Solana/AUDD implementation must pass public adapter, receipt, and Arena evidence contracts first; a materially different no-spend payment fixture and at least two runtime/model profiles then prove neutrality without displacing that obligation-driven sequence.

Nostr events are signed intent/observation, not payment truth. x402 is a payment challenge and response mechanism, not generic escrow. MPP/AP2/ACP/UCP are standards inputs and later adapter/comparison profiles, not first-delivery substitutions. Stripe-style authorization/capture is not assumed to have on-chain finality. Quattro QML is presentation code and never holds signer secrets.

## Consequences

The obligation-first proof takes longer than hard-coding a cross-standard demo, but it creates acceptance evidence for the actual Solana/AUDD commitments while preserving executable evidence of portability. Adapter capability negotiation, normalized receipts, identity binding, and projection diff/conformance are critical-path work rather than later cleanup.

## Amendment log

- 2026-08-31: the Decision previously required the initial stack to pass the same public contracts as a materially different payment fixture concurrently. It now requires the Solana/AUDD implementation to pass adapter, receipt, and Arena evidence contracts first, with the materially different fixture following that obligation evidence. The Context and Consequences sections were restated to match; no other ADR is superseded.
- 2026-09-01: recorded contrary evidence. The 2026-08-31 market/technical refresh registered as `reddi-market-technical-refresh-2026-08-31` in `research/SOURCES.yaml` rates "Solana/AUDD/x402 is a good first adapter profile" as valid but weakened as the sole critical technical proof, and concludes at high confidence that MPP, Stripe x402, AP2 mandates, and conventional/card semantics make a second materially different fixture mandatory earlier because Solana/AUDD/x402 cannot stand in for agent-commerce neutrality. This decision sequences that fixture later anyway: the Superteam Australia and AUDD obligations are recorded commitments with governing text and a release gate, while agent-commerce neutrality is a positioning argument with no counterpart obligation. The accepted cost is that neutrality stays publicly unproven until the acceptance pack is reviewed. The risk is bounded because ECO-041 keeps the core contract rail-neutral, ECO-043 stays P0 within M2, and nothing in the sequencing forecloses the earlier fixture if a maintainer later reverses this weighting.
