import flet as ft
from controllers.student_controller import StudentController

def student_view(page: ft.Page):
    page.controls.clear()
    page.title = "Panel Estudiante"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#f3f4f6"

    course_cards_column = ft.Row(controls=[], scroll=ft.ScrollMode.AUTO, spacing= 32 )
    course_cards_column2 = ft.Row(controls=[], scroll=ft.ScrollMode.AUTO, spacing= 32 )

    top_bar = ft.Container(
        height=120,
        bgcolor="#2563eb",
        content=ft.Row(
            [
                ft.Text("Ulises Galdino Romero Romero", bgcolor=ft.Colors.WHITE, size=30, weight=ft.FontWeight.BOLD),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.Icons.ACCOUNT_CIRCLE, icon_color=ft.Colors.WHITE, icon_size=60),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        ),
        padding=ft.padding.symmetric(horizontal=20),
    )

    
    def inscribirme_a_curso(e):
        std = StudentController()
        
        id_student_field = ft.TextField(label= 'Id de estudiante', width= 300)
        id_course_field = ft.TextField(label= 'Id del curso', width= 300)
        
        
        def reset_values():
            id_student_field.value = ''
            id_course_field = ''
            
        def event(e):
            std.enter_to_course(int(id_student_field.value), int(id_course_field.value))
            create_container()
            reset_values()
            page.close(alert)
        
        alert = ft.BottomSheet(
            content= ft.Container(
                width= 500,
                height= 260,
                alignment= ft.alignment.center,
                padding= 30,
                content= ft.Column(
                    spacing= 20,
                    controls= [
                        id_student_field,
                        id_course_field,
                        ft.ElevatedButton(text= 'Inscribirme al curso', width= 300, on_click= event)
                    ]
                )     
            ),
            dismissible= True,
            on_dismiss= reset_values,
            elevation= 10 
        )
        
        page.open(alert)
        
        def create_container():
            new_course_card = ft.Container(
                width=200,
                height=200,
                bgcolor="#e0e7ff", 
                border_radius=10,
                alignment=ft.alignment.center,
                content=ft.Text(std.get_course(int(id_course_field.value)), size=16, weight=ft.FontWeight.BOLD),
                padding=10,
                margin=5,
            )
        
            if len(course_cards_column.controls) <= 4 :    
                course_cards_column.controls.append(new_course_card)
            elif len(course_cards_column2.controls) <= 4:
                course_cards_column2.controls.append(new_course_card)
    
            page.update()

   
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
                padding= 50,
                content=ft.Column(
                    controls=[
                        ft.Text("Tus cursos", size=20, color="#1f2937", weight=ft.FontWeight.BOLD),
                        course_cards_column,
                        course_cards_column2
                    ],
                    spacing= 25
                )
            )
        ],
        expand=True
    )

    page.add(
        ft.Column(
            controls=[
                top_bar,
                content_layout
            ],
            expand=True
        )
    )

ft.app(target=student_view)
