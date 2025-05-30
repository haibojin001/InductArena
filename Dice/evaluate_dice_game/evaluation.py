def build_evaluation_prompt(expected_rule, inference):
    return f"""You are evaluating the following AI response about a dice roll:

{inference}

The expected rule for this roll is: {expected_rule}

Does the AI correctly identify the rule?

Respond only with '1' if the rule is correct, or '0' if it is incorrect."""


def evaluate_response(client, expected_rule, inference):
    prompt = build_evaluation_prompt(expected_rule, inference)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an objective evaluator of dice rules."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()