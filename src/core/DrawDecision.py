from src.core.PokerHand import *
import logging

logging.basicConfig(filename="output.txt", format='%levelname)s:%(message)s', level=logging.ERROR)
logging.debug("This is a debug level message")
from OldFiles.analyze_wild import *

class DrawDecision:

    def __init__(self, five_cards):

        found = False
        five_cards = sorted(five_cards, reverse=True, key=rank_sort)
        # print five_cards,"  ---   ",
        ranks = "W123456789TJQKA"
        suits = "WSHDC"
        discards = []
        holds = five_cards
        temp = [[],[],[],[],[],[],[]]
        my_hand = PokerHand(five_cards)

        if not found:
            # check for Royal straight flush
            if len(my_hand.analysis.suit_rank_array[25]) > 0:
                for hand in my_hand.analysis.suit_rank_array[25]:
                    if hand[0][1] == "T":
                        hand_description = "1. Dealt royal straight flush"
                        found = True
                        decision = 1
                        discards = []
                        holds = five_cards
            # for i in range (1,5):
            #     royal = 0
            #     for j in range(10,15):
            #         if my_hand.analysis.suit_rank_array[i][j] == 1:
            #             royal += 1
            #     if royal == 5:
            #         hand_description = "1. Dealt royal straight flush"
            #         found = True
            #         decision = 1
            #         discards = []
            #         holds = five_cards
        # look for a straight flush
        if not found:
            if len(my_hand.analysis.suit_rank_array[25]) > 0:
                hand_description = "2. straight flush"
                found = True
                decision = 2
                discards = []
                holds = five_cards


            # for i in range(1,5):
            #     for j in range(1,10):
            #         straightflush_cards = sum(my_hand.suit_rank_array[i][j:j+4])
            #         if straightflush_cards == 5:
            #             hand_description = "2. straight flush"
            #             found = True
            #             decision = 2
            #             discards = []
            #             holds = five_cards
        # look for 4K
        if not found:
            discards = []
            for i in range(2,15):
                if my_hand.analysis.suit_rank_array[5][i] == 4:
                    hand_description = "3. Dealt4 of a kind"
                    found = True
                    decision = 3

        if not found:
            discards = []
            holds = []
            # check for 4 to a Royal Flush
            for i in range (1,5):
                royal = 0
                for j in range(10,15):
                    if my_hand.analysis.suit_rank_array[i][j] == 1:
                        royal += 1
                        temp[royal] = [i,j]
                if royal == 4:
                    hand_description = "4. 4 to royal straight flush"
                    found = True
                    decision = 4
                    for card in five_cards:
                        if suits.index(card[0]) == i and ranks.index(card[1]) >=10 and ranks.index(card[1])<=14:
                            holds.append(card)
                    discards = set(five_cards).difference(set(holds))

        # look for full house
        trip_flag = False
        pair_flag = False
        trip_rank = 0
        if not found:
            discards = []
            for i in range(2,15):
                if my_hand.analysis.suit_rank_array[5][i] == 3:
                    trip_flag = True
                    trip_rank = i
                if my_hand.analysis.suit_rank_array[5][i] == 2:
                    pair_flag = True
        if pair_flag and trip_flag:
            hand_description = "5. Dealt Full House"
            found = True
            decision = 5
            discards = []
            holds = five_cards

        # look for flush
        if not found:
            discards = []
            for i in range (1,5):
                if my_hand.analysis.suit_rank_array[i][15] == 5:
                    hand_description = "6. Dealt flush"
                    found = True
                    decision = 6
                    discards = []
                    holds = five_cards
        # look for trip
        if not found:
            discards = []
            if trip_flag == True:
                hand_description = "7. 3 of a Kind"
                found = True
                decision = 7
                for card in five_cards:
                    if ranks.index(card[1]) != trip_rank:
                        discards.append(card)

        # look for straight
        if not found:
            discards = []
            for i in range (1,11):
                if my_hand.analysis.suit_rank_array[6][i]  == 1:
                    hand_description = "8. Dealt straight"
                    found = True
                    decision = 8

        # look for 4 to a straight flush
        if not found:
            discards = []
            for i in range(1,5):
                for j in range(1,10):
                    straightflush_cards = sum(my_hand.analysis.suit_rank_array[i][j:j+4])

                    if straightflush_cards == 4:
                        hand_description = "9. 4 to straight flush"
                        found = True
                        decision = 9
                        for card in five_cards:
                            if suit.index(card[0]) == i and ranks.index(card[1]) >= j and ranks.index(card[1]) <= j+4 :
                                holds.append(card)
                        discards = set(five_cards).difference(set(holds))


        # check for 2 pairs
        if not found:
            pairs = 0
            pairs_rank = []
            for i in range(2,15):
                if my_hand.analysis.suit_rank_array[5][i] == 2:
                    pairs = pairs + 1
                    pairs_rank.append(i)
            if pairs == 2:
                hand_description = "10. Two Pairs"
                found = True
                decision = 10
                for card in five_cards:
                    if ranks.index(card[1]) not in pairs_rank:
                        discards.append(card)

            if not found:
                discards = []
                # check for High Pair
                pairs_rank = []
                for i in range (11,15):
                    if my_hand.analysis.suit_rank_array[5][i] == 2:
                        pair_flag = True
                        pairs_rank.append(i)
                        hand_description = "11. High Pair"
                        found = True
                        decision = 11
                        for card in five_cards:
                            if ranks.index(card[1]) not in pairs_rank:
                                discards.append(card)
            if not found:
                discards = []
                holds = []
                # check for 3 to a Royal Flush
                for i in range (1,5):
                    royal = 0
                    for j in range(10,15):
                        if my_hand.analysis.suit_rank_array[i][j] == 1:
                            royal += 1
                    if royal == 3:
                        hand_description = "12. 3 to royal flush"
                        found = True
                        decision = 12
                        for card in five_cards:
                            if ranks.index(card[1]) in [14, 13, 12, 11, 10] and suits.index(card[0]) == i:
                                holds.append(card)
                        discards = set(five_cards).difference(set(holds))
            if not found:
                discards = []
                # check for 4 to a flush
                for i in range (1,5):
                    if my_hand.analysis.suit_rank_array[i][15] == 4:
                        hand_description = "13. 4 to a flush"
                        found = True
                        decision = 13
                        for card in five_cards:
                                if suits.index(card[0]) != i:
                                    discards.append(card)


            if not found:
                discards = []
                # check for Low Pair
                for i in range(2, 11):
                    if my_hand.analysis.suit_rank_array[5][i] == 2:
                        hand_description = "15. Low Pair"
                        found = True
                        decision = 15
                        for card in five_cards:
                            if ranks.index(card[1]) != i:
                                discards.append(card)
            if not found:
                # check for unsuited TJQK
                straight = straight_count(my_hand.analysis.suit_rank_array[5], 4)
                for i in range(1,11):
                    discards = []
                    if straight[i] > 0 and i == 10:
                        hand_description = "14. Unsuited TJQK"
                        found = True
                        decision = 14
                        for card in five_cards:
                            if ranks.index(card[1]) not in [10, 13, 12, 11]:
                                discards.append(card)

            if not found:
                # check for 4 to an outside straight
                straight = straight_count(my_hand.analysis.suit_rank_array[5], 4)
                for i in range(1, 11):
                    if straight[i] > 0 and i != 10:
                        hand_description = "16. 4 to an outside straight with 0-2 high cards"
                        found = True
                        decision = 16
                        for card in five_cards:
                            if ranks.index(card[1]) not in [i, i+1, i+2, i+3, i+4]:
                                discards.append(card)
            if not found:
                discards = []
                # check for 3 to straight flush - High Cards >= gaps
                for i in range (1,5):
                    for j in range (1,11):
                        gaps = 0
                        if sum(my_hand.analysis.suit_rank_array[i][j:j+5]) == 3:
                            for k in range(0,4):
                                if (my_hand.analysis.suit_rank_array[i][j+k] == 1) and (my_hand.analysis.suit_rank_array[i][j+k+1]==0):
                                    gaps = gaps + 1
                            high_cards = sum(my_hand.analysis.suit_rank_array[i][10:15])
                            if high_cards >= gaps:
                                hand_description = "17. 3 to straight flush (High cards >= gaps)"
                                found = True
                                decision = 17
                            for card in five_cards:
                                if ranks.index(card[1]) in [j, j + 1, j + 2, j + 3, j + 4] and suits.index(card[0]) == i:
                                    holds.append(card)
                                discards = list(set(five_cards).difference(holds))


            if not found:
                discards = []
                # check for suited QJ
                for i in range(1,5):
                    if my_hand.analysis.suit_rank_array[i][12] == 1 and  my_hand.analysis.suit_rank_array[i][11] == 1:
                        hand_description = '18. suited QJ'
                        found = True
                        decision = 18
                        for card in five_cards:
                            if ranks.index(card[1]) not in [12, 11] and suits.index(card[0]) != i:
                                discards.append(card)

            if not found:
                discards = []
                # check for 4 to an inside straight, 4 high cards
                for j in range(1,11):
                    high_cards = 0
                    if sum(my_hand.analysis.suit_rank_array[5][j:j+5]) == 4:
                        for k in range(0,5):
                            if j+k >= 11:
                                high_cards = high_cards + 1
                        if high_cards == 4:
                            hand_description = "19. 4 to inside straight, 4 high cards"
                            found = True
                            decision = 19
                            for card in five_cards:
                                if ranks.index(card[1]) not in [j, j + 1, j + 2, j + 3, j + 4, j + 5]:
                                        discards.append(card)
            if not found:
                discards = []
                # check for suited KQ or KJ
                for i in range(1, 5):
                    if (my_hand.analysis.suit_rank_array[i][13] == 1 and my_hand.analysis.suit_rank_array[i][12] == 1) or  \
                       (my_hand.analysis.suit_rank_array[i][13] == 1 and my_hand.analysis.suit_rank_array[i][11] == 1):
                        hand_description = '20. suited KQ or KJ'
                        found = True
                        decision = 20

                        # discard based on whether it was KQ or KJ
                        if (my_hand.analysis.suit_rank_array[i][13] == 1 and my_hand.analysis.suit_rank_array[i][12] == 1):
                            for card in five_cards:
                                if ranks.index(card[1]) not in [13, 12] and suits.index(card[0]) != i:
                                    discards.append(card)
                        elif (my_hand.analysis.suit_rank_array[i][13] == 1 and my_hand.analysis.suit_rank_array[i][11] == 1):
                            for card in five_cards:
                                if ranks.index(card[1]) not in [13, 11] and suits.index(card[0]) != i:
                                    discards.append(card)
            if not found:
                discards = []
                holds = []
                # check for suited AK, AQ or AJ
                for i in range(1, 5):
                    if (my_hand.analysis.suit_rank_array[i][14] == 1 and my_hand.analysis.suit_rank_array[i][13] == 1) or \
                       (my_hand.analysis.suit_rank_array[i][14] == 1 and my_hand.analysis.suit_rank_array[i][12] == 1) or \
                        (my_hand.analysis.suit_rank_array[i][14] == 1 and my_hand.analysis.suit_rank_array[i][11] == 1):
                        hand_description = '21. suited AK, AQ or AJ'
                        found = True
                        decision = 21
                        for card in five_cards:
                            if ranks.index(card[1]) in [14, 13, 12, 11] and suits.index(card[0]) == i:
                                holds.append(card)
                        discards = set(five_cards).difference(set(holds))

            if not found:
                discards = []
                holds = []
                # check for 4 to an inside straight, 3 high cards
                for j in range(1,11):
                    high_cards = 0
                    if sum(my_hand.analysis.suit_rank_array[5][j:j+5]) == 4:
                        for k in range(0,5):
                            if j+k >= 11:
                                high_cards = high_cards + 1
                        if high_cards >= 3:
                            hand_description = "22. 4 to inside straight, 3 high cards"
                            found = True
                            decision = 22
                            for card in five_cards:
                                if ranks.index(card[1]) in [j, j+1, j+2, j+3, j+4]:
                                    holds.append(card)
                            discards = set(five_cards).difference(set(holds))

            if not found:
                discards = []
                # check for 3 to straight flush - One gap and no high card or two gaps and 1 high card, ace low and 2-3-4
                gaps = 0;
                for i in range (1,5):
                    for j in range (1,11):
                        if sum(my_hand.analysis.suit_rank_array[i][j:j+5]) == 3:
                            for k in range(0,4):
                                if (my_hand.analysis.suit_rank_array[i][j+k] == 1) and (my_hand.analysis.suit_rank_array[i][j+k+1]==0):
                                    gaps = gaps + 1
                            high_cards = sum(my_hand.analysis.suit_rank_array[i][11:15])
                            if (gaps == 1 and high_cards == 0) or (gaps == 2 and high_cards == 1) or \
                                    (my_hand.analysis.suit_rank_array[i][2]==1 and my_hand.analysis.suit_rank_array[i][3]==1 and \
                                    my_hand.analysis.suit_rank_array[i][4]==1) or my_hand.analysis.suit_rank_array[i][1] == 1 :
                                hand_description = "23. 3 to straight flush (1 gap and 0 hc, 2 gaps and 1 hc, Ace low or 2-3-4)"
                                found = True
                                decision = 23
                                holds = []
                                # print "gaps", gaps, "high_cards", high_cards
                                for card in five_cards:
                                    # print card, j, j+1, j+2, j+3, j+4
                                    if ranks.index(card[1]) in [j, j + 1, j + 2, j + 3, j + 4] and suits.index(card[0]) == i:
                                        holds.append(card)
                                discards = list(set(five_cards).difference(holds))
            if not found:
                discards = []
                # check for unsuited JQK
                if (my_hand.analysis.suit_rank_array[5][11] == 1 and my_hand.analysis.suit_rank_array[5][13] == 1) and \
                    (my_hand.analysis.suit_rank_array[5][12] == 1):
                    hand_description = '24. unsuited KQJ'
                    found = True
                    decision = 24
                    for card in five_cards:
                        if ranks.index(card[1]) not in [13, 12, 11]:
                            discards.append(card)
            if not found:
                discards = []
                # check for unsuited QJ
                if (my_hand.analysis.suit_rank_array[5][12] == 1 and my_hand.analysis.suit_rank_array[5][11] == 1):
                    hand_description = '25. unsuited QJ'
                    found = True
                    decision = 25
                    for card in five_cards:
                        if ranks.index(card[1]) not in [12, 11]:
                            discards.append(card)

            if not found:
                discards = []
                # check for suited TJ
                for i in range(1, 5):
                    if (my_hand.analysis.suit_rank_array[i][11] == 1 and my_hand.analysis.suit_rank_array[i][10] == 1):
                        hand_description = '26. suited TJ'
                        found = True
                        decision = 26
                        for card in five_cards:
                            if ranks.index(card[1]) not in [10, 11]:
                                discards.append(card)
            if not found:
                discards = []
                # two unsuited high cards with King
                if (my_hand.analysis.suit_rank_array[5][13] == 1) and (my_hand.analysis.suit_rank_array[5][11] == 1  \
                        or my_hand.analysis.suit_rank_array[5][12] == 1):
                    hand_description = '27. unsuited KQ or KJ'
                    found = True
                    decision = 27
                    for card in five_cards:
                        if ranks.index(card[1]) not in [13, 12, 11]:
                            discards.append(card)
            if not found:
                discards = []
                # check for suited TQ
                for i in range(1, 5):
                    if (my_hand.analysis.suit_rank_array[i][12] == 1 and my_hand.analysis.suit_rank_array[i][10] == 1):
                        hand_description = '28. suited TQ'
                        found = True
                        decision = 28
                    for card in five_cards:
                        if ranks.index(card[1]) not in [10, 12]:
                            discards.append(card)

            if not found:
                discards = []
                # two unsuited high cards with Ace
                if (my_hand.analysis.suit_rank_array[5][14] == 1) and (my_hand.analysis.suit_rank_array[5][11] == 1  \
                        or my_hand.analysis.suit_rank_array[5][12] == 1 or my_hand.analysis.suit_rank_array[5][13] == 1):
                    hand_description = '29. unsuited AK, AQ or AJ'
                    found = True
                    decision = 29
                    for card in five_cards:
                        if ranks.index(card[1]) not in [14, 13, 12, 11]:
                            discards.append(card)
            if not found:
                discards = []
                if my_hand.analysis.suit_rank_array[5][11] == 1:
                    hand_description = "30. J only"
                    found = True
                    decision = 30
                    for card in five_cards:
                        if ranks.index(card[1]) not in [11]:
                            discards.append(card)
            if not found:
                discards = []
                # check for suited KT
                for i in range(1,5):
                    if my_hand.analysis.suit_rank_array[i][13] == 1 and  my_hand.analysis.suit_rank_array[i][10] == 1:
                        hand_description = '31. suited KT'
                        found = True
                        decision = 31
                        for card in five_cards:
                            if ranks.index(card[1]) not in [10,13]:
                                discards.append(card)
            if not found:
                discards = []
                if my_hand.analysis.suit_rank_array[5][12] == 1:
                    hand_description = "32. Q only"
                    found = True
                    decision = 32
                    for card in five_cards:
                        if ranks.index(card[1]) != 12:
                            discards.append(card)

            if not found:
                discards = []
                if my_hand.analysis.suit_rank_array[5][13] == 1:
                    hand_description = "33. K only"
                    found = True
                    decision = 33
                    for card in five_cards:
                        if ranks.index(card[1]) != 13:
                            discards.append(card)

            if not found:
                discards = []
                if my_hand.analysis.suit_rank_array[5][14] == 1:
                    hand_description = "34. A only"
                    found = True
                    decision = 34
                    for card in five_cards:
                        if ranks.index(card[1]) != 14:
                            discards.append(card)

            if not found:
                # check for 3 to straight flush - 0 High Cards and 2 gaps
                discards = []
                gaps = 0;
                for i in range (1,5):
                    for j in range (1,11):
                        if sum(my_hand.analysis.suit_rank_array[i][j:j+5]) == 3:
                            for k in range(0,4):
                                if (my_hand.analysis.suit_rank_array[i][j+k] == 1) and (my_hand.analysis.suit_rank_array[i][j+k+1]==0):
                                    gaps = gaps + 1
                            high_cards = sum(my_hand.analysis.suit_rank_array[i][11:15])
                            if high_cards == 0 and gaps == 2:
                                hand_description = "35. 3 to straight flush (0 High cards 2 gaps)"
                                found = True
                                decision = 35
                                for card in five_cards:
                                    if ranks.index(card[1]) in [j, j + 1, j + 2, j + 3, j + 4] and suits.index(card[0]) == i:
                                        holds.append(card)
                                discards = list(set(five_cards).difference(holds))

            if not found:
                hand_description = "36. Garbage, Discard everything"
                decision = 36
                discards = five_cards

        holds = list(set(five_cards).difference(discards))
        # print ("{0:>30} {1:>30} {2:>30} {3}".format(five_cards, discards, holds, decision, hand_description))
        self.decision = decision
        self.discards = discards
        self.holds = holds
        self.hand_description = hand_description
        return
