def KFC(x):
    if x == 3:  # 재귀의 depth/level
        return
    for i in range(4):  # 경우의 수
        KFC(x + 1)


KFC(0)