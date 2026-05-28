"""
Alfabeto fonetico NATO (ICAO) per lettere e numeri.
Fonte: https://en.wikipedia.org/wiki/NATO_phonetic_alphabet
"""

# Mappa carattere -> parola fonetica (solo lettere e numeri)
PHONETIC_MAP = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee',
    'Z': 'Zulu',
    '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
    '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine',
}

def text_to_phonetic(text: str) -> str:
    """
    Converte una stringa in alfabeto fonetico NATO.
    I caratteri non mappati vengono lasciati invariati.
    Le parole sono separate da uno spazio.
    """
    result = []
    for ch in text.upper():
        if ch in PHONETIC_MAP:
            result.append(PHONETIC_MAP[ch])
        else:
            result.append(ch)
    return ' '.join(result)
