from .user import User

class Teacher(User):
    
    def __init__(self, id, name, mail, password):
        super().__init__(id, name, mail, password)
        self.courses = []
        
    #correct the method
    def give_task_back(self):
        print('giving the task back')
        
    def show_currentCourses(self):
        return [str(element) for element in self.courses]
    
    