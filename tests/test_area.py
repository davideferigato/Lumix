from lumix.area.convert import convert


def test_convert():
    assert round(convert(50, "m2", "ft2"), 2) == 538.20  # 50 * 10.7639 ≈ 538.20
    assert convert(1, "km2", "m2") == 1_000_000
