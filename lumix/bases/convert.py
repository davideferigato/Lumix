"""
Funzioni di conversione tra basi numeriche.
Supporta decimale, binario, esadecimale, ottale.
"""

def dec_to_bin(n: int) -> str:
    """Converte un intero decimale in binario (stringa senza prefisso)."""
    return bin(n)[2:]

def bin_to_dec(s: str) -> int:
    """Converte una stringa binaria in intero decimale."""
    return int(s, 2)

def dec_to_hex(n: int) -> str:
    """Converte un intero decimale in esadecimale (stringa minuscola senza prefisso)."""
    return hex(n)[2:]

def hex_to_dec(s: str) -> int:
    """Converte una stringa esadecimale in intero decimale."""
    return int(s, 16)

def dec_to_oct(n: int) -> str:
    """Converte un intero decimale in ottale (stringa senza prefisso)."""
    return oct(n)[2:]

def oct_to_dec(s: str) -> int:
    """Converte una stringa ottale in intero decimale."""
    return int(s, 8)

def convert(value: str, from_base: str, to_base: str) -> str:
    """
    Funzione generica di conversione tra basi.

    Args:
        value: valore come stringa (es. '255', 'ff', '1010', '377')
        from_base: base di partenza ('dec', 'bin', 'hex', 'oct')
        to_base: base di destinazione ('dec', 'bin', 'hex', 'oct')

    Returns:
        Valore convertito come stringa (per 'dec' restituisce intero in forma stringa)
    """
    # Mappa delle funzioni di conversione da base a decimale
    to_dec = {
        'dec': int,
        'bin': bin_to_dec,
        'hex': hex_to_dec,
        'oct': oct_to_dec,
    }
    # Mappa delle funzioni di conversione da decimale a base
    from_dec = {
        'dec': str,
        'bin': dec_to_bin,
        'hex': dec_to_hex,
        'oct': dec_to_oct,
    }

    if from_base not in to_dec or to_base not in from_dec:
        raise ValueError(f"Base non supportata: {from_base} -> {to_base}")

    # Converti in decimale
    if from_base == 'dec':
        dec_value = int(value)  # value è già un numero decimale
    else:
        dec_value = to_dec[from_base](value)

    # Converti da decimale a destinazione
    if to_base == 'dec':
        return str(dec_value)
    else:
        return from_dec[to_base](dec_value)
