#clase padre para poder relizar consultas a la bd
from services.database import connect_db

class BaseRepository:
    
    def __init__(self):
        self.conn = connect_db() #conexión con la bd
        self.cursor = self.conn.cursor() # cursor para poder manipula inf de la bd
        
    def execute(self , query , parameters = ()): #ejecúta funciones como insert y delete
        self.cursor.execute(query, parameters)
        return self.conn.commit()
    
    def get_one(self, query, parameters = ()): #regresa un solo dato de la bd
        self.cursor.execute(query, parameters)
        row = self.cursor.fetchone() 
        return row
    
    def get_all(self , query, parameters = ()): #regresa una tupla o lista de tuplas desde la bd
        self.cursor.execute( query, parameters)
        rows = self.cursor.fetchall()
        return rows    