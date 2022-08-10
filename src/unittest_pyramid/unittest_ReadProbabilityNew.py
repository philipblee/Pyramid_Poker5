import unittest
from src.core.ReadProbability import *
import logging


class TestReadProbabilityNew(unittest.TestCase):

    # Testing HandValue for 12 Hands 5K, SF, 4K, FH, F, S, T, 2P, P, HC, lowest SF and S

    test = ReadProbability()

    # def test_ReadProbabilityNew(self):
    #     self.assertGreater(test.score_prob[101400],98)

suite = unittest.TestLoader().loadTestsFromTestCase(TestReadProbabilityNew)
unittest.TextTestRunner(verbosity=3).run(suite)