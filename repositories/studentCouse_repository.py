from .base import BaseRepository
class StudentCourseRepository(BaseRepository):
    
    def register_student(self, student_id,course_id ):
        query = 'INSERT INTO gestor.students_courses(student_id,course_id) VALUES (%s, %s)'
        self.execute(query,(student_id, course_id) )
        
    def look_for_student(self, id_student):
        query = 'SELECT id from gestor.users WHERE id = %s'
        row =self.get_one(query,(id_student,))
        return bool(row)
    
    def look_for_course(self, id_course):
        query = 'SELECT id from gestor.courses WHERE id = %s'
        row = self.get_one(query,(id_course,))
        return bool(row)

    def course_name(self, id):
        query = 'SELECT name from gestor.courses WHERE id = %s'
        row = self.get_one(query, (id,))
        return row[0] if row else None
    
    def get_my_courses(self, id):
        query = '''SELECT c.name
        FROM students_courses sc
        JOIN courses c ON sc.course_id = c.id
        WHERE sc.student_id = %s;
        '''
        rows = self.get_all(query, (id,))
        return [row[0] for row in rows] if rows else None
    
    
    def get_id_courses(self, id):
        query  = '''SELECT c.id
        FROM students_courses sc
        JOIN courses c ON sc.course_id = c.id
        WHERE sc.student_id = %s;
        '''
        rows = self.get_all(query, (id,))
        return [row[0] for row in rows] if rows else None
    
    def is_already_in(self, student_id, course_id):
        query = 'SELECT * FROM gestor.students_courses WHERE student_id = %s AND course_id = %s'
        row = self.get_all(query, (student_id, course_id))
        return bool(row)
    
    def remove_student(self, student_id, course_id):
        query = '''DELETE from gestor.students_courses WHERE
        student_id = %s AND course_id = %s'''
        self.execute(query,(student_id, course_id))
        
        