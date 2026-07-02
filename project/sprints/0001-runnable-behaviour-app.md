---
number: 1
status: closed
started: 2026-07-02
ended: 2026-07-02
value_statement: A Reachy Mini owner installs the Hugging Face app and runs a packaged behaviour like dance-to-music on their own device.
artifact_ref: develop (shipped capability, pre-planning-suite)
roadmap_items: [R-1]
features: [F-1]
---

## Goal

A Reachy Mini owner runs a packaged behaviour on their device through the
`reachy_mini` SDK, installed from a Hugging Face app. Success is verified by F-1
`acceptance-1`: a packaged behaviour runs on a Reachy Mini through the SDK.

## Features

- [F-1](../features/runnable-behaviour-package.md) — Runnable behaviour package — status: done

## Out of scope

- The `reachy_mini` SDK and the Reachy Mini hardware themselves (upstream).
- Further behaviours beyond the first (roadmap item R-2, post-MVP).

## Review notes

Retroactive reconciliation (2026-07-02): the `reachy-mini-behavior-app`
capability shipped before this repository adopted the planning suite (issue
nolte/claude-shared#262 mission-authoring backfill). This sprint records roadmap
item R-1 and feature F-1 as `done`, and itself as `closed`, to document the
minimal runnable behaviour package. The repository stays experimental, so more
behaviours remain post-MVP.
