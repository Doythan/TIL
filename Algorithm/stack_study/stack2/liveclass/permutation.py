# 단순하게 순열 생성
# 집합 {1, 2, 3}에서 모든 순열 생성하기


for i1 in range(1,4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)


# 백트래킹을 이용하여 {1, 2, 3, ..., NMAX}에 대한 순열

