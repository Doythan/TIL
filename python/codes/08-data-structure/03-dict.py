# clear
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person) # {}

# get
person = {'name': 'Alice', 'age': 25}
print(person.get('name')) # Alice
print(person['name']) # Alice
print(person.get('country')) # None
print(person.get('country', 'Unknown')) # Unknown (기본적으로는 None 출력되지만, 기본 값 반환 가능)
# print(person['country']) # keyError: 'country'

# keys
person = {'name': 'Alice', 'age': 25}
print(person.keys()) # dict_keys(['name', 'age']) (리스트랑 비슷하네 그러면 반복을 진행해볼까 ? 라는 사고를 가져야 함)
for k in person.keys():
    print(k) # name
             # age

# values
person = {'name': 'Alice', 'age': 25}
print(person.values()) # dict_keys(['name', 'age'])
for v in person.values():
    print(v) # Alice
             # 25

# items
person = {'name': 'Alice', 'age': 25}
print(person.items()) # dict_items([('name', 'Alice'), ('age', 25)])
for k, v in person.items(): # 변수 두 개 사용하여 한번에 언팩킹 가능 
    print(k, v) # name Alice
                # age 25

# pop (키를 제거하고 연결됐던 값을 반환(없으면 에러나 default를 반환) 
person = {'name': 'Alice', 'age': 25}
print(person.pop('age')) # 25
print(person) # {'name' : 'Alice'}
print(person.pop('country', None))
# print(person.pop('country')) # Key Error

# setdefault (키와 연결된 값을 반환 키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환)
person = {'name': 'Alice', 'age': 25}
print(person.setdefault('name')) # Alice
print(person.setdefault('country', 'KOREA')) # KOREA
print(person) # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}

# update (other가 제공하는 키/값 쌍으로 딕셔너리르 갱신 기존 키는 덮어 씀)
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}

person.update(other_person)
print(person) # {'name': 'Jane', 'age': 25, 'gender': 'Female'}
person.update(age = 50, country = 'KOREA')
print(person) # 'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'KOREA'}
