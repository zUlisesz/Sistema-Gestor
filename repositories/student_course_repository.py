"""Persistencia de inscripciones de estudiantes en cursos."""

from .base import BaseRepository


class StudentCourseRepository(BaseRepository):
    def register_student(self, student_id, course_id):
        query = "INSERT INTO students_courses(student_id, course_id) VALUES (%s, %s)"
        return self.execute(query, (student_id, course_id))

    def look_for_student(self, id_student):
        return bool(self.get_one("SELECT id FROM users WHERE id = %s AND rol = %s", (id_student, "student")))

    def look_for_course(self, id_course):
        return bool(self.get_one("SELECT id FROM courses WHERE id = %s", (id_course,)))

    def course_name(self, id):
        row = self.get_one("SELECT name FROM courses WHERE id = %s", (id,))
        return row[0] if row else None

    def get_my_courses(self, id):
        query = """
            SELECT c.name
            FROM students_courses sc
            JOIN courses c ON sc.course_id = c.id
            WHERE sc.student_id = %s
        """
        return [row[0] for row in self.get_all(query, (id,))]

    def get_id_courses(self, id):
        query = """
            SELECT c.id
            FROM students_courses sc
            JOIN courses c ON sc.course_id = c.id
            WHERE sc.student_id = %s
        """
        return [row[0] for row in self.get_all(query, (id,))]

    def is_already_in(self, student_id, course_id):
        query = "SELECT 1 FROM students_courses WHERE student_id = %s AND course_id = %s LIMIT 1"
        return bool(self.get_one(query, (student_id, course_id)))

    def remove_student(self, student_id, course_id):
        query = "DELETE FROM students_courses WHERE student_id = %s AND course_id = %s"
        return self.execute(query, (student_id, course_id))

    def id_name(self):
        return self.get_all("SELECT id, name FROM courses ORDER BY name")
