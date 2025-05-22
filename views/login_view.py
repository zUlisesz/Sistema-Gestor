import flet as ft
from controllers.login_controller import LoginController
from controllers.student_controller import StudentController
from controllers.teacher_controller import TeacherController
from controllers.admin_controller import AdminController
from .signup_view import signup_view
from .student_view import student_view
from .teacher_view import teacher_view
from .course_view import course_view
from .admin_view import admin_view
from models.student import Student
from models.teacher import Teacher
from models.administrador import Admin

log = LoginController()
std = StudentController()
teach = TeacherController()
ad = AdminController()

def login_view(page: ft.Page):
    
    email_field = ft.TextField(label="Correo electrónico", width=300)
    password_field = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    status_text = ft.Text("", color=ft.Colors.RED_400)

    def login_clicked(e):
        email = email_field.value.strip()
        password = password_field.value.strip()

        if not email or not password:
            status_text.value = "Por favor, llena todos los campos."
            page.update()
            return

        success, message, rol = log.login(email, password)

        if success:
            status_text.value = message
            status_text.color = ft.Colors.GREEN
            if rol == 'student':
                user : Student = std.create_student(email)
            elif rol == 'teacher':
                user : Teacher = teach.create_teacher(email)
            elif rol == 'admin':
                user :Admin = ad.create_admin(email)
            
            page.data = {'my_user' : user}
            page.go(f"/{rol}") 
        else:
            status_text.value = message
            status_text.color = ft.Colors.RED
        page.update()

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
        course_id = page.route.split("/course/")[1]
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


ft.app(target  = main)
