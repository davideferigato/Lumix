from lumix.pressure.convert import convert


def test_convert():
    assert round(convert(2, "bar", "psi"), 2) == 29.01  # 2 / 0.0689476 ≈ 29.0075
    assert convert(1, "atm", "pa") == 101325

