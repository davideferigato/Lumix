"""
Funzioni di conversione per unità di energia.
Tutte le conversioni sono basate su joule (J) come unità base.
Fattori di conversione (approssimati):
1 cal = 4.184 J
1 kcal = 4184 J
1 Wh = 3600 J
1 kWh = 3.6e6 J
1 eV = 1.602176634e-19 J
"""

_TO_JOULES = {
    "j": 1.0,
    "kj": 1000.0,
    "cal": 4.184,
    "kcal": 4184.0,
    "wh": 3600.0,
    "kwh": 3.6e6,
    "ev": 1.602176634e-19,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converte un valore da un'unità di energia a un'altra.

    Args:
        value: Valore numerico da convertire.
        from_unit: Unità di partenza (es. 'j', 'kcal').
        to_unit: Unità di arrivo.

    Returns:
        float: Valore convertito.
    """
    from_norm = from_unit.lower()
    to_norm = to_unit.lower()

    if from_norm not in _TO_JOULES or to_norm not in _TO_JOULES:
        raise ValueError(f"Unità non supportata: {from_unit} o {to_unit}")

    value_in_joules = value * _TO_JOULES[from_norm]
    result = value_in_joules / _TO_JOULES[to_norm]
    return result
