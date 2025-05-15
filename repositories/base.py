from services.database import connect_db

class BaseRepository:
    
    def __init__(self):
        self.conn = connect_db() 
        self.cursor = self.conn.cursor()
        
    def execute(self , query , parameters = ()):
        self.cursor.execute(query, parameters)
        return self.conn.commit()
    
    def get_one(self, query, parameters = ()):
        self.cursor.execute(query, parameters)
        row = self.cursor.fetchone() 
        return row
    
    def get_all(self , query, parameters = ()):
        self.cursor.execute( query, parameters)
        rows = self.cursor.fetchall()
        return rows    