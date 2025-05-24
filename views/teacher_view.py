#vista para los profesores
#se implementa los mismos patrones en todas las vistas
#se crean los elementos de la vista
#se usan eventos que a su vez usan a los controladores importados
#y se regresa la vista con un nombre de ruta 
import flet as ft
from controllers.teacher_controller import TeacherController

def teacher_view(page: ft.Page):
    teacher = page.data['my_user']
    tctrl = TeacherController()

    course_cards_row1 = ft.Row(controls=[], spacing=32)
    course_cards_row2 = ft.Row(controls=[], spacing=32)
    
    def go_back(e):
        page.data = {'my_user': None}
        page.go("/")

    def load_courses():
        data = tctrl.get_my_info_courses(teacher.id)
        if data:
            for element in data:
                course_card = create_course_card(element[1], element[0])
                if len(course_cards_row1.controls) < 5:
                    course_cards_row1.controls.append(course_card)
                else:
                    course_cards_row2.controls.append(course_card)
                page.update()
                
    def create_course_card(name, id):
        return ft.Container(
            width=200,
            height=200,
            bgcolor="#e0e7ff",
            ink=True,
            on_click=lambda e: page.go(f"/course/{id}"),
            data=id,
            border_radius=10,
            alignment=ft.alignment.center,
            content=ft.Text(name, size=16, weight=ft.FontWeight.BOLD),
            padding=10,
            margin=5,
        )


    load_courses()
    
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
                ft.ElevatedButton("Cerrar sesión", icon=ft.Icons.EXIT_TO_APP, style=ft.ButtonStyle(bgcolor="#1e40af", color="white"), on_click= go_back),
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
                        course_cards_row1,
                        course_cards_row2
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
