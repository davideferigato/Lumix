#!/usr/bin/env python3
"""
Parser per il modulo country.
Sintassi: <lang> country from <source> to <target> <value>
Esempio: en country from code to name IT
         it country da codice a nome IT
"""
import sys

from .convert import code_to_name, name_to_code

# Configurazione per lingua
LANG_CONFIG = {
    'en': {
        'from_kw': 'from',
        'to_kw': 'to',
        'source_options': ['code', 'name'],
        'target_options': ['code', 'name'],
        'errors': {
            'syntax': "❌ Syntax: {lang} country from <code|name> to <code|name> <value>",
            'source': "❌ Source must be 'code' or 'name'",
            'target': "❌ Target must be 'code' or 'name'",
        },
    },
    'it': {
        'from_kw': 'da',
        'to_kw': 'a',
        'source_options': ['codice', 'nome'],
        'target_options': ['codice', 'nome'],
        'errors': {
            'syntax': "❌ Sintassi: {lang} paese da <codice|nome> a <codice|nome> <valore>",
            'source': "❌ La sorgente deve essere 'codice' o 'nome'",
            'target': "❌ La destinazione deve essere 'codice' o 'nome'",
        },
    },
    'fr': {
        'from_kw': 'de',
        'to_kw': 'à',
        'source_options': ['code', 'nom'],
        'target_options': ['code', 'nom'],
        'errors': {
            'syntax': "❌ Syntaxe : {lang} pays de <code|nom> à <code|nom> <valeur>",
            'source': "❌ La source doit être 'code' ou 'nom'",
            'target': "❌ La cible doit être 'code' ou 'nom'",
        },
    },
    'es': {
        'from_kw': 'de',
        'to_kw': 'a',
        'source_options': ['código', 'nombre'],
        'target_options': ['código', 'nombre'],
        'errors': {
            'syntax': "❌ Sintaxis: {lang} país de <código|nombre> a <código|nombre> <valor>",
            'source': "❌ El origen debe ser 'código' o 'nombre'",
            'target': "❌ El destino debe ser 'código' o 'nombre'",
        },
    },
    'jp': {
        'from_kw': 'から',
        'to_kw': 'まで',
        'source_options': ['コード', '名前'],
        'target_options': ['コード', '名前'],
        'errors': {
            'syntax': "❌ 構文: {lang} 国 から <コード|名前> まで <コード|名前> <値>",
            'source': "❌ ソースは 'コード' または '名前' でなければなりません",
            'target': "❌ ターゲットは 'コード' または '名前' でなければなりません",
        },
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

    from_kw, source_type, to_kw, target_type, value = parts

    if from_kw != cfg['from_kw'] or to_kw != cfg['to_kw']:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

    if source_type not in cfg['source_options'] or target_type not in cfg['target_options']:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

    # Mappa i termini localizzati a 'code'/'name' interni
    source_map = dict(zip(cfg['source_options'], ['code', 'name']))
    target_map = dict(zip(cfg['target_options'], ['code', 'name']))
    src = source_map[source_type]
    tgt = target_map[target_type]

    if src == 'code' and tgt == 'name':
        # Conversione codice → nome
        result = code_to_name(value, lang)
        print(result)
    elif src == 'name' and tgt == 'code':
        # Conversione nome → codice
        result = name_to_code(value, lang)
        print(result)
    else:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: country_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = sys.argv[2]
    parse(lang, params)
