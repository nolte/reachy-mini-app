"""Smoke tests for the two choreographies — structural + cancel-respect.

These tests do not run a full choreography end-to-end (~200–270 s wall
clock); that is hardware validation territory and belongs to the
`reachy-mini-on-device` agent. What we verify here:

- Section lists parse and only reference known slugs / accents
- Per-slug parameter constraints from the motion specs hold
- A choreography started in a thread exits within a small budget after
  stop_event is set — i.e. the blocks honour cancellation
"""
from __future__ import annotations

import importlib.util
import threading
import time

import pytest

from reachy_mini_app import blocks, choreographies

def _gstreamer_sim_ready() -> bool:
    if importlib.util.find_spec("gi") is None:
        return False
    try:
        import gi  # noqa: F401

        gi.require_version("GstApp", "1.0")
    except (ValueError, ImportError):
        return False
    return True


sim_unavailable = not _gstreamer_sim_ready()


_KNOWN_SLUGS = {"sway-side", "groove-bob", "spin-look-around", "waiting-idle"}
_KNOWN_ACCENTS = {"proud", "bow", None}


@pytest.mark.parametrize(
    "name,sections",
    [
        ("drop-it-like-its-hot", choreographies.DROP_IT_LIKE_ITS_HOT),
        ("resistenza-bella-ciao", choreographies.RESISTENZA_BELLA_CIAO),
    ],
)
def test_choreography_structure(name: str, sections: list[choreographies.Section]) -> None:
    assert sections, f"{name} has no sections"
    for sec in sections:
        assert sec.slug in _KNOWN_SLUGS, f"unknown slug in {name}: {sec.slug}"
        assert sec.accent_slug in _KNOWN_ACCENTS, (
            f"unknown accent in {name}: {sec.accent_slug}"
        )
        if sec.slug == "sway-side":
            assert sec.bpm is not None and 50 <= sec.bpm <= 140
            assert sec.beats is not None and sec.beats > 0 and sec.beats % 2 == 0
        elif sec.slug == "groove-bob":
            assert sec.bpm is not None and 60 <= sec.bpm <= 180
            assert sec.beats is not None and sec.beats > 0
        elif sec.slug == "waiting-idle":
            assert sec.duration_s is not None and sec.duration_s > 0


@pytest.mark.parametrize(
    "fn",
    [choreographies.drop_it_like_its_hot, choreographies.resistenza_bella_ciao],
    ids=["drop-it", "bella-ciao"],
)
@pytest.mark.skipif(sim_unavailable, reason="GStreamer simulation surface missing (need GstApp 1.0).")
def test_choreography_respects_stop_event(fn) -> None:
    from reachy_mini import ReachyMini

    mini = ReachyMini(spawn_daemon=True, use_sim=True)
    stop_event = threading.Event()
    try:
        t = threading.Thread(target=fn, args=(mini, stop_event), daemon=True)
        t.start()
        time.sleep(0.5)
        stop_event.set()
        t.join(timeout=3.0)
        assert not t.is_alive(), "choreography did not honour stop_event within 3s"
    finally:
        close = getattr(mini, "close", None) or getattr(mini, "stop", None)
        if callable(close):
            close()


def test_blocks_validate_parameters() -> None:
    """Constructor-time validation should reject out-of-range bpm / odd beats."""
    stop_event = threading.Event()
    stop_event.set()  # so the function would exit immediately if it got past validation

    class _NoopMini:
        def set_target(self, *args, **kwargs):
            pass

        def set_automatic_body_yaw(self, enabled):
            pass

    with pytest.raises(ValueError):
        blocks.groove_bob(_NoopMini(), stop_event, bpm=200, beats=8)
    with pytest.raises(ValueError):
        blocks.sway_side(_NoopMini(), stop_event, bpm=100, beats=7)
    with pytest.raises(ValueError):
        blocks.sway_side(_NoopMini(), stop_event, bpm=200, beats=8)
