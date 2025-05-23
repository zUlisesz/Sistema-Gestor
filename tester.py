from controllers.teacher_controller import TeacherController

tc = TeacherController()

courses = tc.get_my_courses(19)

for element in courses:
    print(element)
    
