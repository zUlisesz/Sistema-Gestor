from repositories.course_repository import CourseRepository

class AdminController:
    
    def __init__(self):
        self.rep_course = CourseRepository()
        
    def create_course(self, name, description, space, career ):
        query = 'INSERT INTO courses(name, description , space , carerr) VALUES (%s,%s,%s,%s)'
        self.rep_course.execute(query,(name, description,space, career)) 
        print('New course created successfully')
    
    def add_teacher(self , teacher):
        pass
    
    