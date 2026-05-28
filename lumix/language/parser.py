#!/usr/bin/env python3
"""
Parser per il modulo language.
Sintassi: <lang> language <from_kw> <source> <to_kw> <target> <value>
Esempio: en language from name to code "Italian"
         it language da nome a codice "Italiano"
"""
import sys

from lumix.language.convert import code_to_name, name_to_code

LANG_CONFIG = {
    "en": {
        "from_kw": "from",
        "to_kw": "to",
        "source_options": ["name", "code"],
        "target_options": ["name", "code"],
        "errors": {
            "syntax": "❌ Syntax: {lang} language from <name|code> to <name|code> <value>",
        },
    },
    "it": {
        "from_kw": "da",
        "to_kw": "a",
        "source_options": ["nome", "codice"],
        "target_options": ["nome", "codice"],
        "errors": {
            "syntax": "❌ Sintassi: {lang} lingua da <nome|codice> a <nome|codice> <valore>",
        },
    },
    "fr": {
        "from_kw": "de",
        "to_kw": "à",
        "source_options": ["nom", "code"],
        "target_options": ["nom", "code"],
        "errors": {
            "syntax": "❌ Syntaxe : {lang} langue de <nom|code> à <nom|code> <valeur>",
        },
    },
    "es": {
        "from_kw": "de",
        "to_kw": "a",
        "source_options": ["nombre", "código"],
        "target_options": ["nombre", "código"],
        "errors": {
            "syntax": "❌ Sintaxis: {lang} idioma de <nombre|código> a <nombre|código> <valor>",
        },
    },
    "jp": {
        "from_kw": "から",
        "to_kw": "まで",
        "source_options": ["名前", "コード"],
        "target_options": ["名前", "コード"],
        "errors": {
            "syntax": "❌ 構文: {lang} 言語 から <名前|コード> まで <名前|コード> <値>",
        },
    },
}


def parse(lang: str, params: str):
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    # Il valore può contenere spazi (es. "United Kingdom"), quindi usiamo maxsplit
    tokens = params.split(maxsplit=4)
    if len(tokens) != 5:
        print(cfg["errors"]["syntax"].format(lang=lang))
        sys.exit(1)

    from_kw, source_type, to_kw, target_type, value = tokens

    if from_kw != cfg["from_kw"] or to_kw != cfg["to_kw"]:
        print(cfg["errors"]["syntax"].format(lang=lang))
        sys.exit(1)

    if (
        source_type not in cfg["source_options"]
        or target_type not in cfg["target_options"]
    ):
        print(cfg["errors"]["syntax"].format(lang=lang))
        sys.exit(1)

    source_map = dict(zip(cfg["source_options"], ["name", "code"]))
    target_map = dict(zip(cfg["target_options"], ["name", "code"]))
    src = source_map[source_type]
    tgt = target_map[target_type]

    if src == "code" and tgt == "name":
        result = code_to_name(value, lang)
        print(result)
    elif src == "name" and tgt == "code":
        result = name_to_code(value, lang)
        print(result)
    else:
        print(cfg["errors"]["syntax"].format(lang=lang))
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: language_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = " ".join(sys.argv[2:])
    parse(lang, params)
