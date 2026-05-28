"""
Funzioni di conversione per unità di velocità.
Tutte le conversioni sono basate su m/s come unità base.
Fattori di conversione:
1 km/h = 0.2777777778 m/s
1 mph  = 0.44704 m/s
1 m/s  = 1.0
"""

_TO_MS = {
    "km/h": 0.2777777778,
    "kmh": 0.2777777778,
    "mph": 0.44704,
    "m/s": 1.0,
    "ms": 1.0,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converte un valore da un'unità di velocità a un'altra.

    Args:
        value: Valore numerico da convertire.
        from_unit: Unità di partenza (es. 'km/h', 'mph').
        to_unit: Unità di arrivo.

    Returns:
        float: Valore convertito.
    """
    # Normalizza le unità: sostituisci "/" e rimuovi spazi
    from_norm = from_unit.lower().replace("/", "").replace(" ", "")
    to_norm = to_unit.lower().replace("/", "").replace(" ", "")

    if from_norm not in _TO_MS or to_norm not in _TO_MS:
        raise ValueError(f"Unità non supportata: {from_unit} o {to_unit}")

    value_in_ms = value * _TO_MS[from_norm]
    result = value_in_ms / _TO_MS[to_norm]
    return result
