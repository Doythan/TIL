class Person:
    def __init__(self, name):
        
        # 왼쪽 name : 인스턴스 변수 name
        # 오른쪽 name : 생성자 메서드의 매개변수 이름
        self.name = name
        print('인스턴스가 생성되었습니다.')

    def greeting(self):
        print(f'안녕하세요. {self.name}입니다.')

person1 = Person('지민') # 인스턴스가 생성되었습니다.
person1.greeting() # 데이터 중심 단축형 코드 (우리가 쓰는거)
# Person.greeting(person1) # 절차지향방식 
