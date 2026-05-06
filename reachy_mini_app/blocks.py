"""Motion blocks derived 1:1 from the claude-reachy-mini motion specs.

Each block is a synchronous function that drives the robot via `set_target()`
in a tight loop until either its declared duration elapses or `stop_event`
is set. Pose deltas are taken verbatim from the spec tables under
spec/reachy-mini/motions/ in the plugin repo.

Conventions:
- Translation in mm, angles in degrees — both are converted to SDK units
  (m, rad) inside `apply()`.
- Antennas: spec lists `(l, r)`; the SDK takes `[right, left]` in radians.
  The `Pose` dataclass keeps `(left, right)`; `apply()` swaps the order.
- 50 Hz control loop (20 ms tick) — same cadence as the scaffold demo body.
"""
from __future__ import annotations

import threading
import time
from dataclasses import dataclass
from typing import Sequence

import numpy as np
from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose
from reachy_mini.utils.interpolation import InterpolationTechnique, time_trajectory

TICK_S = 0.02


@dataclass(frozen=True)
class Pose:
    """Head pose delta + antennas + body-yaw, in spec units (mm, deg)."""

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    roll: float = 0.0
    pitch: float = 0.0
    yaw: float = 0.0
    antenna_left: float = 0.0
    antenna_right: float = 0.0
    body_yaw: float = 0.0


NEUTRAL = Pose()


@dataclass(frozen=True)
class Phase:
    end: Pose
    duration: float
    easing: InterpolationTechnique = InterpolationTechnique.MIN_JERK


def apply(reachy: ReachyMini, pose: Pose) -> None:
    head = create_head_pose(
        x=pose.x,
        y=pose.y,
        z=pose.z,
        roll=pose.roll,
        pitch=pose.pitch,
        yaw=pose.yaw,
        mm=True,
        degrees=True,
    )
    antennas_rad = np.deg2rad([pose.antenna_right, pose.antenna_left])
    reachy.set_target(
        head=head,
        antennas=antennas_rad,
        body_yaw=float(np.deg2rad(pose.body_yaw)),
    )


def _lerp(a: float, b: float, s: float) -> float:
    return a + (b - a) * s


def _lerp_pose(p0: Pose, p1: Pose, s: float) -> Pose:
    return Pose(
        x=_lerp(p0.x, p1.x, s),
        y=_lerp(p0.y, p1.y, s),
        z=_lerp(p0.z, p1.z, s),
        roll=_lerp(p0.roll, p1.roll, s),
        pitch=_lerp(p0.pitch, p1.pitch, s),
        yaw=_lerp(p0.yaw, p1.yaw, s),
        antenna_left=_lerp(p0.antenna_left, p1.antenna_left, s),
        antenna_right=_lerp(p0.antenna_right, p1.antenna_right, s),
        body_yaw=_lerp(p0.body_yaw, p1.body_yaw, s),
    )


def _run_phase(
    reachy: ReachyMini,
    stop_event: threading.Event,
    start: Pose,
    phase: Phase,
) -> Pose:
    if phase.duration <= 0:
        apply(reachy, phase.end)
        return phase.end
    t0 = time.time()
    while not stop_event.is_set():
        elapsed = time.time() - t0
        if elapsed >= phase.duration:
            break
        s = time_trajectory(min(1.0, elapsed / phase.duration), phase.easing)
        apply(reachy, _lerp_pose(start, phase.end, s))
        time.sleep(TICK_S)
    apply(reachy, phase.end)
    return phase.end


def _run_phases(
    reachy: ReachyMini,
    stop_event: threading.Event,
    start: Pose,
    phases: Sequence[Phase],
) -> Pose:
    cur = start
    for phase in phases:
        if stop_event.is_set():
            return cur
        cur = _run_phase(reachy, stop_event, cur, phase)
    return cur


# -----------------------------------------------------------------------------
# Block: groove-bob
# Spec: spec/reachy-mini/motions/groove-bob/
# -----------------------------------------------------------------------------


