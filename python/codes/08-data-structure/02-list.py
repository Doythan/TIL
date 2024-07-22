# 리스트는 가변적이기 때문에 원본자체를 조작할 수 있음 
# append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list) # [1, 2, 3, 4]
my_list.append([5,6])
print(my_list) # [1, 2, 3, 4, [5, 6]]
print(my_list.append(4)) # None (원본을 바꾸기 때문에 반환이 없다. 헷갈리면 안됨) 

# extend
my_list = [1, 2, 3]
my_list.extend([4,5,6])
print(my_list) # [1, 2, 3, 4, 5, 6]
# my_list.extend(5) error 남 iterable한 객체, 즉 반복 가능한 개체 정수같은거 안됨

# insert
my_list = [1, 2, 3]
my_list.insert(1, [5, 3])
print(my_list) # [1, [5, 3], 2, 3]


# remove
my_list = [1, [2, 3], 2, [2 ,3], 2]
my_list.remove([2,3])
print(my_list) # [1, 2, [2, 3], 2]


# pop, 반환값 존재 
my_list = [1, 2, 3, 4, 5]

item1 = my_list.pop() 
item2 = my_list.pop(3)
print(item1) # 5
print(item2) # 4
print(my_list) # [1, 2, 3]


# clear
my_list = [1, 2, 3]
my_list.clear()
print(my_list) # []


# index
my_list = [1, [2, 3] , 3, 2, 1]
index = my_list.index([2,3]) 
print(index) # 1 


# count
my_list = [1, 3, 2, 2, 3, 3, 3]
count = my_list.count(3)
print(count) # 4


# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list) # [9, 1, 8, 2, 3, 1]
print(my_list.reverse()) # None, 원본을 바꾼거기 때문에 리턴값은 없다. 

# sort
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list) # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list) # [100, 3, 2, 1]

