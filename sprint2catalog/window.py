from io import BytesIO
import threading
from tkinter import Image, ttk,Button
import tkinter as tk
from PIL import Image, ImageTk
from detail_window import detail_windowf

import requests
from cell import Cell

class MainWindow:

    def on_button_clicked (self, cell):
            detail_windowf(cell)
    
    def __init__(self, root,json_data): 

        self.root = root
                       
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
            label.bind("<Button-1>",lambda event, cell=cell : self.on_button_clicked(cell))