#!/usr/bin/env python3
"""
Parser per il modulo timezones.
Sintassi: <lang> timezones <from_kw> <from_tz> <to_kw> <to_tz> <datetime>
Esempio: en timezones from Europe/Rome to Asia/Tokyo "2025-08-02 14:00"
"""
import re
import sys

from lumix.timezones.convert import convert_timezone

# Mappa dei formati di data/ora per lingua
LANG_CONFIG = {
    "en": {
        "from_kw": "from",
        "to_kw": "to",
        "date_format": "%Y-%m-%d %H:%M",
        "date_pattern": r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$",
        "errors": {
            "syntax": "❌ Syntax: {lang} timezones from <timezone> to <timezone> 'YYYY-MM-DD HH:MM'",
            "invalid_date": "❌ Invalid date format. Use YYYY-MM-DD HH:MM",
            "invalid_tz": "❌ Invalid timezone",
        },
    },
    "it": {
        "from_kw": "da",
        "to_kw": "a",
        "date_format": "%d/%m/%Y %H:%M",
        "date_pattern": r"^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$",
        "errors": {
            "syntax": "❌ Sintassi: {lang} fusi da <fuso> a <fuso> 'GG/MM/AAAA HH:MM'",
            "invalid_date": "❌ Formato data non valido. Usa GG/MM/AAAA HH:MM",
            "invalid_tz": "❌ Fuso orario non valido",
        },
    },
    "fr": {
        "from_kw": "de",
        "to_kw": "à",
        "date_format": "%d/%m/%Y %H:%M",
        "date_pattern": r"^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$",
        "errors": {
            "syntax": "❌ Syntaxe : {lang} fuseaux de <fuseau> à <fuseau> 'JJ/MM/AAAA HH:MM'",
            "invalid_date": "❌ Format de date invalide. Utilisez JJ/MM/AAAA HH:MM",
            "invalid_tz": "❌ Fuseau horaire invalide",
        },
    },
    "es": {
        "from_kw": "de",
        "to_kw": "a",
        "date_format": "%d/%m/%Y %H:%M",
        "date_pattern": r"^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$",
        "errors": {
            "syntax": "❌ Sintaxis: {lang} husos de <huso> a <huso> 'DD/MM/AAAA HH:MM'",
            "invalid_date": "❌ Formato de fecha no válido. Use DD/MM/AAAA HH:MM",
            "invalid_tz": "❌ Huso horario no válido",
        },
    },
    "jp": {
        "from_kw": "から",
        "to_kw": "まで",
        "date_format": "%Y年%m月%d日 %H:%M",
        "date_pattern": r"^\d{4}年\d{2}月\d{2}日 \d{2}:\d{2}$",
        "errors": {
            "syntax": "❌ 構文: {lang} タイムゾーン から <タイムゾーン> まで <タイムゾーン> 'YYYY年MM月DD日 HH:MM'",
            "invalid_date": "❌ 日付形式が無効です。YYYY年MM月DD日 HH:MM を使用してください",
            "invalid_tz": "❌ 無効なタイムゾーン",
        },
    },
}


def parse(lang: str, params: str):
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    parts = params.split(maxsplit=4)
    if len(parts) != 5:
        print(cfg["errors"]["syntax"].format(lang=lang))
        sys.exit(1)

    from_kw, from_tz, to_kw, to_tz, dt_str = parts

    if from_kw != cfg["from_kw"] or to_kw != cfg["to_kw"]:
        print(cfg["errors"]["syntax"].format(lang=lang))
        sys.exit(1)

    # Rimuovi eventuali virgolette intorno a dt_str
    if (dt_str.startswith('"') and dt_str.endswith('"')) or (
        dt_str.startswith("'") and dt_str.endswith("'")
    ):
        dt_str = dt_str[1:-1]

    if not re.match(cfg["date_pattern"], dt_str):
        print(cfg["errors"]["invalid_date"])
        sys.exit(1)

    try:
        result = convert_timezone(dt_str, from_tz, to_tz, cfg["date_format"])
    except ValueError as e:
        if "Fuso orario non valido" in str(e) or "Invalid timezone" in str(e):
            print(cfg["errors"]["invalid_tz"])
        else:
            print(f"❌ {e}")
        sys.exit(1)

    print(f"{dt_str} {from_tz} → {result} {to_tz}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: timezones_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = " ".join(sys.argv[2:])
    parse(lang, params)
