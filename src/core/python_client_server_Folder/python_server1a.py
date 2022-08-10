"""  python_server1.py
v1. deals out six hands
then sets up server_socket and binds address
then listens to server socket
when it hears something, then accepts() setting up (client_socket, address)
then it sends Welcome message
then it sends pickled_hand
v1a. after getting player_name, then get going
"""

import socket
from Deck import *
import pickle

new_hand = Deck()
hands = new_hand.deal_6hands()[0]

for i in range(6):
    print(hands[i])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 55555))
server_socket.listen(5)

# This while loop, keeps waiting for additional clients to connect
while True:
    client_socket, address = server_socket.accept()
    print (f"Connection from {address} has been established!")

    player_name = client_socket.recv(4096)
    print (player_name.decode("utf-8"), end="")
    print (" - New Player")

    client_socket.send(bytes("Welcome to Server", "utf-8"))
    print (hands[0])
    pickle_hand = pickle.dumps(hands[0])
    client_socket.send(pickle_hand)