from lumix.unitsymbols.convert import get_info_by_name, get_info_by_symbol


def test_get_info_by_symbol():
    info = get_info_by_symbol("W")
    assert info["name"] == "watt"
    assert info["type"] == "power"


def test_get_info_by_name():
    info = get_info_by_name("kilogram")
    assert info["symbol"] == "kg"
    assert info["type"] == "mass"
