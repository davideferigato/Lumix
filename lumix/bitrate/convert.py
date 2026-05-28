"""
Funzioni di conversione per bitrate.
Tutte le conversioni sono basate su bps (bit per secondo) come unità base.
Fattori: 1 Kbps = 1000 bps, 1 Mbps = 1000 Kbps, ecc. (base 10, non 1024).
"""

# Fattori di conversione verso bps
_TO_BPS = {
    "bps": 1.0,
    "kbps": 1000.0,
    "mbps": 1000.0 * 1000.0,
    "gbps": 1000.0 * 1000.0 * 1000.0,
    "tbps": 1000.0 * 1000.0 * 1000.0 * 1000.0,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converte un valore da un'unità di bitrate a un'altra.

    Args:
        value: Valore numerico da convertire.
        from_unit: Unità di partenza (es. 'mbps', 'kbps').
        to_unit: Unità di arrivo.

    Returns:
        float: Valore convertito.
    """
    from_norm = from_unit.lower()
    to_norm = to_unit.lower()

    if from_norm not in _TO_BPS or to_norm not in _TO_BPS:
        raise ValueError(f"Unità non supportata: {from_unit} o {to_unit}")

    # Converti in bps
    value_in_bps = value * _TO_BPS[from_norm]
    # Converti da bps a unità destinazione
    result = value_in_bps / _TO_BPS[to_norm]
    return result
