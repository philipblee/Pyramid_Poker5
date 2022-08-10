from BestHand25Wild import *
from WriteFile import *
from PokerHand import *
import time
import datetime
import os
from tkinter import *
from CumulativeLearning import *
from ReadProbability import *
import json
from PlayerHand import PlayerHand
from WriteGameSummary import *
from MyHand20_Analysis import *
from ShowDownGame import *
import sys

# PARAMETERS
# RunPyramidPoker2 - uses special_player to see how various strategies affect results
NUMBER_OF_HANDS = 10
PRINT_HAND_FREQUENCY = 1
NUMBER_OF_CARDS = 25 #default
NUMBER_OF_WILD_CARDS = 3

my_hand = PokerHand()

X_GAP = 80
Y_GAP = 110
X_OFFSET = 11
global card_list

if sys.argv[1] == "Batch" or sys.argv[1] == "Interactive":
    MODE = sys.argv[1]
else: MODE = "Interactive" #default

if int(sys.argv[2]) > 0 and int(sys.argv[2]) <10000:
    NUMBER_OF_HANDS = int(sys.argv[2])

else:
    NUMBER_OF_HANDS = 10  #default

print (MODE)
print ("Number of arguments:", len(sys.argv))
print ("Argument List:", str(sys.argv))
simulation_deck = Deck()

top = Tk()
this_hand = PokerHand()

