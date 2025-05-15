from repositories.base import BaseRepository
from repositories.user_repository import UserRepository
from controllers.login_controller import LoginController
from repositories.student_repository import StudentRepository
from views.login_view import login

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
    
ctr = LoginController()


#printUser()  
#ctr.login()


def printStudents():
    repo = StudentRepository()
    
    #student = repo.get_by_id(13)
    #print(student.name, student.career)

    all_students = repo.get_all_students()
    for s in all_students:
        print(f"{s.name} - {s.career} - {s.average}")

#printStudents()
login()