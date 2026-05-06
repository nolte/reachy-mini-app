# plan.md — reachy-mini-app

> AGENTS.md user-approval gate. **No behavior code is committed until the
> human reviewer signs off below.**
>
> Source: <https://github.com/pollen-robotics/reachy_mini/blob/main/AGENTS.md>

## 1. Understanding

In your own words: what should this app do, on what platform, for whom?

- **Purpose:** Implement the two choreographies stored under
  `spec/choreographies/` as runnable behaviors on Reachy Mini:
  - `drop-it-like-its-hot` (Snoop Dogg feat. Pharrell, 2004 — 93 BPM
    West-Coast-Hip-Hop, 11 sections, 263.4 s)
  - `resistenza-bella-ciao` (Mal Élevé, 2019 — 100 BPM reggae-resistance,
    10 sections, 196.8 s)
- **Target platform:** Reachy Mini Wireless (primary). Lite is best-effort
  but not actively validated in this iteration. Simulation is the smoke-test
  channel only — audio + IMU + servo heat are not testable in sim.
- **Audience:** the developer (me). This is still a Playground project —
  the choreographies are exploration vehicles to learn idiomatic SDK use,
  not a product release.
- **User stories:**
  1. As the operator, I open the FastAPI settings UI, click "Drop It Like
     It's Hot" or "Resistenza", and Reachy plays the corresponding
     choreography end-to-end and returns to idle.
  2. As the operator, I can stop the running choreography at any time
     (UI button or app `stop_event`) and Reachy returns to a safe pose.
  3. As a developer, I can run `pytest tests/` and verify both
     choreographies dispatch without raising under
     `ReachyMini(spawn_daemon=True, use_sim=True)`.

## 2. Technical approach

Which SDK methods, which platform profiles, which architectural pieces?

- **Architecture:** **Variante B (Lite/Playground)** — see the discussion
  log. Deliberately *not* the full `reachy-mini-show` stack:
  - **No** WebSocket server on `:8765`
  - **No** `behaviors/{emotions,social,state,dance,defensive}/` subfolder tree
  - **No** slug registry / `Move` ABC subclasses
  - **No** asyncio main loop with three parallel tasks
  - The choreography spec frontmatter `app_target: reachy-mini-show` is
    knowingly violated for this project — `reachy-mini-app` is a
    Playground, not a show app. If the project ever migrates to a real
    show app, this code is the reference for the migration but is not
    spec-conformant on its own.
- **Module layout:**
  - `reachy_mini_app/blocks.py` — block functions, one per motion slug
    (`sway_side`, `groove_bob`, `spin_look_around`, `waiting_idle`) plus
    accent functions (`proud`, `bow`). Each block takes
    `(reachy, stop_event, **params)` and runs a tight `set_target()` loop
    until either its duration elapses or `stop_event.is_set()`.
  - `reachy_mini_app/choreographies.py` — two top-level functions
    `drop_it_like_its_hot(reachy, stop_event)` and
    `resistenza_bella_ciao(reachy, stop_event)`. Each iterates the section
    list from the spec frontmatter and calls the matching block. Section
    list is encoded as a Python list of dataclass / NamedTuple instances
    inside the file — derived from the YAML, not parsed at runtime.
- **Lifecycle:** `ReachyMiniApp.run(self, reachy_mini, stop_event)` keeps
  the existing demo body but adds two FastAPI endpoints
  (`/play/drop-it-like-its-hot`, `/play/resistenza-bella-ciao`) that set a
  shared "current choreography" reference. The main loop checks: if a
  choreography is requested, dispatch it (blocking, but `stop_event`-aware);
  when finished, return to the demo idle pattern.
- **Motion API:** `set_target(head=…, antennas=…)` for every block — same
  approach as the existing demo body. **No** `play_move()` / `Move` ABC —
  that is part of the show-app stack we're explicitly skipping.
- **Body-yaw handling:** `mini.set_automatic_body_yaw(False)` is set
  before `spin_look_around` runs and reset to `True` afterwards (per
  motion spec). Default for sway/groove blocks is `True`.
- **Audio:** Choreographies run **without audio playback** in this first
  iteration (see Open question #1). `play_sound()` hooks are stubbed out —
  the operator is expected to start the music externally and time the
  click roughly with the choreography start. Audio sync is a follow-up.
- **Test profile:** Existing `tests/test_smoke.py` stays. New test:
  `tests/test_choreographies.py` runs each choreography under
  `ReachyMini(spawn_daemon=True, use_sim=True)`, asserts no exception, and
  measures wall-clock duration is within ±2 s of the section sum from the
  spec frontmatter.

## 3. Open questions

Filled out by the developer; reviewer answers or pushes back.

- [ ] **Audio in or out?** Choreographies are written assuming the track
      plays in parallel from an external source (the spec calls this out
      under "Audio sync"). Options: (a) leave audio out for the first
      iteration — operator plays the song manually (current plan); (b)
      bundle the WAVs (F32LE / 48 kHz / 2 ch per Pollen audio pipeline)
      under `reachy_mini_app/audio/` and trigger
      `reachy_mini.media.play_sound()` at section 1 start. Option (b)
      requires the developer to source / convert the audio files; we
      cannot redistribute commercial recordings via the repo.
- [ ] **`spin-look-around` geometry is TBD per the motion spec.** The
      spec carries a `> ⚠ TBD` on the head-yaw / body-yaw IK math. The
      bridge section will use whatever the spec table says, but the look
      may be ugly until validated on hardware. Acceptable as a first
      iteration?
- [ ] **Bella Ciao BPM and track length are estimates.** The choreography
      frontmatter warns that 100 BPM and 210 s are unverified. First
      iteration will hard-code the estimates; if they're wrong, beats per
      section need adjustment after a hardware listen-through.
- [ ] **Trigger model:** two simple FastAPI POST endpoints (one per
      choreography) on the existing settings UI at `:8042`, plus a
      `/stop` endpoint to cancel the running one. Or do you prefer a
      dropdown + start button? The two-endpoint variant is simpler and
      what I'm proposing.
- [ ] **Idle behavior between choreographies:** when no choreography is
      requested, what should Reachy do? Options: (a) the existing demo
      sinusoidal yaw + antennas; (b) `waiting-idle` block (which we
      implement anyway for the choreography intros); (c) hold a neutral
      pose. Proposing (b) for consistency.
- [ ] **HF Space publish stays at `--publish=false` for now.** Publish
      path can be triggered later via `reachy-mini-app-assistant publish`
      once a behavior is sign-off-quality. Confirm?

## 4. Approval gate

| Field | Value |
|---|---|
| Reviewer | nolte (`nolte07@gmail.com`) |
| Approved on | 2026-05-06 |
| Approved revision (commit SHA) | _filled after first commit_ |
| Notes / scope adjustments | All six default answers in section 3 accepted as proposed: audio out, spin-look-around TBD acceptable for v1, Bella Ciao BPM estimate acceptable for v1, two FastAPI POST endpoints + `/stop`, `waiting-idle` between choreographies, HF publish stays off. |

**Until this section is filled and signed, do not commit any behavior
code beyond what `reachy-mini-app-assistant create` produced. The
out-of-the-box CLI demo body is fine; bespoke logic is not.**
