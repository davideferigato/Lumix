import json
import urllib.request

# Tassi di fallback statici (es. da fixare periodicamente)
STATIC_RATES = {
    ("EUR", "USD"): 1.18,
    ("USD", "EUR"): 0.85,
    ("EUR", "GBP"): 0.86,
    ("GBP", "EUR"): 1.16,
    ("USD", "GBP"): 0.78,
    ("GBP", "USD"): 1.28,
}


def fetch_exchange_rate(amount: float, src: str, dst: str) -> float:
    # Prova prima con l'API
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={src}&to={dst}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if "rates" in data and dst in data["rates"]:
                return data["rates"][dst]
            else:
                raise ValueError(f"Nessun tasso trovato per {dst} nella risposta.")
    except Exception:
        # Fallback: usa tassi statici
        key = (src, dst)
        if key in STATIC_RATES:
            return amount * STATIC_RATES[key]
        raise ConnectionError(
            f"Impossibile ottenere il tasso per {src} -> {dst} (fallback non disponibile)"
        )
