import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('1200x800')
root.title('Notebook Demo')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=False)

# create frames
frame1 = ttk.Frame(notebook, width=1200, height=800)
frame2 = ttk.Frame(notebook, width=1200, height=800)
frame3 = ttk.Frame(notebook, width=1200, height=800)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(frame1, text='frame1')
notebook.add(frame2, text='frame2')
notebook.add(frame3, text='frame3')

root.mainloop()