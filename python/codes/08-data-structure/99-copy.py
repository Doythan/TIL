# 할당
a = [1, 2, 3, 4]
b = a
b[0] = 100
print(a) # [100, 2, 3, 4]
print(b) # [100, 2, 3, 4]


a = 20 
b = a
b = 10 
print(a, b) # 20 10

# 얕은 복사
a = [1,2,3]
b = a[:]
c = a.copy()
print(a, b, c) # [1, 2, 3] [1, 2, 3] [1, 2, 3]
b[0] = 100
c[0] = 200
print(a, b, c) # [1, 2, 3] [100, 2, 3] [200, 2, 3]

# 얕은 복사의 한계 : 중첩된 상황에서는 복사가 안됨 
a = [1, 2, [3, 4, 5]]
b = a.copy()
print(a, b) # [1, 2, [3, 4, 5]] [1, 2, [3, 4, 5]]
b[0] = 999
b[2][1] = 100
print(a, b) # [1, 2, [3, 100, 5]] [999, 2, [3, 100, 5]]


# 깊은 복사
import copy 

original_list = [1, 2, [3, 4, 5]]
deep_copied_list = copy.deepcopy(original_list)
print(original_list, deep_copied_list) # [1, 2, [3, 4, 5]] [1, 2, [3, 4, 5]]
deep_copied_list[2][1] = 1000
print(original_list, deep_copied_list) # [1, 2, [3, 4, 5]] [1, 2, [3, 1000, 5]]