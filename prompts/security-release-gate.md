# Security and release gate

Decide whether the exact candidate release and public claim are ready.

Verify source revision, clean build, tests/evals, dependency/SBOM, provenance/signatures, secret
scan, threat model, permissions, update/rollback, incident path, license/notices, data/privacy,
environment labels, and reproducible evidence. Exercise failure and recovery. For agents, compare
declared and effective tools/authority. For payments, reconcile to the authoritative rail.

Return `approve`, `approve-with-explicit-limitations`, or `block` with evidence. Approval of a
package does not approve mainnet, live spend, custody, external publication, or a broader claim.

