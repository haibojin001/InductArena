import json

def build_prompt_text(player, community):
    player_str = " ".join(player)
    community_str = " ".join(community)

    prompt = f"""You are evaluating a hand in a custom version of Texas Hold'em called Lunar Poker.

In this game, the player receives two private cards, and there are five shared community cards on the table.
Your job is to determine if the hand satisfies any of the special or normal ranking rules.

Here is the hand:
- Player hand: {player_str}
- Community cards: {community_str}

Please complete the following steps:
1. Determine whether this hand satisfies any known rule (normal or special).
2. Identify which rule it satisfies and explain why.
3. If multiple rules match, choose the highest-priority one.
4. Output the rule name (e.g., NR3, SR1) and a short justification.

Output format:
Rule: <rule_name>
Explanation: <your reasoning>
""""

    return prompt