# Portfolio architecture

## The product stack

The Reddi Ecosystem is a set of replaceable layers, not a vertically coupled app.

```text
Human / agent experience
  Buzz workspace | CLI | web | Quattro cockpit | third-party clients
                         |
Portable agent definition
  ADL model + harness + declared capabilities + dependency inventory
                         |
Economic work protocol
  RAP discovery -> offer -> agreement -> execution -> evidence -> judgment -> receipt
                         |
Arena and conformance
  deterministic fixtures | replay | judges | adversarial/economic tests
                         |
Replaceable adapters
  identity | event transport | storage | model/runtime | evidence | payment | reputation
                         |
Rails and operations
  Solana/AUDD first | x402/MPP/AP2 fixtures | other chains/assets | Stripe/fiat | local | self-hosted | Lighthouse
```

The first concrete payment implementation and acceptance-evidence path uses Solana rails with AUDD payments because it is tied to the current Solana Superteam Australia and AUDD obligations. x402, MPP, AP2, Buzz, Nostr, and Omarchy Quattro remain projection, comparison, or later-adapter surfaces. Being first buys Solana and AUDD no exemption: none of these products, Solana and AUDD included, may become a required semantic primitive in ADL or RAP.

## Canonical ownership

| Concern | Canonical repository | Ecosystem repository role |
|---|---|---|
| ADL syntax, schema, semantics, conformance | `nissan/reddiagent-lab` | dependency and release view only |
| RAP state machine, receipts, adapters, implementation | `nissan/reddi-agent-protocol` | portfolio dependency and evidence view |
| Arena rules, fixtures, judges, replay | `nissan/reddi-arena` | cross-product milestone view |
| Programme milestones, grant truth, cross-repo graph | `nissan/reddi-ecosystem` | canonical |
| Buzz behavior and Nostr workspace | `block/buzz` upstream | patch/register/integration view |
| Omarchy and Quattro shell | `omacom/omarchy` upstream | patch/register/package view; `basecamp/omarchy` is historical/redirect context |

An ecosystem issue may coordinate component work, but its implementation issue must
live in the canonical component repository. Links are dependencies; copied issue text
is not synchronization.

## Projection rule

ADL is the source definition. A Buzz persona, Nostr event, Quattro tile, container,
systemd unit, cloud deployment, or model-provider configuration is a projection of
that definition. A projection can add environment-specific configuration but cannot
silently change agent identity, capabilities, budget authority, evaluation contract,
or receipt semantics.

## Data and authority planes

- **Intent plane:** signed requests, offers, agreements, approvals, cancellations.
- **Execution plane:** runtime/tool calls, sandboxes, model interactions, outputs.
- **Evidence plane:** content-addressed artifacts, traces, attestations, judge results.
- **Settlement plane:** rail-specific authorizations, transactions, captures, refunds.
- **Reputation plane:** derived assertions with provenance, expiry, and dispute state.
- **Presentation plane:** Buzz, web, CLI, and Quattro views.

Presentation and event transport can report state, but they cannot manufacture
settlement or evidence truth. An authoritative adapter must observe the underlying
system and bind its observation to the RAP job and receipt.

## Delivery shapes

1. **Existing machine:** run the reference local stack and optional Buzz sidecar.
2. **Reddi Pack:** install signed services plus a thin Quattro plugin on supported Omarchy.
3. **Reddi Machine:** reproducible provisioned workstation/node after the packaging and
   recovery gates are proven.
4. **Lighthouse:** optional managed equivalents with export, self-hosting parity, and
   explicit service-level boundaries.

## Decision records required

The graph blocks irreversible choices until evidence supports an ADR for:

- Buzz sidecar versus extension versus maintained fork;
- stock Omarchy plus provisioning versus a custom image;
- portable identity binding and recovery;
- payment adapter contract and receipt normalization;
- hosted data boundaries and custody exclusion;
- licensing, names, marks, and distribution terms.
