def build_prompt_text(dice):
    dice_str = " ".join(str(d) for d in dice)
    return f"""You are analyzing a dice roll in a custom game called Lunar Dice.

Three six-sided dice are rolled. Your task is to determine whether the roll satisfies any special or normal rule defined by the game.

Here is the roll:
Dice: {dice_str}

Instructions:
1. Identify if the roll matches any known rule.
2. If so, name the rule (e.g., NR1, SR2) and justify your choice.
3. If multiple rules apply, choose the highest-priority one.

Format:
Rule: <rule_name>
Explanation: <reasoning>
""""