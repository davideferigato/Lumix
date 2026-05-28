#!/usr/bin/env python3
"""
Modulo per conversione temperature.
Definisce la funzione convert(src_unit, dst_unit, val) che:
  - Riceve src_unit e dst_unit ('C', 'F', 'K'), e val come stringa (con punto come separatore).
  - Converte val in float, esegue la conversione appropriata.
  - Restituisce il risultato formattato a 2 decimali.
"""

_VALID_UNITS = {'C', 'F', 'K'}

def convert(src, dst, val):
    """
    Converte la temperatura da src a dst.

    Args:
        src (str): unità sorgente ('C', 'F', 'K').
        dst (str): unità destinazione ('C', 'F', 'K').
        val (str or float): valore numerico (se stringa, deve usare il punto come separatore).

    Returns:
        str: valore convertito formattato a due decimali,
             oppure None se input non valido o combinazione non supportata.
    """
    # Validazione unità
    if src not in _VALID_UNITS or dst not in _VALID_UNITS:
        return None

    # Conversione valore in float
    try:
        num = float(val)
    except (ValueError, TypeError):
        return None

    # Esegui conversione
    if src == dst:
        result = num
    elif src == 'C' and dst == 'F':
        result = (num * 9/5) + 32
    elif src == 'C' and dst == 'K':
        result = num + 273.15
    elif src == 'F' and dst == 'C':
        result = (num - 32) * 5/9
    elif src == 'F' and dst == 'K':
        result = ((num - 32) * 5/9) + 273.15
    elif src == 'K' and dst == 'C':
        result = num - 273.15
    elif src == 'K' and dst == 'F':
        result = ((num - 273.15) * 9/5) + 32
    else:
        # Combinazione non supportata
        return None

    # Formatta con due decimali
    return f"{result:.2f}"
