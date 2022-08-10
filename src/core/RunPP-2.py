""" RunPyramidPoker runs Batch or Interactive
"""
import sys
from src.core.Analysis import *
from src.core.BestHand25Wild import *
from src.core.WriteFile import *
from src.core.PokerHand import *
import time
import datetime
import os
import tkinter as tk
from src.core.CumulativeLearning import *
from src.core.ReadProbability import *
import json
from src.core.PlayerHand import *
from MyHand20_Analysis import *
import statistics as stats
from FindBestMatches import *
# PARAMETERS
NUMBER_OF_HANDS = 10
PRINT_HAND_FREQUENCY = 1
NUMBER_OF_CARDS = 25 #default
NUMBER_OF_WILD_CARDS = 3
my_hand = PokerHand()

X_GAP = 80
Y_GAP = 110
X_OFFSET = 11
global card_list

if len(sys.argv) < 2:
    MODE = "Interactive"  #default
    NUMBER_OF_HANDS = 10
else:
    if sys.argv[1] == "Batch" or sys.argv[1] == "Interactive" or\
        sys.argv[1] == "Solve":
        MODE = sys.argv[1]
    else:
        MODE = "Interactive"

    if int(sys.argv[2]) > 0 and int(sys.argv[2]) <100000:
        NUMBER_OF_HANDS = int(sys.argv[2])


elapse_time = [[],[],[],[]]  # wilds = 0,1,2,3
print (MODE)
print ("Number of arguments:", len(sys.argv))
print ("Argument List:", str(sys.argv))

