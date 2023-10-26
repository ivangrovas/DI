import tkinter as tk
import threading
import requests

class LoadingWindow:
    
    #words.json
    json_data = []

    #Booleano para controlar la descarga de datos del JSON
    finished=False
    
    def __init__(self,root) -> None:

        self.root = root
        self.root.title ("EL JUEGO DEL AHORCADO")

        #Ajustamos las dimensiones de la ventana
        x = (self.root.winfo_screenwidth()- self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight()- self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")

        #Especificamos las diemsniones exactas de la ventana y negamos la posibilidad de reedimensión
        self.root.geometry("170x120")
        self.root.resizable (False, False)

        #Informamos al usuario de lo que está haciendo el programa en este momento
        self.label = tk.Label (self.root, text="Cargando el juego...", font=("Arial", 14))
        self.label.pack(side=tk.TOP, pady=10)

        label_bg_color = self.label.cget("bg")

        #Creamos un canvas para la circunferencia referente al proceso de carga
        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color) #Pasamos el ancho y alto del mismo, así como el color de fondo el cuál obtuvimos con el metodo cget
        self.canvas.pack()

        self.progress = 0
        self.update_progress_circle()

        #Realizamos la petición HTTP del json que aloja las palabras
        #self.thread = threading.Thread(target=self.feth_json_data)
        #self.thread.start()

        #Comprobamos la actividad del hilo
        #if self.thread.is_alive():
        #    self.check_thread()
    
    #Dibujamos la circunferencia
    def draw_progress_circle(self,progress):
        self.canvas.delete("progress")
        angle = int (360 * (progress/100))
        self.canvas.create_arc(10,10,35,35, start=0,extent=angle,tags="progress", outline='red', width=4, style = tk.ARC) #start indica el punto en el que empieza a dibujarse la circunferencia, extent el tramo de circunferencia que dibujamos
        
    #Actualizamos la circunferencia
    def update_progress_circle(self):
        if self.progress < 100:
            self.progress += 14
        else:
            self.progress=0
        
        self.draw_progress_circle(self.progress)
        self.root.after(100, self.update_progress_circle)
    
    #Hacemos la descarga de datos del JSON
    def feth_json_data(self):
        response= requests.get("https://raw.githubusercontent.com/ivangrovas/DI/main/recursos/words.json") #Consumimos el json alojado en nuestro repositorio de github
        if response.status_code ==200: #Comparamos que la respuesta del json sea exitosa
            self.json_data = response.json() #En ese caso guardamos el json en json_data
            self.finished=True

    #Comprobamos si ha finalizado la ejecución del hilo   
    def check_thread(self):
            if self.finished:
                self.root.destroy()
                #start game window ( [!!!!!!!] FOR DEVELOPER )
            else:
                self.root.after(100, self.check_thread)

#def game window (FOR DEVELOPER)