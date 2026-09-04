"""Casos de uso de autenticacion y registro."""

import re

from repositories.user_repository import UserRepository


class LoginController:
    EMAIL_PATTERN = re.compile(r"^[\w.\-+]+@[\w.\-]+\.[A-Za-z]{2,}$")
    ALLOWED_ROLES = {"admin", "student", "teacher"}

    def __init__(self, user_repository=None):
        self.user_repository = user_repository if user_repository is not None else UserRepository()

    @staticmethod
    def _bcrypt():
        try:
            import bcrypt
        except ModuleNotFoundError as error:
            raise RuntimeError("Falta la dependencia bcrypt. Instala requirements.txt.") from error
        return bcrypt

    def existing_user(self, mail):
        return self.user_repository.existing_mail(mail.strip().lower())

    def is_password_correct(self, mail, password):
        normalized_mail = mail.strip().lower()
        if not self.existing_user(normalized_mail):
            return False, "Usuario no registrado. Crea una cuenta antes de iniciar sesion."
        user_data = self.user_repository.get_mail_pass(normalized_mail)
        if not user_data:
            return False, "Error al recuperar los datos del usuario."
        bcrypt = self._bcrypt()
        stored_password = user_data[1]
        stored_password = stored_password.encode() if isinstance(stored_password, str) else stored_password
        valid = bcrypt.checkpw(password.encode(), stored_password)
        return (True, "Contrasena correcta") if valid else (False, "Contrasena incorrecta")

    def login(self, mail, password):
        success, message = self.is_password_correct(mail, password)
        if not success:
            return False, message, None
        role = self.user_repository.get_rol(mail.strip().lower())
        return True, f"Inicio de sesion exitoso como {role}", role

    def correct_data(self, name, mail, password, rol):
        return (
            isinstance(name, str)
            and bool(name.strip())
            and isinstance(mail, str)
            and bool(self.EMAIL_PATTERN.fullmatch(mail.strip()))
            and isinstance(password, str)
            and len(password) >= 8
            and rol in self.ALLOWED_ROLES
        )

    def sign_up(self, name, mail, password, rol, career=None):
        if not self.correct_data(name, mail, password, rol):
            return False, "Datos invalidos para el registro."
        if rol == "student" and (not isinstance(career, str) or not career.strip()):
            return False, "La carrera es obligatoria para estudiantes."

        normalized_mail = mail.strip().lower()
        if self.existing_user(normalized_mail):
            return False, "Usuario ya registrado."

        bcrypt = self._bcrypt()
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        self.user_repository.execute(
            "INSERT INTO users(name, mail, password, rol) VALUES (%s, %s, %s, %s)",
            (name.strip(), normalized_mail, hashed_password, rol),
        )
        if rol == "student":
            user_id = self.user_repository.get_id(normalized_mail)
            self.user_repository.execute(
                "INSERT INTO student_data(user_id, career) VALUES (%s, %s)",
                (user_id, career.strip()),
            )
        return True, "Usuario registrado exitosamente."
