""" RunPyramidPoker4 - going to try to expand points from 3 cards to 5 cards
    Also, try to fix the way kickers are treated in scoring.  Extra attention to losing by kicker
"""
# todo expand points
# todo scoring based on kicker
# todo streamline with object python

import tkinter as tk
from PlayerHand import PlayerHand
from WriteGameSummary import *
from PlaySixHands20 import *
import global_variables
import sys

random_seed = 0
cumulative_score = 0
# PARAMETERS

NUMBER_OF_HANDS = 1
PRINT_HAND_FREQUENCY = 1
NUMBER_OF_CARDS = 25 #default
NUMBER_OF_WILD_CARDS = 3

running_average_points_stored = 0
running_in_range = 0
running_out_of_range = 0
running_not_applicable = 0
running_prediction_in_range = 0
running_prediction_out_of_range = 0
running_play = 0
running_no_play = 0
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

global player_names, player_wilds, player_wilds
overall_start_time = time.time()
NUMBER_OF_CARDS = 25

player_names = ["Peter ", "Johnny", "Ming  ", "Tony  ", "Edmond", "Philip"]
player_running_ante = [0,0,0,0,0,0,0]
player_running_surrender = [0,0,0,0,0,0,0]
player_running_points = [0, 0, 0, 0, 0, 0]
player_running_totals = [0, 0, 0, 0, 0, 0]
player_running_plays = [0, 0, 0, 0, 0, 0]
player_running_wilds = [0, 0, 0, 0, 0, 0]
player_running_wins = [0, 0, 0, 0, 0, 0]
k_num = 0
print (MODE)
print ("Number of arguments:", len(sys.argv))
print ("Argument List:", str(sys.argv))
simulation_deck = Deck()

