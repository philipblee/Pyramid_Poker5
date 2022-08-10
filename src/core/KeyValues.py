import os, csv
from sort_cards import tuple_sort

# GAME="PP"
# NUMBER_OF_WILD_CARDS = 3
NUMBER_OF_CARDS = 25
NUM_OF_CARDS = str(NUMBER_OF_CARDS) + "CARDS"
PROBABILITY_FILE_NEW = "KeyValuesProb.csv"
CUMULATIVE_LEARNING = "KeyValues.csv"
CUMULATIVE_MEDIUM_SCORES = "Cumulative_Medium_Scores.csv"

def fix_item(old_item):
    temp0 = old_item.replace("(", "")
    temp0 = temp0.replace(")", "")
    new_item = tuple(map(int, temp0.split(', ')))
    return (new_item)

class CumulativeLearning():
    """ Reads Cumulative_Learning.csv and calculates winning_percent
        and writes results to Probability.csv"""
    def __init__(self):
        if os.path.exists(CUMULATIVE_LEARNING):
            with open(CUMULATIVE_LEARNING, "r") as g:
                reader = csv.reader(g, delimiter='/')
                cumulative_output = list(reader)
                cumulative_learning = [[],[],[],[],[],[],[]]
                sorted_list = [[], [], [], [], [], [], []]

            for item in cumulative_output:
                item[0] = fix_item(item[0])
                item[1] = fix_item(item[1])
                item[2] = fix_item(item[2])
                item[3] = fix_item(item[3])
                item[4] = fix_item(item[4])
                item[5] = fix_item(item[5])

                cumulative_learning[6].append((item[5]))
                cumulative_learning[5].append((item[4]))
                cumulative_learning[4].append((item[3]))
                cumulative_learning[3].append((item[2]))
                cumulative_learning[2].append((item[1]))
                cumulative_learning[1].append((item[0]))
            # sort cumulative_learning

            sorted_list[1] = sorted(cumulative_learning[1], key = lambda  x: (x[1], x[2]), reverse=True)
            sorted_list[2] = sorted(cumulative_learning[2], key=lambda x: (x[1], x[2]), reverse=True)
            sorted_list[3] = sorted(cumulative_learning[3], key=lambda x: (x[1], x[2]), reverse=True)
            sorted_list[4] = sorted(cumulative_learning[4], key=lambda x: (x[1], x[2]), reverse=True)
            sorted_list[5] = sorted(cumulative_learning[5], key=lambda x: (x[1], x[2]), reverse=True)
            sorted_list[6] = sorted(cumulative_learning[6], key=lambda x: (x[1]), reverse=True)

            for i in range (1,7):
                cumulative_learning[i] = self.calc_win_percent(sorted_list[i])

            # let's write out PROBABILITY_FILE_NEW
            g = open (PROBABILITY_FILE_NEW, "w")
            g.write("0, 0, 0, 0\n")

            # write out PROBABILITY_FILE
            for i in range(1,7):
                for item in cumulative_learning[i]:
                    cumulative_learning_string = str(i) + ", " + str(item[0]) + ", " + str(item[1]) \
                                                  + ", " + str(item[2]) + "\n"
                    with open(PROBABILITY_FILE_NEW, "a") as g:
                        g.write(cumulative_learning_string)



    def calc_win_percent(self, list_of_hands):
        """ Given a list of hands, calculate_win_percent will return
            a list of tuples corresponding to list_of_hands with
            winning percent and count
        """
        list_of_hands = sorted(list(list_of_hands))
        # sorts as a string and not as a tuple - how to fix?
        # print ("list", list_of_hands)
        hand_winning_percent = [(0, 0 ,0)]
        inum = 1
        count = 1
        # for each hand, count
        for i in range(len(list_of_hands)-1):
            if list_of_hands[i] == list_of_hands[i+1]:
                inum += 1
                count += 1
                # print ("equal", list_of_hands[i], count)
            else:
                winning_percent = round((inum/len(list_of_hands) * 100),4)
                hand_win_tuple = (list_of_hands[i], winning_percent, inum)
                hand_winning_percent.append(hand_win_tuple)
                inum += 1
                # print ("different", list_of_hands[i], count)
                # print(hand_win_tuple)
                count = 1

        # hand_win_tuple = (list_of_hands[i], 100, inum)
        # print (hand_win_tuple)
        winning_percent = round((inum / len(list_of_hands) * 100), 4)
        hand_win_tuple = (list_of_hands[i], winning_percent, inum)
        hand_winning_percent.append(hand_win_tuple)
        # print("last", list_of_hands[i], count)
        # print(hand_win_tuple)
        # hand_winning_percent = sorted(hand_winning_percent, reverse = True)
        # print(hand_winning_percent)
        return hand_winning_percent

CumulativeLearning()