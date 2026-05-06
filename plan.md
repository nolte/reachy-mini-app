# plan.md — reachy-mini-app

> AGENTS.md user-approval gate. **No behavior code is committed until the
> human reviewer signs off below.**
>
> Source: <https://github.com/pollen-robotics/reachy_mini/blob/main/AGENTS.md>

## 1. Understanding

In your own words: what should this app do, on what platform, for whom?

- **Purpose:** Playground projekt — exploration sandbox for Reachy Mini SDK
  idioms. No specific user-visible behavior is committed yet; the app is
  intentionally a clean slate beyond the CLI demo body.
- **Target platform:** Reachy Mini Wireless (primary), Lite (best-effort —
  no IMU, no audio), Simulation (CI default).
- **User stories not yet defined.** TODO: fill in once a concrete behavior
  is selected (e.g., dance to a specific song, react to Home Assistant
  state changes, etc.).

## 2. Technical approach

Which SDK methods, which platform profiles, which architectural pieces?

- **Lifecycle:** `ReachyMiniApp.run(self, reachy_mini, stop_event)` — the
  Pollen-canonical entry point. Loop until `stop_event.is_set()`.
- **Motion API:** `set_target(head=..., antennas=...)` for tight loops,
  `goto_target(...)` / `play_move(...)` for choreographed motion. Decision
  per-behavior.
- **Settings UI:** the demo body uses `self.settings_app` (FastAPI mounted at
  `custom_app_url`). Keep or remove based on whether the behavior needs
  runtime parameters.
- **Static assets:** `reachy_mini_app/static/` for any web UI; `index.html`
  + `style.css` at repo root for the HF Space landing.
- **Test profile:** `ReachyMini(spawn_daemon=True, use_sim=True)` — see
  `tests/test_smoke.py`. Hardware-only assertions belong to the
  `reachy-mini-on-device` agent.

Choreography artifacts (e.g., `spec/choreographies/*.md`) are authoring
inputs — translation to `Move` subclasses or in-loop motion happens in
`reachy_mini_app/main.py`.

## 3. Open questions

Filled out by the developer; reviewer answers or pushes back.

- [ ] What is the first concrete behavior? (Dance to a track, idle ambient
      motion, Home Assistant reactive, …)
- [ ] Does this app need audio? If yes, which backend
      (`gstreamer`, `gstreamer_no_video`, `default`)? Note: Lite has no
      audio.
- [ ] Does it need a settings UI? If no, remove `custom_app_url` and the
      `self.settings_app` block from `main.py`.
- [ ] Should the existing `spec/choreographies/*.md` artifacts be
      translated into actual moves now, or kept as reference for a later
      behavior?
- [ ] Where will hardware testing happen — Wireless on the developer's
      desk, or via a remote `reachy-mini-on-device` run?
- [ ] HF Space publish later, or stays local? Currently scaffolded
      with `--publish=false`.

## 4. Approval gate

| Field | Value |
|---|---|
| Reviewer | _human reviewer name here_ |
| Approved on | _date_ |
| Approved revision (commit SHA) | _SHA_ |
| Notes / scope adjustments | _free text_ |

**Until this section is filled and signed, do not commit any behavior
code beyond what `reachy-mini-app-assistant create` produced. The
out-of-the-box CLI demo body is fine; bespoke logic is not.**
