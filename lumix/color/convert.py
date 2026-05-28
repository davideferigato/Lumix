def rgb_to_hex(r: int, g: int, b: int) -> str:
    """Converte valori RGB (0-255) in stringa esadecimale (#RRGGBB)."""
    if not all(0 <= x <= 255 for x in (r, g, b)):
        raise ValueError("RGB values must be between 0 and 255")
    return f"#{r:02x}{g:02x}{b:02x}"

def hex_to_rgb(hex_str: str) -> tuple:
    """Converte stringa esadecimale (#RRGGBB o RRGGBB) in tuple (r,g,b)."""
    h = hex_str.lstrip('#').lower()
    if len(h) != 6 or not all(c in '0123456789abcdef' for c in h):
        raise ValueError("Invalid hex color format")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
