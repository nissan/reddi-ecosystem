# Adapter boundaries

## Principle

RAP describes the economic lifecycle. Adapters translate that lifecycle to a concrete
environment. They do not alter the lifecycle to match one vendor, chain, asset, or
payment product.

## Required adapter families

| Adapter | Portable input | Portable output | Initial implementation |
|---|---|---|---|
| identity | subject, key purpose, proof request | verified binding, method, expiry | Nostr keys plus wallet binding |
| transport | versioned RAP event envelope | delivery/ordering observation | Nostr/Buzz and HTTP |
| runtime | ADL deployment projection, limits | execution events and artifacts | local/container model harness |
| evidence | artifact or observation | digest, provenance, availability | content-addressed local/object storage |
| judge | task, rubric, evidence | score, explanation, judge identity | deterministic and model-assisted Arena judges |
| payment | normalized intent and authorization | normalized settlement observation | Solana + AUDD + x402 |
| reputation | receipts and attestations | scoped, time-bound assertion | RAP/Quasar profile |

## Payment adapter contract

A payment adapter must expose at least:

1. `quote` — price, asset/currency, network/rail, payee, expiry, and fee policy;
2. `authorize` — user- or policy-approved authority, limits, and idempotency key;
3. `submit` — rail-specific operation without logging secrets;
4. `observe` — authoritative status read from the rail/provider;
5. `settle` — finality/capture semantics and canonical reference;
6. `refund_or_reverse` — supported remedy and resulting state;
7. `reconcile` — bind rail records to job, agreement, and receipt;
8. `redact` — evidence safe for the intended audience.

The normalized state machine must accommodate at least:

```text
proposed -> authorized -> submitted -> pending -> settled
                     \-> rejected/expired/failed
settled -> refund_pending -> refunded
pending -> reversed
```

Escrow is a separate capability, not an assumed property of x402, card authorization,
or delayed capture. An adapter declares `escrow`, `partial_refund`, `chargeback`,
`finality`, `custody`, and `offline_verification` capabilities explicitly.

## Neutrality tests

The base contract is not accepted until the same RAP fixture passes through:

- the Solana/AUDD/x402 adapter;
- a deterministic fake rail used for negative and replay tests; and
- one materially different proof adapter, initially a Stripe-style fiat fixture or a
  second-chain fixture, selected without creating a production account or live charge.

Tests must prove that rail-specific identifiers stay under adapter namespaces and do
not leak into ADL definitions, RAP core transitions, Arena rules, or Buzz event kinds.

## Event contract

Events use a versioned envelope compatible with CloudEvents concepts: stable event ID,
source, type, subject, time, data content type, schema reference, correlation/causation,
and trace context. Delivery is not completion. Consumers must be idempotent and replayable.

Every economically relevant state transition records:

- the prior and next state;
- actor and authority basis;
- correlation to job/agreement/receipt;
- source observation and digest;
- clock and ordering assumptions;
- redaction class;
- whether a human gate was required and who approved it.

## Security boundary

Signer and payment credentials remain in a narrow authority service or external wallet.
Buzz, Nostr relays, Quattro QML, model prompts, and hosted dashboards receive scoped
requests and redacted results only. No adapter may treat model output as authorization.

