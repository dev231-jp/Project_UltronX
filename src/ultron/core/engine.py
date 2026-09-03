"""Application lifecycle for ULTRON X."""

from dataclasses import dataclass


@dataclass
class EngineStatus:
    """Current state of the ULTRON engine."""

    name: str
    version: str
    running: bool


class UltronEngine:
    """Minimal lifecycle controller for the ULTRON platform.

    Detection, collection, and response modules will be attached to this
    engine in later phases. Keeping lifecycle management isolated makes the
    core easy to test and extend.
    """

    name = "ULTRON X"
    version = "2.0.0"

    def __init__(self) -> None:
        self._running = False

    @property
    def running(self) -> bool:
        return self._running

    def start(self) -> EngineStatus:
        """Start the engine and return its current status."""
        self._running = True
        return self.status()

    def stop(self) -> EngineStatus:
        """Stop the engine and return its current status."""
        self._running = False
        return self.status()

    def status(self) -> EngineStatus:
        """Return a snapshot of the engine state."""
        return EngineStatus(
            name=self.name,
            version=self.version,
            running=self._running,
        )
