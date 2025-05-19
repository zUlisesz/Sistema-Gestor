from .base import BaseRepository
class StudentCourseRepository(BaseRepository):
    
    def register_student(self, student_id,course_id ):
        query = 'INSERT INTO gestor.students_courses VALUES (%s, %s)'
        self.execute(query,(student_id, course_id) )
        print('Alumno inscrito al curso')
        