import sys
sys.stdin = open("input.txt", "r")

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    temp, ans = 0, 0
    for i in range(n):
        for j in range(m):
            temp = a[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    temp += a[ni][nj]
            if temp > ans:
                ans = temp
    print(f'#{tc}', ans)

