from repositories.user_repository import UserRepository
class TeacherController:
    def __init__(self):
        self.user_repo = UserRepository()
        
    def create_teacher(self, mail):
        return self.user_repo.get_teacher_byMail(mail)
    
    