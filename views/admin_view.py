import flet as ft
from controllers.admin_controller import AdminController
from controllers.course_controller import CourseController

def admin_view(page: ft.Page):
    admin = page.data['my_user']
    actrl = AdminController()
    cc = CourseController()
    
    course_cards_row1 = ft.Row(controls=[], spacing=32)
    course_cards_row2 = ft.Row(controls=[], spacing=32)
    course_cards_row3 = ft.Row(controls=[], spacing=32)

    user_table = ft.DataTable(
        heading_row_color="#1e40af",
        horizontal_lines=ft.border.BorderSide(1, "#e5e7eb"),
        vertical_lines=ft.border.BorderSide(1, "#e5e7eb"),
        border_radius=8,
        columns=[
            ft.DataColumn(ft.Text("ID", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Nombre", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Correo", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Rol", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Contraseña", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD))
        ],
        rows=[]
    )
    
    def fill_table():
        users = actrl.get_all()
        for element in users:
            new_row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(element[0]))),
                    ft.DataCell(ft.Text(element[1])),
                    ft.DataCell(ft.Text(element[2])),
                    ft.DataCell(ft.Text(element[3])),
                    ft.DataCell(ft.Text(element[4]))
                ]
            )
            user_table.rows.append(new_row)
        page.update()
        
    def load_courses():
        courses = cc.names()
        id_courses = cc.ids()
        
        for i, name_course in enumerate(courses):
            course_card = create_course_card(name_course, id_courses[i])
            if len(course_cards_row1.controls) < 6:
                course_cards_row1.controls.append(course_card)
            elif len(course_cards_row1.controls) >= 6 and len(course_cards_row1.controls) < 13:
                course_cards_row2.controls.append(course_card)
            else:
                course_cards_row3.controls.append(course_card)
                
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
        
    fill_table()
    load_courses()
        
    def go_back(e):
        page.data = {'my_user': None}
        page.go('/')

    def add_course(e):
        name_field = ft.TextField(label='Nombre', width=300)
        description_field = ft.TextField(label='Descripción', width=300)
        space_field = ft.TextField(label='Cupo del curso', width=300)
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
                        ft.ElevatedButton(text='Crear curso', elevation=10, width=300, on_click=event)
                    ]
                )
            ),
            dismissible=True,
            on_dismiss=reset_values,
            elevation=10
        )
        load_courses()
        page.open(alert)

    top_bar = ft.Container(
        height=140,
        bgcolor="#2563eb",
        padding=ft.padding.symmetric(horizontal=20, vertical= 20 ),
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(f'{admin.name} \t\t id de administrador: {admin.id}', color=ft.Colors.WHITE, size=30, weight=ft.FontWeight.BOLD),
                        ft.Container(expand=True),
                        ft.IconButton(icon=ft.Icons.ACCOUNT_CIRCLE, icon_color=ft.Colors.WHITE, icon_size=60),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Agregar curso", icon=ft.Icons.PERSON_ADD, on_click=add_course, style=ft.ButtonStyle(bgcolor="#1e40af", color="white")),
                        ft.ElevatedButton("Cerrar sesión", icon=ft.Icons.EXIT_TO_APP, on_click=go_back, style=ft.ButtonStyle(bgcolor="#1e40af", color="white")),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                )
            ],
            spacing=10,
        )
    )

    content_layout = ft.Column(
        controls=[
            ft.Container(
                expand= True ,
                width = 1520,
                bgcolor="#ffffff",
                border_radius=ft.border_radius.only(top_left=20),
                padding=40 ,
                content=ft.Column(
                    controls=[
                        ft.Text("Cursos", size=20, color="#1f2937", weight=ft.FontWeight.BOLD),
                        course_cards_row1,
                        course_cards_row2,
                        course_cards_row3
                    ],
                    spacing=25
                )
            ),
            ft.Container(
                expand=True,
                width = 1520 , 
                bgcolor="#ffffff",
                border_radius=ft.border_radius.only(top_right=20),
                padding=100,
                content=ft.Column(
                    controls=[
                        ft.Text("Usuarios", size=20, color="#1f2937", weight=ft.FontWeight.BOLD),
                        ft.Container(
                            expand = True , 
                            content=user_table,
                            margin=ft.margin.only(top=10),
                            padding=10,
                            bgcolor="#f9fafb",
                            border_radius=8,
                            border=ft.border.all(1, "#e5e7eb"),
                        )
                    ],
                    spacing=25
                )
            )
        ],
        expand=True
    )

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
        scroll=True,
        vertical_alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.MainAxisAlignment.START,
        bgcolor="#f3f4f6"
    )
