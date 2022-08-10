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

def fix_item2(old_item):
    temp = old_item.replace("(", "")
    temp = temp.replace(")", "")
    return (temp)

class ReadKeyValuesProb():
    """ class reads KeyValues and creates keyval_prob file
    """

    def __init__(self):

        import os
        rel_path = "KeyValuesProb.csv"
        cwd = os.getcwd()
        print (cwd)
        x = {}
        with open(rel_path, "r") as e:
            reader = csv.reader(e)
            keyvalues_list = list(reader)
        index = 0
        for row in keyvalues_list:
            temp = ""
            for i in range(len(row)):
                temp += row[i]

            temp.replace("'", "")
            key_val = ""

            # new_list = []
            key_val_dict = {}
            for i in range (1, len(row)-2):
                temp = fix_item2(row[i])
                key_val += temp
            a_list = key_val.split()
            map_object = map(int, a_list)
            hand_num = int(row[0])
            prob_num = float(row[-2])
            final_keys = list(map_object)
            final_keys.insert(0, hand_num)
            new_tuple = tuple(final_keys)
            key_val_dict = {new_tuple : prob_num}
            x[index] = prob_num
            index += 1
            print (x)
            # key_val_dict[new_tuple] = prob_num
            # print (new_tuple, key_val_dict[new_tuple])
            # print(key_val_dict)
            # print (len(key_val_dict))
        print (x)
        x[(1,1)] = 2
        print (x)
        x[(2,1)] = 3
        print (x)
ReadKeyValuesProb()