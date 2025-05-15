from .base import BaseRepository
from models.profesor import Teacher
from models.alumno import Student

class UserRepository(BaseRepository):
    
    def get_mail_pass(self, mail) :
        query = "SELECT mail,password FROM users WHERE mail = %s"
        rows = self.get_one(query, (mail,))
        return rows if rows is not None else None
    
    def existing_mail(self, mail):
        query = "SELECT * FROM users WHERE mail = %s"
        row  = self.get_one(query, (mail,))
        return row[0] if row is not None else None
    
    def get_rol(self, mail):
        query = "SELECT rol FROM users WHERE mail = %s"
        row = self.get_one(query, (mail,))
        return row[0]
    
    #methods for the teachers table
    def get_teachers(self) -> list:
        query = "SELECET * FROM users WHERE rol = %s"
        rows = self.get_all(query, ())
        return [Teacher(*row) for row in rows]
    
    def get_byMail(self, mail) ->Teacher: # 1 
        query = 'SELECT * FROM teachers WHERE mail = %s'
        row = self.get_one(query, (mail))
        if row:
            return Teacher(*row)
        
    #methods for the students table
        
    def get_by_career(self, career) ->list :
        query = 'SELECT * FROM students_ WHERE career = %s'
        rows = self.get_all(query, (career))
        return [Student(*row) for row in rows ]
            
    def get_approved(self)-> list:  #alumnos con promedio aprovatorio( >= 6)
        pass
    
    def get_failed(self)-> list: #alumnos con promedio reprovatorio ( < 6)
        pass
    
    def get_excellent(self)->list: #alumnos con promedio de excelencia( > 9.4 ) 
        pass