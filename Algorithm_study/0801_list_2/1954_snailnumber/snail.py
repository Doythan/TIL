import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(T):
    N = int(input())
    a = 0
    b = N - 1
    cnt = N + 1
    # matrix = []
    # for _ in range(N):
    #     matrix += [[0] * N]
    matrix = [[0] * N for _ in range(N)]
    for i in range(N):
        matrix[0][i] = i + 1
    for i in range(1, N):  # N번 반복
        if i % 2 == 1:  # 아래, 왼쪽 이동
            for j in range(N - i):
                a = a + 1
                matrix[a][b] = cnt
                cnt += 1
            for j in range(N - i):
                b = b - 1
                matrix[a][b] = cnt
                cnt += 1
        elif i % 2 == 0:
            for j in range(N - i):
                a = a - 1
                matrix[a][b] = cnt
                cnt += 1
            for j in range(N - i):
                b = b + 1
                matrix[a][b] = cnt
                cnt += 1
    print(f'#{t+1}')
    for i in matrix:
        print(*i)