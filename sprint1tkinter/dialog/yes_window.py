import tkinter as tk

from tkinter import ttk

def show_yes_window ():
    yes_root= tk.Tk()
    yes_root.title("Ventana del sí")
    label = ttk.Label(yes_root, text="Bienvenido a las opciones YES")
    label.pack()
    yes_root.mainloop()


