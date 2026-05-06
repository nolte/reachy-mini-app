---
name: resistenza-bella-ciao
description: Reggae-resistance choreography for Mal Élevé — Resistenza (Bella Ciao); dignified solidarity over a 100 BPM Bella-Ciao adaptation, building from solemn sway to a proud final hook
bpm: 100
genre: reggae (political / resistance)
mood: solemn-resistance
duration_s: 210
platform: any
motion_catalog_ref: spec/reachy-mini/motions/
app_target: reachy-mini-show
protocol_version: "1.0"
mood_arc: [solemn, rising, peak, release]
sections:
  - section: intro
    slug: waiting-idle
    bpm: null
    beats: null
    duration_s: 6.0
    lead_time_s: 0.0
    accent_slug: null
    notes: "guitar / acoustic intro phase — Reachy idles in dignified attention before the first verse"
  - section: verse
    slug: sway-side
    bpm: 100
    beats: 50
    duration_s: 30.8
    lead_time_s: 0.05
    accent_slug: null
    notes: "verse 1 — Reggae sway, 25 cycles at T_cycle=1.20s, antennas asymmetric per sway-side spec"
  - section: chorus
    slug: sway-side
    bpm: 100
    beats: 40
    duration_s: 24.8
    lead_time_s: 0.05
    accent_slug: proud
    notes: "Bella-Ciao refrain 1 — proud accent at section start to underline the resistance theme"
  - section: verse
    slug: sway-side
    bpm: 100
    beats: 50
    duration_s: 30.8
    lead_time_s: 0.05
    accent_slug: null
    notes: "verse 2 — sustained reggae sway"
  - section: chorus
    slug: sway-side
    bpm: 100
    beats: 40
    duration_s: 24.8
    lead_time_s: 0.05
    accent_slug: bow
    notes: "Bella-Ciao refrain 2 — bow as a gestural acknowledgement of the partisan tradition (mid-song reverence)"
  - section: bridge
    slug: spin-look-around
    bpm: null
    beats: null
    duration_s: 9.0
    lead_time_s: 0.0
    accent_slug: null
    notes: "single show moment — slow, dignified pseudo-look-around (7s per spec) plus 2s recovery; reads as Reachy acknowledging the solidarity around it. MUST set automatic_body_yaw=False during this section, max_body_yaw stays ≤ ±150°"
  - section: verse
    slug: groove-bob
    bpm: 100
    beats: 32
    duration_s: 19.9
    lead_time_s: 0.05
    accent_slug: null
    notes: "verse 3 — energy lift via groove-bob (pitch-bob replaces the sway), still 100 BPM so no tempo break"
  - section: chorus
    slug: groove-bob
    bpm: 100
    beats: 48
    duration_s: 29.5
    lead_time_s: 0.05
    accent_slug: proud
    notes: "Bella-Ciao refrain 3 — peak section, proud accent at the start, the only section with the more energetic groove-bob carrying the hook"
  - section: outro
    slug: sway-side
    bpm: 100
    beats: 24
    duration_s: 15.2
    lead_time_s: 0.05
    accent_slug: bow
    notes: "fade-out back to dignified sway with a final bow as closing reverence — 12 cycles to neutral"
  - section: outro-idle
    slug: waiting-idle
    bpm: null
    beats: null
    duration_s: 6.0
    lead_time_s: 0.0
    accent_slug: null
    notes: "respectful hold after the song ends — set loop_count=None for unbounded loop until external stop signal"
warnings:
  - "Section duration sum 196.8s vs. estimated track length 210s = -6.3 % (within ±10 % tolerance, so green)"
  - "Track length 3:30 (210s) is an estimate — verify against the actual recording before finalizing the section beats; small per-section beat adjustments may be needed"
  - "BPM 100 is an estimate for Mal Élevé's reggae-resistance arrangement — verify against the actual recording, adjust per-section BPM if the track has tempo variations between verses and refrains"
  - "platform: any — BPM 100 is safely inside every block's hardware range; no platform-specific clamp needed for this choreography"
---

# Resistenza (Bella Ciao) — Reachy Mini choreography

## Context

