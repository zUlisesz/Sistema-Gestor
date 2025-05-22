from .base import BaseRepository
from models.course import Course

class CourseRepository(BaseRepository):
    
    def get_all_courses(self):
        query = 'SELECT * FROM courses'
        rows = self.get_all(query,())
        return [Course(*row) for row in rows]
    
    def get_course(self, id_course):
        query = 'SELECT  * FROM gestor.courses WHERE id = %s'
        row = self.get_all(query, (id_course,))
        return row if row else None
    
    