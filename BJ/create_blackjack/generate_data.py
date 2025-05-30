import os
import json
import itertools
from cards import draw_hand
from rules import NR_FUNCTIONS, SR_FUNCTIONS

def generate_episode(ep_id, nr_keys, sr_keys):
    rules = {k: NR_FUNCTIONS[k] for k in nr_keys} | {k: SR_FUNCTIONS[k] for k in sr_keys}
    rule_counts = {k: 0 for k in rules}
    samples = []

    while any(v < 3 for v in rule_counts.values()):
        hand = draw_hand()
        for rule_name, rule_fn in rules.items():
            if rule_counts[rule_name] >= 3:
                continue
            if rule_fn(hand):
                samples.append({"hand": hand, "rule": rule_name})
                rule_counts[rule_name] += 1
                break

    os.makedirs("blackjack_data", exist_ok=True)
    with open(f"blackjack_data/blackjack_episode_{ep_id}.json", "w", encoding="utf-8") as f:
        json.dump(samples, f, indent=2)

def main():
    nr_combos = list(itertools.combinations(NR_FUNCTIONS.keys(), 2))
    sr_combos = list(itertools.combinations(SR_FUNCTIONS.keys(), 2))
    ep_id = 0
    for nr in nr_combos:
        for sr in sr_combos:
            ep_id += 1
            print(f"Episode {ep_id}: NRs={nr}, SRs={sr}")
            generate_episode(ep_id, nr, sr)

if __name__ == "__main__":
    main()