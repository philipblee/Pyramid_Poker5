from src.core.LegalPokerHands import *
import time
from src.core.PokerHand import *
import logging
import src.core.global_variables as global_variables
from src.core.sort_cards import *

logging.basicConfig(filename="../core/output.txt", format='%levelname)s:%(message)s', level=logging.ERROR)
logging.debug("This is a debug level message")

class BestHand25:

    def __init__(self, pyramid_poker_list, best_points_so_far):

        best_scores = []
        pyramid_poker_list = sorted(pyramid_poker_list, reverse=True, key=rank_sort)
        # print pyramid_poker_list
        best_points_total = best_points_so_far
        my_hand = LegalPokerHands(pyramid_poker_list)
        best_pyramid_poker_hand = []
        hand6 = list(my_hand.hand6)
        hand4 = list(my_hand.hand4)
        hand3 = list(my_hand.hand3)
        hand2 = list(my_hand.hand2)
        hand5 = list(my_hand.hand5)
        hand1 = list(my_hand.hand1)

        self.hand6_count = hand6_count = my_hand.hand6_count
        self.hand5_count = hand5_count = my_hand.hand5_count
        self.hand4_count = hand4_count = my_hand.hand4_count
        self.hand3_count = hand3_count = my_hand.hand3_count
        self.hand2_count = hand2_count = my_hand.hand2_count
        self.hand1_count = hand1_count = my_hand.hand1_count

        # print (hand6_count, hand4_count)

        a_count = 0; ab_count = 0; abc_count = 0
        abcd_count = 0; abcde_count = 0; abcdef_count = 0

        print ("hand6")
        for i in range(hand6_count):
            print (hand6[i])
        print ("hand5")
        for i in range(hand5_count):
            print (hand5[i])
        print ("hand4")
        for i in range(hand4_count):
            print (hand4[i])
        print ("hand3")
        for i in range(hand3_count):
            print (hand3[i])
        print ("hand2")
        for i in range(hand2_count):
            print (hand2[i])
        print ("hand1")
        for i in range(hand1_count):
            print (hand1[i])

        six_hands = PokerHand()
        print ("-- Hands {0:>4} {1:>4} {2:>3} {3:>3} {4:>3} {5:>3}".format(hand6_count,
                    hand5_count, hand4_count, hand3_count, hand2_count, hand1_count),end="")
        print
        best_hand_count = 0; count = 0; count_try = 0
        count_union = 0; count_intersect = 0
        begin_time = time.time()

        # adjust cushion based on whether hands needs fills or not
        cards_in_max_hand6 = len(hand6[0][0])
        cards_in_max_hand5 = len(hand5[1][0])
        cards_in_max_hand4 = len(hand4[0][0])

        max_hand6_cushion = 0; max_hand4_cushion = 0; max_hand5_cushion = 0
        if cards_in_max_hand6 == 4:
            max_hand4_cushion = 40
        if cards_in_max_hand5 == 4:
            max_hand5_cushion = 40
        if cards_in_max_hand4 == 4:
            max_hand6_cushion = 20
        # remember hand6 and 5 are the same and hand4, 3, 2 are the same
        max_hand1 = hand1[0][2]
        max_hand2 = max_hand1 + hand2[2][2]
        max_hand3 = max_hand2 + hand3[1][2]
        max_hand4 = max_hand3 + hand4[0][2]
        max_hand5 = max_hand4 + hand5[1][2]
        best_points_possible = (hand6[0][2] + max_hand5)

        # cushion adjusts when "potential hands" are considered futile and abandoned based on best_points_possible
        # however best_points_total are hands that are filled; best_points_possible do not include fills. cushion compensates for that
        # hand1's have no fill - hand6, hand5 and hand4 have fills, they have 4 cards - 40 points per fill
        cushion = max_hand4_cushion + max_hand5_cushion + max_hand6_cushion + 15

        # print("   ", max_hand1, max_hand2, max_hand3, max_hand4, max_hand5)

        if best_points_possible + cushion > best_points_total:
            for i in range(hand6_count):
                # print ("hand 1 - i", i)
                count_try += 1
                a_count += 1
                a = set(hand6[i][0])
                h6 = hand6[i][1]
                h6_points = hand6[i][2]
                # print ("hand 6", a, h6, h6_points)
                best_points_possible = (h6_points + max_hand5)
                if best_points_possible + cushion > best_points_total:
                    for j in range(i+1, hand5_count):
                        # print("hand 2 - j", j)
                        b = set(hand5[j][0])
                        h5 = hand5[j][1]
                        h5_points = hand5[j][2]
                        best_points_possible = (h6_points + h5_points + max_hand4)
                        count_intersect += 1
                        # print ("best possible", round(best_points_possible), "best points so far", round(best_points_total), "hand6/hand5/max_hand4", h6_points, h5_points, round(max_hand4))
                        if best_points_possible + cushion < best_points_total: break
                        if h6 >= h5 and a.isdisjoint(b):
                            ab_count += 1
                            count_try += 1
                            for k in range(hand4_count):
                                count_union += 1
                                ab = a.union(b)
                                c = set(hand4[k][0])
                                h4 = hand4[k][1]
                                h4_points = hand4[k][2]
                                # given points for h6, h5 and h4, add highest h3, h2, h1 to see if this hand is hopeless
                                best_points_possible = (h6_points + h5_points + h4_points + max_hand3)
                                count_intersect += 1
                                if best_points_total > best_points_possible: break  # loses 1 second
                                if h5 >= h4 and ab.isdisjoint(c):  # and best_points_possible + cushion > best_points_total:
                                    abc_count += 1
                                    count_try += 1
                                    count_union += 1
                                    abc = ab.union(c)
                                    for l in range(k+1, hand3_count):
                                        d = set(hand3[l][0])
                                        h3 = hand3[l][1]
                                        h3_points = hand3[l][2]
                                        best_points_possible = (h6_points + h5_points + h4_points + h3_points + max_hand2)
                                        count_intersect += 1
                                        # print("before d", b, c, d, "h5, h4, h3", h5, h4, h3,
                                        #       "best possible, best total", best_points_possible+cushion, best_points_total)
                                        if best_points_total > best_points_possible + cushion: break # improves 1 second
                                        if h4 >= h3 and abc.isdisjoint(d):    # and best_points_possible > best_points_total:
                                            # abc_count += 1
                                            abcd_count += 1
                                            count_try += 1
                                            for m in range(l+1, hand2_count):
                                                e = set(hand2[m][0])
                                                h2 = hand2[m][1]
                                                h2_points = hand2[m][2]
                                                count_union = + 1
                                                abcd = abc.union(d)
                                                best_points_possible = h6_points + h5_points + h4_points + h3_points + h2_points + max_hand1
                                                count_intersect += 1
                                                # print("before e", c, d, e, "h4, h3, h2", h4, h3, h2, "best possible, best total",
                                                #       best_points_possible + cushion, best_points_total)
                                                if best_points_total > best_points_possible + cushion: break # improves 2 seconds
                                                if h3 >= h2 and e.isdisjoint(abcd):
                                                    abcde_count += 1
                                                    count_try += 1
                                                    count_union += 1
                                                    abcde = abcd.union(e)
                                                    for n in range(hand1_count):
                                                        f = set(hand1[n][0])
                                                        h1 = hand1[n][1]
                                                        h1_points = hand1[n][2]
                                                        best_points_possible = (h6_points + h5_points + h4_points + h3_points + h2_points + h1_points)
                                                        count_intersect += 1
                                                        # print ("before f", d, e, f, "h3, h2, h1", h3, h2, h1, "best possible, best total", best_points_possible+cushion, best_points_total)
                                                        if best_points_total > best_points_possible + cushion: break
                                                        if h2 >= h1 and f.isdisjoint(abcde): #and best_points_possible > best_points_total:
                                                            abcdef_count += 1
                                                            count_try += 1
                                                            count_union += 1
                                                            abcdef = abcde.union(f)
                                                            cards_remaining = list(set(pyramid_poker_list).difference(abcdef))
                                                            cards_remaining = sorted(cards_remaining, key=rank_sort, reverse=True)
                                                            # this statement needs to use list() to ensure it works
                                                            hand_6, hand_5, hand_4, hand_3, hand_2, hand_1 = \
                                                                list(hand6[i][0]), list(hand5[j][0]), list(hand4[k][0]), \
                                                                list(hand3[l][0]), list(hand2[m][0]), list(hand1[n][0])
                                                            # print ("before fill", hand_6, hand_5, hand_4, hand_3, hand_2, hand_1, cards_remaining)
                                                            # fill in all hands, starting with hand5, hand6, hand4, hand2, hand3
                                                            while (len(hand_5) == 4 and len(cards_remaining) > 0):  # fill 4K
                                                                card_z = cards_remaining[0]
                                                                hand_5.append(card_z)
                                                                cards_remaining.remove(card_z)
                                                            while (len(hand_6) == 4 and len(cards_remaining) > 0):  # fill 4K
                                                                card_z = cards_remaining[0]
                                                                hand_6.append(card_z)
                                                                cards_remaining.remove(card_z)
                                                            while (len(hand_4) == 4 and len(cards_remaining) > 0):  # fill 4K
                                                                card_z = cards_remaining[0]
                                                                hand_4.append(card_z)
                                                                cards_remaining.remove(card_z)
                                                            while (len(hand_3) == 4 and len(cards_remaining) > 0):  # fill 4K
                                                                card_z = cards_remaining[0]
                                                                hand_3.append(card_z)
                                                                cards_remaining.remove(card_z)
                                                            while (len(hand_2) == 2 and len(cards_remaining) > 0):  # fill pair
                                                                # make sure fill does not create trip
                                                                card_z = cards_remaining[0]
                                                                if card_z[1] == hand_2[0][1] and len(cards_remaining) > 1:
                                                                    card_z = cards_remaining[1]
                                                                hand_2.append(card_z)
                                                                cards_remaining.remove(card_z)
                                                            # if one high card, need to fill both cards
                                                            if (len(hand_2) == 1) and len(cards_remaining) > 2: # fill high card
                                                                # make sure it does not pair up with existing cards
                                                                # first fill that is not pair
                                                                card_z = cards_remaining[0]
                                                                if card_z[1] == hand_2[0][1] and len(cards_remaining) > 1:
                                                                    card_z = cards_remaining[1]
                                                                hand_2.append(card_z)
                                                                # second fill that is not pair
                                                                cards_remaining.remove(card_z)
                                                                card_z = cards_remaining[0]
                                                                for card_y in hand_2:
                                                                    if card_z[1] == card_y[1] and len(cards_remaining) > 1:
                                                                        card_z = cards_remaining[1]
                                                                hand_2.append(card_z)
                                                                cards_remaining.remove(card_z)
                                                            while (len(hand_3) < 3 and len(cards_remaining) > 0):  # fill pair
                                                                # make sure fill does not create trip
                                                                card_z = cards_remaining[0]
                                                                if card_z[1] == hand_3[0][1] and len(cards_remaining) > 1:
                                                                    card_z = cards_remaining[1]
                                                                hand_3.append(card_z)
                                                                cards_remaining.remove(card_z)
                                                            while (len(hand_4) < 3 and len(cards_remaining) > 0):   # fill pair
                                                                # make sure fill does not create trip
                                                                card_z = cards_remaining[0]
                                                                if card_z[1] == hand_4[0][1] and len(cards_remaining) > 1:
                                                                    card_z = cards_remaining[1]
                                                                hand_4.append(card_z)
                                                                cards_remaining.remove(card_z)

                                                            pyramid_hand = ([0, hand_1, hand_2, hand_3, hand_4, hand_5, hand_6])
                                                            # print((pyramid_hand, cards_remaining))
                                                            hand_points = six_hands.get_six_hands_points(pyramid_hand)
                                                            points_total = hand_points[0]

                                                            print("Next Hand", hand_points[6][1], hand_points[5][1],
                                                                hand_points[4][1], hand_points[3][1], hand_points[2][1],
                                                                hand_points[1][1], points_total)    #, end="")
                                                            print(pyramid_hand[6:0:-1])

                                                            logging.info((h6_points, h5_points, h4_points, h3_points, h2_points, h1_points, points_total))
                                                            best_scores.append ((hand_points[0], hand_points, pyramid_hand[1:7]))
                                                            if points_total > best_points_total:
                                                                best_points_total = points_total
                                                                best_hand_count = count_try
                                                                best_pyramid_poker_hand = pyramid_hand
                                                                print
                                                                print("-----New best", hand_points[6], hand_points[5], hand_points[4],hand_points[3], hand_points[2], hand_points[1], best_points_total)
                                                                print (best_pyramid_poker_hand[6:0:-1])
                                                            count_try += 1
                                                            # break
        end_time = time.time()
        elapse_time = round(end_time - begin_time,1)
        if elapse_time <= .001:
            elapse_time = .001
        hands_per_sec = round(count_try/elapse_time)
        count1 = count
        if count == 0:
            count = 1
        if count_try == 0:
            count_try = 1
        # print ("count_intersect, count_union", count_intersect, count_union)
        percent_found = round(best_hand_count*100/count_try)
        # print ("-- Total:{0:>10,}, Best: {1:>6,}, Time: {2:>6}, Hands/Sec: {3:>9,} Found: {4:>2}%"\
        #    .format(count_try, best_hand_count, elapse_time, hands_per_sec, percent_found), end="")
        self.best_pyramid_poker_hand = best_pyramid_poker_hand
        print ("-- Total:{0:>10,}, a:{1:>5,} b:{2:>8,} c:{3:>10,} d:{4:>9,} e:{5:>4,} f:{6:>4,}, i: {7:>10,}, u: {8:>9,} Best: {9:>6,}, Time: {10:>6}, Hands/Sec: {11:>9,} Found: {12:>2}%"\
           .format(count_try, a_count, ab_count, abc_count, abcd_count, abcde_count, abcdef_count, count_intersect, count_union, best_hand_count, elapse_time, hands_per_sec, percent_found), end="")
        # self.best_pyramid_poker_hand = best_pyramid_poker_hand
        # recalculate best_points after fill
        best_hand = PokerHand()
        if len(best_pyramid_poker_hand) == 0:
            # print ("  -Can't beat", end="")
            self.best_points = -9999, -9999, -9999, -9999, -9999, -9999, -9999
            self.best_hand_points = -9999, -9999, -9999, -9999, -9999, -9999, -9999
            self.best_pyramid_poker_hand = [0,0,0,0,0,0,0]
        else:
            # print ("\n", best_pyramid_poker_hand[6:0:-1])
            best_points = best_hand.get_six_hands_points(best_pyramid_poker_hand)
            self.best_points = best_points  # hand1 in best_points[1] etc.
            self.best_hand_points = best_points[0], best_points[6], best_points[5], best_points[4], best_points[3], \
                                best_points[2], best_points[1]
        # self.five_card_hands = len(hand6)
        # self.three_card_hands = len(hand4)
        self.hands_count = count1
        self.time = elapse_time
        self.best_hand_count = best_hand_count # best points [6]-[1]
        self.hands_per_second = hands_per_sec
        global_variables.best_scores_list.extend(best_scores)
        return

    # def is_true(self, h2,h1, a,b, p_max,p):
    #     if h2>h1 and a.isdisjoint(b) and p_max>p:
    #         return(True)
