from tkinter import Tk #Importamos la clase Tk de la librería tkinter
from window import MainWindow #Importamos la clase MainWindow

if __name__ == "__main__": #Verificamos si la ejecución es la del main. 
    root = Tk() #Instanciamos la clase Tk y lo guardamos en la variable root
    app = MainWindow(root) #Creamos una instancia de la clase MainWindow (al cual pasaremos root como parámetro) y la guardamos en la variable app
    root.mainloop() #Iniciamos el bucle principal para que se muestre la ventana.
