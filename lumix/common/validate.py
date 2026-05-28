def validate_number(value: str) -> float:
    """
    Converte una stringa in numero float, sollevando errore se non valido.
    """
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Invalid value: {value}")


def validate_temp(unit: str) -> str:
    """
    Verifica che l'unità di temperatura sia una tra C, F o K.
    """
    unit = unit.upper()
    if unit not in ("C", "F", "K"):
        raise ValueError(f"Unsupported temperature unit: {unit}")
    return unit


def validate_currency_code(code: str) -> str:
    """
    Verifica che il codice valuta sia alfabetico a 3 lettere.
    """
    if not code.isalpha() or len(code) != 3:
        raise ValueError(f"Invalid currency code: {code}")
    return code.upper()
