from .base import BaseRepository
from models.course import Course

class CourseRepository(BaseRepository):
    
    def get_courses_as_instance(self):
        query = 'SELECT * FROM courses'
        rows = self.get_all(query,())
        return [Course(*row) for row in rows]
    
    def get_courses_as_tuples(self):
        query = 'SELECT * FROM gestor.courses'
        rows = self.get_all(query,())
        return rows if rows else None
    
    def get_names(self):
        query = 'SELECT name FROM gestor.courses'
        rows = self.get_all(query,())
        return [row[0] for row in rows] if rows else None
    
    def get_ids(self):
        query = 'SELECT id FROM gestor.courses'
        rows = self.get_all(query,())
        return [row[0] for row in rows] if rows else None
    
    def get_course(self, id_course)->Course:
        query = 'SELECT  * FROM gestor.courses WHERE id = %s'
        row = self.get_one(query, (id_course,))
        return Course(*row) if row else None
    
    def new_course(self, name ,description, space, career):
        query = '''INSERT INTO gestor.courses(name, description, space, career)
        VALUES( %s, %s, %s, %s)'''
        self.execute(query,(name, description, space, career))
        
    def remove_course(self, id_course):
        query = 'DELETE FROM gestor.course WHERE id = %s'
        self.execute( query,(id_course))
        
    
    
    