# 암시적 형변환(가능한 코드를 이렇게 안짜는게 좋음)
print(3 + 5.0) # 8.0, 정수와 실수의 연산에서 정수가 실수로 변환됨
print(True + 3) # 4, Boolean과 Numeric Type에서만 가능
print(True + False) # 1, 1+0으로 계산함

# 명시적 형변환, 프로그래머가 직접 지정하는 형변화

# str -> int : 형식에 맞는 숫자만 가능
print(int('1')) # 1
print(int('3.5')) # float로 해야함 
print(int(3.5)) # 3, 소수점을 버림
print(float('3.5')) # 3.5
# int -> str : 모두 가능
print(str(1) + '등') #1등