top = tk.Tk()
this_hand = PokerHand()
if MODE == "Batch":
    overall_start_time = time.time()
    NUMBER_OF_CARDS = 25
    wild_count = [0, 0, 0, 0]
    hands_stored = [[],[],[],[],[],[],[]]
    points_stored = [[],[],[],[],[],[],[]]
    player_wilds = [0, 0, 0, 0, 0, 0]
    play_hand20_quality = ["", "", "", "", "", "", ""]
    player_names = ["Peter ", "Johnny", "Ming  ", "Tony  ", "Edmond", "Philip"]
    player_score_prediction = [0,0,0,0,0,0,0]
    player_totals = [0,0,0,0,0,0]
    player_hand20_signal = [0,0,0,0,0,0]
    player_score_hand20 = [0,0,0,0,0,0,0]
    player_wins = [0, 0, 0, 0, 0, 0]
    k_num = 0
    for k_num in range (NUMBER_OF_HANDS):
        six_hands = Deck.deal_6hands()[0]
        play_six_hands = PlaySixHands20(six_hands)
        sd = ShowDownGame(play_six_hands.player_points, play_six_hands.play_hand20)

        for i in range (6):
            player_running_ante[i] += sd.player_ante[i]
            player_running_surrender[i] += sd.player_surrender[i]
            player_running_points[i] += play_six_hands.player_points[i]
            player_running_wilds[i] += play_six_hands.player_wilds[i]
            player_totals[i] = sd.player_ante[i] + sd.player_surrender[i] + play_six_hands.player_points[i]
            player_running_totals[i] += player_totals[i]
            player_running_wins[i] += sd.player_wins[i]
            if play_six_hands.play_hand20[i] == True:
                player_running_plays[i] += 1

        total_points_stored = 0
        print ('Seed  Minimum  Name   Wilds   H20   Predict   Quality    Signal  Actual  Play   Points  P/Player Ante  Surr   Total  Wilds  Ante   Surr  Points  Totals   Plays  Wins  Games  Totals/Game')
        for i in range(6):
            print ('{:>6}'.format(str(global_variables.random_seed)), end="")
            print ('{:>6}'.format(str(global_variables.player_minimums[i])), end="")
            print ('{:>8}'.format(player_names[i]), end="")
            print ('{:>6}'.format(str(play_six_hands.player_wilds[i])), end="")
            print ('{:>9}'.format(str(play_six_hands.player_score_hand20[i])), end="")
            print ('{:>9}'.format(str(play_six_hands.player_score_prediction[i])), end="")
            print ('{:>9}'.format(str(play_six_hands.play_hand20_quality[i])), end="")
            print ('{:>9}'.format(str(play_six_hands.hand20_signal[i])), end="")
            print ('{:>9}'.format(str(play_six_hands.points_stored[i][0])), end="")
            print ('{:>9}'.format(str(play_six_hands.play_hand20[i])), end="")
            print ('{:>9}'.format(str(play_six_hands.player_points[i])), end="")
            points_per_player = round(play_six_hands.player_points[i]/float(sd.number_players))
            print ('{:>6}'.format(str(points_per_player)), end="")
            print ('{:>6}'.format(str(sd.player_ante[i])), end="")
            print ('{:>6}'.format(str(sd.player_surrender[i])), end="")
            print ('{:>6}'.format(str(player_totals[i])), end="")
            print ('{:>6}'.format(str(player_running_wilds[i])), end="")
            print ('{:>6}'.format(str(player_running_ante[i])), end="")
            print ('{:>6}'.format(str(player_running_surrender[i])), end="")
            print ('{:>6}'.format(str(player_running_points[i])), end="")
            print ('{:>6}'.format(str(player_running_totals[i])), end="")
            print ('{:>6}'.format(str(player_running_plays[i])), end="")
            print ('{:>6}'.format(str(player_running_wins[i])), end="")
            print ('{:>6}'.format(k_num + 1), end="")
            print ('{:>6}'.format(player_running_totals[i]/(k_num + 1)), end="")
            if play_six_hands.play_hand20[i] == True:
                running_play += 1
                if abs(points_per_player - play_six_hands.points_stored[i][0]/100) <= 5:
                    print ("      in range")
                    running_in_range += 1
                else:
                    print ("  out of range")
                    running_out_of_range += 1
            else:
                print ("           n/a")
                running_no_play += 1
            total_points_stored += play_six_hands.points_stored[i][0]
            if abs(play_six_hands.player_score_prediction[i] - play_six_hands.points_stored[i][0]) <= 500:
                running_prediction_in_range += 1
            else:
                running_prediction_out_of_range += 1

        average_points_stored = round(total_points_stored/6,1)
        print ("average points stored", average_points_stored)

        # let's run some cumulative statistics
        running_average_points_stored += total_points_stored/(6 * (k_num+1))
        print ("running average points stored", round(running_average_points_stored,2))
        running_in_range_pcnt = float(running_in_range)/(running_in_range+running_out_of_range)
        print ("running points_stored and points_per_player in range pcnt", round(running_in_range_pcnt * 100,2))
        running_prediction_in_range_pcnt = float(running_prediction_in_range)/(running_prediction_out_of_range + running_prediction_in_range)
        print ("running prediction and points_stored in range pcnt", round(running_prediction_in_range_pcnt * 100,2))
        running_play_pcnt = float(running_play)/(running_no_play + running_play)
        print ("running play pcnt", round(running_play_pcnt * 100,2))
        game_string = ""
        for i in range(6):
            game_string = str(random_seed) + ', ' + str(global_variables.player_minimums[i]) + ', '
            game_string += (player_names[i]) + ', ' + str(play_six_hands.player_wilds[i]) + ', '
            game_string += '{:>6}'.format(str(play_six_hands.player_score_hand20[i])) + ', '
            game_string += '{:>6}'.format(str(play_six_hands.player_score_prediction[i])) + ', '
            game_string += '{:>6}'.format(str(play_six_hands.points_stored[i][0])) + ', '
            game_string += '{:>6}'.format(str(play_six_hands.play_hand20_quality[i])) + ', '
            game_string += '{:>6}'.format(str(play_six_hands.play_hand20[i])) + ', '
            game_string += '{:>6}'.format(str(play_six_hands.player_points[i])) + ', '
            game_string += '{:>6}'.format(str(sd.player_ante[i])) + ', '
            game_string += '{:>7}'.format(str(sd.player_surrender[i])) + ', '
            game_string += '{:>7}'.format(str(player_totals[i])) + ', '
            game_string += '{:>7}'.format(str(player_running_wilds[i])) + ', '
            game_string += '{:>7}'.format(str(player_running_ante[i])) + ', '
            game_string += '{:>7}'.format(str(player_running_surrender[i])) + ', '
            game_string += '{:>7}'.format(str(player_running_points[i])) + ', '
            game_string += '{:>7}'.format(str(player_running_totals[i])) + ', '
            game_string += '{:>6}'.format(str(player_running_plays[i])) + ', '
            game_string += '{:>6}'.format(str(player_running_wins[i])) + ', ' + '{:>6}'.format(str(k_num + 1)) + ', '
            for j in range(1, 7):
                hand_description_string = my_hand.get_description_from_score(play_six_hands.points_stored[i][j][0], str(i))
                game_string += '{:}'.format(hand_description_string)
            game_string += '\n'
            # game_string += '{:>30}'.format(str(play_six_hands.points_stored[i])) + "\n"
            # print game_string
            x = WriteGameSummary(game_string)

    overall_end_time = time.time()
    lapse_time = round(overall_end_time - overall_start_time, 2)
    print ("finished", lapse_time, round(lapse_time/NUMBER_OF_HANDS, 2))

