from lumix.data.convert import convert


def test_convert():
    assert round(convert(1500, "mb", "gb"), 4) == round(1500 / 1024, 4)
    assert convert(1, "tb", "gb") == 1024
