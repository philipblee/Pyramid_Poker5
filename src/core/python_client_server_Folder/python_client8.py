"""python_client sets up client_socket
v1 then uses method connect to establish connection
then uses client_socket to receive Welcome message
then uses client_socket to receive hand_pickle
then unpickles hand using pickle.load and prints
v2 no change on client
v3 added a GUI to show cards in text
v4 show cards in images
v5 make cards movable
v6 put two buttons on board - one for I'm finished and one for Toggle which is initially disabled, also
   moved playing cards to lower right hand corner, now board is much smaller instead of 13x8, it's now 10x6
v7 improved GUI considerably
v8 simplifying on X_OFFSET, Y_OFFSET and other miscellaneous statements
"""
import socket
import pickle
import tkinter as tk
from Deck import *
from display_points import rank_sort, create_images
# from PyramidPokerNetwork import onMotion, onRelease, onClick
window = tk.Tk()
window.title("Client")

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

    X_OFFSET = 0
    mx = (event.x - .5 * X_GAP) // X_GAP * X_GAP + 1 + X_OFFSET
    my = event.y // Y_GAP * Y_GAP + 20

    if my < 0: my = 0
    if my > 6 * Y_GAP: my = 6 * Y_GAP
    if mx < 0: mx = 0
    if mx > 12 * X_GAP: mx = 12 * X_GAP

    current_card_x = w.coords("current")[0]
    current_card_y = w.coords("current")[1]

    delta_x = mx - current_card_x + 5
    delta_y = my - current_card_y - 11

    w.move("current", delta_x, delta_y)  # this just snaps into place based on rectangle
    current_card_x = w.coords("current")[0]
    current_card_y = w.coords("current")[1]

    x1 = current_card_x
    y1 = current_card_y
    x2 = current_card_x + X_GAP
    y2 = current_card_y + Y_GAP

    # look for "overlappers" to current card slot
    overlappers = w.find_overlapping(x1, y1, x2, y2)
    if len(overlappers) > 0:
        # see if overlappers are "token" and sitting on current_card_hand and current_card_place
        overlap_cards = []
        # for each tag_id, look for tag "token" to include in overlap_cards
        for object in overlappers:
            for tag in w.gettags(object):
                # restricts overlapping to same row
                if tag == "token": # and mx == tag_coordinates[0]:
                    overlap_cards.append(object)

        # for each overlap card, remove card with tag "current"
        current_card = []
        for card in overlap_cards:
            for tag in w.gettags(card):
                if tag == "current":
                    current_card = card
        overlap_cards.remove(current_card)

        # if overlap_cards is not empty, first look right for open slot, then left
        if overlap_cards != []:
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

    # count number of cards left
    cards_left = list(w.find_withtag("token"))
    list_of_cards_left = list(cards_left)
    for object_id in list_of_cards_left:
        # remove those with x > 5 and y < 2
        if w.coords(object_id)[0] > 5 * X_GAP - 10 or \
            w.coords(object_id)[1] < 1 * Y_GAP:
            cards_left.remove(object_id)

    fixed_destination = [0 + 7, 5 * Y_GAP+17], [X_GAP + 7, 5 * Y_GAP+17], \
                        [2*X_GAP + 7, 5 * Y_GAP+17], [3*X_GAP + 7, 5 * Y_GAP+17], [4*X_GAP + 7, 5 * Y_GAP+17]
    start_location = 5 - len(cards_left)   # start_location is between 0 and 4, 5 cards start at 0, 4 at 1
    destination = fixed_destination[start_location:]

    # when there are 5 or less cards left, move cards to discard area
    index = 0
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


