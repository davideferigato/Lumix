#!/usr/bin/env python3
"""
Parser per il modulo area.
Sintassi: <lang> area <from_kw> <from_unit> <to_kw> <to_unit> <value>
"""
import re
import sys

from .convert import convert

# Configurazione per lingua
LANG_CONFIG = {
    'en': {
        'from_kw': 'from',
        'to_kw': 'to',
        'value_pattern': r'^-?[0-9]+(\.[0-9]+)?$',
        'errors': {
            'syntax': "❌ Syntax: {lang} area from <unit> to <unit> <value>",
            'unit': "❌ Unsupported unit. Try: m2, ft2, km2, mi2, ha, acre, cm2, mm2, yd2, in2",
            'value': "❌ Invalid value. Use dot as decimal separator (e.g. 50.5)",
        },
        'output': "{value} {from_unit} → {result} {to_unit}",
    },
    'it': {
        'from_kw': 'da',
        'to_kw': 'a',
        'value_pattern': r'^-?[0-9]+(,[0-9]+)?$',
        'errors': {
            'syntax': "❌ Sintassi: {lang} area da <unità> a <unità> <valore>",
            'unit': "❌ Unità non supportata. Prova: m2, ft2, km2, mi2, ha, acre, cm2, mm2, yd2, in2",
            'value': "❌ Valore non valido. Usa la virgola come separatore decimale (es. 50,5)",
        },
        'output': "{valore} {from_unit} → {risultato} {to_unit}",
    },
    'fr': {
        'from_kw': 'de',
        'to_kw': 'à',
        'value_pattern': r'^-?[0-9]+(,[0-9]+)?$',
        'errors': {
            'syntax': "❌ Syntaxe : {lang} aire de <unité> à <unité> <valeur>",
            'unit': "❌ Unité non prise en charge. Essayez : m2, ft2, km2, mi2, ha, acre, cm2, mm2, yd2, in2",
            'value': "❌ Valeur non valide. Utilisez la virgule comme séparateur décimal (ex. 50,5)",
        },
        'output': "{valeur} {from_unit} → {résultat} {to_unit}",
    },
    'es': {
        'from_kw': 'de',
        'to_kw': 'a',
        'value_pattern': r'^-?[0-9]+(,[0-9]+)?$',
        'errors': {
            'syntax': "❌ Sintaxis: {lang} área de <unidad> a <unidad> <valor>",
            'unit': "❌ Unidad no soportada. Prueba: m2, ft2, km2, mi2, ha, acre, cm2, mm2, yd2, in2",
            'value': "❌ Valor no válido. Usa la coma como separador decimal (ej. 50,5)",
        },
        'output': "{valor} {from_unit} → {resultado} {to_unit}",
    },
    'jp': {
        'from_kw': 'から',
        'to_kw': 'まで',
        'value_pattern': r'^-?[0-9]+(\.[0-9]+)?$',
        'errors': {
            'syntax': "❌ 構文: {lang} 面積 から <単位> まで <単位> <値>",
            'unit': "❌ サポートされていない単位です。試してください: m2, ft2, km2, mi2, ha, acre, cm2, mm2, yd2, in2",
            'value': "❌ 値が無効です。小数点にはピリオドを使ってください (例: 50.5)",
        },
        'output': "{値} {from_unit} → {結果} {to_unit}",
    },
}

def parse(lang: str, params: str):
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    parts = params.split()
    if len(parts) != 5:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

    from_kw, from_unit, to_kw, to_unit, value_str = parts

    # Controllo sintassi keywords
    if from_kw != cfg['from_kw'] or to_kw != cfg['to_kw']:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

    # Validazione formato valore
    if not re.match(cfg['value_pattern'], value_str):
        print(cfg['errors']['value'])
        sys.exit(1)

    # Normalizza separatore decimale a punto
    if ',' in value_str:
        value_str = value_str.replace(',', '.')

    try:
        value = float(value_str)
    except ValueError:
        print(cfg['errors']['value'])
        sys.exit(1)

    # Tentativo di conversione
    try:
        result = convert(value, from_unit, to_unit)
    except ValueError:
        print(cfg['errors']['unit'])
        sys.exit(1)

    # Formatta output con due decimali
    output = cfg['output'].format(
        value=value_str, from_unit=from_unit,
        risultato=f"{result:.2f}", resultado=f"{result:.2f}",
        résultat=f"{result:.2f}", 結果=f"{result:.2f}",
        to_unit=to_unit
    )
    print(output)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: area_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = sys.argv[2]
    parse(lang, params)
