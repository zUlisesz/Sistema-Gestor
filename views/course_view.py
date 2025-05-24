import flet as ft
from controllers.course_controller import CourseController
from controllers.student_controller import StudentController
from controllers.admin_controller import AdminController
from controllers.teacher_controller import TeacherController
from models.administrador import Admin
from models.student import Student

def course_view(page: ft.Page, course_id):
    std = StudentController()
    cc = CourseController()
    adm = AdminController()
    tc = TeacherController()
    course = cc.create_course(course_id) 

    instance = page.data['my_user']
    
    docente = ft.Text(f"Docente: {adm.get_courses_teacher(course_id)}", size=16, color= ft.Colors.WHITE)

    options = [ft.dropdown.Option(name) for name in adm.check_teachers()]

    dropdown_teachers = ft.Dropdown(
        label='Profesores disponibles',
        options=options,
        width=320,
        visible=False
    )
    
    def post_notice(e):
        name_field = ft.TextField(label='Título del aviso', width=400)
        description_field = ft.TextField(label='Contenido del aviso', width=400)
        
        def reset_values(e):
            name_field.value = ''
            description_field.value = ''
            load_notices()
            page.update()
        
        def event(e):
            name = name_field.value.strip()
            description = description_field.value.strip()
            if name and description:
                tc.make_post(name, description, course_id)
                page.close(alert)
            
            load_notices()
            page.update()
                
        alert = ft.BottomSheet(
            content=ft.Container(
                width=400,
                height=300,
                alignment=ft.alignment.center,
                padding=30,
                content=ft.Column(
                    spacing=20,
                    controls=[
                        name_field,
                        description_field,
                        ft.ElevatedButton(
                            text='Publicar aviso',
                            elevation=10,
                            width=400,
                            on_click=event,
                            style=ft.ButtonStyle(
                                bgcolor="#1e40af",
                                color="white",
                                shape=ft.RoundedRectangleBorder(radius=10)
                            )
                        )
                    ]
                )
            ),
            dismissible=True,
            on_dismiss=reset_values,
            elevation=10
        )
        
        page.open(alert)
        name_field.value = ''
        description_field.value = ''
        
    send_notice = ft.ElevatedButton(
        text="Enviar aviso", 
        icon=ft.Icons.MESSAGE, 
        style=ft.ButtonStyle(
            bgcolor="#1e40af",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=10)
        ),
        on_click=post_notice,
        visible=False
    )
                
    students_table = ft.DataTable(
        heading_row_color="#1e40af",
        heading_row_height=40,
        horizontal_lines=ft.border.BorderSide(1, "#e5e7eb"),
        vertical_lines=ft.border.BorderSide(1, "#e5e7eb"),
        border_radius=8,
        columns=[
            ft.DataColumn(ft.Text("ID", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Nombre", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Correo", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Carrera", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD))
        ],
        rows=[]
    )
    
    def fill_table():
        users = cc.get_students_of(course_id)
        students_table.rows.clear()
        if users:
            for element in users:
                new_row = ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(element[0]))),
                        ft.DataCell(ft.Text(element[1])),
                        ft.DataCell(ft.Text(element[2])),
                        ft.DataCell(ft.Text(element[3])),
                    ]
                )
                students_table.rows.append(new_row)
        page.update()
        
    notices_container = ft.Column(
        controls=[],
        width= 400,
        scroll=ft.ScrollMode.AUTO
    )
        
    def create_notice_card(name, content, date):
        return ft.Container(
            width=340,
            height=120,
            bgcolor="#e0e7ff",
            border_radius=10,
            alignment=ft.alignment.center,
            content=ft.Column(
                controls=[
                    ft.Text(f'{name} | fecha: {date}', size=16, weight=ft.FontWeight.BOLD),
                    ft.Text(content, size=12, weight=ft.FontWeight.W_300),
                ]
            ),
            padding=10,
            margin=5,
        )
        
    def load_notices():
        data = cc.get_post(course_id)
        notices_container.controls.clear()
        if data:
            for element in data:
                notices_container.controls.append(create_notice_card(element[0], element[2], element[1]))
        page.update()
        
    def add_teacher(e):
        pre_id = dropdown_teachers.value.partition(' - ')
        teacher_id = int(pre_id[0])
        adm.assign_teacher(
            teacher_id=teacher_id,
            course_id=course_id
        )
        alert = ft.AlertDialog(
            content=ft.Text(value=f'Docente: {adm.get_courses_teacher(course_id)} asignado al curso: {course.name}'),
            on_dismiss=lambda e: page.update()
        )
        
        page.open(alert)
        docente.value = f"Docente: {adm.get_courses_teacher(course_id)}"
        dropdown_teachers.visible = False
        assign_teacher.visible = False
        
        page.update()

    assign_teacher = ft.ElevatedButton(
        text='Asignar profesor',
        elevation=10,
        visible=False,
        on_click=add_teacher,
        style=ft.ButtonStyle(
            bgcolor="#1e40af",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=10)
        )
    )

    def action(e):
        if isinstance(instance, Admin):
            cc.delete_course(course_id)
        elif isinstance(instance, Student):
            std.leave_course(instance.id, course_id)
        page.go(view)

    action_button = ft.ElevatedButton(
        text='press',
        on_click=action,
        elevation=10,
        style=ft.ButtonStyle(
            bgcolor="#dc2626",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=10)
        )
    )

    if isinstance(instance, Admin):
        view = '/admin'
        action_button.text = 'Eliminar curso'
        if 'Docente no asignado' in docente.value:
            dropdown_teachers.visible = True
            assign_teacher.visible = True
    elif isinstance(instance, Student):
        view = '/student'
        action_button.text = 'Abandonar el curso'
    else:
        view = '/teacher'
        send_notice.visible = True
        action_button.visible = False

    load_notices()
    fill_table()   

    course_card = ft.Card(
        content=ft.Container(
            padding=20,
            expand=True,
            bgcolor="#2563eb",
            border_radius=10,
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text(f"Curso: {course.name}", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ft.Text(f"Descripción: {course.description}", size=16, color=ft.Colors.WHITE),
                            docente,
                        ],
                        spacing=10
                    ),
                    ft.Column(
                        controls=[
                            ft.ElevatedButton(
                                text="Volver",
                                icon=ft.Icons.EXIT_TO_APP,
                                on_click=lambda e: page.go(view),
                                style=ft.ButtonStyle(
                                    bgcolor="#1e40af",
                                    color="white",
                                    shape=ft.RoundedRectangleBorder(radius=10)
                                )
                            ),
                            send_notice
                        ],
                        spacing=10
                    )
                ],
                spacing=100
            )
        )
    )
    
    content_layout = ft.Container(
        expand=True,
        bgcolor="#ffffff",
        border_radius=ft.border_radius.only(top_left=20),
        padding=20,
        content=ft.Row(
            controls=[
                ft.Container(
                    expand=2,
                    content=ft.Column(
                        controls=[
                            ft.Text("Estudiantes inscritos", size=20, color="#1f2937", weight=ft.FontWeight.BOLD),
                            ft.Container(
                                expand=True,
                                content=students_table,
                                margin=ft.margin.only(top=10),
                                padding=10,
                                bgcolor="#f9fafb",
                                border_radius=8,
                                border=ft.border.all(1, "#e5e7eb")
                            )
                        ],
                        spacing=25
                    )
                ),
                ft.Container(
                    expand=1,
                    content=ft.Column(
                        controls=[
                            ft.Text("Avisos de la clase", size=20, color="#1f2937", weight=ft.FontWeight.BOLD),
                            ft.Container(
                                expand=True,
                                content=notices_container,
                                margin=ft.margin.only(top=10),
                                padding=10,
                                bgcolor="#f9fafb",
                                border_radius=8,
                                border=ft.border.all(1, "#e5e7eb")
                            )
                        ]
                    )
                )
            ],
            spacing=40
        )
    )
    
    admin_controls = ft.Card(
        elevation=2,
        content=ft.Container(
            padding=10,
            content=ft.Column(
                controls=[dropdown_teachers, assign_teacher],
                spacing=10
            )
        ),
        visible=isinstance(instance, Admin)
    )
    
    action_controls = ft.Row(
        controls=[action_button],
        spacing=10
    )

    return ft.View(
        route=f"/course/{course_id}",
        controls=[
            course_card,
            content_layout,
            admin_controls,
            action_controls
        ],
        vertical_alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        bgcolor="#f3f4f6"
    )
