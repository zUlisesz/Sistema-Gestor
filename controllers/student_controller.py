from repositories.student_repository import StudentRepository
from repositories.studentCouse_repository import StudentCourseRepository
from models.student import Student

class StudentController:

    def __init__(self):
        self.student_repository = StudentRepository()
        self.student_course = StudentCourseRepository()

    def enter_to_course(self, id_student, id_course):
        if self.check_info(id_student, id_course):
            if self.student_course.look_for_course(id_course) and self.student_course.look_for_student(id_student):
                try:
                    self.student_course.register_student(id_student, id_course)
                except:
                    print('EL usuario ya ha sido agregado a este curso')
            else:
                print('IDs no existentes')
        else:
            print('Datos ingresados incorrectamente')
            
    def get_course(self,id):
        return self.student_course.course_name(id)

    def check_info(self, id_student_field, id_course_field):
        if isinstance(id_student_field, int) and isinstance(id_course_field, int):
            return True
        return False
    
    def get_student(self,mail):
        return self.student_repository.name_byMail(mail)
    
    def create_student(self,mail) -> Student:
        std: Student = self.student_repository.get_by_mail(mail)
        return std
    
    def get_courses_name(self,id):
        return self.student_course.get_my_courses(id)
    
    def get_courses_id(self, id ):
        return self.student_course.get_id_courses(id)
        

        
        
        