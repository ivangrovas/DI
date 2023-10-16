from tkinter import ttk,Button
from yes_window import show_yes_window
from no_window  import show_no_window

class MainWindow:
   
    def on_button_clicked (self):
        show_yes_window()

    def on_button_clicked_no (self):
        show_no_window()
    
    def __init__(self, root) -> None: 

        self.root = root

        self.frame = ttk.Frame(self.root)
        self.frame.pack()
            
        self.label = ttk.Label(self.frame, text="Elige una opción?")
        self.label.pack()

        self.buttonYes = ttk.Button(self.frame, text="Yes", command=self.on_button_clicked)
        self.buttonYes.pack(side="left",expand=True)

        self.buttonNo = ttk.Button(self.frame, text="No", command=self.on_button_clicked_no)
        self.buttonNo.pack(side="right",expand=True)

        