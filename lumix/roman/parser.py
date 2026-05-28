#!/usr/bin/env python3
"""
Parser per il modulo roman.
Sintassi: <lang> roman <comando> <valore>
Comandi:
  from <numero>   - converte numero arabo in romano
  to <numero>     - converte numero romano in arabo
Esempio: en roman from 2025
         it romano da 2025
"""
import sys

from .convert import int_to_roman, roman_to_int

LANG_CONFIG = {
    'en': {
        'cmd_from': 'from',
        'cmd_to': 'to',
        'errors': {
            'syntax': "❌ Syntax: {lang} roman <from|to> <value>",
            'invalid_arabic': "❌ Invalid Arabic number (must be 1-3999)",
            'invalid_roman': "❌ Invalid Roman numeral",
        },
        'output': {
            'from': '{value} → {result}',
            'to': '{value} → {result}',
        }
    },
    'it': {
        'cmd_from': 'da',
        'cmd_to': 'a',
        'errors': {
            'syntax': "❌ Sintassi: {lang} romano <da|a> <valore>",
            'invalid_arabic': "❌ Numero arabo non valido (deve essere 1-3999)",
            'invalid_roman': "❌ Numero romano non valido",
        },
        'output': {
            'from': '{valore} → {risultato}',
            'to': '{valore} → {risultato}',
        }
    },
    'fr': {
        'cmd_from': 'de',
        'cmd_to': 'à',
        'errors': {
            'syntax': "❌ Syntaxe : {lang} romain <de|à> <valeur>",
            'invalid_arabic': "❌ Nombre arabe invalide (doit être 1-3999)",
            'invalid_roman': "❌ Chiffre romain invalide",
        },
        'output': {
            'from': '{valeur} → {résultat}',
            'to': '{valeur} → {résultat}',
        }
    },
    'es': {
        'cmd_from': 'de',
        'cmd_to': 'a',
        'errors': {
            'syntax': "❌ Sintaxis: {lang} romano <de|a> <valor>",
            'invalid_arabic': "❌ Número arábigo no válido (debe ser 1-3999)",
            'invalid_roman': "❌ Número romano no válido",
        },
        'output': {
            'from': '{valor} → {resultado}',
            'to': '{valor} → {resultado}',
        }
    },
    'jp': {
        'cmd_from': 'から',
        'cmd_to': 'へ',
        'errors': {
            'syntax': "❌ 構文: {lang} ローマ数字 <から|へ> <値>",
            'invalid_arabic': "❌ 無効なアラビア数字 (1-3999 である必要があります)",
            'invalid_roman': "❌ 無効なローマ数字",
        },
        'output': {
            'from': '{値} → {結果}',
            'to': '{値} → {結果}',
        }
    },
}

def parse(lang: str, params: str):
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    parts = params.split(maxsplit=1)
    if len(parts) != 2:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

    cmd, value = parts
    value = value.strip()
    # Rimuovi eventuali virgolette
    if (value.startswith('"') and value.endswith('"')) or \
       (value.startswith("'") and value.endswith("'")):
        value = value[1:-1]

    if cmd == cfg['cmd_from']:
        # arabo → romano
        try:
            num = int(value)
            result = int_to_roman(num)
            print(cfg['output']['from'].format(value=value, result=result))
        except ValueError:
            print(cfg['errors']['invalid_arabic'])
            sys.exit(1)
    elif cmd == cfg['cmd_to']:
        # romano → arabo
        try:
            result = roman_to_int(value)
            print(cfg['output']['to'].format(value=value, result=result))
        except ValueError:
            print(cfg['errors']['invalid_roman'])
            sys.exit(1)
    else:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: roman_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = sys.argv[2]
    parse(lang, params)
