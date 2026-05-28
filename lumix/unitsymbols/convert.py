"""
Database di unità di misura con simbolo, nome e tipo.
"""

UNITS_DB = {
    "power": [
        {"symbol": "W", "name": "watt"},
        {"symbol": "kW", "name": "kilowatt"},
        {"symbol": "MW", "name": "megawatt"},
        {"symbol": "hp", "name": "horsepower (mechanical)"},
        {"symbol": "CV", "name": "cavallo vapore"},
    ],
    "length": [
        {"symbol": "m", "name": "meter"},
        {"symbol": "km", "name": "kilometer"},
        {"symbol": "cm", "name": "centimeter"},
        {"symbol": "mm", "name": "millimeter"},
        {"symbol": "mi", "name": "mile"},
        {"symbol": "yd", "name": "yard"},
        {"symbol": "ft", "name": "foot"},
        {"symbol": "in", "name": "inch"},
        {"symbol": "nmi", "name": "nautical mile"},
    ],
    "mass": [
        {"symbol": "g", "name": "gram"},
        {"symbol": "kg", "name": "kilogram"},
        {"symbol": "mg", "name": "milligram"},
        {"symbol": "lb", "name": "pound"},
        {"symbol": "oz", "name": "ounce"},
    ],
    "time": [
        {"symbol": "s", "name": "second"},
        {"symbol": "min", "name": "minute"},
        {"symbol": "h", "name": "hour"},
        {"symbol": "d", "name": "day"},
        {"symbol": "wk", "name": "week"},   # cambiato da 'w' a 'wk' per evitare conflitto con watt
    ],
    "temperature": [
        {"symbol": "°C", "name": "degree Celsius"},
        {"symbol": "°F", "name": "degree Fahrenheit"},
        {"symbol": "K", "name": "kelvin"},
    ],
    "data": [
        {"symbol": "B", "name": "byte"},
        {"symbol": "KB", "name": "kilobyte"},
        {"symbol": "MB", "name": "megabyte"},
        {"symbol": "GB", "name": "gigabyte"},
        {"symbol": "TB", "name": "terabyte"},
    ],
    "bitrate": [
        {"symbol": "bps", "name": "bit per second"},
        {"symbol": "kbps", "name": "kilobit per second"},
        {"symbol": "Mbps", "name": "megabit per second"},
        {"symbol": "Gbps", "name": "gigabit per second"},
        {"symbol": "Tbps", "name": "terabit per second"},
    ],
    "pressure": [
        {"symbol": "Pa", "name": "pascal"},
        {"symbol": "bar", "name": "bar"},
        {"symbol": "atm", "name": "atmosphere"},
        {"symbol": "mmHg", "name": "millimeter of mercury"},
        {"symbol": "psi", "name": "pound per square inch"},
    ],
    "energy": [
        {"symbol": "J", "name": "joule"},
        {"symbol": "kJ", "name": "kilojoule"},
        {"symbol": "cal", "name": "calorie"},
        {"symbol": "kcal", "name": "kilocalorie"},
        {"symbol": "Wh", "name": "watt-hour"},
        {"symbol": "kWh", "name": "kilowatt-hour"},
        {"symbol": "eV", "name": "electronvolt"},
    ],
    "area": [
        {"symbol": "m²", "name": "square meter"},
        {"symbol": "km²", "name": "square kilometer"},
        {"symbol": "ft²", "name": "square foot"},
        {"symbol": "mi²", "name": "square mile"},
        {"symbol": "ha", "name": "hectare"},
        {"symbol": "acre", "name": "acre"},
    ],
    "volume": [
        {"symbol": "L", "name": "liter"},
        {"symbol": "mL", "name": "milliliter"},
        {"symbol": "m³", "name": "cubic meter"},
        {"symbol": "gal", "name": "gallon (US)"},
        {"symbol": "qt", "name": "quart"},
        {"symbol": "pt", "name": "pint"},
        {"symbol": "cup", "name": "cup"},
        {"symbol": "fl oz", "name": "fluid ounce"},
    ],
    "speed": [
        {"symbol": "km/h", "name": "kilometer per hour"},
        {"symbol": "mph", "name": "mile per hour"},
        {"symbol": "m/s", "name": "meter per second"},
        {"symbol": "kn", "name": "knot"},
    ],
}

# Costruiamo indici per ricerca rapida
SYMBOL_TO_INFO = {}
NAME_TO_INFO = {}
for unit_type, units in UNITS_DB.items():
    for u in units:
        sym = u["symbol"]
        name = u["name"]
        SYMBOL_TO_INFO[sym.lower()] = {"symbol": sym, "name": name, "type": unit_type}
        NAME_TO_INFO[name.lower()] = {"symbol": sym, "name": name, "type": unit_type}

def get_info_by_symbol(symbol: str) -> dict:
    """Restituisce le informazioni (nome, tipo) per un dato simbolo (case‑insensitive)."""
    key = symbol.lower()
    return SYMBOL_TO_INFO.get(key)

def get_info_by_name(name: str) -> dict:
    """Restituisce le informazioni (simbolo, tipo) per un dato nome (case‑insensitive)."""
    key = name.lower()
    return NAME_TO_INFO.get(key)
