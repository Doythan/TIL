# add
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.add(4)
print(my_set) # {1, 2, 3, 'c', 'b', 4, 'a'} (순서는 의미가 없다)
my_set.add(4)
print(my_set) # {1, 2, 3, 4, 'c', 'a', 'b'} (순서가 의미가 없다)

# clear
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.clear()
print(my_set) # set()

# remove (세트에서 특정 항목 x를 제거)
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set) # {1, 3, 'a', 'c', 'b'}
# my_set.remove(10)
# print(my_set) # KeyError

# pop (세트에서 임의의 요소를 제거하고 반환 )
my_set = {'a', 'b', 'c', 1, 2, 3}
element = my_set.pop()
print(element) # 1
print(my_set) # {2, 3, 'a', 'c', 'b'}


# discard
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.discard(2)
print(my_set) # {1, 3, 'c', 'a', 'b'}
my_set.discard(10)
print(my_set) # {1, 3, 'c', 'a', 'b'}

# update
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1, 4, 5])  
print(my_set) # {1, 2, 3, 4, 5, 'c', 'a', 'b'}

# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2)) # {0, 2, 4} (set1 - set2)
print(set1.intersection(set2)) # {1, 3} (set1 & set2)
print(set1.issubset(set2)) # False (set1 <= set2)
print(set3.issubset(set1)) # True (set3 <= set1)
print(set1.issuperset(set2)) # False (set1 >= set2)
print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9} (set1 | set2)

