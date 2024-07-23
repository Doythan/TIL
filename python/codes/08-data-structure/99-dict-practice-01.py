# 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']


# 1. [] 표기법을 사용한 방법
def count_blood_types(blood_types):
    btc = {}
    for blood_type in blood_types:
        if blood_type in btc:
            btc[blood_type] += 1
        else:
            btc[blood_type] = 1
    return btc

print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# 2. get() 메서드를 사용한 방법
def count_blood_types(blood_types):
    btc = {}
    for blood_type in blood_types:
        btc[blood_type] = btc.get(blood_type, 0) + 1
    return btc
    


print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


