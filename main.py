from repositories.base import BaseRepository
from repositories.usuario_repository import UserRepository
from controllers.login_controller import LoginController

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

printUser()   
ctr.login()