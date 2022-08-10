""" RunPyramidPoker runs Batch or Interactive

"""
from src.core.BestHand25Wild import *
from src.core.WriteFile import *
from src.core.PokerHand import *
from src.core.PlayerHand import PlayerHand
from src.core.CumulativeLearning import *
from src.core.WriteKeyValues import *
import src.core.global_variables as global_variables

import time
import datetime
import tkinter as tk
import sys
import json
import statistics
import logging

cumulative_score = 0
# PARAMETERS
NUMBER_OF_HANDS = 10
PRINT_HAND_FREQUENCY = 1
NUMBER_OF_CARDS = 25
NUMBER_OF_WILD_CARDS = 3

# my_hand = PokerHand()

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

top = tk.Tk()

Y_GAP = 110
X_GAP = 80
X_OFFSET = 11

if MODE == "Batch":
    overall_start_time = time.time()
    NUMBER_OF_CARDS = 25
    wild_count = [0, 0, 0, 0]

    for k in range (NUMBER_OF_HANDS):
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

        # Use Best25Wild class to get best_hand_score and best_25handx
        myhand = BestHand25Wild(card_list2)
        best_hand_points = myhand.best_hand_points
        # print (points)
        best_card_list1 = json.dumps(myhand.best_25handx[1:7])
        print (myhand.best_25handx[6:0:-1])
        print (myhand.best_hand_points[6:0:-1], myhand.best_hand_points[0])
        key_values = [()]

        for hand_x in myhand.best_25handx[1:7:1]:
            pokerhand = PokerHand(hand_x)
            key_values.append(tuple(pokerhand.hand_key_values))
        # print (key_values)

        end_time = time.time()
        lapse_time = round(end_time - start_time, 2)
        print ("--Total time for hand = ", lapse_time)
        elapse_time[wild_cards].append(lapse_time)
        w0 = w1 = w2 = w3 = ""
        if wild_cards == 0:  w0 = str(best_hand_points[0])
        elif wild_cards == 1:  w1 = str(best_hand_points[0])
        elif wild_cards == 2:  w2 = str(best_hand_points[0])
        elif wild_cards == 3:  w3 = str(best_hand_points[0])

        # cumulative_learning_string1
        cumulative_learning_string = str(best_hand_points[6][0]) + ", " + str(best_hand_points[6][1]) + ", "
        cumulative_learning_string += str(best_hand_points[5][0]) + ", " + str(best_hand_points[5][1]) + ", "
        cumulative_learning_string += str(best_hand_points[4][0]) + ", " + str(best_hand_points[4][1]) + ", "
        cumulative_learning_string += str(best_hand_points[3][0]) + ", " + str(best_hand_points[3][1]) + ", "
        cumulative_learning_string += str(best_hand_points[2][0]) + ", " + str(best_hand_points[2][1]) + ", "
        cumulative_learning_string += str(best_hand_points[1][0]) + ", " + str(best_hand_points[1][1]) + ", "
        cumulative_learning_string += str(best_hand_points[0])
        temporary_string = cumulative_learning_string
        cumulative_learning_string += "," + str(wild_cards) + ", " + w0 + ", " + w1 + ", " + w2 + ", " + w3
        cumulative_learning_string1 = cumulative_learning_string +  "\n"

        OUTPUT = "output." + str(global_variables.random_seed) + "-" + str(global_variables.file_num)
        output_string = "\n" + str(k+1) + ", " + str(wild_cards) + ", " + str(best_hand_points[0]) + ", " + str(lapse_time)

        if os.path.exists(OUTPUT):
            with open(OUTPUT, "a") as g:
                g.write(output_string)
                # print (cumulative_learning_string1)
        else:
            with open(OUTPUT, "w") as g:
                g.write(output_string)

        if os.path.exists(CUMULATIVE_LEARNING):
            with open(CUMULATIVE_LEARNING, "a") as g:
                g.write(cumulative_learning_string1)
                # print (cumulative_learning_string1)
        else:
            with open(CUMULATIVE_LEARNING, "w") as g:
                g.write(cumulative_learning_string1)

        # cumulative_learning_string2 is written to KeyValues.csv
        cumulative_learning_string2 = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")) +  ", "
        cumulative_learning_string2 += str(wild_cards) +  ", "
        cumulative_learning_string2 += str(temporary_string)  +  ", "
        cumulative_learning_string2 += str(lapse_time) +  ","
        # add count here
        cumulative_learning_string2 += str(card_list2) + ","
        cumulative_learning_string2 += str(best_card_list1) + "\n"
        WriteFile(cumulative_learning_string2)
        # print(cumulative_learning_string2)
        keyvalue_string = ""
        keyvalue_string = str(key_values[1]) + " / "
        keyvalue_string += str(key_values[2]) + " / "
        keyvalue_string += str(key_values[3]) + " / "
        keyvalue_string += str(key_values[4]) + " / "
        keyvalue_string += str(key_values[5]) + " / "
        keyvalue_string += str(key_values[6]) + "\n"
        WriteKeyValues(keyvalue_string)

    overall_end_time = time.time()
    lapse_time = round(overall_end_time - overall_start_time, 2)
    print ("finished", lapse_time, round(lapse_time/NUMBER_OF_HANDS, 2))

    for i in range(4):
        if len(elapse_time[i]) > 0:
            print ("number of wild cards", i, len(elapse_time[i]), round(statistics.mean(elapse_time[i]),2))

    #stop program
    top.destroy()

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
        logging.info((card, w.coords(card)[0], card_placex, card_placey))
        # print card, card_placex, card_placey
        if card_placey <  229 + 220 and card_placex <= 1200:
            candidate_25card_hand.append(card)

    card_list2 = sorted(candidate_25card_hand, key=suit_rank_sort, reverse=True)
    twentyfive_cards = card_list2
    card_list2_string = ", ".join(card_list2)
    logging.info(card_list2_string)

    start_time = time.time()
    myhand = BestHand25Wild(card_list2)
    # best_wild_card1 = myhand.best_wild_card[0]
    # best_wild_card2 = myhand.best_wild_card[1]
    # best_wild_card3 = myhand.best_wild_card[2]
    best_card_list1 = myhand.card_list2
    best_hand_points = myhand.best_hand_points
    best_25handx = myhand.best_25handx

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
    all_cards_list = [s + r for s in suit for r in rank for d in deck_number]
    for i in range(1):
        all_cards_list.extend(["WW", "WW", "WW"])
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
    twentyfive_cards.sort(key=suit_rank_sort, reverse=True)
    show_twentyfive_cards()

