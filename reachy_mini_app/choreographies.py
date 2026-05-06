"""Choreographies derived 1:1 from spec/choreographies/.

Variante B (Lite/Playground) per plan.md: choreographies are sequential
section lists; each section dispatches a `blocks` function. Accent slugs
(`proud`, `bow`) play *before* the rhythmic block of their section, since
this app does not run a parallel-Move stack.
"""
from __future__ import annotations

import threading
from dataclasses import dataclass

from reachy_mini import ReachyMini

from . import blocks


@dataclass(frozen=True)
class Section:
    name: str
    slug: str
    bpm: float | None = None
    beats: int | None = None
    duration_s: float | None = None
    lead_time_s: float = 0.0
    accent_slug: str | None = None


# spec/choreographies/drop-it-like-its-hot.md
DROP_IT_LIKE_ITS_HOT: list[Section] = [
    Section("intro", "waiting-idle", duration_s=8.0),
    Section("verse", "sway-side", bpm=93, beats=50, lead_time_s=0.05),
    Section("pre-chorus", "groove-bob", bpm=93, beats=32, lead_time_s=0.05, accent_slug="proud"),
    Section("chorus", "groove-bob", bpm=93, beats=48, lead_time_s=0.05),
    Section("verse", "sway-side", bpm=93, beats=60, lead_time_s=0.05),
    Section("chorus", "groove-bob", bpm=93, beats=48, lead_time_s=0.05),
    Section("bridge", "spin-look-around"),
    Section("verse", "sway-side", bpm=93, beats=50, lead_time_s=0.05),
    Section("chorus", "groove-bob", bpm=93, beats=48, lead_time_s=0.05),
    Section("outro", "sway-side", bpm=93, beats=24, lead_time_s=0.05, accent_slug="proud"),
    Section("outro-idle", "waiting-idle", duration_s=8.0),
]

# spec/choreographies/resistenza-bella-ciao.md
RESISTENZA_BELLA_CIAO: list[Section] = [
    Section("intro", "waiting-idle", duration_s=6.0),
    Section("verse", "sway-side", bpm=100, beats=50, lead_time_s=0.05),
    Section("chorus", "sway-side", bpm=100, beats=40, lead_time_s=0.05, accent_slug="proud"),
    Section("verse", "sway-side", bpm=100, beats=50, lead_time_s=0.05),
    Section("chorus", "sway-side", bpm=100, beats=40, lead_time_s=0.05, accent_slug="bow"),
    Section("bridge", "spin-look-around"),
    Section("verse", "groove-bob", bpm=100, beats=32, lead_time_s=0.05),
    Section("chorus", "groove-bob", bpm=100, beats=48, lead_time_s=0.05, accent_slug="proud"),
    Section("outro", "sway-side", bpm=100, beats=24, lead_time_s=0.05, accent_slug="bow"),
    Section("outro-idle", "waiting-idle", duration_s=6.0),
]


_ACCENTS = {"proud": blocks.proud, "bow": blocks.bow}


def _play_section(
    reachy: ReachyMini, stop_event: threading.Event, section: Section
) -> None:
    if section.accent_slug is not None and not stop_event.is_set():
        accent = _ACCENTS.get(section.accent_slug)
        if accent is None:
            raise ValueError(f"unknown accent: {section.accent_slug}")
        accent(reachy, stop_event)

    if stop_event.is_set():
        return

    if section.slug == "sway-side":
        blocks.sway_side(
            reachy, stop_event,
            bpm=section.bpm, beats=section.beats,
            lead_time_s=section.lead_time_s,
        )
    elif section.slug == "groove-bob":
        blocks.groove_bob(
            reachy, stop_event,
            bpm=section.bpm, beats=section.beats,
            lead_time_s=section.lead_time_s,
        )
    elif section.slug == "spin-look-around":
        blocks.spin_look_around(reachy, stop_event)
    elif section.slug == "waiting-idle":
        blocks.waiting_idle(reachy, stop_event, duration_s=section.duration_s)
    else:
        raise ValueError(f"unknown slug: {section.slug}")


def play(
    reachy: ReachyMini,
    stop_event: threading.Event,
    sections: list[Section],
) -> None:
    for section in sections:
        if stop_event.is_set():
            break
        _play_section(reachy, stop_event, section)


def drop_it_like_its_hot(reachy: ReachyMini, stop_event: threading.Event) -> None:
    play(reachy, stop_event, DROP_IT_LIKE_ITS_HOT)


def resistenza_bella_ciao(reachy: ReachyMini, stop_event: threading.Event) -> None:
    play(reachy, stop_event, RESISTENZA_BELLA_CIAO)
