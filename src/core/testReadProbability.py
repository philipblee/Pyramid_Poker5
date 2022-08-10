from src.core.ReadProbability import *

score_dict = ReadProbability().score_prob

# how to print score_dict

# for a in score_dict:
#     print (a, score_dict[a])

testkeys = ["6091110", "2041344", "3041133", "4081314"]


for key in testkeys:
    if key in score_dict:
        print ("found", score_dict[key])
    else:
        print ("not found")

