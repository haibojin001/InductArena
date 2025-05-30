UNICODE_PIECES = {
    "plane": "✈",
    "mushroom": "♣",
    "shield": "⬒",
    "crown": "♔",
    "wall": "▩",
}
SYMBOL_TO_TYPE = {v: k for k, v in UNICODE_PIECES.items()}
ALL_TYPES = {"plane", "mushroom", "shield", "crown", "wall"}
RED_PIECES = ["plane", "mushroom", "shield", "crown", "shield", "mushroom", "plane"]
BLACK_PIECES = ["plane", "mushroom", "shield", "crown", "shield", "mushroom", "plane"]

def in_bounds(x, y, cols, rows):
    return 0 <= x < cols and 0 <= y < rows