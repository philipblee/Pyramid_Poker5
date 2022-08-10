"""
KeyValues is a tuple of numbers that determine hand strength
Every poker hand has a KeyValue
"""
import ast
import csv
import re
import ast
from src.core.PokerHand import *
from operator import itemgetter
class ReadKeyValues():
    """ class reads KeyValues and creates keyval_prob file
    """

    def __init__(self):

        import os
        rel_path = "KeyValues.csv"
        cwd = os.getcwd()
        print (cwd)

        with open(rel_path, "r") as e:
            reader = csv.reader(e, delimiter='/')
            x = list(reader)

        hand1 = []
        hand2 = []
        hand3 = []
        hand4 = []
        hand5 = []
        hand6 = []

        for a in x:
            # print(a)
            # print (a[0], a[1], a[2], a[3], a[4], a[5])
            hand1.append(a[0])
        print (sorted(hand1))

            # my_tuple = ast.literal_eval(a)
            # print(my_tuple)


ReadKeyValues()