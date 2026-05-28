#!/usr/bin/env python3
"""
Parser per il modulo phonetic.
Sintassi: <lang> phonetic for <testo>
Esempio: en phonetic for CIAO
"""
import sys

from lumix.phonetic.convert import text_to_phonetic

LANG_CONFIG = {
    "en": {
        "cmd_for": "for",
        "errors": {
            "syntax": "❌ Syntax: {lang} phonetic for <text>",
        },
        "output": "{result}",
    },
    "it": {
        "cmd_for": "per",
        "errors": {
            "syntax": "❌ Sintassi: {lang} fonetico per <testo>",
        },
        "output": "{result}",
    },
    "fr": {
        "cmd_for": "pour",
        "errors": {
            "syntax": "❌ Syntaxe : {lang} phonétique pour <texte>",
        },
        "output": "{result}",
    },
    "es": {
        "cmd_for": "para",
        "errors": {
            "syntax": "❌ Sintaxis: {lang} fonético para <texto>",
        },
        "output": "{result}",
    },
    "jp": {
        "cmd_for": "に対して",
        "errors": {
            "syntax": "❌ 構文: {lang} 発音記号 に対して <テキスト>",
        },
        "output": "{result}",
    },
}


def parse(lang: str, params: str):
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    # Il testo può contenere spazi, quindi dividiamo solo il primo token
    parts = params.split(maxsplit=1)
    if len(parts) != 2 or parts[0] != cfg["cmd_for"]:
        print(cfg["errors"]["syntax"].format(lang=lang))
        sys.exit(1)

    text = parts[1].strip()
    # Rimuovi eventuali virgolette
    if (text.startswith('"') and text.endswith('"')) or (
        text.startswith("'") and text.endswith("'")
    ):
        text = text[1:-1]

    result = text_to_phonetic(text)
    print(cfg["output"].format(result=result))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: phonetic_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = " ".join(sys.argv[2:])
    parse(lang, params)
