import os
import json
import random
import itertools
from poker_utils import deal_hand
import rules

NR_FUNCTIONS = {
    "NR1": rules.is_pair,
    "NR2": rules.is_three_of_a_kind,
    "NR3": rules.is_straight,
    "NR4": rules.is_flush,
    "NR5": rules.is_four_of_a_kind,
}
SR_FUNCTIONS = {
    "SR1": rules.is_prime_straight,
    "SR2": rules.is_red_black_alternating,
    "SR3": rules.is_mirror_hand,
    "SR4": rules.is_even_seq_flush,
    "SR5": rules.is_hybrid_hand,
}

def generate_game(rule_set_index, nr_ids, sr_ids):
    sample = []
    rule_funcs = {r: NR_FUNCTIONS[r] for r in nr_ids} | {r: SR_FUNCTIONS[r] for r in sr_ids}
    rule_counts = {r: 0 for r in rule_funcs}
    while any(c < 4 for c in rule_counts.values()):
        player, community = deal_hand()
        cards = player + community
        for rule_id, rule_fn in rule_funcs.items():
            if rule_counts[rule_id] >= 4:
                continue
            if rule_fn(cards):
                sample.append({
                    "player": player,
                    "community": community,
                    "rule": rule_id
                })
                rule_counts[rule_id] += 1
                break
    os.makedirs("texas_data", exist_ok=True)
    with open(f"texas_data/texas_game_{rule_set_index}.json", "w", encoding="utf-8") as f:
        json.dump(sample, f, indent=2)

def main():
    nr_combos = list(itertools.combinations(NR_FUNCTIONS.keys(), 2))
    sr_combos = list(itertools.combinations(SR_FUNCTIONS.keys(), 2))
    idx = 0
    for nr in nr_combos:
        for sr in sr_combos:
            idx += 1
            print(f"Generating game {idx}: NRs={nr}, SRs={sr}")
            generate_game(idx, nr, sr)

if __name__ == "__main__":
    main()