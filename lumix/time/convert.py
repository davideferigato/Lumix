"""
Funzioni di conversione per unità di tempo.
Tutte le conversioni sono basate sui secondi come unità base.
Fattori:
1 minuto = 60 secondi
1 ora = 3600 secondi
1 giorno = 86400 secondi
1 settimana = 604800 secondi
"""

_TO_SECONDS = {
    "s": 1.0,
    "sec": 1.0,
    "secondi": 1.0,
    "m": 60.0,
    "min": 60.0,
    "minuti": 60.0,
    "h": 3600.0,
    "hr": 3600.0,
    "ore": 3600.0,
    "d": 86400.0,
    "day": 86400.0,
    "giorni": 86400.0,
    "w": 604800.0,
    "week": 604800.0,
    "settimane": 604800.0,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converte un valore da un'unità di tempo a un'altra.

    Args:
        value: Valore numerico da convertire.
        from_unit: Unità di partenza (es. 's', 'min', 'h', 'd', 'w').
        to_unit: Unità di arrivo.

    Returns:
        float: Valore convertito.
    """
    from_norm = from_unit.lower()
    to_norm = to_unit.lower()

    if from_norm not in _TO_SECONDS or to_norm not in _TO_SECONDS:
        raise ValueError(f"Unità non supportata: {from_unit} o {to_unit}")

    value_in_seconds = value * _TO_SECONDS[from_norm]
    result = value_in_seconds / _TO_SECONDS[to_norm]
    return result
