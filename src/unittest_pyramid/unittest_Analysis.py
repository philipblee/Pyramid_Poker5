import unittest
from src.core.Analysis import *

class Test_Analysis(unittest.TestCase):

    # Testing Analysis for 12 Hands 5K, SF, 4K, FH, F, S, T, 2P, P, HC, lowest SF and S
    # decided to not use rows 7, 8, 9, 10 to store 5 card straight flushes because
    #    this methodolgy does not address 6, 7, 8, 9, 10 card SF's, I opted for using
    #    rows 45, 46, 47, 48, 49, 50 to display lists of 5-10 card SF's

    def test_Analysis_ten_of_a_kind(self):
        self.assertEqual(Analysis(['SA', 'SA', 'HA', 'CA', 'DA', 'CA', 'HA', 'DA', 'SA', 'HA']).suit_rank_array[5][14], 10)

    def test_Analysis_ten_card_straight_flush_S(self):
        self.assertEqual(Analysis(['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7', 'S6', 'S5']).suit_rank_array[6], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 6])

    def test_Analysis_ten_card_straight_flush_S(self):
        self.assertEqual(Analysis(['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7', 'S6', 'S5']).suit_rank_array[6],
                         [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 6])
        self.assertEqual(Analysis(['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7', 'S6', 'S5']).suit_rank_array[45],
                         [('ST', 'SJ', 'SQ', 'SK', 'SA'),
                          ('S9', 'ST', 'SJ', 'SQ', 'SK'),
                          ('S8', 'S9', 'ST', 'SJ', 'SQ'),
                          ('S7', 'S8', 'S9', 'ST', 'SJ'),
                          ('S6', 'S7', 'S8', 'S9', 'ST'),
                          ('S5', 'S6', 'S7', 'S8', 'S9')])
        self.assertEqual(Analysis(['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7', 'S6', 'S5']).suit_rank_array[46],
                         [('S9', 'ST', 'SJ', 'SQ', 'SK', 'SA'),
                          ('S8', 'S9', 'ST', 'SJ', 'SQ', 'SK'),
                          ('S7', 'S8', 'S9', 'ST', 'SJ', 'SQ'),
                          ('S6', 'S7', 'S8', 'S9', 'ST', 'SJ'),
                          ('S5', 'S6', 'S7', 'S8', 'S9', 'ST')
                          ])
        self.assertEqual(Analysis(['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7', 'S6', 'S5']).suit_rank_array[47],
                         [('S8', 'S9', 'ST', 'SJ', 'SQ', 'SK', 'SA'),
                          ('S7','S8', 'S9', 'ST', 'SJ', 'SQ', 'SK'),
                          ('S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ'),
                          ('S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ')
                          ])
        self.assertEqual(Analysis(['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7', 'S6', 'S5']).suit_rank_array[48],
                         [('S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK', 'SA'),
                          ('S6', 'S7','S8', 'S9', 'ST', 'SJ', 'SQ', 'SK'),
                          ('S5','S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ'),
                          ])
        self.assertEqual(Analysis(['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7', 'S6', 'S5']).suit_rank_array[49],
                         [('S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK', 'SA'),
                          ('S5', 'S6', 'S7','S8', 'S9', 'ST', 'SJ', 'SQ', 'SK'),
                          ])
        self.assertEqual(Analysis(['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7', 'S6', 'S5']).suit_rank_array[50],
                         [('S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK', 'SA'),
                          ])
    def test_Analysis_ten_card_straight_flush_H(self):
        self.assertEqual(Analysis(['HA', 'HK', 'HQ', 'HJ', 'HT', 'H9', 'H8', 'H7', 'H6', 'H5']).suit_rank_array[6],
                          [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 6])

    def test_Analysis_ten_card_straight_flush_D(self):
        self.assertEqual(Analysis(['DA', 'DK', 'DQ', 'DJ', 'DT', 'D9', 'D8', 'D7', 'D6', 'D5']).suit_rank_array[6],
                         [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 6])

    def test_Analysis_ten_card_straight_flush_C(self):
        self.assertEqual(Analysis(['CA', 'CK', 'CQ', 'CJ', 'CT', 'C9', 'C8', 'C7', 'C6', 'C5']).suit_rank_array[6],
                         [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 6])

    def test_Analysis_ten_card_straight_flush_S_All_45to50(self):
        ten_card_straight_flush = ['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7', 'S6', 'S5']
        self.assertEqual(Analysis(ten_card_straight_flush).suit_rank_array[45], [('ST', 'SJ', 'SQ', 'SK', 'SA'), ('S9', 'ST', 'SJ', 'SQ', 'SK'),
                                 ('S8', 'S9', 'ST', 'SJ', 'SQ'), ('S7', 'S8', 'S9', 'ST', 'SJ'), ('S6', 'S7', 'S8', 'S9', 'ST'), ('S5', 'S6', 'S7', 'S8', 'S9')])
        self.assertEqual(Analysis(ten_card_straight_flush).suit_rank_array[46], [('S9', 'ST', 'SJ', 'SQ', 'SK', 'SA'),
                                 ('S8', 'S9', 'ST', 'SJ', 'SQ', 'SK'), ('S7', 'S8', 'S9', 'ST', 'SJ', 'SQ'),
                                 ('S6', 'S7', 'S8', 'S9', 'ST', 'SJ'), ('S5', 'S6', 'S7', 'S8', 'S9', 'ST')])
        self.assertEqual(Analysis(ten_card_straight_flush).suit_rank_array[47], [('S8', 'S9', 'ST', 'SJ', 'SQ', 'SK', 'SA'),
                                ('S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK'), ('S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ'),
                                ('S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ')])
        self.assertEqual(Analysis(ten_card_straight_flush).suit_rank_array[48], [('S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK', 'SA'),
                                ('S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK'), ('S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ')])
        self.assertEqual(Analysis(ten_card_straight_flush).suit_rank_array[49], [('S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK', 'SA'),
                                ('S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK')])
        self.assertEqual(Analysis(ten_card_straight_flush).suit_rank_array[50],
                                [('S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK', 'SA')])

    def test_Analysis_ten_card_straight_flush_S_All_45to50(self):
        ten_card_straight_flush = ['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7', 'S6', 'S5']
        self.assertEqual(Analysis(ten_card_straight_flush).suit_rank_array[45], [('ST', 'SJ', 'SQ', 'SK', 'SA'), ('S9', 'ST', 'SJ', 'SQ', 'SK'),
                                 ('S8', 'S9', 'ST', 'SJ', 'SQ'), ('S7', 'S8', 'S9', 'ST', 'SJ'), ('S6', 'S7', 'S8', 'S9', 'ST'), ('S5', 'S6', 'S7', 'S8', 'S9')])
        self.assertEqual(Analysis(ten_card_straight_flush).suit_rank_array[46], [('S9', 'ST', 'SJ', 'SQ', 'SK', 'SA'),
                                 ('S8', 'S9', 'ST', 'SJ', 'SQ', 'SK'), ('S7', 'S8', 'S9', 'ST', 'SJ', 'SQ'), ('S6', 'S7', 'S8', 'S9', 'ST', 'SJ'), ('S5', 'S6', 'S7', 'S8', 'S9', 'ST')])
        self.assertEqual(Analysis(ten_card_straight_flush).suit_rank_array[47], [('S8', 'S9', 'ST', 'SJ', 'SQ', 'SK', 'SA'),
                                ('S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK'), ('S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ'), ('S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ')])
        self.assertEqual(Analysis(ten_card_straight_flush).suit_rank_array[48], [('S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK', 'SA'),
                                ('S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK'), ('S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ')])
        self.assertEqual(Analysis(ten_card_straight_flush).suit_rank_array[49], [('S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK', 'SA'),
                                ('S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK')])
        self.assertEqual(Analysis(ten_card_straight_flush).suit_rank_array[50],
                                [('S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK', 'SA')])

    def test_Analysis_nine_of_a_kind(self):
        self.assertEqual(Analysis(['SA', 'SA', 'HA', 'CA', 'DA', 'CA', 'HA', 'SA', 'HA']).suit_rank_array[5][14], 9)

    # def test_Analysis_nine_card_straight_flush(self):
    #     self.assertEqual(Analysis(['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7', 'S6']).suit_rank_array[7], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 5, 5])

    def test_Analysis_eight_of_a_kind(self):
        self.assertEqual(Analysis(['SA', 'SA', 'HA', 'CA', 'DA', 'CA', 'HA', 'SA']).suit_rank_array[5][14], 8)

    # def test_Analysis_eight_card_straight_flush(self):
    #     self.assertEqual(Analysis(['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7']).suit_rank_array[7], [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])
    #
    # def test_Analysis_eight_card_straight_flush(self):
    #     self.assertEqual(Analysis(['SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7', 'S6']).suit_rank_array[7], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 4, 4])
    #
    # def test_Analysis_seven_of_a_kind(self):
    #     self.assertEqual(Analysis(['SA', 'SA', 'HA', 'CA', 'DA', 'CA', 'HA']).suit_rank_array[5][14], 7)
    #
    # def test_Analysis_seven_card_straight_flush(self):
    #     self.assertEqual(Analysis(['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8']).suit_rank_array[7], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 3, 3])

    def test_Analysis_six_of_a_kind(self):
        self.assertEqual(Analysis(['SA', 'SA', 'HA', 'CA', 'DA', 'CA']).suit_rank_array[5][14], 6)

    # def test_Analysis_six_card_straight_flush(self):
    #     self.assertEqual(Analysis(['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9']).suit_rank_array[7], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 2, 2])

    def test_Analysis_five_of_a_kind(self):
        self.assertEqual(Analysis(['SA', 'SA', 'HA', 'CA', 'DA']).suit_rank_array[5][14], 5)

    # def test_Analysis_straight_flush(self):
    #     self.assertEqual(Analysis(['SA', 'SK', 'SQ', 'SJ', 'ST']).suit_rank_array[7], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1])

    def test_Analysis_straight_ace(self):
        self.assertEqual(Analysis(['SA', 'SK', 'SQ', 'SJ', 'HT']).suit_rank_array[6], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1])

    def test_Analysis_straight_flush_king(self):
        self.assertEqual(Analysis(['S9', 'SK', 'SQ', 'SJ', 'HT']).suit_rank_array[6], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1])

    def test_Analysis_straight_flush_king_row25_neg(self):
        self.assertEqual(Analysis(['S9', 'SK', 'SQ', 'SJ', 'HT']).suit_rank_array[25][:], [])


    def test_Analysis_straight_two(self):
        self.assertEqual(Analysis(['S9', 'SK', 'SQ', 'SJ', 'HT', 'CA']).suit_rank_array[6], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 2])

    def test_Analysis_straight_three(self):
        self.assertEqual(Analysis(['S9', 'SK', 'SQ', 'SJ', 'HT', 'CA', 'D2', 'D3', 'H4', 'H5']).suit_rank_array[6], [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 3])

    def test_Analysis_four_of_a_kind(self):
        self.assertEqual(Analysis(['SA', 'SA', 'DA', 'CA', 'ST']).suit_rank_array[5][14], 4)

    def test_Analysis_full_house(self):
        self.assertEqual(Analysis(['SA', 'SA', 'DA', 'CT', 'ST']).suit_rank_array[5][14], 3)
        self.assertEqual(Analysis(['SA', 'SA', 'DA', 'CT', 'ST']).suit_rank_array[5][10], 2)

    def test_Analysis_flush_spades(self):
        self.assertEqual(Analysis(['SA', 'SK', 'SQ', 'SJ', 'S3']).suit_rank_array[21], ['S3', 'SJ', 'SQ', 'SK', 'SA'])

    def test_Analysis_flush_hearts(self):
        self.assertEqual(Analysis(['HA', 'HT', 'H8', 'H4', 'H3']).suit_rank_array[22], ['H3', 'H4', 'H8', 'HT', 'HA'])

    def test_Analysis_flush_diamonds(self):
        self.assertEqual(Analysis(['DQ', 'DJ', 'D7', 'D5', 'D2']).suit_rank_array[23], ['D2', 'D5', 'D7', 'DJ', 'DQ'])

    def test_Analysis_flush_clubs(self):
        self.assertEqual(Analysis(['CA', 'CK', 'CQ', 'C3']).suit_rank_array[24], ['C3', 'CQ', 'CK', 'CA'])

suite = unittest.TestLoader().loadTestsFromTestCase(Test_Analysis)
unittest.TextTestRunner(verbosity=3).run(suite)