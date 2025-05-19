from repositories.student_repository import StudentRepository
from repositories.studentCouse_repository import StudentCourseRepository
class StudentController:
    
    def __init__(self):
        self.student_repository = StudentRepository()
        self.student_course = StudentCourseRepository()
        
    def enter_to_course(self, id_student ,id_course):
        self.student_course.register_student(id_student, id_course)
        
    
        
        