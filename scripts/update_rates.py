#!/usr/bin/env python3

"""
Script per aggiornare manualmente la cache dei tassi di cambio.
Esegue una richiesta API e salva i risultati nel file locale.
"""

from lumix.currency.api import fetch_exchange_rates
from lumix.currency.cache import save_rates


def main():
    try:
        rates = fetch_exchange_rates()
        save_rates(rates)
        print("Cache aggiornata con successo.")
    except Exception as e:
        print(f"Errore durante l'aggiornamento della cache: {e}")


if __name__ == "__main__":
    main()
