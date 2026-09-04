"""Casos de uso disponibles para profesores."""

from repositories.course_repository import CourseRepository
from repositories.user_repository import UserRepository


class TeacherController:
    def __init__(self, user_repository=None, course_repository=None):
        self.user_repo = user_repository if user_repository is not None else UserRepository()
        self.course_repo = course_repository if course_repository is not None else CourseRepository()

    def create_teacher(self, mail):
        return self.user_repo.get_teacher_byMail(mail)

    def get_my_courses_name(self, teacher_id):
        return [row[1] for row in self.course_repo.get_courses_of(teacher_id)]

    def get_my_courses_id(self, teacher_id):
        return [row[0] for row in self.course_repo.get_courses_of(teacher_id)]

    def get_my_info_courses(self, teacher_id):
        return self.course_repo.get_courses_of(teacher_id)

    def make_post(self, name, content, course_id):
        return self.course_repo.insert_post(name.strip(), content.strip(), course_id)
