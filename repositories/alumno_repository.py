from .base import BaseRepository
from models.alumno import Student

class StudentRepository(BaseRepository):
    
    def get_byMail(self ,mail) -> Student:
        query = 'SELECT * FROM students WHERE mail = %s'
        row = self.get_one( query, (mail))
        if row:
            return Student(*row)
        
    def get_by_career(self, career) ->list :
        query = 'SELECT * FROM alumnos WHERE career = %s'
        rows = self.get_all(query, (career))
        return [Student(*row) for row in rows ]
            
    def get_approved(self)-> list:  #alumnos con promedio aprovatorio( >= 6)
        pass
    
    def get_failed(self)-> list: #alumnos con promedio reprovatorio ( < 6)
        pass
    
    def get_excellent(self)->list: #alumnos con promedio de excelencia( > 9.4 ) 
        pass