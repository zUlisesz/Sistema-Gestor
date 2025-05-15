from repositories.usuario_repository import UserRepository

class AuthController():
    
    def __init__(self):
        self.user_repository = UserRepository()
        
    def existing_user(self, mail):
        return True if self.user_repository.existing_mail(mail) else False
    
    def right_password(self, mail, password):
        if self.existing_user(mail):
            tupla = self.user_repository.get_mail_pass(mail)
            if tupla[1] == password:
                print('you`ve entered')
                return True
            else:
                print('wrong pasword')
            
 
    def redirecting(self, mail):
        if self.right_password(): 
            rol = self.user_repository.existing_mail(mail)
            if rol == 'student':
                print('directing to studnt view . . .')
            elif rol == 'teacher':
                print('directing to tecaher view . . . ')
            else:
                print('directing to admin view . . .')
        else:
            print('it seems you don´t have an account yet')
    
    