if MODE == "Batch":
    overall_start_time = time.time()
    NUMBER_OF_CARDS = 25
    wild_count = [0, 0, 0, 0]
    hands_stored = [[],[],[],[],[],[],[]]
    points_stored = [[],[],[],[],[],[],[]]
    play_hand20_quality = ["", "", "", "", "", "", ""]
    player_running_wins = [0, 0, 0, 0, 0, 0]
    player_wilds = [0,0,0,0,0,0]
    play_hand20 = [False, False, False, False, False, False]
    player_names = ["Peter ", "Johnny", "Ming  ", "Tony  ", "Edmond", "Philip"]
    player_score_prediction = [0,0,0,0,0,0,0]
    player_running_ante = [0,0,0,0,0,0,0]
    player_running_surrender = [0,0,0,0,0,0,0]
    player_running_points = [0, 0, 0, 0, 0, 0]
    player_running_totals = [0, 0, 0, 0, 0, 0]
    player_score_hand20 =[0,0,0,0,0,0,0]
    player_wins = [0, 0, 0, 0, 0, 0]

    for k_num in range (NUMBER_OF_HANDS):
        six_hands = Deck.deal_6hands()[0]
        for hand_number in range(6):
            card_list = six_hands[hand_number]
            # print card_list
            card_list2_unsorted = list(card_list[0:NUMBER_OF_CARDS])  # deal number_of_cards
            card_list2 = (sorted (card_list2_unsorted, cmp=rank_sort, reverse=True))
            wild_cards = 0
            # count number of wild cards
            if card_list2[2][0:2] == "WW":  wild_cards = 3
            elif card_list2[1][0:2] == "WW":  wild_cards = 2
            elif card_list2[0][0:2] == "WW":  wild_cards = 1

            if wild_cards == 1:  wild_count[1] += 1
            elif wild_cards == 2:  wild_count[2] += 1
            elif wild_cards == 3:  wild_count[3] += 1
            start_time = time.time()
            player_wilds[hand_number] = wild_cards
            if k_num%PRINT_HAND_FREQUENCY == 0:
                print "\nGame#", k_num+1, "Hand#", (k_num)*6 + hand_number + 1, "One Wild=", wild_count[1],\
                    "Two Wild=", wild_count[2], "Three Wild=", wild_count[3], "=========== New Hand ==============="

            # Look at first 20 cards and decide what to do
            card_list20 = list(card_list2_unsorted[0:20])
            card_list20 = (sorted (card_list20, cmp=rank_sort, reverse=True))
            card_list_temp = list(card_list20)
            print ("20 Card Hand before", card_list20)
            myhand20 = BestHand25Wild(card_list_temp)
            print ("20 Card Hand", myhand20.best_25handx)
            print ("20 Card Hand", myhand20.best_hand_score)

            print player_names[hand_number],
            for i in range(1,7):
                hand_description_string = my_hand.get_description_from_score(myhand20.best_hand_score[i][0], str(i))
                print '{:>11}'.format(hand_description_string),
            print
            card_list_temp = list(card_list20)
            match = MyHand20_Analysis(card_list_temp)
            print "average_matches, matches", match.average_matches, match.matches
            average_score = 0
            simulation_hands = 4
            for i in range(simulation_hands):
                card_list25 = simulation_deck.deal_5random_cards(card_list20) + card_list20
                # print "\n", i + 1, card_list25
                myhand = BestHand25Wild(card_list25)
                score = myhand.best_hand_score
                best_25handx = myhand.best_25handx
                # print "  ", myhand.best_25handx
                print "\n", myhand.best_hand_score,
                # print "  ", player_names[hand_number],

                for i in range(1, 7):
                    hand_description_string = my_hand.get_description_from_score(score[i][0], str(i))
                    print '{:>11}'.format(hand_description_string),
                average_score += myhand.best_hand_score[0]
            average_score = average_score / simulation_hands
            player_score_prediction[hand_number] = average_score
            player_score_hand20[hand_number] = myhand20.best_hand_score[0]

            print "\nAverage Score", average_score
            minimum_play_score = 1600
            special_player_score = [1300, 1400, 1500, 1600, 1700, 1800]
            special_player_play =  [False, False, False, False, False, False]

            if hand_number != 5:
                if average_score >= minimum_play_score:
                    play_hand20[hand_number] = True
                else:
                    play_hand20[hand_number] = False
            else:       # for Philip, play anything above 1500
                for special in range(6):
                    if average_score >= special_player_score[special]:
                        special_player_play[special] = True
                    else:
                        special_player_play[special] = False
                    print "special_player_score", special, special_player_score[special], special_player_play[special]
            if average_score >= minimum_play_score + 800:
                print "Play this Monster Hand"
                play_hand20_quality[hand_number] = "Monster"
            elif average_score >= minimum_play_score + 400:
                print "Play this Good Hand"
                play_hand20_quality[hand_number] = "Good"
            elif average_score >= minimum_play_score:
                print "Play this Marginal Hand"
                play_hand20_quality[hand_number] = "Ok"
            elif average_score >= minimum_play_score - 400:
                print "Surrender this Marginal Hand"
                play_hand20_quality[hand_number] = "Not Ok"
            else:
                print "Surrender this Sad Hand"
                play_hand20_quality[hand_number] = "Sad"

            # Pick up 5 card kitty and play hand
            card_list1 = list(card_list2)
            myhand = BestHand25Wild(card_list1)
            score = myhand.best_hand_score
            best_25handx = myhand.best_25handx
            cards_used = 0
            for i in range(1,7):
                cards_used += len(best_25handx[i])
            cards_left = 25 - cards_used
            best_card_list1 = json.dumps(best_25handx[1:7])
            points_stored[hand_number] = score
            hands_stored[hand_number] = best_25handx
            print "\n25 Card Hand", card_list2
            print "25 Card Hand", myhand.best_25handx
            print "25 Card Hand", myhand.best_hand_score

            # minimum_actual_score = 1600
            # phil_min_actual_score = 1500
            # print "minimum_play_score, phil_min_actual_score", minimum_play_score, phil_min_actual_score
            # if hand_number != 5:
            #     pass
            #     # if average_score >= minimum_play_score:
            #     #     play_hand25[hand_number] = True
            #     # else:
            #     #     play_hand25[hand_number] = False
            # else:       # for Philip, play anything above 1500
            #     if myhand.best_hand_score[0] >= phil_min_actual_score:
            #         play_hand25[hand_number] = True
            #     else:
            #         play_hand25[hand_number] = False

            hand_improvement = myhand.best_hand_score[0] - myhand20.best_hand_score[0]
            print "Hand improvement", hand_improvement

            print player_names[hand_number],
            for i in range(1,7):
                hand_description_string = my_hand.get_description_from_score(score[i][0], str(i))
                print '{:>11}'.format(hand_description_string),

            end_time = time.time()
            lapse_time = round(end_time - start_time, 2)
            print "--Time = ", lapse_time
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
            cumulative_learning_string2 += str(card_list2) + ","
            cumulative_learning_string2 += str(best_card_list1) + (cards_left+1) * ","
            cumulative_learning_string2 += str(k_num + 1) + ", " + str(hand_number + 1) + ", "
            for j in range(1,7):
                hand_description_string = my_hand.get_description_from_score(points_stored[hand_number][j][0], str(j))
                cumulative_learning_string2 += hand_description_string + ","
            cumulative_learning_string2 += "\n"
            x = WriteFile(cumulative_learning_string2)

        print
        for i in range(6):
            print points_stored[i]

        print
        for i in range(6):
            print '{:8}'.format(player_names[i]),
            for j in range(1,7):
                hand_description_string = my_hand.get_description_from_score(points_stored[i][j][0], str(j))
                print '{:>12}'.format(hand_description_string),
            print

        # calculate who wins how many points round robin
        # hands_stored is 1-6, points_stored is 1-6
        running_winpoints = 0
        player_points = [0,0,0,0,0,0]
        player_win_loss = ['','','','','','']
        player_win_points = 7*[7*[[0,0,0,0,0,0,0]]]

        # print player_win_points
        print
        for special in range(6):
            play_hand20[5] = special_player_play[special]
            print "\n", special, special_player_score[special], special_player_play[special]
            all_surrender = True
            for i in range(6):
                if play_hand20[i] == True:
                    print player_names[i],
                    all_surrender = False
                    temp_player_sum = 0
                    for j in range (6):
                        temp_hand_sum = 0
                        if play_hand20[j] == True:
                            for k in range(1,7):
                                if i != j:
                                    if points_stored[i][k][0] > points_stored[j][k][0]:
                                        player_win_points[i][j][k] = 1 * this_hand.get_winpoints_from_score(points_stored[i][k][0],str(k))
                                    elif points_stored[i][k][0] < points_stored[j][k][0]:
                                        player_win_points[i][j][k] = -1 * this_hand.get_winpoints_from_score(points_stored[j][k][0],str(k))
                                    elif points_stored[i][k][0] == points_stored[j][k][0]:
                                        player_win_points[i][j][k] = 0
                                else:
                                    player_win_points[i][j][k] = 0
                                # print i,j,k,player_win_points[i][j][k]
                                temp_hand_sum += player_win_points[i][j][k]
                            player_win_points[i][j][0] = temp_hand_sum
                            print '{:>29}'.format(str(player_win_points[i][j])),
                            player_win_loss[i] += str(player_win_points[i][j]) + ', '
                            temp_player_sum += temp_hand_sum
                            player_points[i] = temp_player_sum
                    # print '{:^180}'.format(str(player_win_points[i]))
                    print '{:>5}'.format(temp_player_sum)

        # let's loop through player_special_score to check results of different play thresholds
        for special in range(6):
            play_hand20[5] = special_player_play[special]
            print "\n", special, special_player_score[special], special_player_play[special]
            sd = ShowDownGame(player_points, play_hand20)
            print '  Name    Wilds H20      Predict Actual Quality  Play  Summ   Ante  Surr  Ante   Surr  Totals   Wins   Games'
            for i in range(6):
                # print player_running_points[i], player_points[i]
                # print type(player_running_points[i]), type(player_points[i])
                player_running_points[i] = player_running_points[i] + player_points[i]
                player_wins[i] += sd.player_wins[i]
                player_running_ante[i] += sd.player_ante[i]
                player_running_surrender[i] += sd.player_surrender[i]
                player_running_totals[i] += player_points[i] + sd.player_surrender[i] + sd.player_ante[i]
                print '{:>8}'.format(player_names[i]), str(player_wilds[i]),
                print '{:>8}'.format(str(player_score_hand20[i])),
                print '{:>8}'.format(str(player_score_prediction[i])),
                print '{:>8}'.format(str(points_stored[i][0])),
                print '{:>9}'.format(str(play_hand20_quality[i])),
                print '{:>6}'.format(str(play_hand20[i])),
                print '{:>6}'.format(str(player_points[i])), '{:>6}'.format(str(sd.player_surrender[i])),
                print '{:>6}'.format(str(sd.player_ante[i])),
                print '{:>6}'.format(str(player_running_surrender[i])),
                print '{:>6}'.format(str(player_running_points[i])),
                print '{:>6}'.format(str(player_running_totals[i])),
                print '{:>6}'.format(str(player_wins[i])), '{:>6}'.format(k_num + 1)

        game_string = ""
        for i in range(6):
            game_string = (player_names[i]) + ', ' + str(player_wilds[i]) + ', '
            game_string += '{:>6}'.format(str(player_score_hand20[i])) + ', '
            game_string += '{:>6}'.format(str(player_score_prediction[i])) + ', '
            game_string += '{:>6}'.format(str(points_stored[i][0])) + ', '
            game_string += '{:>6}'.format(str(play_hand20_quality[i])) + ', '
            game_string += '{:>6}'.format(str(play_hand20[i])) + ', '
            game_string += '{:>6}'.format(str(player_points[i])) + ', '
            game_string += '{:>6}'.format(str(sd.player_surrender[i])) + ', '
            game_string += '{:>6}'.format(str(sd.player_ante[i])) + ', '
            game_string += '{:>6}'.format(str(player_running_surrender[i])) + ', '
            game_string += '{:>6}'.format(str(player_running_points[i])) + ', '
            game_string += '{:>6}'.format(str(player_running_totals[i])) + ', '
            game_string += '{:>6}'.format(str(player_wins[i])) + ', ' + '{:>6}'.format(str(k_num + 1)) + ', '
            for j in range(1, 7):
                hand_description_string = my_hand.get_description_from_score(points_stored[i][j][0], str(i))
                game_string += '{:}'.format(hand_description_string)
            game_string += '{:>30}'.format(str(points_stored[i])) + "\n"
            # print game_string,
            x = WriteGameSummary(game_string)

    overall_end_time = time.time()
    lapse_time = round(overall_end_time - overall_start_time, 2)
    print "finished", lapse_time, round(lapse_time/NUMBER_OF_HANDS, 2)