top = tk.Tk()
global k_num, wild_count
k_num = 1
if MODE == "Batch":
    overall_start_time = time.time()
    NUMBER_OF_CARDS = 25
    wild_count = [0, 0, 0, 0]

    for k in range (NUMBER_OF_HANDS):
        special_play_score = global_variables.special_play_score
        simulation_deck = Deck()
        my_hand = PokerHand()
        play_hand20_quality = ["", "", "", "", "", "", ""]
        player_score_hand20 = [0, 0, 0, 0, 0, 0]
        player_names = ["Peter ", "Johnny", "Ming  ", "Tony  ", "Edmond", "Philip"]
        player_score_prediction = [0, 0, 0, 0, 0, 0, 0]
        points_stored = [[], [], [], [], [], [], []]
        hands_stored = [[], [], [], [], [], [], []]
        points_stored_best = [[], [], [], [], [], []]
        hand20_signal = [0, 0, 0, 0, 0, 0]
        player_wilds = [0, 0, 0, 0, 0, 0]
        play_hand20 = [False, False, False, False, False, False]

        for hand_number in range(1):
            card_list = Deck.deal()[0]
            card_list2 = list(card_list[0:NUMBER_OF_CARDS])  # deal number_of_cards
            card_list2 = (sorted(card_list2, key=rank_sort, reverse=True))
            card_list = card_list2
            # print card_list
            card_list2_unsorted = list(card_list[0:NUMBER_OF_CARDS])  # deal number_of_cards
            card_list2 = (sorted(card_list2_unsorted, key=rank_sort, reverse=True))

            wild_cards = 0
            # count number of wild cards
            if card_list2[2][0:2] == "WW":
                wild_cards = 3
            elif card_list2[1][0:2] == "WW":
                wild_cards = 2
            elif card_list2[0][0:2] == "WW":
                wild_cards = 1

            if wild_cards == 1:
                wild_count[1] += 1
            elif wild_cards == 2:
                wild_count[2] += 1
            elif wild_cards == 3:
                wild_count[3] += 1

            player_wilds[hand_number] = wild_cards
            start_time = time.time()
            player_wilds[hand_number] = wild_cards
            print("\nGame#", k_num + 1, "Hand#", (k_num) * 6 + hand_number + 1, "One Wild=", wild_count[1], \
                  "Two Wild=", wild_count[2], "Three Wild=", wild_count[3], "=========== New Hand ===============")

            # Look at first 20 cards and decide what to do
            card_list20 = list(card_list2_unsorted[0:20])
            card_list20 = (sorted(card_list20, key=rank_sort, reverse=True))
            card_list_temp = list(card_list20)
            before_analysis = Analysis(card_list20)
            print(player_names[hand_number], "is the player.  Analysis to follow.")
            print("Player's 20 Card Hand: ", card_list20)

            # analysis2 = MyHand20_Analysis2(card_list_temp)

            myhand20 = BestHand25Wild(card_list_temp)

            # find best myhand20_analysis returns list of "ranks" that are good
            # findbestmatches = FindBestMatches(card_list_temp)

            myhand20_analysis = MyHand20_Analysis(card_list_temp)

            print (myhand20_analysis.match_card_list, "potential match_card_list")
            hand20_signal[hand_number] = myhand20_analysis.hand20_signal

            print("average_matches, matches", myhand20_analysis.average_matches, myhand20_analysis.matches)
            print("20 Cards-Best Hand", myhand20.best_25handx[1:7])
            print("20 Cards-Best Points", myhand20.best_hand_points)
            average_score = 0
            simulation_hands = int(50)

            # print "20 Simulated Hands -",
            points_predicted_list = []


            for i in range(simulation_hands):
                kitty_cards_used_list = []
                kitty_cards = simulation_deck.deal_5random_cards(card_list20)
                card_list25 = kitty_cards + card_list20
                after_analysis = Analysis(card_list25)
                myhand = BestHand25Wild(card_list25)
                points = myhand.best_hand_points
                best_25handx = myhand.best_25handx
                print("\nSimulation", i + 1, kitty_cards)
                print(" ", myhand.best_hand_points[0], myhand.best_25handx)
                # determine number of kitty cards used

                num_kitty_cards_used = 0
                for card in kitty_cards:
                    if card[0:2] == "WW":
                        kitty_cards_used_list.append(card)
                    if str(card[1]) in myhand20_analysis.match_card_list:
                        # print ("is card in match_card_list", card, str(card[1]), myhand20_analysis.match_card_list)
                        kitty_cards_used_list.append(card)
                        print (kitty_cards_used_list, "kitty_cards_used_list")
                        num_kitty_cards_used += 1
                print ("kitty cards used list", kitty_cards_used_list, len(kitty_cards_used_list))
                # kitty_cards_used_list.append(len(kitty_cards_used))
                average_score += myhand.best_hand_points[0]
                points_predicted_list.append(points[0])
                # compare before_analysis to after_analysis
                print("after  - ",after_analysis.suit_rank_array[5])
                print("before - ",before_analysis.suit_rank_array[5])
                diff = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                for k in range(len(after_analysis.suit_rank_array[5])):
                    diff[k] = after_analysis.suit_rank_array[5][k]-before_analysis.suit_rank_array[5][k]
                print("diff   - ", diff)
                before_trips_plus = 0
                for k in range(0,16):
                    if before_analysis.suit_rank_array[5][k] >= 3:
                        before_trips_plus += 1
                after_trips_plus = 0
                for k in range(0,15):
                    if after_analysis.suit_rank_array[5][k] >= 3:
                        after_trips_plus += 1
                # print("Trips_plus",  before_trips_plus, after_trips_plus )
                # print("wilds", before_analysis.wilds, after_analysis.wilds)
                # print("Pairs", before_analysis.pairs,after_analysis.pairs)
                # print("Trips", before_analysis.trips, after_analysis.trips)
                # print ("4k", before_analysis.fourks, after_analysis.fourks)
                # print("5k", before_analysis.fiveks, after_analysis.fiveks)
                # print ("6k", before_analysis.fourks, after_analysis.sixks)
                # print("7k", before_analysis.fiveks, after_analysis.sevenks)
                # print("5SF", before_analysis.five_card_straightflushes, after_analysis.five_card_straightflushes)
                # print("6SF", before_analysis.six_card_straightflushes, after_analysis.six_card_straightflushes)
                # print("7SF", before_analysis.seven_card_straightflushes, after_analysis.seven_card_straightflushes)
                # print("8SF", before_analysis.eight_card_straightflushes, after_analysis.eight_card_straightflushes)
                # print("9SF", before_analysis.nine_card_straightflushes, after_analysis.nine_card_straightflushes)
                # print("10SF", before_analysis.ten_card_straightflushes, after_analysis.ten_card_straightflushes)
                new_pairs = after_analysis.pairs - before_analysis.pairs
                new_trips = after_analysis.trips - before_analysis.trips
                new_fourks = after_analysis.fourks - before_analysis.fourks
                new_fiveks = after_analysis.fiveks - before_analysis.fiveks
                new_sixks = after_analysis.sixks - before_analysis.sixks
                # new_straight_flushes = after_analysis.straight_flushes - before_analysis.straight_flushes
                # print("pairs,trips,4Ks,5Ks,6Ks,SF", new_pairs, new_trips, new_fourks, new_fiveks,
                #       new_sixks)  # , new_straight_flushes)
            average_score = round(average_score / simulation_hands, 1)
            points_predicted_list.sort()
            print()
            print()
            print(points_predicted_list)
            points_predicted_mean = round(stats.mean(points_predicted_list), 2)
            points_predicted_stdev = round(stats.stdev(points_predicted_list), 2)
            print("mean=", points_predicted_mean, "stdev=", points_predicted_stdev)
            # for j in range (0, simulation_hands, int(simulation_hands/4)):
            #     points_predicted_mean = round(stats.mean(points_predicted_list[j*simulation_hands:j+1*simulation_hands]),2)
            #     points_predicted_stdev = round(stats.stdev(points_predicted_list[j*simulation_hands:j+1*simulation_hands]),2)
            #     print(j, "mean=", points_predicted_mean, "stdev=", points_predicted_stdev)
            # how many trips, 4k, 5k, 6k, SF
            kitty_cards_used_list.sort()



            print(kitty_cards_used_list)
            # print("kitty cards used mean, stdev", stats.mean(kitty_cards_used_list), stats.stdev(kitty_cards_used_list))
            player_score_prediction[hand_number] = average_score
            player_score_hand20[hand_number] = myhand20.best_hand_points[0]
            # print("    = Average Prediction Score", average_score, )
            minimum_play_score = global_variables.minimum_play_score
            minimum_h20_play_score = -2000
            # special_play_score = [1300, 1400, 1500, 1600, 1700, 1800]
            # special_player_play =  [False, False, False, False, False, False]

            if average_score >= global_variables.player_minimums[hand_number]:
                play_hand20[hand_number] = True
            else:
                play_hand20[hand_number] = False

            if average_score >= 1000:
                print("Play this Monster Hand")
                play_hand20_quality[hand_number] = "Monster"
            elif average_score >= 500:
                print("Play this Good Hand")
                play_hand20_quality[hand_number] = "Good"
            elif average_score >= minimum_play_score:
                print("Play this Marginal Hand")
                play_hand20_quality[hand_number] = "Ok"
            elif average_score >= -500:
                print("Surrender this Marginal Hand")
                play_hand20_quality[hand_number] = "Not Ok"
            else:
                print("Surrender this Sad Hand")
                play_hand20_quality[hand_number] = "Sad"

            # Pick up 5 card kitty and play hand
            card_list1 = list(card_list2)
            myhand = BestHand25Wild(card_list1)
            points = myhand.best_hand_points
            medium_score = myhand.best_hand_points
            best_25handx = myhand.best_25handx
            # cards_used = 0
            # for i in range(1,7):
            #     cards_used += len(best_25handx[i])
            # cards_left = 25 - cards_used
            # best_card_list1 = json.dumps(best_25handx[1:7])
            points_stored[hand_number] = points
            hands_stored[hand_number] = best_25handx
            kitty_cards = set(card_list2).difference(card_list20)
            print("5-card kitty", kitty_cards)
            print("25 Cards-Card List", card_list2)
            print("25 Cards-Best Hand", myhand.best_25handx[1:7])
            print("25 Cards-Best Points", myhand.best_hand_points)
            kitty_cards_used = []
            for j in range(1, 7):
                kitty_cards_used.extend(list(set(myhand.best_25handx[j]).intersection(kitty_cards)))
            best_card_list1 = json.dumps(best_25handx[1:7])
            print("number of kitty_cards used", len(kitty_cards_used), kitty_cards_used)
            end_time = time.time()
            lapse_time = round(end_time - start_time, 2)
            print("--Elapsed Time = ", lapse_time)
            # prepare cumulative_learning_string
            cumulative_learning_string = str(points[6][0]) + ", " + str(points[6][1]) + ", "
            cumulative_learning_string += str(points[5][0]) + ", " + str(points[5][1]) + ", "
            cumulative_learning_string += str(points[4][0]) + ", " + str(points[4][1]) + ", "
            cumulative_learning_string += str(points[3][0]) + ", " + str(points[3][1]) + ", "
            cumulative_learning_string += str(points[2][0]) + ", " + str(points[2][1]) + ", "
            cumulative_learning_string += str(points[1][0]) + ", " + str(points[1][1]) + ", "
            cumulative_learning_string += str(points[0])
            temporary_string = cumulative_learning_string
            w0 = w1 = w2 = w3 = ""
            if wild_cards == 0:
                w0 = str(points[0])
            elif wild_cards == 1:
                w1 = str(points[0])
            elif wild_cards == 2:
                w2 = str(points[0])
            elif wild_cards == 3:
                w3 = str(points[0])
            cumulative_learning_string += "," + str(wild_cards) + ", " + w0 + ", " + w1 + ", " + w2 + ", " + w3
            cumulative_learning_string1 = cumulative_learning_string + str(play_hand20[hand_number]) + "\n"

            if os.path.exists(CUMULATIVE_LEARNING):
                with open(CUMULATIVE_LEARNING, "a") as g:
                    g.write(cumulative_learning_string1)
            else:
                with open(CUMULATIVE_LEARNING, "w") as g:
                    g.write(cumulative_learning_string1)

            # generate cumulative_medium_scores - for each hand, generate medium_scores
            cumulative_medium_scores = str(medium_score[6]) + ", " + str(points[6][1]) + ", "
            cumulative_medium_scores += str(medium_score[5]) + ", " + str(points[5][1]) + ", "
            cumulative_medium_scores += str(medium_score[4]) + ", " + str(points[4][1]) + ", "
            cumulative_medium_scores += str(medium_score[3]) + ", " + str(points[3][1]) + ", "
            cumulative_medium_scores += str(medium_score[2]) + ", " + str(points[2][1]) + ", "
            cumulative_medium_scores += str(medium_score[1]) + ", " + str(points[1][1]) + ", "
            cumulative_medium_scores += str(points[0]) + "\n"

            if os.path.exists(CUMULATIVE_MEDIUM_SCORES):
                with open(CUMULATIVE_MEDIUM_SCORES, "a") as h:
                    h.write(cumulative_medium_scores)
            else:
                with open(CUMULATIVE_MEDIUM_SCORES, "w") as h:
                    h.write(cumulative_medium_scores)

            cumulative_output = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")) + ", "
            cumulative_output += str(wild_cards) + ", "
            cumulative_output += str(temporary_string) + ", "
            cumulative_output += str(lapse_time) + ","
            # add count here
            cumulative_output += str(card_list2) + ","
            cumulative_output += str(best_card_list1) + "\n"
            WriteFile(cumulative_output)

            # print out the best hands
            global_variables.best_scores_list.sort(key=lambda t: t[0], reverse=True)
            best_score_count = 0
            last_h_score = 0
            # print "global_variables.best_scores_list"
            # for i, (h_score, h_points, h_hand) in enumerate(global_variables.best_scores_list):
            #     if h_score <> last_h_score:
            #         print h_score, h_hand
            #         best_score_count += 1
            #         last_h_score = h_score
            #         points_stored_best[hand_number].append(h_points)
            #         if best_score_count >=5:
            #             break

            for i in range(1, 7):
                hand_description_string = my_hand.get_description_from_score(points[i][0], str(i))
                print('{:>11}'.format(hand_description_string), end=" ")

            print
            print("\nHand Summary:")
            print("   - h20_score ", myhand20.best_medium_score[0], end=" ")
            if myhand20.best_medium_score[0] >= minimum_play_score - 1000:
                print("play")
            else:
                print("do not play")
            print("   - prediction", average_score, end=" ")
            if average_score >= minimum_play_score:
                print("play")
            else:
                print("do not play")
            print("   - h20_signal", myhand20_analysis.hand20_signal, end=" ")
            if myhand20_analysis.hand20_signal >= 5:
                print("play")
            else:
                print("do not play")
            print("   - actual points", myhand.best_hand_points[0], end=" ")
            if myhand.best_hand_points[0] >= minimum_play_score:
                print("play")
            else:
                print("do not play")
            if abs(myhand.best_hand_points[0] - average_score) < 500:
                print("   - actual within 500 of prediction")
            else:
                print("   - actual not within 500 of prediction")
            print("Actual over Prediction:", round(myhand.best_hand_points[0] - average_score, 1))

        card_list = Deck.deal()[0]
        card_list2 = list(card_list[0:NUMBER_OF_CARDS])  # deal number_of_cards
        card_list2 = (sorted (card_list2, key=rank_sort, reverse=True))
        wild_cards = 0
        # count number of wild cards
        if card_list2[2][0:2] == "WW":  wild_cards = 3
        elif card_list2[1][0:2] == "WW":  wild_cards = 2
        elif card_list2[0][0:2] == "WW":  wild_cards = 1

        if wild_cards == 1:  wild_count[1] += 1
        elif wild_cards == 2:  wild_count[2] += 1
        elif wild_cards == 3:  wild_count[3] += 1
        start_time = time.time()
        if k%PRINT_HAND_FREQUENCY == 0:
            print ("\nHand#", k + 1, "One Wild=", wild_count[1], "Two Wild=", wild_count[2], "Three Wild=", wild_count[3], "=========== New Hand ===============")
        print (card_list2)
        # logging.info((card_list2))
        
        # Use Best25Wild class to get best_hand_score and best_25handx

        myhand = BestHand25Wild(card_list2)
        score = myhand.best_hand_points
        # print (points)
        best_card_list1 = json.dumps(myhand.best_25handx[1:7])
        print (myhand.best_25handx[6:0:-1])
        print (myhand.best_hand_points[0], myhand.best_hand_points[6:0:-1])
        end_time = time.time()
        lapse_time = round(end_time - start_time, 2)
        print ("--Total time for hand = ", lapse_time)
        elapse_time[wild_cards].append(lapse_time)
        w0 = w1 = w2 = w3 = ""
        if wild_cards == 0:  w0 = str(score[0])
        elif wild_cards == 1:  w1 = str(score[0])
        elif wild_cards == 2:  w2 = str(score[0])
        elif wild_cards == 3:  w3 = str(score[0])

        cumulative_learning_string = str(score[6][0]) + ", " + str(score[6][1]) + ", "
        cumulative_learning_string += str(score[5][0]) + ", " + str(score[5][1]) + ", "
        cumulative_learning_string += str(score[4][0]) + ", " + str(score[4][1]) + ", "
        cumulative_learning_string += str(score[3][0]) + ", " + str(score[3][1]) + ", "
        cumulative_learning_string += str(score[2][0]) + ", " + str(score[2][1]) + ", "
        cumulative_learning_string += str(score[1][0]) + ", " + str(score[1][1]) + ", "
        cumulative_learning_string += str(score[0])
        temporary_string = cumulative_learning_string
        cumulative_learning_string += "," + str(wild_cards) + ", " + w0 + ", " + w1 + ", " + w2 + ", " + w3
        cumulative_learning_string1 = cumulative_learning_string +  "\n"

        if os.path.exists(CUMULATIVE_LEARNING):
            with open(CUMULATIVE_LEARNING, "a") as g:
                g.write(cumulative_learning_string1)
        else:
            with open(CUMULATIVE_LEARNING, "w") as g:
                g.write(cumulative_learning_string1)
        cumulative_learning_string2 = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")) +  ", "
        cumulative_learning_string2 += str(wild_cards) +  ", "
        cumulative_learning_string2 += str(temporary_string)  +  ", "
        cumulative_learning_string2 += str(lapse_time) +  ","
        # add count here
        cumulative_learning_string2 += str(card_list2) + ","
        cumulative_learning_string2 += str(best_card_list1) + "\n"
        x = WriteFile(cumulative_learning_string2)

    overall_end_time = time.time()
    lapse_time = round(overall_end_time - overall_start_time, 2)
    print ("finished", lapse_time, round(lapse_time/NUMBER_OF_HANDS, 2))

    # import statistics
    # for i in range(4):
    #     if len(elapse_time[i]) > 0:
    #         print ("number of wild cards", i, len(elapse_time[i]), round(statistics.mean(elapse_time[i]),2))


