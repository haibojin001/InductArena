from utils import is_prime, parity

def NR1(dice):  # small total: 4~10
    return 4 <= sum(dice) <= 10

def NR2(dice):  # large total: 11~17
    return 11 <= sum(dice) <= 17

def NR3(dice):  # any pair
    return len(set(dice)) == 2

def NR4(dice):  # triple
    return len(set(dice)) == 1

def SR1(dice):  # sum is prime
    return is_prime(sum(dice))

def SR2(dice):  # all dice are primes
    return all(x in {2, 3, 5} for x in dice)

def SR3(dice):  # parity alternating
    p = [parity(x) for x in dice]
    return (p == ['O', 'E', 'O']) or (p == ['E', 'O', 'E'])

def SR4(dice):  # pair + third differs by 1
    dice = sorted(dice)
    if dice[0] == dice[1] and abs(dice[2] - dice[0]) == 1:
        return True
    if dice[1] == dice[2] and abs(dice[0] - dice[1]) == 1:
        return True
    return False

NR_FUNCTIONS = {"NR1": NR1, "NR2": NR2, "NR3": NR3, "NR4": NR4}
SR_FUNCTIONS = {"SR1": SR1, "SR2": SR2, "SR3": SR3, "SR4": SR4}