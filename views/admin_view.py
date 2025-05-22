import flet as ft
from controllers.admin_controller import AdminController
from controllers.course_controller import CourseController

def admin_view(page: ft.Page):
    admin = page.data['my_user']
    actrl = AdminController()
    cc = CourseController()
    
    course_cards_row1 = ft.Row(controls=[], spacing=32)
    course_cards_row2 = ft.Row(controls=[], spacing=32)

    # Tarjetas de estadísticas
    stats_row = ft.Row(controls=[], spacing=32)
    
    
    def load_courses():
        
        courses = cc.names()
        id_courses = cc.ids()
        
        i = 0 ; 
        for name_course in courses:
            course_card = create_course_card(name_course, id_courses[i])
            if len(course_cards_row1.controls) < 5:
                course_cards_row1.controls.append(course_card)
            else:
                course_cards_row2.controls.append(course_card)
                
            i = i + 1
            
                
        page.update()
        
    def create_course_card(course_name,id):
        return ft.Container(
            width=200,
            height=200,
            bgcolor="#e0e7ff",
            ink= True,
            on_click=lambda e: page.go(f"/course/{id}"),
            data = id,
            border_radius=10,
            alignment=ft.alignment.center,
            content=ft.Text(course_name, size=16, weight=ft.FontWeight.BOLD),
            padding=10,
            margin=5,
        )
        
    load_courses()

    def create_stat_card(title, value, color):
        return ft.Container(
            width=200,
            height=100,
            bgcolor=color,
            border_radius=10,
            alignment=ft.alignment.center,
            content=ft.Column(
                controls=[
                    ft.Text(title, size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text(str(value), size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=10,
            margin=5,
        )
        
    def go_back(e):
        page.data = {'my_user': None}
        page.go('/')

    def cargar_estadisticas():
        total_users = actrl.get_total_users()
        total_students = actrl.get_total_students()
        total_teachers = actrl.get_total_teachers()
        total_courses = actrl.get_total_courses()

        stats_row.controls.clear()
        stats_row.controls.extend([
            create_stat_card("Usuarios", total_users, "#2563eb"),
            create_stat_card("Estudiantes", total_students, "#1e40af"),
            create_stat_card("Profesores", total_teachers, "#1e3a8a"),
            create_stat_card("Cursos", total_courses, "#1e40af"),
        ])
        page.update()

    def add_course(e):
        name_field = ft.TextField(label='Nombre', width=300)
        description_field = ft.TextField(label='Descripción', width=300)
        space_field = ft.TextField(label  = 'Cupo del curso', width= 300)
        career_dropdown = ft.Dropdown(
            label='Carrera',
            options=[
                ft.dropdown.Option("Ciencias de la computación"),
                ft.dropdown.Option("Ciencia de datos"),
                ft.dropdown.Option("Tecnologías de la información"),
            ],
            width=300
        )

        def reset_values():
            name_field.value = ''
            description_field.value = ''
            space_field.value = ''
            career_dropdown.value = None

        def event(e):
            name = name_field.value.strip()
            description = description_field.value.strip()
            space = space_field.value.strip()
            career = career_dropdown.value
            if name and description and space and career:
                cc.make_course(name, description, int(space), career)
                page.update()
                page.close(alert)

        alert = ft.BottomSheet(
            content=ft.Container(
                width=500,
                height=400,
                alignment=ft.alignment.center,
                padding=30,
                content=ft.Column(
                    spacing=20,
                    controls=[
                        name_field,
                        description_field,
                        space_field, 
                        career_dropdown,
                        ft.ElevatedButton(text='Crear curso usuario',elevation= 10 , width=300, on_click=event)
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
                ft.Text(f'{admin.name} \t\t id de administrador: {admin.id}', color=ft.Colors.WHITE, size=30, weight=ft.FontWeight.BOLD),
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
                ft.ElevatedButton("Usuarios", icon=ft.Icons.PEOPLE, style=ft.ButtonStyle(bgcolor="#1e40af", color="white")),
                ft.ElevatedButton("Cursos", icon=ft.Icons.BOOK, style=ft.ButtonStyle(bgcolor="#1e40af", color="white")),
                ft.ElevatedButton("Agregar curso", icon=ft.Icons.PERSON_ADD, on_click= add_course,
                                  style=ft.ButtonStyle(bgcolor="#1e40af", color="white")),
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
                        ft.Text("Panel de administración", size=20, color="#1f2937", weight=ft.FontWeight.BOLD),
                        stats_row,
                        course_cards_row1,
                        course_cards_row2
                    ],
                    spacing=25
                )
            )
        ],
        expand=True
    )

    #cargar_estadisticas() debo completar este método


    return ft.View(
        route="/admin",
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
        horizontal_alignment=ft.MainAxisAlignment.START,
        bgcolor="#f3f4f6"
    )