def display_score(score_array, x, y):
    """
    given score_array displays 6 scores and total points at x,y coordinates
    :param score_array: score0, score1, score2, score2, score3, score4, score5, score6
    :param x: x coordinate of where to display_cardlist points
    :param y: y coordinate of where to display_cardlist points
    """
    score = score_array
    total_score_label = tk.Label(text="total points = " + str(score[0]) + 20*" ", fg="blue", bg="white")
    total_score_label.place(x=x, y=y)
    hand6_score_label = tk.Label(text="hand6 = " + str(score[6]) + 30*" ", fg="blue", bg="white")
    hand6_score_label.place(x=x, y=y + 25)
    hand5_score_label = tk.Label(text="hand5 = " + str(score[5]) + 30*" ", fg="blue", bg="white")
    hand5_score_label.place(x=x, y=y + 50)
    hand4_score_label = tk.Label(text="hand4 = " + str(score[4]) + 30*" ", fg="blue", bg="white")
    hand4_score_label.place(x=x, y=y + 75)
    hand3_score_label = tk.Label(text="hand3 = " + str(score[3]) + 30*" ", fg="blue", bg="white")
    hand3_score_label.place(x=x, y=y + 100)
    hand2_score_label = tk.Label(text="hand2 = " + str(score[2]) + 30*" ", fg="blue", bg="white")
    hand2_score_label.place(x=x, y=y + 125)
    hand1_score_label = tk.Label(text="hand1 = " + str(score[1]) + 30*" ", fg="blue", bg="white")
    hand1_score_label.place(x=x, y=y + 150)