def display_score(score_array, x, y):
    score = score_array
    total_score_label = Label(text="total points = " + str(score[0]) + 20*" ", fg="blue", bg="white")
    total_score_label.place(x=x, y=y)
    hand6_score_label = Label(text="hand6 = " + str(score[6]) + 30*" ", fg="blue", bg="white")
    hand6_score_label.place(x=x, y=y + 25)
    hand5_score_label = Label(text="hand5 = " + str(score[5]) + 30*" ", fg="blue", bg="white")
    hand5_score_label.place(x=x, y=y + 50)
    hand4_score_label = Label(text="hand4 = " + str(score[4]) + 30*" ", fg="blue", bg="white")
    hand4_score_label.place(x=x, y=y + 75)
    hand3_score_label = Label(text="hand3 = " + str(score[3]) + 30*" ", fg="blue", bg="white")
    hand3_score_label.place(x=x, y=y + 100)
    hand2_score_label = Label(text="hand2 = " + str(score[2]) + 30*" ", fg="blue", bg="white")
    hand2_score_label.place(x=x, y=y + 125)
    hand1_score_label = Label(text="hand1 = " + str(score[1]) + 30*" ", fg="blue", bg="white")
    hand1_score_label.place(x=x, y=y + 150)

def create_images():
    """create all card images as a card_name:image_object dictionary"""
    global first_time_images
    first_time_images= True
    if first_time_images == True:
        all_cards_list = Deck().deal_3deck(1)[0]
        image_dict = {}
        for card in all_cards_list:
            # all images have filenames the myhand20_analysis the card_list names + extension .gif
            card_only = card[0:2]
            image_dict[card] = PhotoImage(file=image_dir+card_only+".gif")
            # print "create_images", card, image_dir + card_only+ ".gif"
        image_dict["Deck3"] = PhotoImage(file=image_dir+"Deck3"+".gif")
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

    # which_hand stores [y_coord, hand]; hand6 is 1000, hand5 is 1110, etc
    which_hand = [[0,8], [110,7],[220,6], [330,5], [440,4], [550,3], [660,2], [770,1]]
    current_card_place = []
    current_card_hand = []
    for y_coord, hand in which_hand:
        if my > y_coord:
            current_card_hand = hand
    # which_card stores [x_coord, card]; card1 is 0, card2 is 80, etc.
    which_card = [[0,1], [80,2], [160,3],[240,4], [320,5], [380,6], [460,7], [540,8], [620,9], [700,10], [780,11], [860,12], [940,13]]
    for x_coord, place in which_card:
        if mx > x_coord:
            current_card_place = place
    # print "hand", current_card_hand, "card_place", current_card_place
    # check if current_card_hand and current_card_place is occupied
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
        x1 = mx+80
        x2 = mx+160
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
    if len(cards_left) == 5:
        for object_id in cards_left:
            x_coord = w.coords(object_id)[0]
            y_coord = w.coords(object_id)[1]
            delta_x = destination[index][0] - x_coord
            delta_y = destination[index][1] - y_coord
            w.move(object_id, delta_x, delta_y)
            index += 1
    return

