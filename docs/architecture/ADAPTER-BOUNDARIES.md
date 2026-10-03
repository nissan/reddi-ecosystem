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
| payment | normalized intent and authorization | normalized settlement observation | Solana rails + AUDD payments first; x402/MPP/AP2 as comparison fixtures and later adapters |
| reputation | receipts and attestations | scoped, time-bound assertion | RAP/Quasar profile |

## Payment adapter contract

A payment adapter must expose at least:

1. `quote` — price, asset/currency identifier, network/rail, payee, expiry, fee policy, and environment;
2. `authorize` — user- or operator-policy-approved authority, limits, idempotency key, approval evidence, and explicit no-spend/devnet/live/mainnet scope;
3. `submit` — rail-specific operation without logging secrets or allowing model output to become authorization;
4. `observe` — authoritative status read from the rail/provider, including read-only transaction or account observations where the rail exposes them;
5. `settle` — finality/capture semantics, canonical rail reference, and declared environment;
6. `refund_or_reverse` — supported remedy, compensating transaction or provider reversal, unsupported-state reason, and resulting state;
7. `reconcile` — bind rail records to job, agreement, Arena evidence, authority basis, and receipt;
8. `redact` — evidence safe for the intended audience, preserving verifiability while removing secrets, personal data, and sensitive grant/payment details.

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

## Solana/AUDD-first obligation path

The first concrete adapter implementation is Solana rails with AUDD payments. Once ECO-046 has produced bounded technical evidence and explicit gaps, no-spend, no-contact cross-standard fixture work may proceed. That technical sequence does not satisfy Superteam Australia or AUDD eligibility and acceptance: ECO-047 still owns partner/grant reliance and public promotion, and every live/value action remains behind ECO-047 and the applicable node-level human gates.

The Solana/AUDD path must produce fixture/devnet evidence before any operator-controlled live progression:

- canonical AUDD asset, network, payee, authority, and environment configuration;
- quote, authorize, submit, observe, settle, refund-or-reverse, reconcile, and redact behavior under the normalized contract;
- signer/custody boundaries that keep private keys and payment credentials in an external wallet or narrow authority service, never in prompts, Buzz, Nostr, Quattro, or generated evidence;
- devnet/test fixtures for happy path, wrong asset/network/payee/amount, expiry, replay, duplicate, partial, unavailable provider, refund/reversal-supported, and refund/reversal-unsupported cases;
- receipts binding RAP job/agreement, Arena evidence, judge/rubric, Solana/AUDD observation, environment, redaction class, and prior receipt/version;
- Arena conformance/audit bundles that can be replayed without new spend or mutation;
- privacy-safe acceptance artifacts for Superteam Australia and AUDD obligations, with unsupported live/mainnet/volume/user claims left `unknown` or `blocked` until approved evidence exists.

Live payment, signing/custody, deployment, mainnet, spend, publication, and grantor communication are separate human gates. Passing fixtures or devnet tests does not authorize promotion.

## Neutrality tests

The base contract stays rail-neutral from the start. Bounded local cross-standard fixture work follows ECO-046 technical evidence; public promotion of that proof, partner/grant reliance, and every live/value action remain blocked on ECO-047 and applicable node-level gates. The same RAP fixture then passes through:

- the Solana/AUDD adapter that already produced the obligation evidence;
- a deterministic fake rail used for negative and replay tests; and
- one materially different proof adapter, initially an MPP/AP2/Stripe-style conventional fixture or a second-chain fixture, selected without creating a production account or live charge.

x402, MPP, AP2, ACP/UCP, and similar standards inform capability mapping, authority/mandate comparisons, receipts, and later adapters. They do not displace the first Solana/AUDD implementation. Tests must prove that rail-specific identifiers stay under adapter namespaces and do not leak into ADL definitions, RAP core transitions, Arena rules, or Buzz event kinds.

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

