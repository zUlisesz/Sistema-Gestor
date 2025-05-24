#clase que hereda de la clase Usuario y únicamente almacena datos de un usuario cargado desde la bd para poder manipular la inf entre vistas
from .user import User

class Teacher(User):
    
    def __init__(self, id, name, mail, password):
        super().__init__(id, name, mail, password)
        
    
    