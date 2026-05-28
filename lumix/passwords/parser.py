#!/usr/bin/env python3
"""
Parser per il modulo passwords.
Sintassi: <lang> passwords generate length <N> [symbols <true|false>]
Esempio: en passwords generate length 16 symbols true
"""
import sys

from .generate import generate_password

LANG_CONFIG = {
    "en": {
        "cmd_generate": "generate",
        "kw_length": "length",
        "kw_symbols": "symbols",
        "errors": {
            "syntax": "❌ Syntax: {lang} passwords generate length <N> [symbols true|false]",
            "invalid_length": "❌ Length must be a positive integer",
            "invalid_bool": "❌ symbols must be 'true' or 'false'",
        },
        "output": "Generated password: {password}",
    },
    "it": {
        "cmd_generate": "genera",
        "kw_length": "lunghezza",
        "kw_symbols": "simboli",
        "errors": {
            "syntax": "❌ Sintassi: {lang} password genera lunghezza <N> [simboli true|false]",
            "invalid_length": "❌ La lunghezza deve essere un intero positivo",
            "invalid_bool": "❌ simboli deve essere 'true' o 'false'",
        },
        "output": "Password generata: {password}",
    },
    "fr": {
        "cmd_generate": "générer",
        "kw_length": "longueur",
        "kw_symbols": "symboles",
        "errors": {
            "syntax": "❌ Syntaxe : {lang} motsdepasse générer longueur <N> [symboles true|false]",
            "invalid_length": "❌ La longueur doit être un entier positif",
            "invalid_bool": "❌ symboles doit être 'true' ou 'false'",
        },
        "output": "Mot de passe généré : {password}",
    },
    "es": {
        "cmd_generate": "generar",
        "kw_length": "longitud",
        "kw_symbols": "símbolos",
        "errors": {
            "syntax": "❌ Sintaxis: {lang} contraseñas generar longitud <N> [símbolos true|false]",
            "invalid_length": "❌ La longitud debe ser un entero positivo",
            "invalid_bool": "❌ símbolos debe ser 'true' o 'false'",
        },
        "output": "Contraseña generada: {password}",
    },
    "jp": {
        "cmd_generate": "生成",
        "kw_length": "長さ",
        "kw_symbols": "記号",
        "errors": {
            "syntax": "❌ 構文: {lang} パスワード 生成 長さ <N> [記号 true|false]",
            "invalid_length": "❌ 長さは正の整数でなければなりません",
            "invalid_bool": "❌ 記号は 'true' または 'false' でなければなりません",
        },
        "output": "生成されたパスワード: {password}",
    },
}


def parse(lang: str, params: str):
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    tokens = params.split()
    if len(tokens) < 3 or tokens[0] != cfg["cmd_generate"]:
        print(cfg["errors"]["syntax"].format(lang=lang))
        sys.exit(1)

    if tokens[1] != cfg["kw_length"]:
        print(cfg["errors"]["syntax"].format(lang=lang))
        sys.exit(1)

    try:
        length = int(tokens[2])
        if length <= 0:
            raise ValueError
    except ValueError:
        print(cfg["errors"]["invalid_length"])
        sys.exit(1)

    use_symbols = False
    if len(tokens) >= 5 and tokens[3] == cfg["kw_symbols"]:
        sym_val = tokens[4].lower()
        if sym_val == "true":
            use_symbols = True
        elif sym_val == "false":
            use_symbols = False
        else:
            print(cfg["errors"]["invalid_bool"])
            sys.exit(1)

    password = generate_password(length, use_symbols)
    print(cfg["output"].format(password=password))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: passwords_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = " ".join(sys.argv[2:])
    parse(lang, params)
