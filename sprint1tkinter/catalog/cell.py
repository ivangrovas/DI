from PIL import ImageTk

class Cell:
    def __init__(self,title,path) -> None:
        self.title = title
        self.path = path
        self.image_tk = ImageTk.PhotoImage(file=self.path)