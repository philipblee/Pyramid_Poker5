"""python_client sets up client_socket
v1 then uses method connect to establish connection
then uses client_socket to receive Welcome message
then uses client_socket to receive hand_pickle
then unpickles hand using pickle.load and prints
v2 no change on client
v3 added a GUI to show cards in text
v4 show cards in images
v5 make cards movable
"""
import socket
import pickle
import tkinter as tk
from Deck import *
from display_points import rank_sort, create_images
# from PyramidPokerNetwork import onMotion, onRelease, onClick
window = tk.Tk()
# window.geometry(300, 500)

window.title("Client")

# username = " "

topFrame = tk.Frame(window)
# lblName = tk.Label(topFrame, text = "Name:").pack(side=tk.LEFT)
entName = tk.Entry(topFrame)
# entName.pack(side=tk.LEFT)
# btnConnect = tk.Button(topFrame, text="Connect", command=lambda : connect())
# btnConnect.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP)

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
    which_hand = [[0,8], [100,7],[200,6], [300,5], [400,4], [500,3], [600,2], [700,1]]
    # current_card_place = []
    # current_card_hand = []
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
    y2 = current_card_y + 100
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


    fixed_destination = [657,118], [737,118], [817,118], [897,118], [977,118]
    start_destination = 5 - len(cards_left)
    destination = fixed_destination[start_destination:]

    index = 0
    # print "number of cards left", len(cards_left)

    if len(cards_left) <= 5:
        for object_id in cards_left:

            x_coord = w.coords(object_id)[0]
            y_coord = w.coords(object_id)[1]
            delta_x = destination[index][0] - x_coord
            delta_y = destination[index][1] - y_coord - 10
            w.move(object_id, delta_x, delta_y)
            index += 1
    return


def connect():
    pass

def show_board(*args):
    """ Create the card list use Deck().deal and display_cardlist them"""

    global twentyfive_cards
    window.title("Play Pyramid Poker")
    w.delete("all")   # clear out last hand
    # create white rectangles
    Y_OFFSET = 60 + 60 + 102 - 18 # add 60 to account for buttons on top
    X_OFFSET = 11 - 6 + 6 # where cards and rectangles begin
    tag_number = 1

    # create 13 rectangles for first 13 cards
    x = X_OFFSET
    y = Y_OFFSET - 200
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
    y = Y_OFFSET - 100
    for i in range(13):
        if i>=8:
            fill_color = "light gray"
        else:
            fill_color = "pink"
        item_id = w.create_rectangle(x, y, x + X_GAP, y + Y_GAP, fill=fill_color, tag="twentyfive-two")
        x += X_GAP
        tag_number += 1

    # create 10 rectangles - hand 6
    Y_OFFSET = 60 + 60 + 110 - 8 - 2 # add 60 to account for buttons on top
    x = X_OFFSET
    y = Y_OFFSET - 12
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

MODE = "Interactive"

if MODE == "Interactive":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 55555))

    message = client_socket.recv(4096)
    print (message.decode("utf-8"))

    hand_pickle = client_socket.recv(4096)
    client_hand = pickle.loads(hand_pickle)
    print (client_hand)

    image_dir = "../Cards_gif/"
    image_dict = create_images()

    w = tk.Canvas(window, height=810, width= 13.2 * 80, background="pink", relief="raised")
    twentyfive_cards = list(client_hand)
    twentyfive_cards = sorted(twentyfive_cards, key=rank_sort, reverse=True)

    X_GAP = 80
    Y_GAP = 100
    X_OFFSET = 2
    Y_OFFSET = 10
    y = Y_OFFSET
    x = X_OFFSET + 9   # adds 5 to move card to center of white rectangle

    show_board()
    for card in twentyfive_cards:
        item_id = w.create_image(x + 4, y - 4, image=image_dict[card], anchor="nw", tags=("token", card))
        # print card, item_id
        x += X_GAP
        if x > 13 * X_GAP:
             x = X_OFFSET + 9
             y += Y_GAP

    w.pack()

    w.tag_bind("token", "<Button-1>", onClick)
    w.tag_bind("token", "<B1-Motion>", onMotion)
    w.tag_bind("token", "<ButtonRelease-1>", onRelease)

window.mainloop()