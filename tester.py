from controllers.admin_controller import AdminController

adm = AdminController()

teacher_name = adm.get_courses_teacher(1)
print(teacher_name)