from .base import BaseRepository
from models.profesor import Teacher
from models.alumno import Student

class UserRepository(BaseRepository):

    def get_mail_pass(self, mail):
        query = "SELECT mail, password FROM users WHERE mail = %s"
        row = self.get_one(query, (mail,))
        return row if row else None

    def existing_mail(self, mail):
        query = "SELECT 1 FROM users WHERE mail = %s"
        row = self.get_one(query, (mail,))
        return bool(row)

    def get_rol(self, mail):
        query = "SELECT rol FROM users WHERE mail = %s"
        row = self.get_one(query, (mail,))
        return row[0] if row else None

    def get_all_users(self):
        query = "SELECT * FROM users"
        rows = self.get_all(query)
        return rows

    def get_teachers(self) -> list:
        query = "SELECT * FROM users WHERE rol = %s"
        rows = self.get_all(query, ('teacher',))
        return [Teacher(*row) for row in rows]

    def get_by_mail(self, mail) -> Teacher:
        query = "SELECT * FROM users WHERE mail = %s AND rol = %s"
        row = self.get_one(query, (mail, 'teacher'))
        return Teacher(*row) if row else None

    # Métodos para la tabla de estudiantes - - -  Fantan correcciones en la bd

    def get_by_career(self, career) -> list:
        query = "SELECT * FROM students_ WHERE career = %s"
        rows = self.get_all(query, (career,))
        return [Student(*row) for row in rows]

    def get_approved(self) -> list:
        query = "SELECT * FROM students_ WHERE average >= 6"
        rows = self.get_all(query)
        return [Student(*row) for row in rows]

    def get_failed(self) -> list:
        query = "SELECT * FROM students_ WHERE average < 6"
        rows = self.get_all(query)
        return [Student(*row) for row in rows]

    def get_excellent(self) -> list:
        query = "SELECT * FROM students_ WHERE average > 9.4"
        rows = self.get_all(query)
        return [Student(*row) for row in rows]
