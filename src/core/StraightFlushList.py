from Analysis import *

class StraightFlushList(list):
    """ This class takes 25 cards, counts number of wild cards
        then creates a list of tuples to replace wild cards.
        Then we find best PyramidPoker Hand with 25 cards """
    """ Also used in MyHand20_Analysis.  Looks at 20 cards and 
        see if there are any wilds. Remove wilds, then for each
        potential wild card, look for new straight flushes - only
        checks for one wild, assuming you would not use two wild
        cards to get one straight flush        
    """
    def __init__(self, card_list2):
        card_list = sorted([s + r for s in "SHDC" for r in "23456789TJQKA"], key=suit_rank_sort, reverse=True)
        # count number of wild cards and remove
        number_of_wild_cards = 0
        for cardx in card_list2[::-1]:
            if cardx[0:2] == "WW":
                card_list2.remove(cardx)  # remove all wild cards
                number_of_wild_cards += 1  # count number of wild cards

        self.straightflush_list = []
        for card in card_list:
            # print ("SFL", card, card_list2)
            check_straightflush = self.check_straightflush_card(card_list2, card)
            if check_straightflush == True:
                print ("myhand20_analysis for potential straight flushes, card=", card)
                self.straightflush_list.append(card)

    def check_straightflush_card(self, card_list2, wild_card2):
        """ Given card_list2, return True or False"""
        check_straightflush = False
        # print ("inside check_straightflush_card")
        card_list3 = list(card_list2)
        card_list3.append(wild_card2)
        hand2 = Analysis(card_list2)
        # print ("card_list2", card_list2)
        # print ("card_list3", card_list3)
        # suit_rank_array = analyze_wild(card_list2)
        before_total_straight_flushes = hand2.suit_rank_array[45] + hand2.suit_rank_array[46] + hand2.suit_rank_array[47] + \
                                        hand2.suit_rank_array[48] + hand2.suit_rank_array[49] + hand2.suit_rank_array[50]
        # print ("before", before_total_straight_flushes)
        # print ("hand2[25]", hand2.suit_rank_array[25])
        hand3 = Analysis(card_list3)
        # suit_rank_array = analyze_wild(card_list3)
        after_total_straight_flushes = hand3.suit_rank_array[45] + hand3.suit_rank_array[46] + hand3.suit_rank_array[47] + \
                                       hand3.suit_rank_array[48] + hand3.suit_rank_array[49] + hand3.suit_rank_array[50]
        # for i in range(45,51):
        #     print("hand3", hand3.suit_rank_array[i])
        # print("after", after_total_straight_flushes)
        if after_total_straight_flushes > before_total_straight_flushes:
            check_straightflush = True
        return(check_straightflush)