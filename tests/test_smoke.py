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

# Skip the entire module when the GStreamer surface required by the
# reachy_mini simulation is not fully installed. `gi` alone is not enough —
# the sim also pulls in GstApp at spawn time, which depends on system
# packages like gir1.2-gst-plugins-base-1.0.
def _gstreamer_sim_ready() -> bool:
    if importlib.util.find_spec("gi") is None:
        return False
    try:
        import gi  # noqa: F401

        gi.require_version("GstApp", "1.0")
    except (ValueError, ImportError):
        return False
    return True


requires_sim = pytest.mark.skipif(
    not _gstreamer_sim_ready(),
    reason="GStreamer simulation surface missing (need GstApp 1.0).",
)


def test_app_module_imports() -> None:
    """The scaffolded entry point must import without side effects."""
    from reachy_mini_app import main as app_main

    assert hasattr(app_main, "ReachyMiniApp")


@requires_sim
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


@requires_sim
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
