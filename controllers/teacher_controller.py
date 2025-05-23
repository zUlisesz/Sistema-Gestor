from repositories.user_repository import UserRepository
from repositories.course_repository import CourseRepository
class TeacherController:
    def __init__(self):
        self.user_repo = UserRepository()
        self.course_repo = CourseRepository()
        
    def create_teacher(self, mail):
        return self.user_repo.get_teacher_byMail(mail)
    
    def get_my_courses(self, teacher_id):
        return self.course_repo.get_courses_of(teacher_id)
        
    
    
    