import tkinter as tk
from Deck import *
from sort_cards import *
import tkinter.ttk as ttk

def create_images():
    """create all card images as a card_name:image_object dictionary"""
    global first_time_images, image_dict
    image_dir = "Cards_gif/"
    first_time_images= True
    if first_time_images == True:
        all_cards_list = Deck().deal_3deck(1)[0]
        image_dict = {}
        for card in all_cards_list:
            # all images have filenames the myhand20_analysis the card_list names + extension .gif
            card_only = card[0:2]
            image_dict[card] = tk.PhotoImage(file=image_dir+card_only+".gif")
            print ("create_images", card, image_dir + card_only+ ".gif")
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

    Y_OFFSET = 9
    X_OFFSET = 0
    mx = (event.x - .5 * X_GAP) // X_GAP * X_GAP + 1 + X_OFFSET
    my = (event.y) // Y_GAP * Y_GAP + 20

    if my < 0: my = 0
    if my > 6 * Y_GAP: my = 6 * Y_GAP + Y_OFFSET
    if mx < 0: mx = 0
    if mx > 15 * X_GAP: mx = 15 * X_GAP

    current_card_x = w.coords("current")[0]
    current_card_y = w.coords("current")[1]

    print ("before current_card x,y", current_card_x, current_card_y)
    print ("converted", (current_card_x-6)/X_GAP + 1, (current_card_y-Y_OFFSET)/Y_GAP + 1)
    delta_x = mx - current_card_x + 5
    delta_y = my - current_card_y - 11

    w.move("current", delta_x, delta_y)  # this just snaps into place based on rectangle
    current_card_x = w.coords("current")[0]
    current_card_y = w.coords("current")[1]

    print ("after current_card x,y", current_card_x, current_card_y)
    print ("converted", (current_card_x-6)/X_GAP + 1, (current_card_y-Y_OFFSET)/Y_GAP + 1)

    x1 = current_card_x +10
    y1 = current_card_y +10
    x2 = current_card_x + X_GAP -10
    y2 = current_card_y + Y_GAP -10

    # look for "overlappers" to current card slot
    overlappers = w.find_overlapping(x1, y1, x2, y2)
    print ("overlappers", overlappers)
    if len(overlappers) > 0:
        overlap_cards = []
        current_card = []
        # if tagged as "card" append, then remove tagged as "current"
        for object in overlappers:
            for tag in w.gettags(object):
                if tag == "card":
                    overlap_cards.append(object)
                if tag == "current":
                    current_card = object
        overlap_cards.remove(current_card)
        print ("overlap cards", overlap_cards)

        # if overlap - moving card to right by 33%
        if overlap_cards != []:
            w.move("current", + X_GAP/5, 0)

    # count number of cards left
    cards_left = list(w.find_withtag("card"))
    list_of_cards_left = list(cards_left)
    for object_id in list_of_cards_left:
        # remove those with x > 5 and y < 1
        if w.coords(object_id)[0] > 5 * X_GAP - 10 or \
            w.coords(object_id)[1] < 0 * Y_GAP:
            cards_left.remove(object_id)

    fixed_destination = [0*X_GAP + 9, 6 * Y_GAP+19], [1*X_GAP + 9, 6 * Y_GAP+19], \
                        [2*X_GAP + 9, 6 * Y_GAP+19], [3*X_GAP + 9, 6 * Y_GAP+19], [4*X_GAP + 9, 6 * Y_GAP+19]
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

def show_next_hand(*args):
    """ Create the card list use Deck().deal and display_cardlist them"""
    global twentyfive_cards
    # disable show_next and enable show_best
    # show_best25_hand_button["state"] = "normal"
    # show_next_hand_button["state"] = "disabled"
    six_hands = Deck.deal_6hands()[0]
    a = six_hands[0]
    twentyfive_cards = (sorted(a, key=rank_sort, reverse=True))
    window.title("Play Pyramid Poker")
    w.delete("all")   # clear out last hand
    show_twentyfive_cards()

def show_twentyfive_cards():
    w.delete("card")
    x = 0
    y = 12
    # conserve space - put cards 5 x 5 matrix
    for card in twentyfive_cards:
        print (card, image_dict[card])
        w.create_image(x + 4, y - 4, image=image_dict[card], anchor="nw", tags=("card", card))
        x += X_GAP
        if x > 4 * X_GAP:
            y += Y_GAP
            x = 0

window = tk.Tk()
Y_GAP = 95
X_GAP = 50

topFrame = tk.Frame(window)
topFrame.pack()
create_images()
w = tk.Canvas(topFrame, height=7*Y_GAP, width= 10*X_GAP, bg="light blue")
# display_next_hand()

w.pack()
w.tag_bind("card", "<Button-1>", onClick)
w.tag_bind("card", "<B1-Motion>", onMotion)
w.tag_bind("card", "<ButtonRelease-1>", onRelease)
window.mainloop()
