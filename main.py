from repositories.base import BaseRepository

insert = 'INSERT INTO admin(name , mail , password) VALUES (%s , %s , %s)'

select = "SELECT * FROM admin"

dnd = BaseRepository()

admins = dnd.get_all(select,())

print(admins)