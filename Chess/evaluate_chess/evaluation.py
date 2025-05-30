import json

def build_rule_descriptions(expected_rules):
    special_descriptions = {
        "special1": "Move in a straight line any number of squares, then move vertically exactly 2 squares.",
        "special2": "First move diagonally any number of squares, then move 2 squares diagonally in a direction perpendicular to the first move.",
        "special3": "Move exactly 3 squares in one direction, then move down 1 square.",
        "special4": "Dynamic block-jump: In the same row or column, find the nearest blocking piece and jump to the symmetric position on the other side.",
        "special5": "Swap: Swap positions with another piece on the target square (target must be occupied and distance ≤ 3).",
        "special6": "Move in a straight line any number of squares, then move one square diagonally."
    }
    normal_descriptions = {
        "normal1": "Move one square in any direction (like a King’s move).",
        "normal2": "Move in an L-shaped pattern: two squares in one direction and one square perpendicular (like a Knight’s move).",
        "normal3": "Move any number of squares diagonally.",
        "normal4": "Move exactly 2 squares forward (in the direction of increasing row).",
        "normal5": "Move any number of squares straight (horizontally or vertically).",
        "normal6": "Move exactly 2 squares diagonally."
    }
    result = {}
    for piece, rule_id in expected_rules.items():
        if rule_id.startswith("special"):
            result[piece] = special_descriptions.get(rule_id, "No description available.")
        elif rule_id.startswith("normal"):
            result[piece] = normal_descriptions.get(rule_id, "No description available.")
        else:
            result[piece] = "Unknown rule."
    return result

def evaluate_inference(client, expected_rules, inference):
    detailed = build_rule_descriptions(expected_rules)
    detailed_text = json.dumps(detailed, indent=4)
    eval_prompt = f"""You are an expert in analyzing custom strategy games. The expected movement rules for Lunar Chess are given below:
{detailed_text}

Below is an analysis provided by another AI:
--------------------------------------------------
{inference}
--------------------------------------------------

For each piece, determine if the inferred rule matches the expected one. Return a JSON object with 1 (correct) or 0 (incorrect) for each piece.
Only output the JSON object and nothing else."""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert evaluator of game rules."},
            {"role": "user", "content": eval_prompt}
        ]
    )
    return response.choices[0].message.content