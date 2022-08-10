# MyHand20 Analysis basically analyzes he first 20 cards to decide whether to play or not
# MyHand20 Analusis 2 is changed methodology
# First I determine the number of formed hands
# This would include 4K, SF, Trip or better - how many?
# Next can kitty improve hand?
# First, Pairs can turn into Trips
# Four card straight flushes can turn into SF's
# Trips turn into 4K's
# 4K's can turn into 5K's
# Do you have wild cards and how does that affect the hand?
# I'm probably using wild card to make first

from src.core.Analysis import *
from src.core.StraightFlushList import *
from src.core.BestHand25Wild import *

class MyHand20_Analysis2(list):

    def __init__(self, card_list):
        ranks = "W123456789TJQKA"
        suits = "WCDHS"
        card_list1 = (sorted(card_list, key=rank_sort, reverse=True))
        card_list_temp = list(card_list)
        MyHand20 = Analysis(card_list_temp)
        wilds = 0
        for card in card_list:
            if "WW" in card:
                wilds += 1
        for i in range (0,25):
            print (MyHand20.suit_rank_array[i])


        # Step 1: find formed hands by playing with 20 cards
        # Look at first 20 cards and decide what to do
        card_list20 = list(card_list[0:20])
        card_list20 = (sorted(card_list20, key=rank_sort, reverse=True))
        card_list_temp = list(card_list20)
        print ("Player's 20 Card Hand: ", card_list20)

        myhand20 = BestHand25Wild(card_list_temp)
        card_list_temp = list(card_list20)

        print ("20 Cards-Best Hand", myhand20.best_25handx[1:7])
        print ("20 Cards-Best Points", myhand20.best_hand_points)

        formed_hands = 0
        formed_hands_quality = 0
        # go through hands 2 through 6 and figure out if they are trip or better
        for i in range (2,7):
            # use Analysis to figure out what hand is
            poker_hand = myhand20.best_25handx[i]
            poker_score = PokerHand(poker_hand).short_score
            poker_hand_value = poker_score/10000
            print ("poker_hand", poker_hand)
            print ("poker_score", poker_score)
            # poker_hand_value = poker_score/10000
            # print (poker_hand_value)
            if i >= 2 and i <=4:
                if poker_hand_value == 4:
                    formed_hands += 1
            if i >= 2:
                if poker_hand_value >= 8:
                    formed_hands += 1
            if i>=2 and poker_hand_value >=8:
                formed_hands_quality += 1

            if i == 2 and poker_hand_value == 4:
                if (poker_score - 40000)/100 >= 7:
                    formed_hands_quality += 1
            if i == 3 and poker_hand_value == 4:
                if (poker_score - 40000)/100 >= 11:
                    formed_hands_quality += 1
            if i == 4 and poker_hand_value == 4:
                if (poker_score - 40000)/100 >= 14:
                    formed_hands_quality += 1

            if i == 5 and poker_hand_value >= 8:
                if (poker_score - poker_score*1000)/100  >= 10:
                    formed_hands_quality += 1
            if i == 6 and poker_hand_value >= 8:
                if (poker_score - poker_score*1000)/100 >= 14:
                    formed_hands_quality += 1

            print ("formed_hands", formed_hands)
            print ("formed_hands_quality", formed_hands_quality)


