""" reads key_values.pkl
"""

import os
import pickle
hand_dictionary = {}
# does key_values_dictionary.pkl exist?  If no, open the file
# os.path.dirname(__file__) gives us the directory of script
pathname = os.path.dirname(__file__) + "\\key_values.pkl"
print (pathname)

if os.path.exists(pathname):
    with open("key_values.pkl", "rb") as g:
        data = g.read()
    hand_dictionary = pickle.loads(data)

count = 1
for key,value in sorted(hand_dictionary.items()):
    if key[0] == 5 or key[0] == 6 or key[0] == 7 or key[0] == 7:
        pass
    else:
        # print (count, key, value)
        print (count, key, value[0], value[1])
        count += 1

# print (hand_dictionary)