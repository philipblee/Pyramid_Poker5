import tkinter as tk

top = tk.Tk()
top.title("Window")

def switch():
    if b1["state"] == "normal":
        b1["state"] = "disabled"
        b2["text"] = "enable"
    else:
        b1["state"] = "normal"
        b2["text"] = "disable"

# --Buttons
b1 = tk.Button(top, text="Button", height=5, width=7)
b1.grid(row=0, column=0)

b2 = tk.Button(text="disable", command=switch)
b2.grid(row=0, column=1)

top.mainloop()