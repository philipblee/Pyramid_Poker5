from itertools import *
from src.core.PokerHand import *
from src.core.sort_cards import *
import time
from src.core.Analysis import *


def disjointed_hands(high_hand, high_hand2):
    disjointed_hands_found = False
    hand_num1 = len(high_hand)
    hand_num2 = len(high_hand2)
    for i in range(0, hand_num1):
        handx = high_hand[i]
        # print ("handx",handx)
        for j in range(0, hand_num2):
            handy = high_hand2[j]
            # print ("handy",handy)
            # print("disjointed_hands test, handx, handy", handx, handy)
            a = set(handx)
            b = set(handy)
            if a.isdisjoint(b):
                disjointed_hands_found = True
                # print ("Disjointed Hands Found == True")
                break
        if disjointed_hands_found == True:
            break
    return (disjointed_hands_found)


def disjointed_hands_matrix(high_hand, high_hand2):
    matrix = []
    hand_num1 = len(high_hand)
    hand_num2 = len(high_hand2)
    for i in range(hand_num1):
        row = []
        for j in range(hand_num2):
            row.append(True)
        matrix.append(row)

    for i in range(hand_num1):
        handx = high_hand[i]
        # print ("handx",handx)
        for j in range(hand_num2):
            handy = high_hand2[j]
            # print ("handy",handy)
            # print("disjointed_hands test, handx, handy", handx, handy)
            a = set(handx)
            b = set(handy)
            if a.isdisjoint(b):
                matrix[i][j] = True
            else:
                matrix[i][j] = False
    return (matrix)

