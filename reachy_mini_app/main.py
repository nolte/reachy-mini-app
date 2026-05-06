import threading

from reachy_mini import ReachyMini, ReachyMiniApp

from . import blocks, choreographies


class _AnyEvent:
    """Compose two threading.Events; is_set() is the OR of both."""

    def __init__(self, *events: threading.Event) -> None:
        self._events = events

    def is_set(self) -> bool:
        return any(e.is_set() for e in self._events)


class ReachyMiniApp(ReachyMiniApp):
    custom_app_url: str | None = "http://0.0.0.0:8042"
    request_media_backend: str | None = None

    def run(self, reachy_mini: ReachyMini, stop_event: threading.Event) -> None:
        state: dict[str, str | None] = {"queued": None, "running": None}
        cancel = threading.Event()
        lock = threading.Lock()

        def _request(name: str | None) -> None:
            with lock:
                state["queued"] = name
                cancel.set()

        @self.settings_app.post("/play/drop-it-like-its-hot")
        def play_drop():
            _request("drop-it-like-its-hot")
            return {"queued": "drop-it-like-its-hot"}

        @self.settings_app.post("/play/resistenza-bella-ciao")
        def play_resistenza():
            _request("resistenza-bella-ciao")
            return {"queued": "resistenza-bella-ciao"}

        @self.settings_app.post("/stop")
        def stop_choreography():
            _request(None)
            return {"stopped": True}

        @self.settings_app.get("/status")
        def status():
            with lock:
                return {"running": state["running"], "queued": state["queued"]}

        while not stop_event.is_set():
            with lock:
                req = state["queued"]
                state["queued"] = None
                state["running"] = req if req is not None else "waiting-idle"
                cancel.clear()

            local_stop = _AnyEvent(stop_event, cancel)

            try:
                if req == "drop-it-like-its-hot":
                    choreographies.drop_it_like_its_hot(reachy_mini, local_stop)
                elif req == "resistenza-bella-ciao":
                    choreographies.resistenza_bella_ciao(reachy_mini, local_stop)
                else:
                    blocks.waiting_idle(reachy_mini, local_stop, duration_s=None)
            finally:
                with lock:
                    state["running"] = None


if __name__ == "__main__":
    app = ReachyMiniApp()
    try:
        app.wrapped_run()
    except KeyboardInterrupt:
        app.stop()
