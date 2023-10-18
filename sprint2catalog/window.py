import threading
from tkinter import ttk,Button
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
from cell import Cell
import requests

class MainWindow:
    
    def __init__(self, root,json_data) -> None: 

        for f1 in json_data:
            name = f1.get("name")
            description = f1.get("description")
            image_url=f1.get("image_url")
            self.thread = threading.Thread(target=self.load_image_from_url, args=(name, description, image_url)) #Lanzamos en este hilo secundario la función load_image_from_url la cuál leerá el json
            self.thread.start()

            f1_data = {
                "name": name,
                "description": description,
                "image_url":image_url
            }

            self.cells = []

            self.cells.append (f1_data)

        for i, cell in enumerate (self.cells):
            label = ttk.Label(root,image=cell.image_tk, text=cell.title,compound=tk.BOTTOM) 
            label.grid(row=i,column=0)
            #label.bind("<Button-1>",lambda event, cell=cell:self.on_button_clicked(cell))
        
    def load_image_from_url(self, url):
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content))
        img = ImageTk.PhotoImage(img_data)
        