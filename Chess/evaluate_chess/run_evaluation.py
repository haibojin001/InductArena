import os
import json
from api_client import get_openai_client
from prompt_utils import generate_prompt
from inference import get_inference
from evaluation import evaluate_inference

def main():
    client = get_openai_client()
    input_dir = "./data/chess/game_records"
    output_dir = "./results"
    os.makedirs(output_dir, exist_ok=True)
    for name in os.listdir(input_dir):
        if not name.startswith("game_"):
            continue
        record_path = os.path.join(input_dir, name, "game_record.json")
        prompt_text, expected_rules = generate_prompt(record_path)
        inference = get_inference(client, prompt_text)
        with open(os.path.join(output_dir, f"inference_{name}.txt"), "w", encoding="utf-8") as f:
            f.write(inference)
        result = evaluate_inference(client, expected_rules, inference)
        with open(os.path.join(output_dir, f"evaluation_{name}.json"), "w", encoding="utf-8") as f:
            f.write(result)

if __name__ == "__main__":
    main()