from repositories.base import BaseRepository
from repositories.usuario_repository import UserRepository
from controllers.login_controller import LoginController

def admin_controller():
    
    insert = 'INSERT INTO admin(name , mail , password) VALUES (%s , %s , %s)'
    select = "SELECT * FROM admin"

    dnd = BaseRepository()

    admins = dnd.get_all(select,())

    print(admins)
 
def add_user():
    query =  'INSERT INTO users(name, mail, password, rol) VALUES (%s , %s , %s, %s)'
    rol = 'admin'
    
    name = input('Name: \n')
    mail = input('Mail: \n')
    password = input('Password: \n')
    
    dnd = BaseRepository()
    
    dnd.execute(query, (name , mail, password, rol))
    print('user added successfuly')
    
ctr = LoginController()
dnd = UserRepository()

users = dnd.get_all_users()

for element in users:
    print(element)