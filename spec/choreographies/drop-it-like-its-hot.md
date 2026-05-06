---
name: drop-it-like-its-hot
description: West-Coast-Hip-Hop choreography for Snoop Dogg feat. Pharrell — Drop It Like It's Hot (2004); laid-back swagger over a 93 BPM tongue-click + bass beat
bpm: 93
genre: hip-hop (west-coast)
mood: smooth-swagger
duration_s: 271
platform: any
motion_catalog_ref: spec/reachy-mini/motions/
app_target: reachy-mini-show
protocol_version: "1.0"
mood_arc: [calm, playful, playful, release]
sections:
  - section: intro
    slug: waiting-idle
    bpm: null
    beats: null
    duration_s: 8.0
    lead_time_s: 0.0
    accent_slug: null
    notes: "tongue-click intro phase — Reachy idles, builds attention before the first verse"
  - section: verse
    slug: sway-side
    bpm: 93
    beats: 50
    duration_s: 33.1
    lead_time_s: 0.05
    accent_slug: null
    notes: "Pharrell's verse 1 — smooth side-to-side, 25 sway cycles at T_cycle=1.29s"
  - section: pre-chorus
    slug: groove-bob
    bpm: 93
    beats: 32
    duration_s: 21.3
    lead_time_s: 0.05
    accent_slug: proud
    notes: "energy lift into the hook — pitch-bob with a single proud accent at section start"
  - section: chorus
    slug: groove-bob
    bpm: 93
    beats: 48
    duration_s: 31.7
    lead_time_s: 0.05
    accent_slug: null
    notes: "hook 1 — drop it like it's hot, drop it like it's hot"
  - section: verse
    slug: sway-side
    bpm: 93
    beats: 60
    duration_s: 39.5
    lead_time_s: 0.05
    accent_slug: null
    notes: "Snoop's verse 2 — 30 sway cycles, antennas asymmetric per sway-side spec"
  - section: chorus
    slug: groove-bob
    bpm: 93
    beats: 48
    duration_s: 31.7
    lead_time_s: 0.05
    accent_slug: null
    notes: "hook 2"
  - section: bridge
    slug: spin-look-around
    bpm: null
    beats: null
    duration_s: 9.0
    lead_time_s: 0.0
    accent_slug: null
    notes: "single show moment — pseudo look-around spin (7s per spec) plus 2s recovery; MUST set automatic_body_yaw=False during this section, max_body_yaw stays ≤ ±150°"
  - section: verse
    slug: sway-side
    bpm: 93
    beats: 50
    duration_s: 33.1
    lead_time_s: 0.05
    accent_slug: null
    notes: "Snoop's verse 3 — back to the smooth sway"
  - section: chorus
    slug: groove-bob
    bpm: 93
    beats: 48
    duration_s: 31.7
    lead_time_s: 0.05
    accent_slug: null
    notes: "hook 3 — final hook"
  - section: outro
    slug: sway-side
    bpm: 93
    beats: 24
    duration_s: 16.3
    lead_time_s: 0.05
    accent_slug: proud
    notes: "fade-out with a proud accent — 12 sway cycles back to neutral"
  - section: outro-idle
    slug: waiting-idle
    bpm: null
    beats: null
    duration_s: 8.0
    lead_time_s: 0.0
    accent_slug: null
    notes: "tongue-click outro fade — set loop_count=None for unbounded loop until external stop signal"
warnings:
  - "Section duration sum 263.4s vs. target 271s = -2.8 % (within ±10 % tolerance, so green)"
  - "mood_arc has 4 tokens mapped onto 11 sections — track has no classic rising→peak curve, mapping is intentionally loose; revisit when the skill specifies mood_arc-vs-section-count behavior"
  - "platform: any — BPM 93 is safely inside every block's hardware range; no platform-specific clamp needed for this choreography"
---

# Drop It Like It's Hot — Reachy Mini choreography

## Context

