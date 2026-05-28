import datetime

_zoneinfo_available = True
try:
    from zoneinfo import ZoneInfo
except ImportError:
    try:
        import pytz

        _zoneinfo_available = False
    except ImportError:
        _zoneinfo_available = False
        ZoneInfo = None
        pytz = None

CITY_TIMEZONE = {
    "tokyo": "Asia/Tokyo",
    "rome": "Europe/Rome",
    "london": "Europe/London",
    "newyork": "America/New_York",
    "losangeles": "America/Los_Angeles",
}


def get_time_in_city(city: str) -> str:
    city_lower = city.lower().replace(" ", "").replace("-", "")
    if city_lower not in CITY_TIMEZONE:
        raise ValueError(f"Città '{city}' non trovata nel database")
    tz_name = CITY_TIMEZONE[city_lower]
    try:
        if not _zoneinfo_available:
            if pytz is None:
                raise RuntimeError("pytz not installed")
            tz = pytz.timezone(tz_name)
            now = datetime.datetime.now(tz)
        else:
            tz = ZoneInfo(tz_name)
            now = datetime.datetime.now(tz)
        return now.strftime("%Y-%m-%d %H:%M:%S %Z")
    except Exception as e:
        raise RuntimeError(f"Errore nel determinare l'ora per {tz_name}: {e}")


def what_time(city: str) -> str:
    try:
        time_str = get_time_in_city(city)
        return f"Current time in {city.capitalize()}: {time_str}"
    except ValueError as e:
        return str(e)
    except RuntimeError as e:
        return str(e)
