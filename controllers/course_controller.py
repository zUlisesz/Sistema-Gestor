from repositories.course_repository import CourseRepository
from models.course import Course
class CourseController:
    def __init__(self):
        self.repo = CourseRepository()
        
    def create_course(self, id_course) -> Course:
        cs : Course = self.repo.get_course(id_course)
        return cs