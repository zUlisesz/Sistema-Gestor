"""Consultas y comandos relacionados con cursos."""

from datetime import date

from models.course import Course

from .base import BaseRepository


class CourseRepository(BaseRepository):
    COURSE_COLUMNS = "id, name, description, space, career"

    def get_courses_as_instance(self):
        rows = self.get_all(f"SELECT {self.COURSE_COLUMNS} FROM courses")
        return [Course(*row) for row in rows]

    def get_courses_as_tuples(self):
        return self.get_all(f"SELECT {self.COURSE_COLUMNS} FROM courses")

    def get_summaries(self):
        return self.get_all("SELECT id, name FROM courses")

    def get_names(self):
        return [row[1] for row in self.get_summaries()]

    def get_ids(self):
        return [row[0] for row in self.get_summaries()]

    def get_course(self, id_course):
        row = self.get_one(f"SELECT {self.COURSE_COLUMNS} FROM courses WHERE id = %s", (id_course,))
        return Course(*row) if row else None

    def new_course(self, name, description, space, career):
        query = "INSERT INTO courses(name, description, space, career) VALUES (%s, %s, %s, %s)"
        return self.execute(query, (name, description, space, career))

    def remove_course(self, id_course):
        return self.execute("DELETE FROM courses WHERE id = %s", (id_course,))

    def register_teacher(self, teacher_id, course_id):
        query = "INSERT INTO teachers_courses(teacher_id, course_id) VALUES (%s, %s)"
        return self.execute(query, (teacher_id, course_id))

    def get_teacher_of_the_course(self, course_id):
        query = """
            SELECT u.name
            FROM teachers_courses tc
            JOIN users u ON tc.teacher_id = u.id
            WHERE tc.course_id = %s
            LIMIT 1
        """
        row = self.get_one(query, (course_id,))
        return row[0] if row else "Docente no asignado"

    def get_courses_of(self, teacher_id):
        query = """
            SELECT c.id, c.name
            FROM teachers_courses tc
            JOIN courses c ON tc.course_id = c.id
            WHERE tc.teacher_id = %s
        """
        return self.get_all(query, (teacher_id,))

    def get_belongers_to(self, course_id):
        query = """
            SELECT u.id, u.name, u.mail, sd.career
            FROM students_courses sc
            JOIN users u ON sc.student_id = u.id
            JOIN student_data sd ON u.id = sd.user_id
            WHERE sc.course_id = %s
        """
        return self.get_all(query, (course_id,))

    def insert_post(self, name, content, course_id):
        query = "INSERT INTO notices(name, content, course_id, date) VALUES (%s, %s, %s, %s)"
        return self.execute(query, (name, content, course_id, date.today()))

    def get_notices(self, course_id):
        query = "SELECT name, date, content FROM notices WHERE course_id = %s ORDER BY date DESC"
        return self.get_all(query, (course_id,))
