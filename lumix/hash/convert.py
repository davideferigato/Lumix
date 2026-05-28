import hashlib


def compute_hash(data: str, algorithm: str) -> str:
    """
    Calcola l'hash di una stringa usando l'algoritmo specificato.
    Supporta: md5, sha1, sha224, sha256, sha384, sha512.
    """
    data_bytes = data.encode('utf-8')
    if algorithm == 'md5':
        return hashlib.md5(data_bytes).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(data_bytes).hexdigest()
    elif algorithm == 'sha224':
        return hashlib.sha224(data_bytes).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(data_bytes).hexdigest()
    elif algorithm == 'sha384':
        return hashlib.sha384(data_bytes).hexdigest()
    elif algorithm == 'sha512':
        return hashlib.sha512(data_bytes).hexdigest()
    else:
        raise ValueError(f"Algoritmo non supportato: {algorithm}")
