from .base import BaseRepository
from models.course import Course

class CourseRepository(BaseRepository):
    
    def get_all_courses(self):
        query = 'SELECT * FROM courses'
        rows = self.get_all(query,())
        return [Course(*row) for row in rows]
    
    def get_course(self, id_course)->Course:
        query = 'SELECT  * FROM gestor.courses WHERE id = %s'
        row = self.get_one(query, (id_course,))
        return Course(*row) if row else None
    
    