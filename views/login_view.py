#vista principal del programa, es el login
#se importan los arcivos de el modulo de controladores y las demás vistas
import flet as ft
from controllers.login_controller import LoginController
from services.database import DatabaseError
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
                from controllers.student_controller import StudentController
                user = StudentController().create_student(email)
            elif rol == 'teacher':
                from controllers.teacher_controller import TeacherController
                user = TeacherController().create_teacher(email)
            elif rol == 'admin':
                from controllers.admin_controller import AdminController
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
            page.navigate(f"/{rol}")
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
                    ft.TextButton('Crear cuenta', on_click=lambda _: page.navigate("/signup")),
                    ft.ElevatedButton("Iniciar sesión", on_click=login_clicked),
                    status_text,
                ],
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
