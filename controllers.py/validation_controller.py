from repositories.usuario_repository import UserRepository

class AuthController():
    
    def __init__(self):
        self.user_repository = UserRepository()
        
    def existing_user(self, mail):
        return True if mail in self.user_repository.get_usersMail() else False
    
    
            