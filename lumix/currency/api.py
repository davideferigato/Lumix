

# lumix/currency/api.py

import json
import urllib.request
from urllib.error import HTTPError, URLError


def fetch_exchange_rate(amount: float, src: str, dst: str) -> float:
    """
    Usa l'API di Francoforte per ottenere il valore convertito da una valuta all'altra.

    :param amount: quantità da convertire
    :param src: codice valuta sorgente (es. 'EUR')
    :param dst: codice valuta destinazione (es. 'USD')
    :return: valore convertito
    """
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={src}&to={dst}"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            if "rates" in data and dst in data["rates"]:
                return data["rates"][dst]
            else:
                raise ValueError(f"Nessun tasso trovato per {dst} nella risposta.")
    except (URLError, HTTPError) as e:
        raise ConnectionError(f"Errore durante la connessione all'API di Francoforte: {e}")
    except Exception as e:
        raise RuntimeError(f"Errore durante il parsing della risposta: {e}")
