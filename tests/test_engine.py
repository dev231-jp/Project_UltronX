from ultron import UltronEngine


def test_engine_starts_and_stops() -> None:
    engine = UltronEngine()

    assert engine.running is False

    started = engine.start()
    assert started.name == "ULTRON X"
    assert started.version == "2.0.0"
    assert started.running is True

    stopped = engine.stop()
    assert stopped.running is False