def display_score(score_array, x, y):
    """
    given score_array displays 6 scores and total points at x,y coordinates
    :param score_array: score0, score1, score2, score2, score3, score4, score5, score6
    :param x: x coordinate of where to display_cardlist points
    :param y: y coordinate of where to display_cardlist points
    """
    score = score_array
    field_length = 25
    string_length = len(str(score[0]))
    fill = field_length - string_length
    total_score_label = tk.Label(text="total    =  " + str(score[0]) + fill*" ", fg="blue", bg="white", font=12)
    total_score_label.place(x=x, y=y)
    string_length = len(str(score[6]))
    fill = field_length - string_length
    hand6_score_label = tk.Label(text="hand6 = " + str(score[6]) + fill*" ", fg="blue", bg="white", font=12)
    hand6_score_label.place(x=x, y=y + 25)
    string_length = len(str(score[5]))
    fill = field_length - string_length
    hand5_score_label = tk.Label(text="hand5 = " + str(score[5]) + fill*" ", fg="blue", bg="white", font=12)
    hand5_score_label.place(x=x, y=y + 50)
    string_length = len(str(score[4]))
    fill = field_length - string_length
    hand4_score_label = tk.Label(text="hand4 = " + str(score[4]) + fill*" ", fg="blue", bg="white", font=12)
    hand4_score_label.place(x=x, y=y + 75)
    string_length = len(str(score[3]))
    fill = field_length - string_length
    hand3_score_label = tk.Label(text="hand3 = " + str(score[3]) + fill*" ", fg="blue", bg="white", font=12)
    hand3_score_label.place(x=x, y=y + 100)
    string_length = len(str(score[2]))
    fill = field_length - string_length
    hand2_score_label = tk.Label(text="hand2 = " + str(score[2]) + fill*" ", fg="blue", bg="white", font=12)
    hand2_score_label.place(x=x, y=y + 125)
    string_length = len(str(score[1]))
    fill = field_length - string_length
    hand1_score_label = tk.Label(text="hand1 = " + str(score[1]) + fill*" ", fg="blue", bg="white", font=12)
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
        logging.info((card, w.coords(card)[0], card_placex, card_placey))
        # print (card, card_placex, card_placey)
        if card_placey <  229 + 220 and card_placex <= 1200:
            candidate_25card_hand.append(card)

    card_list2 = sorted(candidate_25card_hand, key=suit_rank_sort, reverse=True)
    twentyfive_cards = card_list2
    card_list2_string = ", ".join(card_list2)
    logging.info(card_list2_string)

    start_time = time.time()
    best_wild_card1, best_wild_card2, best_wild_card3, best_card_list1, best_hand_score, best_25handx = best25_with_3wild(card_list2)

    score6, score5, score4, score3, score2, score1, score7 = best_hand_score[0], best_hand_score[1], best_hand_score[2], \
                                    best_hand_score[3], best_hand_score[4], best_hand_score[5], best_hand_score[6]
    end_time = time.time()
    lapse_time = end_time - start_time
    score7 = round(score7,4)

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
    first_time_images= True
    if first_time_images == True:
        all_cards_list = Deck().deal_3deck(1)[0]
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
        w.create_image(x, y, image=image_dict[card], anchor="NW", tags=("token", card))
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
        print (card, x, Y_OFFSET, image_dict[card])
        w.create_image(x, Y_OFFSET, image=image_dict[card], anchor=NW, tags=("token", card))
        item_id = w.create_image(x, Y_OFFSET)
        w.create_text(x, Y_OFFSET, text=str(item_id))
        x += CARD_GAP
        if x > 1000:
             x = 20
             Y_OFFSET += 110

