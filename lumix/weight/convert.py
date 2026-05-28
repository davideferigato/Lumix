"""
Funzioni di conversione per unità di peso.
Tutte le conversioni sono basate sul grammo (g) come unità base.
Fattori di conversione:
1 g = 1 g
1 kg = 1000 g
1 lb = 453.59237 g
1 oz = 28.349523125 g
1 mg = 0.001 g
1 st (stone) = 6350.29318 g
1 t (tonnellata metrica) = 1_000_000 g
"""

_TO_GRAM = {
    "g": 1.0,
    "gram": 1.0,
    "kg": 1000.0,
    "kilogram": 1000.0,
    "lb": 453.59237,
    "pound": 453.59237,
    "oz": 28.349523125,
    "ounce": 28.349523125,
    "mg": 0.001,
    "milligram": 0.001,
    "st": 6350.29318,
    "stone": 6350.29318,
    "t": 1_000_000.0,
    "tonne": 1_000_000.0,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converte un valore da un'unità di peso a un'altra.

    Args:
        value: Valore numerico da convertire.
        from_unit: Unità di partenza (es. 'kg', 'lb').
        to_unit: Unità di arrivo.

    Returns:
        float: Valore convertito.
    """
    from_norm = from_unit.lower().replace(" ", "")
    to_norm = to_unit.lower().replace(" ", "")

    unit_map = {
        "g": "g",
        "gram": "g",
        "kg": "kg",
        "kilogram": "kg",
        "lb": "lb",
        "pound": "lb",
        "oz": "oz",
        "ounce": "oz",
        "mg": "mg",
        "milligram": "mg",
        "st": "st",
        "stone": "st",
        "t": "t",
        "tonne": "t",
        "metricton": "t",
    }
    from_key = unit_map.get(from_norm, from_norm)
    to_key = unit_map.get(to_norm, to_norm)

    if from_key not in _TO_GRAM or to_key not in _TO_GRAM:
        raise ValueError(f"Unità non supportata: {from_unit} o {to_unit}")

    value_in_gram = value * _TO_GRAM[from_key]
    result = value_in_gram / _TO_GRAM[to_key]
    return result
