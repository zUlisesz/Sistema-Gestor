"""Consultas de usuarios y construccion de entidades por rol."""

from models.administrador import Admin
from models.teacher import Teacher

from .base import BaseRepository


class UserRepository(BaseRepository):
    def get_mail_pass(self, mail):
        return self.get_one("SELECT mail, password FROM users WHERE mail = %s", (mail,))

    def get_id(self, mail):
        row = self.get_one("SELECT id FROM users WHERE mail = %s", (mail,))
        return row[0] if row else None

    def existing_mail(self, mail):
        return bool(self.get_one("SELECT 1 FROM users WHERE mail = %s LIMIT 1", (mail,)))

    def get_rol(self, mail):
        row = self.get_one("SELECT rol FROM users WHERE mail = %s", (mail,))
        return row[0] if row else None

    def get_all_users(self):
        """No devuelve hashes de contrasena a la interfaz de administracion."""
        return self.get_all("SELECT id, name, mail, rol FROM users")

    def get_teachers_names(self):
        rows = self.get_all("SELECT name, id FROM users WHERE rol = %s ORDER BY name", ("teacher",))
        return [f"{row[1]} - {row[0]}" for row in rows]

    def get_teacher_byMail(self, mail):
        row = self.get_one(
            "SELECT id, name, mail, password FROM users WHERE mail = %s AND rol = %s",
            (mail, "teacher"),
        )
        return Teacher(*row) if row else None

    def get_admin_byMail(self, mail):
        row = self.get_one(
            "SELECT id, name, mail, password FROM users WHERE mail = %s AND rol = %s",
            (mail, "admin"),
        )
        return Admin(*row) if row else None
