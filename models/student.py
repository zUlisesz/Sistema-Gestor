#clase que hereda de la clase Usuario y únicamente almacena datos de un usuario cargado desde la bd para poder manipular la inf entre vistas
from .user import User

class Student(User):
    
    def __init__(self, id, name, mail, password, career, average:None ):
        super().__init__(id, name, mail, password)
        self.career = career
        self.average = average
        

    def show_myself(self):
        return super().show_myself() + f' - average: {self.average} - career: {self.career}'
    
              