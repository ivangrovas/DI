from tkinter import ttk,Button
import tkinter as tk
#from yes_window import show_yes_window
#from no_window  import show_no_window
from cell import Cell
from PIL import Image, ImageTk

class MainWindow:
   
    #def on_button_clicked (self):
    #    show_yes_window()

    #def on_button_clicked_no (self):
    #    show_no_window()
    
    def __init__(self, root) -> None: 

        #Inicializamos 5 celdas
        self.cells = [
            Cell("F1 1", "C:\\msys64\\home\\Usuario\\DI\\sprint1tkinter\\catalog\\data\\unedited\\mvwdc.jpeg"),
            Cell("F1 2", "C:\\msys64\\home\\Usuario\\DI\\sprint1tkinter\\catalog\\data\\unedited\\th-828554261.jpeg"),
            Cell("F1 3", "C:\\msys64\\home\\Usuario\\DI\\sprint1tkinter\\catalog\\data\\unedited\\th-3420979466.jpeg"),
            Cell("F1 4", "C:\\msys64\\home\\Usuario\\DI\\sprint1tkinter\\catalog\\data\\unedited\\wc1728204-2069878345.jpeg"),
            Cell("F1 5", "C:\\msys64\\home\\Usuario\\DI\\sprint1tkinter\\catalog\\data\\unedited\\wp6936516-653863971.jpeg"),
        ]

        #recorremos con el bucle for y mostramos al usuario cada imagen en funcion del label.grid
        #Guardamos cada imagen en una variable para posteriormente poder redimensionarla. 
        for i, cell in enumerate (self.cells):
            img = Image.open(cell.path) #Abrimos una imagen en cada cell path con la biblioteca pillow.
            img1 = img.resize((100,100),Image.LANCZOS) #redimensionamos la imagen y usamos el metodo image.LANCZOS para mejorar la calidad de redimensión
            cell.image_tk = ImageTk.PhotoImage(img1) #Creamos un objeto con la imagen redimensionada
            label = ttk.Label(root,image=cell.image_tk, text=cell.title,compound=tk.BOTTOM) #Creamos un widget
            label.grid(row=i,column=0)