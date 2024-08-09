# 동일한 숫자가 포함되지 않았을 때, 각 자리 수 별로 loop을 이용해 구현

for i in range(1, 4):
    for j in range(1, 4):
        if i != j:
            for k in range(1, 4):
                if k != i and k != j:
                    print(i, j, k)
