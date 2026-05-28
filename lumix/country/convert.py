# Dati dei paesi: codici ISO 3166-1 alpha-2 con nomi in varie lingue
_COUNTRY_NAMES = {
    "en": {
        "IT": "Italy",
        "FR": "France",
        "ES": "Spain",
        "DE": "Germany",
        "GB": "United Kingdom",
        "US": "United States",
        "JP": "Japan",
        "CN": "China",
        "RU": "Russia",
        "BR": "Brazil",
        # ... aggiungere altri secondo necessità
    },
    "it": {
        "IT": "Italia",
        "FR": "Francia",
        "ES": "Spagna",
        "DE": "Germania",
        "GB": "Regno Unito",
        "US": "Stati Uniti",
        "JP": "Giappone",
        "CN": "Cina",
        "RU": "Russia",
        "BR": "Brasile",
    },
    "fr": {
        "IT": "Italie",
        "FR": "France",
        "ES": "Espagne",
        "DE": "Allemagne",
        "GB": "Royaume-Uni",
        "US": "États-Unis",
        "JP": "Japon",
        "CN": "Chine",
        "RU": "Russie",
        "BR": "Brésil",
    },
    "es": {
        "IT": "Italia",
        "FR": "Francia",
        "ES": "España",
        "DE": "Alemania",
        "GB": "Reino Unido",
        "US": "Estados Unidos",
        "JP": "Japón",
        "CN": "China",
        "RU": "Rusia",
        "BR": "Brasil",
    },
    "jp": {
        "IT": "イタリア",
        "FR": "フランス",
        "ES": "スペイン",
        "DE": "ドイツ",
        "GB": "イギリス",
        "US": "アメリカ合衆国",
        "JP": "日本",
        "CN": "中国",
        "RU": "ロシア",
        "BR": "ブラジル",
    },
}


def code_to_name(code: str, lang: str = "en") -> str:
    """
    Restituisce il nome del paese per il codice e la lingua dati.
    """
    lang = lang.lower()
    if lang not in _COUNTRY_NAMES:
        lang = "en"  # fallback
    code = code.upper()
    return _COUNTRY_NAMES[lang].get(code, f"Unknown code '{code}'")


def name_to_code(name: str, lang: str = "en") -> str:
    """
    Restituisce il codice del paese per il nome e la lingua dati (case‑insensitive).
    """
    lang = lang.lower()
    if lang not in _COUNTRY_NAMES:
        lang = "en"
    for code, n in _COUNTRY_NAMES[lang].items():
        if n.lower() == name.lower():
            return code
    return f"Unknown name '{name}'"
