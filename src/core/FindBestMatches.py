# FindBestMatches takes 20 card hand and adds one WildCard at a time
# Whatever card is chosen to replace WildCard, then add WildCard again
# and repeat for all 5 kitty cards - this gives you the ideal 5 cards
# in rank order
# Then keep going to 10 cards, basically removing unneccesary cards

from src.core.BestHand25Wild import *

class FindBestMatches(list):

    def __init__(self, card_list20):
        matches = []
        points = []
        besthand = []
        best_wild_cards = []
        # determine 20 card baseline
        card_list = card_list20
        best20 = BestHand25Wild(card_list)
        besthand.append(best20)
        best_points = best20.best_hand_points[0]
        print (best_points, "initial_best_points")
        card_list = card_list20 + ["WW?"]
        for i in range(8):
            best = BestHand25Wild(card_list)
            print ("\n",best.best_wild_card, "best_wild_card")
            print (best.best_25handx, "best_hand")
            # find out which hand, wild card is in
            hand_values = [4, 8, 10, 12, 14, 16, 18, 20]
            best_wild_card = best.best_wild_card
            for hand in best.best_25handx[1:7]:
                if best.best_wild_card in hand:
                    if PokerHand(hand).hand_value in hand_values:
                        # suit is not important
                        best_wild_card = "Any " + best_wild_card[1]
            matches.append(best_wild_card)
            print (best_wild_card, "will work")
            points.append(best.best_hand_points[0])
            print (i+1, "myhand20_analysis card rank")
            # print (points[-1], "best_points")
            print (points[-1], int(points[-1] - best_points), "best_points_increase")
            # print (card_list, "card_list before removing WW?")
            # card_list.remove("WW?")
            card_list.append(best.best_wild_card)
            # print(card_list, "card_list after adding myhand20_analysis card")
            card_list = card_list + ["WW?"]
            best_points = points[-1]
        return