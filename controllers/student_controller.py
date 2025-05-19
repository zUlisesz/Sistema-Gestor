from repositories.student_repository import StudentRepository
from repositories.studentCouse_repository import StudentCourseRepository
class StudentController:
    
    def __init__(self):
        self.student_repository = StudentRepository()
        self.student_course = StudentCourseRepository()
        
    def enter_to_course(self, id_student ,id_course):
        if self.check_info() :
            self.student_course.register_student(id_student, id_course)
        
    def check_info(self, id_student_field, id_course_field):
        if not id_course_field == '' or id_student_field == '':
            if isinstance(id_student_field,int) and isinstance(id_course_field,int):
                return True
        
        return False, 'Parece que tus datos no fueron correctamente escritos '
        
        
        