---
id: F-1
title: Runnable behaviour package
status: done
roadmap_item: R-1
sprint: 1
created: 2026-07-02
ended: 2026-07-02
verifies_sprint_value: acceptance-1
consistency_check:
  performed_at: 2026-07-02
  agent_version: manual-fallback (retroactive; feature-consistency-reviewer not run cross-repo)
  findings:
    - kind: clean
      target: project/features/
      resolution: proceed
      evidence: "project/features/ empty (first decomposition); no feature-to-feature overlap possible."
    - kind: prior-art
      target: the shipped behaviour package
      resolution: proceed
      evidence: "The behaviour package on the reachy_mini SDK already exists; F-1 documents the run contract, it does not build new behaviours."
---

## Description

F-1 is the mission-verifying feature for the shipped `reachy-mini-behavior-app`
capability. The behaviour package is built on the Pollen Robotics / Hugging Face
`reachy_mini` SDK and runs at least one robot behaviour. The contract is met when
a packaged behaviour runs on a Reachy Mini through the SDK. This holds against the
shipped package, so the feature is recorded `done` as part of the retroactive MVP
reconciliation (issue nolte/claude-shared#262).

## Acceptance criteria

- [x] **acceptance-1** A packaged behaviour runs on a Reachy Mini through the
  `reachy_mini` SDK. _(This is the sprint value verifier.)_
- [x] **acceptance-2** The behaviour package is distributable as a Hugging Face
  app.
- [x] **acceptance-3** At least one concrete behaviour (for example
  dance-to-music) is packaged.

## Test hooks

- **acceptance-1** — run the packaged behaviour against a device or the SDK — passing.
- **acceptance-2** — the Hugging Face app packaging — passing.
- **acceptance-3** — inspect the packaged behaviour — passing.

## Consistency notes

Retroactive documentation feature: the behaviour package predates the planning
suite. No new implementation is introduced; the feature exists so the mission's
`verifies_via: F-1:acceptance-1` and sprint 1's `value_statement` resolve to a
real acceptance criterion. The repository is experimental, so further behaviours
are the post-MVP roadmap item R-2.

## References

- `project/portfolio.yml` capability `reachy-mini-behavior-app`
- `AUDIENCES.md` audience "Reachy Mini owner / maker"
- `README.md` (the behaviour package and Hugging Face app)
