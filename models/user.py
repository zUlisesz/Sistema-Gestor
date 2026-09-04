"""Entidades base de usuario."""


class User:
    def __init__(self, id, name, mail, password):
        self.id = id
        self.name = name
        self.mail = mail
        self.__password = password

    def show_myself(self):
        """Devuelve informacion publica, sin exponer la contrasena."""
        return f"id: {self.id} - {self.name} - {self.mail}"

    def set_name(self, new_name):
        self.name = new_name

    def set_password(self, new_password):
        self.__password = new_password

    def get_password(self):
        return self.__password
