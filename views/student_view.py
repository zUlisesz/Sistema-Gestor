import flet as ft
from controllers.student_controller import StudentController

def student_view(page: ft.Page):
    std = StudentController()
    student = page.data['my_user']

    course_cards_row1 = ft.Row(controls=[], spacing=32)
    course_cards_row2 = ft.Row(controls=[], spacing=32)

    def load_courses():
        courses = std.get_courses_name(student.id)
        id_courses = std.get_courses_id(student.id)
        if courses:
            for i, name_course in enumerate(courses):
                course_card = create_course_card(name_course, id_courses[i])
                if len(course_cards_row1.controls) < 5:
                    course_cards_row1.controls.append(course_card)
                else:
                    course_cards_row2.controls.append(course_card)
                page.update()

    def create_course_card(course_name, id):
        return ft.Container(
            width=200,
            height=200,
            bgcolor="#e0e7ff",
            ink=True,
            on_click=lambda e: page.go(f"/course/{id}"),
            data=id,
            border_radius=10,
            alignment=ft.alignment.center,
            content=ft.Text(course_name, size=16, weight=ft.FontWeight.BOLD),
            padding=10,
            margin=5,
        )

    def go_back(e):
        page.data = {'my_user': None}
        page.go("/")

    def inscribirme_a_curso(e):
        id_course_field = ft.TextField(label='Id del curso', width=300)
        status_text = ft.Text('', visible=False)

        def reset_values(e):
            id_course_field.value = ''
            status_text.value = ''
            status_text.visible = False
            page.close(alert)

        def event(e):
            course_id = int(id_course_field.value)
            
            if std.enter_to_course(student.id, course_id):
                course_name = std.get_course(course_id)
                new_course_card = create_course_card(course_name, course_id)
                if len(course_cards_row1.controls) < 5:
                    course_cards_row1.controls.append(new_course_card)
                else:
                    course_cards_row2.controls.append(new_course_card)

                id_course_field.value = ''
                status_text.value = 'Inscripción al curso completada correctamente'
                status_text.color = ft.Colors.GREEN_200
                status_text.visible = True
                status_text.update()
                page.update()
            else:
                status_text.value = 'Id de curso inexistente o ya estás inscrito a este curso'
                status_text.color = ft.Colors.RED_200
                status_text.visible = True
                status_text.update()
                page.update()

        alert = ft.BottomSheet(
            content=ft.Container(
                width=500,
                height=200,
                alignment=ft.alignment.center,
                padding=30,
                content=ft.Column(
                    spacing=20,
                    controls=[
                        id_course_field,
                        status_text,
                        ft.ElevatedButton(text='Inscribirme al curso', width=300, on_click=event)
                    ]
                )
            ),
            dismissible=True,
            on_dismiss=reset_values,
            elevation=10
        )

        page.open(alert)
        page.update()

    top_bar = ft.Container(
        height=120,
        bgcolor="#2563eb",
        content=ft.Row(
            [
                ft.Text(f'{student.name} \t\t id de estudiante: {student.id}', color=ft.Colors.WHITE, size=30, weight=ft.FontWeight.BOLD),
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
                ft.ElevatedButton("Tareas", icon=ft.Icons.TASK, style=ft.ButtonStyle(bgcolor="#1e40af", color="white")),
                ft.ElevatedButton("Calificaciones", icon=ft.Icons.GRADING, style=ft.ButtonStyle(bgcolor="#1e40af", color="white")),
                ft.ElevatedButton("Inscribirme a un curso", icon=ft.Icons.SCHOOL, on_click=inscribirme_a_curso,
                                  style=ft.ButtonStyle(bgcolor="#1e40af", color="white")),
                ft.ElevatedButton("Salir", icon=ft.Icons.EXIT_TO_APP, style=ft.ButtonStyle(bgcolor="#1e40af", color="white"), on_click=go_back)
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
                        ft.Text("Tus cursos", size=20, color="#1f2937", weight=ft.FontWeight.BOLD),
                        course_cards_row1,
                        course_cards_row2
                    ],
                    spacing=25
                )
            )
        ],
        expand=True
    )

    load_courses()

    return ft.View(
        route="/student",
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
