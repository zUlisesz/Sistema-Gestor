from .base import BaseRepository
class StudentCourseRepository(BaseRepository):
    
    def register_student(self, student_id,course_id ):
        query = 'INSERT INTO gestor.students_courses VALUES (%s, %s)'
        self.execute(query,(student_id, course_id) )
        print('Alumno inscrito al curso')
        
    def look_for_student(self, id_student):
        query = 'SELECT id from gestor.users WHERE id = %s'
        row =self.get_one(query,(id_student,))
        return bool(row)
    
    def look_for_course(self, id_course):
        query = 'SELECT id from gestor.courses WHERE id = %s'
        row = self.get_one(query,(id_course,))
        return bool(row)
    
    