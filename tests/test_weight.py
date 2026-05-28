from lumix.weight.convert import convert


def test_convert():
    assert round(convert(75, "kg", "lb"), 2) == 165.35
    assert round(convert(10, "lb", "kg"), 2) == 4.54

