import flet as ft
from controllers.course_controller import CourseController
from controllers.student_controller import StudentController
from controllers.admin_controller import AdminController
from models.administrador import Admin
from models.student import Student

def course_view(page: ft.Page, course_id):
    std = StudentController()
    cc = CourseController()
    adm = AdminController()
    course = cc.create_course(course_id) 

    instance = page.data['my_user']
    
    docente = ft.Text(f"Docente: {adm.get_courses_teacher(course_id)}", size=16, color= ft.Colors.WHITE)
    
    send_notice = ft.ElevatedButton(
        text ="Enviar aviso", 
        icon=ft.Icons.MESSAGE, 
        style=ft.ButtonStyle(bgcolor="#1e40af", color="white"),
        on_click=  lambda e: page.go(view),
        visible= False
    )

    options = [ft.dropdown.Option(name) for name in adm.check_teachers()]

    dropdown_teachers = ft.Dropdown(
        label='Profesores disponibles',
        options=options,
        width=320,
        visible=False
    )
    
    def post_notice(e):
        name_field = ft.TextField(label='título del aviso', width=400)
        description_field = ft.TextField(label='Contenido del aviso', width=400)
        
        def reset_values(e):
            name_field.value = ''
            description_field.value = ''
            
        
        
        alert =  ft.BottomSheet(
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
                        ft.ElevatedButton(text='Publicar aviso', elevation=10, width=300, on_click=event)
                    ]
                )
            ),
            dismissible=True,
            on_dismiss=reset_values,
            elevation=10
            
        )
        
        def event(e):
            name = name_field.value.strip()
            description = description_field.value.strip()
            if name and description :
                cc.make_course(name, description, int(space), career)
                page.update()
                page.close(alert)
    
    students_table = ft.DataTable(
        heading_row_color="#1e40af",
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
        
    def add_teacher(e):
        pre_id = dropdown_teachers.value.partition(' - ')
        teacher_id = int(pre_id[0])
        adm.assign_teacher(
            teacher_id=teacher_id,
            course_id=course_id
        )
        alert = ft.AlertDialog(
            content= ft.Text(value = f'Docente: {adm.get_courses_teacher(course_id)} asignado al curso: {course.name}'),
            on_dismiss = page.update()
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
        on_click=add_teacher
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
        elevation=10
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
     
    fill_table()   
    course_card = ft.Card(
        content=ft.Container(
            padding=20,
            width= 1500,
            bgcolor="#2563eb",
            border_radius= 10 ,
            content= ft.Row(
                controls= [
                    ft.Column(
                        controls=[
                            ft.Text(f"Curso: {course.name}", size=24, weight=ft.FontWeight.BOLD, color= ft.Colors.WHITE),
                            ft.Text(f"Descripción: {course.description}", size=16, color= ft.Colors.WHITE),
                            docente,
                        ],
                        spacing=10
                    ),
                    ft.Column(
                        controls=[
                            ft.ElevatedButton(
                                text ="Volver", 
                                icon=ft.Icons.EXIT_TO_APP, 
                                style=ft.ButtonStyle(bgcolor="#1e40af", color="white"),
                                on_click=  lambda e: page.go(view)
                            ),
                            send_notice
                        ],
                        spacing= 10 
                    )
                ],
                spacing= 600
            )
        )
    )
    
    content_layout = ft.Container(
                expand=True,
                width = 1520 , 
                bgcolor="#ffffff",
                border_radius=ft.border_radius.only(top_left=20),
                padding= 20,
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content= ft.Column(
                                controls= [
                                    ft.Text("Estudiantes inscritos", size=20, color="#1f2937", weight=ft.FontWeight.BOLD),
                                    ft.Container(
                                        expand = True , 
                                        content= students_table,
                                        margin=ft.margin.only(top=10),
                                        padding=10,
                                        bgcolor="#f9fafb",
                                        border_radius=8,
                                        border=ft.border.all(1, "#e5e7eb")
                                    )
                                ],
                                spacing= 25
                            )
                        ),
                        ft.Container(
                            content= ft.Column(
                                controls=[
                                    ft.Text("Avisos de la clase", size=20, color="#1f2937", weight=ft.FontWeight.BOLD),
                                    ft.Container(
                                        expand = True , 
                                        content= ft.Text('Avisos de la clase: '),
                                        margin=ft.margin.only(top=10),
                                        padding=10,
                                        bgcolor="#f9fafb",
                                        border_radius=8,
                                        border=ft.border.all(1, "#e5e7eb"),
                                    )
                                ]
                            )
                        )
                    ],
                    spacing=100
                )
            )
    
    
    admin_controls = ft.Column(
        controls=[
            dropdown_teachers,
            assign_teacher
        ],
        spacing=10,
        visible=isinstance(instance, Admin)
    )
    
    action_controls = ft.Row(
        controls=[
            action_button
        ],
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
