import random

SUITS = ['H', 'D', 'S', 'C']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
DECK = [r + s for r in RANKS for s in SUITS]
PRIME_TOTALS = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}

def draw_hand(n=5):
    deck = DECK.copy()
    random.shuffle(deck)
    return deck[:n]

def card_value(rank, ace_high=True):
    if rank in ['T', 'J', 'Q', 'K']:
        return 10
    if rank == 'A':
        return 11 if ace_high else 1
    return int(rank)

def get_best_total(cards):
    total = 0
    aces = 0
    for c in cards:
        r = c[0]
        if r == 'A':
            aces += 1
            total += 11
        else:
            total += card_value(r)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def is_straight(vals):
    vals = sorted(set(vals))
    for i in range(len(vals) - 2):
        if vals[i+2] - vals[i] == 2 and vals[i+1] - vals[i] == 1:
            return True
    return False