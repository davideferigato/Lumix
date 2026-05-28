from datetime import datetime

# Tentativo di importare zoneinfo (Python 3.9+) o pytz come fallback
try:
    from zoneinfo import ZoneInfo, available_timezones

    USE_ZONEINFO = True
except ImportError:
    import pytz

    USE_ZONEINFO = False


def convert_timezone(
    dt_str: str, from_tz: str, to_tz: str, date_format: str = "%Y-%m-%d %H:%M"
) -> str:
    """
    Converte una data/ora da un fuso orario a un altro.

    Args:
        dt_str: stringa della data/ora
        from_tz: fuso orario di partenza (es. 'Europe/Rome')
        to_tz: fuso orario di arrivo (es. 'Asia/Tokyo')
        date_format: formato della data/ora in dt_str

    Returns:
        stringa con data/ora convertita nello stesso formato
    """
    try:
        if USE_ZONEINFO:
            # Verifica che i fusi siano validi
            if from_tz not in available_timezones():
                raise ValueError(f"Fuso orario non valido: {from_tz}")
            if to_tz not in available_timezones():
                raise ValueError(f"Fuso orario non valido: {to_tz}")
            # Parsing della data/ora naive (senza fuso)
            dt_naive = datetime.strptime(dt_str, date_format)
            # Assegna il fuso di partenza
            dt_from = dt_naive.replace(tzinfo=ZoneInfo(from_tz))
            # Converti al fuso di destinazione
            dt_to = dt_from.astimezone(ZoneInfo(to_tz))
        else:
            # Fallback con pytz
            from_pytz = pytz.timezone(from_tz)
            to_pytz = pytz.timezone(to_tz)
            dt_naive = datetime.strptime(dt_str, date_format)
            dt_from = from_pytz.localize(dt_naive)
            dt_to = dt_from.astimezone(to_pytz)

        # Restituisce nel formato originale
        return dt_to.strftime(date_format)
    except Exception as e:
        raise ValueError(f"Errore nella conversione: {e}")