def suit_quick_sort():
    """ sorting by suit and display_cardlist"""
    global twentyfive_cards
    twentyfive_cards = sorted(twentyfive_cards, cmp=suit_rank_sort, reverse=True)
    show_twentyfive_cards()

def rank_quick_sort():
    """ sorting by rank and display_cardlist"""
    global twentyfive_cards
    twentyfive_cards = sorted(twentyfive_cards, cmp=rank_sort, reverse=True)
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
        print card, x, Y_OFFSET, image_dict[card]
        w.create_image(x, Y_OFFSET, image=image_dict[card], anchor=NW, tags=("token", card))
        item_id = w.create_image(x, Y_OFFSET)
        w.create_text(x, Y_OFFSET, text=str(item_id))
        x += CARD_GAP
        if x > 1000:
             x = 20
             Y_OFFSET += 110

def show_next_hand(*args):
    """ Create the card list use Deck().deal and display_cardlist them"""
    print "\n                  ---------------New Hand-----------"
    global twentyfive_cards

    NUMBER_OF_CARDS = 25
    # twentyfive_cards = (sorted(a[0][0:NUMBER_OF_CARDS], cmp=rank_sort, reverse=True))
    top.title("Number of Wild Cards:" + str(NUMBER_OF_WILD_CARDS) + "     Play Pyramid Poker")
    w.delete("all")   # clear out last hand

    # create white rectangles
    Y_OFFSET = 60 + 60 + 102 # add 60 to account for buttons on top
    X_OFFSET = 11  # where cards and rectangles begin
    tag_number = 1

    # create 13 rectangles for first 13 cards
    x = X_OFFSET
    y = Y_OFFSET - 220
    for i in range(13):
        fill_color = "light gray"
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

    # create 10 rectangles - hand 6
    Y_OFFSET = 60 + 60 + 112 # add 60 to account for buttons on top
    x = X_OFFSET
    y = Y_OFFSET - 10
    for i in range(10):
        fill_color = "light yellow"
        if i == 3 or i == 6 or i == 2 or i == 4 or i == 5:
            fill_color = "white"
        item_id = w.create_rectangle((x, y , x + X_GAP, y + Y_GAP), fill=fill_color, tag="hand6")
        x += X_GAP

    # create 7 rectangles - hand 5
    x = X_OFFSET + 80
    y += Y_GAP
    for i in range(7):
        fill_color = "light yellow"
        if i == 3 or i == 1 or i == 2 or i == 4 or i == 5:
            fill_color = "white"
        item_id = w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill=fill_color, tags="hand5")
        x += X_GAP

    # create 6 rectangles - hand 4
    x = X_OFFSET + 2 * X_GAP
    y += Y_GAP
    for i in range(6):
        fill_color = "light yellow"
        if i == 3 or i == 1 or i == 2 or i == 0 or i==4:
            fill_color = "white"
        if i == 4 or i == 0:
            fill_color = "light gray"
        item_id = w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill=fill_color, tags="hand4")
        x += X_GAP

    # create 5 rectangles - hand 3
    x = X_OFFSET + 2 * X_GAP
    y += Y_GAP
    for i in range(5):
        fill_color = "yellow"
        if i == 3 or i == 1 or i == 2 or i == 0 or i == 4:
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

    x_label = 11 * X_GAP
    y_label = 310  # align with next_hand
    x = x_label
    y = y_label
    score_array = (0, 0, 0, 0, 0, 0, 0, 0)
    display_score(score_array, x, y)


    x_label = 11 * X_GAP  # for labels
    y_label = 310 + 150 + 110 # aligns with player hand
    x = x_label
    y = y_label + 100
    message = 50 * " "
    score_array = (0, 0, 0, 0, 0, 0, 0, 0)
    y = y_label + 50
    valid_hand_label = Label(text=message, fg="blue", bg="pink")
    valid_hand_label.place(x=x - 125, y=y)
    display_score(score_array, x, y)

