# lumix/currency/convert.py

from .api import fetch_exchange_rate


def convert_currency(amount: float, src: str, dst: str) -> float:
    """
    Converte una quantità da una valuta all'altra usando il tasso di cambio corrente.

    :param amount: quantità da convertire
    :param src: codice valuta sorgente (es. 'EUR')
    :param dst: codice valuta destinazione (es. 'USD')
    :return: valore convertito
    """
    if src == dst:
        return round(amount, 4)
    rate = fetch_exchange_rate(amount, src, dst)
    return round(rate, 4)
