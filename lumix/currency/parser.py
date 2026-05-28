#!/usr/bin/env python3
import sys

from lumix.currency.convert import convert_currency

VALID_CURRENCIES = ["EUR", "USD", "GBP", "JPY", "CHF", "CAD", "AUD", "CNY"]

LANG_CONFIG = {
    "en": {
        "from_kw": "from",
        "to_kw": "to",
        "value_pattern": r"^-?[0-9]+(\.[0-9]+)?$",
        "errors": {
            "syntax": "❌ Syntax: {lang} currency from <cur> to <cur> <amount>",
            "currency": "❌ Unsupported currency. Use: EUR, USD, GBP, ...",
            "value": "❌ Invalid amount. Use dot as decimal separator (e.g. 50.5)",
        },
        "output": "{amount} {src} → {result} {dst}",
    },
    "it": {
        "from_kw": "da",
        "to_kw": "a",
        "value_pattern": r"^-?[0-9]+(,[0-9]+)?$",
        "errors": {
            "syntax": "❌ Sintassi: {lang} valuta da <valuta> a <valuta> <importo>",
            "currency": "❌ Valuta non supportata. Usa: EUR, USD, GBP, ...",
            "value": "❌ Importo non valido. Usa la virgola come separatore decimale (es. 50,5)",
        },
        "output": "{importo} {src} → {risultato} {dst}",
    },
    # ... altre lingue ...
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

    from_kw, src_currency, to_kw, dst_currency, amount_str = parts

    if from_kw != cfg["from_kw"] or to_kw != cfg["to_kw"]:
        print(cfg["errors"]["syntax"].format(lang=lang))
        sys.exit(1)

    src_currency = src_currency.upper()
    dst_currency = dst_currency.upper()
    if src_currency not in VALID_CURRENCIES or dst_currency not in VALID_CURRENCIES:
        print(cfg["errors"]["currency"])
        sys.exit(1)

    # sostituisci virgola con punto
    amount_str = amount_str.replace(",", ".")
    try:
        amount = float(amount_str)
    except ValueError:
        print(cfg["errors"]["value"])
        sys.exit(1)

    try:
        result = convert_currency(amount, src_currency, dst_currency)
    except Exception as e:
        print(f"❌ Errore nella conversione: {e}")
        sys.exit(1)

    # output
    output = cfg["output"].format(
        amount=amount_str,
        src=src_currency,
        result=f"{result:.2f}",
        dst=dst_currency,
        importo=amount_str,
        risultato=f"{result:.2f}",
    )
    print(output)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: currency_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = " ".join(sys.argv[2:])
    parse(lang, params)
