""" I need to figure out the if statements that lead to a break
If I can get that to work, it will speed up greatly
05.19.2021 - use of best_points_so_far to prune the search
tree is not working.  Somehow better pyramid poker hands are
getting pruned
"""

from src.core.LegalPokerHands import *
from src.core.PokerHand import *
import src.core.global_variables as global_variables
from src.core.sort_cards import *
import time

class BestHand25:
    def __init__(self, pyramid_poker_list, best_points_so_far):
        """
        :param pyramid_poker_list: 25 card had
        :param best_points_so_far:
        Given 25 cards and best_points_so_far, decide if any combination of LegalPokerHands
        can beat best_points_so_far
        """
        best_scores = []
        best_pyramid_poker_hand = []
        better_hand_found = False

        pyramid_poker_list = sorted(pyramid_poker_list, reverse=True, key=rank_sort)
        # print (pyramid_poker_list, best_points_so_far)

        # comment out best_points_so_far because it's causing BestHand25 to terminate early
        # set best_points = -10000 so every wild card choice is completed
        best_points = best_points_so_far - 200
        # best_points = -10000  # always finds best hand
        # generate all feasible PokerHands for hand (6, 5, 4, 3, 2, 1)
        my_hand = LegalPokerHands(pyramid_poker_list)
        hand6 = list(my_hand.hand6)
        hand5 = list(my_hand.hand5)
        hand4 = list(my_hand.hand4)
        hand3 = list(my_hand.hand3)
        hand2 = list(my_hand.hand2)
        hand1 = list(my_hand.hand1)

        hands = my_hand.hands

        # print (len(hands[0]))
        # print (len(hands[1]))
        # print (len(hands[2]))
        # print (len(hands[3]))
        # print (len(hands[4]))
        # print (len(hands[5]))
        # print (len(hands[6]))

        self.hand6_count = hand6_count = my_hand.hand_count[6]
        self.hand5_count = hand5_count = my_hand.hand_count[5]
        self.hand4_count = hand4_count = my_hand.hand_count[4]
        self.hand3_count = hand3_count = my_hand.hand_count[3]
        self.hand2_count = hand2_count = my_hand.hand_count[2]
        self.hand1_count = hand1_count = my_hand.hand_count[1]

        # print (hand6_count, hand4_count)

        a_count = 0; ab_count = 0; abc_count = 0; abcd_count = 0; abcde_count = 0; abcdef_count = 0
        pokerhand = PokerHand()
        print ("-- Hands {0:>4} {1:>4} {2:>3} {3:>3} {4:>3} {5:>3}".format(hand6_count,
                   hand5_count, hand4_count, hand3_count, hand2_count, hand1_count),end="")
        best_hand_count = 0; count = 0; count_try = 0
        count_union = 0; count_intersect = 0
        begin_time = time.time()
        hand6_end_time = 0
        max_points = find_max_points(6, set([]), hands)
        # print ("keep searching if ", best_points," < ", max_points)
        if not futile(best_points, max_points):  # check futility before hand6
            for i in range(hand6_count):
                start_time = time.time()
                count_try += 1
                a_count += 1
                a = set(hand6[i][0])
                h6 = hand6[i][1]
                h6_points = hand6[i][2]
                max_points = h6_points + find_max_points(5, a, hands)
                disjoint_points = h6_points + find_disjoint_points(5, a, hands)[0]
                # if disjoint_points > best_points: - does not work, finds wrong hand
                if not futile(best_points, max_points):  # check futility before hand5
                    for j in range(i+1, hand5_count):
                        b = set(hand5[j][0])
                        ab = a.union(b)
                        h5 = hand5[j][1]
                        h5_points = hand5[j][2]
                        count_intersect += 1
                        max_points = h6_points + h5_points + find_max_points(4, ab, hands)
                        if h6 >= h5 and a.isdisjoint(b):
                            ab_count += 1
                            count_try += 1
                            # print(round(hand6_end_time,2), i, j, hand6[i][0], hand5[j][0], " if ", max_points, " > ",
                            #      best_points)
                            if not futile(best_points, max_points):  # check futility before hand4
                                for k in range(hand4_count):
                                    count_union += 1
                                    c = set(hand4[k][0])
                                    abc = ab.union(c)
                                    h4 = hand4[k][1]
                                    h4_points = hand4[k][2]
                                    count_intersect += 1
                                    max_points = h6_points + h5_points + h4_points + find_max_points(3, abc, hands)
                                    if h5 >= h4 and ab.isdisjoint(c):
                                        # print(i, j, k, hand6[i][0], hand5[j][0], hand4[k][0], " if ", max_points, " > ",
                                        #       best_points)
                                        abc_count += 1
                                        count_try += 1
                                        count_union += 1
                                        if not futile(best_points, max_points):  # check futility before hand3
                                            for l in range(k+1, hand3_count):
                                                d = set(hand3[l][0])
                                                abcd = abc.union(d)
                                                h3 = hand3[l][1]
                                                h3_points = hand3[l][2]
                                                count_intersect += 1
                                                max_points = h6_points + h5_points + h4_points + h3_points + find_max_points(2, abcd, hands)
                                                if h4 >= h3 and abc.isdisjoint(d):    # and max_points_possible > best_points:
                                                    # abc_count += 1
                                                    abcd_count += 1
                                                    count_try += 1
                                                    # check futility, get hand2, check hand2 disjointed
                                                    if not futile(best_points, max_points):  # check futility before hand2
                                                        for m in range(l+1, hand2_count):
                                                            e = set(hand2[m][0])
                                                            abcde = abcd.union(e)
                                                            h2 = hand2[m][1]
                                                            h2_points = hand2[m][2]
                                                            count_union = + 1
                                                            count_intersect += 1
                                                            max_points = h6_points + h5_points + h4_points + h3_points + h2_points +find_max_points(1, abcde, hands)
                                                            if h3 >= h2 and e.isdisjoint(abcd):
                                                                abcde_count += 1
                                                                count_try += 1
                                                                count_union += 1
                                                                abcde = abcd.union(e)
                                                                # check futility, get hand1, check hand1 disjointed
                                                                if not futile(best_points, max_points):  # check futility before hand1
                                                                    for n in range(hand1_count):
                                                                        f = set(hand1[n][0])
                                                                        h1 = hand1[n][1]
                                                                        h1_points = hand1[n][2]
                                                                        count_intersect += 1
                                                                        max_points = h6_points + h5_points + h3_points + \
                                                                                     h2_points + h1_points + find_max_points(1, abcde, hands)
                                                                        if not futile(best_points, max_points):
                                                                            if h2 >= h1 and f.isdisjoint(abcde):
                                                                                abcdef_count += 1
                                                                                count_try += 1
                                                                                count_union += 1
                                                                                abcdef = abcde.union(f)
                                                                                cards_remaining = list(set(pyramid_poker_list).difference(abcdef))
                                                                                cards_remaining = sorted(cards_remaining, key=rank_sort, reverse=True)
                                                                                # how do I make sure every combination of remaining cards is tried?
                                                                                # this statement needs to use list() to ensure it works
                                                                                # print ("before assignment", hand6[i][0], hand5[j][0], hand4[k][0])
                                                                                # print ("", hand3[l][0], hand2[m][0], hand1[n][0])
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

                                                                                # after filling all hands, you need to sort each hand in place
                                                                                hand_6.sort(key=rank_sort, reverse=True)
                                                                                hand_5.sort(key=rank_sort, reverse=True)
                                                                                hand_4.sort(key=rank_sort, reverse=True)
                                                                                hand_3.sort(key=rank_sort, reverse=True)
                                                                                hand_2.sort(key=rank_sort, reverse=True)

                                                                                pyramid_hand = ([0, hand_1, hand_2, hand_3, hand_4, hand_5, hand_6])
                                                                                # print((pyramid_hand, cards_remaining))
                                                                                hand_points = pokerhand.get_six_hands_points(pyramid_hand)
                                                                                points_total = hand_points[0]

                                                                                # print("Next", hand_points[6][1], hand_points[5][1],
                                                                                #     hand_points[4][1], hand_points[3][1], hand_points[2][1],
                                                                                #     hand_points[1][1], points_total, end="")
                                                                                # print(pyramid_hand[6:0:-1])

                                                                                best_scores.append ((hand_points[0], hand_points, pyramid_hand[1:7]))
                                                                                if points_total > best_points:
                                                                                    best_points = points_total
                                                                                    best_hand_count = count_try
                                                                                    best_pyramid_poker_hand = pyramid_hand
                                                                                    better_hand_found = True
                                                                                    # print
                                                                                    # print("          New best", hand_points[6], hand_points[5], hand_points[4],hand_points[3], hand_points[2], hand_points[1], best_points)
                                                                                    # print (best_pyramid_poker_hand[6:0:-1])
                                                                                count_try += 1
                    hand6_end_time = time.time() - start_time

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
        # commented out this print statement to print simpler one below
        # print ("-- Total:{0:>10,}, a:{1:>5,} b:{2:>8,} c:{3:>10,} d:{4:>9,} e:{5:>4,} f:{6:>4,}, i: {7:>10,}, u: {8:>9,} Best: {9:>6,}, Time: {10:>6}, Hands/Sec: {11:>9,} Found: {12:>2}%"\
        #   .format(count_try, a_count, ab_count, abc_count, abcd_count, abcde_count, abcdef_count, count_intersect, count_union, best_hand_count, elapse_time, hands_per_sec, percent_found), end="")
        print(
            "-- Total: Best: {0:>10,}, Time: {1:>6}" \
            .format(best_hand_count, elapse_time), end="")
        # self.best_pyramid_poker_hand = best_pyramid_poker_hand
        # recalculate best_points after fill
        best_hand = PokerHand()
        if better_hand_found == False:
            print ("  -Can't beat", end="")
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
def futile(best_points_so_far, max_possible_points):
    futile = False
    if best_points_so_far > max_possible_points:
        futile = True
    return (futile)