def show_twentyfive_cards():
    w.delete("token")
    X_OFFSET = 8
    Y_OFFSET = 10
    y = Y_OFFSET
    x = X_OFFSET + 9   # adds 5 to move card to center of white rectangle

    for card in twentyfive_cards:
        item_id = w.create_image(x, y, image=image_dict[card], anchor="nw", tags=("token", card))
        # print card, item_id
        x += X_GAP
        if x > 13 * X_GAP:
             x = X_OFFSET + 9
             y += Y_GAP

def show_best25_hand(*args):
    """ Given  twenty_five cards, find the best hand and show scoring"""

    global message_left_click_label

    player_score = show_player_score()
    player_total_score = player_score[0]

    message_left_click_label = Label(text="TBD")

    # make sure there are cards in twentyfive_cards
    if twentyfive_cards == []:
        message_left_click_label = Label(text="Click button - Show Next Hand")
        message_left_click_label.pack()
        return
    message_left_click_label.pack_forget()

    card_list2 = twentyfive_cards
    card_list2_string = ", ".join(card_list2)
    logging.info(card_list2_string)

    start_time = time.time()
    temp_card_list2 = list(card_list2)
    myhand = BestHand25Wild(temp_card_list2)
    score = myhand.best_hand_score
    best_25handx = myhand.best_25handx

    print score
    end_time = time.time()
    lapse_time = end_time - start_time

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
        for card in best_card_list1[0:13]:  # hand6
            # print card, x, y, image_dict[card]
            w.create_image(x, y, image=image_dict[card[0:3]], anchor="nw", tag="best")
            x += X_GAP
        y += Y_GAP #row 2
        x = X_OFFSET + 5

        for card in best_card_list1[13:25]:  # hand3
           # print card, x, y, image_dict[card]
            w.create_image(x, y, image=image_dict[card[0:3]], anchor="nw", tag="best")
            x += X_GAP

        # showing points of best hand
        x_label = 11 * X_GAP
        y_label = 310 # aligns with best_hand
        x = x_label
        y = y_label
        display_score(score, x, y)

        player_total_adv = player_total_score - score[0]

        # keeping points of wins, losses and ties
        global wins
        global ties
        global losses
        global cumulative_points

        if player_total_score > score[0]:
             wins += 1
        elif score[0] > player_total_score:
             losses +=1
        elif score[0] == player_total_score:
             ties +=1
        cumulative_score += player_total_adv

        wins_label = Label(text="wins = " + str(wins) + 5 * " ", fg="blue", bg="white")
        wins_label.place(x=1080-500, y=700)
        losses_label = Label(text="losses = " + str(losses) + 5 * " ", fg="blue", bg="white")
        losses_label.place(x=1080-500, y=725)
        ties_label = Label(text="ties = " + str(ties)+ 5 * " ", fg="blue", bg="white")
        ties_label.place(x=1080-500, y=750)
        cum_label = Label(text="cum = " + str(cumulative_score) + 12 * " ", fg="blue", bg="white")
        cum_label.place(x=1080-500, y=775)

