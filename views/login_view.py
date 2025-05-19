import flet as ft
from controllers.login_controller import LoginController
from .signup_view import signup_view

log = LoginController()

def login_view(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
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
            page.update()
            page.go(f"/{rol}")  #redirectingo to the appropiate screen
        else:
            status_text.value = message
            status_text.color = ft.Colors.RED
            page.update()

    page.add( ft.Column(
        spacing=20,
        controls=[
            ft.Text("Inicio de sesión", size=24, weight=ft.FontWeight.BOLD),
            email_field,
            password_field,
            ft.TextButton('Crear cuenta', on_click= lambda: signup_view(page)),
            ft.ElevatedButton("Iniciar sesión", on_click=login_clicked),
            status_text,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

