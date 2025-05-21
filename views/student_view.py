import flet as ft
from controllers.teacher_controller import TeacherController

def teacher_view(page: ft.Page):
    teacher = page.data['my_teacher']
    tctrl = TeacherController()

    class_cards_row1 = ft.Row(controls=[], spacing=32)
    class_cards_row2 = ft.Row(controls=[], spacing=32)

    def create_class_card(class_name):
        return ft.Container(
            width=200,
            height=200,
            bgcolor="#fef3c7",
            border_radius=10,
            alignment=ft.alignment.center,
            content=ft.Text(class_name, size=16, weight=ft.FontWeight.BOLD),
            padding=10,
            margin=5,
        )

    def agregar_clase(e):
        class_name_field = ft.TextField(label='Nombre de la clase', width=300)

        def reset_values():
            class_name_field.value = ''

        def event(e):
            class_name = class_name_field.value.strip()
            if class_name:
                tctrl.create_class(teacher.id, class_name)
                new_class_card = create_class_card(class_name)
                if len(class_cards_row1.controls) < 4:
                    class_cards_row1.controls.append(new_class_card)
                else:
                    class_cards_row2.controls.append(new_class_card)
                page.update()
                page.close(alert)

        alert = ft.BottomSheet(
            content=ft.Container(
                width=500,
                height=200,
                alignment=ft.alignment.center,
                padding=30,
                content=ft.Column(
                    spacing=20,
                    controls=[
                        class_name_field,
                        ft.ElevatedButton(text='Agregar clase', width=300, on_click=event)
                    ]
                )
            ),
            dismissible=True,
            on_dismiss=reset_values,
            elevation=10
        )

        page.open(alert)

    top_bar = ft.Container(
        height=120,
        bgcolor="#2563eb",
        content=ft.Row(
            [
                ft.Text(f'{teacher.name} \t\t id de profesor: {teacher.id}', color=ft.Colors.WHITE, size=30, weight=ft.FontWeight.BOLD),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.Icons.ACCOUNT_CIRCLE, icon_color=ft.Colors.WHITE, icon_size=60),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        ),
        padding=ft.padding.symmetric(horizontal=20),
    )

    sidebar = ft.Container(
        width=200,
        bgcolor="#1e40af",
        padding=20,
        content=ft.Column(
            controls=[
                ft.ElevatedButton("Inicio", icon=ft.Icons.HOME, style=ft.ButtonStyle(bgcolor="#1e40af", color="white")),
                ft.ElevatedButton("Estudiantes", icon=ft.Icons.GROUP, style=ft.ButtonStyle(bgcolor="#1e40af", color="white")),
                ft.ElevatedButton("Tareas", icon=ft.Icons.TASK, style=ft.ButtonStyle(bgcolor="#1e40af", color="white")),
                ft.ElevatedButton("Agregar clase", icon=ft.Icons.ADD, on_click=agregar_clase,
                                  style=ft.ButtonStyle(bgcolor="#1e40af", color="white")),
                ft.ElevatedButton("Salir", icon=ft.Icons.EXIT_TO_APP, style=ft.ButtonStyle(bgcolor="#1e40af", color="white")),
            ],
            spacing=30
        )
    )

    content_layout = ft.Row(
        controls=[
            sidebar,
            ft.Container(
                expand=True,
                bgcolor="#ffffff",
                border_radius=ft.border_radius.only(top_left=20),
                padding=50,
                content=ft.Column(
                    controls=[
                        ft.Text("Tus clases", size=20, color="#1f2937", weight=ft.FontWeight.BOLD),
                        class_cards_row1,
                        class_cards_row2
                    ],
                    spacing=25
                )
            )
        ],
        expand=True
    )

    return ft.View(
        route="/teacher",
        controls=[
            ft.Column(
                controls=[
                    top_bar,
                    content_layout
                ],
                expand=True
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        bgcolor="#f3f4f6"
    )
