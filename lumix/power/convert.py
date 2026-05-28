"""
Funzioni di conversione per unità di potenza.
Tutte le conversioni sono basate sul watt (W) come unità base.
Fattori di conversione:
1 W = 1 W
1 kW = 1000 W
1 hp (meccanico) = 745.699872 W
1 CV (cavallo metrico) = 735.49875 W (opzionale, non incluso di default)
"""

_TO_WATT = {
    "w": 1.0,
    "kw": 1000.0,
    "hp": 745.699872,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converte un valore da un'unità di potenza a un'altra.

    Args:
        value: Valore numerico da convertire.
        from_unit: Unità di partenza (es. 'w', 'kw', 'hp').
        to_unit: Unità di arrivo.

    Returns:
        float: Valore convertito.
    """
    from_norm = from_unit.lower()
    to_norm = to_unit.lower()

    if from_norm not in _TO_WATT or to_norm not in _TO_WATT:
        raise ValueError(f"Unità non supportata: {from_unit} o {to_unit}")

    value_in_watt = value * _TO_WATT[from_norm]
    result = value_in_watt / _TO_WATT[to_norm]
    return result
