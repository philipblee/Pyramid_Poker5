import unittest
from src.core.LegalPokerHands import *

class Test_LegalHands(unittest.TestCase):

    def test_LegalHands_1(self):
        pyramid_poker_list = ['SA!', 'SA!', 'SA*', 'SA+', 'HA+', 'CA-', 'SK-', 'SK*', 'DK-', 'SQ-', 'SQ*', 'CQ+', 'SJ*',
                              'CT*', 'S9-', 'D9+', 'S7+', 'C6-', 'S5*', 'H5+', 'C5+', 'S4-', 'C4-', 'S3-', 'C2-']
        legalhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalhands.hand6_count, 1529)

    def test_LegalHands_2(self):
        pyramid_poker_list = ['SA=', 'SA=', 'SA*', 'SA+', 'HA+', 'CA-', 'SK-', 'SK*', 'DK-', 'SQ-', 'SQ*', 'CQ+', 'SJ*',
                              'CT*', 'S9-', 'D9+', 'S7+', 'C6-', 'S5*', 'H5+', 'C5+', 'S4-', 'C4-', 'S3-', 'C2-']
        legalhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalhands.hand4_count, 38)

    def test_LegalHands_3(self):
        pyramid_poker_list = ['SA=', 'SA=', 'SA*', 'SA+', 'HA+', 'CA-', 'SK-', 'SK*', 'DK-', 'SQ-', 'SQ*', 'CQ+', 'SJ*',
                              'CT*', 'S9-', 'D9+', 'S7+', 'C6-', 'S5*', 'H5+', 'C5+', 'S4-', 'C4-', 'S3-', 'C2-']
        legalhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalhands.hand1_count, 16)

    def test_LegalHands_4(self):
        pyramid_poker_list = ['SA=', 'SA=', 'SA*', 'SA+','SK-', 'SK*', 'SQ-', 'SQ*', 'SJ*',
                              'S9-', 'S7+', 'S5*', 'S4-', 'S3-']
        legalhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalhands.hand6_count, 1369)

    def test_LegalHands_7(self):
        pyramid_poker_list = ['SA!', 'SA=', 'SA*', 'SA+','SK-', 'SK*', 'SQ-', 'SQ*', 'SJ*',
                              'S9-', 'S7+', 'S5*', 'S4-', 'S3-']
        legalhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalhands.hand6_count, 1821)

    def test_LegalHands_8(self):
        pyramid_poker_list = ['SA!', 'SA=', 'SA*', 'SA+','SK-', 'SK*', 'SQ-', 'SQ*', 'SJ*',
                              'S9-', 'S7+', 'S5*', 'S4-', 'S3-']
        legalhands = LegalPokerHands(pyramid_poker_list)
        # for h in legalhands.hand4:
        #     print (h)
        self.assertEqual(legalhands.hand4_count, 16)

    def test_LegalHands_9(self):
        pyramid_poker_list = ['SA!', 'SA=', 'SA*', 'SA+','SK-', 'SK*', 'SQ-', 'SQ*', 'SJ*',
                              'S9-', 'S7+', 'S5*', 'S4-', 'S3-']
        legalhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalhands.hand6_count, 1821)

    def test_LegalHands_10(self):
        pyramid_poker_list = ['SA!', 'S8=', 'SA*', 'SA+','SK-', 'SK*', 'SQ-', 'SQ*', 'SJ*',
                              'S9-', 'S7+', 'S5*', 'S4-', 'S3-']
        legalhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalhands.hand6_count, 1949)

    def test_LegalHands_11(self):
        pyramid_poker_list = ['SA!', 'S8=', 'SA*', 'SA+','SK-', 'SK*', 'SQ-', 'SQ*', 'SJ*',
                              'S9-', 'S7+', 'S5*', 'S4-', 'S3-']
        legalhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalhands.hand4_count, 17)

    def test_LegalHands_12(self):
        pyramid_poker_list = ['SA!', 'S8=', 'SA*', 'SA+','SK-', 'SK*', 'SQ-', 'SQ*', 'SJ*',
                              'S9-', 'S7+', 'S5*', 'S4-', 'S3-']
        legalhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalhands.hand1_count, 11)

suite = unittest.TestLoader().loadTestsFromTestCase(Test_LegalHands)
unittest.TextTestRunner(verbosity=3).run(suite)