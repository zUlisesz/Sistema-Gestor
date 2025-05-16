from repositories.base import BaseRepository
from repositories.user_repository import UserRepository
from controllers.login_controller import LoginController
from repositories.student_repository import StudentRepository
from repositories.course_repository import CourseRepository
from repositories.studentCouse_repository import StudentCourseRepository

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
#printStudents()