Choreography for *Mal Élevé — Resistenza (Bella Ciao)* (album *Résistance Mondiale*, 2019): a politically-charged reggae adaptation of the Italian partisan anthem "Bella Ciao". The choreography stays dignified throughout — `sway-side` carries the verses and the first two refrains in classic reggae fashion (the spec calls out `sway-side` for "Reggae-/Slow-Genre-Bewegungen" explicitly), `groove-bob` lifts the energy only in the third verse and the final refrain so the song's resistance crescendo lands. One `spin-look-around` bridge gives Reachy a single, slow show moment. The accent slugs alternate `proud → bow → proud → bow` across the four refrain / outro sections: `proud` carries the inner standfastness across refrains 1 and 3 (peak), `bow` carries the gestural reverence at refrain 2 (mid-song acknowledgement of the partisan tradition) and at the outro (closing reverence). No `headbang-soft` is used — head-banging would read as the wrong genre and clash with the song's solemnity.

## Section table

| # | Section | Slug | BPM | Beats | Duration (s) | Lead time (s) | Accent | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | intro | `waiting-idle` | — | — | 6.0 | 0.00 | — | acoustic intro phase |
| 2 | verse | `sway-side` | 100 | 50 | 30.8 | 0.05 | — | verse 1, dignified sway |
| 3 | chorus | `sway-side` | 100 | 40 | 24.8 | 0.05 | `proud` | Bella-Ciao refrain 1 |
| 4 | verse | `sway-side` | 100 | 50 | 30.8 | 0.05 | — | verse 2 |
| 5 | chorus | `sway-side` | 100 | 40 | 24.8 | 0.05 | `bow` | Bella-Ciao refrain 2, mid-song reverence |
| 6 | bridge | `spin-look-around` | — | — | 9.0 | 0.00 | — | dignified show moment, `automatic_body_yaw=False` |
| 7 | verse | `groove-bob` | 100 | 32 | 19.9 | 0.05 | — | verse 3, energy lifts |
| 8 | chorus | `groove-bob` | 100 | 48 | 29.5 | 0.05 | `proud` | Bella-Ciao refrain 3, peak |
| 9 | outro | `sway-side` | 100 | 24 | 15.2 | 0.05 | `bow` | fade-out with final bow as closing reverence |
| 10 | outro-idle | `waiting-idle` | — | — | 6.0 | 0.00 | — | respectful hold, then `loop_count=None` |

Section duration sum: 196.8 s vs. estimated track length 210 s (−6.3 %, inside the ±10 % tolerance window). **Track length and BPM are estimates** — verify against the actual recording before finalizing.

Slug references (open these for pose tables, easing, and acceptance criteria during translation):

- [`spec/reachy-mini/motions/sway-side/de.md`](../spec/reachy-mini/motions/sway-side/de.md) — 50–140 BPM range, asymmetric antennas per sway direction, `automatic_body_yaw=True` recommended (the spec explicitly calls out this block for reggae-style movement)
- [`spec/reachy-mini/motions/groove-bob/de.md`](../spec/reachy-mini/motions/groove-bob/de.md) — 60–180 BPM range, pitch-only bob, antennas stationary at +15°
- [`spec/reachy-mini/motions/spin-look-around/de.md`](../spec/reachy-mini/motions/spin-look-around/de.md) — 7 s sequence, `automatic_body_yaw=False` MUST, body-yaw ≤ ±150°
- [`spec/reachy-mini/motions/waiting-idle/de.md`](../spec/reachy-mini/motions/waiting-idle/de.md) — idle / breathing default, loop-able
- [`spec/reachy-mini/motions/proud/de.md`](../spec/reachy-mini/motions/proud/de.md) — emotion accent only, never the rhythmic main channel
- [`spec/reachy-mini/motions/bow/de.md`](../spec/reachy-mini/motions/bow/de.md) — social accent (gesture), used at refrain 2 and the outro for dignified reverence

## Platform consequences

| Platform | Status | Notes |
|---|---|---|
| Reachy Mini (Wireless) | full | All sections playable; no `headbang-soft`, so IMU temperature polling is not strictly required; sustained `sway-side` at 100 BPM with antenna asymmetry is mild compared to brown-out scenarios in `control-surface` |
| Reachy Mini Lite | full | Same as Wireless minus IMU read; no `headbang-soft`, so no thermal-budget concern; external power supply means no brown-out risk |
| Simulation | partial | Pose / antenna sequences run; **no audio playback** (the song must be played from another source synced to the choreography), **no IMU telemetry** (`mini.imu` returns `None`), **no real servo heat** to verify; on-hardware validation is required for final sign-off via the `reachy-mini-on-device` agent |

The bridge section uses `spin-look-around` (7 s + 2 s recovery). Per its motion spec, `automatic_body_yaw=False` MUST be set for the duration of the section; the developer toggles it back to `True` for sections 7–9 so `groove-bob` and `sway-side` get the natural body-follow.

## Translation checklist for the developer

