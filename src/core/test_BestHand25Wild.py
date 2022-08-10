from src.core.Deck import *
from src.core.BestHand25Wild import *

total_elapse = 0

for i in range (1):
    card_list = Deck.deal()[0]
    card_list2 = list(card_list[0:25])  # deal number_of_cards
    # card_list2 = ['SA*', 'SA-', 'HA+', 'HA*', 'CA+', 'CA-', 'CK+', 'HQ+', 'DQ-', 'DQ+', 'DQ*', 'CQ-', 'DJ-', 'HT-', 'S9+', 'H8+',
    #  'S7-', 'H7+', 'H7-', 'D7+', 'D7-', 'H6+', 'H5+', 'D3*', 'S2*']
    # card_list2 = ['WW-', 'SA-', 'SQ-', 'SJ-', 'S9+', 'S7-', 'S6-', 'S3-', 'HJ+', 'HT*', 'H8+', 'H6*', 'H3+', 'DK+', 'DK*', 'D6*', 'D5-', 'D4*', 'D2-', 'CA*', 'CA-', 'CQ-', 'CQ+', 'CJ+', 'C2+']
    #   ['WW*', 'DA+', 'DA*', 'SK*', 'HK*', 'DK+', 'DQ-', 'SJ-', 'ST+', 'ST*', 'DT*', 'H9+', 'S8-', 'H8*', 'H8+', 'D8-',
    # card_list2 = ['SJ-', 'DA-', 'SK-', 'HK-', 'SQ+', 'CQ-', 'DJ-', 'HT+', 'HT*', 'DT+', 'ST*', 'S9+', 'S8+',
    #              'H6', 'S6*', 'D6-', 'C8', 'C8-', 'D5+', 'D5+', 'H5+', 'H5+', 'S5+','S5-']
    # 'C8+', 'S7-', 'H6+', 'S5+', 'C4*', 'C3+', 'S2-', 'H2-', 'C2*']

    # Example to pick the best kickers for 4 four of a kinds - 4A, 4Q, 4J
    # card_list2 = ['S4-', 'SA-', 'SQ-', 'SJ-', 'SJ+', 'SQ-', 'SA-', 'ST-', 'HJ+', 'HT*', 'H8+', 'H6*', 'H3+', 'DK+', 'DK*', 'D6*', 'D5-', 'D4*', 'D2-', 'CA*', 'CA-', 'CQ-', 'CQ+', 'CJ+', 'C2+']

    # Example to pick the best kickers for 4 four of a kinds  - 4J, 4 5's, 4 2's
    # card_list2 = ['S4-', 'S5-', 'S2-', 'SJ-', 'SJ+', 'S2-', 'S5-', 'ST-', 'HJ+', 'HT*', 'H8+', 'H6*', 'H3+', 'DK+', 'DK*', 'D6*', 'D5-', 'D4*', 'D2-', 'C5*', 'CA-', 'CQ-', 'CQ+', 'CJ+', 'C2+']

    # Example to pick the best kickers for 4 four of a kinds  - 4 J's, 4 5's, 4 2's - change CA to C6 - then added a WW
    # card_list2 = ['S4-', 'S5-', 'S2-', 'SJ-', 'SJ+', 'S2-', 'S5-', 'ST-', 'HJ+', 'HT*', 'H8+', 'WW*', 'H3+', 'DK+', 'DK*',
    #         'D6*', 'D5-', 'D4*', 'D2-', 'C5*', 'C6-', 'CQ-', 'CQ+', 'CJ+', 'C2+']

    # card_list2 = ["SA+", "DA+", "DA-", "CA+", "C8+", "HJ+", "CJ-", "CJ+", "SJ+", "H9+",
    #               "CQ+", "DT+", "HT+", "HT-", "ST+", "D9+", "S5+", "H5+", "D5+", "C5+",
    #               "D7+", "D7-", "S6+", "HK+", "C6+"]

    # card_list2 = ['WW-', 'HA*', 'SK+', 'CK*', 'CQ-', 'HJ+', 'DJ*', 'CJ+', 'CJ*', 'HT+', 'DT-', 'S9*', 'H9+', 'D9*', 'S8-', 'S8*',
    #  'H8-', 'D8*', 'S7-', 'S7*', 'D7+', 'D3+', 'C3+', 'H2*', 'C2-']
    # card_list2 = ['WW=', 'SA-', 'CA*', 'DK-', 'DK*', 'SQ+', 'DJ*', 'DJ-', 'S9+', 'H9+', 'S8+', 'H8-', 'D8*', 'H7*', 'D7-', 'H6+',
    #  'D6+', 'H5-', 'S4*', 'D4-', 'S3*', 'S3+', 'H3-', 'D3*', 'H2+']
    # card_list2 = ['WW*', 'SA-', 'CA*', 'DK-', 'CK*', 'HQ*', 'SJ-', 'SJ*', 'CJ-', 'ST+', 'CT-', 'CT*', 'S9*',
    #               'S9+', 'H9+', 'C9*', 'S8+', 'H7-', 'H7+', 'H7*', 'D7+', 'S5*', 'S4-', 'D3+', 'S2+']
    # card_list2 = ['DK*', 'CK*', 'CK-', 'DK', 'SA*', 'CA*', 'SA*', 'HA-', 'DT+', 'DT*', 'CT-', 'S4+', 'H4+', 'C4*', 'C8+', 'H8*',
    #  'DJ-', 'D9*', 'S3*', 'H3+', 'C5+', 'S5*', 'S2-', 'D8*', 'H2*']
    # card_list2 = ['WW*', 'SA*', 'HA*', 'HK*', 'HK+', 'SQ*', 'HQ*', 'DQ+', 'DJ*', 'DT+', 'D9*', 'S8-', 'D8*', 'S7*', 'D7*', 'H6-',
    #  'D6-', 'C6*', 'H5-', 'D5-', 'H4+', 'D4-', 'D4+', 'C4-', 'C4+']

    # card_list2 = ['CA+', 'HK*', 'DK*', 'DK+', 'CK-', 'SJ-', 'HJ+', 'HJ-', 'DJ-', 'S8-', 'S7+', 'H7-', 'D7*', 'C7-', 'S6+', 'H6+',
    #  'D6*', 'S5*', 'S4-', 'C4-', 'C3-', 'S2*', 'D2-', 'C2*', 'C2+']

    card_list2 = \
        ['HA*', 'HA-', 'HK-', 'HK*', 'DK+', 'SQ+', 'CQ*', 'D9-', 'C9*', 'H8*', 'S7+', 'D7-', 'C7+', 'H6+', 'S5+', 'H5+',
         'C5+', 'S4+', 'D4*', 'C4+', 'D3+', 'C3*', 'S2-', 'S2+', 'D2-']
        # ['WW+', 'CA+', 'SK+', 'DK+', 'CK-', 'SQ-', 'CQ-', 'HJ*', 'CJ*', 'ST-', 'S7*', 'H7*', 'S6-', 'H6+', 'C6+', 'S5-',
        #  'H5*', 'C5+', 'C5*', 'C4+', 'S3-', 'H3+', 'D3-', 'C3*', 'S2+']
        # ['SQ', 'DA', 'DA', 'DA', 'SK', 'SQ', 'CQ', 'DJ', 'DJ', 'HT', 'HT', 'S9', 'H9', 'D9', 'C8', 'D7',
        #  'C7', 'H6', 'D5', 'D5', 'S4', 'S4', 'C4', 'S3', 'D3']
        # ['SQ*', 'DA*', 'DA-', 'DA+', 'SK*', 'SQ+', 'CQ*', 'DJ*', 'DJ+', 'HT*', 'HT+', 'S9-', 'H9+', 'D9*', 'C8*', 'D7*',
        #  'C7*', 'H6+', 'D5+', 'D5-', 'S4*', 'S4-', 'C4*', 'S3-', 'D3-']
        # ['WW*', 'SA+', 'DA-', 'SK*', 'SQ*', 'SJ+', 'SJ*', 'ST*', 'CT+', 'S9+', 'H8+', 'D8*', 'C8-', 'C8*', 'C7-', 'H6*',
        #  'S5+', 'H5*', 'H4+', 'C4-', 'D3*', 'S2+', 'D2*', 'D2-', 'C2*']
     #    ['WW-', 'SA+', 'SA-', 'SK+', 'HQ*', 'DQ+', 'DJ-', 'HT+', 'DT-', 'CT-', 'S9*', 'D9+', 'D9-', 'H8-', 'C8*', 'S7+',
     # 'H7*', 'H7-', 'S6*', 'H6*', 'H6-', 'D6+', 'D5+', 'H4+', 'S2*']
    card_list2 = sorted(card_list2, key=suit_rank_sort, reverse=True)
    print (card_list2)
    my_hand = BestHand25Wild(card_list2)
    print (my_hand.best_25handx)

    print
