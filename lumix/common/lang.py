import gettext


def get_translator(domain: str, lang: str, localedir: str):
    """
    Restituisce il traduttore gettext per un modulo specifico.

    :param domain: Nome del dominio (es. 'messages')
    :param lang: Codice lingua (es. 'en', 'it', ecc.)
    :param localedir: Directory contenente le cartelle delle lingue
    :return: Funzione di traduzione _
    """
    try:
        translator = gettext.translation(domain, localedir=localedir, languages=[lang])
        return translator.gettext
    except FileNotFoundError:
        return lambda x: x  # fallback: nessuna traduzione


def setup_gettext(domain: str, lang: str, localedir: str):
    """
    Installa il traduttore gettext globalmente come funzione _().
    """
    try:
        translator = gettext.translation(domain, localedir=localedir, languages=[lang])
        translator.install()  # installa _() nel built-in
    except FileNotFoundError:
        gettext.install(domain)  # fallback: passthrough _
