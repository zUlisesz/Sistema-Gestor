from repositories.usuario_repository import UserRepository
import re
import bcrypt

class LoginController:
    def __init__(self):
        self.user_repository = UserRepository()
        
    def existing_user(self, mail):
        return bool(self.user_repository.existing_mail(mail))

    def is_password_correct(self, mail, password):
        if not self.existing_user(mail):
            print('Usuario no registrado en el sistema.')
            print('Por favor regístrate.')
            self.sign_up()
            return False

        tupla = self.user_repository.get_mail_pass(mail)
        if tupla is None:
            print("Error al recuperar los datos del usuario.")
            return False

        stored_hashed_password = tupla[1]

        if bcrypt.checkpw(password.encode(), stored_hashed_password.encode()):
            print('Acceso concedido')
            return True
        else:
            print('Contraseña incorrecta')
            return False

    def redirecting(self, mail):
        rol = self.user_repository.get_rol(mail)
        if rol == 'student':
            print('Redirigiendo a la vista de estudiante...')
        elif rol == 'teacher':
            print('Redirigiendo a la vista de profesor...')
        elif rol == 'admin':
            print('Redirigiendo a la vista de administrador...')
        else:
            print('Rol desconocido')

    def login(self):
        mail = input('Correo electrónico: \n')  
        password = input('Contraseña: \n') 
        
        if self.is_password_correct(mail, password):
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
        name = input('Nombre: \n')
        mail = input('Correo: \n')
        password = input('Contraseña (mínimo 8 caracteres): \n')
        rol = input('Rol (admin, student, teacher): \n')

        if self.correct_data(name, mail, password, rol):
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            query = 'INSERT INTO users(name, mail, password, rol) VALUES (%s, %s, %s, %s)'
            self.user_repository.execute(query, (name, mail, hashed_password, rol))
            print(f'Usuario registrado exitosamente.')
        else:
            print('Los datos proporcionados no son válidos.')
