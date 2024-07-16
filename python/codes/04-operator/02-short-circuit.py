# 단축 평가

vowels = 'aeiou'

print(('a' and 'b') in vowels)  # False
print(('b' and 'a') in vowels)  # True

print(3 and 5)  # 5
print(3 and 0)  # 0
print(0 and 3)  # 0, 앞에 0 뒤에 안 봄(단축평가)
print(0 and 0)  # 0, 앞에 0 뒤에 안 좀(단축평가)

print(5 or 3)  # 5, 5 True 뒤에 안 봄(단축평가)
print(3 or 0)  # 3, 3 True 뒤에 안 봄(단축평가)
print(0 or 3)  # 3, 0 False 3봄
print(0 or 0)  # 0, 뒤에 0
