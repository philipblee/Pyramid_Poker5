""" Deck2 is simple class to deal out six_hands of 25 cards each
    deck is a list of all cards - 3 decks and 3 wild cards 159 cards
    returns a six_hands which is a list of 6 hands -
    each hand is a list of 25 cards
"""

from random import shuffle

class Deck2:
    def __init__(self):
        pass

    @staticmethod
    def deal(num_hands=6, num_cards=25):
        six_hands = [[],[],[],[],[],[]]
        suit = 'SHDC'
        rank = 'AKQJT98765432'
        deck_number = '+-*'
        deck = [s + r + d for s in suit for r in rank for d in deck_number]
        deck.extend(["WW+", "WW-", "WW*"]) # add three wild cards
        for i in range(10):
            shuffle(deck)
        for i in range(num_hands):
            pyramid_poker_list = deck[i::num_hands]
            six_hands[i] = pyramid_poker_list[:num_cards]
        return (six_hands)

# pyramid_poker_list = Deck2.deal()
# print (pyramid_poker_list)
