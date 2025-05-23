from controllers.course_controller import CourseController

cc = CourseController()

rows = cc.get_students_of(1)

for element in rows:
    print(element)
    
