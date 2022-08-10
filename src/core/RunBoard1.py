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
from Deck import Deck2  # Board uses Deck2
from tkinter import ttk


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

    def display_cardlist20(self):
        print ("running display_cardlist20")
        playsixhands = PlaySixHands25(self.pyramid_hands)
        player_names = playsixhands.player_names
        # root window
        root = tk.Tk()
        root.geometry('1800x1200')
        root.title('Pyramid Poker Six Hands')

        # create a notebook
        notebook = ttk.Notebook(root)
        notebook.pack(pady=10, expand=False)

        # create frames
        frame1 = ttk.Frame(notebook, width=1800, height=1200)
        frame2 = ttk.Frame(notebook, width=1800, height=1200)
        frame3 = ttk.Frame(notebook, width=1800, height=1200)
        # frame3 = ttk.Frame(notebook, width=1800, height=1200)

        #        window_label.place(x = 25, y = 25)
        #        window_label.pack()
        hand_separation = 1.04
        X_GAP_factor = .9
        self.CANVAS_W = 25 * self.X_GAP * X_GAP_factor * hand_separation + 25
        self.CANVAS_W *= 2.6
        self.X_GAP = 72 * X_GAP_factor
        self.CANVAS_H = 8.2 * self.Y_GAP + 25
        self.CANVAS_H *= 1.05
        self.Y_OFFSET = 2.2 * self.Y_GAP
        image_dict = create_images()
        w1 = tk.Canvas(frame1, height=1200, width=1800, bg="light blue")
        w2 = tk.Canvas(frame2, height=1200, width=1800, bg="light blue")
        self.X_OFFSET = 0
        xloc = round(self.X_OFFSET,1)
        yloc = 30
        print ("right before entering first for loop")
        print (len(self.pyramid_hands))
        i = 0
        for handx in self.pyramid_hands:
            tk.Label(frame1, text=player_names[i], font=12, bg="White", width=10).place(x=xloc, y=yloc - 25)
            tk.Label(frame2, text=player_names[i], font=12, bg="White", width=10).place(x=xloc, y=yloc - 25)
            # print (player_names[i])
            card_list = (sorted(handx[0:20], key=rank_sort, reverse=True))
            for card in card_list:
                # print(card, image_dict[card],xloc, yloc)

                w1.create_image(xloc, yloc, image=image_dict[card], anchor="nw", tags=("card"))
                w2.create_image(xloc, yloc, image=image_dict[card], anchor="nw", tags=("card"))
                xloc = round(xloc + self.X_GAP,1)
                if xloc >= self.CANVAS_W:
                    yloc = yloc + self.Y_GAP
                    xloc = self.X_OFFSET

            xloc += self.X_GAP
            for card in handx[20:25]:
                # print("card_list20", card, image_dict[card],xloc, yloc)
                w2.create_image(xloc, yloc, image=image_dict[card], anchor="nw", tags=("card"))
                xloc = round(xloc + self.X_GAP, 1)
                if xloc >= self.CANVAS_W:
                    yloc = yloc + self.Y_GAP
                    xloc = self.X_OFFSET

            yloc += 130
            xloc = round(self.X_OFFSET, 1)
            i += 1
        print ("running display 6 hands")
        # root = tk.Tk()

        hand_separation = 1.04
        X_GAP_factor = .5
        self.X_OFFSET = 0
        self.CANVAS_W = 30 * self.X_GAP * X_GAP_factor * hand_separation + 25
        self.X_GAP = 72 * .8
        self.CANVAS_H = 8.2 * self.Y_GAP + 25
        self.Y_OFFSET = 2.2 * self.Y_GAP
        # card_image_dict = create_images()

        w3 = tk.Canvas(frame3, height=1200, width=1800, bg="light pink")
        
        xloc = round(self.X_OFFSET)
        # print ("right before entering first for loop")
        # print (len(self.handslist))
        # playsixhands = PlaySixHands25(self.pyramid_hands)
        self.pyramid_hands = playsixhands.best_pyramid_hands
        self.player_win_points = playsixhands.player_win_points
        for handx in self.pyramid_hands:
            yloc = 0
            print ("handx",handx)
            for i in range(1, 7):
                xloc_start = xloc
                if handx != []:
                    X_GAP_Factor = 1
                    if len(handx[i]) > 5:
                        X_GAP_Factor = 5/len(handx[i])
                    for card in handx[i]:
                        # print("Six hands",card, xloc, yloc)
                        w3.create_image(xloc, yloc, image=image_dict[card], anchor="nw", tags=("card"))
                        xloc += self.X_GAP * X_GAP_Factor
                    xloc = xloc_start
                    yloc = yloc + self.Y_GAP
            xloc = xloc_start + 5 * self.X_GAP * hand_separation
        
        # show player_win_points using grid method
        xloc = 0
        yloc = 600
        player_win_points = self.player_win_points

        # points display parameters
        color = "white"
        label_width = 4
        line_height = 24
        font_size = 16
        for i in range(6):
            for k in range (1,7):
                temp = 0
                for j in range(6):
                    temp = temp + player_win_points[i][j][k]
                player_win_points[i][i][k] = temp
        for i in range(6):
            total_points = 0
            # versus player j
            for j in range(6):
                total_points += player_win_points[i][j][0]
            # printing row labels
            tk.Label(frame3, text="H1", font=font_size, bg=color, width=label_width).place(x=xloc, y=yloc)
            tk.Label(frame3, text="H2", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+1*line_height)
            tk.Label(frame3, text="H3", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+2*line_height)
            tk.Label(frame3, text="H4", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+3*line_height)
            tk.Label(frame3, text="H5", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+4*line_height)
            tk.Label(frame3, text="H6", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+5*line_height)
            tk.Label(frame3, text="Tot", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+6*line_height)
            temp = 0
            # for each hand
            for j in range(6):
                player = self.player_names[j]
                xloc = xloc + 38

                # displaying player name for player j on row 1
                tk.Label(frame3, text=player, font=("Arial 10 bold"), bg=color, width = label_width, anchor="e").place(x=xloc+2, y=yloc-1*line_height)

                # displaying column of points for player j on rows 2-7
                tk.Label(frame3, text=str(player_win_points[i][j][1]), font=font_size, bg=color, width = label_width, anchor="e").place(x=xloc, y=yloc+0*line_height)
                tk.Label(frame3, text=str(player_win_points[i][j][2]), font=font_size, bg=color, width = label_width, anchor="e").place(x=xloc, y=yloc+1*line_height)
                tk.Label(frame3, text=str(player_win_points[i][j][3]), font=font_size, bg=color, width = label_width, anchor="e").place(x=xloc, y=yloc+2*line_height)
                tk.Label(frame3, text=str(player_win_points[i][j][4]), font=font_size, bg=color, width = label_width, anchor="e").place(x=xloc, y=yloc+3*line_height)
                tk.Label(frame3, text=str(player_win_points[i][j][5]), font=font_size, bg=color, width = label_width, anchor="e").place(x=xloc, y=yloc+4*line_height)
                tk.Label(frame3, text=str(player_win_points[i][j][6]), font=font_size, bg=color, width = label_width, anchor="e").place(x=xloc, y=yloc+5*line_height)
                tk.Label(frame3, text=str(player_win_points[i][j][0]), font=font_size, bg=color, width = label_width, anchor="e").place(x=xloc, y=yloc+6*line_height)

            # displaying total points on row 8
            tk.Label(frame3, text=str(total_points),
                     font=font_size, bg=color, anchor="e", width=label_width).place(x=xloc-180+35*i, y=yloc+7*line_height)

            xloc = xloc + hand_separation * 70

        w1.pack()
        w2.pack()
        w3.pack()
        frame1.pack(fill='both', expand=True)
        frame2.pack(fill='both', expand=True)
        frame3.pack(fill='both', expand=True)
        # frame3.pack(fill='both', expand=True)

        # add frames to notebook

        notebook.add(frame1, text='20 card Hands')
        notebook.add(frame2, text='Hands with kitty')
        notebook.add(frame3, text='Results')
        # notebook.add(frame3, text='frame3')
        root.mainloop()

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
