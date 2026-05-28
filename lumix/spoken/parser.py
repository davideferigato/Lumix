#!/usr/bin/env python3
"""
Parser per il modulo spoken.
Sintassi: <lang> spoken from <numero>
Esempio: en spoken from 123456
         it parlato da 123456
"""
import sys

from lumix.spoken.convert import number_to_words

LANG_CONFIG = {
    "en": {
        "cmd_from": "from",
        "errors": {
            "syntax": "❌ Syntax: {lang} spoken from <number>",
            "invalid_number": "❌ Invalid number",
        },
        "output": "{result}",
    },
    "it": {
        "cmd_from": "da",
        "errors": {
            "syntax": "❌ Sintassi: {lang} parlato da <numero>",
            "invalid_number": "❌ Numero non valido",
        },
        "output": "{result}",
    },
    "fr": {
        "cmd_from": "de",
        "errors": {
            "syntax": "❌ Syntaxe : {lang} parlé de <nombre>",
            "invalid_number": "❌ Nombre invalide",
        },
        "output": "{result}",
    },
    "es": {
        "cmd_from": "de",
        "errors": {
            "syntax": "❌ Sintaxis: {lang} hablado de <número>",
            "invalid_number": "❌ Número no válido",
        },
        "output": "{result}",
    },
    "jp": {
        "cmd_from": "から",
        "errors": {
            "syntax": "❌ 構文: {lang} 話し言葉 から <数字>",
            "invalid_number": "❌ 無効な数字",
        },
        "output": "{result}",
    },
}


def parse(lang: str, params: str):
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    parts = params.split(maxsplit=1)
    if len(parts) != 2 or parts[0] != cfg["cmd_from"]:
        print(cfg["errors"]["syntax"].format(lang=lang))
        sys.exit(1)

    num_str = parts[1].strip()
    # Rimuovi eventuali virgolette
    if (num_str.startswith('"') and num_str.endswith('"')) or (
        num_str.startswith("'") and num_str.endswith("'")
    ):
        num_str = num_str[1:-1]

    try:
        num = int(num_str)
    except ValueError:
        print(cfg["errors"]["invalid_number"])
        sys.exit(1)

    try:
        result = number_to_words(num, lang)
    except ValueError as e:
        print(f"❌ {e}")
        sys.exit(1)

    print(cfg["output"].format(result=result))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: spoken_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = " ".join(sys.argv[2:])
    parse(lang, params)
