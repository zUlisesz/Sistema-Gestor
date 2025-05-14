class User:
    def __init__(self, name, mail, password ):
        self.name = name
        self.mail = mail
        self.__password__ = password
        
    def show_myself(self):
        return f'{self.name} - {self.mail} - {self.__password__}'
    
    def set_name(self, new_name):
        self.name = new_name
        
    def set_password(self, new_password):
        self.__password__ = new_password 
        
    