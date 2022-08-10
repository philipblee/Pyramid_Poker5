from random import shuffle, seed, randint
import src.core.global_variables as global_variables

# global_variables.random_seed = 8728
seed(global_variables.random_seed)

suit = 'SHDC'
rank = 'AKQJT98765432'
deck_number = '+-*'
deck = [s + r + d for s in suit for r in rank for d in deck_number]

# print (deck)

class Deal:
    def __init__(self):
        suit = 'SHDC'
        rank = 'AKQJT98765432'
        deck_number = '+-*'
        self.deck = [s + r for s in suit for r in rank]
        # print (self.deck)
        pass

    @staticmethod
    def deal(n=6):
        for i in range(10):
            shuffle(deck)
        poker_hand = [HandDeck(deck[i::n]) for i in range(n)]
        print (poker_hand[0])
        return [poker_hand[0][0:5]]

class HandDeck(list):
    pass
