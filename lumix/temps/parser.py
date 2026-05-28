#!/usr/bin/env python3
"""
Module parser per conversione temperature.
Definisce una funzione parse(lang, params) che valida i parametri localizzati
e invoca temps.convert(src_unit, dst_unit, value) passando sempre il valore con il punto come separatore decimale.
"""

import re
import sys

try:
    from lumix.temps.convert import convert
except ImportError:
    from convert import convert

# Codici ANSI per colorazione
_GREEN = "\033[32m"
_RESET = "\033[0m"

# Unità ammesse
VALID_UNITS = {"C", "F", "K"}

# Configurazione per keyword e regex decimal separator per lingua
LANG_CONFIG = {
    "it": {
        "from_kw": "da",
        "to_kw": "a",
        "value_pattern": r"^-?[0-9]+(,[0-9]+)?$",
        "errors": {
            "syntax": "❌ Sintassi errata per lingua 'it': usa 'da' e 'a'",
            "unit": "❌ Unità non valida. Usa solo C, F, K",
            "value": "❌ Valore non valido: in italiano si usa la virgola (es: 36,5)",
        },
    },
    "fr": {
        "from_kw": "de",
        "to_kw": "à",
        "value_pattern": r"^-?[0-9]+(,[0-9]+)?$",
        "errors": {
            "syntax": "❌ Syntaxe invalide pour 'fr' : utilisez 'de' et 'à'",
            "unit": "❌ Unités invalides. Utilisez C, F, K",
            "value": "❌ Valeur invalide : utilisez la virgule (ex: 36,5)",
        },
    },
    "es": {
        "from_kw": "de",
        "to_kw": "a",
        "value_pattern": r"^-?[0-9]+(,[0-9]+)?$",
        "errors": {
            "syntax": "❌ Sintaxis incorrecta para 'es': usa 'de' y 'a'",
            "unit": "❌ Unidad no válida. Usa C, F, K",
            "value": "❌ Valor no válido: usa coma decimal (ej: 36,5)",
        },
    },
    "en": {
        "from_kw": "from",
        "to_kw": "to",
        "value_pattern": r"^-?[0-9]+(\.[0-9]+)?$",
        "errors": {
            "syntax": "❌ Invalid syntax for 'en': use 'from' and 'to'",
            "unit": "❌ Invalid units. Use C, F, K",
            "value": "❌ Invalid value: use dot as decimal separator (e.g. 36.5)",
        },
    },
    "jp": {
        "from_kw": "から",
        "to_kw": "まで",
        "value_pattern": r"^-?[0-9]+(\.[0-9]+)?$",
        "errors": {
            "syntax": "❌ 無効な構文：'から' と 'まで' を使ってください",
            "unit": "❌ 単位が無効です。C, F, K を使用してください",
            "value": "❌ 値が無効です。小数点にはピリオドを使ってください（例: 36.5）",
        },
    },
}


def parse(lang, params):
    """
    Valida params e invoca temps.convert(src_unit, dst_unit, value_dot).
    """
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    parts = params.split()
    if len(parts) != 5:
        print(
            f"❌ Uso: <lingua> {cfg['from_kw']} <unità_orig> {cfg['to_kw']} <unità_dest> <valore>"
        )
        sys.exit(1)

    from_kw, src_unit, to_kw, dst_unit, value_str = parts

    # Controllo sintassi keywords
    if from_kw != cfg["from_kw"] or to_kw != cfg["to_kw"]:
        print(cfg["errors"]["syntax"])
        sys.exit(1)

    # Controllo unità
    if src_unit not in VALID_UNITS or dst_unit not in VALID_UNITS:
        print(cfg["errors"]["unit"])
        sys.exit(1)

    # Controllo formato valore
    if not re.match(cfg["value_pattern"], value_str):
        print(cfg["errors"]["value"])
        sys.exit(1)

    # Correggiamo il separatore decimale in punto
    value_dot = value_str.replace(",", ".")

    # Invocazione della funzione convert con unità e valore con punto
    result = convert(src_unit, dst_unit, value_dot)
    # Stampa risultato con colore verde
    print(f"{value_str} {src_unit} --> {_GREEN}{result}{_RESET} {dst_unit}")


# Supporto per esecuzione diretta
if __name__ == "__main__":
    if len(sys.argv) != 7:
        print(
            "❌ Uso: ./temps.parser.py <lingua> <from_kw> <unità_orig> <to_kw> <unità_dest> <valore>"
        )
        sys.exit(1)
    lang = sys.argv[1]
    params = " ".join(sys.argv[2:])
    parse(lang, params)
