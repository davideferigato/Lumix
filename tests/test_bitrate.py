from lumix.bitrate.convert import convert


def test_convert():
    assert convert(100, "mbps", "kbps") == 100_000
    assert convert(1, "gbps", "mbps") == 1000
