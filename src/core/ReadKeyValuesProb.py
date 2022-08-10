"""
KeyValues is a tuple of numbers that uniquely identifies han_number and hand strength
Every poker hand has a KeyValue tuple that returns the probability of winning
"""

from src.core.PokerHand import *
from operator import itemgetter

def remove_parenthesis(old_item):
    new_item = old_item.replace("(", "")
    new_item = new_item.replace(")", "")
    return (new_item)

class ReadKeyValuesProb():
    """ class reads KeyValues and creates keyval_prob file
    """

    def __init__(self):
        rel_path = "KeyValuesProb.csv"
        cwd = os.getcwd()
        print (cwd)

        with open(rel_path, "r") as e:
            reader = csv.reader(e)
            keyvalues_list = list(reader)

        key_val_dict = {}

        for row in keyvalues_list:
            temp_string = ""
            for i in range(len(row)):
                temp_string += row[i]

            temp_string.replace("'", "")
            key_val = ""

            for i in range (1, len(row)-2):
                temp = remove_parenthesis(row[i])
                key_val += temp

            a_list = key_val.split()
            map_object = map(int, a_list)
            hand_num = int(row[0])
            prob_num = float(row[-2])
            final_keys = list(map_object)
            final_keys.insert(0, hand_num)
            new_tuple = tuple(final_keys)
            key_val_dict[new_tuple] = prob_num

        # print out dictionary
        # for key,value in key_val_dict.items():
        #     print (key, value)

        print(len(key_val_dict))
        file = open("keyval_dictionary", "wb")
        pickle.dump(key_val_dict, file)
        # key_val_dict1 = pickle.load(file)
        file.close()

ReadKeyValuesProb()