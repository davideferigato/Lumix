#!/usr/bin/env python3
"""
Parser per il modulo morse.
Sintassi: <lang> morse <comando> <stringa>
Comandi:
  from-text <testo>   - converte testo in codice Morse
  to-text <codice>     - converte codice Morse in testo
Esempio: en morse to-text "... --- ..."
"""
import sys

from .convert import morse_to_text, text_to_morse

SUPPORTED_COMMANDS = ['from-text', 'to-text']

LANG_CONFIG = {
    'en': {
        'errors': {
            'syntax': "❌ Syntax: {lang} morse <from-text|to-text> <string>",
            'unknown_cmd': "❌ Unknown command. Use 'from-text' or 'to-text'",
        },
        'output': {
            'from-text': 'Morse code: {result}',
            'to-text': 'Text: {result}',
        }
    },
    'it': {
        'errors': {
            'syntax': "❌ Sintassi: {lang} morse <da-testo|a-testo> <stringa>",
            'unknown_cmd': "❌ Comando sconosciuto. Usa 'da-testo' o 'a-testo'",
        },
        'output': {
            'from-text': 'Codice Morse: {result}',
            'to-text': 'Testo: {result}',
        }
    },
    'fr': {
        'errors': {
            'syntax': "❌ Syntaxe : {lang} morse <de-texte|à-texte> <chaîne>",
            'unknown_cmd': "❌ Commande inconnue. Utilisez 'de-texte' ou 'à-texte'",
        },
        'output': {
            'from-text': 'Code Morse : {result}',
            'to-text': 'Texte : {result}',
        }
    },
    'es': {
        'errors': {
            'syntax': "❌ Sintaxis: {lang} morse <de-texto|a-texto> <cadena>",
            'unknown_cmd': "❌ Comando desconocido. Usa 'de-texto' o 'a-texto'",
        },
        'output': {
            'from-text': 'Código Morse: {result}',
            'to-text': 'Texto: {result}',
        }
    },
    'jp': {
        'errors': {
            'syntax': "❌ 構文: {lang} モールス <テキストから|テキストへ> <文字列>",
            'unknown_cmd': "❌ 不明なコマンド。'テキストから' または 'テキストへ' を使用してください",
        },
        'output': {
            'from-text': 'モールス信号: {result}',
            'to-text': 'テキスト: {result}',
        }
    },
}

def parse(lang: str, params: str):
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    # Il resto dei parametri può contenere spazi, quindi usiamo maxsplit=1
    parts = params.split(maxsplit=1)
    if len(parts) != 2:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

    cmd, value = parts
    cmd = cmd.lower()

    # Mappa i comandi localizzati a quelli interni
    # Per semplicità, supportiamo solo i comandi inglesi per ora,
    # ma potremmo estendere con mappature per lingua
    if cmd not in SUPPORTED_COMMANDS:
        print(cfg['errors']['unknown_cmd'])
        sys.exit(1)

    # Rimuovi eventuali virgolette attorno al valore
    if (value.startswith('"') and value.endswith('"')) or \
       (value.startswith("'") and value.endswith("'")):
        value = value[1:-1]

    try:
        if cmd == 'from-text':
            result = text_to_morse(value)
        else:  # to-text
            result = morse_to_text(value)
    except Exception as e:
        print(f"❌ Errore durante la conversione: {e}")
        sys.exit(1)

    print(cfg['output'][cmd].format(result=result))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: morse_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = sys.argv[2]
    parse(lang, params)