def find_disjoint_index(set_start, list_of_hands):
    # given an existing set, and a list of hands, returns index for
    # first hand that is disjointed
    hand_num = len(list_of_hands)
    index = 0
    for i in range(0, hand_num):
        b = set(list_of_hands[i])
        if set_start.isdisjoint(b):
            index = i
            break
    return(index)

def find_disjoint_points(hand, set_start, hands):
    """
    finds dis_joint_hands for hands not selected yet
    :param i:
    :param hand: 6, 5, 4, 3 or 2
    :param set_start: cards that cannot be used again
    :param hands: hand1-habd6 put into an list of lists
    :return: max_points
    """
    # print ("find max_points inputs", hand, set_start)
    seta = set_start
    hand_index = [-1,-1,-1,-1,-1,-1,-1]
    hand_found = [[],[],[],[],[],[],[]]
    temp = -9999
    max_points = 0
    hand_max_points = [temp, temp,temp, temp,temp, temp,temp]
    handn =[[],[],[],[],[],[],[],[]]
    # starts with handn[hand+num], compare with handn[handn[hand-1]
    for i in range (hand,0,-1):
        handn[i] = [col[0] for col in hands[i]]
        hand_index[i] = find_disjoint_index(seta, handn[i])
        hand_found[i] = handn[i][hand_index[i]]
        # print (hand_index[i], handn[i][hand_index[i]])
        # print ("hand i, points", i, hands[i][hand_index[i]][2])
        seta = seta.union(set(handn[i][hand_index[i]]))
        hand_max_points[i] = hands[i][hand_index[i]][2]
        max_points = round(max_points + hands[i][hand_index[i]][2], 2)
        hand_max_points[0] = max_points
    return(hand_max_points)

