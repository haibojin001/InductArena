import os
import random
import json
from board import draw_board
from prompt import generate_prompt_text, save_prompt_text
from pieces import UNICODE_PIECES, SYMBOL_TO_TYPE, ALL_TYPES, RED_PIECES, BLACK_PIECES, in_bounds

def coord_to_notation(x, y):
    return f"{chr(ord('a') + x)}{y}"

def init_board(rows, cols):
    board = [[None for _ in range(cols)] for _ in range(rows)]
    color_map = [[None for _ in range(cols)] for _ in range(rows)]
    placements = []
    use_col = min(cols, 7)
    for i in range(use_col):
        r = RED_PIECES[i]
        b = BLACK_PIECES[i]
        board[0][i] = UNICODE_PIECES[r]
        color_map[0][i] = 'red'
        placements.append(f"{coord_to_notation(i, 0)} {r}")
        board[rows - 1][i] = UNICODE_PIECES[b]
        color_map[rows - 1][i] = 'black'
        placements.append(f"{coord_to_notation(i, rows - 1)} {b}")
    return board, color_map, placements

def get_piece_type(board, x, y):
    return SYMBOL_TO_TYPE.get(board[y][x]) if board[y][x] else None

def get_all_valid_moves(board, color_map, side):
    rows, cols = len(board), len(board[0])
    moves = []
    for y in range(rows):
        for x in range(cols):
            if color_map[y][x] == side:
                for ey in range(rows):
                    for ex in range(cols):
                        if (x, y) != (ex, ey) and is_valid_move(board, color_map, (x, y), (ex, ey)):
                            moves.append(((x, y), (ex, ey)))
    return moves

def base_is_valid_move(board, start, end, piece_type):
    sx, sy = start
    ex, ey = end
    dx, dy = ex - sx, ey - sy
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0

    if piece_type == "plane":
        if (abs(dx) >= 1 and abs(dy) == 2) or (abs(dy) >= 1 and abs(dx) == 2):
            return True

    elif piece_type == "mushroom":
        if dx == 0 and dy != 0:
            direction = 1 if dy > 0 else -1
            steps = abs(dy)
            for dist in range(1, steps):
                mid_y = sy + direction * dist
                if board[mid_y][sx] is not None:
                    landing_y = mid_y + direction
                    if landing_y == ey:
                        return True

    elif piece_type == "shield":
        line_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        diag_dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx_line, dy_line in line_dirs:
            x1, y1 = sx + dx_line, sy + dy_line
            if not in_bounds(x1, y1, cols, rows) or board[y1][x1] is not None:
                continue
            x2, y2 = x1 + dx_line, y1 + dy_line
            if not in_bounds(x2, y2, cols, rows) or board[y2][x2] is not None:
                continue
            for dx_d1, dy_d1 in diag_dirs:
                x3, y3 = x2 + dx_d1, y2 + dy_d1
                if not in_bounds(x3, y3, cols, rows) or board[y3][x3] is not None:
                    continue
                for dx_d2, dy_d2 in diag_dirs:
                    x4, y4 = x3 + dx_d2, y3 + dy_d2
                    if not in_bounds(x4, y4, cols, rows):
                        continue
                    if board[y4][x4] is not None:
                        continue
                    if (x4, y4) == (ex, ey):
                        return True

    elif piece_type == "crown":
        if abs(dx) <= 1 and abs(dy) <= 1:
            return True

    elif piece_type == "wall":
        if abs(dx) == abs(dy):
            return True

    return False

def is_valid_move(board, color_map, start, end):
    rows, cols = len(board), len(board[0])
    sx, sy = start
    ex, ey = end
    if not in_bounds(sx, sy, cols, rows) or not in_bounds(ex, ey, cols, rows):
        return False
    if (sx, sy) == (ex, ey):
        return False
    if board[sy][sx] is None:
        return False
    if color_map[ey][ex] == color_map[sy][sx]:
        return False
    piece_type = get_piece_type(board, sx, sy)
    return base_is_valid_move(board, start, end, piece_type)

def get_piece_type_on_board(board):
    rows, cols = len(board), len(board[0])
    found = set()
    for y in range(rows):
        for x in range(cols):
            if board[y][x]:
                found.add(SYMBOL_TO_TYPE[board[y][x]])
    return found

def run_single_game(game_index, rows, cols, desired_rounds=25, max_rounds=60):
    board, color_map, placements = init_board(rows, cols)
    game_dir = f"./game_{game_index}"
    os.makedirs(game_dir, exist_ok=True)
    images_dir = os.path.join(game_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    record = []
    move_count = 0
    round_num = 1
    move_counter = {t: 0 for t in ALL_TYPES}
    move_count += 1
    draw_board(board, color_map, move_count, images_dir)

    while True:
        events = []

        red_moves = get_all_valid_moves(board, color_map, 'red')
        if red_moves:
            (sx, sy), (ex, ey) = random.choice(red_moves)
            red_move_str = f"{coord_to_notation(sx, sy)} {coord_to_notation(ex, ey)}"
            if board[ey][ex] and color_map[ey][ex] == 'black':
                captured = get_piece_type(board, ex, ey)
                events.append(f"{captured} in {coord_to_notation(ex, ey)} was removed")
            moved = get_piece_type(board, sx, sy)
            board[ey][ex], board[sy][sx] = board[sy][sx], None
            color_map[ey][ex], color_map[sy][sx] = 'red', None
            move_counter[moved] += 1
        else:
            red_move_str = "/"
        move_count += 1
        draw_board(board, color_map, move_count, images_dir)

        black_moves = get_all_valid_moves(board, color_map, 'black')
        if black_moves:
            (sx, sy), (ex, ey) = random.choice(black_moves)
            black_move_str = f"{coord_to_notation(sx, sy)} {coord_to_notation(ex, ey)}"
            if board[ey][ex] and color_map[ey][ex] == 'red':
                captured = get_piece_type(board, ex, ey)
                events.append(f"{captured} in {coord_to_notation(ex, ey)} was removed")
            moved = get_piece_type(board, sx, sy)
            board[ey][ex], board[sy][sx] = board[sy][sx], None
            color_map[ey][ex], color_map[sy][sx] = 'black', None
            move_counter[moved] += 1
        else:
            black_move_str = "/"
        move_count += 1
        draw_board(board, color_map, move_count, images_dir)

        record.append({
            "round": round_num,
            "red_move": red_move_str,
            "black_move": black_move_str,
            "event": ", ".join(events) if events else "/"
        })
        round_num += 1

        if round_num - 1 >= max_rounds:
            break
        if round_num - 1 >= desired_rounds:
            on_board = get_piece_type_on_board(board)
            if all(move_counter[t] >= 3 for t in on_board):
                break

    with open(os.path.join(game_dir, "move_record.json"), "w", encoding="utf-8") as f:
        json.dump({
            "board_size": {"rows": rows, "cols": cols},
            "initial_setup": placements,
            "moves": record
        }, f, indent=4, ensure_ascii=False)

    prompt_text = generate_prompt_text(rows, cols, placements, record)
    save_prompt_text(prompt_text, os.path.join(game_dir, "prompt_generation.json"))