from src.core.Deck import *
# import cProfile
from src.core.BestHand25Wild import *
import time
import datetime
def test():
    print (datetime.datetime.now())
    total_elapse = 0
    for i in range(1):
        begin = time.time()
        # pyramid_poker_list = Deck.deal()[0]
        # pyramid_poker_list = "SA-","DK-","DK+","CK*","DQ*","CQ-","SJ+","HJ-","ST*","HT+","CT+",'S9+','H9+','C9+','C8+','C7-','D6-','C6*','S5*','C5-','D4+','C4+','C4*','D3+','H2+'
        # pyramid_poker_list = ['H3+', 'HT+', 'DK-', 'DA-', 'CJ*', 'WW-', 'WW+', 'HK+', 'DK*', 'CK+', 'CQ-', 'ST+', 'ST-', 'HT*', 'DT*', 'DT-',
        #  'CT*', 'H9-', 'C9*', 'C9-', 'H8+', 'H7-', 'C5-', 'S4-', 'S2*']

        pyramid_poker_list = \
        ['WW*', 'WW-', 'SA*', 'SA+', 'HA+', 'CA-', 'SK-', 'SK*', 'DK-', 'SQ-', 'SQ*', 'CQ+', 'SJ*', 'CT*', 'S9-', 'D9+',
         'S7+', 'C6-', 'S5*', 'H5+', 'C5+', 'S4-', 'C4-', 'S3-', 'C2-']  # example 1

        # pyramid_poker_list = \
        # ['WW*', 'WW+', 'SA+', 'HA+', 'CK*', 'SQ+', 'HJ+', 'DT-', 'S9+', 'H9+', 'H9-', 'D9-', 'D9+', 'S8*', 'D8*', 'D7+',
        #  'D7-', 'D6-', 'D6+', 'C6+', 'D5-', 'S4+', 'D4-', 'H3-', 'S2-']    # example 7 - this hand triggers too many wild cards - 996 wilds combinations
        # fixed defect in WildList

        # pyramid_poker_list = \
        # ['WW+', 'WW-', 'SA+', 'SA-', 'SK+', 'HK+', 'HK-', 'DK+', 'HQ+', 'HJ-', 'CT*', 'C9-', 'D8+', 'S7+', 'S7*', 'C7*',
        #  'S6*', 'C6-', 'S5+', 'S5*', 'C5+', 'S3*', 'D3+', 'C3+', 'S2+']  # example 5 - computer played hand 1,2,3 wrong

        # pyramid_poker_list = \
        #   ['SK-', 'SK*', 'HK*', 'CK+', 'SQ-', 'DQ*', 'SJ-', 'CT*', 'S9+', 'H9-', 'D9*', 'D9+', 'C9*', 'H7+', 'D7+', 'S6-',
        #    'D6-', 'D6*', 'D5-', 'D5*', 'C5-', 'C5+', 'C3+', 'C3-', 'D2-']   # example 6 - computer plays hand 1, 2, 3 wrong

        #     ['HA=', 'HA=', 'HK=', 'CK=', 'SQ=', 'HJ=', 'ST=', 'ST=', 'HT=', 'DT=', 'S9=', 'H8=', 'D8=', 'S6=', 'H6=',
        #      'D6=', 'D6=', 'D6=', 'C6=', 'S4=', 'H4=', 'H3=', 'D3=', 'C3=', 'D2=']     # example 3
        # ['SA=', 'HA=', 'DA=', 'CA=', 'SK=', 'HK=', 'DK=', 'SQ=', 'CQ=', 'SJ=', 'HJ=', 'CJ=', 'ST=', 'CT=', 'S9=',
        #  'H8=', 'D8=', 'S7=', 'S6=', 'S6=', 'C6=', 'S5=', 'C5=', 'S4=', 'D3=']
        # ['WW-', 'HA=', 'DA=', 'CK=', 'HQ=', 'SJ=', 'HJ=', 'ST=', 'ST=', 'CT=', 'CT=', 'S9=', 'C9=', 'D7=', 'H6=',
        #  'D6=', 'C6=', 'S5=', 'S5=', 'H5=', 'D5=', 'C4=', 'S2=', 'S2=', 'H2=']
        # ['WW-', 'HA=', 'DA=', 'CK=', 'HQ=', 'SJ=', 'HJ=', 'ST=', 'ST=', 'CT=', 'CT=', 'S9=', 'C9=', 'D7=', 'H6=',
        #  'D6=', 'C6=', 'S5=', 'S5=', 'H5=', 'D5=', 'C4=', 'S2=', 'S2=', 'H2=']

        # pyramid_poker_list = \
        # ['DJ*', 'DA=', 'CK=', 'SQ=', 'DQ=', 'HJ=', 'DT=', 'DT=', 'D9=', 'C9=', 'S8=', 'S8=', 'H8=', 'D8=', 'C8=', 'D7=', 'D7=',
        #  'S5=', 'H4=', 'S3=', 'D3=', 'D3=', 'C3=', 'D2=', 'D2=']    #example 2

        # pyramid_poker_list = \
        # ['WW=', 'WW=', 'SA=', 'SA=', 'HA=', 'CA=', 'SK=', 'SK=', 'DK=', 'SQ=', 'SQ=', 'CQ=', 'SJ=', 'CT=', 'S9=', 'D9=',
        #  'S7=', 'C6=', 'S5=', 'H5=', 'C5=', 'S4=', 'C4=', 'S3=', 'C2=']
        # pyramid_poker_list = \
        #     ['H2=', 'HA*', 'HA-', 'CA-', 'HK+', 'HQ+', 'HJ+', 'HJ*', 'HT-', 'HT+', 'S8-', 'D8-', 'C8+', 'S6*', 'S6+',
        #      'C6-', 'C6*', 'H5+', 'C5+', 'S4*', 'S4-', 'H4-', 'H3-', 'D3-', 'D2*']
            # ['S3-', 'SA+', 'SA-', 'HK*', 'SQ*', 'DJ-', 'ST+', 'HT+', 'DT-', 'DT+', 'CT*', 'S9+', 'S9*', 'H9-', 'H7*',
            #  'D7+', 'H6-', 'S5-', 'H3*', 'C3+', 'C3*', 'S2-', 'S2+', 'H2-', 'C2*']
        # ['WW+', 'WW-', 'SA*', 'DA*', 'HK*', 'DK+', 'CT*', 'CT-', 'H9+', 'S8-', 'C8-', 'D7+', 'C7*', 'S6-', 'D6*', 'H5-',
        #  'D5-', 'H4+', 'H4-', 'C4*', 'C3+', 'C3-', 'S2-', 'H2*', 'C2-']

        print ("\nHAND", i+1, " - ", end = "")
        pyramid_poker_list = sorted(pyramid_poker_list, key=rank_sort, reverse=True)
        print (pyramid_poker_list)
        myhand = BestHand25Wild(pyramid_poker_list)
        print (myhand.best_25handx)
        end = time.time()
        elapse = round(end - begin,2)
        total_elapse += elapse
        print (elapse, "avg", round(total_elapse/(i+1),2))
    return

import pstats
# cProfile.run("test()", 'stats')
p = pstats.Stats('stats')
p.sort_stats('time').print_stats(.3)
