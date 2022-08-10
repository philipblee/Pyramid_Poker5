import unittest
from src.core.BestHand25 import *

class Test_BestHand25(unittest.TestCase):

    # Testing BestHand25 - remember some times these tests may fail because sometimes C6* and C6+ can be alternatively be in the solution (same card, different deck)

    def test_BestHand25_1(self):
        pyramid_poker_list = ['S8++', 'S7++', 'S6-', 'S9*', 'S5-', 'SQ*', 'SK-', 'HK+', 'HK*', 'DK-', 'HT+', 'S4+',
                                  'D4-', 'C4*', 'C4-', 'C9+', 'C9*', 'H7+', 'D6-', 'D6-', 'D8+', 'DA*', 'S3+', 'H2*',
                                  'H5-']
        best_hand = BestHand25(pyramid_poker_list, -9999)
        test_hand = best_hand.best_pyramid_poker_hand[6:0:-1]
        print ("\ntest_hand", test_hand)
        answer = [['S9*', 'S8++', 'S7++', 'S6-', 'S5-'], ['SK-', 'HK+', 'HK*', 'DK-', 'SQ*'],
                    ['HT+','S4+', 'D4-', 'C4*', 'C4-'], ['C9+', 'C9*', 'H7+'], ['D8+', 'D6-', 'D6-'], ['DA*']]
        print ("answer   ", answer)
        self.assertEqual(test_hand,
                         [['S9*', 'S8++', 'S7++', 'S6-', 'S5-'], ['SK-', 'HK+', 'HK*', 'DK-', 'SQ*'],
                          ['HT+', 'S4+', 'D4-', 'C4*', 'C4-'], ['C9+', 'C9*', 'H7+'], ['D8+', 'D6-', 'D6-'], ['DA*']])

    def test_BestHand25_2(self):
        pyramid_poker_list = ['S8++', 'S7++', 'S6-', 'S9*', 'S5-', 'SQ*', 'SK-', 'HK+', 'HK*', 'DK-', 'HT+', 'S4+',
                                  'D4-', 'C4*', 'C4-', 'C9+', 'C9*', 'H7+', 'D6-', 'D6-', 'D8+', 'DA*', 'S3+', 'H2*',
                                  'H5-']
        best_hand = BestHand25(pyramid_poker_list, -9999)
        test_points = best_hand.best_hand_points[0]
        print ("\nall test_points", best_hand.best_hand_points)
        print ("tot test_points", test_points)
        self.assertGreater(test_points, 780)

    def test_BestHand25_3(self):
        pyramid_poker_list = ['SA-', 'DA+', 'DA-', 'CA*', 'HK*', 'CK*', 'HQ-', 'DQ*', 'SJ-', 'HT+', 'H9*', 'S8*', 'S8+', 'D8*', 'H7*', 'H7-',
                              'C6+', 'C6+', 'D5*', 'S4-', 'S4*', 'S3+', 'H3*', 'H3-', 'C2+']
        best_hand = BestHand25(pyramid_poker_list, -9999)
        test_hand = best_hand.best_pyramid_poker_hand[6:0:-1]
        self.assertEqual(test_hand,
                         [['CA*', 'CK*', 'C6+', 'C6+', 'C2+'], ['HQ-', 'HT+', 'H9*', 'H7*', 'H7-'],
                          ['SA-', 'DA+', 'DA-'], ['S8*', 'S8+', 'D8*'], ['S3+', 'H3*', 'H3-'], ['HK*']])

    def test_BestHand25_4(self):
        pyramid_poker_list = ['S8++', 'S7++', 'S6-', 'S9*', 'S5-', 'SQ*', 'SK-', 'HK+', 'HK*', 'DK-', 'HT+', 'S4+',
                                  'D4-', 'C4*', 'C4-', 'C9+', 'C9*', 'H7+', 'D6-', 'D6-', 'D8+', 'DA*', 'S3+', 'H2*',
                                  'H5-']
        best_hand = BestHand25(pyramid_poker_list, -9999)
        test_points = best_hand.best_hand_points[0]
        self.assertGreater(test_points, -690)

suite = unittest.TestLoader().loadTestsFromTestCase(Test_BestHand25)
unittest.TextTestRunner(verbosity=3).run(suite)