# Market and technical refresh — evidence record (2026-08-31)

This is the in-repository record of an internal report that is not publicly resolvable.
It exists so that every claim `ADR-0002` and `research/SOURCES.yaml` take from that report
can be checked without access to the author's machine.

## Provenance

- Original location at access time: `/home/nissan/Projects/Redditech/data/reddi-market-technical-refresh/report.md`
- Accessed: 2026-08-31; re-read for this record: 2026-09-01
- Length at access: 311 lines
- SHA-256 of the accessed file: `92102caee8ae90f03a41486a45aec0164a340f5f8361e721e872052a5638f4fd`

The full report is not reproduced here. Publishing it is an `external-publication` human
gate, and the report's externally checkable content is its citations, which are registered
individually in `research/SOURCES.yaml` and were verified against their own primary
artifacts rather than against this report.

## Cited excerpt

The only claim this programme takes from the report as evidence rather than as a pointer is
this row of its assumption-validation table. Quoted verbatim:

> | Solana/AUDD/x402 is a good first adapter profile. | **Valid but weakened as the sole critical technical proof** | It remains a useful profile, but MPP, Stripe x402, AP2 mandates, and conventional/card semantics now make a second materially different fixture mandatory earlier. Solana/AUDD/x402 cannot stand in for agent-commerce neutrality. | High |

`docs/decisions/0002-adapter-and-projection-first.md` records this finding as contrary
evidence that the 2026-09-01 amendment knowingly overrides, and states the reasoning.

## Verification note

If the original file is re-read and its digest differs from the value above, treat this
record as stale: re-transcribe the excerpt and re-check the ADR amendment before relying
on either.
