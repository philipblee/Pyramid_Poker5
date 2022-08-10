from random import randint
import time
random_seed = randint(1,10000)
# random_seed = 1
print("random seed", random_seed)
print ("global_variables routine")
file_num = 1
best_scores_list = []
minimum_play_score = -600
special_play_score = -600
player_minimums = [-500, -500, -500, -500, -500, -500]
