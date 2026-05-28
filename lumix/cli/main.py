#!/usr/bin/env python3
"""
Script di routing per chiamare diversi parser in base alla lingua e al tipo di conversione,
salvando tutto il testo dopo la seconda parola in una variabile e passandolo al parser.
Ora, ogni parser riceverà come primo parametro la lingua, seguito dalla stringa di input.
Uso: python3 script.py <lang> <key> <input...>
"""
import argparse
import os
import subprocess
import sys

try:
    import argcomplete
except ImportError:
    argcomplete = None


def discover_converters():
    """
    (Future plugin system) Scansione dinamica dei moduli converter.
    Attualmente non usata, mantiene la mappa esplicita per stabilità.
    """
    import pkgutil
    from pathlib import Path

    import lumix

    converters = {}
    for module_info in pkgutil.iter_modules(lumix.__path__):
        module_name = module_info.name
        if module_name in ("cli", "common", "gui", "tests"):
            continue
        parser_path = Path(lumix.__file__).parent / module_name / "parser.py"
        if parser_path.exists():
            converters[module_name] = f"{module_name}.parser"
    return converters


# Setup shell autocomplete for lang and key
def setup_autocomplete():
    ac_parser = argparse.ArgumentParser(add_help=False)
    ac_parser.add_argument("lang", choices=list(PARSER_MODULES.keys()))
    key_arg = ac_parser.add_argument("key")

    def key_completer(prefix, parsed_args, **kwargs):
        return [
            k for k in PARSER_MODULES.get(parsed_args.lang, {}) if k.startswith(prefix)
        ]

    key_arg.completer = key_completer
    if argcomplete:
        argcomplete.autocomplete(ac_parser)


# Mappatura dei valori ammessi e del relativo modulo parser
PARSER_MODULES = {
    "fr": {
        "devise": "currency.parser",
        "température": "temps.parser",
        "base": "base.parser",
        "poids": "weight.parser",
        "longueur": "length.parser",
        "volume": "volume.parser",
        "surface": "area.parser",
        "vitesse": "speed.parser",
        "temps": "time.parser",
        "énergie": "energy.parser",
        "pression": "pressure.parser",
        "puissance": "power.parser",
        "données": "data.parser",
        "débit": "bitrate.parser",
        "hash": "hash.parser",
        "couleur": "color.parser",
        "outilsip": "iptools.parser",
        "fuseaux": "timezones.parser",
        "date": "date.parser",
        "calendrier": "calendar.parser",
        "âge": "age.parser",
        "motsdepasse": "passwords.parser",
        "pays": "country.parser",
        "langue": "language.parser",
        "symbolesunités": "unitsymbols.parser",
        "romain": "roman.parser",
        "morse": "morse.parser",
        "robotfuseau": "timezonebot.parser",
        "parlé": "spoken.parser",
        "phonétique": "phonetic.parser",
    },
    "en": {
        "currency": "currency.parser",
        "temperature": "temps.parser",
        "base": "base.parser",
        "weight": "weight.parser",
        "length": "length.parser",
        "volume": "volume.parser",
        "area": "area.parser",
        "speed": "speed.parser",
        "time": "time.parser",
        "energy": "energy.parser",
        "pressure": "pressure.parser",
        "power": "power.parser",
        "data": "data.parser",
        "bitrate": "bitrate.parser",
        "hash": "hash.parser",
        "color": "color.parser",
        "iptools": "iptools.parser",
        "timezones": "timezones.parser",
        "date": "date.parser",
        "calendar": "calendar.parser",
        "age": "age.parser",
        "passwords": "passwords.parser",
        "country": "country.parser",
        "language": "language.parser",
        "unitsymbols": "unitsymbols.parser",
        "roman": "roman.parser",
        "morse": "morse.parser",
        "timezonebot": "timezonebot.parser",
        "spoken": "spoken.parser",
        "phonetic": "phonetic.parser",
    },
    "it": {
        "valuta": "currency.parser",
        "temperatura": "temps.parser",
        "base": "base.parser",
        "peso": "weight.parser",
        "lunghezza": "length.parser",
        "volume": "volume.parser",
        "area": "area.parser",
        "velocità": "speed.parser",
        "tempo": "time.parser",
        "energia": "energy.parser",
        "pressione": "pressure.parser",
        "potenza": "power.parser",
        "dati": "data.parser",
        "bitrate": "bitrate.parser",
        "hash": "hash.parser",
        "colore": "color.parser",
        "strumentiip": "iptools.parser",
        "fusi": "timezones.parser",
        "data": "date.parser",
        "calendario": "calendar.parser",
        "età": "age.parser",
        "password": "passwords.parser",
        "paese": "country.parser",
        "lingua": "language.parser",
        "simboliunita": "unitsymbols.parser",
        "romano": "roman.parser",
        "morse": "morse.parser",
        "timezonebot": "timezonebot.parser",
        "parlato": "spoken.parser",
        "fonetico": "phonetic.parser",
    },
    "jp": {
        "通貨": "currency.parser",
        "温度": "temps.parser",
        "基数": "base.parser",
        "重さ": "weight.parser",
        "長さ": "length.parser",
        "体積": "volume.parser",
        "面積": "area.parser",
        "速度": "speed.parser",
        "時間": "time.parser",
        "エネルギー": "energy.parser",
        "圧力": "pressure.parser",
        "電力": "power.parser",
        "データ": "data.parser",
        "ビットレート": "bitrate.parser",
        "ハッシュ": "hash.parser",
        "色": "color.parser",
        "IPツール": "iptools.parser",
        "タイムゾーン": "timezones.parser",
        "日付": "date.parser",
        "カレンダー": "calendar.parser",
        "年齢": "age.parser",
        "パスワード": "passwords.parser",
        "国": "country.parser",
        "言語": "language.parser",
        "単位記号": "unitsymbols.parser",
        "ローマ数字": "roman.parser",
        "モールス": "morse.parser",
        "タイムゾーンボット": "timezonebot.parser",
        "話し言葉": "spoken.parser",
        "発音記号": "phonetic.parser",
    },
    "es": {
        "moneda": "currency.parser",
        "temperatura": "temps.parser",
        "base": "base.parser",
        "peso": "weight.parser",
        "longitud": "length.parser",
        "volumen": "volume.parser",
        "área": "area.parser",
        "velocidad": "speed.parser",
        "tiempo": "time.parser",
        "energía": "energy.parser",
        "presión": "pressure.parser",
        "potencia": "power.parser",
        "datos": "data.parser",
        "bitrate": "bitrate.parser",
        "hash": "hash.parser",
        "color": "color.parser",
        "herramientasip": "iptools.parser",
        "husos": "timezones.parser",
        "fecha": "date.parser",
        "calendario": "calendar.parser",
        "edad": "age.parser",
        "contraseñas": "passwords.parser",
        "país": "country.parser",
        "idioma": "language.parser",
        "simbolosunidad": "unitsymbols.parser",
        "romano": "roman.parser",
        "morse": "morse.parser",
        "zonabot": "timezonebot.parser",
        "hablado": "spoken.parser",
        "fonético": "phonetic.parser",
    },
}

