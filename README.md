---
title: Reachy Mini App
emoji: 👋
colorFrom: red
colorTo: blue
sdk: static
pinned: false
short_description: Playground projekt
tags:
 - reachy_mini
 - reachy_mini_python_app
---

# reachy-mini-app

Playground projekt — a Reachy Mini app scaffolded via Pollen Robotics'
official `reachy-mini-app-assistant create` CLI and the
[`claude-reachy-mini`](https://github.com/nolte/claude-reachy-mini) plugin's
`app-scaffold` skill.

## Provenance

| Source | Link |
|---|---|
| Plugin | <https://github.com/nolte/claude-reachy-mini> |
| SDK | <https://github.com/pollen-robotics/reachy_mini> |
| Specs | <https://github.com/nolte/claude-reachy-mini/tree/develop/spec/reachy-mini/> |
| Scaffold skill | [`app-scaffold`](https://github.com/nolte/claude-reachy-mini/blob/develop/skills/app-scaffold/SKILL.md) |

## Platform applicability

| Platform | Applicable? | Notes |
|---|---|---|
| Reachy Mini Wireless | yes | full SDK surface; verify on hardware via `reachy-mini-on-device` agent |
| Reachy Mini Lite | partial | no IMU, no audio backend; behaviors that depend on these will skip / fail |
| Simulation (`use_sim=True`) | yes (CI default) | runs without hardware; cannot verify audio playback, IMU telemetry, LED sync, true pose convergence |

## Quickstart

```bash
# install in editable mode
uv pip install -e .

# run the smoke test (simulation, no hardware required)
pytest tests/

# publish to Hugging Face Spaces (when ready)
reachy-mini-app-assistant publish .
```

## Status

`plan.md` at the repo root captures the intent, approach, and open questions
for this app. **Do not commit behavior code until `plan.md` is approved by
the human reviewer** — this is the AGENTS.md user-approval gate.
