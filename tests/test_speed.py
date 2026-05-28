import pytest

from lumix.speed.convert import convert


def test_convert():
    assert round(convert(130, "km/h", "mph"), 2) == 80.78
    assert convert(10, "m/s", "km/h") == pytest.approx(36.0, rel=1e-9)
