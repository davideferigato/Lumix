"""
Funzioni di conversione per unità di volume.
Tutte le conversioni sono basate sul litro (L) come unità base.
Fattori di conversione:
1 L = 1 L
1 mL = 0.001 L
1 m3 = 1000 L
1 gal (US) = 3.78541 L
1 qt (US) = 0.946353 L
1 pt (US) = 0.473176 L
1 cup (US) = 0.236588 L
1 fl oz (US) = 0.0295735 L
1 gal (UK) = 4.54609 L
"""

_TO_LITER = {
    "l": 1.0,
    "litre": 1.0,
    "liter": 1.0,
    "ml": 0.001,
    "milliliter": 0.001,
    "millilitre": 0.001,
    "m3": 1000.0,
    "cubic meter": 1000.0,
    "gal": 3.78541,
    "gallon": 3.78541,
    "qt": 0.946353,
    "quart": 0.946353,
    "pt": 0.473176,
    "pint": 0.473176,
    "cup": 0.236588,
    "fl oz": 0.0295735,
    "fluid ounce": 0.0295735,
    "uk gal": 4.54609,
    "imperial gallon": 4.54609,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converte un valore da un'unità di volume a un'altra.

    Args:
        value: Valore numerico da convertire.
        from_unit: Unità di partenza (es. 'l', 'gal').
        to_unit: Unità di arrivo.

    Returns:
        float: Valore convertito.
    """
    from_norm = from_unit.lower().replace(" ", "")
    to_norm = to_unit.lower().replace(" ", "")

    unit_map = {
        "l": "l",
        "liter": "l",
        "litre": "l",
        "ml": "ml",
        "milliliter": "ml",
        "millilitre": "ml",
        "m3": "m3",
        "cubicmeter": "m3",
        "gal": "gal",
        "gallon": "gal",
        "qt": "qt",
        "quart": "qt",
        "pt": "pt",
        "pint": "pt",
        "cup": "cup",
        "floz": "fl oz",
        "fluidounce": "fl oz",
        "ukgal": "uk gal",
        "imperialgallon": "uk gal",
    }
    from_unit_key = unit_map.get(from_norm, from_norm)
    to_unit_key = unit_map.get(to_norm, to_norm)

    if from_unit_key not in _TO_LITER or to_unit_key not in _TO_LITER:
        raise ValueError(f"Unità non supportata: {from_unit} o {to_unit}")

    value_in_liters = value * _TO_LITER[from_unit_key]
    result = value_in_liters / _TO_LITER[to_unit_key]
    return result
