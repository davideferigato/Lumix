from lumix.roman.convert import int_to_roman, roman_to_int


def test_int_to_roman():
    assert int_to_roman(2025) == "MMXXV"
    assert int_to_roman(3999) == "MMMCMXCIX"


def test_roman_to_int():
    assert roman_to_int("MMXXV") == 2025
    assert roman_to_int("MMMCMXCIX") == 3999
