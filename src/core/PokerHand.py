"""
PokerHand implements a different scoring algorithm for trips
that can represent 3 suits with two digits as follows:
This assumes the trip is sorted by suit

SSS=89
SSD=88
SSH=87
SSC=96
SHH=85
SHD-84
SHC=83
SDD-82
SDC=81
SCC=80

HHH=75
HHD=74
HHC=73
HDD=72
HDC=71
HCC=70

DDD=62
DDC=61
DCC=60

CCC=50

"""
import os

trip_dict = {
    "444": 89,
    "443": 88,
    "442": 87,
    "441": 86,
    "433": 85,
    "432": 84,
    "431": 83,
    "422": 82,
    "421": 81,
    "411": 80,
    "333": 75,
    "332": 74,
    "331": 73,
    "322": 72,
    "321": 71,
    "311": 70,
    "222": 62,
    "221": 61,
    "211": 60,
    "111": 50
}

trip_dict_inverted = {value: key for key, value in trip_dict.items()}

from enum import Enum
from src.core.Analysis import *
from src.core.Card import *
from src.core.ReadProbability import *
from src.core.CumulativeLearning import *
from src.core.sort_cards import *
# from src.core.WriteProb import *
import pickle
#
# import ReadKeyValuesProb
ranks = "W123456789TJQKA"
suits = "WCDHS"
first = True

class HandType(Enum):
    TenK = 20
    TenSF = 19
    NineK = 18
    NineSF = 17
    EightK = 16
    EightSF = 15
    SevenK = 14
    SevenSF = 13
    SixK = 12
    SixSF = 11
    FiveK = 10
    FiveSF = 9
    FourK = 8
    FullH = 7
    Flush = 6
    Straight = 5
    Trip = 4
    TwoPair = 3
    OnePair = 2
    HighCard = 1


