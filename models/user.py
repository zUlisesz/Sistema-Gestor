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
        
    