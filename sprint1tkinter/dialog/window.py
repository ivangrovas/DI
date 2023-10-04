from tkinter import ttk,Button

class MainWindow:
    def on_button_clicked(self):
        pass

    def __init__(self, root) -> None: 
        self.root = root
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label(self.frame, text = "Este mensaje es poco importante")
        self.label.pack()

        self.button = ttk.Button(self.frame, text="Realizar acción", command= self.on_button_clicked)
        self.button.pack()