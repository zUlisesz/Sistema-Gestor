from repositories.course_repository import CourseRepository
from models.course import Course
class CourseController:
    def __init__(self):
        self.repo = CourseRepository()
        
    def create_course(self, id_course) -> Course:
        cs : Course = self.repo.get_course(id_course)
        return cs
    
    def names(self):
        return self.repo.get_names()
    
    def ids(self):
        return self.repo.get_ids()
    
    def make_course(self, name, description, space, career):
        self.repo.new_course(name ,description, space, career)
        
    def delete_course(self, id_course):
        self.repo.remove_course(id_course)
        
    def get_students_of(self, course_id):
        return self.repo.get_belongers_to(course_id)
    
    def get_post(self, course_id):
        return self.repo.get_notices(course_id)
        