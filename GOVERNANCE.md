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

## Delivery and merge policy

This section is the canonical portfolio delivery policy. Agent instructions, contributor
guidance, and the pull-request template point here rather than restating competing rules.
It is process policy; it does not claim that branch protection, required checks, or an
automated merge control currently enforce it.

A change is merge-eligible only when all of the following refer to one full, unchanged
final commit:

1. permitted repository validation and actual hosted checks are green;
2. a fresh independent Claude-family reviewer returns explicit `GO`;
3. a fresh independent Codex reviewer returns explicit `GO`;
4. neither reviewer authored the change, both used only their granted read/review
   permissions, and repository settings/tree integrity evidence is retained; and
5. each reviewer explicitly acknowledges any linked, deduplicated deferrals.

A changed head invalidates both verdicts. `NO-GO`, silence, a partial review, a verdict on
another SHA, or a review obtained by bypassing permissions is never reinterpreted as
`GO`. Review must not persistently change reviewer settings or use unattended blanket
confirmation. After these conditions hold, Firstmate has conditional authority to merge
the unchanged head; the implementation worker and reviewers do not merge their own work.

Review severity describes consequence, not planned feature completeness. Critical/high
findings are corrected in the current delivery cycle. Medium/low findings are deduplicated
against the owning repository, filed once with exact provenance and acceptance criteria,
and linked as backlog; they do not silently expand the current change. Reviewers must say
whether the unchanged head is `GO` with those named deferrals. If a deferred item is
actually critical/high, it cannot be relabelled merely to obtain approval.

Stop correction cycling when the same causal finding recurs without durable progress or
when a stable external wait begins. Preserve a safe checkpoint and escalate with the
review evidence; do not keep generating review rounds, lower severity without evidence,
switch tiers mid-validation, or discard work under review. Planned scope that a change
does not claim to deliver is not automatically a security defect.

Closing keywords (`closes`, `fixes`, or `resolves`) are used only when the PR completes the
named issue's acceptance. Plan-only, partial, evidence-preparation, and follow-up PRs use
`refs`. This semantic rule protects legitimate complete closures rather than banning all
closing keywords.

## Task, model, and effort routing

Firstmate owns dispatch. Before dispatch or resume it checks current catalog and
authentication provenance, short-window and weekly quota/pace/reset/runway, and the
visible active fleet. Unknown quota is recorded as uncertainty. No more than three active
workers in one provider family may run across the visible fleet, and aliases, homes or
model names do not evade that cap. Final independent-review capacity is reserved.

| Work type | Default route |
|---|---|
| Deterministic extraction, counting, joins, graph/projection checks | Script first; no model when deterministic tooling is sufficient. |
| Narrow bounded mechanical edit | Lowest adequate tier and low effort. |
| Substantive implementation, documentation package, or ordinary review | Sufficient moderate tier and effort. |
| Ambiguous contract, consequential security/economic judgment, or conflicting evidence | High reasoning only when the concrete ambiguity or risk is recorded in the task. |

Stable waits are genuinely idle without model calls. Capacity is reassessed before resume;
model tiers are not changed and work custody is not discarded mid-validation merely to
save usage. Provider-specific optimisations may be overlays, never the portable policy.

## Community evolution

When at least three independent contributors have made sustained, reviewed contributions,
the steward will propose a public maintainer and decision-rights model. When multiple
independent implementations exist, specification governance will be revisited to prevent
one hosted operator from controlling the standard solely through implementation ownership.

