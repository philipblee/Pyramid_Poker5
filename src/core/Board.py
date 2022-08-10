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
        # self.player_win_points = [[[0,0,0,0,0,0,0] for i in range(6)] for j in range(6)]

        self.player_win_points = [[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]],
                             [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
                             [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
                             [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
                             [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
                             [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
                             [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]]

        self.player_names = ["Pete", "John", "Ming", "Tony", "Ed", "Phil"]
        self.Y_GAP = 95
        self.X_GAP = 72
        self.CANVAS_H = 7 * self.Y_GAP
        self.CANVAS_W = 25 * self.X_GAP
        self.X_OFFSET = 10
        self.Y_OFFSET = 10
        self.pyramid_hands = []

    def display_cardlist25(self):
        print ("running display_cardlist")
        window1 = tk.Tk()

        window_label = tk.Label(window1, text = "window1")
        window_label.place(x = 25, y = 25)
        window_label.pack()
        hand_separation = 1.04
        X_GAP_factor = .8
        self.CANVAS_W = 25 * self.X_GAP * X_GAP_factor * hand_separation + 25
        self.X_GAP = 72 * X_GAP_factor
        self.CANVAS_H = 8.2 * self.Y_GAP + 25
        self.Y_OFFSET = 2.2 * self.Y_GAP
        image_dict = create_images()
        w2 = tk.Canvas(window1, height=self.CANVAS_H, width=self.CANVAS_W, bg="light blue")
        xloc = round(self.X_OFFSET,1)
        yloc = 0
        for card in self.cardlist:
            print(card, image_dict[card],xloc, yloc)
            w2.create_image(xloc, yloc, image=image_dict[card], anchor="nw", tags=("card"))
            xloc += self.X_GAP
            if xloc >= self.CANVAS_W:
                yloc = yloc + self.Y_GAP
                xloc = self.X_OFFSET
        w2.pack()
        w2.mainloop()

    def display_cardlist20(self):
        print ("running display_cardlist")
        window1 = tk.Tk()

        window_label = tk.Label(window1, text = "window1")
        window_label.place(x = 25, y = 25)
        window_label.pack()
        hand_separation = 1.04
        X_GAP_factor = .8
        self.CANVAS_W = 25 * self.X_GAP * X_GAP_factor * hand_separation + 25
        self.X_GAP = 72 * X_GAP_factor
        self.CANVAS_H = 8.2 * self.Y_GAP + 25
        self.Y_OFFSET = 2.2 * self.Y_GAP
        image_dict = create_images()
        w2 = tk.Canvas(window1, height=self.CANVAS_H, width=self.CANVAS_W, bg="light blue")
        xloc = round(self.X_OFFSET,1)
        yloc = 10
        print ("right before entering first for loop")
        print (len(self.pyramid_hands))
        for handx in self.pyramid_hands:
            card_list = (sorted(handx[0:20], key=rank_sort, reverse=True))
            for card in card_list:
                print(card, image_dict[card],xloc, yloc)
                w2.create_image(xloc, yloc, image=image_dict[card], anchor="nw", tags=("card"))
                xloc = round(xloc + self.X_GAP,1)
                if xloc >= self.CANVAS_W:
                    yloc = yloc + self.Y_GAP
                    xloc = self.X_OFFSET

            xloc += self.X_GAP
            for card in handx[20:25]:
                print(card, image_dict[card],xloc, yloc)
                w2.create_image(xloc, yloc, image=image_dict[card], anchor="nw", tags=("card"))
                xloc = round(xloc + self.X_GAP, 1)
                if xloc >= self.CANVAS_W:
                    yloc = yloc + self.Y_GAP
                    xloc = self.X_OFFSET

            yloc += 100
            xloc = round(self.X_OFFSET, 1)

        w2.pack()
        w2.mainloop()

    def display_6hands(self):
        print ("running display_6hands")
        window2 = tk.Tk()

        hand_separation = 1.04
        X_GAP_factor = .8
        self.CANVAS_W = 30 * self.X_GAP * X_GAP_factor * hand_separation + 25
        self.X_GAP = 72 * .8
        self.CANVAS_H = 8.2 * self.Y_GAP + 25
        self.Y_OFFSET = 2.2 * self.Y_GAP
        card_image_dict = create_images()

        w = tk.Canvas(window2, height=self.CANVAS_H, width=self.CANVAS_W, bg="light blue")
        xloc = round(self.X_OFFSET)
        # print ("right before entering first for loop")
        # print (len(self.handslist))
        for handx in self.pyramid_hands:
            yloc = round(self.Y_OFFSET)
            # print (handx)
            for i in range(1, 7):
                xloc_start = xloc
                if handx != []:
                    X_GAP_Factor = 1
                    if len(handx[i]) > 5:
                        X_GAP_Factor = 5/len(handx[i])
                    for card in handx[i]:
                        # print(card, xloc, yloc)
                        w.create_image(xloc, yloc, image=card_image_dict[card], anchor="nw", tags=("card"))
                        xloc += self.X_GAP * X_GAP_Factor
                    xloc = xloc_start
                    yloc = yloc + self.Y_GAP
            xloc = xloc_start + 5 * self.X_GAP * hand_separation
        
        # show player_win_points using grid method
        xloc = self.X_OFFSET
        yloc = 30
        player_win_points = self.player_win_points

        # points display parameters
        color = "white"
        label_width = 4
        line_height = 24
        font_size = 16
        for i in range(6):
            total_points = 0
            for j in range(6):
                total_points += player_win_points[i][j][0]
            # printing row labels
            tk.Label(window2, text="H1", font=font_size, bg=color, width=label_width).place(x=xloc, y=yloc)
            tk.Label(window2, text="H2", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+1*line_height)
            tk.Label(window2, text="H3", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+2*line_height)
            tk.Label(window2, text="H4", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+3*line_height)
            tk.Label(window2, text="H5", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+4*line_height)
            tk.Label(window2, text="H6", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+5*line_height)
            tk.Label(window2, text="Tot", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+6*line_height)
            for j in range(6):
                player = self.player_names[j]
                xloc = xloc + 38
                if i == j:
                    player_win_points[i][j][1] = "-"
                    player_win_points[i][j][2] = "-"
                    player_win_points[i][j][3] = "-"
                    player_win_points[i][j][4] = "-"
                    player_win_points[i][j][5] = "-"
                    player_win_points[i][j][6] = "-"
                    player_win_points[i][j][0] = "-"
                # displaying player name for player j on row 1
                tk.Label(window2, text=player, font=("Arial 10 bold"), bg=color, width = label_width, anchor="e").place(x=xloc+2, y=yloc-1*line_height)
                # displaying column of points for player j on rows 2-7
                tk.Label(window2, text=str(player_win_points[i][j][1]), font=font_size, bg=color, width = label_width, anchor="e").place(x=xloc, y=yloc+0*line_height)
                tk.Label(window2, text=str(player_win_points[i][j][2]), font=font_size, bg=color, width = label_width, anchor="e").place(x=xloc, y=yloc+1*line_height)
                tk.Label(window2, text=str(player_win_points[i][j][3]), font=font_size, bg=color, width = label_width, anchor="e").place(x=xloc, y=yloc+2*line_height)
                tk.Label(window2, text=str(player_win_points[i][j][4]), font=font_size, bg=color, width = label_width, anchor="e").place(x=xloc, y=yloc+3*line_height)
                tk.Label(window2, text=str(player_win_points[i][j][5]), font=font_size, bg=color, width = label_width, anchor="e").place(x=xloc, y=yloc+4*line_height)
                tk.Label(window2, text=str(player_win_points[i][j][6]), font=font_size, bg=color, width = label_width, anchor="e").place(x=xloc, y=yloc+5*line_height)
                tk.Label(window2, text=str(player_win_points[i][j][0]), font=font_size, bg=color, width = label_width, anchor="e").place(x=xloc, y=yloc+6*line_height)
            # displaying total points on row 8
            tk.Label(window2, text=str(total_points),
                     font=font_size, bg=color, anchor="e", width=label_width).place(x=xloc, y=yloc+7*line_height)
            xloc = xloc + hand_separation * 70
        w.pack()
        w.mainloop()


# using Deck2 deal which is much a simpler class
board2 = Board()
board2.pyramid_hands = Deck2.deal()
board2.display_cardlist20()


# testing Board.display_6hands
# board4 = Board()
# playsixhands = PlaySixHands25(board2.pyramid_hands)
# board4.pyramid_hands = playsixhands.best_pyramid_hands
# board4.player_win_points = playsixhands.player_win_points
# board4.display_6hands()
