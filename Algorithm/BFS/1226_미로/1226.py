from collections import deque
# import sys
# sys.stdin = open("input.txt", "r")


def bfs(si, sj):
    q = deque([])
    v = [[0] * 100 for _ in range(100)]
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

    q.append([si, sj])
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        if arr[ci][cj] == 3:
            return 1

        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]

            if 0 <= ni < 100 and 0 <= nj < 100 and (arr[ni][nj] == 0 or arr[ni][nj] == 3) and v[ni][nj] == 0:
                q.append([ni, nj])
                v[ni][nj] = 1
    return 0


for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input())) for _ in range(100)]

    print(f'#{tc}', bfs(1, 1))



