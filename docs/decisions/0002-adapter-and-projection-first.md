# ADR-0002: Portable core, adapters, and projections first

- Status: accepted direction; contracts remain M2 work
- Date: 2026-08-26
- Decision owner: programme steward
- Review: M2 convergence gate

## Context

The initial proof uses Solana, AUDD, x402, Nostr/Buzz, and Omarchy Quattro, while the product
must support other chains, assets/tokens, payment protocols, Stripe-style rails, model providers,
runtimes, clients, and operating environments over time.

## Decision

ADL defines the portable agent. RAP defines the portable economic-work lifecycle. Environment
products and providers are adapters or projections. The initial stack must pass the same public
contracts as a materially different payment fixture and at least two runtime/model profiles.

Nostr events are signed intent/observation, not payment truth. x402 is a payment challenge and
response mechanism, not generic escrow. Stripe-style authorization/capture is not assumed to
have on-chain finality. Quattro QML is presentation code and never holds signer secrets.

## Consequences

The initial proof takes longer than hard-coding a vertical demo, but it creates executable
evidence of portability. Adapter capability negotiation, normalized receipts, identity binding,
and projection diff/conformance are critical-path work rather than later cleanup.