def show_next_hand(*args):
    """ Create the card list use Deck().deal and display_cardlist them"""
    global twentyfive_cards
    global six_hands
    show_best25_hand_button["state"] = "normal"
    show_next_hand_button["state"] = "disabled"
    NUMBER_OF_CARDS = 25
    six_hands = Deck.deal_6hands()[0]
    a = six_hands[0]
    image_dir = "Cards_gif/"
    image_dict = create_images()
    twentyfive_cards = []
    twentyfive_cards = (sorted(a, key=rank_sort, reverse=True))
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
    valid_hand_label = tk.Label(text=message, fg="blue", bg="pink")
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

def show_deck_of_cards(*args):
    """show full deck of cards that can be moved to playing area"""
    X_OFFSET = 20-8
    Y_OFFSET = 150-24+220
    w.delete("all")
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
    """ Given twenty_five cards, find the best hand and show scoring
    """
    global message_left_click_label

    # disable show_best_hand_button
    show_best25_hand_button["state"] = "disabled"
    # enable finished_setup_button
    show_next_hand_button["state"] = "normal"

    player_score = show_player_score()
    player_total_score = player_score[0]

    message_left_click_label = tk.Label(text="TBD")

    # make sure there are cards in twentyfive_cards
    if twentyfive_cards == []:
        message_left_click_label = tk.Label(text="Click button - Show Next Hand")
        message_left_click_label.pack()
        return
    message_left_click_label.pack_forget()

    card_list2 = twentyfive_cards
    card_list2_string = ", ".join(card_list2)

    start_time = time.time()
    temp_card_list2 = list(card_list2)
    myhand = BestHand25Wild(temp_card_list2)
    score = myhand.best_hand_points
    best_25handx = myhand.best_25handx

    # print points
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

        # display_cardlist points diff next to player scores, y is the same, x is 200 less
        x = x - 220
        score_diff = [0,0,0,0,0,0,0]
        for i in range (1,7):
            score_diff[i] = round(player_score[i][1] - score [i][1], 3)
        score_diff[0] = round (player_score[0] - score[0],3)

        display_score(score_diff, x, y)

        # keeping points of wins, losses and ties
        global wins
        global ties
        global losses
        global cumulative_points
        global cumulative_score

        if player_total_score > score[0]:
             wins += 1
             print ("Player Wins - ", end="")
        elif score[0] > player_total_score:
             losses +=1
             print ("Player Loses - ", end="")
        elif score[0] == player_total_score:
             ties +=1
             print ("Player Ties - ", end="")

        cumulative_score += player_total_adv
        cumulative_score = round(cumulative_score,2)
        player_total_adv = round(player_total_adv,2)
        print ("Player", player_total_score, "Computer", score[0], "Difference", player_total_adv, "Cumulative", cumulative_score)

        wins_label = tk.Label(text="wins = " + str(wins) + 5 * " ", fg="blue", bg="white")
        wins_label.place(x=1080-500, y=700)
        losses_label = tk.Label(text="losses = " + str(losses) + 5 * " ", fg="blue", bg="white")
        losses_label.place(x=1080-500, y=725)
        ties_label = tk.Label(text="ties = " + str(ties)+ 5 * " ", fg="blue", bg="white")
        ties_label.place(x=1080-500, y=750)
        cum_label = tk.Label(text="cum = " + str(cumulative_score) + 12 * " ", fg="blue", bg="white")
        cum_label.place(x=1080-500, y=775)

