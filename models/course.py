class Course:
    def __init__(self, id, name, description, limit, career):
        self.id_course = id
        self.name = name
        self.description = description
        self.limit = limit 
        self.career = career
        self.students = []
        self.teacher = None 
        
    def show_myself(self) -> str:
        return f'id: {self.id_course} - {self.name} -limit: {self.limit} - career: {self.career} - teacher: {self.teacher}'
    
    def add_student(self, student) -> None:
        self.students.append(student)
        print('student added successfuly')
        
    def add_teacher(self, teacher) -> None :
        self.teacher = teacher
        print('teacher added successfuly')