def rank_quick_sort():
    """ sorting by rank and display_cardlist"""
    twentyfive_cards.sort(key=rank_sort, reverse=True)
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
    # a[0] = ['SA+', 'HK+', 'HK-', 'DQ+', 'CQ+', 'DJ+', 'CJ+', 'CJ-', 'ST+', 'DT+', 'DT-', 'CT+', 'S9+', 'H9+', 'H9-', 'C9+',
    #  'S8+', 'H7+', 'D7+', 'C7+', 'C7-', 'S5+', 'C3+', 'C3-', 'H2+']
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
        item_id = w.create_image(x, y, image=image_dict[card[0:2]], anchor="nw", tags=("token", card))
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
        w.create_image(x/3, Y_OFFSET, image=image_dict[card], anchor=tk.NW, tags=("token", card))
        x += CARD_GAP
        if x > 3060:
             x = 20
             Y_OFFSET += 90

def show_best25_hand(*args):
    """ Given  twenty_five cards, find the best hand and show scoring"""

    global message_left_click_label

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
            w.create_image(x, y, image=image_dict[card[0:2]], anchor="nw", tag="best")
            x += X_GAP
        y += Y_GAP #row 2
        x = X_OFFSET + 5

        for card in best_card_list1[13:25]:  # last 7-12 cards
           # print (card, x, y, image_dict[card])
            w.create_image(x, y, image=image_dict[card[0:2]], anchor="nw", tag="best")
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
        global cumulative_points

        if player_total_score > score[0]:
            message = "You Win"
            wins += 1
        elif score[0] > player_total_score:
            message = "You Lose"
            losses +=1
        elif score[0] == player_total_score:
            message = "It's a Tie"
            ties +=1
        cumulative_points += player_total_adv
        cumulative_points = round(cumulative_points,2)

        # show wins, losses, ties and cumulative points
        wins_label = tk.Label(text="wins = " + str(wins) + 5 * " ", fg="blue", bg="white")
        wins_label.place(x=1080-500, y=700)
        losses_label = tk.Label(text="losses = " + str(losses) + 5 * " ", fg="blue", bg="white")
        losses_label.place(x=1080-500, y=725)
        ties_label = tk.Label(text="ties = " + str(ties)+ 5 * " ", fg="blue", bg="white")
        ties_label.place(x=1080-500, y=750)
        cum_label = tk.Label(text="cum = " + str(cumulative_points) + 12 * " ", fg="blue", bg="white")
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
             print (card, card_placex, card_placey, real_hand_number)
    player = PlayerHand(player_hand)
    player_hand_points = player.player_hand_score

    for hand in player_hand:
        hand = sorted(hand, key=rank_sort, reverse=True)
        print (hand)

    player_points_total = player_hand_points[0]
    print ("Player point", player_points_total)

    valid_hand = True
    for i in range (1,6):
        if player_hand_points[i+1] < player_hand_points[i]:
            valid_hand = False
            # print "hand",i+1, "is less than hand", i


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
        logging.info((card, w.coords(card)[0], card_placex, card_placey))
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
    cumulative_points = 0
    image_dir = "Cards_gif/"
    image_dict = create_images()

    next_setup_button = tk.Button(top, text="Next Setup", command=show_next_hand)
    show_twentyfive_cards_button = tk.Button(top, text="Buy Cards", command=show_twentyfive_cards)
    text_solve_best25_hand_button = tk.Button(top, text="Solve - User Input", command=text_solve_best25_hand)

    show_player_score_button = tk.Button(top, text="Player Hand Score", command=show_player_score)
    suit_button = tk.Button(top, text="Suit", command=suit_quick_sort)
    rank_button = tk.Button(top, text="Rank", command=rank_quick_sort)

    next_setup_button.pack()
    text_solve_best25_hand_button.pack()
    show_player_score_button.pack(side=tk.RIGHT)
    show_twentyfive_cards_button.pack(side=tk.RIGHT)
    suit_button.pack(side=tk.RIGHT)
    rank_button.pack(side=tk.RIGHT)
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
    # for interactive display

    Y_GAP = 110
    XGAP = 80
    X_OFFSET = 11
    save_position1 = 25 * [[]]
    w = tk.Canvas(top, height=900, width=13.5 * XGAP, background="pink", relief="raised")
    m_box = tk.Tk()

    wins = 0
    losses = 0
    ties = 0
    cumulative_points = 0
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