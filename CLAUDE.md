# Claude Code conventions for reachy-mini-app

This is a Reachy Mini app scaffolded via Pollen Robotics' official
`reachy-mini-app-assistant create` CLI, wrapped by the
[`claude-reachy-mini`](https://github.com/nolte/claude-reachy-mini) plugin's
`app-scaffold` skill.

The app skeleton (entry point, manifest, package layout, HF Space landing
page) is owned by the upstream CLI — never hand-edit those structural pieces.

## Architecture

- `reachy_mini_app/main.py` — `ReachyMiniApp` subclass; entry point in the
  `reachy_mini_apps` group. Behavior logic lives inside `run(self, reachy_mini, stop_event)`.
- `reachy_mini_app/static/` — **runtime** web UI for the FastAPI settings app
  exposed at `custom_app_url` while the app runs on the device. Served by
  FastAPI as `/static/*`. Optional: drop the folder if the app sets
  `custom_app_url = None`.
- `index.html` + `style.css` (repo root) — **discovery-time** Hugging Face
  Space landing page, rendered by HF because the README frontmatter declares
  `sdk: static`. Pollen requires these at the repo root; their presence is
  enforced by `reachy-mini-app-assistant check`. **They are not duplicates of
  `static/`** — different audience (HF visitors vs. on-device operator),
  different lifecycle, different host.
- `tests/` — pytest; smoke test runs against `ReachyMini(spawn_daemon=True, use_sim=True)`.
- `spec/` — local specifications and choreography artifacts.

## Plugin skills and agents

| Concern | Skill / Agent |
|---|---|
| New app skeleton | [`claude-reachy-mini:app-scaffold`](https://github.com/nolte/claude-reachy-mini/blob/develop/skills/app-scaffold/SKILL.md) |
| SDK idioms (`ReachyMini`, `goto_target`, `play_move`, `Move`, `mini.imu`, `mini.media`) | [`claude-reachy-mini:reachy-mini-sdk`](https://github.com/nolte/claude-reachy-mini/blob/develop/skills/reachy-mini-sdk/SKILL.md) |
| Dance choreography artifact | [`claude-reachy-mini:dance-choreography`](https://github.com/nolte/claude-reachy-mini/blob/develop/skills/dance-choreography/SKILL.md) |
| Deploy app to a real Reachy Mini (sync + install + verify) | [`claude-reachy-mini:reachy-mini-deploy`](https://github.com/nolte/claude-reachy-mini/blob/develop/agents/reachy-mini-deploy.md) |
| Start an installed app on a real Reachy Mini | [`claude-reachy-mini:reachy-mini-start`](https://github.com/nolte/claude-reachy-mini/blob/develop/skills/reachy-mini-start/SKILL.md) |
| Live test on real Reachy Mini | [`claude-reachy-mini:reachy-mini-on-device`](https://github.com/nolte/claude-reachy-mini/blob/develop/agents/reachy-mini-on-device.md) |
| Home Assistant integration | [`claude-reachy-mini:home-assistant-bridge`](https://github.com/nolte/claude-reachy-mini/blob/develop/skills/home-assistant-bridge/SKILL.md) |

## User-approval gate (AGENTS.md convention)

Before any behavior code is committed, fill out `plan.md` and obtain
explicit human approval. The plan is the contract that traps approach drift
early. The four required sections are: Understanding, Approach, Open
questions, Approval gate.

## Conventions

- Source code, comments, identifiers, commit messages, and PR descriptions
  are written in English.
- Don't hand-roll the app folder shape — the upstream CLI owns
  `pyproject.toml`, `main.py`, `README.md` frontmatter, `index.html`,
  `style.css`, and the entry-point declaration.
- Run `reachy-mini-app-assistant check .` after any structural change to
  confirm the Pollen contract still holds.
