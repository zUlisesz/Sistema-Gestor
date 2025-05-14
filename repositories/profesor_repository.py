from .base import BaseRepository
from models.profesor import Teacher

class TeacherRepository(BaseRepository):

    def existing_teacher(self, mail):
        query = 'SELECT * FROM teachers WHERE mail = %s'
        row = self.get_one(query, (mail,))
        return row[0] if row else None
        
    def get_byMail(self, mail) ->Teacher: # 1 
        query = 'SELECT * FROM teachers WHERE mail = %s'
        row = self.get_one(query, (mail))
        if row:
            return Teacher(*row)
        
    def get_teachers(self) -> list: # >= 1
        query = 'SELECT * FROM teachers'
        rows = self.get_all(query,())
        return [Teacher(*row) for row in rows]
        
    