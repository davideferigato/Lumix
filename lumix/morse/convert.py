"""
Funzioni di conversione tra testo e codice Morse.
Utilizza il codice Morse internazionale.
"""

# Mappa carattere -> codice Morse
CHAR_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Mappa inversa codice Morse -> carattere
MORSE_TO_CHAR = {v: k for k, v in CHAR_TO_MORSE.items()}

def text_to_morse(text: str) -> str:
    """
    Converte una stringa di testo in codice Morse.
    Le lettere sono separate da uno spazio, le parole da "/".
    """
    text = text.upper()
    words = text.split()
    morse_words = []
    for word in words:
        morse_chars = [CHAR_TO_MORSE.get(c, '?') for c in word]
        morse_words.append(' '.join(morse_chars))
    return ' / '.join(morse_words)

def morse_to_text(morse: str) -> str:
    """
    Converte una stringa in codice Morse in testo.
    Gestisce spazi tra lettere e '/' tra parole.
    """
    words = morse.split(' / ')
    result_words = []
    for word in words:
        chars = word.split()
        result_chars = [MORSE_TO_CHAR.get(c, '?') for c in chars]
        result_words.append(''.join(result_chars))
    return ' '.join(result_words)