def find_max_points(hand, set_start, hands):
    """
    finds max_points for hands not selected yet
    :param i:
    :param hand: 6, 5, 4, 3 or 2
    :param set_start: cards that cannot be used again
    :param hands: hand1-habd6 put into an list of lists
    :return: max_points
    """
    # print ("find max_points inputs", hand, set_start)
    seta = set_start
    hand_index = [-1,-1,-1,-1,-1,-1,-1]
    hand_found = [[],[],[],[],[],[],[]]
    temp = -9999
    hand_max = [temp, temp,temp, temp,temp, temp,temp]
    handn =[[],[],[],[],[],[],[],[]]
    max_points = 0
    # cushion adjusts when "potential hands" are considered futile and abandoned based on max_points
    # however best_points are hands that are filled; max_points do not include fills, cushion compensates for that
    max_hand6_cushion = 0
    max_hand5_cushion = 0
    max_hand4_cushion = 0
    max_hand3_cushion = 0
    max_hand2_cushion = 0

    hand_index[6] = 0
    hand_index[5] = 1
    hand_index[4] = 0
    hand_index[3] = 1
    hand_index[2] = 2
    hand_index[1] = 0

    # starts with handn[hand+num], compare with handn[handn[hand-1]
    for i in range (hand,0,-1):
        hand_max[i] = hands[i][hand_index[i]][2]
        max_points = round(max_points + hands[i][hand_index[i]][2], 2)
        hand_max[0] = max_points

    if len(hand_found[6]) == 4:
        max_hand6_cushion = 40
    if len(hand_found[5]) == 4:
        max_hand5_cushion = 60
    if len(hand_found[4]) == 4:
        max_hand4_cushion = 100
    if len(hand_found[4]) < 3:
        max_hand4_cushion = 10
    if len(hand_found[3]) < 3:
        max_hand3_cushion = 10
    if len(hand_found[2]) < 3:
        max_hand2_cushion = 10

    max_points = max_points + max_hand4_cushion + max_hand5_cushion + \
                 max_hand6_cushion + max_hand3_cushion + max_hand2_cushion
    # print ("max_points", max_points)
    return (max_points)