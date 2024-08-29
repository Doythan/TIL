# 10진수로 형변환
print(int('10'))

# 2진수로 변환
print(bin(10))  # 주의. 문자열
# 0b1010 -> 0b 라는 문자열로 2진수를 나타냈음을 표기
print(oct(10))  # 8진수로 변환
print(hex(10))  # 16진수로 변환

# 16 -> 10진법
print(int('F', base=16))
print(int('1010', base=2))  # 2 -> 10진법

print(bin(8)[2:])  # 4bit로 표기 -> 전처리
print(bin(1)[2:].zfill(4))

for i in range(16):
    print(bin(i)[2:].zfill(4))




