from repositories.base import BaseRepository
from repositories.user_repository import UserRepository
from controllers.login_controller import LoginController
from repositories.student_repository import StudentRepository
from repositories.course_repository import CourseRepository
from repositories.studentCouse_repository import StudentCourseRepository
from views.login_view import login_view
import flet as ft
from views.signup_view import signup_view

def register_student_into_course(user, course):
    fx = StudentCourseRepository()
    fx.register_student(user, course)

def admin_controller():
    
    insert = 'INSERT INTO admin(name , mail , password) VALUES (%s , %s , %s)'
    select = "SELECT * FROM admin"

    dnd = BaseRepository()

    admins = dnd.get_all(select,())

    print(admins)
 
def printUser():
    dnd = UserRepository()

    users = dnd.get_all_users()

    for element in users:
        print(element)
    
def addCourse():
    dnd = BaseRepository()
    query = 'INSERT INTO courses(name, description, space, career) VALUES(%s, %s, %s, %s)'
    
    name = 'Fundamentos matemáticos'
    description = 'Estudio de axiomas, teoría de conjuntos, lógica matemática y demostraciones'
    career = 'Ciencias de la computacion'
    space = 40
    
    dnd.execute(query, (name , description, space, career))
    
def printCourses():
    cd  = CourseRepository()
    tuples = cd.get_all_courses()
    for element in tuples:
        print(element.show_myself())
    
def printStudents():
    repo = StudentRepository()
    
    #student = repo.get_by_id(13)
    #print(student.name, student.career)

    all_students = repo.get_all_students()
    for s in all_students:
        print(f"id: {s.id } - {s.name} - {s.career} - {s.average}")

def start():
    dnd = LoginController()
    dnd.login()

def run():
    import flet as ft
    from views.login_view import login_view
    from views.signup_view import signup_view

    def main(page: ft.Page):

        def route_change(e):
            page.views.clear()

            if page.route == "/":
                page.views.append(ft.View("/", [login_view(page)]))
            elif page.route == "/signup":
                page.views.append(ft.View("/signup", [signup_view(page)]))

            page.update()

        page.on_route_change = route_change
        page.go("/")  # Ruta inicial

    ft.app(target=main)

ft.app(target= login_view)