from datetime import datetime

_zoneinfo_available = True
try:
    from zoneinfo import ZoneInfo, available_timezones
except ImportError:
    try:
        import pytz

        _zoneinfo_available = False

        def available_timezones():
            return []

    except ImportError:
        _zoneinfo_available = False
        ZoneInfo = None
        pytz = None

        def available_timezones():
            return []


def convert_timezone(
    dt_str: str, from_tz: str, to_tz: str, date_format: str = "%Y-%m-%d %H:%M"
) -> str:
    try:
        if not _zoneinfo_available:
            if pytz is None:
                raise ValueError("pytz not installed")
            from_pytz = pytz.timezone(from_tz)
            to_pytz = pytz.timezone(to_tz)
            dt_naive = datetime.strptime(dt_str, date_format)
            dt_from = from_pytz.localize(dt_naive)
            dt_to = dt_from.astimezone(to_pytz)
        else:
            if from_tz not in available_timezones():
                raise ValueError(f"Fuso orario non valido: {from_tz}")
            if to_tz not in available_timezones():
                raise ValueError(f"Fuso orario non valido: {to_tz}")
            dt_naive = datetime.strptime(dt_str, date_format)
            dt_from = dt_naive.replace(tzinfo=ZoneInfo(from_tz))
            dt_to = dt_from.astimezone(ZoneInfo(to_tz))
        return dt_to.strftime(date_format)
    except Exception as e:
        raise ValueError(f"Errore nella conversione: {e}")
