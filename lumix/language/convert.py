# Dizionario: per ogni lingua supportata, mappa codice ISO -> nome in quella lingua
# Includiamo solo un set base di lingue (quelle in cui è localizzato lumix)
_LANGUAGE_NAMES = {
    "en": {
        "en": "English",
        "it": "Italian",
        "fr": "French",
        "es": "Spanish",
        "jp": "Japanese",
        "de": "German",
        "zh": "Chinese",
        "ru": "Russian",
        "pt": "Portuguese",
        "ar": "Arabic",
        "hi": "Hindi",
        "bn": "Bengali",
        # ... possiamo aggiungere altre secondo necessità
    },
    "it": {
        "en": "Inglese",
        "it": "Italiano",
        "fr": "Francese",
        "es": "Spagnolo",
        "jp": "Giapponese",
        "de": "Tedesco",
        "zh": "Cinese",
        "ru": "Russo",
        "pt": "Portoghese",
        "ar": "Arabo",
        "hi": "Hindi",
        "bn": "Bengalese",
    },
    "fr": {
        "en": "Anglais",
        "it": "Italien",
        "fr": "Français",
        "es": "Espagnol",
        "jp": "Japonais",
        "de": "Allemand",
        "zh": "Chinois",
        "ru": "Russe",
        "pt": "Portugais",
        "ar": "Arabe",
        "hi": "Hindi",
        "bn": "Bengali",
    },
    "es": {
        "en": "Inglés",
        "it": "Italiano",
        "fr": "Francés",
        "es": "Español",
        "jp": "Japonés",
        "de": "Alemán",
        "zh": "Chino",
        "ru": "Ruso",
        "pt": "Portugués",
        "ar": "Árabe",
        "hi": "Hindi",
        "bn": "Bengalí",
    },
    "jp": {
        "en": "英語",
        "it": "イタリア語",
        "fr": "フランス語",
        "es": "スペイン語",
        "jp": "日本語",
        "de": "ドイツ語",
        "zh": "中国語",
        "ru": "ロシア語",
        "pt": "ポルトガル語",
        "ar": "アラビア語",
        "hi": "ヒンディー語",
        "bn": "ベンガル語",
    },
}


def code_to_name(code: str, lang: str = "en") -> str:
    """
    Restituisce il nome della lingua per il codice ISO dato, nella lingua specificata.
    """
    lang = lang.lower()
    if lang not in _LANGUAGE_NAMES:
        lang = "en"  # fallback
    code = code.lower()
    return _LANGUAGE_NAMES[lang].get(code, f"Unknown code '{code}'")


def name_to_code(name: str, lang: str = "en") -> str:
    """
    Restituisce il codice ISO per il nome della lingua dato, cercando nella lingua specificata.
    """
    lang = lang.lower()
    if lang not in _LANGUAGE_NAMES:
        lang = "en"
    # Cerca il nome (case-insensitive) tra i valori della lingua
    for code, n in _LANGUAGE_NAMES[lang].items():
        if n.lower() == name.lower():
            return code
    # Se non trovato, restituisci messaggio di errore
    return f"Unknown language name '{name}'"