def solve_best25_hand(*args):
    """ Given  twenty_five cards, solve for the best hand and show scoring"""
    # X_GAP = 80
    # Y_GAP = 110
    X_OFFSET = 11 + 4
    global twentyfive_cards
    global card_list
    candidate_25card_hand = []
    # determine 25 cards to solve
    card_list = list(Deck().deal_3deck(1))[0]
    card_list = sorted(card_list, key=suit_rank_sort)
    card_list = list(card_list)
    for card in card_list:
        card_placex = int((w.coords(card)[0] + X_OFFSET) / X_GAP)  # determines x coordinate of card
        card_placey = int((w.coords(card)[1]))  # determines y coordinate of card
        # logging.info((card, w.coords(card)[0], card_placex, card_placey))
        # print card, card_placex, card_placey
        if card_placey <  229 + 220 and card_placex <= 1200:
            candidate_25card_hand.append(card)

    card_list2 = sorted(candidate_25card_hand, key=suit_rank_sort, reverse=True)
    twentyfive_cards = card_list2
    card_list2_string = ", ".join(card_list2)
    # logging.info(card_list2_string)

    start_time = time.time()
    best_wild_card1, best_wild_card2, best_wild_card3, best_card_list1, best_hand_points, best_25handx = best25_with_3wild(card_list2)

    score6, score5, score4, score3, score2, score1, score7 = best_hand_points[0], best_hand_points[1], best_hand_points[2], \
                                    best_hand_points[3], best_hand_points[4], best_hand_points[5], best_hand_points[6]
    end_time = time.time()
    lapse_time = end_time - start_time
    score7 = round(score7,2)

    # showing best hand
    top.title("Best Hand Below and Best Scores on Right")
    X_OFFSET = 11 + 4
    j = 0
    for i in range(1):
        x = X_OFFSET + 5
        y = 10 * (j + 1)
        j += 1
        for card in best_card_list1[0:13]:  # hand6
            w.create_image(x, y, image=image_dict[card], anchor="nw", tag="best")
            x += X_GAP

        y += Y_GAP #row 2
        x = X_OFFSET + 5

        for card in best_card_list1[13:25]:  # hand3
            w.create_image(x, y, image=image_dict[card], anchor="nw", tag="best")
            x += X_GAP

        # showing points of best hand
        x_label = 13.5 * X_GAP
        y_label = 60 # aligns with best_hand
        x = x_label
        y = y_label
        score_array = (0, score1, score2, score3, score4, score5, score6, score7)
        display_score(score_array, x, y)

def create_images():
    """create all card images as a card_name:image_object dictionary"""
    global first_time_images
    suit = 'SHDC'
    rank = 'AKQJT98765432'
    deck_number = '+-*.=^'
    all_cards_list = [s + r + d for s in suit for r in rank for d in deck_number]
    for i in range(1):
        all_cards_list.extend(["WW+", "WW-", "WW*"])
    # print (all_cards_list)
    first_time_images= True
    if first_time_images == True:
        image_dict = {}
        for card in all_cards_list:
            # all images have filenames the myhand20_analysis the card_list names + extension .gif
            card_only = card[0:2]
            image_dict[card] = tk.PhotoImage(file=image_dir+card_only+".gif")
            # print ("create_images", card, image_dir + card_only+ ".gif")
        image_dict["Deck3"] = tk.PhotoImage(file=image_dir+"Deck3"+".gif")
        first_time_images = False
    return image_dict

def onClick(event):
    w.click = event.x, event.y
    w.tag_raise("current")

def onMotion(event):
    x, y = w.click
    dx = event.x - x
    dy = event.y - y
    w.move('current', dx, dy)
    w.click = event.x, event.y

