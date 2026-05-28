#!/usr/bin/env python3
"""
Parser per il modulo hash.
Sintassi: <lang> hash <algorithm> <string>
Esempio: en hash sha256 "hello world"
"""
import sys

from .convert import compute_hash

SUPPORTED_ALGORITHMS = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']

LANG_CONFIG = {
    'en': {
        'errors': {
            'syntax': "❌ Syntax: {lang} hash <algorithm> <string>",
            'algorithm': "❌ Unsupported algorithm. Use: md5, sha1, sha224, sha256, sha384, sha512",
        },
        'output': '"{input}" → {hash}',
    },
    'it': {
        'errors': {
            'syntax': "❌ Sintassi: {lang} hash <algoritmo> <stringa>",
            'algorithm': "❌ Algoritmo non supportato. Usa: md5, sha1, sha224, sha256, sha384, sha512",
        },
        'output': '"{input}" → {hash}',
    },
    'fr': {
        'errors': {
            'syntax': "❌ Syntaxe : {lang} hash <algorithme> <chaîne>",
            'algorithm': "❌ Algorithme non pris en charge. Utilisez : md5, sha1, sha224, sha256, sha384, sha512",
        },
        'output': '"{input}" → {hash}',
    },
    'es': {
        'errors': {
            'syntax': "❌ Sintaxis: {lang} hash <algoritmo> <cadena>",
            'algorithm': "❌ Algoritmo no soportado. Usa: md5, sha1, sha224, sha256, sha384, sha512",
        },
        'output': '"{input}" → {hash}',
    },
    'jp': {
        'errors': {
            'syntax': "❌ 構文: {lang} ハッシュ <アルゴリズム> <文字列>",
            'algorithm': "❌ サポートされていないアルゴリズムです。使用可能: md5, sha1, sha224, sha256, sha384, sha512",
        },
        'output': '"{input}" → {hash}',
    },
}

def parse(lang: str, params: str):
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    # Gestisce la possibilità che la stringa sia tra virgolette
    parts = params.split()
    if len(parts) < 2:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

    algorithm = parts[0].lower()
    if algorithm not in SUPPORTED_ALGORITHMS:
        print(cfg['errors']['algorithm'])
        sys.exit(1)

    # Ricostruisce la stringa (potrebbe contenere spazi se tra virgolette)
    # Se il primo carattere dopo l'algoritmo è una virgoletta, gestiamo
    input_str = ' '.join(parts[1:]).strip()
    # Rimuovi eventuali virgolette all'inizio e alla fine se presenti
    if (input_str.startswith('"') and input_str.endswith('"')) or \
       (input_str.startswith("'") and input_str.endswith("'")):
        input_str = input_str[1:-1]

    try:
        hash_result = compute_hash(input_str, algorithm)
    except ValueError:
        print(cfg['errors']['algorithm'])
        sys.exit(1)

    print(cfg['output'].format(input=input_str, hash=hash_result))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: hash_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = sys.argv[2]
    parse(lang, params)
