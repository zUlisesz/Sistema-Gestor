from .usuario import User

class Student(User):
    
    def __init__(self, name, mail, password, career):
        super().__init__(name, mail, password)
        self.average = 0  #gotta change this value later
        self.courses = []
        self.career  = career

    def show_myself(self):
        return super().show_myself() + f' - average: {self.average} - career: {self.career}'
    
    
    #complete these methods, they´re not completed
    def send_task(self):
        print('Sending my homework')
        
    def quit_course(self):
        print('leaving the course')
        
    def get_into_course(self):
        print('Entering into the course')
              