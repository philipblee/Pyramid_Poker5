from src.core.straight_count import *

ranks = "W123456789TJQKA"
suits = "WSHDC"

def analyze_wild(card_list):
    """ returns suit_rank_array[i] where i is row
     0 - W                11 - singles_list    21 - S_list       31 - ranks of 11
     1 - S                12 - pairs_list      22 - H_list       32 - ranks of 12
     2 - H                13 - trips_list      23 - D_list       33 - ranks of 13
     3 - D                14 - fourks_list     24 - C_list       34 - ranks of 14
     4 - C                15 - fiveks_list     25 - 5 card SF    35 - ranks of 15
     5 - Frequency        16 - sixks_list      26 - 6 card SF    36 - ranks of 16
     6 - Straights        17 - sevenks_list    27 - 7 card SF    37 - ranks of 17
     7 - SF S             18 - eightks_list    28 - 8 card SF    38 - ranks of 18
     8 - SF H             19 - nineks_list     29 - 9 card SF    39 - ranks of 19
     9 - SF D             20 - tenks_list      30 - 10 card SF   40 - ranks of 20
    10 - SF C                                                    41 - ranks of spades
                                                                 42 - ranks of hearts
                                                                 43 - ranks of diamonds
                                                                 44 - ranks of clubs
     cards are stored in rows 11 to 24; ranks are stored in rows 31 to 44
     column 15 is always sum of row - for flushes [5][15], sf totals [7][14]
     """

    suit_rank_array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [], [], [], [], [], [], [], [], [], [],
                       [], [], [], [], [], [], [], [], [], [],
                       [], [], [], [], [], [], [], [], [], [],
                       [], [], [], [], [], [], [], [], [], []]

    # add test to make sure that every card is valid and not wild

    for card in reversed(card_list):
        suit_int = suits.index(card[0])  # 1:5
        rank_int = ranks.index(card[1])  # 1:15
        suit_rank_array[suit_int][rank_int] += 1  # increment[i][j] by 1
        suit_rank_array[20 + suit_int].append(card)  # store cards of each suit in rows 21:24
        suit_rank_array[40 + suit_int].append(card[1])   # store ranks of each suit in rows 41:44

    flushes = 0  # count flushes
    for i in range(5):
        suit_rank_array[i][15] = sum(suit_rank_array[i][0:15])  # put suit frequency in 15
        suit_rank_array[i][1] = suit_rank_array[i][14]  # set up Ace as 1 for straights
        if suit_rank_array[i][15] >= 5:
            flushes += 1
    suit_rank_array[5][15] = flushes  # store sum of flushes in [5][15]

    for j in range(0, 15):   # put rank j frequency in row 5
        suit_rank_array[5][j] = suit_rank_array[0][j] + suit_rank_array[1][j]+ suit_rank_array[2][j]+ suit_rank_array[3][j]+ suit_rank_array[4][j]

    # go through each card and put in suit_rank_array 11-20 based on frequency of rank
    for card in card_list:
        # suit_int = suits.index(card[0])  # 1:5
        rank_int = ranks.index(card[1])  # 1:15
        frequency = suit_rank_array[5][rank_int]
        if frequency > 0:
            suit_rank_array[10+frequency].append(card)

    # split into multiple lists
    for size in range(2, 10):
        seq = suit_rank_array[10+size]
        suit_rank_array[10+size] = [seq[i:i + size] for i in range(0, len(seq), size)]

    # 5 card straights - 1st call straight_count - put straights in row 6
    suit_rank_array[6] = straight_count(suit_rank_array[5], 5)

    # 5 card straight flush
    for i in range(1, 5):
        if suit_rank_array[i][15] >= 5:
            # 2nd to 5th call to straight_count
            suit_rank_array[i+6] = straight_count(suit_rank_array[i], 5)
            if suit_rank_array[i+6][15] >= 1:
                 for j in range(10,0,-1):
                     if suit_rank_array[i+6][j] >= 1:
                         # i is the suit, j is the highest
                         if j == 1:
                             lowest_card = suits[i] + "A"
                         else:
                             lowest_card = suits[i] + ranks[j]
                         suit_rank_array[25].append(lowest_card)
    suit_rank_array[7][14] = suit_rank_array[7][15] + suit_rank_array[8][15] + \
                             suit_rank_array[9][15] + suit_rank_array[10][15]  # 5 card straightflush

    # 6 card straight flush
    straight_ct = 5 * [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    for i in range(7, 11):
        if suit_rank_array[i - 6][15] >= 6:
            straight_ct[i-6] = straight_count(suit_rank_array[i - 6], 6)
    six_card_straightflushes = straight_ct[1][15] + straight_ct[2][15] + \
                         straight_ct[3][15] + straight_ct[4][15]  # 6 card straightflush

    if six_card_straightflushes > 0:
        # print(("6 card straightflush", six_card_straightflushes))
        for i in range(1,5):
            for j in range (9,0,-1):
                if straight_ct[i][j]  > 0:
                    # i is the suit, j is the highest
                    if j == 1:
                        lowest_card = suits[i] + "A"
                    else:
                        lowest_card = suits[i] + ranks[j]
                    suit_rank_array[26].append(lowest_card)
        # print(("6 card straightflush lowest_card", suit_rank_array[26]))

    # 7 card straight flush
    straight_ct = 5 * [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(7, 11):  # for each suit
        if suit_rank_array[i - 6][15] >= 7:
            straight_ct[i-6] = straight_count(suit_rank_array[i - 6], 7)
    seven_card_straightflushes = straight_ct[1][15] + straight_ct[2][15] + \
                             straight_ct[3][15] + straight_ct[4][15]  # 7 card straightflush

    if seven_card_straightflushes > 0:
     # print(("7 card straightflush", seven_card_straightflushes))
        for i in range(1,5):
            for j in range (8,0,-1):
                if straight_ct[i][j]  > 0:
                    # i is the suit, j is the lowest
                    if j == 1:
                        lowest_card = suits[i] + "A"
                    else:
                        lowest_card = suits[i] + ranks[j]
                    suit_rank_array[27].append(lowest_card)
        # print(("7 card straightflush lowest_card", suit_rank_array[27]))
    straight_ct = 5 * [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    # 8 card straight flush
    for i in range(7, 11):
        if suit_rank_array[i - 6][15] >= 8:
            straight_ct[i-6] = straight_count(suit_rank_array[i - 6], 8)
    eight_card_straightflushes = straight_ct[1][15] + straight_ct[2][15] + \
                             straight_ct[3][15] + straight_ct[4][15]  # 8 card straightflush

    if eight_card_straightflushes > 0:
        # print(("8 card straightflush", eight_card_straightflushes))
        for i in range(1,5):
            for j in range (7,0,-1):
                if straight_ct[i][j]  > 0:
                    # i is the suit, j is the lowest
                    if j == 1:
                        lowest_card = suits[i] + "A"
                    else:
                        lowest_card = suits[i] + ranks[j]
                    suit_rank_array[28].append(lowest_card)
        # print(("8 card straightflush lowest_card", suit_rank_array[28]))

    # 9 card straight flush
    straight_ct = 5 * [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(7, 11):
        if suit_rank_array[i - 6][15] >= 9:
            straight_ct[i-6] = straight_count(suit_rank_array[i - 6], 9)
    nine_card_straightflushes = straight_ct[1][15] + straight_ct[2][15] + \
                             straight_ct[3][15] + straight_ct[4][15]

    if nine_card_straightflushes > 0:
        # print(("9 card straightflush", nine_card_straightflushes))
        for i in range(1,5):
            for j in range (6,0,-1):
                if straight_ct[i][j]  > 0:
                    # i is the suit, j is the lowest
                    if j == 1:
                        lowest_card = suits[i] + "A"
                    else:
                        lowest_card = suits[i] + ranks[j]
                    suit_rank_array[29].append(lowest_card)
        # print(("9 card straightflush lowest_card", suit_rank_array[29]))

    # 10 card straight flush
    straight_ct = 5 * [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(7, 11):
        if suit_rank_array[i-6][15] >= 10:
            straight_ct[i-6] = straight_count(suit_rank_array[i - 6], 10)

    ten_card_straightflushes = straight_ct[1][15] + straight_ct[2][15] + \
                             straight_ct[3][15] + straight_ct[4][15]  # 9 card straightflush

    if ten_card_straightflushes > 0:
        # print(("10 card straightflush", ten_card_straightflushes))
        for i in range(1,5):
            for j in range (5,0,-1):
                if straight_ct[i][j]  > 0:
                    # i is the suit, j is the lowest
                    if j == 1:
                        lowest_card = suits[i] + "A"
                    else:
                        lowest_card = suits[i] + ranks[j]
                    suit_rank_array[30].append(lowest_card)
        # print(("10 card straightflush lowest_card", suit_rank_array[30]))

    # Go through all 15 ranks and count singles, pairs, trips, etc.
    for j in range(14,1,-1):
        # print j, ranks[j], suit_rank_array[5][j]
        if suit_rank_array[5][j] == 0:
            pass
        elif suit_rank_array[5][j] == 1:
            suit_rank_array[31].append(ranks[j])
        elif suit_rank_array[5][j] == 2:
            suit_rank_array[32].append(ranks[j])
        elif suit_rank_array[5][j] == 3:
            suit_rank_array[33].append(ranks[j])
        elif suit_rank_array[5][j] == 4:
            suit_rank_array[34].append(ranks[j])
        elif suit_rank_array[5][j] == 5:
            suit_rank_array[35].append(ranks[j])
        elif suit_rank_array[5][j] == 6:
            suit_rank_array[36].append(ranks[j])
        elif suit_rank_array[5][j] == 7:
            suit_rank_array[37].append(ranks[j])
        elif suit_rank_array[5][j] == 8:
            suit_rank_array[38].append(ranks[j])
        elif suit_rank_array[5][j] == 9:
            suit_rank_array[39].append(ranks[j])
        elif suit_rank_array[5][j] == 10:
            suit_rank_array[40].append(ranks[j])
        # for i in range(45):
        #     print (i, suit_rank_array[i])
    return (suit_rank_array)
