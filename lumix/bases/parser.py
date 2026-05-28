#!/usr/bin/env python3
"""
Parser per il modulo base.
Sintassi: <lang> base <from_kw> <from_base> <to_kw> <to_base> <value>
"""
import sys

from .convert import convert

# Basi supportate
VALID_BASES = ['dec', 'bin', 'hex', 'oct']

# Configurazione per lingua
LANG_CONFIG = {
    'en': {
        'from_kw': 'from',
        'to_kw': 'to',
        'value_pattern': r'^[0-9A-Fa-f]+$',  # generico, poi validiamo in base al contesto
        'errors': {
            'syntax': "❌ Syntax: {lang} base from <base> to <base> <value>",
            'base': "❌ Invalid base. Use: dec, bin, hex, oct",
            'value': "❌ Invalid value for base {base}",
        },
        'output': "{value} ({from_base}) → {result} ({to_base})",
    },
    'it': {
        'from_kw': 'da',
        'to_kw': 'a',
        'value_pattern': r'^[0-9A-Fa-f]+$',
        'errors': {
            'syntax': "❌ Sintassi: {lang} base da <base> a <base> <valore>",
            'base': "❌ Base non valida. Usa: dec, bin, hex, oct",
            'value': "❌ Valore non valido per la base {base}",
        },
        'output': "{valore} ({from_base}) → {risultato} ({to_base})",
    },
    'fr': {
        'from_kw': 'de',
        'to_kw': 'à',
        'value_pattern': r'^[0-9A-Fa-f]+$',
        'errors': {
            'syntax': "❌ Syntaxe : {lang} base de <base> à <base> <valeur>",
            'base': "❌ Base non valide. Utilisez : dec, bin, hex, oct",
            'value': "❌ Valeur non valide pour la base {base}",
        },
        'output': "{valeur} ({from_base}) → {résultat} ({to_base})",
    },
    'es': {
        'from_kw': 'de',
        'to_kw': 'a',
        'value_pattern': r'^[0-9A-Fa-f]+$',
        'errors': {
            'syntax': "❌ Sintaxis: {lang} base de <base> a <base> <valor>",
            'base': "❌ Base no válida. Usa: dec, bin, hex, oct",
            'value': "❌ Valor no válido para la base {base}",
        },
        'output': "{valor} ({from_base}) → {resultado} ({to_base})",
    },
    'jp': {
        'from_kw': 'から',
        'to_kw': 'まで',
        'value_pattern': r'^[0-9A-Fa-f]+$',
        'errors': {
            'syntax': "❌ 構文: {lang} 基数 から <基数> まで <基数> <値>",
            'base': "❌ 無効な基数です。使用可能: dec, bin, hex, oct",
            'value': "❌ 基数 {base} に対して値が無効です",
        },
        'output': "{値} ({from_base}) → {結果} ({to_base})",
    },
}

def validate_value(value: str, base: str) -> bool:
    """Verifica che la stringa sia valida per la base specificata."""
    if base == 'dec':
        return value.isdigit()
    elif base == 'bin':
        return all(c in '01' for c in value)
    elif base == 'hex':
        return all(c in '0123456789ABCDEFabcdef' for c in value)
    elif base == 'oct':
        return all(c in '01234567' for c in value)
    return False

def parse(lang: str, params: str):
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    parts = params.split()
    if len(parts) != 5:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

    from_kw, from_base, to_kw, to_base, value_str = parts

    # Controllo sintassi keywords
    if from_kw != cfg['from_kw'] or to_kw != cfg['to_kw']:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

    # Validazione basi
    from_base = from_base.lower()
    to_base = to_base.lower()
    if from_base not in VALID_BASES or to_base not in VALID_BASES:
        print(cfg['errors']['base'])
        sys.exit(1)

    # Validazione formato valore in base alla base sorgente
    if not validate_value(value_str, from_base):
        print(cfg['errors']['value'].format(base=from_base))
        sys.exit(1)

    # Tentativo di conversione
    try:
        result = convert(value_str, from_base, to_base)
    except ValueError:
        print(cfg['errors']['value'].format(base=from_base))
        sys.exit(1)

    # Output formattato
    output = cfg['output'].format(
        value=value_str, from_base=from_base,
        risultato=result, resultado=result, résultat=result, 結果=result,
        to_base=to_base
    )
    print(output)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: base_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = sys.argv[2]
    parse(lang, params)