def onRelease(event):  # anytime you change where widgets are, you need to fix
    """ when left-mouse button is released, place card in card slot if empty,
        if it is not empty look right, then look left and place if empty,
        if, <= 5 cards left, re-arrange in discard slots (gray color)
        """
    X_OFFSET = 11
    mx = (event.x - .5 * X_GAP) // X_GAP * X_GAP + 1 + X_OFFSET
    my = event.y // Y_GAP * Y_GAP + 20
    if my > 840:
         my = 840
    if mx > 1044:
         mx = 1044
    if mx < 10:
        mx = 4
    if my < 11:
        my = 11
    current_card_x = w.coords("current")[0]
    current_card_y = w.coords("current")[1]
    delta_x = mx - current_card_x + 5
    delta_y = my - current_card_y - 11
    w.move("current", delta_x, delta_y)  # this just snaps into place based on rectangle
    current_card_x = w.coords("current")[0]
    current_card_y = w.coords("current")[1]

    x1 = current_card_x
    y1 = current_card_y
    x2 = current_card_x + 80
    y2 = current_card_y + 110
    # look for "overlappers" to current card slot
    overlappers = w.find_overlapping(x1, y1, x2, y2)

    # see if overlappers are "token" and sitting on current_card_hand and current_card_place
    overlap_cards = []
    # for each tag_id, look for tag "token" to include in overlap_cards
    for object in overlappers:
        for tag in w.gettags(object):
            # print "tags", tag
            # restricts overlapping to same row
            if tag == "token": # and mx == tag_coordinates[0]:
                overlap_cards.append(object)
    # remove card with tag "current"
    current_card = []
    for card in overlap_cards:
        for tag in w.gettags(card):
            if tag == "current":
                current_card = card
    overlap_cards.remove(current_card)
    # if overlap_cards is empty, then all is good, otherwise look right, then left
    if overlap_cards == []:
        pass
    else:
        # check slot to right of current slot
        x1 = mx + 80
        x2 = mx + 160
        overlappers = w.find_overlapping(x1, y1, x2, y2)
        right_slot = []
        for object in overlappers:
            for tag in w.gettags(object):
                if tag == "token":
                    right_slot.append(object)
        # if right_slot is empty, then move current to it
        if right_slot == []:
            w.move("current", 80, 0)
            # print "card moved right", w.gettags("current")
        else:
            # if right slot filled, check left slot
            x1 = mx-80
            x2 = mx
            overlappers = w.find_overlapping(x1, y1, x2, y2)
            left_slot = []
            for object in overlappers:
                for tag in w.gettags(object):
                    if tag == "token":
                        left_slot.append(object)
            # if left_slot is empty, then move current to it
            if left_slot == []:
                w.move("current", -80, 0)
                # print "card moved left", w.gettags("current")
    # count number of cards left
    cards_left = list(w.find_withtag("token"))
    # print cards_left
    list_of_cards_left = list(cards_left)
    for object_id in list_of_cards_left:
        if w.coords(object_id)[1] > 120:
            cards_left.remove(object_id)

    destination = [657,118], [737,118], [817,118], [897,118], [977,118]
    index = 0
    # print "number of cards left", len(cards_left)
    if len(cards_left) <= 5:
        start_position = 5 - len(cards_left)
        for object_id in cards_left:
            x_coord = w.coords(object_id)[0]
            y_coord = w.coords(object_id)[1]
            delta_x = destination[index + start_position][0] - x_coord
            delta_y = destination[index][1] - y_coord
            w.move(object_id, delta_x, delta_y)
            index += 1
    return

def suit_quick_sort():
    """ sorting by suit and display_cardlist"""
    global twentyfive_cards
    twentyfive_cards = sorted(twentyfive_cards, key=suit_rank_sort, reverse=True)
    show_twentyfive_cards()

def rank_quick_sort():
    """ sorting by rank and display_cardlist"""
    global twentyfive_cards
    twentyfive_cards = sorted(twentyfive_cards, key=rank_sort, reverse=True)
    show_twentyfive_cards()

def save_position():
    """ saves locations of all cards in save_position1 """
    # count number of cards left
    global save_position1
    save_list = list(w.find_withtag("token"))
    # print "save_list", save_list
    index = 0
    for object_id in save_list:
        tags = w.gettags(object_id)[1]
        save_position1[index] = [tags, object_id, w.coords(object_id)[0], w.coords(object_id)[1]]
        w.gettags(object_id)
        # print "saved", save_position1[index]
        index += 1
    save_position1 = filter(None, save_position1)
    return

def restore_position():
    """ saves locations of all cards in save_position1 """
    w.delete("token")
    global save_position1
    for pos in save_position1:
        card, object_id, x, y = pos
        w.create_image(x, y, image=image_dict[card], anchor=NW, tags=("token", card))
    return

def show_card_list(*args):
    """show 25 cards in two rows, that can be moved into 6 part hand"""
    X_OFFSET = 20-8
    Y_OFFSET = 150-24+220
    tag_number = 1
    x = X_OFFSET + 0 * X_GAP
    y = Y_OFFSET - 10
    for i in range(13):
        fill_color = "light gray"
        w.create_rectangle((x, y , x + X_GAP, y + Y_GAP), fill=fill_color, tags=tag_number)
        x += X_GAP
        tag_number += 1

    x = X_OFFSET + 0 * X_GAP
    y = Y_OFFSET - 10 - 110
    for i in range(13):
        fill_color = "light gray"
        w.create_rectangle((x, y , x + X_GAP, y + Y_GAP), fill=fill_color, tags=tag_number)
        x += X_GAP
        tag_number += 1

    X_OFFSET = 20
    Y_OFFSET = 300 - 60
    CARD_GAP = 80
    y = 10 + 30 + 20
    x = X_OFFSET
    for card in card_list:
        # print card, x, Y_OFFSET, image_dict[card]
        w.create_image(x, Y_OFFSET, image=image_dict[card], anchor=NW, tags=("token", card))
        item_id = w.create_image(x, Y_OFFSET)
        w.create_text(x, Y_OFFSET, text=str(item_id))
        x += CARD_GAP
        if x > 1000:
             x = 20
             Y_OFFSET += 110

def show_next_hand(*args):
    """ Create the card list use Deck().deal and display_cardlist them"""
    # print "\n                  ---------------New Hand-----------"
    global twentyfive_cards

    NUMBER_OF_CARDS = 25
    a = Deck.deal()
