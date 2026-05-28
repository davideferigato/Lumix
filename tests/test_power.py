from lumix.power.convert import convert


def test_convert():
    assert round(convert(1000, "w", "hp"), 4) == round(1000 / 745.699872, 4)
    assert convert(2, "kw", "w") == 2000
