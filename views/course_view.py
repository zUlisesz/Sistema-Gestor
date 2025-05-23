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
        label = 'Profesores inscritos',
        options= options,
        width= 320,
        visible= False
    )
    
    def action(e):
        if isinstance(instance, Admin ):
            cc.delete_course(course_id)
        elif isinstance(instance, Student):
            std.leave_course(instance.id, course_id)
            
        page.go(view)
    
    button = ft.ElevatedButton('', on_click= action, elevation= 10, visible= False) 
    
    if isinstance(instance, Admin ):
        view = '/admin'
        button.text =  'Eliminar curso'
        dropdown_teachers.visible = True
        button.visible = True
    elif isinstance(instance, Student):
        view = '/student'
        button.text =  'Abandonar el curso'
       
           
        
    return ft.View(
        route=f"/course/{course_id}",
        controls=[
            ft.Text(f"Curso: {course.name}", size=24, weight=ft.FontWeight.BOLD),
            ft.Text(f"Descripción: {course.description}"),
            ft.Text(f"Profesor: Profesor de la materia"),
            ft.Text("Estudiantes inscritos:"),
            #ft.ListView(
                #controls= [ft.Text(student) for student in course['students']]
            #),
            dropdown_teachers,
            ft.ElevatedButton('Asignar profesor', elevation= 10 ),
            button,
            ft.ElevatedButton("Volver", on_click=lambda e: page.go(view), elevation= 10 )
        ],
        vertical_alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        bgcolor="#f3f4f6"
    )
