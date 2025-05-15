from repositories.usuario_repository import UserRepository
import re

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
                return False
        
        print('user not in the system')
        print('Sign up')
        self.sign_up()
            
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
          
    def correct_data(self, name, mail, password, rol):
    
        if not isinstance(name, str) or len(name.strip()) == 0:
            return False
        
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
        if not isinstance(mail, str) or not re.match(email_pattern, mail):
            return False
        
        if not isinstance(password, str) or len(password) < 8:
            return False
        
        allowed_roles = ['admin', 'student', 'teacher'] 
        if not isinstance(rol, str) or rol not in allowed_roles:
            return False
    
        return True
  
    def sign_up(self):
        query =  'INSERT INTO users(name, mail, password, rol) VALUES (%s , %s , %s, %s)'
        name = input('Name: \n')
        mail = input('Mail: \n')
        password = input('Password: \n')
        rol = input('Rol: \n')
        
        if self.correct_data(name ,mail ,password, rol):
            self.user_repository.execute(query, (name,mail,password,rol))
            print('user added successfully')
        else:
            print('It seems that you did`t type the correct data')
            
 