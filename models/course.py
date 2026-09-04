"""Entidad de curso."""


class Course:
    def __init__(self, id, name, description, space, career, teacher=None):
        self.id_course = id
        self.name = name
        self.description = description
        self.space = space
        self.career = career
        self.teacher = teacher

    def show_myself(self):
        teacher = self.teacher or "Docente no asignado"
        return f"id: {self.id_course} - {self.name} - limit: {self.space} - career: {self.career} - teacher: {teacher}"
