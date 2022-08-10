from src.core.PokerHand0 import *
from OldFiles.analyze_wild import *
import time
from src.core.Analysis import *

class LegalHands():
    """ returns self.suit_rank_array[i] where i is row
     0 - W           7 - SF S        11 - singles_list    21 - S_list
     1 - S           8 - SF H        12 - pairs_list      22 - H_list
     2 - H           9 - SF D        13 - trips_list      23 - D_list
     3 - D          10 - SF C        14 - fourks_list     24 - C_list
     4 - C                           15 - fiveks_list     25 - 5 card SF
     5 - Frequency                   16 - sixks_list      26 - 6 card SF
     6 - Straights                   17 - sevenks_list    27 - 7 card SF
                                     18 - eightks_list    28 - 8 card SF
                                     19 - nineks_list     29 - 9 card SF
                                     20 - tenks_list      30 - 10 card SF
]
     column 15 is always sum of row - for flushes [5][15], sf[7][14]
     """

    suits = "WSHDC"
    ranks = "W123456789TJQKA"
    straight_ranks = "WA23456789TJQKA"

    def __init__ (self, card_list):


        self.card_list = card_list
        # LegalHands cannot handle wild cards
        for card in card_list:
            if card[0] == "W":
                print ("Error in LegalHands2, remove wild cards and continue")
                self.card_list.remove(card)

        card_list = self.card_list

        # suit_array = Analysis(card_list)
        self.card_list = card_list
        self.suit_rank_array = analyze_wild(card_list)
        self.five_card_straightflushes = self.suit_rank_array[7][14]
        self.flushes = self.suit_rank_array[5][15]
        self.straights = self.suit_rank_array[6][15]
        self.singles_list = self.suit_rank_array[11]
        self.pairs_list = self.suit_rank_array[12]
        self.trips_list = self.suit_rank_array[13]
        self.fourks_list = self.suit_rank_array[14]
        self.fiveks_list = self.suit_rank_array[15]
        self.sixks_list = self.suit_rank_array[16]
        self.sevenks_list = self.suit_rank_array[17]
        self.eightks_list = self.suit_rank_array[18]
        self.nineks_list = self.suit_rank_array[19]
        self.tenks_list = self.suit_rank_array[20]
        self.singles = len(self.singles_list)
        self.pairs = len(self.pairs_list)
        self.trips = len(self.trips_list)
        self.fourks = len(self.fourks_list)
        self.fiveks = len(self.fiveks_list)
        self.sixks = len(self.sixks_list)
        self.sevenks = len(self.sevenks_list)
        self.eightks = len(self.eightks_list)
        self.nineks = len(self.nineks_list)
        self.tenks = len(self.tenks_list)
        self.ninekx_list = self.nineks_list + self.tenks_list
        self.eightkx_list = self.eightks_list + self.ninekx_list
        self.sevenkx_list = self.sevenks_list + self.eightkx_list
        self.sixkx_list = self.sixks_list + self.sevenkx_list
        self.fivekx_list = self.fiveks_list + self.sixkx_list
        self.fourkx_list = self.fourks_list + self.fivekx_list
        self.tripx_list = self.fourkx_list + self.trips_list
        self.five_card_straightflush = self.suit_rank_array[25]
        self.six_card_straightflush = self.suit_rank_array[26]
        self.seven_card_straightflush = self.suit_rank_array[27]
        self.eight_card_straightflush = self.suit_rank_array[28]
        self.nine_card_straightflush = self.suit_rank_array[29]
        self.ten_card_straightflush = self.suit_rank_array[30]
        self.five_card_hands()
        self.three_card_hands()

        return

    def five_card_hands(self):
        """ five_card_hands will find all possible high_hand's by hand type in order
            5K's, SF's, 4K's, FH's, Flushes', Straights', Trip's, 2Ps and P's.
            Includes hands with 6 cards and more
        """
        start_time = time.time()
        best_hand = PokerHand()

        self.hand5 = 2000 * [None]
        self.hand6 = 2000 * [None]
        self.high_hand = 2000 * [[]]
        flush_hand = 2000 * [[]]
        self.high_hand_score = []
        card_list2 = self.card_list

        hand_num = 0
        # create 10 of a kind
        for tenks in self.tenks_list:
            self.high_hand[hand_num] = tenks
            hand_num += 1

            # look to create 9k, 8k, ..., to 4k
            for x in range(9,3,-1):
                for xkind in list(combinations(tenks, x)):
                    self.high_hand[hand_num] = xkind
                    hand_num += 1

        if len(self.ten_card_straightflush) > 0:
            for cardx in self.ten_card_straightflush: # for each straight flush
                straight_flush_hand = []
                for i in range(10): # look for ten consecutive cards
                    suit_index = self.suits.index(cardx[0]) + 20
                    rank_index = self.straight_ranks.index(cardx[1]) + i
                    for cardy in reversed(self.suit_rank_array[suit_index]): # find matching card
                        if self.straight_ranks[rank_index] in cardy: # look for each card of straight flush
                            straight_flush_hand.append(cardy)
                            break
                self.high_hand[hand_num] = straight_flush_hand
                hand_num = hand_num + 1

        # create 9 of a kind
        for nineks in self.nineks_list:
            self.high_hand[hand_num] = nineks
            hand_num += 1

            # look to create 8k, 7k, ..., to 4k
            for x in range(8,3,-1):
                for xkind in list(combinations(nineks, x)):
                    self.high_hand[hand_num] = xkind
                    hand_num += 1


        for nineks in self.nineks_list:
            self.high_hand[hand_num] = nineks[0:3]
            hand_num += 1
            self.high_hand[hand_num] = nineks[3:6]
            hand_num += 1
            self.high_hand[hand_num] = nineks[6:9]
            hand_num += 1

        if len(self.five_card_straightflush) > 0:
            for cardx in self.nine_card_straightflush: # for each straight flush
                straight_flush_hand = []
                for i in range(9): # look for nine consecutive cards
                    suit_index = self.suits.index(cardx[0]) + 20
                    rank_index = self.straight_ranks.index(cardx[1]) + i
                    for cardy in reversed(self.suit_rank_array[suit_index]): # find matching card
                        if self.straight_ranks[rank_index] in cardy: # look for each card of straight flush
                            straight_flush_hand.append(cardy)
                            break
                self.high_hand[hand_num] = straight_flush_hand
                hand_num = hand_num + 1

        # each 8 of a kind
        for eightks in self.eightks_list:
            self.high_hand[hand_num] = eightks
            hand_num += 1

            # look to create 7k, 6k, ..., to 4k
            for x in range(7,3,-1):
                for xkind in list(combinations(eightks, x)):
                    self.high_hand[hand_num] = xkind
                    hand_num += 1

        if len(self.eight_card_straightflush) > 0:
            for cardx in self.eight_card_straightflush: # for each straight flush
                straight_flush_hand = []
                for i in range(8): # look for eight consecutive cards
                    suit_index = self.suits.index(cardx[0]) + 20
                    rank_index = self.straight_ranks.index(cardx[1]) + i
                    for cardy in reversed(self.suit_rank_array[suit_index]): # find matching card
                        if self.straight_ranks[rank_index] in cardy: # look for each card of straight flush
                            straight_flush_hand.append(cardy)
                            break
                self.high_hand[hand_num] = straight_flush_hand
                hand_num = hand_num + 1

        # create 7 of a kind
        for sevenks in self.sevenks_list:
            self.high_hand[hand_num] = sevenks
            hand_num += 1

            # look to create 6k, 5k, ..., to 4k
            for x in range(6,3,-1):
                for xkind in list(combinations(sevenks, x)):
                    self.high_hand[hand_num] = xkind
                    hand_num += 1

        if len(self.seven_card_straightflush) > 0:
            for cardx in self.seven_card_straightflush: # for each straight flush
                straight_flush_hand = []
                for i in range(7): # look for seven consecutive cards
                    suit_index = self.suits.index(cardx[0]) + 20
                    rank_index = self.straight_ranks.index(cardx[1]) + i
                    for cardy in reversed(self.suit_rank_array[suit_index]): # find matching card
                        if self.straight_ranks[rank_index] in cardy: # look for each card of straight flush
                            straight_flush_hand.append(cardy)
                            break
                self.high_hand[hand_num] = straight_flush_hand
                hand_num = hand_num + 1

        # create 6 of kinds
        for sixks in self.sixks_list:
            self.high_hand[hand_num] = sixks
            hand_num += 1

            # look to create 5k, 4k
            for x in range(5,3,-1):
                for xkind in list(combinations(sixks, x)):
                    self.high_hand[hand_num] = xkind
                    hand_num += 1

        if len(self.six_card_straightflush) > 0:
            # print "enter six card straight flush"
            for cardx in self.six_card_straightflush: # for each straight flush
                straight_flush_hand = []
                for i in range(6): # look for six consecutive cards
                    suit_index = self.suits.index(cardx[0]) + 20
                    rank_index = self.straight_ranks.index(cardx[1]) + i
                    for cardy in reversed(self.suit_rank_array[suit_index]): # find matching card
                        if self.straight_ranks[rank_index] in cardy: # look for each card of straight flush
                            straight_flush_hand.append(cardy)
                            break
                self.high_hand[hand_num] = straight_flush_hand
                hand_num = hand_num + 1

        # create 5 of kinds
        for fiveks in self.fiveks_list:
            self.high_hand[hand_num] = fiveks
            hand_num = hand_num + 1

            # create 4 of kinds
            for fourk in list(combinations(fiveks,4)):
                self.high_hand[hand_num] = fourk
                hand_num = hand_num + 1

        if len(self.five_card_straightflush) > 0:
            for cardx in self.five_card_straightflush: # for each straight flush
                straight_flush_hand = []
                for i in range(5): # look for five consecutive cards
                    suit_index = self.suits.index(cardx[0]) + 20
                    rank_index = self.straight_ranks.index(cardx[1]) + i
                    for cardy in reversed(self.suit_rank_array[suit_index]): # find matching card
                        if self.straight_ranks[rank_index] in cardy: # look for each card of straight flush
                            straight_flush_hand.append(cardy)
                            break
                self.high_hand[hand_num] = straight_flush_hand
                hand_num = hand_num + 1

        # find 4K hands
        for fourks in self.fourks_list:
            self.high_hand[hand_num] = fourks
            hand_num = hand_num + 1

        # for each hand, look for 3 specials which do not intersect
        special_hands = list(filter(None, self.high_hand))

        self.three_specials = False
        No_Flush_or_Straight = False
        No_Full_Houses = False

        if len(self.tripx_list) >=5 and len(self.pairs_list) >=2 \
                and len(special_hands) == 0:
            No_Flush_or_Straight = True

        # if len(self.fourkx_list) >= 3:
        #     No_Flush_or_Straight = True
        #     self.three_specials = True
        #     No_Full_Houses = True
        #     # print "3-4K ",
        # else:
        #     if len(special_hands) >= 3:
        #         combos = list(combinations(special_hands, 3))
        #         for hand1, hand2, hand3 in combos:
        #             hand1 = set(list(hand1))
        #             hand2 = set(list(hand2))
        #             hand3 = set(list(hand3))
        #             if hand1.intersection(hand2) == set([]):
        #                 if hand1.intersection(hand3) == set([]):
        #                     if hand2.intersection(hand3) == set([]):
        #                         No_Flush_or_Straight = True
        #                         No_Full_Houses = True
        #                         self.three_specials = True
        #                         # print "3-SF ",
        #                         break

        if not No_Full_Houses:
            # full houses with trips and pairs
            if self.trips >= 1 and self.pairs >=1:
                for trip in self.trips_list:
                    for pair in self.pairs_list:
                        self.high_hand[hand_num] = trip + pair
                        hand_num += 1

            # for each fourk, create 4 trips and add pairs to make full houses
            if self.fourks >= 1 and self.pairs >= 1:
                for fourk in self.fourks_list:
                    for trip in list(combinations(fourk,3)):
                        for pair in self.pairs_list:
                            self.high_hand[hand_num] = list(trip) + list(pair)
                            hand_num += 1

            # for each trip, create 3 pairs to potentially make full houses
            for trip1 in self.trips_list:
                for trip2 in self.trips_list:
                    if trip1 is not trip2:
                        for pair in list(combinations(trip2,2)):
                            self.high_hand[hand_num] = list(trip1) + list(pair)
                            hand_num += 1

        # flushes
        if not No_Flush_or_Straight:
            flush_num = 0
            for i in range(1, 5):  # cycle through self.suits
                if self.suit_rank_array[i][15] >= 5:
                    flush_hand[flush_num] = []
                    for card in card_list2:
                        if self.suits[i] == card[0]:
                            flush_hand[flush_num].append(card)

                for number in range(5, 16):
                    if len(flush_hand[flush_num]) == number:
                        temp = list(combinations(flush_hand[flush_num], 5))
                        for handy in temp:
                            flush_hand[flush_num] = handy
                            flush_num += 1
                            flush_hand[flush_num] = []

            for i in range(flush_num):
                self.high_hand[hand_num + i] = flush_hand[i][0:5]
            hand_num = hand_num + flush_num

            for j in [10,1,9,8,7,6,5,4,3,2]:  # straight
                if self.suit_rank_array[6][j] >= 1:
                    straight_card = [[],[],[],[],[]]
                    for k in range(5):
                        for card in card_list2:
                            if self.straight_ranks[j + k] in card:
                                straight_card[k].append(card)

                    for straight_hand in list(product(straight_card[0], straight_card[1],
                                                      straight_card[2], straight_card[3], straight_card[4])):
                        self.high_hand[hand_num] = straight_hand
                        hand_num = hand_num + 1

        # remove any hands that are empty
        self.high_hand = list(filter(None, self.high_hand))

        # make sure cards in all hands are sorted in rank_sort order
        if len(self.high_hand) > 0:
            for i in range(len(self.high_hand)):
                self.high_hand[i] = sorted(self.high_hand[i], key=rank_sort, reverse=True)

        # np_hand = np.array([self.high_hand], dtype="unicode")
        # print (np_hand.shape, np_hand.dtype)
        # print (np_hand)

        # for each hand, get the short_score
        for hand in self.high_hand:
            self.high_hand_score.append(PokerHand(hand).short_score)

        # now sort high_hand like high_hand_score as primary, then sort high_hand_score
        self.high_hand = [x for _,x in sorted(zip(self.high_hand_score, self.high_hand), reverse=True)]
        self.high_hand_score = sorted(self.high_hand_score, reverse=True)

        # for each high_hand, create self.hand6 and self.hand5
        for i in range(len(self.high_hand)):
            x = best_hand.get_points_from_hand(self.high_hand[i], "6")[1]
            y = best_hand.get_points_from_hand(self.high_hand[i], "5")[1]
            self.hand6[i] = [self.high_hand[i], self.high_hand_score[i], x]
            self.hand5[i] = [self.high_hand[i], self.high_hand_score[i], y]
            # print (self.hand6[i])
        self.hand5 = filter(None, self.hand5)
        self.hand6 = filter(None, self.hand6)
        end_time = time.time()
        elapse_time = end_time - start_time
        # print (" Legal Hands 5 card hands", round(elapse_time,2))
    def three_card_hands(self):
        """ three_card_hands will find all possible 3 card hands including special hands
        """
        # print "entering three_card_hands"
        suits = "WSHDC"
        ranks = "WA23456789TJQKA"
        start_time = time.time()

        best_hand = PokerHand()
        self.high_hand_points = [None] * 10000
        self.hand4 = [None] * 10000
        self.hand3 = [None] * 10000
        self.hand2 = [None] * 10000
        self.high_hand_score = []
        self.high_hand = 10000 * [[]]

        card_list2 = self.card_list

        # LegalHands cannot handle wild cards
        for card in card_list2:
            if card[0] == "W":
                print ("Error in three_card_hands(), cannot handle wild cards in LegalHands")
                return

        hand_num = 0

        # hand4 cannot be more than 5 cards

        # for each 6K create 6 5K's
        for sixks in self.sixks_list:
            for fivek in list(combinations(sixks, 5)):
                self.high_hand[hand_num] = fivek
                hand_num += 1

        # for each 6K create 15 4K's
        for sixks in self.sixks_list:
            for fourk in list(combinations(sixks, 4)):
                self.high_hand[hand_num] = fourk
                hand_num += 1

        # for each 6K, create 60 trips
        for sixk in self.sixks_list:
            for trip in list(combinations(sixk,3)):
                self.high_hand[hand_num] = trip
                hand_num += 1

        # for each fiveks, create 5K hands
        for handx in self.fiveks_list:
            self.high_hand[hand_num] = handx
            hand_num = hand_num + 1

        # for each fiveks, create 5 4K hands
        for handx in self.fiveks_list:
            for fourk in combinations(handx, 4):
                self.high_hand[hand_num] = fourk
                hand_num += 1

        # for each fivek, create 10 trips
        for fivek in self.fiveks_list:
            for trip in list(combinations(fivek,3)):
                self.high_hand[hand_num] = trip
                hand_num += 1

        if len(self.five_card_straightflush) > 0:
            for cardx in self.five_card_straightflush: # for each straight flush
                straight_flush_hand = []
                for i in range(5): # look for five consecutive cards
                    suit_index = self.suits.index(cardx[0]) + 20
                    rank_index = self.straight_ranks.index(cardx[1]) + i
                    for cardy in reversed(self.suit_rank_array[suit_index]): # find matching card
                        if self.straight_ranks[rank_index] in cardy: # look for each card of straight flush
                            straight_flush_hand.append(cardy)
                            break
                self.high_hand[hand_num] = straight_flush_hand
                hand_num = hand_num + 1

        # for each 4K, create 4K hands
        # find 4K hands
        for fourks in self.fourks_list:
            self.high_hand[hand_num] = fourks
            hand_num = hand_num + 1


        # for each fourk, create 4 trips
        for fourk in self.fourks_list:
            for trip in list(combinations(fourk,3)):
                self.high_hand[hand_num] = trip
                hand_num += 1

        for trip in self.trips_list:
            self.high_hand[hand_num] = trip
            hand_num += 1

        for pair in self.pairs_list:
            self.high_hand[hand_num] = pair
            hand_num += 1

        # for each trip, create 3 pairs
        for trip in self.trips_list:
            for pair in list(combinations(trip,2)):
                pair1_list = list(pair)
                self.high_hand[hand_num] = pair1_list
                hand_num += 1

        for single in self.singles_list:
            # print hand_num, single
            self.high_hand[hand_num] = [single]
            hand_num += 1


        # remove any hands that are empty
        self.high_hand = list(filter(None, self.high_hand))

        # make sure cards in hands are sorted in rank_sort order
        for i in range(len(self.high_hand)):
            self.high_hand[i] = sorted(self.high_hand[i], key=rank_sort, reverse=True)

        for hand in self.high_hand:
            if hand[0] == "W":
                print ("Error, cannot handle wild cards in LegalHands")
            self.high_hand_score.append(PokerHand(hand).short_score)
            # print "5 card hand, add short_score", hand, Hand(hand).short_score

        # sort high_hand like high_hand_score, then sort high_hand_score
        self.high_hand = [x for _, x in sorted(zip(self.high_hand_score, self.high_hand), reverse=True)]
        self.high_hand_score = sorted(self.high_hand_score, reverse=True)

        # for each high_hand, create self.hand4, self.hand3, self.hand2 with hand, points and points
        for i in range(len(self.high_hand)):
            x = best_hand.get_points_from_hand(self.high_hand[i], "4")[1]
            y = best_hand.get_points_from_hand(self.high_hand[i], "3")[1]
            z = best_hand.get_points_from_hand(self.high_hand[i], "2")[1]
            self.hand4[i] = (self.high_hand[i], self.high_hand_score[i], x)
            self.hand3[i] = (self.high_hand[i], self.high_hand_score[i], y)
            self.hand2[i] = (self.high_hand[i], self.high_hand_score[i], z)
            # print(self.high_hand[i], self.high_hand_score[i],x,y,z)
        # remove empty hands
        self.hand4 = list(filter(None, self.hand4))
        self.hand3 = list(filter(None, self.hand3))
        self.hand2 = list(filter(None, self.hand2))

        # determine self.hand1
        self.hand1 = []
        for i in range(len(card_list2)):
            self.hand1.append([card_list2[i]])

        for i in range(len(self.hand1)):
            y = best_hand.get_points_from_hand(self.hand1[i], "1")
            self.hand1[i] = self.hand1[i], y[0], y[1]

        # sort by self.hand1 points
        self.hand1.sort(key=lambda x: x[1], reverse=True)
        end_time = time.time()
        elapse_time = end_time - start_time
        # print ("  Legal Hands 3 card hand", round(elapse_time,2))
        return