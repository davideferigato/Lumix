from lumix.volume.convert import convert


def test_convert():
    assert round(convert(2, "l", "gal"), 4) == round(2 / 3.78541, 4)
    assert convert(1, "m3", "l") == 1000
