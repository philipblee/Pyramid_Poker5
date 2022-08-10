"""  python_server.py
v1. deals out six hands
then sets up server_socket and binds address
then listens to server socket
when it hears something, then accepts() setting up (client_socket, address)
then it sends Welcome message
then it sends pickled_hand
v2. now handles multiple clients (players)
v3. no change on server
v4. no change on server
v5. no change on server
v6. add GUI
v7 and v8. no change on server
v9. gets player_hand from client - storing all six hands in hands_stored
v10 trying to get showdown to work on server
v11 pretty up output on server, uses Board class
v12 TBD
"""

import socket
from Deck import *
import pickle
import threading
import tkinter as tk
from PokerHand import PokerHand
from ShowDownPoints import ShowDownPoints
from display_points import create_images
# from Board import Board
client_sockets = []
new_hand = Deck()
hands = new_hand.deal_6hands()[0]
hands_stored =[[], [], [], [], [], [], []]
points_stored = [[], [], [], [], [], [], []]
play_hand = [False, False, False, False, False, False, False]
player_names = ["Peter ", "Johnny", "Ming  ", "Tony  ", "Edmond", "Philip"]
for i in range(6):
    print(hands[i])

window = tk.Tk()
window.title("Pyramid Poker Server")

# Top frame consisting of two buttons widgets (i.e. btnStart, btnStop)
topFrame = tk.Frame(window)
btnStart = tk.Button(topFrame, text="Start Game", command=lambda : start_game())
btnStart.pack(side=tk.LEFT)
# btnStop = tk.Button(topFrame, text="Stop Server", command=lambda : stop_server(), state=tk.DISABLED)
# btnStop.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP, pady=(5, 0))

# Middle frame consisting of two labels for displaying the host and port info
middleFrame = tk.Frame(window)
lblHost = tk.Label(middleFrame, text = "Host: X.X.X.X")
lblHost.pack(side=tk.LEFT)
lblPort = tk.Label(middleFrame, text = "Port:XXXX")
lblPort.pack(side=tk.LEFT)
middleFrame.pack(side=tk.TOP, pady=(5, 0))

# The client frame shows the client area
clientFrame = tk.Frame(window)
lblLine = tk.Label(clientFrame, text="**********Client List**********").pack()
scrollBar = tk.Scrollbar(clientFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(clientFrame, height=15, width=30)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollBar.set, background="#F4F6F7", highlightbackground="grey", state="disabled")
clientFrame.pack(side=tk.BOTTOM, pady=(5, 10))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("10.0.0.209", 55555))
server_socket.listen(5)

def accepting_clients(the_server):
    global client_sockets
    while True:
        client_socket, address = the_server.accept()  # waits for client
        print (f"Connection accepted from {address}")
        client_sockets.append(client_socket)

        print ("number of players:", len(client_sockets))
        client_socket.send(bytes("Welcome to Server", "utf-8"))
        idx = len(client_sockets) - 1
        print ("player#", idx+1, hands[idx])
        play_hand[idx] = True
        pickle_hand = pickle.dumps(hands[idx])
        client_socket.send(pickle_hand)
        threading._start_new_thread(receive_result, (client_socket, idx))

def receive_result(sck, idx):
    global hands_stored, play_hand, play_hand_count
    pickled_hand = sck.recv(4096)
    hand = pickle.loads(pickled_hand)
    hands_stored[idx] = hand
    play_hand[idx] = True
    play_hand_count += 1
    this_hand = PokerHand()
    points_stored[idx] = this_hand.get_six_hands_points(hands_stored[idx])
    sd = ShowDownPoints(points_stored, play_hand)
    for i in range (6):
        if play_hand[i] == True:
            for cardlist in hands_stored[i]:
                window.title("Player Hands")
                y_list = [0, 5 * Y_GAP, 4 * Y_GAP, 3 * Y_GAP, 2 * Y_GAP, Y_GAP, 0]
                for j in [6, 5, 4, 3, 2, 1]:
                    x = X_OFFSET
                    x1 = x
                    y = y_list[j] + 8
                    overlap_factor = 1
                    for card in cardlist[j]:
                        if len(cardlist[i]) > 5:
                            overlap_factor = 5 / (len(cardlist[j]) + 1)
                        r.create_image(x, y, image=image_dict[card[0:3]], anchor="nw", tag="best")
                        x += X_GAP * overlap_factor
                    x1 = x1 + 5 * X_GAP
                    x = x1
    print ("Server Received", idx, hand)

def start_game():
    threading._start_new_thread(accepting_clients(server_socket))


player_hand_count = 0
results = tk.Tk()
image_dict = create_images()
X_GAP = 72
Y_GAP = 95
X_OFFSET = 13
Y_OFFSET = 7
y = Y_OFFSET
x = X_OFFSET
X_OFFSET = 11
w = tk.Canvas(results, height=7 * Y_GAP + 10 + Y_OFFSET,
              width=10 * X_GAP + X_OFFSET, bg="light blue", relief="raised")
w.pack()
window.mainloop()