# Messaggi di errore localizzati
ERROR_MESSAGES = {
    "fr": "❌ Valeur '{value}' non valide pour la langue '{lang}'",
    "en": "❌ Invalid value '{value}' for language '{lang}'",
    "it": "❌ Valore '{value}' non valido per la lingua '{lang}'",
    "jp": "❌ 無効な値 '{value}'（日本語）",
    "es": "❌ Valor '{value}' no válido para el idioma '{lang}'",
}


def run_cli():
    """Entry point per il comando lumix (chiama main())."""
    sys.exit(main())


def main():
    if len(sys.argv) == 2 and sys.argv[1] in ("--help", "-h"):
        print("Usage: lumix <lang> <key> <input...>")
        print("Example: lumix en temperature from C to F 36.5")
        return 0
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <lang> <key> <input...>")
        return 1

    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <lang> <key> <input...>")
        return 1

    lang = sys.argv[1]
    key = sys.argv[2]
    # Tutto ciò che segue la seconda parola
    rest_args = sys.argv[3:]

    modules = PARSER_MODULES.get(lang)
    if modules is None:
        print(f"❌ Lingua non riconosciuta: {lang}")
        return 1

    module_path = modules.get(key)
    if module_path is None:
        msg = ERROR_MESSAGES.get(
            lang, "❌ Invalid value '{value}' for language '{lang}'"
        )
        print(msg.format(value=key, lang=lang))
        return 1

    # Invoca lo script parser via subprocess
    script_dir = os.path.dirname(__file__)
    # Il percorso del parser si trova in ../<module_path>.py
    parser_script = os.path.normpath(
        os.path.join(script_dir, "..", module_path.replace(".", os.sep) + ".py")
    )
    cmd = [sys.executable, parser_script, lang] + rest_args
    result = subprocess.run(cmd)
    return result.returncode


if __name__ == "__main__":
    setup_autocomplete()
    sys.exit(main())
