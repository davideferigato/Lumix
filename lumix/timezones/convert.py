import sys
from datetime import datetime

try:
    from zoneinfo import ZoneInfo, available_timezones

    USE_ZONEINFO = True
except ImportError:
    try:
        import pytz

        USE_ZONEINFO = False
        # Definisci available_timezones fittizio per compatibilità
        if not hasattr(sys.modules[__name__], "available_timezones"):

            def available_timezones():
                return []

    except ImportError:
        print("Error: pytz not installed. Run: pip install pytz")
        sys.exit(1)


def convert_timezone(
    dt_str: str, from_tz: str, to_tz: str, date_format: str = "%Y-%m-%d %H:%M"
) -> str:
    try:
        if USE_ZONEINFO:
            # Verifica che i fusi siano validi
            if from_tz not in available_timezones():
                raise ValueError(f"Fuso orario non valido: {from_tz}")
            if to_tz not in available_timezones():
                raise ValueError(f"Fuso orario non valido: {to_tz}")
            dt_naive = datetime.strptime(dt_str, date_format)
            dt_from = dt_naive.replace(tzinfo=ZoneInfo(from_tz))
            dt_to = dt_from.astimezone(ZoneInfo(to_tz))
        else:
            from_pytz = pytz.timezone(from_tz)
            to_pytz = pytz.timezone(to_tz)
            dt_naive = datetime.strptime(dt_str, date_format)
            dt_from = from_pytz.localize(dt_naive)
            dt_to = dt_from.astimezone(to_pytz)
        return dt_to.strftime(date_format)
    except Exception as e:
        raise ValueError(f"Errore nella conversione: {e}")
