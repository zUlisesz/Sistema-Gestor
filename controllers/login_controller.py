from repositories.user_repository import UserRepository
import re
import bcrypt

class LoginController:
    def __init__(self):
        self.user_repository = UserRepository()

    def existing_user(self, mail):
        return bool(self.user_repository.existing_mail(mail))

    def is_password_correct(self, mail, password):
        if not self.existing_user(mail):
            return False, "Usuario no registrado."

        user_data = self.user_repository.get_mail_pass(mail)
        if user_data is None:
            return False, "Error al recuperar los datos del usuario."

        stored_hashed_password = user_data[1]
        if bcrypt.checkpw(password.encode(), stored_hashed_password.encode()):
            return True, "Contraseña correcta"
        else:
            return False, "Contraseña incorrecta"

    def login(self, mail, password):
        """Devuelve (éxito, mensaje, rol)"""
        success, message = self.is_password_correct(mail, password)
        if success:
            rol = self.user_repository.get_rol(mail)
            return True, f"Inicio de sesión exitoso como {rol}", rol
        else:
            return False, message, None

    def correct_data(self, name, mail, password, rol):
        if not isinstance(name, str) or len(name.strip()) == 0:
            return False

        email_pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
        if not isinstance(mail, str) or not re.match(email_pattern, mail):
            return False

        if not isinstance(password, str) or len(password) < 8:
            return False

        allowed_roles = ['admin', 'student', 'teacher']
        if rol not in allowed_roles:
            return False

        return True

    def sign_up(self, name, mail, password, rol, career=None):
        """Devuelve (éxito, mensaje)"""
        if self.existing_user(mail):
            return False, "Usuario ya registrado."

        if self.correct_data(name, mail, password, rol):
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            query = 'INSERT INTO users(name, mail, password, rol) VALUES (%s, %s, %s, %s)'
            self.user_repository.execute(query, (name, mail, hashed_password, rol))

            if rol == 'student' and career:
                user_id = self.user_repository.get_id(mail)
                query = 'INSERT INTO student_data(user_id, career) VALUES (%s, %s)'
                self.user_repository.execute(query, (user_id, career))

            return True, "Usuario registrado exitosamente."
        else:
            return False, "Datos inválidos para el registro."