def show_next_hand(*args):
    """ Create the card list use Deck().deal and display_cardlist them"""
    global twentyfive_cards
    window.title("Play Pyramid Poker")
    w.delete("all")   # clear out last hand
    # create white rectangles

    X_OFFSET = 5 * X_GAP

    # create 10 rectangles - hand 6
    Y_OFFSET = 60 + 60 + 86 # add 60 to account for buttons on top
    x = 2 * X_GAP
    y = Y_OFFSET - 2 * Y_GAP
    for i in range(10):
        fill_color = "light yellow"
        if i >= 3 and i <= 7:
            fill_color = "white"
        w.create_rectangle((x, y , x + X_GAP, y + Y_GAP), fill=fill_color, tag="hand6")
        x += X_GAP

    # create 7 rectangles - hand 5
    x = X_OFFSET
    y += Y_GAP
    for i in range(8):
        fill_color = "light yellow"
        if i <= 4:
            fill_color = "white"
        w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill=fill_color, tags="hand5")
        x += X_GAP

    # create 6 rectangles - hand 4
    x = X_OFFSET
    y += Y_GAP
    for i in range(6):
        fill_color = "light yellow"
        if i == 3 or i == 1 or i == 2:
            fill_color = "white"
        w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill=fill_color, tags="hand4")
        x += X_GAP

    # create 5 rectangles - hand 3
    x = X_OFFSET
    y += Y_GAP
    for i in range(5):
        fill_color = "light yellow"
        if i == 3 or i == 1 or i == 2:
            fill_color = "white"
        w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill=fill_color, tags="hand3")
        x += X_GAP

    # create 3 rectangles - hand 2
    x = X_OFFSET + X_GAP
    y += Y_GAP
    for i in range(3):
        w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill="white", tags="hand2")
        x += X_GAP

    # create 1 rectangle - hand 1
    x = X_OFFSET + 2 * X_GAP
    y += Y_GAP
    for i in range(1):
        w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill="white", tags="hand1")
        x += X_GAP
    show_twentyfive_cards()

def show_twentyfive_cards():
    x = 0
    y = 9 + Y_GAP + 3
    # conserve space - put cards 5 x 5 matrix
    for card in twentyfive_cards:
        w.create_image(x + 4, y - 4, image=image_dict[card], anchor="nw", tags=("token", card))
        x += X_GAP
        if x > 4 * X_GAP:
            y += Y_GAP
            x = 0

def toggle_finished():
    if show_best25_hand_button["state"] == "normal":
        show_best25_hand_button["state"] = "disabled"
        disable_show_best["text"] = "Toggle"
    else:
        show_best25_hand_button["state"] = "normal"
        disable_show_best["text"] = "Toggle"

def stub():
    pass

if True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 55555))

    message = client_socket.recv(4096)
    print (message.decode("utf-8"))

    hand_pickle = client_socket.recv(4096)
    client_hand = pickle.loads(hand_pickle)
    print (client_hand)

    twentyfive_cards = sorted(client_hand, key=rank_sort, reverse=True)

    image_dict = create_images()

    X_GAP = 80
    Y_GAP = 100
    X_OFFSET = 11
    Y_OFFSET = 10 + Y_GAP
    y = Y_OFFSET
    x = X_OFFSET
    w = tk.Canvas(window, height=6*Y_GAP+10, width=12*X_GAP, background="light blue", relief="raised")

    show_next_hand()

    # finished_setup_button, toggle_show_next_hand to enable/disable
    finished_setup_button = tk.Button(window, text="I'm Done!", font=12, command=stub)
    finished_setup_button.place(x=10, y=10, width=100, height=24)
    toggle_button = tk.Button(window, text="Toggle", font=12, command=toggle_finished, state='disabled')
    toggle_button.place(x=10, y=40, width=100, height=24)
    reset_button = tk.Button(window, text="Reset Hand", font=12, command=show_next_hand)
    reset_button.place(x=10, y=70, width=100, height=24)
    w.pack()

    w.tag_bind("token", "<Button-1>", onClick)
    w.tag_bind("token", "<B1-Motion>", onMotion)
    w.tag_bind("token", "<ButtonRelease-1>", onRelease)

window.mainloop()