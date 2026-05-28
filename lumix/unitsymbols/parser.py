#!/usr/bin/env python3
"""
Parser per il modulo unitsymbols.
Sintassi: <lang> unitsymbols from <symbol|name> to <"unit name"|"symbol"|"type">
Esempio: en unitsymbols from W to "unit name"
         it unitsymbols da W a "nome unità"
"""
import sys

from .convert import get_info_by_name, get_info_by_symbol

LANG_CONFIG = {
    'en': {
        'from_kw': 'from',
        'to_kw': 'to',
        'target_options': {
            'unit name': 'name',
            'symbol': 'symbol',
            'type': 'type',
        },
        'errors': {
            'syntax': "❌ Syntax: {lang} unitsymbols from <symbol|name> to <'unit name'|'symbol'|'type'>",
            'not_found': "❌ Unit not found for '{query}'",
            'invalid_target': "❌ Invalid target. Use: 'unit name', 'symbol', or 'type'",
        },
    },
    'it': {
        'from_kw': 'da',
        'to_kw': 'a',
        'target_options': {
            'nome unità': 'name',
            'simbolo': 'symbol',
            'tipo': 'type',
        },
        'errors': {
            'syntax': "❌ Sintassi: {lang} unitsymbols da <simbolo|nome> a <'nome unità'|'simbolo'|'tipo'>",
            'not_found': "❌ Unità non trovata per '{query}'",
            'invalid_target': "❌ Destinazione non valida. Usa: 'nome unità', 'simbolo', o 'tipo'",
        },
    },
    'fr': {
        'from_kw': 'de',
        'to_kw': 'à',
        'target_options': {
            'nom unité': 'name',
            'symbole': 'symbol',
            'type': 'type',
        },
        'errors': {
            'syntax': "❌ Syntaxe : {lang} unités de <symbole|nom> à <'nom unité'|'symbole'|'type'>",
            'not_found': "❌ Unité non trouvée pour '{query}'",
            'invalid_target': "❌ Cible invalide. Utilisez : 'nom unité', 'symbole', ou 'type'",
        },
    },
    'es': {
        'from_kw': 'de',
        'to_kw': 'a',
        'target_options': {
            'nombre unidad': 'name',
            'símbolo': 'symbol',
            'tipo': 'type',
        },
        'errors': {
            'syntax': "❌ Sintaxis: {lang} unidades de <símbolo|nombre> a <'nombre unidad'|'símbolo'|'tipo'>",
            'not_found': "❌ Unidad no encontrada para '{query}'",
            'invalid_target': "❌ Destino no válido. Use: 'nombre unidad', 'símbolo', o 'tipo'",
        },
    },
    'jp': {
        'from_kw': 'から',
        'to_kw': 'まで',
        'target_options': {
            '単位名': 'name',
            '記号': 'symbol',
            '種類': 'type',
        },
        'errors': {
            'syntax': "❌ 構文: {lang} 単位記号 から <記号|名前> まで <'単位名'|'記号'|'種類'>",
            'not_found': "❌ クエリ '{query}' に対する単位が見つかりません",
            'invalid_target': "❌ 無効なターゲットです。'単位名'、'記号'、または'種類'を使用してください",
        },
    },
}

def parse(lang: str, params: str):
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    # Il target può essere una frase con spazi (es. "unit name"), quindi usiamo maxsplit
    parts = params.split(maxsplit=3)
    if len(parts) != 4:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

    from_kw, query, to_kw, target = parts

    if from_kw != cfg['from_kw'] or to_kw != cfg['to_kw']:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

    # Rimuovi eventuali virgolette dal target
    if (target.startswith('"') and target.endswith('"')) or \
       (target.startswith("'") and target.endswith("'")):
        target = target[1:-1]

    # Verifica che il target sia tra le opzioni
    target_lower = target.lower()
    if target_lower not in cfg['target_options']:
        print(cfg['errors']['invalid_target'])
        sys.exit(1)

    target_key = cfg['target_options'][target_lower]

    # Cerca per simbolo o per nome
    info = get_info_by_symbol(query)
    if not info:
        info = get_info_by_name(query)
    if not info:
        print(cfg['errors']['not_found'].format(query=query))
        sys.exit(1)

    # Restituisci il campo richiesto
    result = info[target_key]
    print(result)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: unitsymbols_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = sys.argv[2]
    parse(lang, params)
