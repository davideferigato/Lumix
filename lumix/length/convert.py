"""
Funzioni di conversione per unità di lunghezza.
Tutte le conversioni sono basate sul metro (m) come unità base.
Fattori di conversione:
1 m = 1 m
1 km = 1000 m
1 cm = 0.01 m
1 mm = 0.001 m
1 mi = 1609.344 m
1 yd = 0.9144 m
1 ft = 0.3048 m
1 in = 0.0254 m
1 nmi = 1852 m (miglio nautico)
"""

_TO_METER = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mm": 0.001,
    "mi": 1609.344,
    "yd": 0.9144,
    "ft": 0.3048,
    "in": 0.0254,
    "nmi": 1852.0,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converte un valore da un'unità di lunghezza a un'altra.

    Args:
        value: Valore numerico da convertire.
        from_unit: Unità di partenza (es. 'm', 'ft', 'km').
        to_unit: Unità di arrivo.

    Returns:
        float: Valore convertito.
    """
    from_norm = from_unit.lower()
    to_norm = to_unit.lower()

    if from_norm not in _TO_METER or to_norm not in _TO_METER:
        raise ValueError(f"Unità non supportata: {from_unit} o {to_unit}")

    value_in_meters = value * _TO_METER[from_norm]
    result = value_in_meters / _TO_METER[to_norm]
    return result
