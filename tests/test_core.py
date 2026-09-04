import unittest

from controllers.login_controller import LoginController
from controllers.student_controller import StudentController
from models.course import Course
from models.student import Student


class FakeUserRepository:
    def existing_mail(self, mail):
        return mail == "existente@example.com"


class FakeStudentRepository:
    def name_byMail(self, mail):
        return "Ana"

    def get_by_mail(self, mail):
        return Student(1, "Ana", mail, "hash", "Computacion")


class FakeStudentCourseRepository:
    def __init__(self):
        self.registered = []

    def is_already_in(self, student_id, course_id):
        return (student_id, course_id) in self.registered

    def look_for_course(self, course_id):
        return course_id == 10

    def look_for_student(self, student_id):
        return student_id == 1

    def register_student(self, student_id, course_id):
        self.registered.append((student_id, course_id))
        return 1

    def remove_student(self, student_id, course_id):
        return 1


class CoreTests(unittest.TestCase):
    def test_user_display_never_exposes_password(self):
        student = Student(1, "Ana", "ana@example.com", "hash-secreto", "Computacion")
        self.assertNotIn("hash-secreto", student.show_myself())

    def test_course_has_safe_default_teacher(self):
        course = Course(10, "Python", "Curso base", 30, "Computacion")
        self.assertIn("Docente no asignado", course.show_myself())

    def test_login_validation_is_independent_from_database(self):
        controller = LoginController(FakeUserRepository())
        self.assertTrue(controller.correct_data("Ana", "ana@example.com", "secreto123", "student"))
        self.assertFalse(controller.correct_data(" ", "ana@example.com", "secreto123", "student"))
        self.assertFalse(controller.correct_data("Ana", "correo-invalido", "secreto123", "student"))
        self.assertFalse(controller.existing_user("nueva@example.com"))

    def test_student_registration_returns_boolean(self):
        courses = FakeStudentCourseRepository()
        controller = StudentController(FakeStudentRepository(), courses)
        self.assertTrue(controller.enter_to_course(1, 10))
        self.assertFalse(controller.enter_to_course(1, 10))
        self.assertFalse(controller.enter_to_course("1", 10))


if __name__ == "__main__":
    unittest.main()
