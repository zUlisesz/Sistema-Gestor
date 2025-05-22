import flet as ft
from controllers.course_controller import CourseController

def course_view(page: ft.Page, course_id):
    cc = CourseController()
    course = cc.create_course(course_id) 
    print(course_id)

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
            ft.ElevatedButton("Volver", on_click=lambda e: page.go("/student"))
        ],
        vertical_alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        bgcolor="#f3f4f6"
    )
