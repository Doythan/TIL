from .base import Person

class Teacher(Person):
    def teach(self):
        print("수업합니다.")

    def __str__(self):
        # str 매직메서드의 반환값은 
        # print 함수로 호출했을때 출력할 값 
        return self.name
    
    def __repr__(self):
        return self.name 

