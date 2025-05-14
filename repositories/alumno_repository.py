from .base import BaseRepository
from models.alumno import Student

class StudentRepository(BaseRepository):
    
    def get_byMail(self ,mail) -> Student:
        query = 'SELECT * FROM students WHERE mail = %s'
        row = self.get_one( query, (mail))
        if row:
            return Student(*row)
        
    def get_by_career(self, career): # >= 1
        query = 'SELECT * FROM alumnos WHERE career = %s'
        rows = self.get_all(query, (career))
        return [Student(*row) for row in rows ]
            
    
        
        