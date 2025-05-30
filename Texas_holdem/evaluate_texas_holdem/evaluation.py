def build_evaluation_prompt(expected_rule, inference):
    return f"""You are an expert poker evaluator. A model attempted to analyze the hand and output the following reasoning:

{inference}

The expected rule for this hand is: {expected_rule}

Decide whether the model correctly identified this rule. Reply only with '1' if correct, or '0' if incorrect."""


def evaluate_response(client, expected_rule, inference):
    prompt = build_evaluation_prompt(expected_rule, inference)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a precise and concise evaluator."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()