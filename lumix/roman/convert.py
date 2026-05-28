"""
Funzioni di conversione tra numeri arabi (interi) e numeri romani.
Supporta numeri da 1 a 3999 (limite della notazione romana standard).
"""


def int_to_roman(num: int) -> str:
    """
    Converte un intero (1-3999) in numero romano.
    """
    if not (1 <= num <= 3999):
        raise ValueError("Numero fuori dall'intervallo supportato (1-3999)")

    val = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    result = []
    for v, s in val:
        while num >= v:
            result.append(s)
            num -= v
    return "".join(result)


def roman_to_int(roman: str) -> int:
    """
    Converte una stringa di numero romano in intero.
    """
    roman = roman.upper()
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for ch in reversed(roman):
        value = roman_map.get(ch)
        if value is None:
            raise ValueError(f"Carattere romano non valido: {ch}")
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return total
