import numpy as np

def straightcount (rankcount, length):
    """ count straights - takes in rankcount(list of ranks), and returns straightct
        array with straights in straightct [1:10] - if 1, it's A2345, if 2 it's23456
        finally straightct [15] = total number of straights
        used mainly by analyze()"""

    # re-done with numpy

    np_straightct = np.zeros(16)

    if sum(rankcount) >= length:
        np_rankcount = np.array([rankcount])
        # vectorize finding straights
        straight_test = np.array(np_rankcount > 0)   # boolean vector

        for j in range(1,11):
            if straight_test[0][j:j+length].sum == length:
                np_straightct[j] = 1
        np_straightct[15] = np_straightct.sum()

    straightct = list(np_straightct)
    return(straightct)
