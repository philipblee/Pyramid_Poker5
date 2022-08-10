from src.core.Deck import *
from src.core.WildList import *

for k in range(100):
    print ("\nHand#", k+1)
    card_list = Deck.deal()[0]
    card_list2 = list(card_list[0:25])  # deal number_of_cards
    card_list2 = sorted(card_list2, key=rank_sort, reverse=True)
    print (card_list2)
    wild_list = WildList(card_list2)
    print ('number of wild cards: {}, number of wild card combinations to try: {} '.format(wild_list.number_of_wild_cards, wild_list.number_wild_card_combinations))
    print ('wild card combinations: {}'.format(wild_list.wild_card_combinations))
