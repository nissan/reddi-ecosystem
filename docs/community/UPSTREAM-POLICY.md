# Upstream-first policy

Reddi succeeds by making Buzz, Nostr, Omarchy, and the broader agent ecosystem more
useful—not by quietly extracting their work into an opaque downstream product.

## Before downstream implementation

1. Read the upstream contribution guide, architecture, roadmap, license, and trademark rules.
2. Search issues, discussions, and pull requests for the proposed extension.
3. Open a design discussion for any material architectural change.
4. Prefer a generic capability that benefits upstream users over a Reddi-only hook.
5. Record the decision and expected rebase/maintenance cost in the upstream register.

## Patch order

1. Documentation correction, test, or bug fix directly upstream.
2. Generic extension seam directly upstream.
3. Thin public adapter/sidecar maintained downstream.
4. Temporary patch queue with an upstream issue and exit condition.
5. Maintained fork only after an ADR proves the other paths insufficient.

## Fork obligations

A fork decision names maintainers, upstream revision, sync cadence, security intake,
release policy, patch register, rebase budget, license/notice handling, and exit strategy.
Names and visual identity must not imply endorsement. Apache-2.0 or MIT permission is
not trademark permission.

## Community reciprocity measures

- upstream issues opened and resolved;
- generally useful patches submitted, accepted, and maintained;
- review latency and respectful response rate;
- documentation and reproducible examples contributed;
- downstream-only patch count and age;
- contributors who move between communities;
- funds or maintainer time returned to critical dependencies.

These measures complement adoption and revenue; they are not marketing decorations.

## Buzz and Nostr specifics

- Start with a sidecar that consumes stable Buzz/Nostr interfaces.
- Reuse documented job events where semantics match; propose versioned extensions where they do not.
- Never claim a Nostr event proves payment, settlement, or spend authority.
- Document relay trust, event deletion limits, encryption, metadata leakage, and replay behavior.
- Contribute generic extension points, tests, and documentation to Buzz before carrying a fork.

## Omarchy and Quattro specifics

- Keep the public Quattro plugin thin and inspectable.
- Put signing, wallet policy, sandboxing, updates, and protocol services outside QML.
- Respect plugin constraints; do not hide installers or privilege escalation in a plugin.
- Contribute generic shell/plugin defects and documentation upstream.
- Treat “Reddi Machine” as a downstream distribution, never as official Omarchy endorsement.

