import tkinter as tk
from tkinter import ttk


def detail_windowf (cell):
    root = tk.Toplevel() #Creamos una ventana emergente con Toplavel y la almacenamos en la variable root
    #Creamos 3 widgtes utilizando el constructor ttk de la libreria tkinter, el cual se colocará sobre la ventana root y contendrá 
    #una imágen y texto (título/descropción)
    #Ajustamos el tamaño de las ventanas con estas funciones.
    x = (root.winfo_screenwidth()- root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight()- root.winfo_reqheight()) / 2
    root.geometry(f"+{int(x)}+{int(y)}")
    label1 = ttk.Label(root, image=cell.Image_tk) 
    label2= ttk.Label(root, text=cell.title)
    label3 = ttk.Label(root, text=cell.desc)
    #Empaquetamos los 3 widgets.
    label1.pack()
    label2.pack()
    label3.pack()
    #Iniciamos el bucle principal para que se muestre la ventana.
    root.mainloop()