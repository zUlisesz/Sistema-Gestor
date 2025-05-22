import flet as ft
from controllers.login_controller import LoginController

controller = LoginController()

def signup_view(page: ft.Page):

    name_field = ft.TextField(label="Nombre", width=300)
    email_field = ft.TextField(label="Correo electrónico", width=300)
    password_field = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)

    rol_field = ft.Dropdown(
        label="Rol",
        options=[
            ft.dropdown.Option("student"),
            ft.dropdown.Option("teacher"),
            ft.dropdown.Option("admin")
        ],
        width=300
    )

    career_field = ft.TextField(label="Carrera", width=300, visible=False)
    status_text = ft.Text(color=ft.Colors.RED_400)

    def on_rol_change(e):
        career_field.visible = rol_field.value == "student"
        page.update()

    rol_field.on_change = on_rol_change

    def reset_values():
        name_field.value = ''
        email_field.value = ''
        password_field.value = ''
        rol_field.value = None
        career_field.value = ''
        career_field.visible = False
        
        
    def on_submit(e):
        name = name_field.value
        email = email_field.value
        password = password_field.value
        career_dropdown = ft.Dropdown(
            label='Carrera',
            options=[
                ft.dropdown.Option("Ciencias de la computación"),
                ft.dropdown.Option("Ciencia de datos"),
                ft.dropdown.Option("Tecnologías de la información"),
            ],
            width=300
        )
        rol = rol_field.value
        career = career_dropdown.value

        success, message = controller.sign_up(name, email, password, rol, career)
        status_text.value = message
        status_text.color = ft.Colors.GREEN if success else ft.Colors.RED
        reset_values()
        page.update()

    def go_back(e):
        page.go("/")

    return ft.Column(
        controls=[
            ft.Text("Formulario de registro", size=24, weight="bold"),
            name_field,
            email_field,
            password_field,
            rol_field,
            career_field,
            ft.Row(
                [ft.ElevatedButton("Registrarse", on_click=on_submit),
                 ft.TextButton("Volver al login", on_click=go_back)],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            status_text,
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
