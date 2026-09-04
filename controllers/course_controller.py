"""Casos de uso de consulta y mantenimiento de cursos."""

from repositories.course_repository import CourseRepository


class CourseController:
    def __init__(self, repository=None):
        self.repo = repository if repository is not None else CourseRepository()

    def create_course(self, id_course):
        return self.repo.get_course(id_course)

    def names(self):
        return self.repo.get_names()

    def ids(self):
        return self.repo.get_ids()

    def summaries(self):
        return self.repo.get_summaries()

    def make_course(self, name, description, space, career):
        return self.repo.new_course(name.strip(), description.strip(), space, career)

    def delete_course(self, id_course):
        return self.repo.remove_course(id_course)

    def get_students_of(self, course_id):
        return self.repo.get_belongers_to(course_id)

    def get_post(self, course_id):
        return self.repo.get_notices(course_id)