# logging.info ("\n=========== New Interactive Hand ===============\n")
    # a[0] = ['WW*', 'WW+', 'SA-', 'HA*', 'SJ*', 'HJ*', 'DJ-', 'CJ*', 'ST-', 'S9-', 'D9+', 'C9+', 'S8+', 'H8*', 'D8*', 'S7-',
    #  'S5+', 'H5+', 'C5*', 'S4-', 'S4*', 'S3*', 'C3*', 'H2*', 'C2-']
    # a[0] = \
    #     ['SA_', 'SA.', 'SA*', 'SA+', 'HA+', 'CA-', 'SK-', 'SK*', 'DK-', 'SQ-', 'SQ*', 'CQ+', 'SJ*', 'CT*', 'S9-', 'D9+',
    #      'S7+', 'C6-', 'S5*', 'H5+', 'C5+', 'S4-', 'C4-', 'S3-', 'C2-']
    twentyfive_cards = (sorted(a[0][0:NUMBER_OF_CARDS], key=rank_sort, reverse=True))
    print (twentyfive_cards)
    top.title("Number of Wild Cards:" + str(NUMBER_OF_WILD_CARDS) + "     Play Pyramid Poker")
    w.delete("all")   # clear out last hand

    # two rows of 13 rectangles each
    Y_OFFSET = 60 + 60 + 102 # add 60 to account for buttons on top
    X_OFFSET = 11  # where cards and rectangles begin
    tag_number = 1

    # create 13 rectangles for first 13 cards
    x = X_OFFSET
    y = Y_OFFSET - 220
    for i in range(13):
        # w.create_rectangle((x, y , x + X_GAP, y + Y_GAP), tags=tag_number)
        item_id = w.create_rectangle(x, y, x + X_GAP, y + Y_GAP, tag="twentyfive-one")
        # print item_id
        # w.create_text(x, y, text = item_id)
        x += X_GAP
        tag_number += 1

    # create 13 rectangles for second 12 cards
    x = X_OFFSET
    y = Y_OFFSET - 110
    for i in range(13):
        if i>=8:
            fill_color = "light gray"
        else:
            fill_color = "pink"
        item_id = w.create_rectangle(x, y, x + X_GAP, y + Y_GAP, fill=fill_color, tag="twentyfive-two")
        x += X_GAP
        tag_number += 1

    # create 10 rectangles for hand 6 - rectangles 2-6 are white
    Y_OFFSET = 60 + 60 + 112 # add 60 to account for buttons on top
    x = X_OFFSET
    y = Y_OFFSET - 10
    for i in range(10):
        fill_color = "light yellow"
        if i >= 2 and i <= 6:
            fill_color = "white"
        item_id = w.create_rectangle((x, y , x + X_GAP, y + Y_GAP), fill=fill_color, tag="hand6")
        x += X_GAP

    # create 7 rectangles for hand 5 amd rectangles 1-5 are white
    x = X_OFFSET + 80
    y += Y_GAP
    for i in range(7):
        fill_color = "light yellow"
        if i >= 1 and i <= 5:
            fill_color = "white"
        item_id = w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill=fill_color, tags="hand5")
        x += X_GAP

    # create 6 rectangles for hand 4 and rectangles 1-3 are white, 0,4 are gray
    x = X_OFFSET + 2 * X_GAP
    y += Y_GAP
    for i in range(6):
        fill_color = "light yellow"
        if i >= 1 and i <= 3:
            fill_color = "white"
        if i == 4 or i == 0:
            fill_color = "light gray"
        item_id = w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill=fill_color, tags="hand4")
        x += X_GAP

    # create 5 rectangles for hand 3 and rectangles 1-3 are white, 0,4 are gray
    x = X_OFFSET + 2 * X_GAP
    y += Y_GAP
    for i in range(5):
        fill_color = "light yellow"
        if i >= 1 and i <= 3:
            fill_color = "white"
        if i == 4 or i == 0:
            fill_color = "light gray"
        item_id = w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill=fill_color, tags="hand3")
        x += X_GAP

    # create 3 rectangles - hand 2
    x = X_OFFSET + 3 * X_GAP
    y += Y_GAP
    for i in range(3):
        item_id = w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill="white", tags="hand2")
        x += X_GAP

    # create 1 rectangle - hand 1
    x = X_OFFSET + 4 * X_GAP
    y += Y_GAP
    for i in range(1):
        item_id = w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill="white", tags="hand1")
        x += X_GAP

    show_twentyfive_cards()

    # show best hand scores
    x_label = 11 * X_GAP
    y_label = 310  # align with next_hand
    x = x_label
    y = y_label
    score_array = (0, 0, 0, 0, 0, 0, 0, 0)
    display_score(score_array, x, y)

    # show player scores
    x_label = 11 * X_GAP  # for labels
    y_label = 310 + 150 + 110 # aligns with player hand
    x = x_label
    y = y_label + 100
    message = 50 * " "
    score_array = (0, 0, 0, 0, 0, 0, 0, 0)
    y = y_label + 50
    valid_hand_label = tk.Label(text=message, fg="blue", bg="pink")
    valid_hand_label.place(x=x - 125, y=y)
    display_score(score_array, x, y)

    blank_out = tk.Label(text = "                 ", fg="blue", bg="pink")
    blank_out.config(font=("arial", 20))
    blank_out.place(x=1080-350, y = 400)

def show_twentyfive_cards():
    w.delete("token")
    X_OFFSET = 8
    Y_OFFSET = 10
    y = Y_OFFSET
    x = X_OFFSET + 9   # move card to center of white rectangle

    for card in twentyfive_cards:
        item_id = w.create_image(x, y, image=image_dict[card[0:3]], anchor="nw", tags=("token", card))
        # print card, item_id
        x += X_GAP
        if x > 13 * X_GAP:
             x = X_OFFSET + 9
             y += Y_GAP

def show_deck_of_cards(*args):
    """show full deck of cards that can be moved to playing area"""
    X_OFFSET = 20-8
    Y_OFFSET = 150-24+220
    # X_GAP = 80
    # Y_GAP = 110
    tag_number = 1
    x = X_OFFSET + 0 * X_GAP
    y = Y_OFFSET - 10
    for i in range(12):
        fill_color = "light gray"
        w.create_rectangle((x, y , x + X_GAP, y + Y_GAP), fill=fill_color, tags=tag_number)
        x += X_GAP
        tag_number += 1

    x = X_OFFSET + 0 * X_GAP
    y = Y_OFFSET - 10 - 110
    for i in range(13):
        fill_color = "light gray"
        w.create_rectangle((x, y , x + X_GAP, y + Y_GAP), fill=fill_color, tags=tag_number)
        x += X_GAP
        tag_number += 1

    card_list = list(Deck().deal_3deck(1))[0]
    card_list = sorted(card_list, key=suit_rank_sort)
    card_list = list(card_list)
    X_OFFSET = 20
    Y_OFFSET = 300 - 60 + 220
    CARD_GAP = 80
    y = 10 + 30 + 20
    x = X_OFFSET
    for card in card_list:
        # print card, x, Y_OFFSET, image_dict[card]
        w.create_image(x/3, Y_OFFSET, image=image_dict[card], anchor=NW, tags=("token", card))
        x += CARD_GAP
        if x > 3060:
             x = 20
             Y_OFFSET += 90

