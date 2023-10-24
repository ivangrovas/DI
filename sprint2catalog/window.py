from io import BytesIO
import threading
from tkinter import Canvas, Frame, Image, Label, Scrollbar, messagebox, ttk,Button
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
        
        #Creamos un widget canvas para hacer el scrollbar
        self.canvas = Canvas (self.root) 
        self.scrollbar = Scrollbar (self.root, orient="vertical", command=self.canvas.yview) #Necesitamos un scrollbar, al cual le indicamos qn es el padre, su orientancion y que hará scroll en el eje y
        self.scrollable_frame= Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>", #Indicamos que el fram cambié de tamaño en función de si actualiza el tamaño de la región del desplazamiento del Canvas
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw") #Colocamos el frame dentro del canvas en la posicion 0,0 y lo ubicamos en el noroeste con nw
        self.canvas.configure(yscrollcommand=self.scrollbar.set) #Vinculamos la barra de desplazamiento al Canvas, de forma q cuando se desplace el Canvas, se actualiza automáticamente

        for i, cell in enumerate (self.cells):
            self.add_item(cell)

        self.canvas.grid(row=0, column=0, sticky="nsew") #Con grid se coloca el canvas en la ventana principal, el argumento stocky=nsew permite que canvas se espanda en todas lasd direcciones
        self.scrollbar.grid(row=0,column=1, sticky="ns") #Coloca la barrra de desplazamiento justo al lado del canvas. Ns permite que se expanda verticalmente

        self.root.grid_rowconfigure(0, weight=1) #Permite que con peso 1 se redimensione de manera proporcional cuando se redimensione el tamaño de la ventana principal
        self.root.grid_columnconfigure (0, weight=1) #Lo mismo que el anterior pero para la primera columna

        #Creamos una barra de menús
        barra_menus = tk.Menu()
        menu_archivo = tk.Menu(barra_menus, tearoff=False)  #Creamos el primer menú
        menu_archivo.add_command(
            label="Acerca de", #Indicamos como se va a llamar el menú
            accelerator="Ctrl+N", #Le añadimos un atajo de teclado
            command= self.on_button_clicked #Le asignamos una utilidad através de una función
        )       
        barra_menus.add_cascade(menu=menu_archivo, label="Ayuda") #Lo agregamos a la barra de menús
        self.root.config(menu=barra_menus)
        self.root.mainloop()
    
    def add_item(self, cell): #Refactorización del código hecho en tareas anteriores

        #Frame será un hijo del canvas, el cual será un widget desplazable
        frame = Frame (self.scrollable_frame)
        frame.pack(pady=10)

        label = ttk.Label (frame, image = cell.Image_tk, text= cell.title, compound= tk.BOTTOM)
        label.grid(row = 0, column=0)

        label.bind("<Button-1>", lambda event, cell=  cell : detail_windowf(cell))    

        