fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f' 인덱스: {index} {fruit}')

for index, fruit in enumerate(fruits, 3):
    print(index, fruit)