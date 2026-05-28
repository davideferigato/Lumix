from datetime import datetime


def date_diff(date1_str: str, date2_str: str, date_format: str = "%Y-%m-%d") -> dict:
    """
    Calcola la differenza tra due date.

    Args:
        date1_str: Prima data come stringa.
        date2_str: Seconda data come stringa.
        date_format: Formato delle date.

    Returns:
        Dizionario con differenza in giorni, settimane, mesi, anni.
    """
    d1 = datetime.strptime(date1_str, date_format).date()
    d2 = datetime.strptime(date2_str, date_format).date()

    # Ordina le date per avere sempre differenza positiva
    if d1 > d2:
        d1, d2 = d2, d1

    delta = d2 - d1
    days = delta.days

    # Calcolo approssimativo di settimane, mesi, anni
    weeks = days // 7
    months = (d2.year - d1.year) * 12 + (d2.month - d1.month)
    years = d2.year - d1.year

    # Aggiusta per il giorno del mese (se d2.day < d1.day, il mese non è completo)
    if d2.day < d1.day:
        months -= 1
        if months < 0:
            months = 11
            years -= 1

    # Calcolo giorni rimanenti dopo aver sottratto anni e mesi?
    # Per semplicità, restituiamo i valori principali.
    return {
        "days": days,
        "weeks": weeks,
        "months": months,
        "years": years,
    }