def show_player_score():
    """ First, it determines how player set his hand based on position of cards in twentyfive_cards"""
    print "entering display_player_points"
    players_25card_hand = 25*[-1]

    # make sure every card is use
    player_hand = [[],[],[],[],[],[],[]]

    for card in twentyfive_cards:
         # X_GAP = 80
         card_placex = int((w.coords(card)[0] + X_OFFSET)/X_GAP)  # determines x coordinate of card
         card_placey = int((w.coords(card)[1])) # determines y coordinate of card
         logging.info((card, w.coords(card)[0], card_placex, card_placey))
         # print card, card_placex, card_placey
         if card_placey >= 229 and card_placex <= 850:
             hand_diff = [-2,3,7,10,13,15]   # hand_diff[0] = -2 which is hand6
             hand_number = card_placey//100 - 2 # hand6 = 0, hand5 = 1, etc
             converted_hand_number = 6 - hand_number
             card_number = card_placex + hand_diff[hand_number]
             # print card_number
             players_25card_hand[card_number] = str(card)
             player_hand[converted_hand_number].append(card)

    player = PlayerHand(player_hand)
    player_hand_score = player.player_hand_score

    # player_score_total = player_hand_score[0]
    # print "after points", player_score_total
    print "after points 2", player_hand_score
    valid_hand = True
    for i in range (1,6):
        if player_hand_score[i+1] < player_hand_score[i]:
            valid_hand = False
            print "hand",i+1, "is less than hand", i

    # if player socre is invalid
    if valid_hand == False:
        message = "Player Hand Invalid"
        x_label = 11 * X_GAP  # for labels
        y_label = 310 + 150 + 110  # aligns with player hand
        x = x_label
        y = y_label + 25
        valid_hand_label = Label(text=message, fg="red", bg="white")
        valid_hand_label.place(x=x - 150, y=y)
        display_score(player_hand_score, x, y + 25)
        print "player hand is invalid"
        return player_hand_score

    else:
         message = "Player Hand Valid   "
    # print player_hand6,player_hand5,player_hand4,player_hand3, player_hand2, player_hand1, player_total

    x_label = 11 * X_GAP  # for labels
    y_label = 310 + 150 + 110 # aligns with player hand
    x = x_label
    y = y_label + 25
    valid_hand_label = Label(text=message , fg="blue", bg="white")
    valid_hand_label.place(x=x-150, y=y)
    display_score(player_hand_score, x, y + 25)
    return player_hand_score

