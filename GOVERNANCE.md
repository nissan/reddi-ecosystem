# Governance

## Present phase

The project is maintainer-led while the contributor base and implementation evidence
form. Nissan Dookeran is the initial programme steward and decision owner. The target is
earned community governance, not governance theatre before participation exists.

## Decision classes

| Class | Examples | Required path |
|---|---|---|
| Reversible implementation | Refactor, test, documentation correction | Issue, PR, review, green checks |
| Cross-repository architecture | Canonical ownership, adapter contract, event semantics | RFC/ADR, affected-repo review |
| Protocol/specification | ADL or RAP semantic change | Canonical repo intake, compatibility analysis, versioning decision |
| Upstream relationship | Buzz event kinds, Omarchy extension seams, Nostr proposal | Upstream discussion before large implementation |
| Safety or economic | Spend authority, custody, mainnet, reputation/dispute policy | Threat model, independent review, explicit maintainer approval |
| Public commitment | Grant claim, release promise, partnership, pricing | Evidence pack and maintainer approval |

## Human gates

Agents may prepare decisions but cannot approve:

- mainnet or live value movement;
- custody or delegated signing authority;
- legal commitments, grants, pricing, or partnership representations;
- security-risk acceptance;
- final trademark or branding use;
- publication of material claims or launch announcements;
- changes to this covenant's open-source boundary.

## RFC lifecycle

`idea -> discussion -> draft -> experiment -> accepted | rejected | deferred -> implementation -> retrospective`

Accepted RFCs identify canonical owner, compatibility impact, migration plan, evidence,
security implications, upstream impact, and rollback/reversal path.

## Community evolution

When at least three independent contributors have made sustained, reviewed contributions,
the steward will propose a public maintainer and decision-rights model. When multiple
independent implementations exist, specification governance will be revisited to prevent
one hosted operator from controlling the standard solely through implementation ownership.

