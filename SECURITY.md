# Security Policy

## Reporting

Do not open a public issue for an exploitable vulnerability, leaked secret, wallet risk,
or private user data. Use GitHub private vulnerability reporting once enabled for the
repository. Until then, contact the maintainer privately through the contact method in
the GitHub profile.

## Scope assumptions

- Fixture, dry-run, localnet, and devnet are not interchangeable with production safety.
- A signed Nostr event proves authorship of that event, not payment settlement.
- x402 payment evidence is not automatically escrow, refund, or dispute resolution.
- Quattro plugins are unsandboxed and share the user's session permissions.
- Mainnet, custody, and unattended signing remain blocked pending explicit workstreams.

## Supply chain

Published distributions will require pinned provenance, SBOMs, signed artifacts,
dependency review, reproducible-build evidence where practical, and a documented rollback.
Third-party plugins and agent definitions remain untrusted until conformance and policy
checks complete.

