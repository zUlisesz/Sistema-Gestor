"""Casos de uso exclusivos del administrador."""

from repositories.course_repository import CourseRepository
from repositories.user_repository import UserRepository


class AdminController:
    def __init__(self, course_repository=None, user_repository=None):
        self.rep_course = course_repository if course_repository is not None else CourseRepository()
        self.user_repo = user_repository if user_repository is not None else UserRepository()

    def create_course(self, name, description, space, career):
        return self.rep_course.new_course(name, description, space, career)

    def assign_teacher(self, teacher_id, course_id):
        return self.rep_course.register_teacher(teacher_id, course_id)

    def check_teachers(self):
        return self.user_repo.get_teachers_names()

    def create_admin(self, mail):
        return self.user_repo.get_admin_byMail(mail)

    def get_courses_teacher(self, course_id):
        return self.rep_course.get_teacher_of_the_course(course_id)

    def get_all(self):
        return self.user_repo.get_all_users()
