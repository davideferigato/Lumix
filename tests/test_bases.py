from lumix.bases.convert import (
    bin_to_dec,
    dec_to_bin,
    dec_to_hex,
    dec_to_oct,
    hex_to_dec,
    oct_to_dec,
)


def test_dec_to_bin():
    assert dec_to_bin(42) == "101010"
    assert dec_to_bin(0) == "0"


def test_bin_to_dec():
    assert bin_to_dec("101010") == 42
    assert bin_to_dec("0") == 0


def test_dec_to_hex():
    assert dec_to_hex(255) == "ff"
    assert dec_to_hex(0) == "0"


def test_hex_to_dec():
    assert hex_to_dec("ff") == 255
    assert hex_to_dec("0") == 0


def test_dec_to_oct():
    assert dec_to_oct(64) == "100"
    assert dec_to_oct(0) == "0"


def test_oct_to_dec():
    assert oct_to_dec("100") == 64
    assert oct_to_dec("0") == 0
