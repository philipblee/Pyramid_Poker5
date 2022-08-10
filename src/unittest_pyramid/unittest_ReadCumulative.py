import unittest
from src.core.ReadCumulative import *
import logging


class TestReadCumulative(unittest.TestCase):
    test = ReadCumulative()
    for item in test.item:
        print (item)

    # def test_ReadProbabilityNew(self):
    #     self.assertGreater(test.score_prob[101400],98)

suite = unittest.TestLoader().loadTestsFromTestCase(TestReadCumulative)
unittest.TextTestRunner(verbosity=3).run(suite)