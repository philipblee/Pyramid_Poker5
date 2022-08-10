import unittest
from src.core.PokerHand import *
import logging


class TestHandscore(unittest.TestCase):

    # Testing HandValue for 12 Hands 5K, SF, 4K, FH, F, S, T, 2P, P, HC, lowest SF and S

    def test_Handscore_ten_of_a_kind(self):
        self.assertEqual(str(PokerHand(['SA', 'SA', 'HA', 'CA', 'DA', 'CA', 'HA', 'DA', 'SA', 'HA']).score), "2014141414141414141414")

    # def test_Handscore_ten_of_a_kind(self):
    #     self.assertEqual(Hand(['SA', 'SA', 'HA', 'CA', 'DA', 'CA', 'HA', 'DA', 'SA', 'HA']).points, 2014141414141414141414)

    def test_Handscore_ten_card_straight_flush(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7', 'S6', 'S5']).score), "1914131211100908070605")

    def test_Handscore_nine_of_a_kind(self):
        self.assertEqual(str(PokerHand(['SA', 'SA', 'HA', 'CA', 'DA', 'CA', 'HA', 'SA', 'HA']).score), "18141414141414141414")

    def test_Handscore_nine_card_straight_flush(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7', 'S6']).score), "17141312111009080706")

    def test_Handscore_eight_of_a_kind(self):
        self.assertEqual(str(PokerHand(['SA', 'SA', 'HA', 'CA', 'DA', 'CA', 'HA', 'SA']).score), "161414141414141414")

    def test_Handscore_eight_card_straight_flush(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7']).score), "151413121110090807")

    def test_Handscore_eight_card_straight_flush(self):
        self.assertEqual(str(PokerHand(['SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7', 'S6']).score), "151312111009080706")

    def test_Handscore_seven_of_a_kind(self):
        self.assertEqual(str(PokerHand(['SA', 'SA', 'HA', 'CA', 'DA', 'CA', 'HA']).score), "1414141414141414")

    def test_Handscore_seven_card_straight_flush(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8']).score), "1314131211100908")

    def test_Handscore_six_of_a_kind(self):
        self.assertEqual(str(PokerHand(['SA', 'SA', 'HA', 'CA', 'DA', 'CA']).score), "12141414141414")

    def test_Handscore_six_card_straight_flush(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'SJ', 'ST', 'S9']).score), "11141312111009")

    def test_Handscore_five_of_a_kind(self):
        self.assertEqual(str(PokerHand(['SA', 'SA', 'HA', 'CA', 'DA']).score), "101414141414")

    def test_Handscore_straight_flush(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'SJ', 'ST']).score), "91413121110")

    def test_Handscore_four_of_a_kind(self):
        self.assertEqual(str(PokerHand(['SA', 'SA', 'DA', 'CA', 'ST']).score), "81414141410")

    def test_Handscore_full_house_3A2T(self):
        self.assertEqual(str(PokerHand(['SA', 'SA', 'HA', 'DT', 'ST']).score), "71414141010")

    def test_Handscore_full_house_3T2A(self):
        self.assertEqual(str(PokerHand(['SA', 'SA', 'CT', 'DT', 'ST']).score), "71414101010")

    def test_Handscore_flush(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'SJ', 'S4']).score), "61413121104")

    def test_Handscore_straight(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'SJ', 'DT']).score), "51413121110")

    def test_Handscore_trip(self):
        self.assertEqual(str(PokerHand(['SA', 'DA', 'HA', 'SJ', 'ST']).score), "41414141110")

    def test_Handscore_two_pair(self):
        self.assertEqual(str(PokerHand(['SA', 'DA', 'SQ', 'DQ', 'CT']).score), "31414121210")

    def test_Handscore_pair(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'DQ', 'ST']).score), "21413121210")

    def test_Handscore_high_card(self):
        self.assertEqual(str(PokerHand(['SA', 'C3', 'SQ', 'SJ', 'ST']).score), "11412111003")

    def test_Handscore_straight_flush_low(self):
        self.assertEqual(str(PokerHand(['SA', 'S2', 'S3', 'S4', 'S5']).score), "91405040302")

    def test_Handscore_straight_low(self):
        self.assertEqual(str(PokerHand(['SA', 'D2', 'H3', 'C4', 'S5']).score), "51405040302")

    def test_Handscore_straight_flush(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'SJ', 'ST']).score), "91413121110")


    # test 12 cases for get_hand_score

    def test_hand_score_five_of_a_kind(self):
        self.assertEqual(str(PokerHand(['SA', 'SA', 'HA', 'CA', 'DA']).score), "101414141414")

    def test_get_hand_score_straight_flush(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'SJ', 'ST']).score), "91413121110")

    def test_get_hand_score_four_of_a_kind(self):
        self.assertEqual(str(PokerHand(['SA', 'SA', 'DA', 'CA', 'ST']).score), "81414141410")

    def test_get_hand_score_full_house_3A2T(self):
        self.assertEqual(str(PokerHand(['SA', 'SA', 'HA', 'DT', 'ST']).score), "71414141010")

    def test_get_hand_score_full_house_3T2A(self):
        self.assertEqual(str(PokerHand(['SA', 'SA', 'CT', 'DT', 'ST']).score), "71414101010")

    def test_get_hand_score_flush(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'SJ', 'S4']).score), "61413121104")

    def test_get_hand_score_straight(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'SJ', 'DT']).score), "51413121110")

    def test_get_hand_score_trip(self):
        x = ['SA', 'DA', 'HA', 'SJ', 'ST']
        self.assertEqual(str(PokerHand(['SA', 'DA', 'HA', 'SJ', 'ST']).score), "41414141110")

    def test_get_hand_score_two_pair(self):
        self.assertEqual(str(PokerHand(['SA', 'DA', 'SQ', 'DQ', 'CT']).score), "31414121210")

    def test_get_hand_score_one_pair(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'DQ', 'ST']).score), "21413121210")

    def test_get_hand_score_high_card(self):
        self.assertEqual(str(PokerHand(['SA', 'C3', 'SQ', 'SJ', 'ST']).score), "11412111003")

    def test_get_hand_score_straightflush_low(self):
        self.assertEqual(str(PokerHand(['SA', 'S2', 'S3', 'S4', 'S5']).score), "91405040302")

    def test_get_hand_score_straight_low(self):
        self.assertEqual(str(PokerHand(['SA', 'D2', 'H3', 'C4', 'S5']).score), "51405040302")




  # test 12 cases for HandType
    def test_HandType_five_of_a_kind(self):
        x = PokerHand(['SA', 'SA', 'HA', 'CA', 'DA'])
        self.assertEqual(str(x.get_hand_type()), "HandType.FiveK")

    def test_HandType_straight_flush(self):
        x = PokerHand(['SA', 'SK', 'SQ', 'SJ', 'ST'])
        self.assertEqual(str(x.get_hand_type()), "HandType.FiveSF")

    def test_HandType_four_of_a_kind(self):
        x = PokerHand(['SA', 'SA', 'DA', 'CA', 'ST'])
        self.assertEqual(str(x.get_hand_type()), "HandType.FourK")

    def test_HandType_full_house(self):
        x = PokerHand(['SA', 'SA', 'HA', 'DT', 'ST'])
        self.assertEqual(str(x.get_hand_type()), "HandType.FullH")

    def test_HandType_flush(self):
        x = PokerHand(['SA', 'SK', 'SQ', 'SJ', 'S4'])
        self.assertEqual(str(x.get_hand_type()), "HandType.Flush")

    def test_HandType_straight(self):
        x = PokerHand(['SA', 'SK', 'SQ', 'SJ', 'DT'])
        self.assertEqual(str(x.get_hand_type()), "HandType.Straight")

    def test_HandType_trip(self):
        x = PokerHand(['SA', 'DA', 'HA', 'SJ', 'ST'])
        self.assertEqual(str(x.get_hand_type()), "HandType.Trip")

    def test_HandType_two_pair(self):
        x = PokerHand(['SA', 'DA', 'SQ', 'DQ', 'CT'])
        self.assertEqual(str(x.get_hand_type()), "HandType.TwoP")

    def test_HandType_pair(self):
        x = PokerHand(['SA', 'SK', 'SQ', 'DQ', 'ST'])
        self.assertEqual(str(x.get_hand_type()), "HandType.OneP")

    def test_HandType_high_card(self):
        x = PokerHand(['SA', 'C3', 'SQ', 'SJ', 'ST'])
        self.assertEqual(str(x.get_hand_type()), "HandType.HighC")

    def test_HandType_straight_flush_low(self):
        x = PokerHand(['SA', 'S2', 'S3', 'S4', 'S5'])
        self.assertEqual(str(x.get_hand_type()), "HandType.FiveSF")

    def test_HandType_straight_low(self):
        x = PokerHand(['SA', 'D2', 'H3', 'C4', 'S5'])
        self.assertEqual(str(x.get_hand_type()), "HandType.Straight")

    # Hand_short_score

    def test_Hand_short_score_five_of_a_kind(self):
        self.assertEqual(str(PokerHand(['SA', 'SA', 'HA', 'CA', 'DA']).short_score), "101400")

    def test_Hand_short_score_straight_flush(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'SJ', 'ST']).short_score), "91413")

    def test_Hand_short_score_four_of_a_kind(self):
        self.assertEqual(str(PokerHand(['SA', 'SA', 'DA', 'CA', 'ST']).short_score), "81410")

    def test_Hand_short_score_full_house(self):
        self.assertEqual(str(PokerHand(['SA', 'SA', 'HA', 'DT', 'ST']).short_score), "71410")

    def test_Hand_short_score_full_house_3T2A(self):
        x = ['SA', 'SA', 'CT', 'DT', 'ST']
        self.assertEqual(str(PokerHand(['SA', 'SA', 'CT', 'DT', 'ST']).short_score), "71014")

    def test_Hand_short_score_flush(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'SJ', 'S4']).short_score), "61413")

    def test_Hand_short_score_straight(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'SJ', 'DT']).short_score), "51413")

    def test_Hand_short_score_trip(self):
        self.assertEqual(str(PokerHand(['SA', 'DA', 'HA', 'SJ', 'ST']).short_score), "41461")

    def test_Hand_short_score_trip2(self):
        self.assertEqual(str(PokerHand(['ST', 'DA', 'HT', 'SJ', 'ST']).short_score), "41064")

    def test_Hand_short_score_two_pair(self):
        self.assertEqual(str(PokerHand(['SA', 'DA', 'SQ', 'DQ', 'CT']).short_score), "31412")

    def test_Hand_short_score_pair(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'DQ', 'ST']).short_score), "21214")

    def test_Hand_short_score_high_card(self):
        self.assertEqual(str(PokerHand(['SA', 'C3', 'SQ', 'SJ', 'ST']).short_score), "11412")

    def test_Hand_short_score_straight_flush_low(self):
        self.assertEqual(str(PokerHand(['SA', 'S2', 'S3', 'S4', 'S5']).short_score), "91405")

    def test_Hand_short_score_straight_low(self):
        self.assertEqual(str(PokerHand(['SA', 'D2', 'H3', 'C4', 'S5']).short_score), "51405")

    def test_Hand_short_score_straight_flush(self):
        self.assertEqual(str(PokerHand(['SA', 'SK', 'SQ', 'SJ', 'ST']).short_score), "91413")

suite = unittest.TestLoader().loadTestsFromTestCase(TestHandscore)
unittest.TextTestRunner(verbosity=3).run(suite)