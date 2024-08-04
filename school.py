class student :
    def __init__(self,name,age,id) :
        self.name=name
        self.age=age
        self.id=id
class course:
    def __init__(self,name,teacher) :
        self.name=name
        self.teacher=teacher
class teacher :
    def __init__(self,name,course) :
        self.name=name
        self.course=course

class school :
    def __init__(self,name,students,teachers,courses) :
        self.name=name
        self.students=students
        self.teachers=teachers
        self.courses=courses
    def get_student(self) :
        for student in students :
            print(student.name)    

    def get_student_id(self) :
        for student in students :
            print(student.id)        

school_name='phitron'
ds_course=course('data stracture','abul')
algo_course=course('algorithm','babul')
teacher_1=teacher('abul',ds_course)
teacher_2=teacher('babul',ds_course)
student_1=student('akib',17,50)
student_2=student('rakib',18,60)
student_3=student('shakib',24,55)



teachers=[teacher_1,teacher_2]
courses=[ds_course,algo_course]
students=[student_1,student_2,student_3]
my_school=school(school_name,students,teachers,courses)
print(my_school.students)
my_school.get_student()
my_school.get_student_id()



        

