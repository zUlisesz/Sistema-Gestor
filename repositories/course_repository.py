from .base import BaseRepository
from models.course import Course

class CourseRepository(BaseRepository):
    
    def get_all_courses(self):
        query = 'SELECT * FROM courses'
        rows = self.get_all(query,())
        return [Course(*row) for row in rows]
    
    