import tkinter as tk
import threading
import requests
from window import MainWindow

class LoadingWindow:

    def __init__(self,root) -> None:

        self.root = root
        #Ajustamos el tamaño de las ventanas con estas funciones.
        x = (self.root.winfo_screenwidth()- self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight()- self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")
        print (self.root.winfo_reqwidth())
        print (self.root.winfo_reqheight())
        self.finished = False
        self.json_data= []
        self.root.title("Cargando...")
        self.root.geometry("170x120") #Definimos el ancho y el alto de la ventana
        self.root.resizable (False, False) #Indicamos con resizable que no queremos redimensionar la ventana ni en alto ni en ancho poniendo False

        self.label = tk.Label (self.root, text="Cargando datos...", font=("Arial", 14)) #Con font definimos tipo de letra y tamaño
        self.label.pack(side=tk.TOP, pady=10)

        label_bg_color = self.label.cget("bg") #Con el método cget obtenemos el valor de la opción que pasamos como parámetro
        #en este caso, pasando bg queremos obtener el color del fondo

        #El widget canvas lo usaremos para pintar una circunferencia de carga que represente su progreso.
        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color) #Pasamos el ancho y alto del mismo, así como el color de fondo el cuál obtuvimos con el metodo cget
        self.canvas.pack()

        self.progress = 0

        self.draw_progress_circle(self.progress)

        self.update_progress_circle()

        #Realizamos la petición HTTP desde un hilo secundario, es una norma general.
        self.thread = threading.Thread(target=self.feth_json_data) #Lanzamos en este hilo secundario la función fetch_json_data la cuál leerá el json
        self.thread.start()

        #Comprobamos que el hilo está activo
        if self.thread.is_alive():
            self.check_thread()
        
    def draw_progress_circle(self,progress):
        self.canvas.delete("progress") #Elimina el elemento dibujado que tiene la tag asociada
        angle = int (360 * (progress/100))

        #Con el método create_arc dibujamos el arco de circunferencia. Los 4 primeros numeros indican la x y la y del punto inferior derecho de ese mismo cuadrado
        self.canvas.create_arc(10,10,35,35, start=0,extent=angle,tags="progress", outline='green', width=4, style = tk.ARC) #start indica el punto en el que empieza a dibujarse la circunferencia, extent el tramo de circunferencia que dibujamos
        #tags el nombre que asociamos a este dibujo dentro del canvas, outline el color del arco que dibujamos, width el ancho del circulo, style=tk.ARC indica que pintaremos un arco


    def update_progress_circle(self):
        if self.progress < 100:
            self.progress += 14
        else:
            self.progress=0
        
        self.draw_progress_circle(self.progress)
        self.root.after(100, self.update_progress_circle) #Root after llama de nuevo a la función

    def feth_json_data(self):
        response= requests.get("https://raw.githubusercontent.com/ivangrovas/DI/main/recursos/catalog.json") #Consumimos el json alojado en nuestro repositorio de github
        if response.status_code ==200: #Comparamos que la respuesta del json sea exitosa
            self.json_data = response.json() #En ese caso guardamos el json en json_data
            self.finished=True

    #Comprobamos que la ejecución del hilo ha finalizado , en ese caso instanciaremos mainWindow
    def check_thread(self):
            if self.finished:
                self.root.destroy()
                launch_main_window(self.json_data)
            else:
                self.root.after(100, self.check_thread)

def launch_main_window(json_data):
    root = tk.Tk()
    app = MainWindow(root,json_data)
    root.mainloop()