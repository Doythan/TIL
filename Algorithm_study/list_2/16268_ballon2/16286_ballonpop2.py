import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    my_list = []
    ans = 0
    for x in range(n):
        for y in range(m):
            sum_v = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    sum_v += arr[nx][ny]
            sum_v += arr[x][y]
            if ans < sum_v:
                ans = sum_v
    print(f'#{tc}', ans)




