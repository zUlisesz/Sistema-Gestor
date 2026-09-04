"""Shell de la Flet app: configuracion, sesion y navegacion."""

import flet as ft

from .admin_view import admin_view
from .course_view import course_view
from .login_view import login_view
from .signup_view import signup_view
from .student_view import student_view
from .teacher_view import teacher_view


class ClassroomApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Sistema Gestor"
        self.page.theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE)
        self.page.data = {}
        self.page.on_route_change = self.on_route_change
        self.page.on_view_pop = self.on_view_pop

    def _has_session(self):
        return bool(self.page.data.get("my_user"))

    def on_route_change(self, event):
        route = event.route if event else self.page.route
        self.page.views.clear()
        self.page.views.append(login_view(self.page))

        if route != "/" and not self._has_session():
            self.page.navigate("/")
            return

        if route == "/signup":
            self.page.views.append(signup_view(self.page))
        elif route == "/student":
            self.page.views.append(student_view(self.page))
        elif route == "/teacher":
            self.page.views.append(teacher_view(self.page))
        elif route == "/admin":
            self.page.views.append(admin_view(self.page))
        elif route.startswith("/course/"):
            course_id = route.removeprefix("/course/")
            self.page.views.append(course_view(self.page, course_id))
        elif route != "/":
            self.page.views.append(self._not_found_view(route))
        self.page.update()

    def on_view_pop(self, event):
        if len(self.page.views) <= 1:
            return
        self.page.views.pop()
        self.page.navigate(self.page.views[-1].route)

    @staticmethod
    def _not_found_view(route):
        return ft.View(
            route=route,
            controls=[ft.Text("404 - Pagina no encontrada", size=24)],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def run(self):
        self.page.navigate(self.page.route or "/")


def main(page: ft.Page):
    ClassroomApp(page).run()
