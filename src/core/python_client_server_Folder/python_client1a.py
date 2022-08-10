"""python_client1.py
v1. sets up client_socket
then uses method connect to establish connection
then uses client_socket to receive Welcome message
then uses client_socket to receive hand_pickle
then unpickles hand using pickle.load and prints
v1a. get player_name from tkinter and then sends it to server
"""

import socket
import pickle
import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.title("Client")
topFrame = tk.Frame(window)

player_name =  tk.StringVar()
lblName = tk.Label(topFrame, text = "Name:").pack(side=tk.LEFT)
entName = ttk.Entry(topFrame, textvariable = player_name)
entName.pack(side=tk.LEFT)
btnConnect = tk.Button(topFrame, text="Connect", command=lambda : start_client())
btnConnect.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP)

def start_client():
    if len(entName.get()) < 1:
        tk.Message.showerror(title="ERROR!!!", message="You MUST enter your first name <e.g. John>")
    else:
        player_name = entName.get()
        print (player_name)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 55555))

    # sends player_name to server
    client_socket.send(bytes(player_name, "utf-8"))

    # recv's message from server
    message = client_socket.recv(4096)
    print (message.decode("utf-8"))

    # recv's hand from server
    hand_pickle = client_socket.recv(4096)
    client_hand = pickle.loads(hand_pickle)
    print (client_hand)

window.mainloop()