import random
from itertools import combinations

SUITS = ['H', 'D', 'S', 'C']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
DECK = [r + s for r in RANKS for s in SUITS]

PRIMES = {'2', '3', '5', '7', 'J'}
REDS = {'H', 'D'}
BLACKS = {'S', 'C'}
ODDS = {'1', '3', '5', '7', '9', 'J', 'K', 'A'}
EVENS = {'2', '4', '6', '8', 'T', 'Q'}

def get_deck():
    return DECK.copy()

def deal_hand():
    deck = get_deck()
    random.shuffle(deck)
    player = deck[:2]
    community = deck[2:7]
    return player, community

def card_color(card):
    return 'R' if card[1] in REDS else 'B'

def card_parity(card):
    rank = card[0]
    return 'O' if rank in ODDS else 'E'

def card_suit(card):
    return card[1]

def card_rank(card):
    return card[0]