def show_player_score():
    """ First, it determines how player set his hand based on position of cards in twentyfive_cards"""
    # print "entering display_player_points"
    players_25card_hand = 25*[-1]

    # make sure every card is use
    player_hand = [[],[],[],[],[],[],[]]

    for card in twentyfive_cards:
         # X_GAP = 80
         card_placex = int((w.coords(card)[0] + X_OFFSET)/X_GAP)  # determines x coordinate of card
         card_placey = int((w.coords(card)[1])) # determines y coordinate of card
         # logging.info((card, w.coords(card)[0], card_placex, card_placey))
         # print card, card_placex, card_placey
         if card_placey >= 229 and card_placex <= 850:
             hand_diff = [-2,3,7,10,13,15]   # hand_diff[0] = -2 which is hand6
             hand_number = card_placey//100 - 2 # hand6 = 0, hand5 = 1, etc
             converted_hand_number = 6 - hand_number
             card_number = card_placex + hand_diff[hand_number]
             # print card_number
             players_25card_hand[card_number] = str(card)
             player_hand[converted_hand_number].append(card)

    # print ("player_hand before",player_hand)
    player = PlayerHand(player_hand)
    # print ("player_hand after",player_hand)
    player_hand_score = player.player_hand_score
    # print ("display_player_points", player_hand_score)
    valid_hand = True
    for i in range (1,6):
        if player_hand_score[i+1] < player_hand_score[i]:
            valid_hand = False
            # print "hand",i+1, "is less than hand", i

    # if valid_hand is False
    if valid_hand == False:
        message = "Player Hand Invalid - Try Again"
        x_label = 11 * X_GAP  # for labels
        y_label = 310 + 150 + 110  # aligns with player hand
        x = x_label
        y = y_label + 25
        valid_hand_label = tk.Label(text=message, fg="red", bg="white")
        valid_hand_label.place(x=x - 150, y=y)
        display_score(player_hand_score, x, y + 25)
        print ("Player Hand Invalid, player_score set to -9999, restore_position")
        player_hand_score = -9999
        show_twentyfive_cards()
        return player_hand_score

    # else hand is valid
    else:
        message = "Player Hand Valid   "

        # display_cardlist differences by total and hand
    # print player_hand6,player_hand5,player_hand4,player_hand3, player_hand2, player_hand1, player_total

    x_label = 11 * X_GAP  # for labels
    y_label = 310 + 150 + 110 # aligns with player hand
    x = x_label
    y = y_label + 25
    valid_hand_label = tk.Label(text=message , fg="blue", bg="white", font=12)
    valid_hand_label.place(x=x-150, y=y)
    display_score(player_hand_score, x, y + 25)
    return player_hand_score



def text_solve_best25_hand(*args):
    """ Given  twenty_five cards, solve for the best hand and show scoring"""
    # # X_GAP = 80
    # Y_GAP = 110
    X_OFFSET = 11 + 4
    # global twentyfive_cards
    candidate_25card_hand = []
    card_list = list(Deck().deal_3deck(1))[0]
    card_list = sorted(card_list, key=rank_sort, reverse=True)
    card_list = list(card_list)
    for card in card_list:
        card_placex = int((w.coords(card)[0] + X_OFFSET) / X_GAP)  # determines x coordinate of card
        card_placey = int((w.coords(card)[1]))  # determines y coordinate of card
        # print card, card_placex, card_placey
        if card_placey <  229 + 220 and card_placex <= 1200:
            candidate_25card_hand.append(card)

    card_list2 = sorted(candidate_25card_hand, key=suit_rank_sort, reverse=True)
    # card_list2_string = ", ".join(card_list2)
    # logging.info(card_list2_string)
    # print card_list2
    start_time = time.time()
    best_hand = BestHand25Wild(card_list2)
    # best_wild_card1, best_wild_card2, best_wild_card3, best_card_list1, best_hand_score, best_25handx = BestHand25Wild(card_list2)
    best_card_list1 = best_hand.best_25handx[6] + best_hand.best_25handx[5]+ best_hand.best_25handx[4]\
                      + best_hand.best_25handx[3]+ best_hand.best_25handx[2]+ best_hand.best_25handx[1]

    score6, score5, score4, score3, score2, score1, score0 = best_hand.best_hand_score[6], best_hand.best_hand_score[5], best_hand.best_hand_score[4], \
                                    best_hand.best_hand_score[3], best_hand.best_hand_score[2], best_hand.best_hand_score[1], best_hand.best_hand_score[0]
    end_time = time.time()
    score0 = round(score0,4)

     # showing best hand
    top.title("Best Hand")
    # w.delete("all")
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

        # display_cardlist points of best hand
        x_label = 13.5 * X_GAP
        y_label = 60 # aligns with best_hand
        x = x_label
        y = y_label
        score_array = (score0, score1, score2, score3, score4, score5, score6)
        display_score(score_array, x, y)

        # display_cardlist differences




def switch2():
    if show_best25_hand_button["state"] == "normal":
        show_best25_hand_button["state"] = "disabled"
        disable_show_best["text"] = "Toggle"
    else:
        show_best25_hand_button["state"] = "normal"
        disable_show_best["text"] = "Toggle"

