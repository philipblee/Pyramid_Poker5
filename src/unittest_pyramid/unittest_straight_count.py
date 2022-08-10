import unittest
from src.core.straight_count import *

class Test_straight_count(unittest.TestCase):

    # Testing HandValue for 12 Hands 5K, SF, 4K, FH, F, S, T, 2P, P, HC, lowest SF and S

    def test_straight_count5_10_neg(self):
        rankcount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.assertEqual(straight_count(rankcount, 5), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_straight_count5_10_pos(self):
        rankcount = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0]
        self.assertEqual(straight_count(rankcount, 5), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1])

    def test_straight_count5_10_pos_2(self):
        rankcount = [0,0,0,0,0,0,0,0,0,0,2,1,1,1,1,0]
        self.assertEqual(straight_count(rankcount, 5), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2])

    def test_straight_count5_10_pos_3(self):
        rankcount = [0,0,0,0,0,0,0,0,0,0,2,2,1,1,1,0]
        self.assertEqual(straight_count(rankcount, 5), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4])

    def test_straight_count5_10_pos_4(self):
        rankcount = [0,0,0,0,0,0,0,0,0,0,2,1,1,3,1,0]
        self.assertEqual(straight_count(rankcount, 5), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 6])

    def test_straight_count5_10_pos_5(self):
        rankcount = [0,0,0,0,0,0,0,0,0,0,2,4,3,1,3,0]
        self.assertEqual(straight_count(rankcount, 5), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 72, 0, 0, 0, 0, 72])

    def test_straight_count5_1_pos(self):
        rankcount = [0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0]
        self.assertEqual(straight_count(rankcount, 5), [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

    def test_straight_count5_6_pos(self):
        rankcount = [0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0]
        self.assertEqual(straight_count(rankcount, 5), [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1])

    def test_straight_count6_9_neg(self):
        rankcount = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0]
        self.assertEqual(straight_count(rankcount, 6), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_straight_count6_9_pos(self):
        rankcount = [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0]
        self.assertEqual(straight_count(rankcount, 6), [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1])
        
    def test_straight_count7_8_neg(self):
        rankcount = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0]
        self.assertEqual(straight_count(rankcount, 6), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_straight_count7_8_pos(self):
        rankcount = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0]
        self.assertEqual(straight_count(rankcount, 7), [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1])

    def test_straight_count8_7_neg(self):
        rankcount = [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0]
        self.assertEqual(straight_count(rankcount, 8), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_straight_count8_7_pos(self):
        rankcount = [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0]
        self.assertEqual(straight_count(rankcount, 8), [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1])

    def test_straight_count9_6_neg(self):
        rankcount = [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0]
        self.assertEqual(straight_count(rankcount, 9), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_straight_count9_6_pos(self):
        rankcount = [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0]
        self.assertEqual(straight_count(rankcount, 9), [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1])

    def test_straight_count10_5_neg(self):
        rankcount = [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0]
        self.assertEqual(straight_count(rankcount, 10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_straight_count10_5_pos(self):
        rankcount = [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0]
        self.assertEqual(straight_count(rankcount, 10), [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

suite = unittest.TestLoader().loadTestsFromTestCase(Test_straight_count)
unittest.TextTestRunner(verbosity=3).run(suite)