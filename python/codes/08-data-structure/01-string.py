# find
text = 'banana'
print(text.find('a')) # 첫번째 a의 위치 반환
print(text.find('q')) # 찾는게 없으면 반환값이 -1

# index
print(text.index('a')) # find와 동일하나, 
# print(text.index('q')) # 찾는게 없으면 에러

# isupper, islower
string = 'Hello'
string2 = 'HELLO'
string3 = 'hello'
print(string.isupper()) # 전체가 다 대문자이면 True
print(string2.isupper())
print(string3.isupper())
print(string3.islower()) # 전체가 다 소문자이면 True 

# isalpha
string1 = 'Hello'
string2 = '123heis'
print(string1.isalpha()) # 문자열이 알파벳으로만 이루어져 있는지 확인 # True
print(string2.isalpha()) # False

# replace, 원본을 바꾸는 것은 아니고 반환함, 새로운 변수에 할당해야함 (str 불변이므로) 
text = 'Hello, world! world world'
new_text = text.replace('world', 'python', 2) # 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
print(new_text)

# strip 문자열의 시작과 끝에 있는 공백 혹은 지정한 문자를 제거
text = '  Hello, world!  '
new_text = text.strip()
print(new_text) # 'Hello, world!'

# split 지정한 문자를 구분자로 문자열을 분리하여 문자열의 리스트로 반환 
text = 'Hello, world!'
words = text.split(',')
print(words)

# join
words = ['Hello', 'world!']
text = ' '.join(words)
print(text)

# capitalize
text = 'heLLo, woRld!'
new_text = text.capitalize() 
print(new_text) #Hello world! 첫 문자를 대문자로 변환하고 나머지 문자는 소문자로 변환

# title
new_text2 = text.title()
print(new_text2)
# upper , 다 대문자로 변환
# lower , 다 소문자로 변환 
# swapcase, 소는 대로 대는 소문자로 변환
new_text3 = text.swapcase()
print(new_text3)


# 참고
# isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
print("isdecimal() 메서드 예시:")
print("'12345'.isdecimal():", '12345'.isdecimal())
print("'123.45'.isdecimal():", '123.45'.isdecimal())
print("'-123'.isdecimal():", '-123'.isdecimal())
print("'Ⅳ'.isdecimal():", 'Ⅳ'.isdecimal())
print("'½'.isdecimal():", '½'.isdecimal())
print("'²'.isdecimal():", '²'.isdecimal())
print()

# isdigit() : 일반 숫자뿐만 아니라 지수 표현(²)도 True로 인식
print("isdigit() 메서드 예시:")
print("'12345'.isdigit():", '12345'.isdigit())
print("'123.45'.isdigit():", '123.45'.isdigit())
print("'-123'.isdigit():", '-123'.isdigit())
print("'Ⅳ'.isdigit():", 'Ⅳ'.isdigit())
print("'½'.isdigit():", '½'.isdigit())
print("'²'.isdigit():", '²'.isdigit())
print()

# isnumeric() : 일반 숫자, 로마 숫자, 분수, 지수 등 다양한 형태의 숫자 표현을 True로 인식
print("isnumeric() 메서드 예시:")
print("'12345'.isnumeric():", '12345'.isnumeric())
print("'123.45'.isnumeric():", '123.45'.isnumeric())
print("'-123'.isnumeric():", '-123'.isnumeric())
print("'Ⅳ'.isnumeric():", 'Ⅳ'.isnumeric())
print("'½'.isnumeric():", '½'.isnumeric())
print("'²'.isnumeric():", '²'.isnumeric())