def show_best25_hand(*args):
    """ Given  twenty_five cards, find the best hand and show scoring"""

    global message_left_click_label
    global cumulative_score
    player_score = show_player_score()
    player_total_score = player_score[0]

    message_left_click_label = tk.Label(text="Show Next Hand")

    # make sure there are cards in twentyfive_cards
    if twentyfive_cards == []:
        message_left_click_label = tk.Label(text="Show Next Hand")
        message_left_click_label.pack()
        return

    message_left_click_label.pack_forget()

    card_list2 = twentyfive_cards
    card_list2_string = ", ".join(card_list2)
# logging.info(card_list2_string)

    start_time = time.time()
    temp_card_list2 = list(card_list2)
    myhand = BestHand25Wild(temp_card_list2)
    score = myhand.best_hand_points
    best_25handx = myhand.best_25handx

    end_time = time.time()
    lapse_time = round(end_time - start_time,2)
    print (lapse_time)

    best_card_list1 = best_25handx[6] + best_25handx[5] + best_25handx[4] + \
                      best_25handx[3] + best_25handx[2] + best_25handx[1]

    # showing best hand
    top.title("Best Hand Below and Best Scores on Right")
    X_OFFSET = 11 + 4
    j = 0
    for i in range(1):
        x = X_OFFSET + 5
        y = 10 * (j + 1)
        j += 1
        for card in best_card_list1[0:13]:  # first 13 cards
            # print card, x, y, image_dict[card]
            w.create_image(x, y, image=image_dict[card[0:3]], anchor="nw", tag="best")
            x += X_GAP
        y += Y_GAP #row 2
        x = X_OFFSET + 5

        for card in best_card_list1[13:25]:  # last 7-12 cards
           # print (card, x, y, image_dict[card])
            w.create_image(x, y, image=image_dict[card[0:3]], anchor="nw", tag="best")
            x += X_GAP

        # show scores of best hand
        x_label = 11 * X_GAP
        y_label = 310 # aligns with best_hand
        x = x_label
        y = y_label
        display_score(score, x, y)

        player_total_adv = player_total_score - score[0]

        # keep track of wins, losses and ties
        global wins
        global ties
        global losses
        global cumulative_score

        if player_total_score > score[0]:
            message = "You Win"
            wins += 1
        elif score[0] > player_total_score:
            message = "You Lose"
            losses +=1
        elif score[0] == player_total_score:
            message = "It's a Tie"
            ties +=1
        cumulative_score += player_total_adv
        cumulative_score = round(cumulative_score,2)

        # show wins, losses, ties and cumulative points
        wins_label = tk.Label(text="wins = " + str(wins) + 5 * " ", fg="blue", bg="white")
        wins_label.place(x=1080-500, y=700)
        losses_label = tk.Label(text="losses = " + str(losses) + 5 * " ", fg="blue", bg="white")
        losses_label.place(x=1080-500, y=725)
        ties_label = tk.Label(text="ties = " + str(ties)+ 5 * " ", fg="blue", bg="white")
        ties_label.place(x=1080-500, y=750)
        cum_label = tk.Label(text="cum = " + str(cumulative_score) + 12 * " ", fg="blue", bg="white")
        cum_label.place(x=1080-500, y=775)
        message_label = tk.Label(text=message+"  ", fg="red", bg="white", )
        message_label.config (font=("arial", 20))
        message_label.place(x = 1080-350, y =400)
def show_player_score():
    """ First, it determines how player set his hand based on position of cards in twentyfive_cards"""
    print ("entering display_player_points")
    players_25card_hand = 25*[-1]

    # make sure every card is use
    player_hand = [[],[],[],[],[],[],[]]
    hand_diff = [-2, 3, 7, 10, 13, 15]  # hand_diff[0] = -2 which is hand6
    for card in twentyfive_cards:
         # X_GAP = 80
         # print ("card", card)
         card_placex = int((w.coords(card)[0] + X_OFFSET)/X_GAP)  # determines x coordinate of card
         card_placey = int((w.coords(card)[1])) # determines y coordinate of card
         # print (card, card_placex, card_placey)
     # logging.info((card, w.coords(card)[0], card_placex, card_placey))

         # make sure card is in playing card area
         if card_placey >= 229 and card_placex <= 850:
             hand_number = card_placey//100 - 2 # y is 229, 329, 429, etc.
             # hand_number = 0 when hand is 6; 1, 5; 2, 4; 3, 3; 4, 2; 5, 1
             real_hand_number = 6 - hand_number
             card_number = card_placex + hand_diff[hand_number]
             players_25card_hand[card_number] = str(card)
             player_hand[real_hand_number].append(card)
             # print (card, card_placex, card_placey, real_hand_number)

             # hand_number = card_placey//100 - 2 # hand6 = 0, hand5 = 1, etc
             # converted_hand_number = 6 - hand_number
             # card_number = card_placex + hand_diff[hand_number]
             # # print card_number
             # players_25card_hand[card_number] = str(card)
             # player_hand[converted_hand_number].append(card)

    # for hand in player_hand:
    #     print (hand)

    player = PlayerHand(player_hand)
    player_hand_points = player.player_hand_score

    player_points_total = player_hand_points[0]
    print ("Player point", player_points_total)

    valid_hand = True
    for i in range (1,6):
        if player_hand_points[i+1] < player_hand_points[i]:
            valid_hand = False
            # print "hand",i+1, "is less than hand", i

    # if player socre is invalid
    if valid_hand == False:
        message = "Player Hand Invalid"
        x_label = 11 * X_GAP  # for labels
        y_label = 310 + 150 + 110  # aligns with player hand
        x = x_label
        y = y_label + 25
        valid_hand_label = tk.Label(text=message, fg="red", bg="white")
        valid_hand_label.place(x=x - 150, y=y)
        display_score(player_hand_points, x, y + 25)
        # print "player hand is invalid"
        return player_hand_points

    # logging.info((players_25card_hand))
    else:
         message = "Player Hand Valid   "
    # print player_hand6,player_hand5,player_hand4,player_hand3, player_hand2, player_hand1, player_total

    x_label = 11 * X_GAP  # for labels
    y_label = 310 + 150 + 110 # aligns with player hand
    x = x_label
    y = y_label + 25
    valid_hand_label = tk.Label(text=message , fg="blue", bg="white")
    valid_hand_label.place(x=x-150, y=y)
    display_score(player_hand_points, x, y + 25)
    return player_hand_points

