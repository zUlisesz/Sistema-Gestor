from repositories.course_repository import CourseRepository
from repositories.user_repository import UserRepository

class AdminController:
    
    def __init__(self):
        self.rep_course = CourseRepository()
        self.user_repo = UserRepository()
        
    def create_course(self, name, description, space, career ):
        query = 'INSERT INTO courses(name, description , space , carerr) VALUES (%s,%s,%s,%s)'
        self.rep_course.execute(query,(name, description,space, career)) 
        print('New course created successfully')
    
    def assign_teacher(self, teacher_id, course_id):
        self.rep_course.register_teacher(teacher_id, course_id)
       
    def check_teachers(self):
        return self.user_repo.get_teachers_names()
    
    def create_admin(self,mail):
        return self.user_repo.get_admin_byMail(mail)
    
    
    
    