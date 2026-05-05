# Claude Code conventions for reachy-mini-app

This repository is a Reachy Mini behavior package built on the Pollen Robotics /
Hugging Face [`reachy_mini`](https://github.com/pollen-robotics/reachy-mini) SDK.

## Architecture

- `src/reachy_mini_app/` — primary source: behavior implementations as `Move`
  subclasses and lifecycle entry points.
- `tests/` — unit and integration tests; mirror the shape of `src/`.
- `spec/` — requirements, behavior choreography artifacts, and domain knowledge.
- `docs/` — MkDocs source for the published documentation site.

## Command entry points

All reproducible commands run through Taskfile so local and CI behavior stay
identical:

- `task lint` — Ruff lint and format check.
- `task test` — pytest run.
- `task docs` — MkDocs build.

## Conventions

- Source code, comments, identifiers, commit messages, and PR descriptions are
  in English.
- Reachy Mini behaviors follow the Pollen Robotics behavior layout: manifest,
  behavior module with lifecycle hooks, test stub, docs stub.
- Use the `claude-reachy-mini:behavior-scaffold` skill to add a new behavior;
  do not hand-roll the folder shape.
- Use the `claude-reachy-mini:reachy-mini-sdk` skill for guidance on SDK idioms
  (`ReachyMini`, `goto_target`, `play_move`, `Move` subclasses, `mini.imu`,
  `mini.media`, …).

## What lives where

| Concern | Skill / Agent |
|---|---|
| New behavior skeleton | `claude-reachy-mini:behavior-scaffold` |
| SDK idioms | `claude-reachy-mini:reachy-mini-sdk` |
| Dance choreography artifact | `claude-reachy-mini:dance-choreography` |
| On-device test run | `claude-reachy-mini:reachy-mini-on-device` |
| Home Assistant bridge | `claude-reachy-mini:home-assistant-bridge` |