1. For each section slug, instantiate the matching `Move` subclass from `reachy_mini_show/behaviors/`:
   - sections 1, 10: `WaitingIdle(duration_s=6.0)` for section 1, `WaitingIdle(loop_count=None)` for section 10 (unbounded)
   - sections 2, 3, 4, 5, 9: `SwaySide(bpm=100, beats=<beats>, lead_time_s=0.05)` with `beats` as in the section table — `sway-side` requires `beats` to be even (every value in this choreography satisfies that)
   - sections 7, 8: `GrooveBob(bpm=100, beats=<beats>, lead_time_s=0.05)`
   - section 6: `SpinLookAround()` (the spec defines a fixed 7 s sequence; budget 2 s for transition recovery before section 7 starts)
2. Pass BPM, beats, and lead time as constructor parameters exactly as listed in the YAML frontmatter — do not reinterpret the lead time, it is the audio-pipeline-latency compensation per `groove-bob` / `sway-side` specs.
3. The four accent slugs (sections 3, 5, 8, 9) alternate between an **emotion overlay** (`proud` in sections 3 and 8) and a **social gesture** (`bow` in sections 5 and 9). Trigger the matching move once at the start of the section and let the dance block continue underneath; do not loop the accent. `proud` reads as inner standfastness and supports the `groove-bob` peak in section 8; `bow` reads as gestural reverence and lands the dignity of the partisan tradition at the mid-song refrain and at the closing fade.
4. Section 6 (`spin-look-around`) MUST set `mini.set_automatic_body_yaw(False)` before the move starts and `mini.set_automatic_body_yaw(True)` after section 6 finishes, before section 7 begins. Per the spin-look-around spec, treat the body-yaw values in the spec table as a draft until the IK math is verified against real hardware (the spec carries a `> ⚠ TBD` on the head-yaw / body-yaw geometry).
5. Audio sync: align the `play_sound(file=...)` call for *Resistenza (Bella Ciao)* with section 1's start, accounting for the ~50 ms GStreamer audio buffer (per `control-surface` spec). Beat detection is **not** part of this choreography — BPM is hard-coded to 100 (estimated). The planned `audio-beat-tracking` skill can replace the hard-coded BPM with a live beat estimate later; until then, manual sync is required and per-section beat counts may need adjustment if the actual track tempo deviates.
6. Test against `ReachyMini(use_sim=True)` first — verify no slug raises and the duration sum lands within ±2 s of 196.8 s. Then dispatch the `reachy-mini-on-device` agent for hardware validation of the dignified feel, the bridge spin, and the energy lift in sections 7–8.
7. Platform fallbacks for this choreography are minimal because `headbang-soft` is intentionally absent; no servo-heat fallback is needed. The only platform-conditional logic is whether to play audio at all (skip on simulation, where audio is unsupported).

## Open questions

- **Track length and BPM are estimates.** Confirmed song length and any per-section tempo variations should be measured against the actual recording before this choreography is finalized; small per-section beat adjustments may be needed to keep audio sync tight. The ±10 % duration tolerance is the formal gate, but for a politically-charged song mis-timing the final refrain reads worse than mis-timing a pop hook.
- **Accent alternation `proud → bow → proud → bow` is one composition choice among several.** Variants worth trying on hardware: (a) all four refrain accents on `bow` for a more unified gestural reading; (b) `agreeing-nod` instead of `proud` in section 3, signalling affirmation at the first refrain; (c) `recognition` in the bridge (section 6) instead of the `spin-look-around`, for a more contemplative-resistance reading. Decide on hardware which reading the audience expects.
- **Tempo lift via groove-bob in section 7 is a chosen contrast, not a tempo change.** BPM stays at 100 throughout — the lift comes purely from the change in dance pattern (sway → bob), not from playing a faster block. If the actual recording has a real tempo lift in the third verse, the choreography should reflect that with a per-section BPM increase (e.g. 100 → 105 in section 7, 110 in section 8) — verify against the recording.
- **Section 6's bridge uses `spin-look-around` once.** An alternative dignified bridge would be a short `thinking` insert (state block) plus an emotion accent like `proud` instead of the spin — that variant feels less "show-piece" and more "contemplative resistance". Decide on hardware which reading the audience expects.
- **The choreography lives at `choreographies/resistenza-bella-ciao.md` inside the plugin repo** as a demo / example. Per `spec/reachy-mini/app-architecture/de.md`, choreographies for production use belong inside the `reachy-mini-show` app repo (suggested home: `reachy_mini_show/choreographies/`). Move the file there before the developer integrates it into the slug registry.
