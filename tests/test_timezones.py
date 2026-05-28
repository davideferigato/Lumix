from lumix.timezones.convert import convert_timezone


def test_convert_timezone():
    result = convert_timezone("2025-08-02 14:00", "Europe/Rome", "Asia/Tokyo")
    assert result == "2025-08-02 21:00"
