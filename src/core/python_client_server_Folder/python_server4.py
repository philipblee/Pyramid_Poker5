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
"""

import socket
from Deck import *
import pickle
import threading

client_sockets = []
new_hand = Deck()
hands = new_hand.deal_6hands()[0]

for i in range(6):
    print(hands[i])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 55555))
server_socket.listen(5)

def accepting_clients(the_server):
    global client_sockets
    while True:
        client_socket, address = the_server.accept()  # waits for client
        print (f"Connection accepted from {address}")
        client_sockets.append(client_socket)
        # print ("number of players:", len(client_sockets))
        threading._start_new_thread(send_recv,(client_socket, address))

def send_recv(client_connection, client_address):
    global client_sockets
    client_connection.send(bytes("Welcome to Server", "utf-8"))
    idx = len(client_sockets) - 1
    print ("player#", idx+1, hands[idx])
    pickle_hand = pickle.dumps(hands[idx])
    client_connection.send(pickle_hand)

threading._start_new_thread(accepting_clients(server_socket))