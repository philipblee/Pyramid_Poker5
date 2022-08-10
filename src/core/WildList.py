""" This class takes 25 cards, counts number of wild cards
    then creates the complete wild_list.  Then using method
    check_wild_card(), determine check_wild_list
    Using check_wild_list create check_wild_combintions
    These candidate combinations of wilds need to be evaluated
"""

from itertools import combinations_with_replacement
from src.core.Analysis import *

class WildList(list):
    """ This class takes 25 cards, counts number of wild cards
        then creates a list of candidate tuples for evaluating hands.
    """
    def __init__(self, cardlist25):
        all_cards = sorted([s + r + d for s in "SHDC" for r in "23456789TJQKA" for d in "+"], key=suit_rank_sort, reverse=True)
        # count number of wild cards and remove
        number_of_wild_cards = 0
        for cardx in cardlist25[::-1]:
            if cardx[0:2] == "WW":
                cardlist25.remove(cardx)  # remove all wild cards
                number_of_wild_cards += 1  # count number of wild cards
        if number_of_wild_cards >= 1:
            check_wild_list = []
            for wild_card in all_cards:
                check_wild = self.check_wild_card(cardlist25, wild_card)
                if check_wild == True:
                    check_wild_list.append(wild_card)
            check_wild_combinations = list(combinations_with_replacement(check_wild_list, number_of_wild_cards))
            self.wild_list = check_wild_list
            self.wild_card_combinations = check_wild_combinations
            self.number_of_wild_cards = number_of_wild_cards
            self.number_wild_card_combinations = len(check_wild_combinations)
        else:
            self.wild_list = []
            self.wild_card_combinations = []
            self.number_of_wild_cards = number_of_wild_cards
            self.number_wild_card_combinations = 0




    def check_wild_card(self, card_list2, wild_card2):
        """
        parameter 1: card_list2 is list of 25 cards less wild cards
        parameter 2: wild_card2 is potential candidate to substitute for wild card

        Given card_list2, this method checks to see if wild_card2 can improve
        1. (x of a kind) is spade and increases 3K, 4K, etc to 10K or
        2. (x card straight flush)increase quantity of straight_flushes of
            length 5, 6, 7, 8, 9 or 10

        methodology is to compare analysis between cardlist2 and cardlist3
        (which is cardlist2 plus wild_card2)
        """

        check_wild = False
        card_list3 = list(card_list2)
        card_list3.append(wild_card2)

        analysis2 = Analysis(card_list2)
        analysis3 = Analysis(card_list3)
        suit_rank_array = analysis2.suit_rank_array

        before_trips = len(suit_rank_array[13])
        before_fourks = len(suit_rank_array[14])
        before_fiveks = len(suit_rank_array[15])
        before_sixks = len(suit_rank_array[16])
        before_sevenks = len(suit_rank_array[17])
        before_eightks = len(suit_rank_array[18])
        before_nineks = len(suit_rank_array[19])
        before_tenks = len(suit_rank_array[20])

        before_total_straight_flushes = suit_rank_array[25] + suit_rank_array[26] + suit_rank_array[27] + \
                                        suit_rank_array[28] + suit_rank_array[29] + suit_rank_array[30]
        before_SF5 = len(suit_rank_array[25])
        before_SF6 = len(suit_rank_array[26])
        before_SF7 = len(suit_rank_array[27])
        before_SF8 = len(suit_rank_array[28])
        before_SF9 = len(suit_rank_array[29])
        before_SF10 = len(suit_rank_array[30])

        if wild_card2[0] == "S":
            # if wild card is a Spade suit, then we only have to try that card
            # if it gets to a trip or better OR adds a straight flus

            suit_rank_array = analysis3.suit_rank_array

            after_trips = len(suit_rank_array[13])
            after_fourks = len(suit_rank_array[14])
            after_fiveks = len(suit_rank_array[15])
            after_sixks = len(suit_rank_array[16])
            after_sevenks = len(suit_rank_array[17])
            after_eightks = len(suit_rank_array[18])
            after_nineks = len(suit_rank_array[19])
            after_tenks = len(suit_rank_array[20])
            after_total_straight_flushes = suit_rank_array[25] + suit_rank_array[26] + suit_rank_array[27] + \
                                           suit_rank_array[28] + suit_rank_array[29] + suit_rank_array[30]

            if after_total_straight_flushes > before_total_straight_flushes:
                check_wild = True
            elif len(suit_rank_array[25]) > before_SF5 or len(suit_rank_array[26]) > before_SF6 or \
                    len(suit_rank_array[27]) > before_SF7 or len(suit_rank_array[28]) > before_SF8 or \
                        len(suit_rank_array[29]) > before_SF9 or len(suit_rank_array[30]) > before_SF10:
                check_wild = True

            if (before_trips < after_trips) or (before_fourks < after_fourks) or (before_fiveks < after_fiveks):
                check_wild = True
            if (before_sixks < after_sixks) or (before_sevenks < after_sevenks) or (before_eightks < after_eightks):
                check_wild = True
            if before_nineks < after_nineks or before_tenks < after_tenks:
                check_wild = True

        # not a spade
        else:

            suit_rank_array = analysis2.suit_rank_array
            before_total_straight_flushes = suit_rank_array[25] + suit_rank_array[26] + suit_rank_array[27] + \
                                     suit_rank_array[28] + suit_rank_array[29] + suit_rank_array[30]

            suit_rank_array = analysis3.suit_rank_array
            after_total_straight_flushes = suit_rank_array[25] + suit_rank_array[26] + suit_rank_array[27] + \
                                     suit_rank_array[28] + suit_rank_array[29] + suit_rank_array[30]

            # print ("before", before_SF5, before_SF6, before_SF7, before_SF8, before_SF9, before_SF10)
            # print ("after-", len(suit_rank_array[45]), len(suit_rank_array[46]), len(suit_rank_array[47]), \
            #       len(suit_rank_array[48]), len(suit_rank_array[49]), len(suit_rank_array[50]))

            if after_total_straight_flushes > before_total_straight_flushes:
                check_wild = True
            elif len(suit_rank_array[25]) > before_SF5 or len(suit_rank_array[26]) > before_SF6 or \
                    len(suit_rank_array[27]) > before_SF7 or len(suit_rank_array[28]) > before_SF8 or \
                        len(suit_rank_array[29]) > before_SF9 or len(suit_rank_array[30]) > before_SF10:
                check_wild = True
            # print ("check wild results", wild_card2, check_wild)
            # print ("before", before_total_straight_flushes)
            # print ("after",  after_total_straight_flushes)

        return(check_wild)