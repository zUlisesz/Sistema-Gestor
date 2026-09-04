"""Casos de uso disponibles para estudiantes."""

from models.student import Student
from repositories.student_course_repository import StudentCourseRepository
from repositories.student_repository import StudentRepository


class StudentController:
    def __init__(self, student_repository=None, student_course=None):
        self.student_repository = student_repository if student_repository is not None else StudentRepository()
        self.student_course = student_course if student_course is not None else StudentCourseRepository()

    def enter_to_course(self, id_student, id_course):
        if not self.check_info(id_student, id_course):
            return False
        if self.student_course.is_already_in(id_student, id_course):
            return False
        if not self.student_course.look_for_course(id_course) or not self.student_course.look_for_student(id_student):
            return False
        return bool(self.student_course.register_student(id_student, id_course))

    def get_course(self, id):
        return self.student_course.course_name(id)

    @staticmethod
    def check_info(id_student_field, id_course_field):
        return (
            isinstance(id_student_field, int)
            and not isinstance(id_student_field, bool)
            and isinstance(id_course_field, int)
            and not isinstance(id_course_field, bool)
            and id_student_field > 0
            and id_course_field > 0
        )

    def get_student(self, mail):
        return self.student_repository.name_byMail(mail)

    def create_student(self, mail) -> Student | None:
        return self.student_repository.get_by_mail(mail)

    def get_courses_name(self, id):
        return self.student_course.get_my_courses(id)

    def get_courses_id(self, id):
        return self.student_course.get_id_courses(id)

    def leave_course(self, student_id, course_id):
        return self.student_course.remove_student(student_id, course_id)

    def get_available_courses(self):
        return self.student_course.id_name()
