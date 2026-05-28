from lumix.time.convert import convert


def test_convert():
    assert convert(3, "d", "h") == 72
    assert convert(2, "h", "min") == 120

