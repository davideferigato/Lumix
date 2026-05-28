from lumix.color.convert import hex_to_rgb, rgb_to_hex


def test_rgb_to_hex():
    assert rgb_to_hex(255, 255, 255) == "#ffffff"
    assert rgb_to_hex(0, 0, 0) == "#000000"

def test_hex_to_rgb():
    assert hex_to_rgb("#ff0000") == (255, 0, 0)
    assert hex_to_rgb("00ff00") == (0, 255, 0)