class LegalPokerHands():
    suits = "WSHDC"
    ranks = "W123456789TJQKA"
    straight_ranks = "WA23456789TJQKA"

    def __init__ (self, card_list):
        """
        :param card_list:
        Given 25 card_list, determine all feasible hand6, 5, 4, 3, 2, 1
        """

        analysis = Analysis(card_list)
        self.card_list = card_list

        """ This next section will find all possible 5+ card hand's by hand type in order
            5K's, SF's, 4K's, FH's, Flushes', Straights', Trip's, 2Ps and P's.
        """

        # generating all feasible hand6 and hand5's - high_hand is used for interim list of hands
        best_hand = PokerHand()
        self.hand5 = 3000 * [None]
        self.hand6 = 3000 * [None]
        high_hand = 3000 * [None]
        flush_hand = 3000 * [None]
        high_hand_score = []
        card_list2 = card_list

        # LegalHands cannot handle wild cards
        for card in card_list2:
            if card[0] == "W":
                print ("\n *** Error in LegalHands(), cannot handle wild cards ***")
                return

        hand_num = 0

        # create 10 of a kind
        for tenks in analysis.tenks_list:
            high_hand[hand_num] = tenks
            hand_num += 1

            # look to create 9k, 8k, ..., to 4k
            for x in range(9,3,-1):
                for xkind in list(combinations(tenks, x)):
                    high_hand[hand_num] = xkind
                    hand_num += 1

        if len(analysis.ten_card_straightflush) > 0:
            for hand in analysis.suit_rank_array[30]: # for each straight flush
                high_hand[hand_num] = hand
                hand_num = hand_num + 1

        # create 9 of a kind
        for nineks in analysis.nineks_list:
            high_hand[hand_num] = nineks
            hand_num += 1

            # look to create 8k, 7k, ..., to 4k
            for x in range(8,3,-1):
                for xkind in list(combinations(nineks, x)):
                    high_hand[hand_num] = xkind
                    hand_num += 1

        # create 3 trips
        for nineks in analysis.nineks_list:
            high_hand[hand_num] = nineks[0:3]
            hand_num += 1
            high_hand[hand_num] = nineks[3:6]
            hand_num += 1
            high_hand[hand_num] = nineks[6:9]
            hand_num += 1

        if len(analysis.nine_card_straightflush) > 0:
            for hand in analysis.suit_rank_array[29]: # for each straight flush
                high_hand[hand_num] = hand
                hand_num = hand_num + 1


        # each 8 of a kind
        for eightks in analysis.eightks_list:
            high_hand[hand_num] = eightks
            hand_num += 1

            # look to create 7k, 6k, ..., to 4k
            for x in range(7,3,-1):
                for xkind in list(combinations(eightks, x)):
                    high_hand[hand_num] = xkind
                    hand_num += 1

        if len(analysis.eight_card_straightflush) > 0:
            for hand in analysis.suit_rank_array[28]: # for each straight flush
                high_hand[hand_num] = hand
                hand_num = hand_num + 1

        # create 7 of a kind
        for sevenks in analysis.sevenks_list:
            high_hand[hand_num] = sevenks
            hand_num += 1

            # look to create 6k, 5k, ..., to 4k
            for x in range(6,3,-1):
                for xkind in list(combinations(sevenks, x)):
                    high_hand[hand_num] = xkind
                    hand_num += 1

        if len(analysis.seven_card_straightflush) > 0:
            for hand in analysis.suit_rank_array[27]: # for each straight flush
                high_hand[hand_num] = hand
                hand_num = hand_num + 1

        # create 6 of kinds
        for sixks in analysis.sixks_list:
            high_hand[hand_num] = sixks
            hand_num += 1

        # look to create 5k, 4k
        for sixks in analysis.sixks_list:
            for x in [5,4]:
                for xkind in list(combinations(sixks, x)):
                    high_hand[hand_num] = xkind
                    hand_num += 1

        if len(analysis.six_card_straightflush) > 0:
            for hand in analysis.suit_rank_array[26]: # for each straight flush
                high_hand[hand_num] = hand
                hand_num = hand_num + 1

        # create 5 of kinds
        for fiveks in analysis.fiveks_list:
            high_hand[hand_num] = fiveks
            hand_num = hand_num + 1

            # create 4 of kinds
            for fourk in list(combinations(fiveks,4)):
                high_hand[hand_num] = fourk
                hand_num = hand_num + 1

        if len(analysis.five_card_straightflush) > 0:
            for hand in analysis.suit_rank_array[25]: # for each straight flush
                # print ("five card straight flushes", hand)
                high_hand[hand_num] = hand
                hand_num = hand_num + 1

        # create simple 4 of kinds 9/22/2021
        for fourks in analysis.fourks_list:
            high_hand[hand_num] = fourks
            hand_num = hand_num + 1

        # # find 4K hands - comment out 9/22/2021
        # for fourks in analysis.fourks_list:
        #     flat_list = []
        #     for sublist in analysis.pairs_list:
        #         for item in sublist:
        #             flat_list.append(item)
        #     for item in analysis.singles_list:
        #         flat_list.append(item)
        #
        #     # get flat_list of singles_list and pairs_list as kickers for 4K
        #     # this ensures that 4K with every kicker is considered in deciding best hands
        #     for card in flat_list:
        #         temp = []
        #         temp = list(fourks)
        #         temp.append(card)
        #         high_hand[hand_num] = temp
        #         # print (high_hand[hand_num])
        #         hand_num = hand_num + 1

        # make sure there are at least 2 disjointed hands, or BestHand25 will fail
        # look for two disjointed hands in high_hand

        # for each hand, look for 3 specials which do not intersect
        special_hands = list(filter(None, high_hand))
        analysis.three_specials = False
        No_Flush_or_Straight = False
        No_Full_Houses = False

        # look for 3 trips and 2 full houses
        if len(analysis.tripx_list) >=5 and len(analysis.pairs_list) >=2 \
                and len(special_hands) == 0:
            No_Flush_or_Straight = True

        self.Three_Disjointed_Specials = False
        # look for 3 specials that isdisjoint
        if len(special_hands) >= 3:
            # look for disjoint specials from 3 to 4
            combos = list(combinations(special_hands, 3))
            for hand1, hand2, hand3 in combos:
                hand1, hand2, hand3 = set(hand1), set(hand2), set(hand3)
                # print ("h1,h2,h3", hand1, hand2, hand3)
                if hand1.isdisjoint(hand2) and hand1.isdisjoint(hand3) and hand2.isdisjoint(hand3):
                    No_Flush_or_Straight = True
                    No_Full_Houses = True
                    analysis.three_specials = True
                    self.Three_Disjointed_Specials = True
                    break

        # # look for 2 specials and at least 3 trips that don't intersect
        # elif (len(special_hands) == 2) and (len(analysis.trips_list) >= 3):
        #     # look for five hands that do not overlap
        #     test_five_hands = special_hands
        #     for trips in analysis.trips_list:
        #         test_five_hands.append(trips)
        #         combos = list(combinations(test_five_hands, 5))
        #         h = [[],[],[],[],[],[]]
        #         for h1, h2, h3, h4, h5 in combos:
        #             h1, h2, h3, h4, h5 = set(h1), set(h2), set(h3), set(h4), set(h5)
        #             h1_no_overlap = False
        #             # does h[1] intersect with h[2:6]
        #             if h1.intersection(h2) == set([]):
        #                 if h1.intersection(h3) == set([]):
        #                     if h1.intersection(h4) == set([]):
        #                         if h1.intersection(h5) == set([]):
        #                             h1_no_overlap = True
        #             h2_no_overlap = False
        #             # does h[2] intersect with h[3:6]
        #             if h2.intersection(h3) == set([]):
        #                 if h3.intersection(h4) == set([]):
        #                     if h2.intersection(h5) == set([]):
        #                         h2_no_overlap = True
        #             if h1_no_overlap and h2_no_overlap:
        #                 No_Flush_or_Straight = True
        # # print ("3 disjointed specials",  self.Three_Disjointed_Specials)

        if not No_Full_Houses:
            # full houses with trips and pairs
            if analysis.trips >= 1 and analysis.pairs >=1:
                for trip in analysis.trips_list:
                    for pair in analysis.pairs_list:
                        high_hand[hand_num] = trip + pair
                        hand_num += 1

            # for each fourk, create 4 trips and add pairs to make full houses
            if analysis.fourks >= 1 and analysis.pairs >= 1:
                for fourk in analysis.fourks_list:
                    for trip in list(combinations(fourk,3)):
                        for pair in analysis.pairs_list:
                            high_hand[hand_num] = list(trip) + list(pair)
                            hand_num += 1

            # for each trip, create 3 pairs to potentially make full houses
            for trip1 in analysis.trips_list:
                for trip2 in analysis.trips_list:
                    if trip1 is not trip2:
                        for pair in list(combinations(trip2,2)):
                            high_hand[hand_num] = list(trip1) + list(pair)
                            hand_num += 1

        # finding flushes - make sure each flush is not a straight flush or a 4k or 5k
        flush_overlap = 0
        if not No_Flush_or_Straight:
            flush_num = 0
            for i in range(1, 5):  # cycle through analysis.suits
                if analysis.suit_rank_array[i][15] >= 5:
                    flush_cards = []
                    for card in card_list2:
                        if self.suits[i] == card[0]:
                            flush_cards.append(card)
                    # print ("\nprint suits", i, flush_cards)
                    flush_hands_list = list(combinations(flush_cards, 5))

                    # this next statement removes all duplicates
                    flush_hands_list = list(set(flush_hands_list))

                    # this next section deletes flushes that are also Trips/4K's/5K's and SF's
                    for handy in flush_hands_list:
                        flush_overlap_trips_or_better = False
                        duplicate = False
                        flush_analyze = Analysis(handy)
                        flush_analyze = flush_analyze.suit_rank_array
                        for i in range(14):
                            if flush_analyze[5][i] >= 3 or len(flush_analyze[45]) > 0:
                                flush_overlap_trips_or_better = True
                                flush_overlap += 1
                                # print ("flush_overlap_trips_or_better found")
                        if not flush_overlap_trips_or_better and not duplicate:
                            flush_hand[flush_num] = handy
                            flush_num += 1

            for i in range(flush_num):
                high_hand[hand_num + i] = flush_hand[i][0:5]
            hand_num = hand_num + flush_num

            # print "after_flush", high_hand[0:20]
            for j in [10,1,9,8,7,6,5,4,3,2]:  # straight
                if analysis.suit_rank_array[6][j] >= 1:
                    straight_card = [[],[],[],[],[]]
                    for k in range(5):
                        for card in card_list2:
                            if self.straight_ranks[j + k] in card:
                                straight_card[k].append(card)

                    for straight_hand in list(product(straight_card[0], straight_card[1],
                                                      straight_card[2], straight_card[3], straight_card[4])):
                        high_hand[hand_num] = straight_hand
                        hand_num = hand_num + 1

        high_hand = list(filter(None, high_hand))
        # make sure cards in all hands are sorted in rank_sort order
        length = len(high_hand)
        if length > 0:
            for i in range(len(high_hand)):
                high_hand[i] = sorted(high_hand[i], key=rank_sort, reverse=True)

        # print ("number of high_hand's", len(high_hand), high_hand[0], high_hand[1])

        if disjointed_hands(high_hand, high_hand) == True:
            pass
            # print ("disjointed hands found in high_hand")
        else:
            print ("FATAL ERROR in LegalPokerHands, can't find two disjointed hands in high_hand")

        # remove duplicates
        high_hand = sorted(high_hand, reverse=True)
        hands_list = high_hand
        last_handy = ""
        no_duplicates_list = []
        for hand in hands_list:
            duplicate = False
            if (last_handy == hand):
                duplicate = True
            if not duplicate:
                no_duplicates_list.append(hand)
            last_handy = hand
        high_hand = list(no_duplicates_list)

        # for each hand, get the short_score
        for hand in high_hand:
            high_hand_score.append(PokerHand(hand).short_score)

        # now sort high_hand like high_hand_score as primary, then sort high_hand_score
        high_hand = [x for _,x in sorted(zip(high_hand_score, high_hand), reverse=True)]
        high_hand_score = sorted(high_hand_score, reverse=True)

        # for each high_hand, create analysis.hand6 and self.hand5
        for i in range(len(high_hand)):
            x = best_hand.get_points_from_hand(high_hand[i], "6")[1]
            y = best_hand.get_points_from_hand(high_hand[i], "5")[1]
            self.hand6[i] = [high_hand[i], high_hand_score[i], x]
            self.hand5[i] = [high_hand[i], high_hand_score[i], y]
            # print (self.hand6[i])

        self.hand5 = list(filter(None, self.hand5))
        self.hand6 = list(filter(None, self.hand6))

        """ three_card_hands will find all possible 3 card hands including special hands
        """

        best_hand = PokerHand()
        # high_hand_points = [None] * 10000
        self.hand4 = [None] * 2500
        self.hand3 = [None] * 2500
        self.hand2 = [None] * 2500
        high_hand_score = []
        high_hand = [None] * 2500

        card_list2 = self.card_list

        # print ("printing 3 card hands as I create them")
        hand_num = 0
        for hand in special_hands:
            if len(hand) <= 6:
                high_hand[hand_num] = hand
                # print(hand_num, high_hand[hand_num])
                hand_num += 1

        # for each 6K, create 60 trips
        for sixk in analysis.sixks_list:
            for trip in list(combinations(sixk,3)):
                high_hand[hand_num] = trip
                hand_num += 1
        # for each fivek, create 10 trips
        for fivek in analysis.fiveks_list:
            for trip in list(combinations(fivek,3)):
                high_hand[hand_num] = trip
                hand_num += 1

        # for each fourk, create 4 trips
        for fourk in analysis.fourks_list:
            for trip in list(combinations(fourk,3)):
                high_hand[hand_num] = trip
                hand_num += 1

        for trip in analysis.trips_list:
            high_hand[hand_num] = trip
            # print(hand_num, high_hand[hand_num])
            hand_num += 1

        for pair in analysis.pairs_list:
            high_hand[hand_num] = pair
            # print(hand_num, high_hand[hand_num])
            hand_num += 1

        # for each trip, create 3 pairs
        for trip in analysis.trips_list:
            for pair in list(combinations(trip,2)):
                pair1_list = list(pair)
                high_hand[hand_num] = pair1_list
                # print(hand_num, high_hand[hand_num])
                hand_num += 1

        for pair in analysis.pairs_list:
            high_hand[hand_num] = [pair[0]]
            hand_num += 1
            high_hand[hand_num] = [pair[1]]
            hand_num += 1

        for single in analysis.singles_list:
            # print hand_num, single
            high_hand[hand_num] = [single]
            # print(hand_num, high_hand[hand_num])
            hand_num += 1

        # remove any hands that are empty
        high_hand = list(filter(None, high_hand))

        # print ("entire list")
        # make sure cards in hands are sorted in rank_sort order
        for i in range(len(high_hand)):
            high_hand[i] = sorted(high_hand[i], key=rank_sort, reverse = True)
            # print (high_hand[i])

        high_hand = sorted(high_hand, reverse = True)

        # remove duplicates
        hands_list = high_hand
        last_handy = ""
        no_duplicates_list = []
        for hand in hands_list:
            duplicate = False
            # print (last_handy, hand, last_handy == hand)
            if (last_handy == hand):
                duplicate = True
            if not duplicate:
                no_duplicates_list.append(hand)
            last_handy = hand
        high_hand = list(no_duplicates_list)

        for hand in high_hand:
            if hand[0] == "W":
                print ("Error, cannot handle wild cards in LegalHands")
            high_hand_score.append(PokerHand(hand).short_score)
            # print "5 card hand, add short_score", hand, Hand(hand).short_score

        # sort high_hand like high_hand_score, then sort high_hand_score
        high_hand = [x for _, x in sorted(zip(high_hand_score, high_hand), reverse=True)]
        high_hand_score = sorted(high_hand_score, reverse=True)

        # for each high_hand, create self.hand4, self.hand3, self.hand2 with hand, points and points
        for i in range(len(high_hand)):
            x = best_hand.get_points_from_hand(high_hand[i], "4")[1]
            y = best_hand.get_points_from_hand(high_hand[i], "3")[1]
            z = best_hand.get_points_from_hand(high_hand[i], "2")[1]
            self.hand4[i] = (high_hand[i], high_hand_score[i], x)
            self.hand3[i] = (high_hand[i], high_hand_score[i], y)
            self.hand2[i] = (high_hand[i], high_hand_score[i], z)
            # print(high_hand[i], high_hand_score[i],x,y,z)

        # remove empty hands
        self.hand4 = list(filter(None, self.hand4))
        self.hand3 = list(filter(None, self.hand3))
        self.hand2 = list(filter(None, self.hand2))

        if set(self.hand6[0][0]) == (set(self.hand4[0][0])):
            self.hand4 = self.hand4[1:]
            self.hand3 = self.hand3[1:]
            self.hand2 = self.hand2[1:]

        if set(self.hand5[0][0]) == (set(self.hand4[0][0])):
            self.hand4 = self.hand4[1:]
            self.hand3 = self.hand3[1:]
            self.hand2 = self.hand2[1:]

        i = 0
        if not self.Three_Disjointed_Specials:
            while len(self.hand4[i][0]) > 3:
                i += 1
            self.hand4 = self.hand4[i:]
            self.hand3 = self.hand3[i:]
            self.hand2 = self.hand2[i:]

        # determine self.hand1
        # remove trips - since trips will never be broken up to make hand1
        analysis.straight_flush_cards = []
        if len(analysis.five_card_straightflush) > 0:
            for row in range(45,51):
                for hand in analysis.suit_rank_array[row]:
                    analysis.straight_flush_cards.append(set(hand))

        self.hand1 = []
        # find do not delete list based on trip being in a straight flush
        do_not_delete_list = []
        for trip in analysis.trips_list:
            for card in trip:
                if card in analysis.straight_flush_cards:
                    do_not_delete_list.extend(trip)
                    break

        for card in card_list2:
            # print ("hand 1", card, ranks.index(card[1]), analysis.suit_rank_array[5][ranks.index(card[1])])
            if analysis.suit_rank_array[5][ranks.index(card[1])] != 3 or card in do_not_delete_list:
                self.hand1.append([card])

        for i in range(len(self.hand1)):
            y = best_hand.get_points_from_hand(self.hand1[i], "1")
            self.hand1[i] = self.hand1[i], y[0], y[1]

        # sort by self.hand1 points
        self.hand1.sort(key=lambda x: x[1], reverse=True)

        # [print(x) for x in self.hand2]
        self.hand6_count = len(self.hand6)
        self.hand5_count = len(self.hand5)
        self.hand4_count = len(self.hand4)
        self.hand3_count = len(self.hand3)
        self.hand2_count = len(self.hand2)
        self.hand1_count = len(self.hand1)

        self.hand4_trips = analysis.trips

        self.hands = [[]]
        self.hands.append(self.hand1)
        self.hands.append(self.hand2)
        self.hands.append(self.hand3)
        self.hands.append(self.hand4)
        self.hands.append(self.hand5)
        self.hands.append(self.hand6)

        self.hand_count = [0, self.hand1_count, self.hand2_count,
                           self.hand3_count, self.hand4_count,
                           self.hand5_count, self.hand6_count]

        # # create disjoint_matrix
        # temp = [[],[],[],[],[],[],[]]
        # temp[6] = [(x[0]) for x in self.hand6]
        # temp[5] = [(x[0]) for x in self.hand5]
        # temp[4] = [(x[0]) for x in self.hand4]
        # temp[3] = [(x[0]) for x in self.hand3]
        # temp[2] = [(x[0]) for x in self.hand2]
        # temp[1] = [(x[0]) for x in self.hand1]
        #
        # matrix = []
        # for i in range(7):
        #     vector = []
        #     for j in range(7):
        #         vector.append([])
        #     matrix.append(vector)
        #
        # for i in range(7):
        #     for j in range(7):
        #         matrix[i][j] = disjointed_hands_matrix(temp[i], temp[j])


        # print ("hand6_count =", self.hand6_count)
        # [print (x) for x in self.hand6]
        # print ("hand5_count =", self.hand5_count)
        # [print (x) for x in self.hand5]
        # print ("hand4_count =", self.hand4_count)
        # [print (x) for x in self.hand4]
        # print ("hand3_count =", self.hand3_count)
        # [print (x) for x in self.hand3]
        # print ("hand2_count =", self.hand2_count)
        # [print (x) for x in self.hand2]
        # print ("hand1_count =", self.hand1_count)
        # [print (x) for x in self.hand1]


        # look for duplicate hands, meaning that the cards are identical

        return

