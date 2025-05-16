import flet as ft
from controllers.login_controller import LoginController

log = LoginController()

def main(page: ft.Page):
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    email_field = ft.TextField(label="Correo electrónico", width=300)
    password_field = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)

    status_text = ft.Text("")

    def login_clicked(e):
        email = email_field.value
        password = password_field.value
        success, message, rol = log.login(email, password)

        if success:
            status_text.value = message
            #move to other views from here
        else:
            status_text.value = message

        page.update()

    
    login_button = ft.ElevatedButton(text="Iniciar sesión", on_click=login_clicked)

    
    page.add(
        ft.Column(
            spacing= 20,
            controls= [
            ft.Text("Inicio de sesión", size=24, weight=ft.FontWeight.BOLD),
            email_field,
            password_field,
            login_button,
            status_text,
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)
