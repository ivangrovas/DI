from io import BytesIO
from PIL import ImageTk, Image
import requests #Hacemos estos imports para trabajar con las imágenes 

class Cell: #Creamos la clase
    def __init__(self,title,url,desc) -> None: #Definimos el constructor de la clase al cuál le pasamos los parámetros correspondeintes
        #Asignamos los 3 valores que pasamos como parámetros al atributo
        self.title = title
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content))
        self.Image_tk = ImageTk.PhotoImage(img_data)
        self.desc = desc
    
        
 
