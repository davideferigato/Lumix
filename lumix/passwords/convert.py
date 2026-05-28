import random
import string


def generate_password(length: int, use_symbols: bool = False) -> str:
    """
    Genera una password casuale con la lunghezza specificata.
    Di default usa lettere (maiuscole e minuscole) e numeri.
    Se use_symbols è True, include anche simboli di punteggiatura.
    """
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password
