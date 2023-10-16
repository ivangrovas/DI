from tkinter import ttk,Button
import tkinter as tk
#from yes_window import show_yes_window
#from no_window  import show_no_window
from cell import Cell
from detail_window import detail_windowf


class MainWindow: #Creamos la clase MainWindow
   
   #Creamos una función pora cuanto se haga clic en la imágen. Esta función llamrá a otra función a la cuál le pasaremos cell como parámetro
    def on_button_clicked (self,cell):
        detail_windowf(cell)

    #def on_button_clicked_no (self):
    #    show_no_window()
    
    def __init__(self, root) -> None: 

        #Inicializamos 5 celdas
        self.cells = [
            Cell("F1 1", "C:\\msys64\\home\\Usuario\\DI\\sprint1tkinter\\catalog\\data\\unedited\\mvwdc.jpeg", "Max Verstappen se llevó una nueva victoria en la carrera del Gran Premio de Japón 2023 de Fórmula 1. Mira los resultados y el resumen del domingo en Suzuka. "),
            Cell("F1 2", "C:\\msys64\\home\\Usuario\\DI\\sprint1tkinter\\catalog\\data\\unedited\\th-828554261.jpeg","La asociación McLaren-Honda demostró ser imparable, y el MP4/4 ganó todas las carreras excepto una esa temporada, y también todas las pole position del año menos una."),
            Cell("F1 3", "C:\\msys64\\home\\Usuario\\DI\\sprint1tkinter\\catalog\\data\\unedited\\th-3420979466.jpeg","La carrera del Gran Premio de Mónaco 2023 de Fórmula 1 nos dejó una nueva victoria de Max Verstappen y un podio de Fernando Alonso. Resumen y resultados del domingo. "),
            Cell("F1 4", "C:\\msys64\\home\\Usuario\\DI\\sprint1tkinter\\catalog\\data\\unedited\\wc1728204-2069878345.jpeg","El Ferrari F2005 fue un monoplaza de Fórmula 1, con el cual Scuderia Ferrari compitió en la temporada 2005. Finalmente las prestaciones que ofrecía el F2005 no estuvieron a la altura."),
            Cell("F1 5", "C:\\msys64\\home\\Usuario\\DI\\sprint1tkinter\\catalog\\data\\unedited\\wp6936516-653863971.jpeg","El Ferrari SF71H fue un monoplaza de Fórmula 1 diseñado por la Scuderia Ferrari para competir en la temporada 2018 de Fórmula 1. "),
        ]

        #recorremos con el bucle for y mostramos al usuario cada imagen en funcion del label.grid
        #Guardamos cada imagen en una variable para posteriormente poder redimensionarla. 
        for i, cell in enumerate (self.cells):
            label = ttk.Label(root,image=cell.image_tk, text=cell.title,compound=tk.BOTTOM) #Creamos un widget
            label.grid(row=i,column=0)
            label.bind("<Button-1>",lambda event, cell=cell:self.on_button_clicked(cell))