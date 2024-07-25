# 클래스 정의
class Person:
    blood_color = 'red' # 속성 (blood_color를 변수라 안하고 class 변수 or 속성이라고 함) 

    def __init__(self, name): # 인스턴스 메서드 
        self.name = name

    def singing(self):
        return f'{self.name}이 노래합니다.'

# 인스턴스 생성
singer1 = Person('iu')

# (인스턴스) 메서드 호출
print(singer1.singing())

# 클래스 속성(변수) 접근
print(singer1.blood_color)

# 인스턴스 속성(변수) 
print(singer1.name)

