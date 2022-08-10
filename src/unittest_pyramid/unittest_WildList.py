import unittest
from src.core.WildList import *

class TestWildList(unittest.TestCase):


    def test_wildlist1(self):
        wildlist = WildList(['WW-', 'SA*', 'SA-', 'HA*', 'HA-', 'CA*', 'DK-', 'SQ+', 'SQ-',
                             'SJ+', 'HT+', 'CT*', 'S9*', 'S8*', 'S8+', 'C8*', 'S7-', 'S7*',
                             'H6*', 'C5+', 'C4*', 'H3*', 'C3*', 'C3+', 'H2+'])
        self.assertEqual(wildlist.wild_card_combinations, [('SA*',), ('SQ*',), ('ST*',), ('S8*',), ('S7*',), ('S3*',), ('C2*',)])

    def test_wildlist2(self):
        wildlist = WildList(['WW-', 'WW+', 'SK*', 'SK-', 'HK*', 'DK-', 'SQ*', 'CQ*', 'HJ-', 'ST-', 'HT-', 'CT*',
                    'CT-', 'S9*', 'D9-', 'C9-', 'H8-', 'D8*', 'C8+', 'D7+', 'C7+', 'D6+', 'S5*', 'C4*', 'D3+'])
        self.assertEqual(wildlist.wild_card_combinations,
                         [('SK*', 'SK*'), ('SK*', 'SQ*'), ('SK*', 'SJ*'), ('SK*', 'ST*'), ('SK*', 'S9*'),
                          ('SK*', 'S8*'), ('SK*', 'S7*'), ('SK*', 'DT*'), ('SK*', 'D5*'), ('SK*', 'CJ*'),
                          ('SK*', 'C6*'), ('SQ*', 'SQ*'), ('SQ*', 'SJ*'), ('SQ*', 'ST*'), ('SQ*', 'S9*'),
                          ('SQ*', 'S8*'), ('SQ*', 'S7*'), ('SQ*', 'DT*'), ('SQ*', 'D5*'), ('SQ*', 'CJ*'),
                          ('SQ*', 'C6*'), ('SJ*', 'SJ*'), ('SJ*', 'ST*'), ('SJ*', 'S9*'), ('SJ*', 'S8*'),
                          ('SJ*', 'S7*'), ('SJ*', 'DT*'), ('SJ*', 'D5*'), ('SJ*', 'CJ*'), ('SJ*', 'C6*'),
                          ('ST*', 'ST*'), ('ST*', 'S9*'), ('ST*', 'S8*'), ('ST*', 'S7*'), ('ST*', 'DT*'),
                          ('ST*', 'D5*'), ('ST*', 'CJ*'), ('ST*', 'C6*'), ('S9*', 'S9*'), ('S9*', 'S8*'),
                          ('S9*', 'S7*'), ('S9*', 'DT*'), ('S9*', 'D5*'), ('S9*', 'CJ*'), ('S9*', 'C6*'),
                          ('S8*', 'S8*'), ('S8*', 'S7*'), ('S8*', 'DT*'), ('S8*', 'D5*'), ('S8*', 'CJ*'),
                          ('S8*', 'C6*'), ('S7*', 'S7*'), ('S7*', 'DT*'), ('S7*', 'D5*'), ('S7*', 'CJ*'),
                          ('S7*', 'C6*'), ('DT*', 'DT*'), ('DT*', 'D5*'), ('DT*', 'CJ*'), ('DT*', 'C6*'),
                          ('D5*', 'D5*'), ('D5*', 'CJ*'), ('D5*', 'C6*'), ('CJ*', 'CJ*'), ('CJ*', 'C6*'), ('C6*', 'C6*')])

    def test_wildlist3(self):
        wildlist = WildList(['WW*', 'HA*', 'DA+', 'DA*', 'HK-', 'DK*', 'CK+', 'SJ-', 'ST+', 'DT-', 'S9*', 'H9+'
                            , 'D9+', 'D9-', 'D7+', 'C7*', 'S6-', 'H6-', 'C6*', 'S5-', 'S4-', 'H4-', 'D4+', 'S3+', 'D3-'])
        self.assertEqual(wildlist.wild_card_combinations,
                         [('SA*',), ('SK*',), ('ST*',), ('S9*',), ('S7*',), ('S6*',), ('S4*',), ('S3*',), ('S2*',)])

    def test_wildlist4(self):
        wildlist = WildList(['WW*', 'SA*', 'CA*', 'CK-', 'HQ*', 'SJ+', 'DJ+', 'ST-', 'HT+', 'DT+', 'CT+',
                             'S9*', 'D9*', 'C9*', 'S8-', 'C8+', 'S6*', 'S5+', 'C5-', 'S4+', 'H4-', 'C4+', 'D3*', 'S2*', 'H2+'])
        self.assertEqual(wildlist.wild_card_combinations,
                         [('SA*',), ('SQ*',), ('SJ*',), ('ST*',), ('S9*',), ('S8*',), ('S7*',), ('S5*',), ('S4*',),
                          ('S3*',), ('S2*',)])

    def test_wildlist5(self):
        wildlist = WildList(['WW*', 'WW+', 'SA+', 'SA*', 'HA+', 'SK+', 'HK+', 'HK-', 'SQ*', 'CQ+',
                             'DJ*', 'CJ+', 'S9+', 'D9*', 'H8-', 'S7-', 'D7+', 'C7*', 'S6*', 'C6-', 'S4*', 'H4*', 'C4+', 'S2+', 'C2-'])
        self.assertEqual(wildlist.wild_card_combinations,
                         [('SA*', 'SA*'), ('SA*', 'SK*'), ('SA*', 'SQ*'), ('SA*', 'SJ*'), ('SA*', 'S9*'),
                          ('SA*', 'S7*'), ('SA*', 'S6*'), ('SA*', 'S4*'), ('SA*', 'S2*'), ('SK*', 'SK*'),
                          ('SK*', 'SQ*'), ('SK*', 'SJ*'), ('SK*', 'S9*'), ('SK*', 'S7*'), ('SK*', 'S6*'),
                          ('SK*', 'S4*'), ('SK*', 'S2*'), ('SQ*', 'SQ*'), ('SQ*', 'SJ*'), ('SQ*', 'S9*'),
                          ('SQ*', 'S7*'), ('SQ*', 'S6*'), ('SQ*', 'S4*'), ('SQ*', 'S2*'), ('SJ*', 'SJ*'),
                          ('SJ*', 'S9*'), ('SJ*', 'S7*'), ('SJ*', 'S6*'), ('SJ*', 'S4*'), ('SJ*', 'S2*'),
                          ('S9*', 'S9*'), ('S9*', 'S7*'), ('S9*', 'S6*'), ('S9*', 'S4*'), ('S9*', 'S2*'),
                          ('S7*', 'S7*'), ('S7*', 'S6*'), ('S7*', 'S4*'), ('S7*', 'S2*'), ('S6*', 'S6*'),
                          ('S6*', 'S4*'), ('S6*', 'S2*'), ('S4*', 'S4*'), ('S4*', 'S2*'), ('S2*', 'S2*')])


suite = unittest.TestLoader().loadTestsFromTestCase(TestWildList)
unittest.TextTestRunner(verbosity=3).run(suite)