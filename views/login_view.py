#vista principal del programa, es el login
#se importan los arcivos de el modulo de controladores y las demás vistas
import flet as ft
from controllers.admin_controller import AdminController
from controllers.login_controller import LoginController
from controllers.student_controller import StudentController
from controllers.teacher_controller import TeacherController
from services.database import DatabaseError
from .signup_view import signup_view
from .student_view import student_view
from .teacher_view import teacher_view
from .course_view import course_view
from .admin_view import admin_view
def login_view(page: ft.Page):
    email_field = ft.TextField(label="Correo electrónico", width=300)
    password_field = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    status_text = ft.Text("", color=ft.Colors.RED_400)

    def login_clicked(e):
        email = (email_field.value or "").strip()
        password = (password_field.value or "").strip()

        if not email or not password:
            status_text.value = "Por favor, llena todos los campos."
            page.update()
            return

        try:
            login_controller = LoginController()
            success, message, rol = login_controller.login(email, password)
        except (DatabaseError, RuntimeError) as error:
            status_text.value = str(error)
            status_text.color = ft.Colors.RED
            page.update()
            return

        if success:
            status_text.value = message
            status_text.color = ft.Colors.GREEN
            user = None
            if rol == 'student':
                user = StudentController().create_student(email)
            elif rol == 'teacher':
                user = TeacherController().create_teacher(email)
            elif rol == 'admin':
                user = AdminController().create_admin(email)
            else:
                success = False
                message = "Rol de usuario no reconocido."

            if not success or user is None:
                status_text.value = "No se pudo cargar el perfil del usuario."
                status_text.color = ft.Colors.RED
                page.update()
                return

            page.data = {'my_user' : user}
            page.go(f"/{rol}") 
        else:
            status_text.value = message
            status_text.color = ft.Colors.RED
        page.update()

    #regresa la vista asignando un nombre de ruta a la vista
    return ft.View(
        route="/",
        controls=[
            ft.Column(
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Inicio de sesión", size=24, weight=ft.FontWeight.BOLD),
                    email_field,
                    password_field,
                    ft.TextButton('Crear cuenta', on_click=lambda _: page.go("/signup")),
                    ft.ElevatedButton("Iniciar sesión", on_click=login_clicked),
                    status_text,
                ],
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

#este método sirve como direccinador de vistas para saber a donde moverse
def route_change(e: ft.RouteChangeEvent):
    page = e.page
    page.views.clear()

    if page.route == "/":
        page.views.append(login_view(page))
    elif page.route == "/signup":
        page.views.append(signup_view(page))
    elif page.route == "/student":
        page.views.append(student_view(page))
    elif page.route == '/teacher':
        page.views.append(teacher_view(page))
    elif page.route == '/admin':
        page.views.append(admin_view(page))
    elif page.route.startswith("/course/"):
        course_id = page.route.removeprefix("/course/")
        page.views.append(course_view(page, course_id))
        
    else:
        
        page.views.append(
            ft.View(
                route=page.route,
                controls=[
                    ft.Text("404 - Página no encontrada", size=24, weight=ft.FontWeight.BOLD)
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
    page.update()

def main(page: ft.Page):
    page.title = "Aplicación Flet"
    page.on_route_change = route_change
    page.go(page.route)
