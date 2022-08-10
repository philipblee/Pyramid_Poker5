import statistics as stats
from sort_cards import *
from BestHand25Wild import *
from PokerHand import *
from ShowDownPoints import *
from MyHand20_Analysis import *
from MyHand20_Analysis2 import *
from WriteFile import *
import datetime
import json
from ShowDownPoints import *
from ShowDownGame import *
import global_variables

k_num = 0
wild_count = [0, 0, 0, 0]
import tkinter as tk

class PlaySixHands20():

    """ Given six_hands, PlaySixHands25 plays all six hands and determines:
        self.points_stored = points_stored
        self.hand_stored = hands_stored
        self.player_score_hand20 = player_score_hand20
        self.play_hand20_quality = play_hand20_quality
        self.player_score_prediction = player_score_prediction
        self.play_hand25 = play_hand25
        self.player_wilds = player_wilds

        after that it uses ShowDownPoints to determine:
        self.player_points = winpoints.player_points
        self.player_win_points = winpoints.player_win_points    """

    def __init__(self, six_hands):
        global k_num, wild_count
        special_play_score = global_variables.special_play_score
        simulation_deck = Deck()
        my_hand = PokerHand()
        play_hand20_quality = ["", "", "", "", "", "", ""]
        player_score_hand20 =[0,0,0,0,0,0]
        player_names = ["Peter ", "Johnny", "Ming  ", "Tony  ", "Edmond", "Philip"]
        player_score_prediction = [0, 0, 0, 0, 0, 0, 0]
        points_stored = [[], [], [], [], [], [], []]
        hands_stored = [[], [], [], [], [], [], []]
        points_stored_best = [[],[],[],[],[],[]]
        hand20_signal = [0, 0, 0, 0, 0, 0]
        player_wilds = [0, 0, 0, 0, 0, 0]
        play_hand20 = [False, False, False, False, False, False]
        for hand_number in range(6):
            card_list = six_hands[hand_number]
            # print card_list
            card_list2_unsorted = list(card_list[0:NUMBER_OF_CARDS])  # deal number_of_cards
            card_list2 = (sorted(card_list2_unsorted, key=rank_sort, reverse=True))
            wild_cards = 0
            # count number of wild cards
            if card_list2[2][0:2] == "WW":  wild_cards = 3
            elif card_list2[1][0:2] == "WW":  wild_cards = 2
            elif card_list2[0][0:2] == "WW":  wild_cards = 1

            if wild_cards == 1:  wild_count[1] += 1
            elif wild_cards == 2:  wild_count[2] += 1
            elif wild_cards == 3:  wild_count[3] += 1

            player_wilds[hand_number] = wild_cards
            start_time = time.time()
            player_wilds[hand_number] = wild_cards
            print ("\nGame#", k_num + 1, "Hand#", (k_num) * 6 + hand_number + 1, "One Wild=", wild_count[1], \
                "Two Wild=", wild_count[2], "Three Wild=", wild_count[3], "=========== New Hand ===============")

            # Look at first 20 cards and decide what to do
            card_list20 = list(card_list2_unsorted[0:20])
            card_list20 = (sorted(card_list20, key=rank_sort, reverse=True))
            card_list_temp = list(card_list20)
            print (player_names[hand_number], "is the player.  Analysis to follow.")
            print ("Player's 20 Card Hand: ", card_list20)

            # analysis2 = MyHand20_Analysis2(card_list_temp)

            myhand20 = BestHand25Wild(card_list_temp)
            card_list_temp = list(card_list20)
            match = MyHand20_Analysis(card_list_temp)
            hand20_signal[hand_number] = match.hand20_signal
            # print ("average_matches, matches", match.average_matches, match.matches)
            # print ("20 Cards-Best Hand", myhand20.best_25handx[1:7])
            # print ("20 Cards-Best Points", myhand20.best_hand_points)
            average_score = 0
            simulation_hands = int(200)
            # print "20 Simulated Hands -",
            points_predicted_list = []
            kitty_cards_used_list = []
            for i in range(simulation_hands):
                kitty_cards = simulation_deck.deal_5random_cards(card_list20)
                card_list25 = kitty_cards + card_list20
                myhand = BestHand25Wild(card_list25)
                points = myhand.best_hand_points
                best_25handx = myhand.best_25handx
                # determine number of kitty cards used
                kitty_cards_used = []
                for j in range (1,7):
                    kitty_cards_used.extend(list(set(myhand.best_25handx[j]).intersection(kitty_cards)))
                for card in kitty_cards:
                    if card[0:2] == "WW":
                        kitty_cards_used.append(card)
                print("Simulation", i + 1, kitty_cards)
                print ("# kitty cards used=", len(kitty_cards_used),kitty_cards_used)
                print (" ", myhand.best_hand_points[0], myhand.best_25handx)
                kitty_cards_used_list.append(len(kitty_cards_used))
                average_score += myhand.best_hand_points[0]
                points_predicted_list.append(points[0])
            average_score = round(average_score / simulation_hands,1)
            points_predicted_list.sort()
            print()
            print()
            print(points_predicted_list)
            points_predicted_mean = round(stats.mean(points_predicted_list),2)
            points_predicted_stdev = round(stats.stdev(points_predicted_list),2)
            print ("mean=", points_predicted_mean, "stdev=", points_predicted_stdev)
            # for j in range (0, simulation_hands, int(simulation_hands/4)):
            #     points_predicted_mean = round(stats.mean(points_predicted_list[j*simulation_hands:j+1*simulation_hands]),2)
            #     points_predicted_stdev = round(stats.stdev(points_predicted_list[j*simulation_hands:j+1*simulation_hands]),2)
            #     print(j, "mean=", points_predicted_mean, "stdev=", points_predicted_stdev)

            kitty_cards_used_list.sort()
            print (kitty_cards_used_list)
            print ("kitty cards used mean, stdev",stats.mean(kitty_cards_used_list), stats.stdev(kitty_cards_used_list))
            player_score_prediction[hand_number] = average_score
            player_score_hand20[hand_number] = myhand20.best_hand_points[0]
            print ("    = Average Prediction Score", average_score,)
            minimum_play_score = global_variables.minimum_play_score
            minimum_h20_play_score = -2000
            # special_play_score = [1300, 1400, 1500, 1600, 1700, 1800]
            # special_player_play =  [False, False, False, False, False, False]

            if average_score >= global_variables.player_minimums[hand_number]:
                play_hand20[hand_number] = True
            else:
                play_hand20[hand_number] = False

            if average_score >=1000:
                print ("Play this Monster Hand")
                play_hand20_quality[hand_number] = "Monster"
            elif average_score >= 500:
                print ("Play this Good Hand")
                play_hand20_quality[hand_number] = "Good"
            elif average_score >= minimum_play_score:
                print ("Play this Marginal Hand")
                play_hand20_quality[hand_number] = "Ok"
            elif average_score >= -500:
                print ("Surrender this Marginal Hand")
                play_hand20_quality[hand_number] = "Not Ok"
            else:
                print ("Surrender this Sad Hand")
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
            print ("5-card kitty", kitty_cards)
            print ("25 Cards-Card List", card_list2)
            print ("25 Cards-Best Hand", myhand.best_25handx[1:7])
            print ("25 Cards-Best Points", myhand.best_hand_points)
            kitty_cards_used = []
            for j in range(1, 7):
                kitty_cards_used.extend(list(set(myhand.best_25handx[j]).intersection(kitty_cards)))
            best_card_list1 = json.dumps(best_25handx[1:7])
            print ("number of kitty_cards used", len(kitty_cards_used), kitty_cards_used)
            end_time = time.time()
            lapse_time = round(end_time - start_time, 2)
            print ("--Elapsed Time = ", lapse_time)
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
            if wild_cards == 0:  w0 = str(points[0])
            elif wild_cards == 1:  w1 = str(points[0])
            elif wild_cards == 2:  w2 = str(points[0])
            elif wild_cards == 3:  w3 = str(points[0])
            cumulative_learning_string += "," + str(wild_cards) + ", " + w0 + ", " + w1 + ", " + w2 + ", " + w3
            cumulative_learning_string1 = cumulative_learning_string +  str(play_hand20[hand_number]) + "\n"

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
            cumulative_medium_scores += str(medium_score[1]) +  ", " + str(points[1][1]) + ", "
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

            for i in range(1,7):
                hand_description_string = my_hand.get_description_from_score(points[i][0], str(i))
                print ('{:>11}'.format(hand_description_string), end=" ")

            print
            print ("\nHand Summary:")
            print ("   - h20_score ", myhand20.best_medium_score[0], end=" ")
            if myhand20.best_medium_score[0] >= minimum_play_score-1000:
                print ("play")
            else:
                print ("do not play")
            print ("   - prediction", average_score, end=" ")
            if average_score >= minimum_play_score:
                print ("play")
            else:
                print ("do not play")
            print ("   - h20_signal", match.hand20_signal, end =" ")
            if match.hand20_signal >= 5:
                print ("play")
            else:
                print ("do not play")
            print ("   - actual points", myhand.best_hand_points[0], end=" ")
            if myhand.best_hand_points[0] >= minimum_play_score:
                print ("play")
            else:
                print ("do not play")
            if abs(myhand.best_hand_points[0] - average_score) < 500:
                print ("   - actual within 500 of prediction")
            else:
                print ("   - actual not within 500 of prediction")
            print ("Actual over Prediction:", round(myhand.best_hand_points[0] - average_score, 1))

        k_num = k_num + 1
        # save_wins = -1

        winpoints = ShowDownPoints(points_stored, hands_stored, play_hand20)
        sd = ShowDownGame(winpoints.player_points, play_hand20)

        self.points_stored = points_stored
        self.hand_stored = hands_stored
        self.player_score_hand20 = player_score_hand20
        self.play_hand20_quality = play_hand20_quality
        self.player_score_prediction = player_score_prediction
        self.play_hand20 = play_hand20
        self.player_wilds = player_wilds
        self.hand20_signal = hand20_signal

        # winpoints = ShowDownPoints(points_stored, play_hand25)
        self.player_points = winpoints.player_points
        self.player_win_points = winpoints.player_win_points

        print()
        for i in range(6):
            # print ("player", i, end = "")
            print ('{:8}'.format(player_names[i]), end=" ")
            print (points_stored[i])

        print()
        for i in range(6):
            print ('{:8}'.format(player_names[i]), end=" ")
            #print ("player", i, end="")
            for j in range(1,7):
                hand_description_string = my_hand.get_description_from_score(points_stored[i][j][0], str(j))
                print ('{:>12}'.format(hand_description_string), end="")
            print()

        return ()