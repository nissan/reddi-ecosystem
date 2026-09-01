# ADR-0002: Portable core, adapters, and projections first

- Status: accepted direction; contracts remain M2 work
- Date: 2026-08-26
- Decision owner: programme steward
- Review: M2 convergence gate

## Context

The first concrete payment implementation and acceptance-evidence profile uses Solana rails with AUDD payments for Solana Superteam Australia and AUDD obligations, while the product must support x402, MPP, AP2, other chains, assets/tokens, payment protocols, Stripe-style rails, model providers, runtimes, clients, and operating environments over time.

## Decision

ADL defines the portable agent. RAP defines the portable economic-work lifecycle. Environment products and providers are adapters or projections. The Solana/AUDD implementation must pass public adapter, receipt, and Arena evidence contracts first; a materially different no-spend payment fixture and at least two runtime/model profiles then prove neutrality without displacing that obligation-driven sequence.

Nostr events are signed intent/observation, not payment truth. x402 is a payment challenge and response mechanism, not generic escrow. MPP/AP2/ACP/UCP are standards inputs and later adapter/comparison profiles, not first-delivery substitutions. Stripe-style authorization/capture is not assumed to have on-chain finality. Quattro QML is presentation code and never holds signer secrets.

## Consequences

The obligation-first proof takes longer than hard-coding a cross-standard demo, but it creates acceptance evidence for the actual Solana/AUDD commitments while preserving executable evidence of portability. Adapter capability negotiation, normalized receipts, identity binding, and projection diff/conformance are critical-path work rather than later cleanup.