Choreography for *Snoop Dogg feat. Pharrell — Drop It Like It's Hot* (2004): a 93 BPM, 4:31 West-Coast-Hip-Hop track defined by Pharrell's minimal tongue-click and sub-bass production. The choreography stays in laid-back swagger mode the whole way through — `sway-side` carries the verses, `groove-bob` carries the three hooks, one `spin-look-around` acts as the single show moment in the middle bridge, and `proud` accents underline the swagger feeling at the pre-hook and the outro. No `headbang-soft` is used: the track is intentionally low-aggression, and head-banging would read as the wrong genre.

## Section table

| # | Section | Slug | BPM | Beats | Duration (s) | Lead time (s) | Accent | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | intro | `waiting-idle` | — | — | 8.0 | 0.00 | — | tongue-click intro phase |
| 2 | verse | `sway-side` | 93 | 50 | 33.1 | 0.05 | — | Pharrell verse 1 |
| 3 | pre-chorus | `groove-bob` | 93 | 32 | 21.3 | 0.05 | `proud` | energy lift into the hook |
| 4 | chorus | `groove-bob` | 93 | 48 | 31.7 | 0.05 | — | hook 1 |
| 5 | verse | `sway-side` | 93 | 60 | 39.5 | 0.05 | — | Snoop verse 2 |
| 6 | chorus | `groove-bob` | 93 | 48 | 31.7 | 0.05 | — | hook 2 |
| 7 | bridge | `spin-look-around` | — | — | 9.0 | 0.00 | — | single show moment, `automatic_body_yaw=False` |
| 8 | verse | `sway-side` | 93 | 50 | 33.1 | 0.05 | — | Snoop verse 3 |
| 9 | chorus | `groove-bob` | 93 | 48 | 31.7 | 0.05 | — | hook 3, final hook |
| 10 | outro | `sway-side` | 93 | 24 | 16.3 | 0.05 | `proud` | fade-out with proud accent |
| 11 | outro-idle | `waiting-idle` | — | — | 8.0 | 0.00 | — | tongue-click outro, then `loop_count=None` |

Section duration sum: 263.4 s vs. track length 271 s (−2.8 %, inside the ±10 % tolerance window).

Slug references (open these for pose tables, easing, and acceptance criteria during translation):

- [`spec/reachy-mini/motions/sway-side/de.md`](../spec/reachy-mini/motions/sway-side/de.md) — 50–140 BPM range, asymmetric antennas per sway direction, `automatic_body_yaw=True` recommended
- [`spec/reachy-mini/motions/groove-bob/de.md`](../spec/reachy-mini/motions/groove-bob/de.md) — 60–180 BPM range, pitch-only bob, antennas stationary at +15°
- [`spec/reachy-mini/motions/spin-look-around/de.md`](../spec/reachy-mini/motions/spin-look-around/de.md) — 7 s sequence, `automatic_body_yaw=False` MUST, body-yaw ≤ ±150°
- [`spec/reachy-mini/motions/waiting-idle/de.md`](../spec/reachy-mini/motions/waiting-idle/de.md) — idle / breathing default, loop-able
- [`spec/reachy-mini/motions/proud/de.md`](../spec/reachy-mini/motions/proud/de.md) — emotion accent only, never the rhythmic main channel

## Platform consequences

| Platform | Status | Notes |
|---|---|---|
| Reachy Mini (Wireless) | full | All sections playable; IMU temperature polling not strictly required because no `headbang-soft` is used; sustained `sway-side` at 93 BPM with antenna asymmetry plus `automatic_body_yaw=True` is mild compared to the brown-out scenarios in `control-surface` (well below the simultaneous-full-load case) |
| Reachy Mini Lite | full | Same as Wireless minus IMU read; no `headbang-soft`, so no thermal-budget concern; external power supply means no brown-out risk |
| Simulation | partial | Pose / antenna sequences run; **no audio playback** (the song must be played from another source synced to the choreography), **no IMU telemetry** (`mini.imu` returns `None`), **no real servo heat** to verify; on-hardware validation is required for final sign-off via the `reachy-mini-on-device` agent |

