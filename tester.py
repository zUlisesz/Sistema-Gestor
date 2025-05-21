from repositories.studentCouse_repository import StudentCourseRepository

stdc = StudentCourseRepository()

names = stdc.get_my_courses(13)
print(names)