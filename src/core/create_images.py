import tkinter as tk
from deck_of_cards import *

def create_images():
    """create all card images as a dictionary card_name:image_object"""
    image_dir = "Cards_gif/"
    image_dict = {}
    for card in list(deck_of_cards):
        # all images have filenames the myhand20_analysis the card_list names + extension .gif
        card_only = card[0:2]
        image_dict[card] = tk.PhotoImage(file=image_dir+card_only+".gif")
        # print (card, image_dict[card])
    image_dict["Deck3"] = tk.PhotoImage(file=image_dir+"Deck3"+".gif")
    return image_dict


