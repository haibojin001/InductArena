from cards import card_value, get_best_total, is_straight, PRIME_TOTALS

def NR1(hand):
    return get_best_total(hand) == 21

def NR2(hand):
    return get_best_total(hand) > 21

def NR3(hand):
    return get_best_total(hand) < 21

def NR4(hand):
    total = get_best_total(hand)
    return total <= 21

def SR1(hand):
    return sum([card_value(c[0]) for c in hand]) in PRIME_TOTALS

def SR2(hand):
    if len(hand) < 3:
        return False
    suits = [c[1] for c in hand]
    vals = [int(card_value(c[0], ace_high=False)) for c in hand]
    for i in range(len(hand)-2):
        sub = hand[i:i+3]
        s = [c[1] for c in sub]
        v = [int(card_value(c[0], ace_high=False)) for c in sub]
        if len(set(s)) == 1 and sorted(v[1] - v[0] == 1 and v[2] - v[1] == 1):
            return True
    return False

def SR3(hand):
    ranks = [c[0] for c in hand]
    suits = [c[1] for c in hand]
    for i in range(len(hand)):
        for j in range(i+1, len(hand)):
            if ranks[i] == ranks[j] and suits[i] != suits[j]:
                return True
    return False

def SR4(hand):
    vals = sorted([card_value(c[0]) for c in hand])
    for i in range(len(vals) - 2):
        a, b, c = vals[i:i+3]
        if b * 2 == a + c and abs(a - b) > 1 and abs(b - c) > 1:
            return True
    return False

NR_FUNCTIONS = {"NR1": NR1, "NR2": NR2, "NR3": NR3, "NR4": NR4}
SR_FUNCTIONS = {"SR1": SR1, "SR2": SR2, "SR3": SR3, "SR4": SR4}