from .user import User

class Student(User):
    
    def __init__(self, id, name, mail, password, career, average:None ):
        super().__init__(id, name, mail, password)
        self.career = career
        self.average = average
        self.courses = []
        

    def show_myself(self):
        return super().show_myself() + f' - average: {self.average} - career: {self.career}'
    
    def show_currentCourses(self):
        return [str(element) for element in self.courses]
    
    #complete these methods, they´re not completed
    def send_task(self):
        print('Sending my homework')
        
    def quit_course(self):
        print('leaving the course')
        
    def get_into_course(self):
        print('Entering into the course')
              