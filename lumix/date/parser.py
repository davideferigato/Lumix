#!/usr/bin/env python3
"""
Parser per il modulo date.
Sintassi: <lang> date <from_kw> <from_format> <to_kw> <to_format> <date_string>
"""
import re
import sys

from lumix.date.convert import FORMAT_MAP, convert_date

# Mappa dei formati per le regex di validazione
FORMAT_REGEX = {
    "us": r"^\d{2}/\d{2}/\d{4}$",  # MM/DD/YYYY
    "iso": r"^\d{4}-\d{2}-\d{2}$",  # YYYY-MM-DD
    "eu": r"^\d{2}/\d{2}/\d{4}$",  # DD/MM/YYYY
    "jp": r"^\d{4}年\d{2}月\d{2}日$",  # YYYY年MM月DD日
}

LANG_CONFIG = {
    "en": {
        "from_kw": "from",
        "to_kw": "to",
        "errors": {
            "syntax": "❌ Syntax: {lang} date from <format> to <format> <date>",
            "format": "❌ Invalid format. Use: us, iso, eu, jp",
            "date": "❌ Invalid date for the given source format",
        },
        "output": "{date_str} ({from_format}) → {result} ({to_format})",
    },
    "it": {
        "from_kw": "da",
        "to_kw": "a",
        "errors": {
            "syntax": "❌ Sintassi: {lang} data da <formato> a <formato> <data>",
            "format": "❌ Formato non valido. Usa: us, iso, eu, jp",
            "date": "❌ Data non valida per il formato sorgente specificato",
        },
        "output": "{data_str} ({from_format}) → {risultato} ({to_format})",
    },
    "fr": {
        "from_kw": "de",
        "to_kw": "à",
        "errors": {
            "syntax": "❌ Syntaxe : {lang} date de <format> à <format> <date>",
            "format": "❌ Format invalide. Utilisez : us, iso, eu, jp",
            "date": "❌ Date invalide pour le format source",
        },
        "output": "{date_str} ({from_format}) → {résultat} ({to_format})",
    },
    "es": {
        "from_kw": "de",
        "to_kw": "a",
        "errors": {
            "syntax": "❌ Sintaxis: {lang} fecha de <formato> a <formato> <fecha>",
            "format": "❌ Formato no válido. Usa: us, iso, eu, jp",
            "date": "❌ Fecha no válida para el formato origen",
        },
        "output": "{fecha_str} ({from_format}) → {resultado} ({to_format})",
    },
    "jp": {
        "from_kw": "から",
        "to_kw": "まで",
        "errors": {
            "syntax": "❌ 構文: {lang} 日付 から <形式> まで <形式> <日付>",
            "format": "❌ 無効な形式です。使用可能: us, iso, eu, jp",
            "date": "❌ 指定されたソース形式に対して日付が無効です",
        },
        "output": "{日付} ({from_format}) → {結果} ({to_format})",
    },
}


def parse(lang: str, params: str):
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    parts = params.split()
    if len(parts) != 5:
        print(cfg["errors"]["syntax"].format(lang=lang))
        sys.exit(1)

    from_kw, from_fmt, to_kw, to_fmt, date_str = parts

    if from_kw != cfg["from_kw"] or to_kw != cfg["to_kw"]:
        print(cfg["errors"]["syntax"].format(lang=lang))
        sys.exit(1)

    if from_fmt not in FORMAT_MAP or to_fmt not in FORMAT_MAP:
        print(cfg["errors"]["format"])
        sys.exit(1)

    # Validazione con regex del formato sorgente
    regex = FORMAT_REGEX.get(from_fmt)
    if regex and not re.match(regex, date_str):
        print(cfg["errors"]["date"])
        sys.exit(1)

    try:
        result = convert_date(date_str, from_fmt, to_fmt)
    except ValueError:
        print(cfg["errors"]["date"])
        sys.exit(1)

    output = cfg["output"].format(
        date_str=date_str,
        from_format=from_fmt,
        risultato=result,
        resultado=result,
        résultat=result,
        結果=result,
        to_format=to_fmt,
        data_str=date_str,
        fecha_str=date_str,
        日付=date_str,
    )
    print(output)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: date_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = " ".join(sys.argv[2:])
    parse(lang, params)
