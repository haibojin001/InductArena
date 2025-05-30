def build_evaluation_prompt(expected_rule, inference):
    return f"""An AI was asked to identify which rule a Blackjack hand satisfies. Here's what it said:

{inference}

The correct rule for this hand is: {expected_rule}

Is the model's answer correct?

Return only:
'1' → correct
'0' → incorrect
"""


def evaluate_response(client, expected_rule, inference):
    prompt = build_evaluation_prompt(expected_rule, inference)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a precise Blackjack rule evaluator."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()