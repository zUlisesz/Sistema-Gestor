from repositories.usuario_repository import UserRepository

class LoginController():
    
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
        
        print('user not in the system')
        return False
            
    def redirecting(self, mail):
        rol = self.user_repository.get_rol(mail)
        if rol == 'student':
            print('directing to student view . . .')
        elif rol == 'teacher':
            print('directing to teacher view . . . ')
        else:
            print('directing to admin view . . .')
            
    def login(self):
        mail  = input('Insert your email: \n')  
        password = input('Type your password: \n') 
        
        if self.right_password(mail, password):
            self.redirecting(mail)
 