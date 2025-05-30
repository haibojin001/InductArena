def get_inference(client, prompt_text):
    response = client.chat.completions.create(
        model="o1",
        reasoning_effort="medium",
        messages=[
            {"role": "system", "content": "You are an expert at analyzing dice rules."},
            {"role": "user", "content": prompt_text}
        ]
    )
    return response.choices[0].message.content