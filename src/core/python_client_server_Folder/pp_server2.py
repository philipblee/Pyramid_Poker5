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
v9. gets player_hand from client/player
"""

""" pp4_server v1 pyramid poker server
v1. works - receiveds player_hand from client
v2. add a thread

"""
import socket
from Deck import *
import pickle
import threading
import tkinter as tk

client_sockets = []
new_hand = Deck()
hands = new_hand.deal_6hands()[0]

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
server_socket.bind(("127.0.0.1", 55555))
server_socket.listen(5)

def accepting_clients(the_server):
    global client_sockets
    while True:
        client_socket, address = the_server.accept()  # waits for client
        print (f"Connection accepted from {address}")
        # username = client_socket.recv(4096)
        # print ("server received username", username)
        client_sockets.append(client_socket)
        # print ("number of players:", len(client_sockets))

        client_socket.send(bytes("Welcome to Server", "utf-8"))
        idx = len(client_sockets) - 1
        print ("player#", idx+1, hands[idx])
        pickle_hand = pickle.dumps(hands[idx])
        client_socket.send(pickle_hand)
        threading._start_new_thread(receive_result, (client_socket, "m"))

def receive_result(sck, idx):
    pickled_hand = sck.recv(4096)
    hand = pickle.loads(pickled_hand)
    print ("Server Received", idx, hand)

def start_game():
    threading._start_new_thread(accepting_clients(server_socket))

window.mainloop()