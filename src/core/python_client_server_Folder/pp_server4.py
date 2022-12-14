""" pp_server3 builds off of chat_server
v3. add the dealing of hands and deck of cards, sends hand instead of welcome message
v4. server no change
"""

import tkinter as tk
import socket
import threading
from Deck import *
import pickle

new_hand = Deck()
hands = new_hand.deal_6hands()[0]
for i in range(6):
    print(hands[i])

window = tk.Tk()
window.title("Chat Server")

# Top frame consisting of two buttons widgets (i.e. btnStart, btnStop)
topFrame = tk.Frame(window)
btnStart = tk.Button(topFrame, text="Connect", command=lambda : start_server())
btnStart.pack(side=tk.LEFT)
btnStop = tk.Button(topFrame, text="Stop", command=lambda : stop_server(), state=tk.DISABLED)
btnStop.pack(side=tk.LEFT)
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


server = None
HOST_ADDR = "127.0.0.1"
HOST_PORT = 55555
client_name = " "
clients = []
clients_names = []


# Start server function
def start_server():
    global server, HOST_ADDR, HOST_PORT # code is fine without this
    btnStart.config(state=tk.DISABLED)
    btnStop.config(state=tk.NORMAL)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST_ADDR, HOST_PORT))
    server.listen(5)  # server is listening for client connection

    threading._start_new_thread(accept_clients, (server, " "))

    lblHost["text"] = "Host: " + HOST_ADDR
    lblPort["text"] = "Port: " + str(HOST_PORT)

# Stop server function
def stop_server():
    global server
    btnStart.config(state=tk.NORMAL)
    btnStop.config(state=tk.DISABLED)

def accept_clients(the_server, y):
    while True:
        client, addr = the_server.accept()
        clients.append(client)
        # use a thread so as not to clog the gui thread
        threading._start_new_thread(send_receive_client_message, (client, addr))

# Function to receive message from current client AND
# Send that message to other clients
def send_receive_client_message(client_connection, client_ip_addr):
    global server, client_name, clients, clients_addr
    client_msg = " "

    # # send welcome message to client
    # bytes_client_name  = client_connection.recv(4096)
    # client_name = bytes_client_name.decode("utf-8")
    # string_msg = "Welcome " + client_name + ". Use 'exit' to quit"
    # bytes_message = bytes(string_msg, "utf-8")
    # client_connection.send(bytes_message)

    # send pickled hand to client
    idx = len(clients) - 1
    print("player#", idx + 1, hands[idx])
    pickle_hand = pickle.dumps(hands[idx])
    client_connection.send(pickle_hand)

    clients_names.append(client_name)
    update_client_names_display(clients_names)  # update client names display_cardlist

    while True:
        bytes_msg = client_connection.recv(4096)
        data = bytes_msg.decode("UTF-8")
        client_msg = data
        if not data: break
        if data == "exit": break

        idx = get_client_index(clients, client_connection)
        sending_client_name = clients_names[idx]

        for c in clients:
            if c != client_connection:
                msg = sending_client_name + "->" + client_msg
                c.send(bytes(msg,"utf-8"))

    # find the client index then remove from both lists(client name list and connection list)
    idx = get_client_index(clients, client_connection)
    del clients_names[idx]
    del clients[idx]
    client_connection.send("BYE!")
    client_connection.close()

    update_client_names_display(clients_names)  # update client names display_cardlist


# Return the index of the current client in the list of clients
def get_client_index(client_list, curr_client):
    idx = 0
    for conn in client_list:
        if conn == curr_client:
            break
        idx = idx + 1

    return idx


# Update client name display_cardlist when a new client connects OR
# When a connected client disconnects
def update_client_names_display(name_list):
    tkDisplay.config(state=tk.NORMAL)
    tkDisplay.delete('1.0', tk.END)

    for c in name_list:
        tkDisplay.insert(tk.END, c+"\n")
    tkDisplay.config(state=tk.DISABLED)


window.mainloop()