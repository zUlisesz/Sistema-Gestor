"""Consultas de estudiantes."""

from models.student import Student

from .base import BaseRepository


class StudentRepository(BaseRepository):
    STUDENT_COLUMNS = "u.id, u.name, u.mail, u.password, sd.career, sd.average"
    STUDENT_JOIN = "FROM users u JOIN student_data sd ON u.id = sd.user_id"

    def _students(self, condition="", parameters=()):
        query = f"SELECT {self.STUDENT_COLUMNS} {self.STUDENT_JOIN} {condition}"
        return [Student(*row) for row in self.get_all(query, parameters)]

    def get_by_career(self, career):
        return self._students("WHERE sd.career = %s", (career,))

    def get_approved(self):
        return self._students("WHERE sd.average >= 6")

    def get_failed(self):
        return self._students("WHERE sd.average < 6")

    def get_excellent(self):
        return self._students("WHERE sd.average > 9.4")

    def get_by_id(self, user_id):
        students = self._students("WHERE u.id = %s", (user_id,))
        return students[0] if students else None

    def get_by_mail(self, mail):
        students = self._students("WHERE u.mail = %s", (mail,))
        return students[0] if students else None

    def get_all_students(self):
        return self._students()

    def name_byMail(self, mail):
        row = self.get_one("SELECT name FROM users WHERE mail = %s", (mail,))
        return row[0] if row else None
