#!/usr/bin/env python3
"""
Parser per il modulo calendar.
Sintassi: <lang> calendar diff <date1> <date2>
"""
import re
import sys

from .convert import date_diff

# Configurazione per lingua
LANG_CONFIG = {
    'en': {
        'command': 'diff',
        'date_format': '%Y-%m-%d',
        'date_pattern': r'^\d{4}-\d{2}-\d{2}$',
        'errors': {
            'syntax': "❌ Syntax: {lang} calendar diff YYYY-MM-DD YYYY-MM-DD",
            'date': "❌ Invalid date format. Use YYYY-MM-DD (e.g., 2025-01-01)",
        },
        'output': "Difference: {days} days, {weeks} weeks, {months} months, {years} years",
    },
    'it': {
        'command': 'diff',
        'date_format': '%d/%m/%Y',
        'date_pattern': r'^\d{2}/\d{2}/\d{4}$',
        'errors': {
            'syntax': "❌ Sintassi: {lang} calendario diff GG/MM/AAAA GG/MM/AAAA",
            'date': "❌ Formato data non valido. Usa GG/MM/AAAA (es., 01/01/2025)",
        },
        'output': "Differenza: {days} giorni, {weeks} settimane, {months} mesi, {years} anni",
    },
    'fr': {
        'command': 'diff',
        'date_format': '%d/%m/%Y',
        'date_pattern': r'^\d{2}/\d{2}/\d{4}$',
        'errors': {
            'syntax': "❌ Syntaxe : {lang} calendrier diff JJ/MM/AAAA JJ/MM/AAAA",
            'date': "❌ Format de date invalide. Utilisez JJ/MM/AAAA (ex., 01/01/2025)",
        },
        'output': "Différence : {days} jours, {weeks} semaines, {months} mois, {years} ans",
    },
    'es': {
        'command': 'diff',
        'date_format': '%d/%m/%Y',
        'date_pattern': r'^\d{2}/\d{2}/\d{4}$',
        'errors': {
            'syntax': "❌ Sintaxis: {lang} calendario diff DD/MM/AAAA DD/MM/AAAA",
            'date': "❌ Formato de fecha no válido. Use DD/MM/AAAA (ej., 01/01/2025)",
        },
        'output': "Diferencia: {days} días, {weeks} semanas, {months} meses, {years} años",
    },
    'jp': {
        'command': 'diff',
        'date_format': '%Y年%m月%d日',
        'date_pattern': r'^\d{4}年\d{2}月\d{2}日$',
        'errors': {
            'syntax': "❌ 構文: {lang} カレンダー diff YYYY年MM月DD日 YYYY年MM月DD日",
            'date': "❌ 日付形式が無効です。YYYY年MM月DD日を使用してください (例: 2025年01月01日)",
        },
        'output': "差: {days}日, {weeks}週間, {months}ヶ月, {years}年",
    },
}

def parse(lang: str, params: str):
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    parts = params.split()
    if len(parts) != 3:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

    command, date1_str, date2_str = parts
    if command != cfg['command']:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

    # Validazione formato date
    if not re.match(cfg['date_pattern'], date1_str) or not re.match(cfg['date_pattern'], date2_str):
        print(cfg['errors']['date'])
        sys.exit(1)

    # Calcolo differenza
    try:
        diff = date_diff(date1_str, date2_str, cfg['date_format'])
    except ValueError:
        print(cfg['errors']['date'])
        sys.exit(1)

    # Output
    output = cfg['output'].format(**diff)
    print(output)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: calendar_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = sys.argv[2]
    parse(lang, params)
