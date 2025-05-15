from repositories.base import BaseRepository
from controllers.validation_controller import AuthController

def admin_controller():
    
    insert = 'INSERT INTO admin(name , mail , password) VALUES (%s , %s , %s)'
    select = "SELECT * FROM admin"

    dnd = BaseRepository()

    admins = dnd.get_all(select,())

    print(admins)
 
def add_user():
    query =  'INSERT INTO users(name, mail, password, rol) VALUES (%s , %s , %s, %s)'
    rol = 'student'
    
    name = input('Name: \n')
    mail = input('Mail: \n')
    password = input('Password: \n')
    
    dnd = BaseRepository()
    
    dnd.execute(query, (name , mail, password, rol))
    print('user added successfuly')
    
def login():
    mail  = input('InSert your email: \n')  
    auth = AuthController()
    print(auth.existing_user(mail))
    
login()