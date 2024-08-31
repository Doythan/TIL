# 구간합 문제

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    min_v = float('inf')
    max_v = float('-inf')
    temp = 0

    for i in range(N-M+1):
        for j in range(i, i+M):
            temp += arr[j]

        if temp >= max_v:
            max_v = temp
        if temp <= min_v:
            min_v = temp
        temp = 0

    print(f'#{tc}', max_v-min_v)
