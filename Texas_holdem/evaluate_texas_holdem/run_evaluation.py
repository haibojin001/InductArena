import os
import json
from api_client import get_openai_client
from prompt_utils import build_prompt_text
from inference import get_inference
from evaluation import evaluate_response

def main():
    client = get_openai_client()
    input_dir = "./texas_data"
    output_dir = "./texas_results"
    os.makedirs(output_dir, exist_ok=True)

    for fname in os.listdir(input_dir):
        if not fname.endswith(".json"):
            continue
        with open(os.path.join(input_dir, fname), "r", encoding="utf-8") as f:
            data = json.load(f)

        results = []
        for i, hand in enumerate(data):
            prompt = build_prompt_text(hand["player"], hand["community"])
            inference = get_inference(client, prompt)
            evaluation = evaluate_response(client, hand["rule"], inference)
            results.append({
                "index": i,
                "player": hand["player"],
                "community": hand["community"],
                "expected_rule": hand["rule"],
                "inference": inference,
                "evaluation": evaluation
            })

        with open(os.path.join(output_dir, f"eval_{fname}"), "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()