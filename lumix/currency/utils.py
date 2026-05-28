# lumix/currency/utils.py

from .cache import get_cached_rates

# Tassi statici di fallback
STATIC_RATES = {
    ("EUR", "USD"): 1.10,
    ("USD", "EUR"): 0.91,
    ("EUR", "GBP"): 0.86,
    ("GBP", "EUR"): 1.16,
    ("USD", "GBP"): 0.78,
    ("GBP", "USD"): 1.28,
}


def get_exchange_rate(src: str, dst: str) -> float:
    """
    Restituisce il tasso di cambio tra due valute. Prima prova da cache, poi fallback statico.

    :param src: codice valuta sorgente
    :param dst: codice valuta destinazione
    :return: tasso di cambio
    """
    try:
        rates = get_cached_rates()
        if dst in rates.get(src, {}):
            return rates[src][dst]
    except Exception:
        pass

    return STATIC_RATES.get((src, dst), 1.0)
