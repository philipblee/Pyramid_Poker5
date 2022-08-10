"""python_client1.py
v1. sets up client_socket
then uses method connect to establish connection
then uses client_socket to receive Welcome message
then uses client_socket to receive hand_pickle
then unpickles hand using pickle.load and prints
v1a. get player_name from tkinter and then sends it to server
"""

import tkinter.ttk as ttk
from python_client_server_Folder.python_client7 import *

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

    # 1st thing sent - player_name
    try:
        client_socket.send(bytes(player_name, "utf-8"))
    except Exception as e:
        print ("client error - sending player_name")

    # 1st thing recv'd - message from server
    try:
        message = client_socket.recv(4096)
    except Exception as e:
        print ("client error - sending welcome message")
    print (message.decode("utf-8"))

    # 2nd thing recv'd -  hand from server
    try:
        hand_pickle = client_socket.recv(4096)
    except Exception as e:
        print ("client error - sending hand")

    client_hand = pickle.loads(hand_pickle)
    print (client_hand)

    image_dir = "../Cards_gif/"
    image_dict = create_images()

    X_GAP = 80
    Y_GAP = 100

    w = tk.Canvas(window, height=6*Y_GAP+10, width=12*X_GAP, background="pink", relief="raised")

    X_OFFSET = 2
    Y_OFFSET = 10 + Y_GAP
    y = Y_OFFSET
    x = X_OFFSET + 9   # adds 5 to move card to center of white rectangle

    show_next_hand()

    # finished_setup_button, toggle_show_next_hand to enable/disable
    finished_setup_button = tk.Button(window, text="I'm Done!", font=12, command=stub)
    finished_setup_button.place(x=10, y=10, width=100, height=24)
    toggle_button = tk.Button(window, text="Toggle", font=12, command=toggle_finished, state='disabled')
    toggle_button.place(x=10, y=40, width=100, height=24)
    reset_button = tk.Button(window, text="Reset Hand", font=12, command=show_next_hand)
    reset_button.place(x=10, y=70, width=100, height=24)

    w.pack()

    w.tag_bind("token", "<Button-1>", onClick)
    w.tag_bind("token", "<B1-Motion>", onMotion)
    w.tag_bind("token", "<ButtonRelease-1>", onRelease)

window.mainloop()