from tkinter import Tk , ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox

class MainWindow():
    def on_button_clicked(self, cell):
        message= "Has hecho click en la celda"+cell.title
        messagebox.showinfo(("Información"+ message))

    def __init__(self, root) -> None: #self equivale al this de java
        root.title ("MainWindow")

        self.cells = [
            Cell("Fer 1", "C:\\Users\\Usuario\\Downloads\\Fer1.jpeg"),
            Cell("Fer 2", "C:\\Users\\Usuario\\Downloads\\Fer2.jpeg"),
            Cell("Fer 3", "C:\\Users\\Usuario\\Downloads\\Fer3.jpeg"),
        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root,image=cell.image_tk,text=cell.title,compound= tk.BOTTOM)
            label.grid(row=i,column=0)
            label.bind("Button-1", lambda event, cell = cell: self.on_button_clicked)
