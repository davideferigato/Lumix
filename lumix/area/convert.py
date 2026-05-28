"""
Funzioni di conversione per unità di superficie.
Tutte le conversioni sono basate sul metro quadro (m²) come unità base.
"""

# Fattori di conversione verso m²
_TO_SQM = {
    "m2": 1.0,
    "m²": 1.0,
    "km2": 1_000_000.0,
    "km²": 1_000_000.0,
    "ft2": 0.092903,
    "ft²": 0.092903,
    "mi2": 2_589_988.0,
    "mi²": 2_589_988.0,
    "ha": 10_000.0,
    "acre": 4046.86,
    "ac": 4046.86,
    "cm2": 0.0001,
    "cm²": 0.0001,
    "mm2": 0.000001,
    "mm²": 0.000001,
    "yd2": 0.836127,
    "yd²": 0.836127,
    "in2": 0.00064516,
    "in²": 0.00064516,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converte un valore da un'unità di superficie a un'altra.

    Args:
        value: Valore numerico da convertire.
        from_unit: Unità di partenza (es. 'm2', 'ft2', 'km2').
        to_unit: Unità di arrivo.

    Returns:
        float: Valore convertito.
    """
    # Normalizza le unità (ignora il simbolo '²' se presente)
    from_norm = from_unit.lower().replace("²", "2")
    to_norm = to_unit.lower().replace("²", "2")

    if from_norm not in _TO_SQM or to_norm not in _TO_SQM:
        raise ValueError(f"Unità non supportata: {from_unit} o {to_unit}")

    # Converti da unità sorgente a m²
    value_in_sqm = value * _TO_SQM[from_norm]
    # Converti da m² a unità destinazione
    result = value_in_sqm / _TO_SQM[to_norm]
    return result
