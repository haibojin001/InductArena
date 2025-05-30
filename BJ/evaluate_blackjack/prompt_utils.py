def build_prompt_text(hand):
    hand_str = " ".join(hand)
    return f"""You are analyzing a hand in a custom Blackjack variant called Lunar Blackjack.

Each hand contains five cards. Aces can be valued as 1 or 11. Special rules may override normal win/loss conditions.

Here is the hand:
Cards: {hand_str}

Instructions:
1. Determine if this hand satisfies any known rule (normal or special).
2. If so, identify the rule (e.g., NR2, SR3) and explain why.
3. If multiple rules apply, select the most decisive/high-priority one.

Format:
Rule: <rule_name>
Explanation: <reasoning>
"""