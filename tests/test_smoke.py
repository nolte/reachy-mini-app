"""Smoke test — runs without hardware, against the reachy_mini simulation.

What this test verifies:
- The app's entrypoint module imports cleanly.
- A `ReachyMini` simulation instance can be spawned with a daemon.
- A single `set_target` tick is accepted by the sim.

What this test cannot verify (hardware-only — see the
`reachy-mini-on-device` agent):
- Audio playback through `mini.media`.
- IMU telemetry via `mini.imu`.
- LED synchronisation.
- True pose convergence on real motors.
"""

from __future__ import annotations

import importlib.util
import threading
import time

import numpy as np
import pytest

# Skip the entire module when GStreamer is missing — the reachy_mini
# simulation refuses to spawn without it.
gstreamer_missing = importlib.util.find_spec("gi") is None
pytestmark = pytest.mark.skipif(
    gstreamer_missing,
    reason="GStreamer (python3-gi) not installed; sim cannot start.",
)


def test_app_module_imports() -> None:
    """The scaffolded entry point must import without side effects."""
    from reachy_mini_app import main as app_main

    assert hasattr(app_main, "ReachyMiniApp")


def test_reachy_mini_sim_set_target_tick() -> None:
    """A single set_target tick on the simulation must succeed."""
    from reachy_mini import ReachyMini
    from reachy_mini.utils import create_head_pose

    mini = ReachyMini(spawn_daemon=True, use_sim=True)
    try:
        head_pose = create_head_pose(yaw=0.0, degrees=True)
        antennas_rad = np.deg2rad(np.array([0.0, 0.0]))
        mini.set_target(head=head_pose, antennas=antennas_rad)
        # let the daemon process at least one control cycle
        time.sleep(0.05)
    finally:
        # best-effort teardown — exact API depends on SDK version
        close = getattr(mini, "close", None) or getattr(mini, "stop", None)
        if callable(close):
            close()


def test_run_loop_respects_stop_event() -> None:
    """The Pollen lifecycle contract: run() exits when stop_event is set."""
    from reachy_mini import ReachyMini
    from reachy_mini_app.main import ReachyMiniApp

    app = ReachyMiniApp()
    mini = ReachyMini(spawn_daemon=True, use_sim=True)
    stop_event = threading.Event()

    thread = threading.Thread(target=app.run, args=(mini, stop_event), daemon=True)
    thread.start()
    time.sleep(0.2)  # let the loop iterate at least once
    stop_event.set()
    thread.join(timeout=2.0)

    assert not thread.is_alive(), "run() did not exit within 2s of stop_event"

    close = getattr(mini, "close", None) or getattr(mini, "stop", None)
    if callable(close):
        close()
