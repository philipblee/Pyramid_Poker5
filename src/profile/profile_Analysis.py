from src.core.Analysis import *
from src.core.Deck import *
import cProfile
import time


def profiler_function():
    total_elapse = 0
    for i in range(100000):
        begin = time.time()
        pyramid_poker_list = Deck.deal()[0]
        # pyramid_poker_list = "SA-,DK-,DK+,CK*,DQ*,CQ-,SJ+,HJ-,ST*,HT+,CT+,S9+,H9+,C9+,C8+,C7-,D6-,C6*,S5*,C5-,D4+,C4+,C4*,D3+,H2+"
        # pyramid_poker_list = "D9+,C8-,HA-,HA*,H9+,SQ+,H8-,C2*,S2+,S5*,HT*,CQ+,SK-,H6+,C5-,H5+,D9-,HT+,DT*,SA*,H2*,H6-,S8*,H7*,H6*"
        # pyramid_poker_list= "SA+,SQ-,SJ+,S9*,S9-,S4-,HT+,H7*,H5-,H4-,DA-,DQ+,DJ*,DJ-,D9+,D6+,D6-,D5-,D5*,D4*,D3*,D2*,CJ-,C7-,C2-"
        # pyramid_poker_list = pyramid_poker_list.split(",")

        analysis = Analysis(pyramid_poker_list)


        # for i in range(30):
        #     print solution[i]
        end = time.time()
        elapse = end - begin

        total_elapse += elapse
        # print elapse, "avg", total_elapse/(i+1)
    return


import pstats
cProfile.run("profiler_function()", "stats")
p = pstats.Stats('stats')
p.sort_stats('time').print_stats(.99)