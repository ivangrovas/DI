import tkinter as tk
from tkinter import ttk


def detail_windowf (cell):
    root = tk.Toplevel()
    label1 = ttk.Label(root, image=cell.image_tk)
    label2= ttk.Label(root, text=cell.title)
    label3 = ttk.Label(root, text=cell.desc)
    label1.pack()
    label2.pack()
    label3.pack()

    root.mainloop()