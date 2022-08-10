from src.core.BestHand25 import *
from src.core.Deck import *
from src.core.WildList import *


import src.core.global_variables as global_variables

class BestHand25Wild(BestHand25):
    """
    given 25 cards with wild cards (card_list2)
    This class finds the best hand
    Attributes include:
        self.best_hand_points = best_wild_hand_points  = [-10000,0,0,0,0,0,0]
        self.best_25handx = best_25handx = [[],[],[],[],[],[],[]]
        self.best_wild_card = best_wild_cards[0]
    """

    def __init__(self, card_list2):
        global_variables.best_scores_list = []
        self.card_list2 = card_list2
        card_list2 = self.card_list2
        best_25handx = [[],[],[],[],[],[],[]]
        wild_cards = WildList(card_list2)
        best_wild_cards = []
        best_wild_hand_points = [-10000, 0, 0, 0, 0, 0, 0]
        # wild_cards.wild_card_combinations.reverse()
        if wild_cards.number_of_wild_cards == 0:
            # best_wild_hand_score, best_25handx = best_25card_hand(self.card_list2)
            myhand = BestHand25(card_list2,
                                best_wild_hand_points[0])
            best_wild_hand_points = candidate_hand_score = myhand.best_points[0], myhand.best_points[1], myhand.best_points[2],\
                                    myhand.best_points[3], myhand.best_points[4], myhand.best_points[5], myhand.best_points[6]
            best_25handx = myhand.best_pyramid_poker_hand

            print ("--------------{0:>9.2f}".format(candidate_hand_score[0]))
        else:
            card_list2_no_wilds = self.card_list2
            count = 0
            # print wild_cards.wild_card_combinations
            for wild_card_combos in wild_cards.wild_card_combinations:
                # print wild_card_combos
                for wild_card in wild_card_combos:
                    wild_card_x = wild_card
                    card_list2_no_wilds.append(wild_card_x)
                # print card_list2_no_wilds
                count = count + 1
                print ("Trying {0:7} {1:>3}".format(str(wild_card_combos), str(count)), end="")
                # candidate_hand_score, candidate_25handx = best_25card_hand(card_list2_no_wilds)
                myhand = BestHand25(card_list2, best_wild_hand_points[0])
                # myhand = BestHand25(card_list2, -99999)
                candidate_hand_score = myhand.best_points[0], myhand.best_points[1], myhand.best_points[2], myhand.best_points[3], \
                                       myhand.best_points[4], myhand.best_points[5], myhand.best_points[6]
                candidate_25handx = myhand.best_pyramid_poker_hand

                # print ("  ", candidate_hand_score[0], end="")
                if candidate_hand_score[0] > best_wild_hand_points[0]:
                    best_wild_hand_points = candidate_hand_score
                    best_25handx = candidate_25handx
                    best_wild_cards = wild_card_combos
                    print ("--------{0:>10} {1:>9.2f}".format(str(best_wild_cards), candidate_hand_score[0]))

                else:
                    pass
                    print ("--{0:>9}".format(str(candidate_hand_score[0])))
                for wild_card in wild_card_combos:
                    wild_card_x = wild_card
                    card_list2_no_wilds.remove(wild_card_x)

        self.best_hand_points = best_wild_hand_points
        self.best_25handx = best_25handx
        self.best_medium_score = myhand.best_hand_points
        if len(best_wild_cards) > 0:
            self.best_wild_card = best_wild_cards[0]
        else:
            self.best_wild_card = ""
        return