def text_solve_best25_hand(*args):
    """ Given  twenty_five cards, solve for the best hand and show scoring"""
    # # X_GAP = 80
    # Y_GAP = 110
    X_OFFSET = 11 + 4
    # global twentyfive_cards
    candidate_25card_hand = []
    card_list = list(Deck().deal_3deck(1))[0]
    card_list = sorted(card_list, key=suit_rank_sort)
    card_list = list(card_list)
    for card in card_list:
        card_placex = int((w.coords(card)[0] + X_OFFSET) / X_GAP)  # determines x coordinate of card
        card_placey = int((w.coords(card)[1]))  # determines y coordinate of card
        # logging.info((card, w.coords(card)[0], card_placex, card_placey))
        # print card, card_placex, card_placey
        if card_placey <  229 + 220 and card_placex <= 1200:
            candidate_25card_hand.append(card)

    card_list2 = sorted(candidate_25card_hand, key=suit_rank_sort, reverse=True)
    twentyfive_cards = card_list2
    # card_list2_string = ", ".join(card_list2)
    # logging.info(card_list2_string)
    # print card_list2
    start_time = time.time()
    best_hand = BestHand25Wild(card_list2)
    # best_wild_card1, best_wild_card2, best_wild_card3, best_card_list1, best_hand_points, best_25handx = BestHand25Wild(card_list2)
    best_card_list1 = best_hand.best_25handx[6] + best_hand.best_25handx[5]+ best_hand.best_25handx[4]\
                      + best_hand.best_25handx[3]+ best_hand.best_25handx[2]+ best_hand.best_25handx[1]

    score6, score5, score4, score3, score2, score1, score0 = best_hand.best_hand_points[6], best_hand.best_hand_points[5], best_hand.best_hand_points[4], \
                                    best_hand.best_hand_points[3], best_hand.best_hand_points[2], best_hand.best_hand_points[1], best_hand.best_hand_points[0]
    end_time = time.time()
    lapse_time = end_time - start_time
    # print "Time to find best hand: ", lapse_time
    # print score7
    score0 = round(score0,2)

     # showing best hand
    top.title("Best Hand Below and Best Scores on Right")
    # w.delete("all")
    X_OFFSET = 11 + 4
    j = 0
    for i in range(1):
        x = X_OFFSET + 5
        y = 10 * (j + 1)
        j += 1
        for card in best_card_list1[0:13]:  # hand6
            # print card, x, y, image_dict[card]
            w.create_image(x, y, image=image_dict[card], anchor="nw", tag="best")
            x += X_GAP

        y += Y_GAP #row 2
        x = X_OFFSET + 5

        for card in best_card_list1[13:25]:  # hand3
           # print card, x, y, image_dict[card]
            w.create_image(x, y, image=image_dict[card], anchor="nw", tag="best")
            x += X_GAP

        # showing points of best hand
        x_label = 13.5 * X_GAP
        y_label = 60 # aligns with best_hand
        x = x_label
        y = y_label
        score_array = (0, 0, 0, 0, 0, 0, 0, 0)
        score_array = (score0, score1, score2, score3, score4, score5, score6)
        display_score(score_array, x, y)

if MODE == "Solve" or MODE == "Text":
    XGAP = 80
    w = tk.Canvas(top, height=950, width=13.5 * XGAP, background="pink", relief="raised")
    m_box = tk.Tk()
    X_OFFSET = 11
    wins = 0
    losses = 0
    ties = 0
    cumulative_score = 0
    image_dir = "Cards_gif/"
    image_dict = create_images()

    next_setup_button = Button(top, text="Next Setup", command=show_next_hand)
    show_twentyfive_cards_button = Button(top, text="Buy Cards", command=show_twentyfive_cards)
    text_solve_best25_hand_button = Button(top, text="Solve - User Input", command=text_solve_best25_hand)

    show_player_score_button = Button(top, text="Player Hand Score", command=show_player_score)
    suit_button = Button(top, text="Suit", command=suit_quick_sort)
    rank_button = Button(top, text="Rank", command=rank_quick_sort)

    next_setup_button.pack()
    text_solve_best25_hand_button.pack()
    show_player_score_button.pack(side=RIGHT)
    show_twentyfive_cards_button.pack(side=RIGHT)
    suit_button.pack(side=RIGHT)
    rank_button.pack(side=RIGHT)
    w.pack()

    w.tag_bind("token", "<Button-1>", onClick)
    w.tag_bind("token", "<B1-Motion>", onMotion)
    w.tag_bind("token", "<ButtonRelease-1>", onRelease)
    if MODE == "Text":
        input_string = input("Enter 25 Cards: ")
        card_listx = input_string.split(",")
        card_list = sorted(card_listx, key=rank_sort, reverse=True)
        print (card_list)
        show_card_list()
    else:
        show_deck_of_cards()

if MODE == "Interactive":
    XGAP = 80
    save_position1 = 25 * [[]]
    w = tk.Canvas(top, height=900, width=13.5 * XGAP, background="pink", relief="raised")
    m_box = tk.Tk()
    X_OFFSET = 11
    wins = 0
    losses = 0
    ties = 0
    cumulative_score = 0
    image_dir = "Cards_gif/"
    image_dict = create_images()
    twentyfive_cards = []
    show_next_hand()

    show_next_hand_button = tk.Button(top, text="Show Next Hand", command=show_next_hand).place(x=1080-200,y=250,width=140, height=24)
    show_best25_hand_button = tk.Button(top, text="Show Best Hand", command=show_best25_hand).place(x=1080-200,y=275,width=140, height=24)
    show_player_score_button = tk.Button(top, text="Player Score", command=show_player_score).place(x=1080-200, y=525-40, width=140, height=24)
    suit_button = tk.Button(top, text="Suit", command=suit_quick_sort).place(x=1080-200, y=550-40, width=140, height=24)
    rank_button = tk.Button(top, text="Rank", command=rank_quick_sort).place(x=1080-200, y=575-40, width=140, height=24)
    save_button = tk.Button(top, text="Save", command=save_position).place(x=1080-200, y=600-40, width=140, height=24)
    restore_button = tk.Button(top, text="Restore", command=restore_position).place(x=1080-200, y=625-40, width=140, height=24)

    w.pack()

    w.tag_bind("token", "<Button-1>", onClick)
    w.tag_bind("token", "<B1-Motion>", onMotion)
    w.tag_bind("token", "<ButtonRelease-1>", onRelease)

top.mainloop()