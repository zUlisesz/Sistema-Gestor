from repositories.usuario_repository import UserRepository

class AuthController():
    
    def __init__(self):
        self.user_repository = UserRepository()
        
    def existing_user(self, mail):
        if self.user_repository.existing_mail(mail): 
            rol = self.user_repository.existing_mail(mail)
            if rol == 'student':
                print('directing to studnt view . . .')
            elif rol == 'teacher':
                print('directing to tecaher view . . . ')
            else:
                print('directing to admin view . . .')
        else:
            print('it seems you don´t have an account yet')
    
    