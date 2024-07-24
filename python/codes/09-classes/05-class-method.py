class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod # 데코레이트 붙는 순간 기능이 달라짐 
    def number_of_population(cls): 
        print(f'인구수는 {cls.count}입니다.')
        # print(f'인구수는 {Person.count}입니다.') # 반쪽짜리 정답, 하위클래스 상속이라는 개념 때문에


person1 = Person('iu')
person2 = Person('BTS')

Person.number_of_population() 