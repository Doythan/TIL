# 딕셔너리를 입력받아 value와 key를 뒤집은 결과를 반환하는 함수 `dict_invert()`를 작성하기





# 1. [] 표기법을 사용한 방법
def dict_invert(input_dict):
    inverted_dict = {}
    for key, value in input_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    return inverted_dict
# print(dict_invert({1: 10, 2: 20, 3: 30}))
# print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30})) 
# print(dict_invert({1: True, 2: True, 3: True}))


# 2. get 메서드를 사용한 방법
def dict_invert(input_dict):
    inverted_dict = {}
    for key, value in input_dict.items():
        inverted_dict[value] = inverted_dict.get(value, [])
        inverted_dict[value].append(key)
    return inverted_dict
 
# print(dict_invert({1: 10, 2: 20, 3: 30}))
# print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30})) 
# print(dict_invert({1: True, 2: True, 3: True}))


# 3. setdefault 메서드를 사용한 방법
def dict_invert(input_dict):
    inverted_dict = {}
    for key, value in input_dict.items():
        inverted_dict[value] = inverted_dict.setdefault(value, [])
        inverted_dict[value].append(key)
    return inverted_dict

print(dict_invert({1: 10, 2: 20, 3: 30}))
print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30})) 
print(dict_invert({1: True, 2: True, 3: True}))


