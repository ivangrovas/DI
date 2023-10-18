from PIL import ImageTk, Image #Hacemos estos imports para trabajar con las imágenes 

class Cell: #Creamos la clase
    def __init__(self,title,path,desc) -> None: #Definimos el constructor de la clase al cuál le pasamos los parámetros self,title, path y desc
        #Asignamos los 3 valores que pasamos como parámetros al atributo
        self.title = title
        self.path = path
        self.desc = desc
        img = Image.open(self.path) #Abrimos la imágen con Image.open de la ruta de self.path y la cuardamos en una variable
        img1 = img.resize((100,100),Image.LANCZOS) #Redimensionamos la imágen  con el método resize y la guardamos en otra variable
        self.image_tk = ImageTk.PhotoImage(img1) #Mostramos la imágen en pantalla.

 
