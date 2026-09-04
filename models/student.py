"""Entidad de estudiante."""

from .user import User


class Student(User):
    def __init__(self, id, name, mail, password, career, average=None):
        super().__init__(id, name, mail, password)
        self.career = career
        self.average = average

    def show_myself(self):
        return f"{super().show_myself()} - average: {self.average} - career: {self.career}"
