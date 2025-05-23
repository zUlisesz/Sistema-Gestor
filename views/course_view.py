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

    options = [ft.dropdown.Option(name) for name in adm.check_teachers()]

    dropdown_teachers = ft.Dropdown(
        label='Profesores disponibles',
        options=options,
        width=320,
        visible=False
    )
    

    def add_teacher(e):
        pre_id = dropdown_teachers.value.partition(' - ')
        teacher_id = int(pre_id[0])
        adm.assign_teacher(
            teacher_id=teacher_id,
            course_id=course_id
        )
        page.snack_bar = ft.SnackBar(ft.Text("Profesor asignado correctamente"))
        page.snack_bar.open = True
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
        text='',
        on_click=action,
        elevation=10
    )

    if isinstance(instance, Admin):
        view = '/admin'
        action_button.text = 'Eliminar curso'
        dropdown_teachers.visible = True
        assign_teacher.visible = True
    elif isinstance(instance, Student):
        view = '/student'
        action_button.text = 'Abandonar el curso'

    # Crear la tarjeta del curso
    course_card = ft.Card(
        content=ft.Container(
            padding=20,
            width= 800,
            bgcolor="#2563eb",
            border_radius= 10 ,
            content=ft.Column(
                controls=[
                    ft.Text(f"Curso: {course.name}", size=24, weight=ft.FontWeight.BOLD, color= ft.Colors.WHITE),
                    ft.Text(f"Descripción: {course.description}", size=16, color= ft.Colors.WHITE),
                    ft.Text(f"Docente: {adm.get_courses_teacher(course_id)}", size=16, color= ft.Colors.WHITE),
                    #ft.Text("Estudiantes inscritos:", size=16, color= ft.Colors.WHITE),
                    # Aquí puedes agregar una lista de estudiantes si está disponible
                ],
                spacing=10
            )
        )
    )

    # Controles adicionales (solo visibles para administradores)
    admin_controls = ft.Column(
        controls=[
            dropdown_teachers,
            assign_teacher
        ],
        spacing=10,
        visible=isinstance(instance, Admin)
    )

    # Botones de acción
    action_controls = ft.Row(
        controls=[
            action_button,
            ft.ElevatedButton("Volver", on_click=lambda e: page.go(view), elevation=10)
        ],
        spacing=10
    )

    return ft.View(
        route=f"/course/{course_id}",
        controls=[
            course_card,
            admin_controls,
            action_controls
        ],
        vertical_alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        bgcolor="#f3f4f6"
    )