if MODE == "Interactive":
    XGAP = 80
    save_position1 = 25 * [[]]
    w = Canvas(top, height=900, width=13.5 * XGAP, background="pink", relief="raised")
    m_box = Tk()
    X_OFFSET = 11
    wins = 0
    losses = 0
    ties = 0
    cumulative_points = 0

    a = Deck.deal()
    image_dir = "../Cards_gif/"
    image_dict = create_images()
    twentyfive_cards = []
    twentyfive_cards = (sorted(a[0][0:NUMBER_OF_CARDS], cmp=rank_sort, reverse=True))
    show_next_hand()

    show_next_hand_button = Button(top, text="Show Next Hand", command=show_next_hand).place(x=1080-200,y=250,width=140, height=24)
    show_best25_hand_button = Button(top, text="Show Best Hand", command=show_best25_hand).place(x=1080-200,y=275,width=140, height=24)
    show_player_score_button = Button(top, text="Player Score", command=show_player_score).place(x=1080-200, y=525-40, width=140, height=24)
    suit_button = Button(top, text="Suit", command=suit_quick_sort).place(x=1080-200, y=550-40, width=140, height=24)
    rank_button = Button(top, text="Rank", command=rank_quick_sort).place(x=1080-200, y=575-40, width=140, height=24)
    save_button = Button(top, text="Save", command=save_position).place(x=1080-200, y=600-40, width=140, height=24)
    restore_button = Button(top, text="Restore", command=restore_position).place(x=1080-200, y=625-40, width=140, height=24)

    w.pack()

    w.tag_bind("token", "<Button-1>", onClick)
    w.tag_bind("token", "<B1-Motion>", onMotion)
    w.tag_bind("token", "<ButtonRelease-1>", onRelease)

top.mainloop()


