from tkinter import ttk,Button
import tkinter as tk
#from yes_window import show_yes_window
#from no_window  import show_no_window
from cell import Cell

class MainWindow:
   
    #def on_button_clicked (self):
    #    show_yes_window()

    #def on_button_clicked_no (self):
    #    show_no_window()
    
    def __init__(self, root) -> None: 

        #Inicializamos 5 celdas
        self.cells = [
            Cell("F1 1", "C:\\msys64\\home\\Usuario\\DI\\sprint1tkinter\\catalog\\data\\edited\\mvwdc.jpeg"),
            Cell("F1 2", "C:\\msys64\\home\\Usuario\\DI\\sprint1tkinter\\catalog\\data\\edited\\th-828554261.jpeg"),
            Cell("F1 3", "C:\\msys64\\home\\Usuario\\DI\\sprint1tkinter\\catalog\\data\\edited\\th-3420979466.jpeg"),
            Cell("F1 4", "C:\\msys64\\home\\Usuario\\DI\\sprint1tkinter\\catalog\\data\\edited\\wc1728204-2069878345.jpeg"),
            Cell("F1 5", "C:\\msys64\\home\\Usuario\\DI\\sprint1tkinter\\catalog\\data\\edited\\wp6936516-653863971.jpeg"),
        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root,image=cell.image_tk,text=cell.title,compound= tk.BOTTOM)
            label.grid(row=i,column=0)
            label.bind("Button-1", lambda event, cell = cell: self.on_button_clicked)