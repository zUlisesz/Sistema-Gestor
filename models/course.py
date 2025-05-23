class Course:
    def __init__(self, id, name, description, space, career):
        self.id_course = id
        self.name = name
        self.description = description
        self.space = space 
        self.career = career
        
    def show_myself(self) -> str:
        return f'id: {self.id_course} - {self.name} -limit: {self.space} - career: {self.career} - teacher: {self.teacher}'
    
        
    def add_teacher(self, teacher) -> None :
        self.teacher = teacher
        print('teacher added successfuly')


