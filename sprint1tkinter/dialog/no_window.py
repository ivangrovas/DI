import tkinter as tk

def show_no_window ():
    #Creamos una ventana nueva con la librería tkinter
    no_root= tk.Tk()
    #Ponemos un titulo a la ventana
    no_root.title("Ventana del NO")
    #Creamos un mensaje dentro de la ventana con label y como cualquier widget lo empaquetamos con pack
    label = tk.Label(no_root, text="Bienvenido a las opciones del NO")
    label.pack()
    #Cerramos la ejecución de la ventana con mainloop
    no_root.mainloop()
