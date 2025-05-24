#esta es una clase padre para todos los típos de usuarios
#en general estas clase únicamente sirven para almacenar información de un usuario traido desde la bd y poder manipular la información entre vistas
class User:
    def __init__(self, id, name, mail, password ):
        self.id = id
        self.name = name
        self.mail = mail
        self.__password__ = password
        
    def show_myself(self):
        return f'id: {self.id} - {self.name} - {self.mail} - {self.__password__}'
    
    def set_name(self, new_name):
        self.name = new_name
        
    def set_password(self, new_password):
        self.__password__ = new_password 
        
    def get_password(self):
        return self.__password__
        
    