def groove_bob(
    reachy: ReachyMini,
    stop_event: threading.Event,
    bpm: float,
    beats: int,
    lead_time_s: float = 0.0,
) -> None:
    if not 60 <= bpm <= 180:
        raise ValueError(f"groove-bob bpm out of range [60, 180]: {bpm}")
    T = 60.0 / bpm

    DOWN = Pose(z=-3.0, pitch=-8.0, antenna_left=15.0, antenna_right=15.0)
    UP = Pose(z=+2.0, pitch=+5.0, antenna_left=15.0, antenna_right=15.0)

    if lead_time_s > 0:
        time.sleep(min(lead_time_s, 1.0))

    cur = _run_phase(reachy, stop_event, NEUTRAL, Phase(end=UP, duration=0.30))
    for _ in range(beats):
        if stop_event.is_set():
            break
        cur = _run_phase(reachy, stop_event, cur, Phase(end=DOWN, duration=0.4 * T))
        if stop_event.is_set():
            break
        cur = _run_phase(reachy, stop_event, cur, Phase(end=UP, duration=0.6 * T))
    _run_phase(reachy, stop_event, cur, Phase(end=NEUTRAL, duration=0.40))


# -----------------------------------------------------------------------------
# Block: sway-side
# Spec: spec/reachy-mini/motions/sway-side/
# -----------------------------------------------------------------------------


