import json

def filter_empty_rounds(game_record):
    filtered = [
        move for move in game_record.get("moves", [])
        if not (move.get("red_move", "") == "no move" and
                move.get("black_move", "") == "no move" and
                move.get("event", "") == "/")
    ]
    game_record["moves"] = filtered
    return game_record

def generate_prompt(record_path):
    with open(record_path, "r", encoding="utf-8") as f:
        game_record = json.load(f)

    game_record = filter_empty_rounds(game_record)
    rows = game_record["board_size"]["rows"]
    cols = game_record["board_size"]["cols"]
    board_size = f"{rows} x {cols}"
    placements_str = "\n".join(game_record["initial_setup"])

    moves_lines = []
    for move in game_record["moves"]:
        line = f"Round {move['round']}: Red move: {move['red_move']}, Black move: {move['black_move']} (Event: {move['event']})"
        moves_lines.append(line)
    moves_text = "\n".join(moves_lines)

    prompt_text = f"""I’m playing a custom strategy game called Lunar Chess.
The board size is {board_size}, labeled from bottom to top and left to right.

The pieces for each side are arranged symmetrically:
- Red side at the bottom
- Black side at the top

Below is the initial piece placement (listed from left to right for each side):
{placements_str}

Each piece has unique movement rules, and the game alternates turns between Red and Black.

Since you’re a beginner, I will now show you a full example game. Please observe how each piece moves during the game.
After watching the entire game, try to infer the movement rules of each piece and explain your reasoning.

Here is an example game (move by move):

{moves_text}

Your task is:
1) Learn from the moves in this example game.
2) Summarize how each piece moves.
3) Provide your best guess for the movement rules and justify them based on what you observed."""".strip()

    return prompt_text, game_record["piece_rules"]