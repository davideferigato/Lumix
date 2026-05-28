#!/usr/bin/env python3
"""
Parser per il modulo timezonebot.
Sintassi: <lang> timezonebot what-time <città>
Esempio: en timezonebot what-time Tokyo
"""
import sys

from .convert import what_time

LANG_CONFIG = {
    'en': {
        'cmd': 'what-time',
        'errors': {
            'syntax': "❌ Syntax: {lang} timezonebot what-time <city>",
        },
    },
    'it': {
        'cmd': 'what-time',
        'errors': {
            'syntax': "❌ Sintassi: {lang} timezonebot what-time <città>",
        },
    },
    'fr': {
        'cmd': 'what-time',
        'errors': {
            'syntax': "❌ Syntaxe : {lang} timezonebot what-time <ville>",
        },
    },
    'es': {
        'cmd': 'what-time',
        'errors': {
            'syntax': "❌ Sintaxis: {lang} timezonebot what-time <ciudad>",
        },
    },
    'jp': {
        'cmd': 'what-time',
        'errors': {
            'syntax': "❌ 構文: {lang} timezonebot what-time <都市>",
        },
    },
}

def parse(lang: str, params: str):
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    parts = params.split(maxsplit=1)
    if len(parts) != 2 or parts[0] != cfg['cmd']:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

    city = parts[1].strip()
    # Rimuovi eventuali virgolette
    if (city.startswith('"') and city.endswith('"')) or \
       (city.startswith("'") and city.endswith("'")):
        city = city[1:-1]

    result = what_time(city)
    print(result)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: timezonebot_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = sys.argv[2]
    parse(lang, params)
