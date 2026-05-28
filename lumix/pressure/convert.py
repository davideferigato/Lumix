"""
Funzioni di conversione per unità di pressione.
Tutte le conversioni sono basate su pascal (Pa) come unità base.
Fattori di conversione:
1 bar = 100000 Pa
1 atm = 101325 Pa
1 mmHg = 133.322 Pa (torr)
1 psi = 6894.76 Pa
"""

_TO_PASCAL = {
    "pa": 1.0,
    "bar": 100000.0,
    "atm": 101325.0,
    "mmhg": 133.322,
    "psi": 6894.76,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converte un valore da un'unità di pressione a un'altra.

    Args:
        value: Valore numerico da convertire.
        from_unit: Unità di partenza (es. 'bar', 'psi').
        to_unit: Unità di arrivo.

    Returns:
        float: Valore convertito.
    """
    from_norm = from_unit.lower()
    to_norm = to_unit.lower()

    if from_norm not in _TO_PASCAL or to_norm not in _TO_PASCAL:
        raise ValueError(f"Unità non supportata: {from_unit} o {to_unit}")

    value_in_pa = value * _TO_PASCAL[from_norm]
    result = value_in_pa / _TO_PASCAL[to_norm]
    return result
