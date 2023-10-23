from io import BytesIO
import threading
from tkinter import Image, messagebox, ttk,Button
import tkinter as tk
from PIL import Image, ImageTk
from detail_window import detail_windowf

import requests
from cell import Cell

class MainWindow:

    def on_button_clicked (self):
        messagebox.showinfo(message="Iván Grovas Pérez, son programador", title="Desarrollador") #Creamos un messagebox al cual le pasaremos como parámetros el mensaje a mostrar y el título de la ventana donde se muestra el mensaje
    
    def __init__(self, root,json_data): 

        self.root = root
        #Ajustamos el tamaño de las ventanas con estas funciones.
        x = (self.root.winfo_screenwidth()- self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight()- self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")
                       
        self.cells = [] #Creamos una lista vacía para guardar los datos

        for f1 in json_data: #recorremos el json para consumir sus datos y almacenarlos en variables
            name = f1.get("name")
            description = f1.get("description")
            image_url=f1.get("image_url")

            #guardar en una celda las variables
            cell = Cell (name, image_url, description)
            self.cells.append(cell)

        #recorremos la lista de celdas para mostrar las imágenes en la mainwindow
        for i, cell in enumerate (self.cells):
            label = ttk.Label(root,image=cell.Image_tk, text=cell.title,compound=tk.BOTTOM) 
            label.grid(row=i,column=0)
            label.bind("<Button-1>",lambda event, cell=cell : detail_windowf(cell))

        #Creamos una barra de menús
        barra_menus = tk.Menu()
        menu_archivo = tk.Menu(barra_menus, tearoff=False)  #Creamos el primer menú
        menu_archivo.add_command(
            label="Acerca de", #Indicamos como se va a llamar el menú
            accelerator="Ctrl+N", #Le añadimos un atajo de teclado
            command= self.on_button_clicked #Le asignamos una utilidad através de una función
        )       
        barra_menus.add_cascade(menu=menu_archivo, label="Ayuda") #Lo agregamos a la barra de menús
        root.config(menu=barra_menus)
        root.mainloop()