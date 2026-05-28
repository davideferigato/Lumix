"""
Funzioni di conversione per unità di dati digitali.
Tutte le conversioni sono basate su byte come unità base.
Fattori: 1 KB = 1024 B, 1 MB = 1024 KB, 1 GB = 1024 MB, 1 TB = 1024 GB.
"""

_TO_BYTES = {
    "b": 1.0,
    "kb": 1024.0,
    "mb": 1024.0 * 1024.0,
    "gb": 1024.0 * 1024.0 * 1024.0,
    "tb": 1024.0 * 1024.0 * 1024.0 * 1024.0,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converte un valore da un'unità digitale a un'altra.
    """
    from_norm = from_unit.lower()
    to_norm = to_unit.lower()

    if from_norm not in _TO_BYTES or to_norm not in _TO_BYTES:
        raise ValueError(f"Unità non supportata: {from_unit} o {to_unit}")

    value_in_bytes = value * _TO_BYTES[from_norm]
    result = value_in_bytes / _TO_BYTES[to_norm]
    return result
