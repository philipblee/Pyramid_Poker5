import pickle

file = open("prob_dictionary", "rb")
score_dict = pickle.load(file)

for d in sorted(score_dict.keys()):
    print (d, score_dict[d])
