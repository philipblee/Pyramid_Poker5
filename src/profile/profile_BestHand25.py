from src.core.BestHand25 import *
import cProfile
import time
from src.core.Deck import *


def test():
    total_elapse = 0
    for i in range(1):
        begin = time.time()
        pyramid_poker_list = Deck.deal()[0]
        pyramid_poker_list = ["SA-,DK-,DK+,CK*,DQ*,CQ-,SJ+,HJ-,ST*,HT+,CT+,S9+,H9+,C9+,C8+,C7-,D6-,C6*,S5*,C5-,D4+,C4+,C4*,D3+,H2+"]
        # pyramid_poker_list = ['C3+', 'D5*', 'H6-', 'C5-', 'SQ*', 'DJ-', 'D3*', 'H9+', 'D5+', 'SJ*', 'HK-', 'D5-', 'H8+', 'S6-', 'CA*', 'S7-',
        #  'WW-', 'CJ*', 'D8+', 'C8+', 'C6-', 'CA-', 'CK-', 'C6*', 'SQ+']
        # pyramid_poker_list = "D9+,C8-,HA-,HA*,H9+,SQ+,H8-,C2*,S2+,S5*,HT*,CQ+,SK-,H6+,C5-,H5+,D9-,HT+,DT*,SA*,H2*,H6-,S8*,H7*,H6*"
        # # pyramid_poker_list= "SA+,SQ-,SJ+,S9*,S9-,S4-,HT+,H7*,H5-,H4-,DA-,DQ+,DJ*,DJ-,D9+,D6+,D6-,D5-,D5*,D4*,D3*,D2*,CJ-,C7-,C2-"
        # pyramid_poker_list = ['CJ-', 'HA-', 'CA*', 'SK-', 'HK*', 'SQ+', 'CQ-', 'HJ-', 'ST*', 'DT*', 'CT*', 'D9*', 'C9-', 'C8+', 'S7+', 'C7+',
        #  'H6+', 'S5*', 'D5*', 'S4-', 'S4*', 'H4-', 'C4+', 'C4*', 'H2*']
        # pyramid_poker_list = ['SA-', 'CA-', 'DK+', 'DQ-', 'DJ*', 'CJ-', 'CT-', 'CT+', 'CT*', 'S9*', 'D8-', 'H7*', 'H7+', 'D7+', 'C7-', 'S6+',
        #  'D6*', 'S5+', 'H5*', 'D5-', 'D5+', 'S4*', 'S3*', 'D3+', 'H2*']   # this hand tests for pairs becomimg trip with matching filler hand 3
        # pyramid_poker_list = ['S5-', 'SK*', 'DK+', 'CK*', 'CK-', 'SJ*', 'DT*', 'CT+', 'S9*', 'H9-', 'H9+', 'C9*', 'H8+', 'D8*', 'C8+', 'C8*',
        #  'C7+', 'C6+', 'H5*', 'C5*', 'S4+', 'H4+', 'C4*', 'C3-', 'C2-']
        # pyramid_poker_list = ['C6+', 'DA+', 'DA*', 'CA+', 'SK-', 'HK+', 'DK*', 'CK+', 'DQ*', 'DJ-', 'DT+', 'CT+', 'H9*', 'D9*', 'C9*', 'S8+', 'C8-', 'H7-', 'C7-', 'S6*', 'S6+', 'C5*', 'H4*', 'C4+', 'H3-']
        # pyramid_poker_list = ['SA*', 'DA-', 'CA+', 'HK+', 'HK-', 'DK*', 'CK*', 'CQ-', 'DJ*', 'CJ-', 'HT-', 'CT*', 'CT+', 'H9+', 'D9+', 'D8*',
        #  'H7*', 'H7+', 'S6+', 'H6+', 'C5*', 'H3+', 'C3+', 'C2+', 'C2-']

        # pyramid_poker_list = ['SA-', 'DA+', 'DA-', 'CA*', 'HK*', 'CK*', 'HQ-', 'DQ*', 'SJ-', 'HT+', 'H9*', 'S8*', 'S8+', 'D8*', 'H7*', 'H7-',
        #                       'C6+', 'C6*', 'D5*', 'S4-', 'S4*', 'S3+', 'H3*', 'H3-', 'C2+']   # this hand tests for pairs becomimg trip with matching filler hand 2
        # pyramid_poker_list = ['S8++', 'S7++', 'S6-', 'S9*', 'S5-', 'SQ*', 'SK-', 'HK+', 'HK*', 'DK-', 'HT+', 'S4+', 'D4-', 'C4*', 'C4-', 'C9+',
        #   'C9*', 'H7+', 'D6-', 'D6-', 'D8+', 'DA*', 'S3+', 'H2*', 'H5-']
        # pyramid_poker_list = 'SA+,SA+,HA-,HA*,CA-,CA*,HQ*,HT-,S9+,H9+,D8*,D8+,S7-,D7+,S6+,D6-,S5*,S5+,C5-,H4+,C4+,H3*,S2*,S2+,S2-'
        # pyramid_poker_list = \
        # ['SA!', 'SA!', 'SA*', 'SA+', 'HA+', 'CA-', 'SK-', 'SK*', 'DK-', 'SQ-', 'SQ*', 'CQ+', 'SJ*', 'CT*', 'S9-', 'D9+',
        #  'S7+', 'C6-', 'S5*', 'H5+', 'C5+', 'S4-', 'C4-', 'S3-', 'C2-']
        # pyramid_poker_list = pyramid_poker_list.split(",")

        # pyramid_poker_list = ['S8++', 'S7++', 'S6-', 'S9*', 'S5-', 'SQ*', 'SK-', 'HK+', 'HK*', 'DK-', 'HT+', 'S4+',
        #                           'D4-', 'C4*', 'C4-', 'C9+', 'C9*', 'H7+', 'D6-', 'D6-', 'D8+', 'DA*', 'S3+', 'H2*',
        #                           'H5-']
        # pyramid_poker_list = \
        # ['WW+', 'WW-', 'SA*', 'DA*', 'HK*', 'DK+', 'CT*', 'CT-', 'H9+', 'S8-', 'C8-', 'D7+', 'C7*', 'S6-', 'D6*', 'H5-',
        #  'D5-', 'H4+', 'H4-', 'C4*', 'C3+', 'C3-', 'S2-', 'H2*', 'C2-']

        print ("\nHAND", i+1, 80 * "-")
        print (pyramid_poker_list)
        wild_found = False
        for card in pyramid_poker_list:
            if card[0] == "W":
                wild_found = True
                print ("Cannot handle wild cards here")
                break

        if wild_found != True:
            best_hand = BestHand25(pyramid_poker_list, -10000)
            print ("\n", best_hand.best_pyramid_poker_hand[6:0:-1])
            print (best_hand.best_points[6:0:-1], best_hand.best_points[0])
        end = time.time()
        elapse = round(end - begin,2)

        total_elapse += elapse
        print (elapse, "avg", total_elapse/(i+1))
    return

# test()
import pstats
cProfile.run("test()", 'stats')
p = pstats.Stats('stats')
p.sort_stats('time').print_stats(.2)
