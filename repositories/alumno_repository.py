from .base import BaseRepository
from models.alumno import Student

class StudentRepository(BaseRepository):
    
    def existing_student(self, mail):
        query = 'SELECT name FROM students_ WHERE mail = %s'
        row = self.get_one(query,(mail,)) 
        return row[0] if row else None
    
    def get_byMail(self ,mail) -> Student:
        query = 'SELECT * FROM students_ WHERE mail = %s'
        row = self.get_one( query, (mail))
        if row:
            return Student(*row)
        
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