""" Board is a class that displays cards on Canvas
    if Board.cardlist populated, it displays cards in one row
    if Board.handslist populated, it plays all six hands and
        displays them with showdown points by hand and total

"""

import tkinter as tk
import tkinter.font as font
from create_images import create_images
from PlaySixHands25 import *
from display_points import *
from Deck2 import Deck2  # Board uses Deck2

class Board():
    def __init__(self):
        print ("running class Board init")
        self.Y_GAP = 95
        self.X_GAP = 72
        self.CANVAS_H = 7 * self.Y_GAP
        self.CANVAS_W = 10 * self.X_GAP
        self.X_OFFSET = 10
        self.Y_OFFSET = 10
        self.pyramid_hands = []

    def display_cardlist(self):
        print ("running display_cardlist")

        window1 = tk.Tk()
        window_label = tk.Label(window1, text = "window1")
        window_label.place(x = 25, y = 25)
        window_label.pack()
        hand_separation = 1.04
        X_GAP_factor = 1
        self.CANVAS_W = 10 * self.X_GAP * X_GAP_factor * hand_separation + 25
        self.X_GAP = 72 * X_GAP_factor
        self.CANVAS_H = 8.2 * self.Y_GAP + 25
        self.Y_OFFSET = 2.2 * self.Y_GAP
        image_dict = create_images()
        w2 = tk.Canvas(window1, height=self.CANVAS_H, width=self.CANVAS_W, bg="light blue")
        xloc = self.X_OFFSET
        yloc = self.Y_OFFSET
        print(self.cardlist)
        for card in self.cardlist:
            print(card, image_dict[card],xloc, yloc)
            w2.create_image(xloc, yloc, image=image_dict[card], anchor="nw", tags=("card"))
            xloc += self.X_GAP
            # if xloc >= self.CANVAS_W:
            if xloc >= 5 * self.X_GAP:
                yloc = yloc + self.Y_GAP
                xloc = self.X_OFFSET
        w2.pack()
        w2.mainloop()

# using Deck2 deal which is much a simpler class
board2 = Board()
board2.cardlist = Deck2.deal()[0]
board2.display_cardlist()