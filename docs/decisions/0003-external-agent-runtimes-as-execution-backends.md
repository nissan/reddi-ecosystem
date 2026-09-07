# ADR-0003: External agent runtimes as RAP execution backends

- Status: proposed
- Date: 2026-09-06
- Decision owner: programme steward
- Affected graph nodes/repositories: ECO-024, ECO-026, ECO-030, ECO-035, ECO-040, ECO-044, ECO-045, ECO-054; ecosystem, adl-lab, rap, arena
- Review/expiry: accept, amend, or reject before the M2 runtime-adapter contract is frozen

## Context and decision

Buzz, OpenClaw, Firstmate, and Hermes now provide overlapping but distinct parts of a
human-directed multi-agent system. Reddi should not reproduce their general orchestration,
messaging, memory, worktree, or runtime responsibilities.

RAP owns portable economic-work agreements, lifecycle observations, evidence binding,
judgment, settlement receipts, disputes, and reputation. ADL owns portable agent capability,
dependency, authority, and deployment declarations. Arena owns conformance and evaluation.
External systems remain replaceable execution or collaboration backends:

- OpenClaw is the first general-purpose reference runtime and Gateway integration target;
- Firstmate is the reference coding-crew and worktree delivery target;
- Hermes is the reference durable profile, memory, skill, and messaging-agent target;
- Buzz is the reference multi-human/multi-agent collaboration and Nostr projection target.

All integrations use a versioned runtime adapter contract. Project-name compatibility is never
claimed without a pinned revision/version and a passing conformance record.

## Constraints and non-goals

- Runtime-specific configuration is an ADL deployment projection, not portable ADL identity.
- Skills and prompts guide behavior but do not enforce payment, custody, publication, or
  approval authority.
- A profile, session, worktree, or working directory is not accepted as a security sandbox
  without effective-permission evidence.
- Nostr messages, chat transcripts, model claims, and agent completion messages are
  observations, not authoritative settlement evidence.
- The ecosystem repository coordinates this decision but does not take ownership of canonical
  ADL semantics, RAP implementation, or Arena rules.

## Primary evidence and confidence

Primary upstream repositories and documentation are registered in `research/SOURCES.yaml`.
Confidence is high that the systems expose materially different extension and orchestration
surfaces. Compatibility confidence remains unknown until ECO-026 pins versions and ECO-024
publishes conformance results.

## Options

1. Build a new Reddi orchestration runtime. Rejected as duplicative and likely to dilute RAP.
2. Hard-code one preferred runtime. Rejected because it would undermine ADL portability and
   make runtime implementation details accidental protocol semantics.
3. Use capability-negotiated adapters with named reference implementations. Proposed.

## Experiment or validation

1. Define a deterministic mock adapter and common lifecycle/evidence fixtures.
2. Prove the contract through OpenClaw at a pinned version.
3. Run the same task through Firstmate and Hermes without changing portable ADL or RAP core.
4. Project the lifecycle into Buzz only after the execution/evidence join gate passes.
5. Compare declared Agent BOM authority with observed runtime permissions and recovery.

## Security, privacy, economic, compatibility, and upstream impact

Each Gateway/runtime instance has an explicit identity and trust boundary. Evidence identifies
the runtime, underlying harness/model where disclosed, parent/child sessions, tools, artifacts,
and verifier. Private memory and hidden reasoning are excluded from public evidence. Signing and
settlement occur in deterministic, policy-enforced components outside model-generated text.

Adapters prefer stable public extension seams. Generic fixes, tests, and documentation are
offered upstream before downstream patches or forks. Dependency upgrades run compatibility and
Arena smoke tests before adoption.

## Consequences, migration, and rollback

The M2 scope gains an explicit runtime contract, mock, version matrix, and reference adapter
proof. OpenClaw is evaluated first because it is already part of the local Reddi operating
environment; this is a validation priority, not a permanent dependency.

An adapter can be disabled or removed without changing RAP receipts or portable ADL. If an
upstream seam proves unstable, its support state becomes experimental or unsupported while the
mock and other conforming runtimes remain valid.
