import random

def roll_dice():
    return sorted([random.randint(1, 6) for _ in range(3)])

def is_prime(n):
    return n in {2, 3, 5, 7, 11, 13, 17}

def parity(n):
    return 'E' if n % 2 == 0 else 'O'