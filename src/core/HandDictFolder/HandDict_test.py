from HandDictFolder.HandDict import *


with open("hand_dict.pickle", "rb") as file:
    hand_dict = pickle.load(file)

import sys
original_stdout = sys.stdout
with open("hand_dict.txt", "w") as f:
    sys.stdout = f
    for item in hand_dict:
        print(item, "/", hand_dict[item])
sys.stdout = original_stdout

# for i in hand_dict:
#     print (i, hand_dict[i])


