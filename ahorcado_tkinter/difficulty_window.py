from tkinter import ttk, Button
from tkinter import messagebox
from game_window import GameWindow
import tkinter as tk

class MainWindow:
    def on_button_clicked (self):
        self.root.destroy()
        self.root = tk.Tk()
        app = GameWindow()
        self.root.mainloop()

    def close(self):
        if messagebox.askokcancel("Cerrar", "¿Estás seguro que deseas salir?"):
            self.root.destroy()
    
    def __init__(self, root,json_data): 

        self.root = root

        #Ajustamos el tamaño de las ventanas con estas funciones.
        x = (self.root.winfo_screenwidth()- self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight()- self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")

        #Creamos un frame para contener los widgets
        self.frame = ttk.Frame(self.root)
        self.frame.pack()
        
        #Añadimos un label para darle información al usuario
        self.label = ttk.Label(self.frame, text="Elige dificultad: ")
        self.label.pack()

        #Añadimos los botones
        self.buttonEasy = ttk.Button(self.frame, text="Fácil", command=self.on_button_clicked)
        self.buttonEasy.pack(side="left",expand=True)

        self.buttonNormal = ttk.Button(self.frame, text="Normal", command=self.on_button_clicked)
        self.buttonNormal.pack(side="left",expand=True)

        self.buttonHard = ttk.Button(self.frame, text="Difícil", command=self.on_button_clicked)
        self.buttonHard.pack(side="right",expand=True)

        close_button = ttk.Button(root, text="Salir", command=self.close)
        close_button.pack(pady=10)
    
   