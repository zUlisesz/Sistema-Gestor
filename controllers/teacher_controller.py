#dentro de las clases controladoras se comunican las vistas con los repositorios
#los controladores recibe datos de las vitas , algunas hacen operaciones
#además estos controladores logran usan las clases de repositorios para mostrar info a través de las vistas
#en general estos constructores son mediadores entre las vistas y los modelos y repositorios
from repositories.user_repository import UserRepository
from repositories.course_repository import CourseRepository
class TeacherController:
    def __init__(self):
        self.user_repo = UserRepository()
        self.course_repo = CourseRepository()
        
    def create_teacher(self, mail):
        return self.user_repo.get_teacher_byMail(mail)
    
    def get_my_courses_name(self, teacher_id):
        return [row[0] for row in self.course_repo.get_courses_of(teacher_id)]
    
    def get_my_courses_id(self, teacher_id):
        return [row[1] for row in self.course_repo.get_courses_of(teacher_id)]
    
    def get_my_info_courses(self, teacher_id):
        return self.course_repo.get_courses_of(teacher_id)
    
    def make_post( self , name, content, course_id):
        self.course_repo.insert_post(name, content, course_id)
        
    
    
    