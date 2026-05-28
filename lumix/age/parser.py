#!/usr/bin/env python3
"""
Parser per il modulo age.
Sintassi: <lang> age from <birth_date>
"""
import re
import sys

from .convert import calculate_age

# Configurazione per lingua
LANG_CONFIG = {
    'en': {
        'from_kw': 'from',
        'date_format': '%Y-%m-%d',
        'date_pattern': r'^\d{4}-\d{2}-\d{2}$',
        'errors': {
            'syntax': "❌ Syntax: {lang} age from YYYY-MM-DD",
            'date': "❌ Invalid date format. Use YYYY-MM-DD (e.g., 1990-05-23)",
        },
        'output': "{} years old",
    },
    'it': {
        'from_kw': 'da',
        'date_format': '%d/%m/%Y',
        'date_pattern': r'^\d{2}/\d{2}/\d{4}$',
        'errors': {
            'syntax': "❌ Sintassi: {lang} età da GG/MM/AAAA",
            'date': "❌ Formato data non valido. Usa GG/MM/AAAA (es., 23/05/1990)",
        },
        'output': "{} anni",
    },
    'fr': {
        'from_kw': 'de',
        'date_format': '%d/%m/%Y',
        'date_pattern': r'^\d{2}/\d{2}/\d{4}$',
        'errors': {
            'syntax': "❌ Syntaxe: {lang} âge de JJ/MM/AAAA",
            'date': "❌ Format de date invalide. Utilisez JJ/MM/AAAA (ex., 23/05/1990)",
        },
        'output': "{} ans",
    },
    'es': {
        'from_kw': 'de',
        'date_format': '%d/%m/%Y',
        'date_pattern': r'^\d{2}/\d{2}/\d{4}$',
        'errors': {
            'syntax': "❌ Sintaxis: {lang} edad de DD/MM/AAAA",
            'date': "❌ Formato de fecha no válido. Use DD/MM/AAAA (ej., 23/05/1990)",
        },
        'output': "{} años",
    },
    'jp': {
        'from_kw': 'から',
        'date_format': '%Y年%m月%d日',
        'date_pattern': r'^\d{4}年\d{2}月\d{2}日$',
        'errors': {
            'syntax': "❌ 構文: {lang} 年齢 から YYYY年MM月DD日",
            'date': "❌ 日付形式が無効です。YYYY年MM月DD日を使用してください (例: 1990年05月23日)",
        },
        'output': "{}歳",
    },
}

def parse(lang: str, params: str):
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    parts = params.split()
    if len(parts) != 2:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

    from_kw, birth_date_str = parts
    if from_kw != cfg['from_kw']:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

    if not re.match(cfg['date_pattern'], birth_date_str):
        print(cfg['errors']['date'])
        sys.exit(1)

    try:
        age = calculate_age(birth_date_str, cfg['date_format'])
        print(cfg['output'].format(age))
    except ValueError:
        print(cfg['errors']['date'])
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: age_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = sys.argv[2]
    parse(lang, params)
