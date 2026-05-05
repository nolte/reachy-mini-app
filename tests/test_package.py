"""Smoke tests for the reachy_mini_app package."""

import reachy_mini_app


def test_package_importable() -> None:
    assert reachy_mini_app.__version__ == "0.0.1"