def switch3():
    if show_next_hand_button["state"] == "normal":
        show_next_hand_button["state"] = "disabled"
        disable_show_next["text"] = "Toggle"
    else:
        show_next_hand_button["state"] = "normal"
        disable_show_next["text"] = "Toggle"

if MODE == "Solve" or MODE == "Text":
    XGAP = 80
    w = Canvas(top, height=950, width=13.5 * XGAP, background="pink", relief="raised")
    m_box = Tk()
    X_OFFSET = 11
    wins = 0
    losses = 0
    ties = 0
    cumulative_points = 0
    image_dir = "Cards_gif/"
    image_dict = create_images()

    next_setup_button = tk.Button(top, text="Next User Input", command=show_deck_of_cards)
    show_twentyfive_cards_button = tk.Button(top, text="Buy Cards", command=show_twentyfive_cards)
    text_solve_best25_hand_button = tk.Button(top, text="Solve - User Input", command=text_solve_best25_hand)

    show_player_score_button = tk.Button(top, text="Player Hand Score", command=show_player_score)
    suit_button = tk.Button(top, text="Suit", command=suit_quick_sort)
    rank_button = tk.Button(top, text="Rank", command=rank_quick_sort)

    next_setup_button.pack()
    text_solve_best25_hand_button.pack()
    show_player_score_button.pack(side=RIGHT)
    show_twentyfive_cards_button.pack(side=RIGHT)
    suit_button.pack(side=RIGHT)
    rank_button.pack(side=RIGHT)
    w.pack()

    w.tag_bind("token", "<tk.Button-1>", onClick)
    w.tag_bind("token", "<B1-Motion>", onMotion)
    w.tag_bind("token", "<tk.ButtonRelease-1>", onRelease)
    if MODE == "Text":
        input_string = input("Enter 25 Cards: ")
        card_listx = input_string.split(",")
        card_list = sorted(card_listx, key=rank_sort, reverse=True)
        print (card_list)
        show_card_list()
    else:
        show_deck_of_cards()

if MODE == "Interactive":
    k_num = 1
    XGAP = 80
    save_position1 = 25 * [[]]
    w = tk.Canvas(top, height=900, width=13.5 * XGAP, background="pink", relief="raised")
    m_box = tk.Tk()
    X_OFFSET = 11
    wins = 0
    losses = 0
    ties = 0
    cumulative_points = 0
    image_dir = "Cards_gif/"
    image_dict = create_images()
    twentyfive_cards = []

    # finished_setup_button, toggle_show_next_hand to enable/disable
    show_next_hand_button = tk.Button(top, text="Show Next Hand", font=12, command=show_next_hand)
    show_next_hand_button.place(x=1080-250,y=225, width=130, height=24)
    disable_show_next = tk.Button(top, text="Toggle", font=12, command=switch3)
    disable_show_next.place(x=1080-120+10,y=225, width=100, height=24)

    # show_best_hand_button, toggle_show_best to enable/disable
    show_best25_hand_button = tk.Button(top, text="Show Best Hand", font=12, command=show_best25_hand)
    show_best25_hand_button.place(x=1080-250,y=250,width=130, height=24)
    disable_show_best = tk.Button(top, text="Toggle", font=12, command=switch2)
    disable_show_best.place(x=1080-120+10,y=250, width=100, height=24)

    print ("show next hand button state", show_next_hand_button["state"])
    show_next_hand()

    # showdown_hand_button = tk.Button(top, text="ShowDownGame", command=show_ShowDown).place(x=1080-200,y=275,width=140, height=24)
    show_player_score_button = tk.Button(top, text="Player Score", font=12, command=show_player_score).place(x=1080-200, y=525-40, width=140, height=24)
    suit_button = tk.Button(top, text="Suit", font=12, command=suit_quick_sort).place(x=1080-200, y=550-40, width=140, height=24)
    rank_button = tk.Button(top, text="Rank", font=12, command=rank_quick_sort).place(x=1080-200, y=575-40, width=140, height=24)
    save_button = tk.Button(top, text="Save", font=12, command=save_position).place(x=1080-200, y=600-40, width=140, height=24)
    restore_button = tk.Button(top, text="Restore", font=12, command=restore_position).place(x=1080-200, y=625-40, width=140, height=24)

    w.pack()

    w.tag_bind("token", "<Button-1>", onClick)
    w.tag_bind("token", "<B1-Motion>", onMotion)
    w.tag_bind("token", "<ButtonRelease-1>", onRelease)

top.mainloop()