def sway_side(
    reachy: ReachyMini,
    stop_event: threading.Event,
    bpm: float,
    beats: int,
    lead_time_s: float = 0.0,
) -> None:
    if not 50 <= bpm <= 140:
        raise ValueError(f"sway-side bpm out of range [50, 140]: {bpm}")
    if beats % 2 != 0:
        raise ValueError(f"sway-side beats must be even, got {beats}")

    half = 60.0 / bpm  # half a sway cycle == one beat
    LEFT = Pose(
        z=+2.0, roll=+15.0, pitch=+3.0, yaw=-3.0,
        antenna_left=-10.0, antenna_right=+15.0, body_yaw=-3.0,
    )
    RIGHT = Pose(
        z=+2.0, roll=-15.0, pitch=+3.0, yaw=+3.0,
        antenna_left=+15.0, antenna_right=-10.0, body_yaw=+3.0,
    )

    if lead_time_s > 0:
        time.sleep(min(lead_time_s, 1.0))

    cur = _run_phase(reachy, stop_event, NEUTRAL, Phase(end=LEFT, duration=0.40))
    for i in range(beats // 2):
        if stop_event.is_set():
            break
        cur = _run_phase(reachy, stop_event, cur, Phase(end=RIGHT, duration=half))
        if stop_event.is_set():
            break
        if i == beats // 2 - 1:
            break
        cur = _run_phase(reachy, stop_event, cur, Phase(end=LEFT, duration=half))
    _run_phase(reachy, stop_event, cur, Phase(end=NEUTRAL, duration=0.40))


# -----------------------------------------------------------------------------
# Block: spin-look-around (no-tracking variant — head yaw stays at 0°)
# Spec: spec/reachy-mini/motions/spin-look-around/
# -----------------------------------------------------------------------------


def spin_look_around(
    reachy: ReachyMini,
    stop_event: threading.Event,
) -> None:
    ANT = (25.0, 25.0)
    LIFT = Pose(z=+3.0, pitch=+5.0, antenna_left=ANT[0], antenna_right=ANT[1])
    LEFT = Pose(z=+3.0, pitch=+5.0, body_yaw=-150.0,
                antenna_left=ANT[0], antenna_right=ANT[1])
    RIGHT = Pose(z=+3.0, pitch=+5.0, body_yaw=+150.0,
                 antenna_left=ANT[0], antenna_right=ANT[1])
    CENTER = Pose(z=+3.0, pitch=+5.0,
                  antenna_left=ANT[0], antenna_right=ANT[1])

    reachy.set_automatic_body_yaw(False)
    try:
        _run_phases(
            reachy, stop_event, NEUTRAL,
            [
                Phase(end=LIFT, duration=0.20),
                Phase(end=LEFT, duration=1.80, easing=InterpolationTechnique.EASE_IN_OUT),
                Phase(end=LEFT, duration=0.30),
                Phase(end=RIGHT, duration=2.50, easing=InterpolationTechnique.EASE_IN_OUT),
                Phase(end=RIGHT, duration=0.30),
                Phase(end=CENTER, duration=1.50, easing=InterpolationTechnique.EASE_IN_OUT),
                Phase(end=NEUTRAL, duration=0.40),
            ],
        )
    finally:
        reachy.set_automatic_body_yaw(True)


# -----------------------------------------------------------------------------
# Block: waiting-idle
# Spec: spec/reachy-mini/motions/waiting-idle/
# -----------------------------------------------------------------------------


def waiting_idle(
    reachy: ReachyMini,
    stop_event: threading.Event,
    duration_s: float | None = None,
) -> None:
    BREATH_FREQ = 0.25  # Hz → 4.0 s per breath cycle
    apply(reachy, NEUTRAL)
    t0 = time.time()
    while not stop_event.is_set():
        t = time.time() - t0
        if duration_s is not None and t >= duration_s:
            break
        s = float(np.sin(2.0 * np.pi * BREATH_FREQ * t))
        apply(
            reachy,
            Pose(
                z=2.0 * s,
                pitch=1.0 * s,
                antenna_left=2.0 * s,
                antenna_right=2.0 * s,
            ),
        )
        time.sleep(TICK_S)
    apply(reachy, NEUTRAL)


# -----------------------------------------------------------------------------
# Accent: proud
# Spec: spec/reachy-mini/motions/proud/
# -----------------------------------------------------------------------------


def proud(reachy: ReachyMini, stop_event: threading.Event) -> None:
    P_FLINCH = Pose(x=+2.0, z=-2.0, pitch=-5.0, antenna_left=5.0, antenna_right=5.0)
    P_LIFT = Pose(x=-3.0, z=+12.0, pitch=+20.0, antenna_left=40.0, antenna_right=40.0)
    P_SETTLE = Pose(x=-3.0, z=+10.0, pitch=+18.0, antenna_left=38.0, antenna_right=38.0)
    P_HOLD = Pose(x=-3.0, z=+12.0, pitch=+20.0, antenna_left=40.0, antenna_right=40.0)
    P_YAW_R = Pose(x=-3.0, z=+12.0, pitch=+20.0, yaw=+12.0,
                   antenna_left=40.0, antenna_right=40.0, body_yaw=+5.0)
    P_CENTER = Pose(x=-3.0, z=+12.0, pitch=+20.0,
                    antenna_left=40.0, antenna_right=40.0)

    _run_phases(
        reachy, stop_event, NEUTRAL,
        [
            Phase(end=P_FLINCH, duration=0.15),
            Phase(end=P_LIFT, duration=0.40, easing=InterpolationTechnique.CARTOON),
            Phase(end=P_SETTLE, duration=0.20, easing=InterpolationTechnique.CARTOON),
            Phase(end=P_HOLD, duration=0.80),
            Phase(end=P_YAW_R, duration=0.30, easing=InterpolationTechnique.EASE_IN_OUT),
            Phase(end=P_CENTER, duration=0.20),
            Phase(end=NEUTRAL, duration=0.50),
        ],
    )


# -----------------------------------------------------------------------------
# Accent: bow
# Spec: spec/reachy-mini/motions/bow/
# -----------------------------------------------------------------------------


def bow(reachy: ReachyMini, stop_event: threading.Event) -> None:
    B_LIFT = Pose(z=+3.0, pitch=+5.0, antenna_left=-5.0, antenna_right=-5.0)
    B_DEEP = Pose(z=-5.0, pitch=-25.0, antenna_left=-10.0, antenna_right=-10.0)

    _run_phases(
        reachy, stop_event, NEUTRAL,
        [
            Phase(end=B_LIFT, duration=0.20),
            Phase(end=B_DEEP, duration=0.80),
            Phase(end=B_DEEP, duration=0.40),
            Phase(end=NEUTRAL, duration=0.60),
            Phase(end=NEUTRAL, duration=0.40),
        ],
    )