class PokerHand():
    """ represents a n-card hand - calculates various attributes """

    def __init__(self, hand = ["SA+"]):
        """ initializes object with hand, suit_rank_array, hand_type
        hand_type_value and hand_score"""
        descriptions = ["NA", "High Card", "1 Pair", "2 Pair", "Trip",
                        "Straight", "Flush", "Full House", "4 of a Kind"
                        "Straight Flush", "5 of a Kind", " 6 Card SF", "6 of a Kind",
                        " 7 Card SF", "7 of a Kind"," 8 Card SF", "8 of a Kind",
                        " 9 Card SF", "9 of a Kind"," 10 Card SF", "10 of a Kind", "error"]

        self.analysis = Analysis(hand) #run Analysis on hand
        # print hand
        # for i in range(44):
        #     print self.suit_rank_array[i]
        self.get_hand_type_value()
        # self.hand_value = self.hand_type_value
        # print (self.hand_type_value)
        # self.hand_desc = descriptions[self.hand_type_value]

        # choice is to add char instead of numbers
        self.card_list = hand
        self.get_hand_score(hand)
        self.get_hand_key_values()
        # self.suit_rank_array = self.analysis.suit_rank_array

    def get_hand_type_value(self):
        """ given hand, it returns hand_type_value and hand_type"""
        if self.analysis.tenks > 0:
            self.hand_type_value = 20
        elif len(self.analysis.ten_card_straightflush) >= 1:
            self.hand_type_value = 19
        elif self.analysis.nineks > 0:
            self.hand_type_value = 18
        elif len(self.analysis.nine_card_straightflush) >= 1:
            self.hand_type_value = 17
        elif self.analysis.eightks > 0:
            self.hand_type_value = 16
        elif len(self.analysis.eight_card_straightflush) >= 1:
            self.hand_type_value = 15
        elif self.analysis.sevenks > 0:
            self.hand_type_value = 14
        elif len(self.analysis.seven_card_straightflush) >= 1:
            self.hand_type_value = 13
        elif self.analysis.sixks > 0:
            self.hand_type_value = 12
        elif len(self.analysis.six_card_straightflush) >= 1:
            self.hand_type_value = 11
        elif self.analysis.fiveks > 0:
            self.hand_type_value = 10
        elif len(self.analysis.five_card_straightflush) >= 1:
            self.hand_type_value = 9
        elif self.analysis.fourks > 0:
            self.hand_type_value = 8
        elif self.analysis.trips > 0 and self.analysis.pairs >= 1:
            self.hand_type_value = 7
        elif self.analysis.flushes > 0:
            self.hand_type_value = 6
        elif self.analysis.straights > 0:
            self.hand_type_value = 5
        elif self.analysis.trips > 0 and self.analysis.pairs == 0:
            self.hand_type_value = 4
        elif self.analysis.pairs > 1:
            self.hand_type_value = 3
        elif self.analysis.pairs == 1:
            self.hand_type_value = 2
        elif self.analysis.singles == 1:
            self.hand_type_value = 1
        else:
            self.hand_type_value = 1
        return self.hand_type_value
        # return self.hand_type_value

    def get_hand_key_values(self):
        kicker_rank = []
        kicker_suit = []
        self.hand_key_rank_value = []
        self.hand_key_suit_value = []

        # default rank and suit values based on card_list sorted
        # this is good for HC, Trip, Straight, Flush 5K, 5SF, etc.

        #
        for card in self.card_list:
            self.hand_key_rank_value.append(Card(card).rank_value)
            self.hand_key_suit_value.append(Card(card).suit_value)

        # print (self.card_list)
        # print ("ranks", self.hand_key_rank_value)
        # print ("suits", self.hand_key_suit_value)
        # print (self.card_list, self.hand_type_value)
        # for straight flushes and flush, only one hand_key_suit_value needed

        if (self.hand_type_value == 6):
            self.hand_key_suit_value = [self.hand_key_suit_value[0]]

        # if straight flush, only need first rank and first suit
        if (self.hand_type_value == 9 or
            self.hand_type_value == 11 or
            self.hand_type_value == 13 or
            self.hand_type_value == 15 or
            self.hand_type_value == 17 or
            self.hand_type_value == 19):
            self.hand_key_rank_value = [self.hand_key_rank_value[0]]
            self.hand_key_suit_value = [self.hand_key_suit_value[0]]

        # For 8, 9 and 10 of kind, suits are not necessary
        # only 12 of each card plus 3 wild cards means that suits not nececesary
        # if player 1 has 10 8's, the other person can only have 5 8's so rank wins
        if (self.hand_type_value == 16 or
            self.hand_type_value == 18 or
            self.hand_type_value == 20):
            self.hand_key_suit_value = []

        # for 3K, Straight, 5K, 5SF, 6K, etc., only need first rank
        if (self.hand_type_value == 4 or
            self.hand_type_value == 5 or
                self.hand_type_value >= 10):
            self.hand_key_rank_value = [self.hand_key_rank_value[0]]

        # default sort does not work for following hands
        # Pair, 2 Pair, 4K - because of kickers
        # House - because of Trip, then Pair

        if self.hand_type_value == 2:   # Pair
            pair_rank = [ranks.index(self.analysis.pairs_ranks[0])]
            pair_suits = [suits.index(self.analysis.pairs_list[0][0][0]),
                          suits.index(self.analysis.pairs_list[0][1][0])]
            if len(self.analysis.singles_list) > 0:
                kicker_rank = [ranks.index(self.analysis.singles_ranks[0])]
                kicker_suit = [suits.index(self.analysis.singles_list[0][0])]
            self.hand_key_rank_value = pair_rank + kicker_rank
            self.hand_key_suit_value = pair_suits + kicker_suit

        elif self.hand_type_value == 3:    # 2 Pair
            pair1_rank = [ranks.index(self.analysis.pairs_ranks[0])]
            pair2_rank = [ranks.index(self.analysis.pairs_ranks[1])]
            pair1_suits = [suits.index(self.analysis.pairs_list[0][0][0])] +\
                          [suits.index(self.analysis.pairs_list[0][1][0])]

            pair2_suits = [suits.index(self.analysis.pairs_list[1][0][0])] +\
                          [suits.index(self.analysis.pairs_list[1][1][0])]

            kicker_rank = [ranks.index(self.analysis.singles_list[0][1])]
            kicker_suit = [suits.index(self.analysis.singles_list[0][0])]

            self.hand_key_rank_value = pair1_rank + pair2_rank + kicker_rank
            self.hand_key_suit_value = pair1_suits + pair2_suits + kicker_suit

        if self.hand_type_value == 7:  # Full House
            trip_rank  = [ranks.index(self.analysis.trips_ranks[0])]
            trip_suits = [suits.index(self.analysis.trips_list[0][0][0]),
                          suits.index(self.analysis.trips_list[0][1][0]),
                          suits.index(self.analysis.trips_list[0][2][0])]
            pair_rank = [ranks.index(self.analysis.pairs_ranks[0])]
            pair_suits = [suits.index(self.analysis.pairs_list[0][0][0]),
                          suits.index(self.analysis.pairs_list[0][1][0])]
            self.hand_key_rank_value = trip_rank + pair_rank
            self.hand_key_suit_value = trip_suits + pair_suits

        if self.hand_type_value == 8:   # 4K
            fourks_rank = [ranks.index(self.analysis.fourks_ranks[0])]
            fourks_suits = [suits.index(self.analysis.fourks_list[0][0][0]),
                          suits.index(self.analysis.fourks_list[0][1][0]),
                          suits.index(self.analysis.fourks_list[0][2][0]),
                          suits.index(self.analysis.fourks_list[0][3][0])]
            if len(self.analysis.singles_ranks) == 0:
                pass
            else:
                kicker_rank = [ranks.index(self.analysis.singles_ranks[0][0])]
                kicker_suit = [suits.index(self.analysis.singles_list[0][0])]

            self.hand_key_rank_value = fourks_rank + kicker_rank
            self.hand_key_suit_value = fourks_suits + kicker_suit

        self.hand_key_values = [self.hand_type_value] + self.hand_key_rank_value + self.hand_key_suit_value
        place = 10
        hand_key = self.hand_type_value * 10**place
        hand_rank_key = 0
        hand_suit_key = 0

        place = place - 2
        for val in self.hand_key_rank_value:
            hand_rank_key += val * 10**place
            place = place - 2

        place += 1
        for val in self.hand_key_suit_value:
            hand_suit_key += val * 10**place
            place = place - 1

        self.final_hand_key = int(hand_key + hand_rank_key + hand_suit_key)

        # if self.hand_type_value != 7 and self.hand_type_value != 5 and self.hand_type_value != 6:
        #     print (hand_key, hand_rank_key, hand_suit_key, final_hand_key)

        # print ("ranks", self.hand_key_rank_value, "suits", self.hand_key_suit_value)
        # print (self.hand_key_values, len(self.hand_key_values))
        return

    def get_hand_type(self):
        return(HandType(self.hand_type_value))

    def get_hand_score(self, hand):
        """ Given hand, return self.points - hand_score
            plus two digits for each of 5 cards for 11 or 12 digits,
            Also returns self.short_score for compatibility 5 or 6 digits
            """
        suits = "WCDHS"
        ranks = "0123456789TJQKA"
        # value of five cards - cards sorted by Rank then Suit from High to Low
        self.hand = sorted(hand, key=rank_sort, reverse=True)   # not needed
        # if len(self.hand) == 3: print ("sorted", self.hand)
        self.score = 0
        # i is the card index, example - self.score for 81413000000 = 4 Aces with king kicker
        # two digits per card up to 10 cards
        for i in range(len(hand)):
            self.score += ranks.index(self.hand[i][1]) * 100 ** (len(hand) - 1 - i)

        # short_score is value with last 3 card values (6 digits)truncated for SF, Flush and Straight and High Card
        # short_score for 81413000000 is 81413 (last 6 digits truncated)
        self.short_score = self.score // 1000000

        self.score = str(self.hand_type_value) + str(self.score)
        # print (str(self.hand_type_value))

        # short_score needs to be changed for 5K, 4K, Full House, 4K, Trip, Two Pair and Pair
        if self.hand_type_value == 6: # Flush
            self.short_score = 60000 + ranks.index(self.hand[0][1]) * 100 + ranks.index(self.hand[1][1])
            self.short_score_plus = int(self.score) + ranks.index(self.hand[0][1]) * 1000000 + \
                    ranks.index(self.hand[1][1]) * 10000 + ranks.index(self.hand[2][1]) * 100 + ranks.index(self.hand[3][1]) * 1
        elif self.hand_type_value == 7:  # House
            self.short_score = 70000 + ranks.index(self.analysis.trips_ranks[0]) * 100 + ranks.index(self.analysis.pairs_ranks[0])
        elif self.hand_type_value == 5:   # Straight
            self.short_score = 50000 + ranks.index(self.hand[0][1]) * 100 + ranks.index(self.hand[1][1])


        # elif self.hand_type_value == 4:   # Trip
        #     if self.analysis.singles > 0:
        #         self.short_score = 40000 + ranks.index(self.analysis.trips_ranks[0]) * 100 + (ranks.index(self.analysis.singles_ranks[0])+50)
        #     else:
        #         # for trips, short value = hand_type_value concat trip_value concat suit1_suit2
        #         # need to make trip with kicker 50 higher to make it larger than suit1_suit2
        #         self.short_score = 40000 + ranks.index(self.analysis.trips_ranks[0]) * 100 + \
        #                            (suits.index(self.hand[0][0])) * 10 + (suits.index(self.hand[1][0]))

        elif self.hand_type_value == 4:   # Trip
            if self.analysis.singles > 0:
                self.short_score = 40000 + ranks.index(self.analysis.trips_ranks[0]) * 100 + (ranks.index(self.analysis.singles_ranks[0])+50)
            else:
                # for trips, short value = hand_type_value concat trip_value concat suit1_suit2
                # need to make trip with kicker 50 higher to make it larger than suit1_suit2
                self.hand = sorted(hand, key=rank_sort, reverse=True)
                # determine the suits of the three cards
                trip_suits = str(suits.index(self.hand[0][0])) + str(suits.index(self.hand[1][0])) + str(suits.index(self.hand[2][0]))

                for i in range(2):
                    if suits.index(self.hand[i][0]) < suits.index(self.hand[i+1][0]):
                        print (self.hand, "FATAL ERROR in PokerHand trip_suits not sorted",trip_suits)
                        # why are suits it 341 when it should be 441
                        # let's fix it.
                        trip_suits = str(4) + str(suits.index(self.hand[0][0])) + str(suits.index(self.hand[2][0]))
                        print ("fixed trip"
                               "_suits", trip_suits)
                new_trip_suits = trip_dict[trip_suits]
                self.short_score = 40000 + ranks.index(self.analysis.trips_ranks[0]) * 100 + new_trip_suits

        elif self.hand_type_value == 3:    # 2 Pair
            self.short_score = 30000 + ranks.index(self.analysis.pairs_ranks[0]) * 100 + ranks.index(self.analysis.pairs_ranks[1])
        elif self.hand_type_value == 2:    # 1 Pair
            if self.analysis.singles > 0:
                self.short_score = 20000 + ranks.index(self.analysis.pairs_ranks[0]) * 100 + ranks.index(self.analysis.singles_ranks[0])
            else:
                self.short_score = 20000 + ranks.index(self.analysis.pairs_ranks[0]) * 100
        elif self.hand_type_value == 1:     # High Card
            if len(self.analysis.singles_ranks) >= 2:
                self.short_score = 10000 + ranks.index(self.hand[0][1]) * 100 + ranks.index(self.hand[1][1])
            elif len(self.analysis.singles_ranks) == 1:
                self.short_score = 10000 + ranks.index(self.hand[0][1]) * 100 + suits.index(self.hand[0][0])
            elif len(self.analysis.singles_ranks) == 0:
                self.short_score = 10000
                # self.short_score = 10000
        elif len(self.hand) == 0:
            self.short_score = 10000
        elif self.hand_type_value == 8:   # four of kind
            if self.analysis.singles > 0:  # kicker
                self.short_score = 80000 + ranks.index(self.analysis.fourks_ranks[0]) * 100 + \
                                   ranks.index(self.analysis.singles_ranks[0])
            else:
                self.short_score = 80000 + ranks.index(self.analysis.fourks_ranks[0]) * 100 # no kicker
        elif self.hand_type_value in [9,11,13,15,17,19]:

            # self.short_score = self.hand_type_value * 10000
            self.short_score = self.hand_type_value * 10000 + ranks.index(self.hand[0][1]) * 100 + ranks.index(self.hand[1][1])
        elif self.hand_type_value in [10,12,14,16,18,20]:
            self.short_score = self.hand_type_value * 10000 + ranks.index(self.hand[0][1]) * 100
        return

    def get_points_from_hand(self, card_list, hand):
        # try:
        new_hand = PokerHand(card_list)
        self.score = new_hand.short_score
        self.points = self.get_points_from_score(self.score, hand)
        self.points  = round(self.points, 4)
        # except:
        #     self.points = 0
        #     self.points = 0
        return [self.score, self.points]

    def get_winpoints_from_hand(self, handx, hand):
        new_hand = PokerHand(handx)
        self.score = new_hand.short_score
        self.points = self.get_winpoints_from_score(self.score, hand)
        self.points  = round(self.points, 2)
        return (self.score, self.points)

    def get_points_from_score(self, score, hand):
        """ given 1-5 cards, returns initial points and prob depending on hand number(1-6)"""
        #  print "points, hand", points, hand
        prob = self.get_hand_prob(score, hand)
        # print (score, hand, prob)
        # points matrix uses same points when there are too many cards for that hand
        # each row is a hand starting from row 1 to row 6
        # each element is points won depending on hand_type_value which is 1-20 as follows:
        # high card, 1 pair, 2 pair, trip, str, flush, fh, 4k, sf, 5k, 6sf, 6k, 7sf, 7k, 8sf, 8k, 9sf, 9k, 10sf, 10k
        points_matrix = ([0],
                         [0, 1],
                         [0, 1, 1, 1, 9, 0, 0, 0, 20, 25, 30, 40, 40],
                         [0, 1, 1, 1, 6, 0, 0, 0, 16, 20, 24, 32, 40],
                         [0, 1, 1, 1, 3, 0, 0, 0, 12, 15, 18, 24, 30, 30, 30],
                         [0, 1, 1, 1, 1, 1, 1, 2,  8, 10, 12, 16, 20, 22, 28, 28, 28, 28, 28, 28, 28],
                         [0, 1, 1, 1, 1, 1, 1, 1,  4,  5,  6,  8, 10, 11, 14, 14, 18, 17, 22, 20, 26])

        # prob_of_loss_array is probability of winning by each hand type value)
        # example: hand 2 - prob of loss 1 point is 45%, prob of loss 9 points is 55%
        #          hand 3 - prob of loss 1 point is 23%, prob of loss 6 points is 67%
        #          hand 4 - prob of loss 1 point is 7%, prob of loss 3 points is 64%, prob of loss 12 points is 14%, prob of loss 15 points is 15%
        #          hand 5 - prob of loss 1 point is 7%, prob of loss 3 points is 64%, prob of loss 12 points is 14%, prob of loss 15 points is 15%,
        #          hand 6 - prob of loss 1 point is 39%, prob of loss 4 points is 26%, prob of loss 5 points is 10%,
        #                   prob of loss 6 points is 16%, prob of loss 8 is 3%, prob of loss 10 3%, prob of loss 11, 14, 14 is 1% each
        loss_points_array = (0,      [1,1],    [1,9],     [1,6],     [1,3,12,15],        [1,2,8,10,12,20],            [1, 4, 5,   6,  8, 10,  11, 14, 14])
        prob_of_loss_array = (0,     [0,0],    [44,56],   [23,67],   [7, 77, 15.7,  .3], [44.5,17.5, 32, 3, 2.6,.3], [38,26,10,16.4,3.8,3.5, 1.2, .6, .5])
        cum_prob_of_loss_array = (0, [0, 100], [45, 100], [23, 100], [7, 84, 99.7, 100], [44.5,  62, 94, 97, 99.6, 100],
                                [38, 64, 74, 90.4, 94.2, 97.7, 98.9, 99.5, 100])
        expected_loss_points_array = [0,[0,0],[0,0],[0,0],[0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

        for i in range(1, 7):
            for j in range(0,len(loss_points_array[i])):
                expected_loss_points_array[i][j] = round(loss_points_array[i][j] * prob_of_loss_array[i][j],3)
        hand_type_value = int(score/10000)
        hand_number = int(hand)

        # win_points depends on hand_number,hand_type_value - ie. 4th hand, 4K (8th value) is 12 points
        # 5th hand 4K is 8 points
        # print ("debug1", hand_number, hand_type_value)
        win_points = points_matrix[hand_number][hand_type_value]
        positive_points = round(win_points * prob,3)
        loss_points = win_points

        # find index in loss_points_array
        index = 0
        for i,n in enumerate(loss_points_array[hand_number]):
            if loss_points == n:
                index = i
                break

        # find negative_points
        if hand_number == 1:
            negative_points = round(100 - prob, 3)

        else:
            negative_points = 0
            prob_of_loss = 0
            for i in range(index, len(loss_points_array[hand_number])):
                if i == index:
                    prob_of_loss += cum_prob_of_loss_array[hand_number][i] - prob
                    negative_points += prob_of_loss * loss_points
                    # print i, prob_of_loss, loss_points, negative_points
                else:
                    negative_points += loss_points_array[hand_number][i] * prob_of_loss_array[hand_number][i]
                    # print i, prob_of_loss_array[hand_number][i], loss_points_array[hand_number][i], negative_points
        # negative_points = max(0,round(negative_points,2))
        negative_points = round(negative_points,2)
        net_points = positive_points - negative_points
        # if win_points > 11:
        #     net_points = 3 * net_points
        points = round(net_points, 3)

        # calculate negative_points2 using expected_loss_points_array

        if hand_number == 1:
            negative_points2 = round(100 - prob, 3)

        else:
            negative_points2 = 0
            prob_of_loss = 0
            for i in range(index, len(loss_points_array[hand_number])):
                if i == index:
                    prob_of_loss += cum_prob_of_loss_array[hand_number][i] - prob
                    negative_points2 += prob_of_loss * loss_points
                    # print i, prob_of_loss, loss_points, negative_points
                else:
                    negative_points2 += expected_loss_points_array[hand_number][i]
        negative_points2 = round(negative_points2, 3)
        points2 = round(positive_points - negative_points2, 3)
        # points = positive_points
        self.score = score
        self.points = points
        # print ("v1 points", hand, score, positive_points, negative_points * -1, points)
        # print ("v2 points", hand, score, positive_points, negative_points2 * -1, points2)
        # print ("points, hand, pr ("v1 points", hand, score, positive_points, negative_points * -1, points)ob, points, pos, neg", points, hand, prob, win_points, positive_points, negative_points)

        # print ("-- Score: {0:>9}, Hand: {1:>7}, Prob: {2:>7}, Points: {3:>7}, Positive: {4:>7}, Negative: {5:>7}, Expected Value: {6:>7}"\
        #    .format(points, hand, prob, win_points, positive_points, negative_points))
        return (points)

    def get_winpoints_from_score(self, score, hand):
        """ given points, returns win_points depending hand 1,2,3,4,5,6"""
        # points matrix uses same points when there are too many cards for that hand
        points_matrix = [[0],
                         [0, 1],
                         [0, 1, 1, 1, 9, 0, 0, 0, 20, 25, 30, 40, 40],
                         [0, 1, 1, 1, 6, 0, 0, 0, 16, 20, 24, 32, 32],
                         [0, 1, 1, 1, 3, 0, 0, 0, 12, 15, 18, 24, 30, 30],
                         [0, 1, 1, 1, 1, 1, 1, 2,  8, 10, 12, 16, 20, 20, 20],
                         [0, 1, 1, 1, 1, 1, 1, 1,  4,  5,  6,  8, 10, 11, 14, 14, 18, 17, 22, 20, 26]]

        score_int = int(score/10000)
        hand_number = int(hand)
        win_points = round(points_matrix[hand_number][score_int], 2)
        self.score = score
        self.points = win_points
        return(int(win_points))

    def get_hand_prob(self, score, hand):


        global first
        global prob_dictionary
        global ProbabilityFile
        global keycount, patterncount, score_dict, update_count
        prob_dictionary = True
        if first == True:
            if prob_dictionary:
                # print ("loading pickle data")
                # print (os.getcwd())
                file = open("prob_dictionary", "rb")
                score_dict = pickle.load(file)
                # still need to figure out best way to use keyval_dict
                # file1 = open("keyval_dictionary", "rb")
                # keyval_dict = pickle.load(file1)
            else:
                CumulativeLearning()
                print ('running cumulative learning')
                ProbabilityFile = ReadProbability()
            first = False
            keycount = 0
            update_count = 0
            patterncount = 0

        self.hand = hand
        self.score = score

        # score_dict is dictionary which stores "points" and "probability"
        if prob_dictionary:
            pass
        else:
            score_dict = ProbabilityFile.score_prob

        if score >= 100000:
            key = hand + str(score)
        else: key = hand + "0" + str(score)

        if key in score_dict:  # if found in dictionary
            prob = score_dict[key]
            # keycount += 1
            # print (key, "key found", "keycount:", keycount)
        else:    # if not found, then we need to use wild card search
            for i in range(1,7,1):
                # we need to go from 8 chars to 7 chars and a ".", etc
                key_start = key[0:(7-i)]
                key_end = str(i * ".")
                pattern = key_start + key_end
                patterncount += 1
                # print (key, "key not found, searching pattern", pattern, "patterncount:", patterncount)
                prob_pattern = tuple(score_dict.find(pattern))
                if prob_pattern:
                    prob = min(prob_pattern)
                    new = {key : prob}
                    # print (new, end="")
                    score_dict.update(new)   # add to dictionary
                    update_count += 1
                    if update_count >0:
                        # print("     A new points is found", update_count, key, prob)
                        file = open("prob_dictionary", "wb")
                        pickle.dump(score_dict, file)
                        file.close()
                        # WriteProb(score_dict)
                    # print ("pattern:", pattern, "found")
                    break
                else:
                    prob = .0000001
        self.prob = round(prob,5)
        # print ("score, hand, prob", score, hand, prob)
        # print ("keycount, patterncount", keycount, patterncount)
        return prob

    def get_six_hands_points(self, list_of_hands):
        hand_score = [0,0,0,0,0,0,0]
        hand_score[6] = self.get_points_from_hand(list_of_hands[6], "6")
        hand_score[5] = self.get_points_from_hand(list_of_hands[5], "5")
        hand_score[4] = self.get_points_from_hand(list_of_hands[4], "4")
        hand_score[3] = self.get_points_from_hand(list_of_hands[3], "3")
        hand_score[2] = self.get_points_from_hand(list_of_hands[2], "2")
        hand_score[1] = self.get_points_from_hand(list_of_hands[1], "1")

        for i in range (1,7):
            # print (list_of_hands[i], hand_score[i]),
            hand_score[0] = hand_score[0] + hand_score[i][1]
        hand_score[0] = round(hand_score[0],2)
        # print ("get_six_hands_points", hand_score)
        # print
        return (hand_score)

    def get_description_from_score(self,score, hand_num):

        hand_string = ['', '', 'Pair', 'TwoP', 'Trip', 'Straight',
                       'Flush', 'FullH', 'Four', 'FiveSF', 'Five', 'SixSF',
                       'Six', 'SevenSF', 'Seven', 'EightSF', 'Eight', 'NineSF',
                       'Nine', 'TenSF', 'Ten']
        handtype = int(score / 10000)
        card_rank = int((score - handtype * 10000) / 100)
        card_rank_string = ranks[card_rank]
        card_suit = score - card_rank * 100 - handtype * 10000
        card_suit_string = ""
        if handtype == 1 and hand_num == '1':
            if int(card_suit) > 4 or int(card_suit) <1:
                print ("error card suit out of range", score, hand_num, int(card_suit))
            else:
                card_suit_string = suits[int(card_suit)]
        elif handtype == 1 and hand_num != 1:
            card_suit_string = " "
        elif handtype == 4:

            # needs to be redone based on how trips are represented
            # card1 suit
            # card2 suit
            original_card_suit = trip_dict_inverted[card_suit]
            card1_suit = int(original_card_suit[0])
            card2_suit = int(original_card_suit[1])
            card3_suit = int(original_card_suit[2])
            card_suit_string = suits[card1_suit] + suits[card2_suit] + suits[card3_suit]+" "
            # print ("suits of trips",suits[card1_suit], suits[card2_suit])

        handtype_string = hand_string[handtype] + " " + card_rank_string + " " + card_suit_string + " "

        # print (card_suit_string, card_rank_string)

        return (handtype_string)