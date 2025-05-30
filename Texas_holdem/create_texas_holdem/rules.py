from poker_utils import card_rank, card_suit, card_color, card_parity, PRIMES

def is_pair(cards):
    ranks = [card_rank(c) for c in cards]
    return any(ranks.count(r) == 2 for r in ranks)

def is_three_of_a_kind(cards):
    ranks = [card_rank(c) for c in cards]
    return any(ranks.count(r) == 3 for r in ranks)

def is_two_pair(cards):
    ranks = [card_rank(c) for c in cards]
    return len(set([r for r in ranks if ranks.count(r) == 2])) >= 2

def is_four_of_a_kind(cards):
    ranks = [card_rank(c) for c in cards]
    return any(ranks.count(r) == 4 for r in ranks)

def is_flush(cards):
    suits = [card_suit(c) for c in cards]
    return all(s == suits[0] for s in suits)

def is_straight(cards):
    rank_order = {r: i for i, r in enumerate('23456789TJQKA')}
    unique_ranks = sorted(set(card_rank(c) for c in cards), key=lambda r: rank_order[r])
    values = [rank_order[r] for r in unique_ranks]
    for i in range(len(values) - 4):
        if values[i+4] - values[i] == 4:
            return True
    return False

def is_prime_straight(cards):
    ranks = set(card_rank(c) for c in cards)
    return len(PRIMES.intersection(ranks)) >= 5

def is_red_black_alternating(cards):
    colors = [card_color(c) for c in cards]
    return all(colors[i] != colors[i+1] for i in range(len(colors)-1))

def is_even_seq_flush(cards):
    evens = {'2', '4', '6', '8', 'T', 'Q'}
    same_suit = all(card_suit(c) == card_suit(cards[0]) for c in cards)
    even_vals = all(card_rank(c) in evens for c in cards)
    return same_suit and even_vals

def is_mirror_hand(cards):
    parities = [card_parity(c) for c in cards]
    return all(parities[i] != parities[i+1] for i in range(len(parities)-1))

def is_hybrid_hand(cards):
    parities = [card_parity(c) for c in cards]
    count = {'O': parities.count('O'), 'E': parities.count('E')}
    return (count['O'] == 4 and count['E'] == 1) or (count['E'] == 4 and count['O'] == 1)