from lumix.timezonebot.convert import what_time


def test_what_time():
    result = what_time("Tokyo")
    assert "Tokyo" in result or "Current time" in result

