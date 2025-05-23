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
        query = 'DELETE FROM gestor.courses WHERE id = %s'
        self.execute( query,(id_course,))
        
    def register_teacher(self, teacher_id , course_id):
        query = '''INSERT INTO gestor.teachers_courses(teacher_id, course_id)
        VALUES(%s , %s)'''
        self.execute(query, (teacher_id, course_id))
      
        
    def get_teacher_of_the_course(self, course_id):
        query = '''SELECT u.name
        FROM gestor.teachers_courses tc
        JOIN gestor.users u ON tc.teacher_id = u.id
        WHERE tc.course_id = %s;'''

        row = self.get_one(query, (course_id,))
        return row[0] if row else 'Docente no asignado'
    
    def get_courses_of(self, teacher_id):
        query  = '''SELECT c.id , c.name
        FROM gestor.teachers_courses tc
        JOIN courses c ON tc.course_id = c.id
        WHERE tc.teacher_id = %s;
        '''
        rows = self.get_all(query, (teacher_id,))
        return rows if rows else None
    
    

        
    
    
    