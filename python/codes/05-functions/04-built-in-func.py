# 내장 함수(기본적으로 제공하는 함수)
numbers = [1, 2, 3, 4, 5]

print(len(numbers))  # 5
print(max(numbers))  # 5
print(min(numbers))  # 1
print(sum(numbers))  # 15
print(sorted(numbers, reverse=True))  # [5, 4, 3, 2, 1]
print(sorted(numbers))

# map, map(function, iterable) iterable : 요소임 요소는 반복 가능한 객체 컬렉션 map은 요소 하나하나에  function(함수)을 줌
# map, function에 내가 만든 함수도 넣을 수 있음 따라서 map은 확장성이 굉장히 큼 
numbers = [1, 2, 3]
result = map(str, numbers)
print(result)  # <map object at 0x00000239C915D760>
print(list(result))  # ['1', '2', '3']

#split은 메서드 리스트로 만들어준다. 
numbers1 = input().split()
print(numbers1)  # ['1', '2', '3']
#map을 이용, map(int, ~) 요소들을 정수형으로 다 바꿔줌 
numbers2 = list(map(int, input().split()))
print(numbers2)  # [1, 2, 3]


# zip(*iterables), 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)
print(pair)  # <zip object at 0x000001C76DE58700>
print(list(pair))  # [('jane', 'peter'), ('ashley', 'jay')]

kr_scores = [10, 20, 30, 50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]

for student_scores in zip(kr_scores, math_scores, en_scores):
    print(student_scores)


scores = [
    [10, 20, 30],
    [40, 50, 39],
    [20, 40, 50],
]
for score in zip(*scores):
    print(score)
