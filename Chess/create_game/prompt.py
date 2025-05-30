import os
import json

def generate_prompt_text(rows, cols, initial_placements, record_list):
    board_size_desc = f"{rows} rows by {cols} columns"
    placements_str = ", ".join(initial_placements)
    moves_text_lines = []
    for m in record_list:
        line = f"Round {m['round']}: Red -> {m['red_move']}, Black -> {m['black_move']}, Event: {m['event']}"
        moves_text_lines.append(line)
    moves_text = "\n".join(moves_text_lines)
    return f"""I’m playing a custom strategy game.
The board size is {board_size_desc}, labeled from bottom to top and left to right.
The pieces for each side are arranged symmetrically:
- Red side at the bottom
- Black side at the top
Below is the initial piece placement (left to right for each side), which includes walls:
{placements_str}
Each piece has unique movement rules, and the game alternates turns between Red and Black.
Since you’re a beginner, I will now show you a full example game. Please observe how each piece moves during the game. After watching the entire game, try to infer the movement rules of each piece and explain your reasoning.
Here is an example game (move by move):
{moves_text}
Your task is:
1) Learn from the moves in this example game.
2) Summarize how each piece moves.
3) Provide your best guess for the movement rules and justify them based on what you observed."""".strip()

def save_prompt_text(prompt_text, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"prompt": prompt_text}, f, ensure_ascii=False, indent=4)