---
mission_statement: "reachy-mini-app packages robot behaviours on the reachy_mini SDK and distributes them as a Hugging Face app, so Reachy Mini owners run behaviours like dance-to-music on their own device."
relevant_outcomes: [O-1, O-2]
audiences:
  - Reachy Mini owner / maker
  - "Maintainer (`nolte`)"
verifies_via: F-1:acceptance-1
time_bound:
  kind: mvp_completion
mvp_status: achieved
created: 2026-07-02
revised_at: null
---

## Statement

`reachy-mini-app` packages robot behaviours on the `reachy_mini` SDK and
distributes them as a Hugging Face app, so Reachy Mini owners run behaviours like
dance-to-music on their own device.

- **Specific** — the statement names *what* (a behaviour package on the
  `reachy_mini` SDK, distributed as a Hugging Face app) and *for whom* (Reachy
  Mini owners and the maintainer, resolved in `audiences`).
- **Measurable** — `verifies_via: F-1:acceptance-1`: a packaged behaviour runs on
  a Reachy Mini through the `reachy_mini` SDK.
- **Achievable** — the minimum viable product is the shipped behaviour package;
  roadmap item R-1 is `mvp: true`, `detail: fine`, `target_sprint: 1`. Further
  behaviours (R-2) are post-MVP.
- **Relevant** — `relevant_outcomes: [O-1, O-2]`, each resolving to an outcome in
  `project/goals.md`.
- **Time-bound** — `time_bound: { kind: mvp_completion }`; the bound is the moment
  the shipped behaviour-app MVP is recorded as achieved.

## Audiences

- **Reachy Mini owner / maker** — the MVP delivers a runnable behaviour package
  (for example dance-to-music) that an owner installs from a Hugging Face app and
  runs on their own Reachy Mini.
- **Maintainer (`nolte`)** — the MVP delivers a behaviour package built on the
  `reachy_mini` SDK that the maintainer extends and distributes as a Hugging Face
  app, on a playground base kept experimental while behaviours mature.

## Verification

The mission is verified by feature **F-1 — Runnable behaviour package**,
acceptance criterion 1: *"A packaged behaviour runs on a Reachy Mini through the
`reachy_mini` SDK."* This is the `verifies_sprint_value` criterion for sprint
0001 and holds against the shipped package, so the minimal MVP is recorded as
`achieved`.

## Source

- **Audience artefact**: `AUDIENCES.md` at the `reachy-mini-app` repository root
  (consulted at its current develop tip); the two `audiences` entries are the
  device owner and the maintainer.
- **Outcomes referenced**: O-1, O-2 from `project/goals.md`.
- **Authored by**: the `mission-define` cascade (issue nolte/claude-shared#262
  mission-authoring backfill), 2026-07-02. The capability is `status:
  experimental`; the MVP is modelled as the minimal runnable behaviour package
  (already shipped), so R-1 is recorded `status: done` and `mvp_status` opens at
  `achieved`, with further behaviours tracked as the post-MVP roadmap item R-2.
