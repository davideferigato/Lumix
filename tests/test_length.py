from lumix.length.convert import convert


def test_convert():
    assert round(convert(1.80, "m", "ft"), 2) == 5.91  # 1.80 / 0.3048 ≈ 5.9055
    assert round(convert(5, "km", "mi"), 2) == 3.11

