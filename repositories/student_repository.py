from .base import BaseRepository
from models.student import Student

class StudentRepository(BaseRepository):

    def get_by_career(self, career) -> list:
        query = """
            SELECT u.id, u.name, u.mail,u.password, sd.career, sd.average
            FROM users u
            JOIN student_data sd ON u.id = sd.user_id
            WHERE sd.career = %s
        """
        rows = self.get_all(query, (career,))
        return [Student(*row) for row in rows]

    def get_approved(self) -> list:
        query = """
            SELECT u.id, u.name, u.mail,u.password, sd.career, sd.average
            FROM users u
            JOIN student_data sd ON u.id = sd.user_id
            WHERE sd.average >= 6
        """
        rows = self.get_all(query)
        return [Student(*row) for row in rows]

    def get_failed(self) -> list:
        query = """
            SELECT u.id, u.name, u.mail,u.password, sd.career, sd.average
            FROM users u
            JOIN student_data sd ON u.id = sd.user_id
            WHERE sd.average < 6
        """
        rows = self.get_all(query)
        return [Student(*row) for row in rows]

    def get_excellent(self) -> list:
        query = """
            SELECT u.id, u.name, u.mail,u.password, sd.career, sd.average
            FROM users u
            JOIN student_data sd ON u.id = sd.user_id
            WHERE sd.average > 9.4
        """
        rows = self.get_all(query)
        return [Student(*row) for row in rows]

    def get_by_id(self, user_id) -> Student | None: #rhis method returns onely one row
        query = """
            SELECT u.id, u.name, u.mail,password, sd.career, sd.average
            FROM users u
            JOIN student_data sd ON u.id = sd.user_id
            WHERE u.id = %s
        """
        row = self.get_one(query, (user_id,))
        return Student(*row) if row else None 
    
    def get_by_mail(self, mail) -> Student | None: #rhis method returns onely one row
        query = """
            SELECT u.id, u.name, u.mail,password, sd.career, sd.average
            FROM users u
            JOIN student_data sd ON u.id = sd.user_id
            WHERE u.mail = %s
        """
        
        row = self.get_one(query, (mail,))
        return Student(*row) if row else None 

    def get_all_students(self) -> list:
        query = """
            SELECT u.id, u.name, u.mail,password, sd.career, sd.average
            FROM users u
            JOIN student_data sd ON u.id = sd.user_id
        """
        rows = self.get_all(query)
        return [Student(*row) for row in rows]
    
    
    def name_byMail(self, mail):
        
        query = 'SELECT name FROM gestor.users WHERE mail = %s'
        row = self.get_one(query, (mail,))
        return row[0]
     

