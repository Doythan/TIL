import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
ni = 0
nj = 0
temp, ans = 0, 0
for tc in range(1, T+1):
    ni, nj, temp, ans = 0, 0, 0, 0
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n:
                    temp = a[ni][nj] - a[i][j]
                    if temp >= 0:
                        ans += temp
                    else:
                        ans += temp * -1
    print(f'#{tc}', ans)

