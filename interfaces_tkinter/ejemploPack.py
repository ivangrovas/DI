from tkinter import Tk, Button

root = Tk()
root.title = "Ejemplo de uso del pack"

button1 = Button (root, text="Botón 1")
button2 = Button (root, text="Botón 2")
button3 = Button (root, text="Botón 3")

button1.pack (side="top", fill= "both", expand=True, padx=10, pady=5, anchor="nw")
button2.pack (side="left", fill= "x", expand=True)
button3.pack (side="right", fill= "y")

root.mainloop()
