from .user import User

class Admin(User):
    def __init__(self,id,  name, mail, password):
        super().__init__(id, name, mail, password)
        
    def create_course(self, name, limit, career):
        print(f'New course: {name} - {limit} - {career}')
        
    def delete_course(sefl, name):
        print(f'deleting {name}')
        
    def send_notice(self, notice):
        print(f'notice: {notice}')