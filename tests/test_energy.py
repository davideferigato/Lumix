from lumix.energy.convert import convert


def test_convert():
    assert round(convert(500, "j", "kcal"), 6) == round(500 / 4184, 6)
    assert convert(1, "kwh", "j") == 3_600_000
