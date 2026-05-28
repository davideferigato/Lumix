from datetime import date, datetime


def calculate_age(birth_date_str: str, date_format: str = "%Y-%m-%d") -> int:
    """
    Calcola l'età in anni compiuti.

    Args:
        birth_date_str: Data di nascita come stringa.
        date_format: Formato della data (default ISO).

    Returns:
        int: Età in anni.
    """
    birth_date = datetime.strptime(birth_date_str, date_format).date()
    today = date.today()
    age = today.year - birth_date.year
    # Se non ha ancora compiuto gli anni quest'anno
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age
