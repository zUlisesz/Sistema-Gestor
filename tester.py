from controllers.teacher_controller import TeacherController

tc = TeacherController()

names = tc.get_my_courses_name(19)

ids = tc.get_my_courses_id(19)

print(tc.get_my_info_courses(19))
    
