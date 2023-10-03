from tkinter import Tk,Label
from PIL import Image, ImageTk

root= Tk();
root.title("Ejemplo de imagen")

imagen = ImageTk.PhotoImage(file="C:\\Users\\Usuario\\Downloads\\aston-martins-spanish-driver-fernando-alonso-walks-in-the-news-photo-1695894076-1848099226.jpeg")
label = Label(root, image=imagen)
label.pack()

root.mainloop()