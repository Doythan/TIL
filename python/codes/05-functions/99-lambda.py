# Lambda expressions 람다 표현식 : 익명 함수를 만드는 데 사용되는 표현식 -> 한 줄로 간단한 함수를 정의 
def addition(x, y):
    return x + y


result = addition(3, 5)
print(result)  # 8


# lambda 표현식으로 작성한 addition 함수
addition = lambda x, y: x + y
result = addition(3, 5)
print(result)


# with map 함수
numbers = [1, 2, 3, 4, 5]


def square(x):
    return x**2


# lambda 미사용
squared1 = list(map(square, numbers))
print(squared1)  # [1, 4, 9, 16, 25]

# lambda 사용
square2 = list(map(lambda x: x**2, numbers))
print(square2)