from .base import BaseRepository
from models.teacher import Teacher
from models.administrador import Admin

class UserRepository(BaseRepository):

    def get_mail_pass(self, mail):
        query = "SELECT mail, password FROM users WHERE mail = %s"
        row = self.get_one(query, (mail,))
        return row if row else None
    
    def get_id(self, mail):
        query = 'SELECT id from users WHERE mail = %s'
        row = self.get_one(query,(mail,))
        return row[0] if row else None

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

    def get_teacher_byMail(self, mail) -> Teacher:
        query = "SELECT id,name, mail, password FROM users WHERE mail = %s AND rol = %s"
        row = self.get_one(query, (mail, 'teacher'))
        return Teacher(*row) if row else None
    
    def get_admin_byMail(self, mail) -> Admin:
        query = "SELECT id,name, mail, password FROM users WHERE mail = %s AND rol = %s"
        row = self.get_one(query, (mail, 'admin'))
        return Admin(*row) if row else None
