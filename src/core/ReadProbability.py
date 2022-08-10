import csv
import re
from src.core.PokerHand import *

class ScoreProb(dict):

    """ ScoreProb is a class that is based on Python's dict class """
    def find(self, dict):
        """ find looks for pattern myhand20_analysis in the dictionary
            example:  pattern= "604...." looks for keys that begin with 604 in dictionary
            """
        return (self[pattern] for pattern in self if re.match(dict, pattern))


class ReadProbability():
    """ class reads PROBABILITY_FILE_NEW2 and stores into score_prob
        which is a dictionary with a find method for pattern matching
        when the exect myhand20_analysis cannot be found in dictionary"""


    def __init__(self):
        # my_hand = Hand()
        import os
        rel_path = "Probability.csv"
        cwd = os.getcwd()
        print (cwd)
        # print (ReadProbability)
        with open(rel_path, "r") as e:
            reader = csv.reader(e)
            x = list(reader)
        self.score_prob = ScoreProb()
        self.score_points = ScoreProb()
        for a in x:
            self.score_prob [str(a[0])] = float(a[1])
            hand = int(a[0][0])
            score = int(a[0][1:])
            # points = my_hand.get_points_from_score(points, hand)
            # self.score_points [str(a[0])] = round(float(a[1]) * points/100, 4)
            # print (hand, points, a[0], points)

        # # put results into a list
        # self.score_prob_array = dict([])
        # for a in x:
        #     hand = int(a[0][0])
        #     points = int(a[0][1:])
        #     # see if anything is stored in points
        #     if points in self.score_prob_array:
        #         prob_list = self.score_prob_array[points]
        #     else:
        #         prob_list = [None, None, None, None, None, None, None]
        #     prob_list[hand] = float(a[1])
        #     self.score_prob_array [str(points)] = prob_list
        #     # print (str(a[0]), float(a[1]))
        #
        # for i in self.score_prob_array:
        #     print (i, self.score_prob_array[i])