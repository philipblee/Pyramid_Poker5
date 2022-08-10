import unittest
from src.core.PokerHand import *

hand1 = PokerHand(["SA+"])
hand2 = PokerHand(["SA+", "HA-", "D5"])                 # 1 pair
hand3 = PokerHand(["S5+", "S5-", "HA*", "DA-", "SK-"])  # 2 Pair
hand4 = PokerHand(["S4", "C4", "H4"])                   # Trip
hand5 = PokerHand(["SA+", "HK+", "SQ+" , "SJ+", "ST+"]) # Straight
hand6 = PokerHand(["SA+", "S5+", "SQ+" , "SJ+", "S4+"]) # flush
hand7 = PokerHand(["SA+", "SA-", "HA*", "SK-", "CK"])   # house
hand8 = PokerHand(["SA+", "SA-", "HA*", "DA-", "SK-"])  # 4K
hand9 = PokerHand(["SA+", "SK+", "SQ+" , "SJ+", "ST+"]) # SF
hand10 = PokerHand(["SA+", "SA-", "HA*", "SA-", "CA"])   # 5K
hand11 = PokerHand(["SA+", "SK+", "SQ+" , "SJ+", "ST+", "S9-"]) # 6SF
hand12 = PokerHand(["DA+", "SA+", "SA-", "HA*", "SA-", "CA"])   # 6K
hand13 = PokerHand(["SA+", "SK+", "SQ+" , "SJ+", "ST+", "S9-", "S8+"]) # 7SF
hand14 = PokerHand(["DA+", "SA+", "SA-", "HA*", "SA-", "CA*", "DA+"])   # 7K
hand15 = PokerHand(["SA+", "SK+", "SQ+" , "SJ+", "ST+", "S9-", "S8+", "S7-"]) # 8SF
hand16 = PokerHand(["DA+", "SA+", "SA-", "HA*", "SA-", "CA*", "DA+", "DA-"])   # 8K
hand17 = PokerHand(["SA+", "SK+", "SQ+" , "SJ+", "ST+", "S9-", "S8+", "S7-", "S6"]) # 9SF
hand18 = PokerHand(["DA+", "SA+", "SA-", "HA*", "SA-", "CA*", "DA+", "DA-", "CA+"])   # 9K
hand19 = PokerHand(["SA+", "SK+", "SQ+" , "SJ+", "ST+", "S9-", "S8+", "S7-", "S6", "S5"]) # 10SF
hand20 = PokerHand(["DA+", "SA+", "SA-", "HA*", "SA-", "CA*", "DA+", "DA+", "DA-", "CA+"])   # 10K
hand21 = PokerHand(["C9-", "S4+", "H3*"])

class Test_Hand(unittest.TestCase):

    def test_Hand_HighCard(self):
        self.assertEqual(hand1.hand_key_values, [1, 14, 4])

    def test_Hand_HighCard2(self):
        self.assertEqual(hand21.hand_key_values, [1, 9, 4, 3, 1, 4, 3])

    def test_Analysis_OnePair(self):
        self.assertEqual(hand2.hand_key_values, [2, 14, 5, 4, 3, 2])

    def test_Analysis_TwoPair(self):
        self.assertEqual(hand3.hand_key_values, [3, 14, 5, 13, 3, 2, 4, 4, 4])

    def test_Analysis_Trip(self):
        self.assertEqual(hand4.hand_key_values, [4, 4, 4, 3, 1])

    def test_Analysis_Straight(self):
        self.assertEqual(hand5.hand_key_values, [5, 14, 4, 3, 4, 4, 4])

    def test_Analysis_Flush(self):
        self.assertEqual(hand6.hand_key_values, [6, 14, 12, 11, 5, 4, 4])

    def test_Analysis_House(self):
        self.assertEqual(hand7.hand_key_values, [7, 14, 13, 4, 4, 3, 4, 1])

    def test_Analysis_Fourk(self):
        self.assertEqual(hand8.hand_key_values, [8, 14, 13, 4, 4, 3, 2, 4])

    def test_Analysis_5SF(self):
        self.assertEqual(hand9.hand_key_values, [9, 14, 4])

    def test_Analysis_Fivek(self):
        self.assertEqual(hand10.hand_key_values, [10, 14, 4, 4, 4, 3, 1])

    def test_Analysis_6SF(self):
        self.assertEqual(hand11.hand_key_values, [11, 14, 4])

    def test_Analysis_Sixk(self):
        self.assertEqual(hand12.hand_key_values, [12, 14, 4, 4, 4, 3, 2, 1])

    def test_Analysis_7SF(self):
        self.assertEqual(hand13.hand_key_values, [13, 14, 4])

    def test_Analysis_Sevenk(self):
        self.assertEqual(hand14.hand_key_values, [14, 14, 4, 4, 4, 3, 2, 2, 1])

    def test_Analysis_8SF(self):
        self.assertEqual(hand15.hand_key_values, [15, 14, 4])

    def test_Analysis_Eightk(self):
        self.assertEqual(hand16.hand_key_values, [16, 14, 4, 4, 4, 3, 2, 2, 2, 1])

    def test_Analysis_9SF(self):
        self.assertEqual(hand17.hand_key_values, [17, 14, 4])

    def test_Analysis_Ninek(self):
        self.assertEqual(hand18.hand_key_values, [18, 14, 4, 4, 4, 3, 2, 2, 2, 1, 1])

    def test_Analysis_10SF(self):
        self.assertEqual(hand19.hand_key_values, [19, 14, 4])

    def test_Analysis_Tenk(self):
        self.assertEqual(hand20.hand_key_values, [20, 14, 4, 4, 4, 3, 2, 2, 2, 2, 1, 1])


suite = unittest.TestLoader().loadTestsFromTestCase(Test_Hand)
unittest.TextTestRunner(verbosity=3).run(suite)