The bridge section uses `spin-look-around` (7 s + 2 s recovery). Per its motion spec, `automatic_body_yaw=False` MUST be set for the duration of the section; the developer toggles it back to `True` for sections 8–10 so `sway-side` and `groove-bob` get the natural body-follow.

## Translation checklist for the developer

1. For each section slug, instantiate the matching `Move` subclass from `reachy_mini_show/behaviors/`:
   - sections 1, 11: `WaitingIdle(loop_count=None)` for section 11 (unbounded), `WaitingIdle(duration_s=8.0)` for section 1
   - sections 2, 5, 8, 10: `SwaySide(bpm=93, beats=<beats>, lead_time_s=0.05)` with `beats` as in the section table — note that `sway-side` requires `beats` to be even (every value in this choreography satisfies that)
   - sections 3, 4, 6, 9: `GrooveBob(bpm=93, beats=<beats>, lead_time_s=0.05)`
   - section 7: `SpinLookAround()` (the spec defines a fixed 7 s sequence; budget 2 s for transition recovery before section 8 starts)
2. Pass BPM, beats, and lead time as constructor parameters exactly as listed in the YAML frontmatter — do not reinterpret the lead time, it is the audio-pipeline-latency compensation per `groove-bob` / `sway-side` specs.
3. The two `accent_slug: proud` entries (sections 3 and 10) are **emotion overlays**, not rhythmic main channels. Trigger `Proud()` once at the start of the section and let the dance block continue underneath; do not loop the proud accent.
4. Section 7 (`spin-look-around`) MUST set `mini.set_automatic_body_yaw(False)` before the move starts and `mini.set_automatic_body_yaw(True)` after section 7 finishes, before section 8 begins. Per the spin-look-around spec, treat the body-yaw values in the spec table as a draft until the IK math is verified against real hardware (the spec carries a `> ⚠ TBD` on the head-yaw / body-yaw geometry).
5. Audio sync: align the `play_sound(file=...)` call for *Drop It Like It's Hot* with section 1's start, accounting for the ~50 ms GStreamer audio buffer (per `control-surface` spec). Beat detection is **not** part of this choreography — BPM is hard-coded to 93. The planned `audio-beat-tracking` skill can replace the hard-coded BPM with a live beat estimate later; until then, manual sync is required.
6. Test against `ReachyMini(use_sim=True)` first — verify no slug raises and the duration sum lands within ±2 s of 263.4 s. Then dispatch the `reachy-mini-on-device` agent for hardware validation of the swagger feel and the bridge spin.
7. Platform fallbacks for this choreography are minimal because `headbang-soft` is intentionally absent; no servo-heat fallback is needed. The only platform-conditional logic is the IMU read in section 1's Wireless idle (which doesn't apply to this choreography either).

## Open questions

- The `mood_arc=[calm, playful, playful, release]` has 4 tokens mapped loosely onto 11 sections because *Drop It Like It's Hot* has no classic rising → peak energy curve. The skill spec carries this as a known open question (mood_arc length vs. section count). Empirically, the choreography reads as smooth-throughout without a peak — verify on hardware whether that matches the song or whether the third hook should bias toward a slightly higher BPM (e.g. `groove-bob` at 95–96 BPM) for a perceived lift. The `control-surface` spec allows ±5–15 % timing variation for liveliness, so a small BPM bump in section 9 would not violate any rule.
- Section 7's bridge uses `spin-look-around` once. An alternative would be to insert a second emotion accent (`curious` or `confused`) instead of the spin and keep the dance pattern continuous — that variant feels more "smooth West-Coast" and less "show piece". Decide on hardware which reading the audience expects.
- The choreography lives at `choreographies/drop-it-like-its-hot.md` inside the **plugin repo** as a demo / example. Per `spec/reachy-mini/app-architecture/de.md`, choreographies for production use belong inside the **`reachy-mini-show` app repo** (suggested home: `reachy_mini_show/choreographies/`). Move the file there before the developer integrates it into the slug registry.
