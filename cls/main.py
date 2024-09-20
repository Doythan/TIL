# conf 패키지에 있는 2개의 클래스 모두 가져오기 
from conf.students import Student
from conf.teacher import Teacher

s1 = Student('학생', 27)
t1 = Teacher('선생', 30) 

t1.teach()
t1.eat() 

class Course:
    def __init__(self):
        self.students = []
        self.teacher = None

c1 = Course()
print(c1.students, c1.teacher) 

s1 = Student('학생', 27)
t1 = Teacher('선생', 30) 

c1.teacher = t1
print(c1.students, c1.teacher)  # [] None 

c1.teacher.eat()
c1.teacher.teach()
print(c1.teacher.name)