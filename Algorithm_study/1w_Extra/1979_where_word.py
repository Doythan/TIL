import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    a = [[0] * (n+2)]
    a += [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
    a += [[0] * (n+2)]
    print(a)
    cnt = 0
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if a[i][j] == 1 and cnt != k:
                cnt += 1
            elif a[i][j] == 0:
                cnt = 0
            if cnt == k and a[i][j+1] != 1:
                cnt = 0
                ans += 1
    for j in range(1, n+1):
        for i in range(1, n+1):
            if a[i][j] == 1:
                cnt += 1
            elif a[i][j] == 0:
                cnt = 0
            if cnt == k and a[i+1][j] != 1:
                cnt = 0
                ans += 1
    print(ans)

