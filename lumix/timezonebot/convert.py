import datetime

try:
    from zoneinfo import ZoneInfo

    USE_ZONEINFO = True
except ImportError:
    import pytz

    USE_ZONEINFO = False

CITY_TIMEZONE = {
    "tokyo": "Asia/Tokyo",
    "roma": "Europe/Rome",
    "rome": "Europe/Rome",
    "london": "Europe/London",
    "newyork": "America/New_York",
    "losangeles": "America/Los_Angeles",
    "chicago": "America/Chicago",
    "paris": "Europe/Paris",
    "berlin": "Europe/Berlin",
    "moscow": "Europe/Moscow",
    "beijing": "Asia/Shanghai",
    "hongkong": "Asia/Hong_Kong",
    "singapore": "Asia/Singapore",
    "sydney": "Australia/Sydney",
    "auckland": "Pacific/Auckland",
    "dubai": "Asia/Dubai",
    "mumbai": "Asia/Kolkata",
    "cairo": "Africa/Cairo",
    "rio": "America/Sao_Paulo",
    "toronto": "America/Toronto",
    "vancouver": "America/Vancouver",
    "sanfrancisco": "America/Los_Angeles",
}


def get_time_in_city(city: str) -> str:
    city_lower = city.lower().replace(" ", "").replace("-", "")
    if city_lower not in CITY_TIMEZONE:
        raise ValueError(f"Città '{city}' non trovata nel database")
    tz_name = CITY_TIMEZONE[city_lower]
    try:
        if USE_ZONEINFO:
            tz = ZoneInfo(tz_name)
            now = datetime.datetime.now(tz)
        else:
            tz = pytz.timezone(tz_name)
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
