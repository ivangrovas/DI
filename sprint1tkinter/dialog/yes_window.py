import tkinter as tk

from tkinter import ttk

def show_yes_window ():
    #Creamos una ventana nueva con la librería tkinter
    yes_root= tk.Tk()
    #Ponemos un titulo a la ventana
    yes_root.title("Ventana del sí")
    #Creamos un mensaje dentro de la ventana con label y como cualquier widget lo empaquetamos con pack
    label = ttk.Label(yes_root, text="Bienvenido a las opciones YES")
    label.pack()
    #Cerramos la ejecución de la ventana con mainloop
    yes_root.mainloop()


