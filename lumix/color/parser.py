#!/usr/bin/env python3
"""
Parser per il modulo color.
Sintassi: <lang> color from rgb to hex <r,g,b>  (con virgole)
Oppure: <lang> color from hex to rgb <#RRGGBB>
"""
import re
import sys

from lumix.color.convert import hex_to_rgb, rgb_to_hex

LANG_CONFIG = {
    "en": {
        "from_kw": "from",
        "to_kw": "to",
        "rgb_pattern": r"^(\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})$",
        "hex_pattern": r"^#?[0-9A-Fa-f]{6}$",
        "errors": {
            "syntax": "❌ Syntax: {lang} color from rgb to hex <r,g,b> or from hex to rgb <#RRGGBB>",
            "rgb": "❌ Invalid RGB values. Use format: 255,255,255 (each 0-255)",
            "hex": "❌ Invalid hex color. Use format: #RRGGBB or RRGGBB",
        },
        "output_rgb2hex": "RGB({r},{g},{b}) → {hex}",
        "output_hex2rgb": "{hex} → RGB({r},{g},{b})",
    },
    "it": {
        "from_kw": "da",
        "to_kw": "a",
        "rgb_pattern": r"^(\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})$",
        "hex_pattern": r"^#?[0-9A-Fa-f]{6}$",
        "errors": {
            "syntax": "❌ Sintassi: {lang} colore da rgb a hex <r,g,b> o da hex a rgb <#RRGGBB>",
            "rgb": "❌ Valori RGB non validi. Usa formato: 255,255,255 (ogni valore 0-255)",
            "hex": "❌ Colore hex non valido. Usa formato: #RRGGBB o RRGGBB",
        },
        "output_rgb2hex": "RGB({r},{g},{b}) → {hex}",
        "output_hex2rgb": "{hex} → RGB({r},{g},{b})",
    },
    "fr": {
        "from_kw": "de",
        "to_kw": "à",
        "rgb_pattern": r"^(\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})$",
        "hex_pattern": r"^#?[0-9A-Fa-f]{6}$",
        "errors": {
            "syntax": "❌ Syntaxe : {lang} couleur de rgb à hex <r,v,b> ou de hex à rgb <#RRGGBB>",
            "rgb": "❌ Valeurs RGB invalides. Utilisez le format: 255,255,255 (chaque 0-255)",
            "hex": "❌ Couleur hex invalide. Utilisez le format: #RRGGBB ou RRGGBB",
        },
        "output_rgb2hex": "RGB({r},{g},{b}) → {hex}",
        "output_hex2rgb": "{hex} → RGB({r},{g},{b})",
    },
    "es": {
        "from_kw": "de",
        "to_kw": "a",
        "rgb_pattern": r"^(\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})$",
        "hex_pattern": r"^#?[0-9A-Fa-f]{6}$",
        "errors": {
            "syntax": "❌ Sintaxis: {lang} color de rgb a hex <r,g,b> o de hex a rgb <#RRGGBB>",
            "rgb": "❌ Valores RGB no válidos. Use formato: 255,255,255 (cada 0-255)",
            "hex": "❌ Color hex no válido. Use formato: #RRGGBB o RRGGBB",
        },
        "output_rgb2hex": "RGB({r},{g},{b}) → {hex}",
        "output_hex2rgb": "{hex} → RGB({r},{g},{b})",
    },
    "jp": {
        "from_kw": "から",
        "to_kw": "まで",
        "rgb_pattern": r"^(\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})$",
        "hex_pattern": r"^#?[0-9A-Fa-f]{6}$",
        "errors": {
            "syntax": "❌ 構文: {lang} 色 から rgb まで hex <r,g,b> または から hex まで rgb <#RRGGBB>",
            "rgb": "❌ RGB値が無効です。形式: 255,255,255 (各0-255)",
            "hex": "❌ 無効な16進色です。形式: #RRGGBB または RRGGBB",
        },
        "output_rgb2hex": "RGB({r},{g},{b}) → {hex}",
        "output_hex2rgb": "{hex} → RGB({r},{g},{b})",
    },
}


def parse(lang: str, params: str):
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    tokens = params.split()
    if len(tokens) != 5:
        print(cfg["errors"]["syntax"].format(lang=lang))
        sys.exit(1)

    from_kw, from_type, to_kw, to_type, value = tokens

    if from_kw != cfg["from_kw"] or to_kw != cfg["to_kw"]:
        print(cfg["errors"]["syntax"].format(lang=lang))
        sys.exit(1)

    from_type = from_type.lower()
    to_type = to_type.lower()

    # RGB -> HEX
    if from_type == "rgb" and to_type == "hex":
        match = re.match(cfg["rgb_pattern"], value)
        if not match:
            print(cfg["errors"]["rgb"])
            sys.exit(1)
        r, g, b = map(int, match.groups())
        try:
            hex_color = rgb_to_hex(r, g, b)
            print(cfg["output_rgb2hex"].format(r=r, g=g, b=b, hex=hex_color))
        except ValueError:
            print(cfg["errors"]["rgb"])
            sys.exit(1)

    # HEX -> RGB
    elif from_type == "hex" and to_type == "rgb":
        value = value.strip()
        if not re.match(cfg["hex_pattern"], value):
            print(cfg["errors"]["hex"])
            sys.exit(1)
        try:
            r, g, b = hex_to_rgb(value)
            # Formatta l'hex con # se manca
            hex_display = value if value.startswith("#") else f"#{value}"
            print(cfg["output_hex2rgb"].format(hex=hex_display, r=r, g=g, b=b))
        except ValueError:
            print(cfg["errors"]["hex"])
            sys.exit(1)

    else:
        print(cfg["errors"]["syntax"].format(lang=lang))
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: color_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = " ".join(sys.argv[2:])
    parse(lang, params)
